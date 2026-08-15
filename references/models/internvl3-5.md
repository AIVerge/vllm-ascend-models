# InternVL3.5

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/InternVL3.5.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 5
- `vllm serve` snippets: 2
- API or client verification snippets: 1

## Snippets

### 1. InternVL3.5(InternVL3_5-38B/241B-A28B) > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-a3
export NAME=vllm-ascend

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
-v /root/.cache:/root/.cache \
-it $IMAGE bash
```

### 2. InternVL3.5(InternVL3_5-38B/241B-A28B) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl -w vm.swappiness=0
sysctl -w kernel.numa_balancing=0
sysctl -w kernel.sched_migration_cost_ns=50000

export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export VLLM_ASCEND_ENABLE_FUSED_MC2=1
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export TASK_QUEUE_ENABLE=1
export HCCL_OP_EXPANSION_MODE="AIV"
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export VLLM_USE_V1=1
export VLLM_TORCH_PROFILER_WITH_STACK=0
export HCCL_BUFFSIZE=1536

vllm serve /root/.cache/modelscope/hub/models/vllm-ascend/InternVL3_5-38B-w8a8/ \
    --port 2002 \
    --served-model-name internvl3_5 \
    --trust-remote-code \
    --max-model-len 40960 \
    --max-num-batched-tokens 16384 \
    --tensor-parallel-size 4 \
    --max-num-seqs 32 \
    --gpu-memory-utilization 0.9 \
    --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY", "cudagraph_capture_sizes":[4,32,64,128,192,256,512]}' \
    --additional-config '{"enable_weight_nz_layout": true, "enable_cpu_binding": true}' \
    --mm-processor-cache-gb 0 \
    --enable-chunked-prefill \
    --safetensors-load-strategy 'prefetch' \
    --allowed-local-media-path "/"
```

### 3. InternVL3.5(InternVL3_5-38B/241B-A28B) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
sysctl -w vm.swappiness=0
sysctl -w kernel.numa_balancing=0
sysctl -w kernel.sched_migration_cost_ns=50000

export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export VLLM_ASCEND_ENABLE_FUSED_MC2=1
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export TASK_QUEUE_ENABLE=1
export HCCL_OP_EXPANSION_MODE="AIV"
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export VLLM_USE_V1=1
export VLLM_TORCH_PROFILER_WITH_STACK=0
export HCCL_BUFFSIZE=1536

vllm serve /root/.cache/modelscope/hub/models/vllm-ascend/InternVL3_5-241B-A28B-w8a8/ \
    --port 2001 \
    --served-model-name internvl3_5 \
    --trust-remote-code \
    --max-model-len 40960 \
    --max-num-batched-tokens 4096 \
    --tensor-parallel-size 4 \
    --data-parallel-size 2 \
    --max-num-seqs 70 \
    --gpu-memory-utilization 0.9 \
    --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
    --additional-config '{"enable_weight_nz_layout": true, "enable_cpu_binding": true}' \
    --mm-processor-cache-gb 0 \
    --enable-chunked-prefill \
    --enable-expert-parallel \
    --safetensors-load-strategy 'prefetch' \
    --allowed-local-media-path "/"
```

### 4. InternVL3.5(InternVL3_5-38B/241B-A28B) > 6 Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
    "model": "internvl3_5",
    "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": "https://modelscope.oss-cn-beijing.aliyuncs.com/resource/tiger.jpeg"}},
        {"type": "text", "text": "What is the text in the illustration?"}
    ]}
    ]
    }'
```

### 5. InternVL3.5(InternVL3_5-38B/241B-A28B) > 6 Functional Verification

```json
{"id":"chatcmpl-d3270d4a16cb4b98936f71ee3016451f","object":"chat.completion","created":1764924127,"model":"internvl3_5","choices":[{"index":0,"message":{"role":"assistant","content":"The text in the illustration is: **a tiger**","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning_content":null},"logprobs":null,"finish_reason":"stop","stop_reason":null,"token_ids":null}],"service_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":107,"total_tokens":123,"completion_tokens":16,"prompt_tokens_details":null},"prompt_logprobs":null,"prompt_token_ids":null,"kv_transfer_params":null}
```
