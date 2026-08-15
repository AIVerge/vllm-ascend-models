# Qwen3-Reranker

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3-Reranker.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 7
- `vllm serve` snippets: 2
- API or client verification snippets: 1

## Snippets

### 1. Qwen3-Reranker > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-a3
docker run --rm \
    --name vllm-ascend \
    --shm-size=1g \
    --net=host \
    --privileged=true \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /root/.cache:/root/.cache \
    -it $IMAGE bash
```

### 2. Qwen3-Reranker > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1
docker run --rm \
    --name vllm-ascend \
    --shm-size=1g \
    --net=host \
    --privileged=true \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /root/.cache:/root/.cache \
    -it $IMAGE bash
```

### 3. Qwen3-Reranker > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-310p
docker run --rm \
    --name vllm-ascend \
    --shm-size=1g \
    --net=host \
    --privileged=true \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /root/.cache:/root/.cache \
    -it $IMAGE bash
```

### 4. Qwen3-Reranker > 5 Online Service Deployment

```bash
#!/bin/sh
vllm serve Qwen/Qwen3-Reranker-0.6B \
    --served-model-name Qwen/Qwen3-Reranker-0.6B \
    --runner pooling \
    --hf_overrides '{"architectures": ["Qwen3ForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' \
    --port 8000 \
    --max-model-len 1024
```

### 5. Qwen3-Reranker > 5 Online Service Deployment

```bash
#!/bin/sh
vllm serve Qwen/Qwen3-Reranker-0.6B \
    --served-model-name Qwen/Qwen3-Reranker-0.6B \
    --runner pooling \
    --hf_overrides '{"architectures": ["Qwen3ForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' \
    --compilation-config '{"cudagraph_capture_sizes": [1024,512]}' \
    --additional-config '{"ascend_compilation_config": {"fuse_norm_quant": false}}' \
    --dtype float16 \
    --port 8000 \
    --max-model-len 1024
```

### 6. Qwen3-Reranker > 6 Functional Verification

```python
import requests

url = "http://127.0.0.1:8000/v1/rerank"

# Please use the query_template and document_template to format the query and
# document for better reranker results.

prefix = '<|im_start|>system\nJudge whether the Document meets the requirements based on the Query and the Instruct provided. Note that the answer can only be "yes" or "no".<|im_end|>\n<|im_start|>user\n'
suffix = "<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n\n"

query_template = "{prefix}<Instruct>: {instruction}\n<Query>: {query}\n"
document_template = "<Document>: {doc}{suffix}"

instruction = (
    "Given a web search query, retrieve relevant passages that answer the query"
)

query = "What is the capital of China?"

documents = [
    "The capital of China is Beijing.",
    "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun.",
]

documents = [
    document_template.format(doc=doc, suffix=suffix) for doc in documents
]

response = requests.post(url,
                         json={
                             "query": query_template.format(prefix=prefix, instruction=instruction, query=query),
                             "documents": documents,
                         }).json()

print(response)
```

### 7. Qwen3-Reranker > 6 Functional Verification

```json
{
    "id": "score-xxx",
    "model": "Qwen/Qwen3-Reranker-0.6B",
    "usage": {
        "prompt_tokens": 193,
        "total_tokens": 193
    },
    "results": [
        {
            "index": 0,
            "document": {
                "text": "<Document>: The capital of China is Beijing.<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n\n",
                "multi_modal": null
            },
            "relevance_score": 0.9994981288909912
        },
        {
            "index": 1,
            "document": {
                "text": "<Document>: Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun.<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n\n",
                "multi_modal": null
            },
            "relevance_score": 0.00000506485957885161
        }
    ]
}
```
