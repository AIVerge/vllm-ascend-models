# Qwen3.5-27B & Qwen3.6-27B

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3.5-27B-Qwen3.6-27B.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 19
- `vllm serve` snippets: 6
- API or client verification snippets: 3

## Snippets

### 1. Qwen3.5-27B/Qwen3.6-27B > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=m.daocloud.io/quay.io/ascend/vllm-ascend:v0.22.1rc1-a3
docker run --rm \
    --name vllm-ascend \
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

### 2. Qwen3.5-27B/Qwen3.6-27B > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=m.daocloud.io/quay.io/ascend/vllm-ascend:v0.22.1rc1
docker run --rm \
    --name vllm-ascend \
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

### 3. Qwen3.5-27B/Qwen3.6-27B > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=m.daocloud.io/quay.io/ascend/vllm-ascend:v0.22.1rc1-310p
docker run --rm \
    --name vllm-ascend \
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
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /root/.cache:/root/.cache \
    -p 8080:8080 \
    -it $IMAGE bash
```

### 4. Qwen3.5-27B/Qwen3.6-27B > 4 Installation > 4.2 Source Code Installation

```bash
git clone https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
pip install -e .
```

### 5. Qwen3.5-27B/Qwen3.6-27B > 4 Installation > 4.2 Source Code Installation

```bash
pip uninstall -y triton-ascend triton
```

### 6. Qwen3.5-27B/Qwen3.6-27B > 4 Installation > 4.2 Source Code Installation

```bash
pip show vllm-ascend
```

### 7. Qwen3.5-27B/Qwen3.6-27B > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
#!/bin/sh
# Load model from ModelScope to speed up download
export VLLM_USE_MODELSCOPE=True
# To reduce memory fragmentation and avoid out of memory
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
# Size of the shared buffer (in MB) used by HCCL for NPU-to-NPU collective communication
export HCCL_BUFFSIZE=512
# Whether OpenMP threads are bound to specific CPU cores
export OMP_PROC_BIND=false
# Number of OpenMP threads available for parallel regions
export OMP_NUM_THREADS=1
# Enables the Ascend task queue for asynchronous operator dispatch
export TASK_QUEUE_ENABLE=1

# Model weight path; can be a ModelScope model id (e.g., Eco-Tech/Qwen3.5-27B-w8a8-mtp) or a local directory path
export MODEL_PATH=Eco-Tech/Qwen3.5-27B-w8a8-mtp

vllm serve $MODEL_PATH \
--host 0.0.0.0 \
--port 8000 \
--data-parallel-size 1 \
--tensor-parallel-size 2 \
--seed 1024 \
--quantization ascend \
--served-model-name qwen3.5 \
--max-num-seqs 32 \
--max-model-len 133000 \
--max-num-batched-tokens 16384 \
--trust-remote-code \
--gpu-memory-utilization 0.90 \
--no-enable-prefix-caching \
--speculative-config '{"method": "qwen3_5_mtp", "num_speculative_tokens": 3, "enforce_eager": true}' \
--compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
--additional-config '{"enable_cpu_binding":true}'
```

### 8. Qwen3.5-27B/Qwen3.6-27B > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
#!/bin/sh
# Load model from ModelScope to speed up download
export VLLM_USE_MODELSCOPE=True
# To reduce memory fragmentation and avoid out of memory
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
# Size of the shared buffer (in MB) used by HCCL for NPU-to-NPU collective communication
export HCCL_BUFFSIZE=512
# Whether OpenMP threads are bound to specific CPU cores
export OMP_PROC_BIND=false
# Number of OpenMP threads available for parallel regions
export OMP_NUM_THREADS=1
# Enables the Ascend task queue for asynchronous operator dispatch
export TASK_QUEUE_ENABLE=1

# Model weight path; can be a ModelScope model id (e.g., Eco-Tech/Qwen3.6-27B-w8a8) or a local directory path
export MODEL_PATH=Eco-Tech/Qwen3.6-27B-w8a8

