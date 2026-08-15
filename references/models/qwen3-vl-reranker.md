# Qwen3-VL-Reranker

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3-VL-Reranker.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 8
- `vllm serve` snippets: 2
- API or client verification snippets: 1

## Snippets

### 1. Qwen3-VL-Reranker > 4 Installation > 4.1 Docker Image Installation

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

### 2. Qwen3-VL-Reranker > 4 Installation > 4.1 Docker Image Installation

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

### 3. Qwen3-VL-Reranker > 4 Installation > 4.1 Docker Image Installation

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

### 4. Qwen3-VL-Reranker > 5 Online Service Deployment > 5.1 Chat Template

```bash
<|im_start|>system
Judge whether the Document meets the requirements based on the Query and the Instruct provided. Note that the answer can only be "yes" or "no".<|im_end|>
<|im_start|>user
<Instruct>: {{
    messages
    | selectattr("role", "eq", "system")
    | map(attribute="content")
    | first
    | default("Given a search query, retrieve relevant candidates that answer the query.")
}}<Query>:{{
    messages
    | selectattr("role", "eq", "query")
    | map(attribute="content")
    | first
}}
<Document>:{{
    messages
    | selectattr("role", "eq", "document")
    | map(attribute="content")
    | first
}}<|im_end|>
<|im_start|>assistant
```

### 5. Qwen3-VL-Reranker > 5 Online Service Deployment > 5.1 Chat Template

```bash
#!/bin/sh
vllm serve Qwen/Qwen3-VL-Reranker-2B \
    --served-model-name Qwen/Qwen3-VL-Reranker-2B \
    --runner pooling \
    --hf_overrides '{"architectures": ["Qwen3VLForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' \
    --chat-template ./qwen3_vl_reranker.jinja \
    --port 8000 \
    --max-model-len 1024
```

### 6. Qwen3-VL-Reranker > 5 Online Service Deployment > 5.1 Chat Template

```bash
#!/bin/sh
vllm serve Qwen/Qwen3-VL-Reranker-2B \
    --served-model-name Qwen/Qwen3-VL-Reranker-2B \
    --runner pooling \
    --hf_overrides '{"architectures": ["Qwen3VLForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' \
    --chat-template ./qwen3_vl_reranker.jinja \
    --compilation-config '{"cudagraph_capture_sizes": [1024,512]}' \
    --additional-config '{"ascend_compilation_config": {"fuse_norm_quant": false}}' \
    --dtype float16 \
    --port 8000 \
    --max-model-len 1024
```

### 7. Qwen3-VL-Reranker > 6 Functional Verification

```bash
curl  http://localhost:8000/v1/rerank \
    -X POST \
    -d '{"query":"What is the capital of China?", "documents": ["The capital of China is Beijing.", "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun."]}' \
    -H 'Content-Type: application/json'
```

### 8. Qwen3-VL-Reranker > 6 Functional Verification

```json
{
    "id": "score-xxxxx",
    "model": "Qwen/Qwen3-VL-Reranker-2B",
    "usage": {
        "prompt_tokens": 179,
        "total_tokens": 179
    },
    "results": [
        {
            "index": 0,
            "document": {
                "text": "The capital of China is Beijing.",
                "multi_modal": null
            },
            "relevance_score": 0.7209711670875549
        },
        {
            "index": 1,
            "document": {
                "text": "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun.",
                "multi_modal": null
            },
            "relevance_score": 0.18871910870075226
        }
    ]
}
```
