# Qwen3-Coder-30B-A3B

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3-Coder-30B-A3B.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 9
- `vllm serve` snippets: 1
- API or client verification snippets: 1

## Snippets

### 1. Qwen3-Coder-30B-A3B > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-a3

docker run \
    --name vllm-ascend-env \
    --ipc host \
    --net host \
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
    -v /usr/local/Ascend/driver:/usr/local/Ascend/driver \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /usr/local/sbin:/usr/local/sbin \
    -it -d $IMAGE bash
```

### 2. Qwen3-Coder-30B-A3B > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1

docker run \
    --name vllm-ascend-env \
    --ipc host \
    --net host \
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
    -v /usr/local/Ascend/driver:/usr/local/Ascend/driver \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /usr/local/sbin:/usr/local/sbin \
    -it -d $IMAGE bash
```

### 3. Qwen3-Coder-30B-A3B > 4 Installation > 4.1 Docker Image Installation

```bash
docker ps | grep vllm-ascend-env
```

### 4. Qwen3-Coder-30B-A3B > 4 Installation > 4.1 Docker Image Installation

```bash
pip show vllm-ascend
```

### 5. Qwen3-Coder-30B-A3B > 4 Installation > 4.2 Source Code Installation

```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm
pip install -e .
```

### 6. Qwen3-Coder-30B-A3B > 4 Installation > 4.2 Source Code Installation

```bash
git clone https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
pip install -e .
```

### 7. Qwen3-Coder-30B-A3B > 4 Installation > 4.2 Source Code Installation

```bash
pip show vllm vllm-ascend
```

### 8. Qwen3-Coder-30B-A3B > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3
export HCCL_OP_EXPANSION_MODE="AIV"  # not needed on A2
export HCCL_BUFFSIZE=1024
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

vllm serve your_model_path \
    --served-model-name qwen3-coder \
    --trust-remote-code \
    --max-num-seqs 100 \
    --max-model-len 40960 \
    --max-num-batched-tokens 16384 \
    --tensor-parallel-size 4 \
    --enable-expert-parallel \
    --quantization ascend \
    --distributed_executor_backend "mp" \
    --no-enable-prefix-caching \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \
    --additional-config '{"enable_flashcomm1": true, "weight_nz_mode": 2}' \
    --gpu-memory-utilization 0.95 \
    --port 8000 \
    --speculative-config '{"method": "eagle3", "model": "your_eagle3_model_path", "num_speculative_tokens": 3}'
```

### 9. Qwen3-Coder-30B-A3B > 6 Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen3-coder",
        "messages": [
            {"role": "user", "content": "Give me a short introduction to large language models."}
        ],
        "temperature": 0.6,
        "top_p": 0.95,
        "top_k": 20,
        "max_completion_tokens": 4096
    }'
```
