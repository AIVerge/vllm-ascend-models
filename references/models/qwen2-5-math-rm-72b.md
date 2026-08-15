# Qwen2.5-Math-RM-72B

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen2.5-Math-RM-72B.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 4
- `vllm serve` snippets: 1
- API or client verification snippets: 2

## Snippets

### 1. Qwen2.5-Math-RM-72B > Environment Preparation > Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1
docker run --rm \
    --device /dev/davinci0 \
    --device /dev/davinci1 \
    --device /dev/davinci2 \
    --device /dev/davinci3 \
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

### 2. Qwen2.5-Math-RM-72B > Deployment > Single-node Deployment

```bash
#!/bin/sh
export ASCEND_RT_VISIBLE_DEVICES=0
export MODEL_PATH="Qwen/Qwen2.5-Math-RM-72B"

vllm serve ${MODEL_PATH} \
          --host 0.0.0.0 \
          --port 8000 \
          --served-model-name qwen2.5-math-rm-72b \
          --trust-remote-code \
          --max-model-len 32768 \
          --task reward
```

### 3. Qwen2.5-Math-RM-72B > Functional Verification

```bash
curl http://localhost:8000/v1/reward \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen2.5-math-rm-72b",
        "messages": [
            {"role": "system", "content": "You are a helpful math assistant."},
            {"role": "user", "content": "What is 2+2?"},
            {"role": "assistant", "content": "2+2 equals 4."}
        ]
    }'
```

### 4. Qwen2.5-Math-RM-72B > Functional Verification > Batch Reward Scoring

```bash
curl http://localhost:8000/v1/reward/batch \
    -H "Content-Type: application/json" \
    -d '{
  "model": "qwen2.5-math-rm-72b",
  "conversations": [
    [
      {"role": "system", "content": "You are a helpful math assistant."},
      {"role": "user", "content": "What is 2+2?"},
      {"role": "assistant", "content": "2+2 equals 4."}
    ],
    [
      {"role": "system", "content": "You are a helpful math assistant."},
      {"role": "user", "content": "What is 2+2?"},
      {"role": "assistant", "content": "2+2 equals 5."}
    ]
  ],
  "batch_rewards": [
    {
      "index": 0,
      "score": 9.85,
      "reasoning": "The answer is mathematically correct and concise."
    },
    {
      "index": 1,
      "score": 1.20,
      "reasoning": "The answer contains a factual mathematical error (2+2 is not 5)."
    }
  ]
}'
```
