# Kimi-K2.6

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Kimi-K2.6.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 16
- `vllm serve` snippets: 5
- API or client verification snippets: 3

## Snippets

### 1. Kimi-K2.6 > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-a3
docker run --rm \
    --name vllm-ascend \
    --shm-size=1g \
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
    -v /root/.cache:/root/.cache \
    -it $IMAGE bash
```

### 2. Kimi-K2.6 > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1
docker run --rm \
    --name vllm-ascend \
    --shm-size=1g \
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
    -v /root/.cache:/root/.cache \
    -it $IMAGE bash
```

### 3. Kimi-K2.6 > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
#!/bin/sh
export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export TASK_QUEUE_ENABLE=1
export VLLM_ASCEND_ENABLE_MLAPO=1

# [Optional] jemalloc
# jemalloc is for better performance, if `libjemalloc.so` is installed on your machine, you can turn it on.
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl -w vm.swappiness=0
sysctl -w kernel.numa_balancing=0
sysctl -w kernel.sched_migration_cost_ns=50000

export HCCL_BUFFSIZE=600
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export VLLM_ASCEND_BALANCE_SCHEDULING=0

vllm serve Eco-Tech/Kimi-K2.6-W4A8 \
    --quantization ascend \
    --tool-call-parser kimi_k2 \
    --reasoning-parser kimi_k2 \
    --allowed-local-media-path / \
    --served-model-name kimi_k26 \
    --trust-remote-code \
    --tensor-parallel-size 4 \
    --data-parallel-size 4 \
    --no-enable-prefix-caching \
    --enable-expert-parallel \
    --port 8000 \
    --max-num-seqs 4 \
    --max-model-len 34816 \
    --max-num-batched-tokens 16384 \
    --gpu-memory-utilization 0.87 \
    --seed 42 \
    --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
    --profiler-config '{"profiler": "torch", "torch_profiler_dir": "./vllm_profile", "torch_profiler_with_stack": true}' \
    --mm-processor-cache-gb 0 \
    --mm-encoder-tp-mode data \
    --additional-config '{"enable_balance_scheduling": true}' \
    --speculative-config '{"method": "dflash","model": "z-lab/Kimi-K2.5-DFlash", "num_speculative_tokens": 15}'
```

### 4. Kimi-K2.6 > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
curl http://<node_ip>:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "kimi_k26",
        "messages": [{
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": "The future of AI is"
            }]
        }],
        "max_tokens": 1024,
        "temperature": 1.0,
        "top_p": 0.95
    }'
```

### 5. Kimi-K2.6 > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```json
{
    "id": "chatcmpl-9df13fd5e539af93",
    "object": "chat.completion",
    "created": 1780971952,
    "model": "kimi_k26",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "The future of AI is not a destination we are passively approaching, but a design problem we are actively solving right now...",
                "reasoning": "The user is asking for my thoughts on \"The future of AI is\"...",
                "refusal": null,
                "annotations": null,
                "audio": null,
                "function_call": null
            },
            "logprobs": null,
            "finish_reason": "length",
            "stop_reason": null,
            "token_ids": null
        }
    ],
    "usage": {
        "prompt_tokens": 13,
        "total_tokens": 1037,
        "completion_tokens": 1024,
        "completion_tokens_details": {
            "reasoning_tokens": 0,
            "audio_tokens": null,
            "accepted_prediction_tokens": null,
            "rejected_prediction_tokens": null
        }
    }
}
```

### 6. Kimi-K2.6 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
# this obtained through ifconfig
# nic_name is the network interface name corresponding to local_ip of the current node
nic_name="xxx"
local_ip="141.xx.xx.1"

# The value of node0_ip must be consistent with the value of local_ip set in node0 (master node)
node0_ip="xxxx"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name

# [Optional] jemalloc
# jemalloc is for better performance, if `libjemalloc.so` is installed on your machine, you can turn it on.
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl -w vm.swappiness=0
sysctl -w kernel.numa_balancing=0
sysctl kernel.sched_migration_cost_ns=50000
export VLLM_RPC_TIMEOUT=3600000
export VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS=30000
export HCCL_EXEC_TIMEOUT=204
export HCCL_CONNECT_TIMEOUT=120

export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export TASK_QUEUE_ENABLE=1
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/mooncake:$LD_LIBRARY_PATH

export HCCL_BUFFSIZE=1536
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export ASCEND_RT_VISIBLE_DEVICES=$1

vllm serve Eco-Tech/Kimi-K2.6-W4A8 \
    --host 0.0.0.0 \
    --port $2 \
    --data-parallel-size $3 \
    --data-parallel-rank $4 \
    --data-parallel-address $5 \
    --data-parallel-rpc-port $6 \
    --tensor-parallel-size $7 \
    --enable-expert-parallel \
    --seed 1024 \
    --quantization ascend \
    --served-model-name kimi_k26 \
    --trust-remote-code \
    --max-num-seqs 1 \
    --max-model-len 133120 \
    --max-num-batched-tokens 16384 \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.92 \
    --enforce-eager \
    --enable-auto-tool-choice \
    --tool-call-parser kimi_k2 \
    --reasoning-parser kimi_k2 \
    --additional-config '{"recompute_scheduler_enable":true,"enable_shared_expert_dp": true}' \
    --mm-encoder-tp-mode data \
    --kv-transfer-config \
    '{"kv_connector": "MooncakeConnectorV1",
    "kv_role": "kv_producer",
    "kv_port": "30000",
    "engine_id": "0",
    "kv_connector_extra_config": {
            "use_ascend_direct": true,
            "prefill": {
                    "dp_size": 4,
                    "tp_size": 4
            },
            "decode": {
                    "dp_size": 8,
                    "tp_size": 4
            }
        }
    }'
```

