# MiniMax-M2

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/MiniMax-M2.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 17
- `vllm serve` snippets: 4
- API or client verification snippets: 3

## Snippets

### 1. MiniMax-M2 > 4 Installation > 4.1 Docker Image Installation

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

### 2. MiniMax-M2 > 4 Installation > 4.1 Docker Image Installation

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

### 3. MiniMax-M2 > 4 Installation > 4.1 Docker Image Installation

```bash
docker ps | grep vllm-ascend-env
```

### 4. MiniMax-M2 > 4 Installation > 4.1 Docker Image Installation

```bash
pip show vllm-ascend
```

### 5. MiniMax-M2 > 4 Installation > 4.2 Source Code Installation

```bash
python -c "import vllm_ascend; print(vllm_ascend.__version__)"
```

### 6. MiniMax-M2 > 5 Online Service Deployment > 5.1 Single-Node Online Deployment > A3 (single node)

```bash
export HCCL_OP_EXPANSION_MODE="AIV"
export HCCL_BUFFSIZE=1024
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_NUM_THREADS=1
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl -w vm.swappiness=0
sysctl -w kernel.numa_balancing=0
sysctl kernel.sched_migration_cost_ns=50000
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD
export TASK_QUEUE_ENABLE=1

export VLLM_ASCEND_BALANCE_SCHEDULING=0

vllm serve /path/to/weight/MiniMax-M2.7-w8a8-QuaRot \
    --served-model-name "MiniMax-M2.7" \
    --host 0.0.0.0 \
    --port 8000 \
    --trust-remote-code \
    --quantization ascend \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \
    --additional-config '{"enable_cpu_binding":true,
                          "enable_fused_mc2":true,
                          "enable_flashcomm1":true,
                          "weight_nz_mode":true}' \
    --enable-expert-parallel \
    --tensor-parallel-size 4 \
    --data-parallel-size 4 \
    --max-num-seqs 48 \
    --max-model-len 40690 \
    --max-num-batched-tokens 16384 \
    --gpu-memory-utilization 0.85 \
    --speculative_config '{"enforce_eager": true, "method": "eagle3", "model": "/path/to/weight/Eagle3/", "num_speculative_tokens": 3}'
```

### 7. MiniMax-M2 > 5 Online Service Deployment > 5.1 Single-Node Online Deployment > A3 (single node)

```bash
--enable-auto-tool-choice \
    --tool-call-parser minimax_m2 \
    --reasoning-parser minimax_m2_append_think \
```

### 8. MiniMax-M2 > 5 Online Service Deployment > 5.1 Single-Node Online Deployment > A2 (single node)

```bash
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD
export HCCL_OP_EXPANSION_MODE="AIV"
export HCCL_BUFFSIZE=512
sysctl -w vm.swappiness=0
sysctl -w kernel.numa_balancing=0
sysctl kernel.sched_migration_cost_ns=50000
export TASK_QUEUE_ENABLE=1
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTRA_ROCE_ENABLE=0
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1

vllm serve /path/to/weight/MiniMax-M2.7-w8a8-QuaRot \
    --served-model-name MiniMax-M2.7 \
    --host 0.0.0.0 \
    --port 8000 \
    --trust-remote-code \
    --tensor-parallel-size 8 \
    --quantization ascend \
    --enable-expert-parallel \
    --max-num-seqs 32 \
    --seed 1024 \
    --max-num-batched-tokens 32768 \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \
    --gpu-memory-utilization 0.85 \
    --additional-config '{"enable_cpu_binding":true,
                          "enable_flashcomm1":true}' \
    --model-loader-extra-config '{"enable_multithread_load":true,"num_threads":16}' \
    --speculative_config '{"method": "eagle3", "model": "/path/to/weight/Eagle3/",  "num_speculative_tokens":3}'
```

### 9. MiniMax-M2 > 5 Online Service Deployment > 5.1 Single-Node Online Deployment > A2 (single node)

```bash
--enable-auto-tool-choice \
    --tool-call-parser minimax_m2 \
    --reasoning-parser minimax_m2_append_think \
```

### 10. MiniMax-M2 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
unset http_proxy https_proxy ftp_proxy

nic_name="<your_nic_name>"
local_ip="<your_ip>"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name

export HCCL_BUFFSIZE=1024
export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_NUM_THREADS=1
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl -w vm.swappiness=0
sysctl -w kernel.numa_balancing=0
sysctl kernel.sched_migration_cost_ns=50000
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/mooncake:$LD_LIBRARY_PATH

export TASK_QUEUE_ENABLE=1
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export VLLM_ASCEND_ENABLE_FUSED_MC2=1
export PYTHONHASHSEED=0

export ASCEND_RT_VISIBLE_DEVICES=$1

