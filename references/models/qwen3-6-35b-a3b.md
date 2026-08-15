# Qwen3.6-35B-A3B

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3.6-35B-A3B.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 8
- `vllm serve` snippets: 2
- API or client verification snippets: 1

## Snippets

### 1. Qwen3.6-35B-A3B Deployment Tutorial > 4 Installation > 4.1 Docker Image Installation

```bash
# Download the model weight to /root/.cache in advance.
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
  -v /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool \
  -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
  -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
  -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
  -v /etc/ascend_install.info:/etc/ascend_install.info \
  -v /root/.cache:/root/.cache \
  -it $IMAGE bash
```

### 2. Qwen3.6-35B-A3B Deployment Tutorial > 4 Installation > 4.1 Docker Image Installation

```bash
# Download the model weight to /root/.cache in advance.
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1
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

### 3. Qwen3.6-35B-A3B Deployment Tutorial > 4 Installation > 4.1 Docker Image Installation > Standard container

```bash
# Use the vllm-ascend image
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-310p

docker run --rm \
--name vllm-ascend \
--shm-size=10g \
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
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-p 8080:8080 \
-it $IMAGE bash
```

### 4. Qwen3.6-35B-A3B Deployment Tutorial > 4 Installation > 4.1 Docker Image Installation > Standard container

```bash
python -c "import vllm, vllm_ascend; print('vllm and vllm_ascend are ready')"
```

### 5. Qwen3.6-35B-A3B Deployment Tutorial > 4 Installation > 4.2 Source Code Installation

```bash
pip uninstall -y triton-ascend triton
```

### 6. Qwen3.6-35B-A3B Deployment Tutorial > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
#!/bin/sh

# Load model from ModelScope to speed up download.
export VLLM_USE_MODELSCOPE=True

# Reduce memory fragmentation and avoid out-of-memory errors.
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

export HCCL_OP_EXPANSION_MODE="AIV"
export HCCL_BUFFSIZE=1024
export OMP_NUM_THREADS=1
export TASK_QUEUE_ENABLE=1
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl -w vm.swappiness=0
sysctl -w kernel.numa_balancing=0
sysctl kernel.sched_migration_cost_ns=50000
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

vllm serve Eco-Tech/Qwen3.6-35B-A3B-w8a8 \
  --host 0.0.0.0 \
  --port 8000 \
  --data-parallel-size 1 \
  --tensor-parallel-size 2 \
  --enable-expert-parallel \
  --seed 1024 \
  --quantization ascend \
  --served-model-name qwen3.6 \
  --max-num-seqs 128 \
  --max-model-len 262144 \
  --max-num-batched-tokens 16384 \
  --trust-remote-code \
  --gpu-memory-utilization 0.90 \
  --enable-prefix-caching \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --additional-config '{"enable_cpu_binding":true, "enable_flashcomm1":true, "multistream_overlap_shared_expert": true}'
```

### 7. Qwen3.6-35B-A3B Deployment Tutorial > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
export VLLM_USE_MODELSCOPE=True
export ASCEND_RT_VISIBLE_DEVICES=0,1

vllm serve Eco-Tech/Qwen3.6-35B-A3B-w8a8 \
  --host 127.0.0.1 \
  --port 8080 \
  --tensor-parallel-size 2 \
  --gpu-memory-utilization 0.90 \
  --max-num-seqs 16 \
  --served-model-name qwen3.6 \
  --dtype float16 \
  --additional-config '{"ascend_compilation_config": {"enable_npugraph_ex":false}}' \
  --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,8]}' \
  --quantization ascend \
  --max-model-len 20480 \
  --no-enable-prefix-caching
```

### 8. Qwen3.6-35B-A3B Deployment Tutorial > 6 Functional Verification

```bash
curl http://<server_ip>:<port>/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3.6",
    "prompt": "The future of AI is",
    "max_tokens": 50,
    "temperature": 0
  }'
```