### 7. Kimi-K2.6 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
# this obtained through ifconfig
# nic_name is the network interface name corresponding to local_ip of the current node
nic_name="xxx"
local_ip="141.xx.xx.2"

# The value of node0_ip must be consistent with the value of local_ip set in node0 (master node)
node0_ip="xxxx"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name

# [Optional] jemalloc
# jemalloc is for better performance, if `libjemalloc.so` is installed on your machine, you can turn it on.
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl -w vm.swappiness=0
sysctl -w kernel.numa_balancing=0
sysctl kernel.sched_migration_cost_ns=50000
export VLLM_RPC_TIMEOUT=3600000
export VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS=30000
export HCCL_EXEC_TIMEOUT=204
export HCCL_CONNECT_TIMEOUT=120

export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export TASK_QUEUE_ENABLE=1
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/mooncake:$LD_LIBRARY_PATH

export HCCL_BUFFSIZE=1536
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export ASCEND_RT_VISIBLE_DEVICES=$1

vllm serve Eco-Tech/Kimi-K2.6-W4A8 \
    --host 0.0.0.0 \
    --port $2 \
    --data-parallel-size $3 \
    --data-parallel-rank $4 \
    --data-parallel-address $5 \
    --data-parallel-rpc-port $6 \
    --tensor-parallel-size $7 \
    --enable-expert-parallel \
    --seed 1024 \
    --quantization ascend \
    --served-model-name kimi_k26 \
    --trust-remote-code \
    --max-num-seqs 1 \
    --max-model-len 133120 \
    --max-num-batched-tokens 16384 \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.92 \
    --enforce-eager \
    --enable-auto-tool-choice \
    --tool-call-parser kimi_k2 \
    --reasoning-parser kimi_k2 \
    --additional-config '{"recompute_scheduler_enable":true,"enable_shared_expert_dp": true}' \
    --mm-encoder-tp-mode data \
    --kv-transfer-config \
    '{"kv_connector": "MooncakeConnectorV1",
    "kv_role": "kv_producer",
    "kv_port": "30100",
    "engine_id": "1",
    "kv_connector_extra_config": {
            "prefill": {
                    "dp_size": 4,
                    "tp_size": 4
            },
            "decode": {
                    "dp_size": 8,
                    "tp_size": 4
            }
        }
    }'
