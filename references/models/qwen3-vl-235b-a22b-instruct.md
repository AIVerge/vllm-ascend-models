# Qwen3-VL-235B-A22B-Instruct

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3-VL-235B-A22B-Instruct.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 15
- `vllm serve` snippets: 5
- API or client verification snippets: 2

## Snippets

### 1. Qwen3-VL-235B-A22B-Instruct > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-a3
docker run --rm \
    --name vllm-ascend \
    --shm-size=512g \
    --net=host \
    --privileged=true \
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
    -v /etc/hccn.conf:/etc/hccn.conf \
    -v /root/.cache:/root/.cache \
    -it $IMAGE bash
```

### 2. Qwen3-VL-235B-A22B-Instruct > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1
docker run --rm \
    --name vllm-ascend \
    --shm-size=512g \
    --net=host \
    --privileged=true \
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
    -v /etc/hccn.conf:/etc/hccn.conf \
    -v /root/.cache:/root/.cache \
    -it $IMAGE bash
```

### 3. Qwen3-VL-235B-A22B-Instruct > 4 Installation > 4.1 Docker Image Installation

```bash
docker ps | grep vllm-ascend
```

### 4. Qwen3-VL-235B-A22B-Instruct > 4 Installation > 4.1 Docker Image Installation

```bash
pip show vllm-ascend
```

### 5. Qwen3-VL-235B-A22B-Instruct > 4 Installation > 4.2 Source Code Installation

```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm
pip install -e .
```

### 6. Qwen3-VL-235B-A22B-Instruct > 4 Installation > 4.2 Source Code Installation

```bash
git clone https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
pip install -e .
```

### 7. Qwen3-VL-235B-A22B-Instruct > 4 Installation > 4.2 Source Code Installation

```bash
pip show vllm vllm-ascend
```

### 8. Qwen3-VL-235B-A22B-Instruct > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
#!/bin/sh

# Load model from ModelScope to speed up download.
export VLLM_USE_MODELSCOPE=True

# Reduce memory fragmentation and avoid out-of-memory errors.
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

export HCCL_OP_EXPANSION_MODE="AIV"
export HCCL_BUFFSIZE=1536
export OMP_NUM_THREADS=1
export OMP_PROC_BIND=false
export TASK_QUEUE_ENABLE=1
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export VLLM_ASCEND_ENABLE_FUSED_MC2=1
export VLLM_ASCEND_BALANCE_SCHEDULING=1

vllm serve Eco-Tech/Qwen3-VL-235B-A22B-Instruct-w8a8-QuaRot \
  --host 0.0.0.0 \
  --port 8000 \
  --served-model-name qwen3-vl-235b \
  --quantization ascend \
  --data-parallel-size 4 \
  --tensor-parallel-size 4 \
  --enable-expert-parallel \
  --seed 1024 \
  --max-num-seqs 32 \
  --max-model-len 32768 \
  --max-num-batched-tokens 16384 \
  --trust-remote-code \
  --gpu-memory-utilization 0.92 \
  --no-enable-prefix-caching \
  --mm-processor-cache-gb 0 \
  --limit-mm-per-prompt.image 1 \
  --limit-mm-per-prompt.video 0 \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY","cudagraph_capture_sizes":[1,2,4,8,16,24,32]}'
```

### 9. Qwen3-VL-235B-A22B-Instruct > 5 Online Service Deployment > 5.2 Multi-Node Deployment with MP (Recommended for BF16)

```bash
#!/bin/sh

export VLLM_USE_MODELSCOPE=True
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

# Get these values through ifconfig.
# nic_name is the network interface name corresponding to local_ip.
nic_name="xxxx"
local_ip="xxxx"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export HCCL_BUFFSIZE=1024
export TASK_QUEUE_ENABLE=1
export HCCL_OP_EXPANSION_MODE="AIV"

vllm serve Eco-Tech/Qwen3-VL-235B-A22B-Instruct-w8a8-QuaRot \
  --host 0.0.0.0 \
  --port 8000 \
  --quantization ascend \
  --data-parallel-size 2 \
  --api-server-count 2 \
  --data-parallel-size-local 1 \
  --data-parallel-address $local_ip \
  --data-parallel-rpc-port 13389 \
  --seed 1024 \
  --served-model-name qwen3-vl-235b \
  --tensor-parallel-size 8 \
  --enable-expert-parallel \
  --max-num-seqs 16 \
  --max-model-len 262144 \
  --max-num-batched-tokens 4096 \
  --trust-remote-code \
  --gpu-memory-utilization 0.9 \
  --no-enable-prefix-caching \
  --mm-processor-cache-gb 0 \
  --limit-mm-per-prompt.image 1 \
  --limit-mm-per-prompt.video 0 \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --additional-config '{"enable_cpu_binding":true,"enable_flashcomm1":true}'
```

### 10. Qwen3-VL-235B-A22B-Instruct > 5 Online Service Deployment > 5.2 Multi-Node Deployment with MP (Recommended for BF16)

```bash
#!/bin/sh

export VLLM_USE_MODELSCOPE=True
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

# Get these values through ifconfig.
# nic_name is the network interface name corresponding to local_ip.
nic_name="xxxx"
local_ip="xxxx"

