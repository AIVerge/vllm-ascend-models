# gpt-oss-120b

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/gpt-oss-120b.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 5
- `vllm serve` snippets: 1
- API or client verification snippets: 1

## Snippets

### 1. gpt-oss-120b > Environment Preparation > Installation > Docker Pull (by tag)

```bash
docker pull quay.io/ascend/vllm-ascend:v0.22.1rc1
```

### 2. gpt-oss-120b > Environment Preparation > Installation > Docker run

```bash
# Update --device according to your device (Atlas A2: /dev/davinci[0-7] Atlas A3:/dev/davinci[0-15]).
# Update the vllm-ascend image according to your environment.
# Note you should download the weight to /root/.cache in advance.
# For Atlas A2 machines:
# export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1
# For Atlas A3 machines:
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-a3
docker run --rm \
    --name vllm-ascend-env \
    --shm-size=1g \
    --net=host \
    --device /dev/davinci0 \
    --device /dev/davinci1 \
    --device /dev/davinci2 \
    --device /dev/davinci3 \
    --device /dev/davinci4 \
    --device /dev/davinci5 \
    --device /dev/davinci6 \
    --device /dev/davinci7 \
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

### 3. gpt-oss-120b > Deployment > Troubleshooting

```bash
mkdir -p tiktoken_encodings
wget -O tiktoken_encodings/o200k_base.tiktoken "https://openaipublic.blob.core.windows.net/encodings/o200k_base.tiktoken"
wget -O tiktoken_encodings/cl100k_base.tiktoken "https://openaipublic.blob.core.windows.net/encodings/cl100k_base.tiktoken"
export TIKTOKEN_ENCODINGS_BASE=${PWD}/tiktoken_encodings
```

### 4. gpt-oss-120b > Deployment > Single-node Deployment

```bash
#!/bin/sh
# Load model from ModelScope to speed up download
export VLLM_USE_MODELSCOPE=True
# To reduce memory fragmentation and avoid out of memory
export HCCL_OP_EXPANSION_MODE="AIV"
export HCCL_BUFFSIZE=512
export NPU_MEMORY_FRACTION=0.95
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3
export OMP_PROC_BIND=false
export VLLM_USE_V1=1
export TASK_QUEUE_ENABLE=1
export OMP_NUM_THREADS=1
export TIKTOKEN_ENCODINGS_BASE=${PWD}/tiktoken_encodings

vllm serve unsloth/gpt-oss-120b-BF16 \
--served-model-name gpt-oss-120b-bf16 \
--port 8000 \
--trust-remote-code \
--max-num-seqs 4 \
--gpu-memory-utilization 0.90 \
--tensor-parallel-size 4 \
--max-model-len 4096 \
--max-num-batched-tokens 4096 \
--enable-expert-parallel \
--compilation_config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes":[1,2,3,4]}'
```

### 5. gpt-oss-120b > Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "gpt-oss-120b-bf16",
        "messages": [{"role":"user", "content":"who are you"}]
    }'
```
