# Hunyuan-A13B-Instruct

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Hunyuan-A13B-Instruct.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 5
- `vllm serve` snippets: 1
- API or client verification snippets: 1

## Snippets

### 1. Hunyuan-A13B-Instruct > Environment Preparation > Installation

```bash
# Update the vllm-ascend image
# For Atlas A2 machines:
# export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1
# For Atlas A3 machines:
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-a3
docker run --rm \
  --name vllm-ascend \
  --shm-size=1g \
  --device /dev/davinci0 \
  --device /dev/davinci1 \
  --device /dev/davinci2 \
  --device /dev/davinci3 \
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

### 2. Hunyuan-A13B-Instruct > Environment Preparation > Installation

```bash
# Install vLLM.
git clone --depth 1 --branch v0.22.1 https://github.com/vllm-project/vllm
cd vllm
VLLM_TARGET_DEVICE=empty pip install -e .
cd ..

# Install vLLM Ascend.
git clone --depth 1 --branch v0.22.1rc1 https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
git submodule update --init --recursive
pip install -e .
cd ..
```

### 3. Hunyuan-A13B-Instruct > Deployment > Single-node Deployment (4-NPU)

```bash
export HCCL_INTRA_ROCE_ENABLE=1
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3
export HF_HOME=/data
export MODEL_PATH="Hunyuan-A13B-Instruct"

vllm serve ${MODEL_PATH} \
    --trust-remote-code \
    --host 0.0.0.0 \
    --port 8000 \
    --served-model-name Hunyuan \
    --tensor-parallel-size 4 \
    --max-model-len 32768 \
    --gpu-memory-utilization 0.90
```

### 4. Hunyuan-A13B-Instruct > Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "Hunyuan",
        "messages": [{"role": "user", "content": "Give me a short introduction to large language models."}],
        "max_tokens": 100,
        "temperature": 0.7
    }'
```

### 5. Hunyuan-A13B-Instruct > Functional Verification

```json
{"id":"chatcmpl-9a60df2b23bb539f","object":"chat.completion","created":1774751760,"model":"Hunyuan","choices":[{"index":0,"message":{"role":"assistant","content":"<think>\nOkay, I need to write a short introduction to large language models. Let me start by recalling what I know. First, what are LLMs? They're machine learning models trained on vast amounts of text data. The key here is \"large\"—so they have a huge number of parameters. Maybe mention the scale, like billions or trillions of parameters.\n\nThen, how are they trained? They're trained on diverse text sources—books, websites, articles, etc. The","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning":null},"logprobs":null,"finish_reason":"length","stop_reason":null,"token_ids":null}],"service_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":12,"total_tokens":112,"completion_tokens":100,"prompt_tokens_details":null},"prompt_logprobs":null,"prompt_token_ids":null,"kv_transfer_params":null}
```