# The value of node0_ip must be consistent with local_ip on node 0.
node0_ip="xxxx"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export HCCL_BUFFSIZE=1024
export TASK_QUEUE_ENABLE=1
export HCCL_OP_EXPANSION_MODE="AIV"

vllm serve Eco-Tech/Qwen3-VL-235B-A22B-Instruct-w8a8-QuaRot \
  --host 0.0.0.0 \
  --port 8000 \
  --quantization ascend \
  --headless \
  --data-parallel-size 2 \
  --data-parallel-size-local 1 \
  --data-parallel-start-rank 1 \
  --data-parallel-address $node0_ip \
  --data-parallel-rpc-port 13389 \
  --seed 1024 \
  --tensor-parallel-size 8 \
  --served-model-name qwen3-vl-235b \
  --max-num-seqs 16 \
  --max-model-len 262144 \
  --max-num-batched-tokens 4096 \
  --enable-expert-parallel \
  --trust-remote-code \
  --gpu-memory-utilization 0.9 \
  --no-enable-prefix-caching \
  --mm-processor-cache-gb 0 \
  --limit-mm-per-prompt.image 1 \
  --limit-mm-per-prompt.video 0 \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --additional-config '{"enable_cpu_binding":true,"enable_flashcomm1":true}'
```

### 11. Qwen3-VL-235B-A22B-Instruct > 5 Online Service Deployment > 5.2 Multi-Node Deployment with MP (Recommended for BF16)

```bash
INFO:     Started server process [44610]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Started server process [44611]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 12. Qwen3-VL-235B-A22B-Instruct > 5 Online Service Deployment > 5.3 Multi-Node PD Separation Deployment > 5.3.1 Prefill Node

```bash
#!/bin/bash

export VLLM_USE_MODELSCOPE=True
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_BUFFSIZE=1024
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export HCCL_OP_EXPANSION_MODE="AIV"
export TASK_QUEUE_ENABLE=1

vllm serve Eco-Tech/Qwen3-VL-235B-A22B-Instruct-w8a8-QuaRot \
  --host 0.0.0.0 \
  --port 8080 \
  --quantization ascend \
  --data-parallel-size 2 \
  --data-parallel-size-local 2 \
  --tensor-parallel-size 8 \
  --seed 1024 \
  --served-model-name qwen3-vl-235b \
  --enable-expert-parallel \
  --max-num-seqs 32 \
  --max-model-len 8192 \
  --max-num-batched-tokens 8192 \
  --trust-remote-code \
  --no-enable-prefix-caching \
  --gpu-memory-utilization 0.9 \
  --kv-transfer-config \
  '{"kv_connector":"MooncakeConnectorV1",
    "kv_role":"kv_producer",
    "kv_port":"30000",
    "kv_connector_extra_config":{
      "prefill":{"dp_size":2,"tp_size":8},
      "decode":{"dp_size":4,"tp_size":4}
    }
  }'
```

### 13. Qwen3-VL-235B-A22B-Instruct > 5 Online Service Deployment > 5.3 Multi-Node PD Separation Deployment > 5.3.2 Decode Node

```bash
#!/bin/bash

export VLLM_USE_MODELSCOPE=True
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_BUFFSIZE=1024
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export HCCL_OP_EXPANSION_MODE="AIV"
export TASK_QUEUE_ENABLE=1

vllm serve Eco-Tech/Qwen3-VL-235B-A22B-Instruct-w8a8-QuaRot \
  --host 0.0.0.0 \
  --port 8080 \
  --quantization ascend \
  --data-parallel-size 4 \
  --data-parallel-size-local 4 \
  --tensor-parallel-size 4 \
  --seed 1024 \
  --served-model-name qwen3-vl-235b \
  --enable-expert-parallel \
  --max-num-seqs 32 \
  --max-model-len 8192 \
  --max-num-batched-tokens 8192 \
  --trust-remote-code \
  --no-enable-prefix-caching \
  --gpu-memory-utilization 0.9 \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --kv-transfer-config \
  '{"kv_connector":"MooncakeConnectorV1",
    "kv_role":"kv_consumer",
    "kv_port":"30200",
    "kv_connector_extra_config":{
      "prefill":{"dp_size":2,"tp_size":8},
      "decode":{"dp_size":4,"tp_size":4}
    }
  }'
```

### 14. Qwen3-VL-235B-A22B-Instruct > 5 Online Service Deployment > 5.3 Multi-Node PD Separation Deployment > 5.3.2 Decode Node

```bash
curl http://<server_ip>:<port>/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen3-vl-235b",
        "messages": [
            {
                "role": "user",
                "content": "Who are you?"
            }
        ],
        "max_tokens": 256,
        "temperature": 0
    }'
```

### 15. Qwen3-VL-235B-A22B-Instruct > 6 Functional Verification

```bash
curl http://<server_ip>:<port>/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-vl-235b",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": "https://modelscope.oss-cn-beijing.aliyuncs.com/resource/qwen.png"}},
        {"type": "text", "text": "What is the text in the illustration?"}
      ]}
    ],
    "max_completion_tokens": 100,
    "temperature": 0
  }'
```
