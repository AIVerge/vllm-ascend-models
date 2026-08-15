#!/usr/bin/env python3
"""Generate vLLM Ascend model reference files from the official docs."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen


DEFAULT_SOURCE_URL = (
    "https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/"
    "DeepSeek-V4-Flash.html"
)
START_LABEL = "Model Tutorials"
END_LABEL = "Feature Tutorials"
USER_AGENT = "Mozilla/5.0 (Codex skill reference generator)"

INCLUDE_PATH_KEYWORDS = (
    "installation",
    "environment preparation",
    "deployment",
    "functional verification",
    "verify",
)
SKIP_PATH_KEYWORDS = (
    "accuracy evaluation",
    "performance evaluation",
    "performance tuning",
    "using aisbench",
    "using vllm benchmark",
    "known limitations",
    "faq",
)


@dataclass(frozen=True)
class ModelLink:
    name: str
    url: str
    filename: str


@dataclass(frozen=True)
class CodeBlock:
    path: str
    code: str


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str | None]] = []
        self._in_anchor = False
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        self._in_anchor = True
        self._href = dict(attrs).get("href")
        self._text = []

    def handle_data(self, data: str) -> None:
        if self._in_anchor:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != "a" or not self._in_anchor:
            return
        text = normalize_text("".join(self._text))
        self.links.append((text, self._href))
        self._in_anchor = False
        self._href = None
        self._text = []


class ArticleCodeParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.blocks: list[CodeBlock] = []
        self._article_depth = 0
        self._heading_level: int | None = None
        self._heading_text: list[str] = []
        self._path: list[tuple[int, str]] = []
        self._pre_depth = 0
        self._code_depth = 0
        self._code_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "article":
            self._article_depth += 1
        if not self._article_depth:
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._heading_level = int(tag[1])
            self._heading_text = []
        if tag == "pre":
            self._pre_depth += 1
        if tag == "code" and self._pre_depth:
            self._code_depth += 1
            self._code_text = []

    def handle_data(self, data: str) -> None:
        if not self._article_depth:
            return
        if self._heading_level is not None:
            self._heading_text.append(data)
        if self._code_depth:
            self._code_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if not self._article_depth:
            return
        if self._heading_level is not None and tag == f"h{self._heading_level}":
            heading = normalize_text("".join(self._heading_text).replace("¶", ""))
            if heading:
                level = self._heading_level
                self._path = [item for item in self._path if item[0] < level]
                self._path.append((level, heading))
            self._heading_level = None
            self._heading_text = []
        if tag == "code" and self._code_depth:
            code = unescape("".join(self._code_text).strip())
            if code:
                self.blocks.append(CodeBlock(path=self.current_path, code=code))
            self._code_depth -= 1
            self._code_text = []
        if tag == "pre" and self._pre_depth:
            self._pre_depth -= 1
        if tag == "article":
            self._article_depth -= 1

    @property
    def current_path(self) -> str:
        return " > ".join(text for _, text in self._path)


def normalize_text(text: str) -> str:
    return " ".join(text.split())


def slugify(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "-", value.strip()).strip("-").lower()
    return re.sub(r"-{2,}", "-", slug)


def fetch_html(url: str) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=45) as response:
            return response.read().decode("utf-8", "replace")
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RuntimeError(f"failed to fetch {url}: {exc}") from exc


def discover_models(source_url: str) -> list[ModelLink]:
    parser = LinkParser()
    parser.feed(fetch_html(source_url))

    models: list[ModelLink] = []
    seen: set[str] = set()
    in_model_section = False
    for text, href in parser.links:
        if text == START_LABEL:
            in_model_section = True
            continue
        if in_model_section and text == END_LABEL:
            break
        if not in_model_section or not text or not href or not href.endswith(".html"):
            continue
        if text in seen:
            continue
        seen.add(text)
        filename = f"{slugify(text)}.md"
        models.append(ModelLink(name=text, url=urljoin(source_url, href), filename=filename))

    if not models:
        raise RuntimeError("no model tutorial links found")
    return models


def parse_code_blocks(url: str) -> list[CodeBlock]:
    parser = ArticleCodeParser()
    parser.feed(fetch_html(url))
    return [block for block in parser.blocks if is_relevant(block)]


def is_relevant(block: CodeBlock) -> bool:
    path = block.path.lower()
    code = block.code.lower()
    if any(keyword in path for keyword in SKIP_PATH_KEYWORDS):
        return False
    if any(keyword in path for keyword in INCLUDE_PATH_KEYWORDS):
        return True
    return "vllm serve" in code or "/v1/" in code or "curl " in code


def code_language(code: str) -> str:
    first_line = code.strip().splitlines()[0] if code.strip() else ""
    if first_line.startswith(("import ", "from ", "def ", "class ")):
        return "python"
    if first_line.startswith(("{", "[")):
        return "json"
    return "bash"


def count_api_checks(blocks: list[CodeBlock]) -> int:
    needles = ("curl ", "/v1/", "OpenAI(", "chat.completions", "embeddings.create")
    return sum(any(needle in block.code for needle in needles) for block in blocks)


def write_model_reference(output_dir: Path, model: ModelLink, blocks: list[CodeBlock]) -> None:
    lines = [
        f"# {model.name}",
        "",
        f"Source: {model.url}",
        "",
        "Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.",
        "",
        "## Quick Facts",
        "",
        f"- Extracted snippets: {len(blocks)}",
        f"- `vllm serve` snippets: {sum('vllm serve' in block.code for block in blocks)}",
        f"- API or client verification snippets: {count_api_checks(blocks)}",
        "",
        "## Snippets",
        "",
    ]
    for index, block in enumerate(blocks, start=1):
        lines.extend(
            [
                f"### {index}. {block.path}",
                "",
                f"```{code_language(block.code)}",
                block.code,
                "```",
                "",
            ]
        )
    output_dir.joinpath(model.filename).write_text("\n".join(lines), encoding="utf-8")


def write_index(
    reference_dir: Path,
    source_url: str,
    models: list[ModelLink],
    counts: dict[str, tuple[int, int, int]],
) -> None:
    lines = [
        "# vLLM Ascend Model Reference Index",
        "",
        "This index maps official vLLM Ascend Model Tutorials to local reference files. The references contain extracted installation, deployment, special inference mode, and functional verification snippets.",
        "",
        f"Source seed URL: {source_url}",
        "",
        "| Model | Reference | Source | Snippets | vLLM serve | API checks |",
        "| --- | --- | --- | ---: | ---: | ---: |",
    ]
    for model in models:
        total, serve_count, api_count = counts[model.name]
        lines.append(
            f"| {model.name} | `references/models/{model.filename}` | {model.url} | {total} | {serve_count} | {api_count} |"
        )
    reference_dir.joinpath("model-index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate(source_url: str, reference_dir: Path) -> None:
    models_dir = reference_dir / "models"
    models_dir.mkdir(parents=True, exist_ok=True)

    models = discover_models(source_url)
    counts: dict[str, tuple[int, int, int]] = {}
    expected_files = {model.filename for model in models}
    for stale_file in models_dir.glob("*.md"):
        if stale_file.name not in expected_files:
            stale_file.unlink()

    for model in models:
        blocks = parse_code_blocks(model.url)
        if not blocks:
            raise RuntimeError(f"no relevant snippets extracted for {model.name}")
        serve_count = sum("vllm serve" in block.code for block in blocks)
        api_count = count_api_checks(blocks)
        counts[model.name] = (len(blocks), serve_count, api_count)
        write_model_reference(models_dir, model, blocks)

    write_index(reference_dir, source_url, models, counts)
    print(f"Generated {len(models)} model references in {reference_dir}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-url",
        default=DEFAULT_SOURCE_URL,
        help="Seed model tutorial URL used to discover the Model Tutorials sidebar.",
    )
    parser.add_argument(
        "--reference-dir",
        type=Path,
        default=Path("references"),
        help="Directory that will receive model-index.md and models/*.md.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    generate(args.source_url, args.reference_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
