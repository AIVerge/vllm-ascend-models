# Qwen3-Next

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3-Next.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 9
- `vllm serve` snippets: 1
- API or client verification snippets: 1

## Snippets

### 1. Qwen3-Next > 4 Installation > 4.1 Docker Image Installation

```bash
#!/bin/sh
# Update the vllm-ascend image
# For Atlas A2 machines:
# export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1
# For Atlas A3 machines:
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-a3
docker run --rm \
--shm-size=1g \
--name vllm-ascend-qwen3 \
--device /dev/davinci0 \
--device /dev/davinci1 \
--device /dev/davinci2 \
--device /dev/davinci3 \
--device /dev/davinci4 \
--device /dev/davinci5 \
--device /dev/davinci6 \
--device /dev/davinci7 \
--device /dev/davinci8 \
--device /dev/davinci9 \
--device /dev/davinci10 \
--device /dev/davinci11 \
--device /dev/davinci12 \
--device /dev/davinci13 \
--device /dev/davinci14 \
--device /dev/davinci15 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-p 8000:8000 \
-it $IMAGE bash
```

### 2. Qwen3-Next > 4 Installation > 4.1 Docker Image Installation

```bash
pip show vllm vllm-ascend
```

### 3. Qwen3-Next > 4 Installation > 4.2 Source Code Installation

```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm
pip install -e .
```

### 4. Qwen3-Next > 4 Installation > 4.2 Source Code Installation

```bash
git clone https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
pip install -e .
```

### 5. Qwen3-Next > 4 Installation > 4.2 Source Code Installation

```bash
pip show vllm vllm-ascend
```

### 6. Qwen3-Next > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct --served-model-name qwen3_next --tensor-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.8 --max-num-batched-tokens 4096 --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}'
```

### 7. Qwen3-Next > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
INFO:     Started server process [2736]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 8. Qwen3-Next > 6 Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{
  "model": "qwen3_next",
  "messages": [
    {"role": "user", "content": "Who are you?"}
  ],
  "temperature": 0.6,
  "top_p": 0.95,
  "top_k": 20,
  "max_completion_tokens": 32
}'
```

### 9. Qwen3-Next > 6 Functional Verification

```json
{
    "id": "chatcmpl-9df13fd5e539af93",
    "object": "chat.completion",
    "created": 1780971952,
    "model": "qwen3_next",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "What do you know about me?\n\nHello! I am Qwen, a large-scale language model independently developed by the Tongyi Lab under Alibaba Group. I am...",
                "reasoning": "The user is asking for my thoughts on \"Who are you?\"...",
                "refusal": null,
                "annotations": null,
                "audio": null,
                "function_call": null
            },
            "logprobs": null,
            "finish_reason": "length",
            "stop_reason": null,
            "token_ids": null
        }
    ]
}
```
