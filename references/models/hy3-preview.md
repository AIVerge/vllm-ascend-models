# Hy3-preview

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Hy3-preview.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 6
- `vllm serve` snippets: 1
- API or client verification snippets: 3

## Snippets

### 1. Hy3-preview > Environment Preparation > Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-a3
  export NAME=vllm-ascend

  docker run --rm \
    --name $NAME \
    --net=host \
    --shm-size=1g \
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
    -v /models:/models \
    -it $IMAGE bash
```

### 2. Hy3-preview > Deployment > Single-node Deployment

```bash
cd /workspace
export MODEL_PATH=/models/Hy3-preview

HCCL_OP_EXPANSION_MODE=AIV \
vllm serve ${MODEL_PATH} \
  --served-model-name hy3-preview \
  --tensor-parallel-size 16 \
  --speculative-config.method mtp \
  --speculative-config.num_speculative_tokens 1 \
  --enable-expert-parallel \
  --enable-ep-weight-filter \
  --tool-call-parser hy_v3 \
  --reasoning-parser hy_v3 \
  --enable-auto-tool-choice \
  --max-model-len 32768 \
  --max-num-seqs 8 \
  --host 0.0.0.0 \
  --port 8000
```

### 3. Hy3-preview > Functional Verification

```bash
curl -sf http://127.0.0.1:8000/v1/models
```

### 4. Hy3-preview > Functional Verification

```bash
curl -sS http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "hy3-preview",
    "messages": [{"role": "user", "content": "Say hi in one word."}],
    "max_tokens": 16,
    "temperature": 0,
    "top_p": 1,
    "chat_template_kwargs": {"reasoning_effort": "no_think"}
  }'
```

### 5. Hy3-preview > Functional Verification

```json
{
  "model": "hy3-preview",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Hi"
      },
      "finish_reason": "stop"
    }
  ]
}
```

### 6. Hy3-preview > Performance > Lightweight Online Benchmark

```bash
vllm bench serve \
  --backend openai-chat \
  --base-url http://127.0.0.1:8000 \
  --endpoint /v1/chat/completions \
  --model /models/Hy3-preview \
  --served-model-name hy3-preview \
  --dataset-name random \
  --random-input-len 1024 \
  --random-output-len 128 \
  --num-prompts 4 \
  --request-rate inf \
  --max-concurrency 1 \
  --temperature 0 \
  --top-p 1
```
