# Mixtral-8x7B-Instruct-v0.1

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Mixtral-8x7B-Instruct-v0.1.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 6
- `vllm serve` snippets: 1
- API or client verification snippets: 3

## Snippets

### 1. Mixtral-8x7B-Instruct-v0.1 > Environment Preparation > Installation

```bash
# Update --device according to your device (Atlas A2: /dev/davinci[0-7] Atlas A3:/dev/davinci[0-15]).
# Update the vllm-ascend image according to your environment.
# Note you should download the weight to /root/.cache in advance.
# Update the vllm-ascend image
export IMAGE=m.daocloud.io/quay.io/ascend/vllm-ascend:v0.22.1rc1
export NAME=vllm-ascend

# Run the container using the defined variables
# Note: If you are running bridge network with docker, please expose available ports for multiple nodes communication in advance.
docker run --rm \
    --name $NAME \
    --net=host \
    --shm-size=1g \
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

### 2. Mixtral-8x7B-Instruct-v0.1 > Deployment > Single-node Deployment

```bash
export HCCL_OP_EXPANSION_MODE="AIV"
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=200
export VLLM_ASCEND_ENABLE_MLAPO=1
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
```

### 3. Mixtral-8x7B-Instruct-v0.1 > Deployment > Single-node Deployment

```bash
vllm serve "mistralai/Mixtral-8x7B-Instruct-v0.1" \
  --tensor-parallel-size 4 \
  --max-model-len 4096 \
  --dtype bfloat16 \
  --trust-remote-code \
  --enforce-eager \
  --block-size 128 \
  --gpu-memory-utilization 0.7
```

### 4. Mixtral-8x7B-Instruct-v0.1 > Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "user", "content": "你好，介绍一下你自己"}
        ],
        "max_tokens": 100,
        "temperature": 0.7
    }'
```

### 5. Mixtral-8x7B-Instruct-v0.1 > Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "user", "content": "扮演一位资深架构师，评价一下在昇腾 Atlas A2 上部署 vLLM 的优势。"}
        ],
        "max_tokens": 100,
        "temperature": 0.7
    }'
```

### 6. Mixtral-8x7B-Instruct-v0.1 > Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "user", "content": "简单解释一下为什么 Mixtral 模型被称为\"混合专家模型\"(MoE)？"}
        ],
        "max_tokens": 100,
        "temperature": 0.7
    }'
```