vllm serve /path/to/weight/MiniMax-M2.7-w8a8-QuaRot \
    --host 0.0.0.0 \
    --port $2 \
    --data-parallel-size $3 \
    --data-parallel-rank $4 \
    --data-parallel-address $5 \
    --data-parallel-rpc-port $6 \
    --tensor-parallel-size $7 \
    --enable-expert-parallel \
    --served-model-name minimax \
    --max-model-len 200000 \
    --max-num-batched-tokens 16384 \
    --max-num-seqs 64 \
    --trust-remote-code \
    --gpu-memory-utilization 0.75 \
    --quantization ascend \
    --enforce-eager \
    --speculative_config '{"method": "eagle3", "model": "/path/to/weight/Eagle3/", "num_speculative_tokens": 1}' \
    --additional-config '{"enable_cpu_binding":true}' \
    --kv-transfer-config \
        '{"kv_connector": "MooncakeConnectorV1",
        "kv_role": "kv_producer",
        "kv_port": "35880",
        "engine_id": "0",
        "kv_connector_extra_config": {
             "use_ascend_direct": true,
             "prefill": {"dp_size": 2, "tp_size": 8},
             "decode":  {"dp_size": 2, "tp_size": 8}
        }}'
```

### 11. MiniMax-M2 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
unset http_proxy https_proxy ftp_proxy

nic_name="<your_nic_name>"
local_ip="<your_ip>"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name

export HCCL_BUFFSIZE=2048
export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_NUM_THREADS=1
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl -w vm.swappiness=0
sysctl -w kernel.numa_balancing=0
sysctl kernel.sched_migration_cost_ns=50000
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/mooncake:$LD_LIBRARY_PATH

export TASK_QUEUE_ENABLE=1
export VLLM_ASCEND_ENABLE_FLASHCOMM1=0
export VLLM_ASCEND_ENABLE_FUSED_MC2=1
export PYTHONHASHSEED=0

export ASCEND_RT_VISIBLE_DEVICES=$1

vllm serve /path/to/weight/MiniMax-M2.7-w8a8-QuaRot \
    --host 0.0.0.0 \
    --port $2 \
    --data-parallel-size $3 \
    --data-parallel-rank $4 \
    --data-parallel-address $5 \
    --data-parallel-rpc-port $6 \
    --tensor-parallel-size $7 \
    --enable-expert-parallel \
    --served-model-name minimax \
    --max-model-len 200000 \
    --max-num-batched-tokens 16384 \
    --max-num-seqs 16 \
    --trust-remote-code \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.75 \
    --quantization ascend \
    --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
    --speculative_config '{"method": "eagle3", "model": "/path/to/weight/Eagle3/", "num_speculative_tokens": 3}' \
    --additional-config '{"enable_cpu_binding":true}' \
    --kv-transfer-config \
        '{"kv_connector": "MooncakeConnectorV1",
        "kv_role": "kv_consumer",
        "kv_port": "56900",
        "engine_id": "1",
        "kv_connector_extra_config": {
             "use_ascend_direct": true,
             "prefill": {"dp_size": 2, "tp_size": 8},
             "decode":  {"dp_size": 2, "tp_size": 8}
        }}'
```

### 12. MiniMax-M2 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
python launch_online_dp.py \
    --dp-size 2 --tp-size 8 \
    --dp-size-local 2 --dp-rank-start 0 \
    --dp-address <prefill_ip> --dp-rpc-port 12321 \
    --vllm-start-port 7000
```

### 13. MiniMax-M2 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
python launch_online_dp.py \
    --dp-size 2 --tp-size 8 \
    --dp-size-local 2 --dp-rank-start 0 \
    --dp-address <decode_ip> --dp-rpc-port 12321 \
    --vllm-start-port 7100
```

### 14. MiniMax-M2 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment > Request Forwarding

```bash
unset http_proxy https_proxy

python load_balance_proxy_server_example.py \
    --port 8009 \
    --host <prefill_ip> \
    --prefiller-hosts \
       <prefill_ip> <prefill_ip> \
    --prefiller-ports \
       7000 7001 \
    --decoder-hosts \
       <decode_ip> <decode_ip> \
    --decoder-ports \
       7100 7101
```

### 15. MiniMax-M2 > 6 Functional Verification > Using curl

```bash
curl http://<node_ip>:<port>/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMax-M2.7",
    "messages": [{"role": "user", "content": "Hello, who are you?"}],
    "stream": false,
    "temperature": 0.8,
    "max_tokens": 200
  }'
```

### 16. MiniMax-M2 > 6 Functional Verification > Using OpenAI Python Client

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="na")

resp = client.chat.completions.create(
    model="MiniMax-M2.7",
    messages=[{"role": "user", "content": "你好，请介绍一下你自己，并展示一次工具调用的参数格式。"}],
    max_tokens=256,
)
print(resp.choices[0].message.content)
```

### 17. MiniMax-M2 > 6 Functional Verification > Tool Calling Verification

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMax-M2.7",
    "messages": [{"role": "user", "content": "请查询上海的天气。"}],
    "tools": [{
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get weather by city",
        "parameters": {
          "type": "object",
          "properties": {
            "city": {"type": "string"},
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
          },
          "required": ["city"]
        }
      }
    }],
    "tool_choice": "auto",
    "temperature": 0,
    "max_tokens": 512
  }'
```