vllm serve $MODEL_PATH \
--host 0.0.0.0 \
--port 8000 \
--data-parallel-size 1 \
--tensor-parallel-size 2 \
--seed 1024 \
--quantization ascend \
--served-model-name qwen3.6 \
--max-num-seqs 32 \
--max-model-len 262144 \
--max-num-batched-tokens 16384 \
--trust-remote-code \
--gpu-memory-utilization 0.90 \
--no-enable-prefix-caching \
--speculative-config '{"method": "qwen3_5_mtp", "num_speculative_tokens": 3, "enforce_eager": true}' \
--compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
--additional-config '{"enable_cpu_binding":true}'
```

### 9. Qwen3.5-27B/Qwen3.6-27B > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
#!/bin/sh
# Load model from ModelScope to speed up download
export VLLM_USE_MODELSCOPE=True

# Model weight path; can be a ModelScope model id (e.g., Eco-Tech/Qwen3.5-27B-w8a8-mtp) or a local directory path
export MODEL_PATH=Eco-Tech/Qwen3.5-27B-w8a8-mtp

vllm serve $MODEL_PATH \
--host 127.0.0.1 \
--port 1025 \
--tensor-parallel-size 4 \
--served-model-name qwen3.5 \
--max-num-seqs 128 \
--max-model-len 16384 \
--trust-remote-code \
--gpu-memory-utilization 0.90 \
--mamba-ssm-cache-dtype float16 \
--dtype float16 \
--speculative-config '{"method": "qwen3_5_mtp","num_speculative_tokens":1}' \
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,8]}' \
--additional-config '{"ascend_compilation_config": {"enable_npugraph_ex": false}}'
```

### 10. Qwen3.5-27B/Qwen3.6-27B > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
#!/bin/sh
# Load model from ModelScope to speed up download
export VLLM_USE_MODELSCOPE=True

# Model weight path; can be a ModelScope model id (e.g., Eco-Tech/Qwen3.6-27B-w8a8) or a local directory path
export MODEL_PATH=Eco-Tech/Qwen3.6-27B-w8a8

vllm serve $MODEL_PATH \
--host 127.0.0.1 \
--port 1025 \
--tensor-parallel-size 4 \
--served-model-name qwen3.6 \
--max-num-seqs 128 \
--max-model-len 16384 \
--trust-remote-code \
--gpu-memory-utilization 0.90 \
--mamba-ssm-cache-dtype float16 \
--dtype float16 \
--speculative-config '{"method": "qwen3_5_mtp","num_speculative_tokens":1}' \
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,8]}' \
--additional-config '{"ascend_compilation_config": {"enable_npugraph_ex": false}}'
```

### 11. Qwen3.5-27B/Qwen3.6-27B > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
(APIServer pid=<pid>) INFO:     Started server process [<pid>]
(APIServer pid=<pid>) INFO:     Waiting for application startup.
(APIServer pid=<pid>) INFO:     Application startup complete.
```

### 12. Qwen3.5-27B/Qwen3.6-27B > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
# nic_name is the network interface name corresponding to local_ip of the current node
nic_name="xxx"
local_ip="141.xx.xx.1"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name

# [Optional] jemalloc
# jemalloc is for better performance, if `libjemalloc.so` is installed on your machine, you can turn it on.
# export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export TASK_QUEUE_ENABLE=1
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/mooncake:$LD_LIBRARY_PATH

export HCCL_BUFFSIZE=1024
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export ASCEND_RT_VISIBLE_DEVICES=$1

vllm serve Eco-Tech/Qwen3.5-27B-w8a8-mtp \
  --host 0.0.0.0 \
  --port $2 \
  --data-parallel-size $3 \
  --data-parallel-rank $4 \
  --data-parallel-address $5 \
  --data-parallel-rpc-port $6 \
  --tensor-parallel-size $7 \
  --seed 1024 \
  --quantization ascend \
  --served-model-name qwen3.5 \
  --trust-remote-code \
  --max-num-seqs 4 \
  --max-model-len 32768 \
  --max-num-batched-tokens 16384 \
  --no-enable-prefix-caching \
  --gpu-memory-utilization 0.95 \
  --enforce-eager \
  --speculative-config '{"method": "qwen3_5_mtp", "num_speculative_tokens": 3, "enforce_eager": true}' \
  --additional-config '{"enable_cpu_binding":true}' \
  --kv-transfer-config \
  '{"kv_connector": "MooncakeConnectorV1",
  "kv_role": "kv_producer",
  "kv_port": "30000",
  "engine_id": "0",
  "kv_connector_extra_config": {
            "prefill": {
                    "dp_size": 8,
                    "tp_size": 2
            },
            "decode": {
                    "dp_size": 8,
                    "tp_size": 2
        }
    }
  }'
