# Qwen3-VL-Embedding

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3-VL-Embedding.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 7
- `vllm serve` snippets: 2
- API or client verification snippets: 1

## Snippets

### 1. Qwen3-VL-Embedding > 4 Installation > 4.1 Docker Image Installation

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

### 2. Qwen3-VL-Embedding > 4 Installation > 4.1 Docker Image Installation

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

### 3. Qwen3-VL-Embedding > 4 Installation > 4.1 Docker Image Installation

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

### 4. Qwen3-VL-Embedding > 5 Online Service Deployment

```bash
#!/bin/sh
vllm serve Qwen/Qwen3-VL-Embedding-2B  \
  --served-model-name Qwen/Qwen3-VL-Embedding-2B  \
  --runner pooling \
  --port 8000 \
  --max-model-len 1024
```

### 5. Qwen3-VL-Embedding > 5 Online Service Deployment

```bash
#!/bin/sh
vllm serve Qwen/Qwen3-VL-Embedding-2B  \
  --served-model-name Qwen/Qwen3-VL-Embedding-2B  \
  --compilation-config '{"cudagraph_capture_sizes": [1024,512]}' \
  --additional-config '{"ascend_compilation_config": {"fuse_norm_quant": false}}' \
  --runner pooling \
  --dtype float16 \
  --port 8000 \
  --max-model-len 1024
```

### 6. Qwen3-VL-Embedding > 6 Functional Verification

```bash
curl -X POST http://localhost:8000/v1/embeddings -H "Content-Type: application/json" -d '{
  "input": [
        "The capital of China is Beijing.",
        "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun."
    ]
}'
```

### 7. Qwen3-VL-Embedding > 6 Functional Verification

```json
{
  "id": "embd-8136155c01e8411d",
  "object": "list",
  "created": 1784538286,
  "model": "Qwen/Qwen3-VL-Embedding-2B",
  "data": [
    {
      "index": 0,
      "object": "embedding",
      "embedding": [
        -0.028474265709519386,
        -0.02678542211651802
      ]
    },
    {
      "index": 1,
      "object": "embedding",
      "embedding": [
        -0.016785264015197754,
        -0.003787524998188019
      ]
    }
  ],
  "usage": {
    "prompt_tokens": 39,
    "total_tokens": 39,
    "completion_tokens": 0,
    "prompt_tokens_details": null
  }
}
```
