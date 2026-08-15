---
name: vllm-ascend-models
description: Use when Codex needs to create, adapt, or troubleshoot vLLM Ascend model inference and deployment commands from the official Model Tutorials, including Qwen, DeepSeek, GLM, Kimi, MiniMax, multimodal, embedding, reranker, ASR, OCR, and other vLLM Ascend model pages. The skill provides per-model online deployment, offline inference where documented, and functional verification snippets for Ascend NPU environments.
---

# vLLM Ascend Models

## Overview

Use this skill to produce model-specific vLLM Ascend inference commands without rediscovering the official tutorial pages. The bundled references are generated from the vLLM Ascend Model Tutorials and preserve each model page's documented deployment and verification snippets.

## Workflow

1. Identify the requested model, model family, and inference mode:
   - Single-node online service.
   - Multi-node or PD separation deployment.
   - Offline inference or special deployment mode, when the model page documents one.
   - Embedding, reranker, multimodal, ASR, OCR, or chat completion verification.
2. Open `references/model-index.md` and match the user model name to the reference file. Use `rg -i "<model-or-alias>" references/model-index.md references/models` when the exact name is unclear.
3. Read only the matching file under `references/models/`. Do not load every model reference unless the user asks for a cross-model comparison.
4. Start from the documented `vllm serve` or offline inference snippet. Preserve model-specific flags such as tokenizer mode, reasoning parser, quantization, expert parallelism, speculative config, multimodal limits, task type, and served model name.
5. Replace only environment-specific values:
   - Local model path or weight cache path.
   - Host, port, node IPs, NIC names, and visible NPU device IDs.
   - Tensor parallel, data parallel, pipeline parallel, and local rank values when the user's hardware differs.
   - Docker image tag only when the user explicitly targets a different vLLM Ascend release.
6. Include the corresponding verification request from the same model reference. Use the documented endpoint shape (`/v1/chat/completions`, embeddings, rerank, OpenAI Python client, audio, image, or model-specific request) rather than forcing a generic chat-completions request.
7. If a requested flag or model variant is missing from the bundled references, check the official vLLM Ascend docs before inventing values.

## Guardrails

- Do not simplify away model-specific parser, quantization, speculative decoding, hybrid KV cache, or multimodal flags.
- Do not mix commands from different model pages unless the user explicitly asks for a hybrid deployment plan.
- Keep placeholders visible for values the operator must set, such as `your_model_path`, `<node_ip>`, `nic_name`, and `ASCEND_RT_VISIBLE_DEVICES`.
- When answering in Chinese, keep shell commands unchanged and explain substitutions around them.
- For production guidance, call out hardware topology assumptions and any multi-node networking variables that must be aligned across nodes.

## References

- `references/model-index.md`: Model list, source URLs, and generated reference filenames.
- `references/models/`: One Markdown file per model containing extracted inference, deployment, and verification snippets.
- `scripts/update_model_references.py`: Regenerate references from the official vLLM Ascend Model Tutorials without third-party Python dependencies.