```

### 8. Kimi-K2.6 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
# this obtained through ifconfig
# nic_name is the network interface name corresponding to local_ip of the current node
nic_name="xxx"
local_ip="141.xx.xx.3"

# The value of node0_ip must be consistent with the value of local_ip set in node0 (master node)
node0_ip="xxxx"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name

# [Optional] jemalloc
# jemalloc is for better performance, if `libjemalloc.so` is installed on your machine, you can turn it on.
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl -w vm.swappiness=0
sysctl -w kernel.numa_balancing=0
sysctl kernel.sched_migration_cost_ns=50000
export VLLM_RPC_TIMEOUT=3600000
export HCCL_EXEC_TIMEOUT=204
export HCCL_CONNECT_TIMEOUT=120
export VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS=30000

export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export TASK_QUEUE_ENABLE=1
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/mooncake:$LD_LIBRARY_PATH

export HCCL_BUFFSIZE=800
export VLLM_ASCEND_ENABLE_MLAPO=1
export ASCEND_RT_VISIBLE_DEVICES=$1

vllm serve Eco-Tech/Kimi-K2.6-W4A8 \
    --host 0.0.0.0 \
    --port $2 \
    --data-parallel-size $3 \
    --data-parallel-rank $4 \
    --data-parallel-address $5 \
    --data-parallel-rpc-port $6 \
    --tensor-parallel-size $7 \
    --enable-expert-parallel \
    --seed 1024 \
    --quantization ascend \
    --served-model-name kimi_k26 \
    --trust-remote-code \
    --max-num-seqs 8 \
    --max-model-len 133720 \
    --max-num-batched-tokens 32 \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.91 \
    --enable-auto-tool-choice \
    --tool-call-parser kimi_k2 \
    --reasoning-parser kimi_k2 \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \
    --additional-config '{"recompute_scheduler_enable":true,"multistream_overlap_shared_expert": true}' \
    --speculative-config '{"method": "eagle3", "model":"lightseekorg/kimi-k2.6-eagle3", "num_speculative_tokens": 3}' \
    --kv-transfer-config \
    '{"kv_connector": "MooncakeConnectorV1",
    "kv_role": "kv_consumer",
    "kv_port": "30200",
    "engine_id": "2",
    "kv_connector_extra_config": {
            "prefill": {
                    "dp_size": 4,
                    "tp_size": 4
            },
            "decode": {
                    "dp_size": 8,
                    "tp_size": 4
            }
        }
    }'
```

### 9. Kimi-K2.6 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
# this obtained through ifconfig
# nic_name is the network interface name corresponding to local_ip of the current node
nic_name="xxx"
local_ip="141.xx.xx.4"

# The value of node0_ip must be consistent with the value of local_ip set in node0 (master node)
node0_ip="xxxx"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name

# [Optional] jemalloc
# jemalloc is for better performance, if `libjemalloc.so` is installed on your machine, you can turn it on.
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl -w vm.swappiness=0
sysctl -w kernel.numa_balancing=0
sysctl kernel.sched_migration_cost_ns=50000
export VLLM_RPC_TIMEOUT=3600000
export HCCL_EXEC_TIMEOUT=204
export HCCL_CONNECT_TIMEOUT=120
export VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS=30000

export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export TASK_QUEUE_ENABLE=1
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/mooncake:$LD_LIBRARY_PATH

export HCCL_BUFFSIZE=800
export VLLM_ASCEND_ENABLE_MLAPO=1
export ASCEND_RT_VISIBLE_DEVICES=$1

vllm serve Eco-Tech/Kimi-K2.6-W4A8 \
    --host 0.0.0.0 \
    --port $2 \
    --data-parallel-size $3 \
    --data-parallel-rank $4 \
    --data-parallel-address $5 \
    --data-parallel-rpc-port $6 \
    --tensor-parallel-size $7 \
    --enable-expert-parallel \
    --seed 1024 \
    --quantization ascend \
    --served-model-name kimi_k26 \
    --trust-remote-code \
    --max-num-seqs 8 \
    --max-model-len 133720 \
    --max-num-batched-tokens 32 \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.91 \
    --enable-auto-tool-choice \
    --tool-call-parser kimi_k2 \
    --reasoning-parser kimi_k2 \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \
    --additional-config '{"recompute_scheduler_enable":true,"multistream_overlap_shared_expert": true}' \
    --speculative-config '{"method": "eagle3", "model":"lightseekorg/kimi-k2.6-eagle3", "num_speculative_tokens": 3}' \
    --kv-transfer-config \
    '{"kv_connector": "MooncakeConnectorV1",
    "kv_role": "kv_consumer",
    "kv_port": "30300",
    "engine_id": "3",
    "kv_connector_extra_config": {
            "prefill": {
                    "dp_size": 4,
                    "tp_size": 4
            },
            "decode": {
                    "dp_size": 8,
                    "tp_size": 4
            }
        }
    }'
