# LLaVA-OneVision-Qwen2-0.5B-OV

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/LLaVA-OneVision-Qwen2-0.5B-OV.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 8
- `vllm serve` snippets: 1
- API or client verification snippets: 3

## Snippets

### 1. LLaVA-OneVision-Qwen2-0.5B-OV > Environment Preparation > Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1
docker run --rm \
    --name vllm-ascend \
    --shm-size=1g \
    --net=host \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /root/.cache:/root/.cache \
    -it $IMAGE bash
```

### 2. LLaVA-OneVision-Qwen2-0.5B-OV > Deployment > Single-node Deployment > Single NPU

```bash
export MODEL_PATH="llava-hf/llava-onevision-qwen2-0.5b-ov-hf"

vllm serve "${MODEL_PATH}" \
    --host 0.0.0.0 \
    --port 8000 \
    --served-model-name LLaVA-OneVision-0.5B \
    --trust-remote-code \
    --gpu-memory-utilization 0.8
```

### 3. LLaVA-OneVision-Qwen2-0.5B-OV > Functional Verification

```bash
INFO:     Started server process [8173]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 4. LLaVA-OneVision-Qwen2-0.5B-OV > Functional Verification

```bash
curl http://127.0.0.1:8000/v1/models
```

### 5. LLaVA-OneVision-Qwen2-0.5B-OV > Functional Verification > Text-only Request

```bash
curl http://127.0.0.1:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "LLaVA-OneVision-0.5B",
        "messages": [
            {
                "role": "user",
                "content": "Say hello in one short sentence."
            }
        ],
        "max_completion_tokens": 16,
        "temperature": 0
    }'
```

### 6. LLaVA-OneVision-Qwen2-0.5B-OV > Functional Verification > Text-only Request

```json
{"choices":[{"message":{"content":"Hello! How can I assist you today?"}}]}
```

### 7. LLaVA-OneVision-Qwen2-0.5B-OV > Functional Verification > Image Understanding Request

```bash
curl http://127.0.0.1:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "LLaVA-OneVision-0.5B",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe this image briefly."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://modelscope.oss-cn-beijing.aliyuncs.com/resource/qwen.png"
                        }
                    }
                ]
            }
        ],
        "max_completion_tokens": 64,
        "temperature": 0
    }'
```

### 8. LLaVA-OneVision-Qwen2-0.5B-OV > Functional Verification > Image Understanding Request

```json
{"choices":[{"message":{"content":"The image features a logo consisting of a stylized geometric figure and the text \"TONGYI\" and \"Qwen\"..."}}]}
```
