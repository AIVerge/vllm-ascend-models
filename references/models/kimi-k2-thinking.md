# Kimi-K2-Thinking

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Kimi-K2-Thinking.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 8
- `vllm serve` snippets: 1
- API or client verification snippets: 1

## Snippets

### 1. Kimi-K2-Thinking > 4 Installation > 4.1 Docker Image Installation

```bash
# Update the vllm-ascend image according to your environment.
   export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-a3

# Run the container using the defined variables
# Note: If you are running bridge network with docker, please expose available ports for multiple nodes communication in advance
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
-v /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /mnt/sfs_turbo/.cache:/home/cache \
-it $IMAGE bash
```

### 2. Kimi-K2-Thinking > 4 Installation > 4.1 Docker Image Installation

```bash
docker ps --filter name=vllm-ascend --format "table {{.Names}}\t{{.Status}}"
```

### 3. Kimi-K2-Thinking > 4 Installation > 4.1 Docker Image Installation

```bash
npu-smi info
```

### 4. Kimi-K2-Thinking > 4 Installation > 4.2 Source Code Installation

```bash
# Install vLLM.
git clone --depth 1 --branch v0.22.1 https://github.com/vllm-project/vllm
cd vllm
VLLM_TARGET_DEVICE=empty pip install -e .
cd ..

# Install vLLM Ascend.
git clone --depth 1 --branch v0.22.1rc1 https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
pip install -e .
```

### 5. Kimi-K2-Thinking > 4 Installation > 4.2 Source Code Installation

```bash
python -c "import vllm; import vllm_ascend; print('vllm and vllm_ascend import ok')"
```

### 6. Kimi-K2-Thinking > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
export HCCL_BUFFSIZE=1024
export TASK_QUEUE_ENABLE=1
export OMP_PROC_BIND=false
export HCCL_OP_EXPANSION_MODE=AIV
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export SERVER_PORT=8000

vllm serve moonshotai/Kimi-K2-Thinking \
  --tensor-parallel-size 16 \
  --port $SERVER_PORT \
  --max-model-len 8192 \
  --max-num-batched-tokens 8192 \
  --max-num-seqs 12 \
  --gpu-memory-utilization 0.9 \
  --trust-remote-code \
  --enable-expert-parallel \
  --no-enable-prefix-caching
```

### 7. Kimi-K2-Thinking > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
INFO:     Started server process [...]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 8. Kimi-K2-Thinking > 6 Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{
  "model": "moonshotai/Kimi-K2-Thinking",
  "messages": [
    {"role": "user", "content": "Who are you?"}
  ],
  "temperature": 1.0
}'
```