```

### 10. Kimi-K2.6 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
# p0
python launch_online_dp.py --dp-size 4 --tp-size 4 --dp-size-local 4 --dp-rank-start 0 --dp-address 141.xx.xx.1 --dp-rpc-port 12321 --vllm-start-port 7100
# p1
python launch_online_dp.py --dp-size 4 --tp-size 4 --dp-size-local 4 --dp-rank-start 0 --dp-address 141.xx.xx.2 --dp-rpc-port 12321 --vllm-start-port 7100
# d0
python launch_online_dp.py --dp-size 8 --tp-size 4 --dp-size-local 4 --dp-rank-start 0 --dp-address 141.xx.xx.3 --dp-rpc-port 12321 --vllm-start-port 7100
# d1
python launch_online_dp.py --dp-size 8 --tp-size 4 --dp-size-local 4 --dp-rank-start 4 --dp-address 141.xx.xx.3 --dp-rpc-port 12321 --vllm-start-port 7100
```

### 11. Kimi-K2.6 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
python load_balance_proxy_server_example.py \
  --port 1999 \
  --host 141.xx.xx.1 \
  --prefiller-hosts \
    141.xx.xx.1 \
    141.xx.xx.1 \
    141.xx.xx.1 \
    141.xx.xx.1 \
    141.xx.xx.2 \
    141.xx.xx.2 \
    141.xx.xx.2 \
    141.xx.xx.2 \
  --prefiller-ports \
    7100 7101 7102 7103 7100 7101 7102 7103 \
  --decoder-hosts \
    141.xx.xx.3 \
    141.xx.xx.3 \
    141.xx.xx.3 \
    141.xx.xx.3 \
    141.xx.xx.4 \
    141.xx.xx.4 \
    141.xx.xx.4 \
    141.xx.xx.4 \
  --decoder-ports \
    7100 7101 7102 7103 \
    7100 7101 7102 7103 \
```

### 12. Kimi-K2.6 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
cd vllm-ascend/examples/disaggregated_prefill_v1/
bash proxy.sh
```

### 13. Kimi-K2.6 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```bash
curl http://141.xx.xx.1:1999/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "kimi_k26",
        "messages": [{
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": "The future of AI is"
            }]
        }],
        "max_tokens": 1024,
        "temperature": 1.0,
        "top_p": 0.95
    }'
```

### 14. Kimi-K2.6 > 5 Online Service Deployment > 5.2 Multi-Node PD Separation Deployment

```json
{
    "id": "chatcmpl-xxxxxxxxxxxxx",
    "object": "chat.completion",
    "model": "kimi_k26",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "The future of AI is not a destination we are passively approaching...",
                "finish_reason": "length"
            }
        }
    ],
    "usage": {
        "prompt_tokens": 13,
        "total_tokens": 1037,
        "completion_tokens": 1024
    }
}
```

### 15. Kimi-K2.6 > 6 Functional Verification

```bash
curl http://<node0_ip>:<port>/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "kimi_k26",
        "messages": [{
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": "The future of AI is"
            }]
        }],
        "max_tokens": 1024,
        "temperature": 1.0,
        "top_p": 0.95
    }'
```

### 16. Kimi-K2.6 > 6 Functional Verification

```json
{
    "id": "chatcmpl-9df13fd5e539af93",
    "object": "chat.completion",
    "created": 1780971952,
    "model": "kimi_k26",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "The future of AI is not a destination we are passively approaching, but a design problem we are actively solving right now...",
                "reasoning": "The user is asking for my thoughts on...",
                "finish_reason": "length"
            }
        }
    ],
    "usage": {
        "prompt_tokens": 13,
        "total_tokens": 1037,
        "completion_tokens": 1024
    }
}
```