```

### 13. Qwen3.5-27B/Qwen3.6-27B > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
# nic_name is the network interface name corresponding to local_ip of the current node
nic_name="xxx"
local_ip="141.xx.xx.2"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name

# [Optional] jemalloc
# jemalloc is for better performance, if `libjemalloc.so` is installed on your machine, you can turn it on.
# export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export TASK_QUEUE_ENABLE=1
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/mooncake:$LD_LIBRARY_PATH

export HCCL_BUFFSIZE=1024
export ASCEND_RT_VISIBLE_DEVICES=$1

vllm serve Eco-Tech/Qwen3.5-27B-w8a8-mtp \
  --host 0.0.0.0 \
  --port $2 \
  --data-parallel-size $3 \
  --data-parallel-rank $4 \
  --data-parallel-address $5 \
  --data-parallel-rpc-port $6 \
  --tensor-parallel-size $7 \
  --seed 1024 \
  --quantization ascend \
  --served-model-name qwen3.5 \
  --trust-remote-code \
  --max-num-seqs 16 \
  --max-model-len 32768 \
  --max-num-batched-tokens 2048 \
  --no-enable-prefix-caching \
  --gpu-memory-utilization 0.91 \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --additional-config '{"recompute_scheduler_enable":true,"enable_cpu_binding":true}' \
  --speculative-config '{"method": "qwen3_5_mtp", "num_speculative_tokens": 3, "enforce_eager": true}' \
  --kv-transfer-config \
  '{"kv_connector": "MooncakeConnectorV1",
  "kv_role": "kv_consumer",
  "kv_port": "30200",
  "engine_id": "1",
  "kv_connector_extra_config": {
            "prefill": {
                    "dp_size": 8,
                    "tp_size": 2
            },
            "decode": {
                    "dp_size": 8,
                    "tp_size": 2
        }
    }
  }'
```

### 14. Qwen3.5-27B/Qwen3.6-27B > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
# p0 (Prefill node 0)
python launch_online_dp.py --dp-size 8 --tp-size 2 --dp-size-local 8 --dp-rank-start 0 --dp-address 141.xx.xx.1 --dp-rpc-port 12321 --vllm-start-port 7100
# d0 (Decode node 0)
python launch_online_dp.py --dp-size 8 --tp-size 2 --dp-size-local 8 --dp-rank-start 0 --dp-address 141.xx.xx.2 --dp-rpc-port 12321 --vllm-start-port 7100
```

### 15. Qwen3.5-27B/Qwen3.6-27B > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
python load_balance_proxy_server_example.py \
  --port 1999 \
  --host 141.xx.xx.1 \
  --prefiller-hosts \
    141.xx.xx.1 \
    141.xx.xx.1 \
    141.xx.xx.1 \
    141.xx.xx.1 \
    141.xx.xx.1 \
    141.xx.xx.1 \
    141.xx.xx.1 \
    141.xx.xx.1 \
  --prefiller-ports \
    7100 7101 7102 7103 7104 7105 7106 7107 \
  --decoder-hosts \
    141.xx.xx.2 \
    141.xx.xx.2 \
    141.xx.xx.2 \
    141.xx.xx.2 \
    141.xx.xx.2 \
    141.xx.xx.2 \
    141.xx.xx.2 \
    141.xx.xx.2 \
  --decoder-ports \
    7100 7101 7102 7103 7104 7105 7106 7107 \
```

### 16. Qwen3.5-27B/Qwen3.6-27B > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
curl http://<proxy_node0_ip>:1999/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen3.5",
        "messages": [
            {"role": "user", "content": "The future of AI is"}
        ],
        "max_tokens": 1024,
        "temperature": 1.0,
        "top_p": 0.95
    }'
```

### 17. Qwen3.5-27B/Qwen3.6-27B > 6 Functional Verification

```bash
curl http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen3.5",
        "prompt": "The future of AI is",
        "max_tokens": 50,
        "temperature": 0
    }'
```

### 18. Qwen3.5-27B/Qwen3.6-27B > 6 Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen3.5",
        "messages": [
            {"role": "user", "content": "The future of AI is"}
        ],
        "max_completion_tokens": 1024,
        "temperature": 0.7,
        "top_p": 0.95
    }'
```

### 19. Qwen3.5-27B/Qwen3.6-27B > 6 Functional Verification

```json
{
    "id": "cmpl-xxxxxxxxxxxxx",
    "object": "text_completion",
    "created": 1780971952,
    "model": "qwen3.5",
    "choices": [
        {
            "index": 0,
            "text": "The future of AI is a rapidly evolving landscape with breakthroughs in natural language understanding, multimodal reasoning, and autonomous agents. As models grow more capable and efficient...",
            "logprobs": null,
            "finish_reason": "length"
        }
    ],
    "usage": {
        "prompt_tokens": 4,
        "total_tokens": 54,
        "completion_tokens": 50
    }
}
```
