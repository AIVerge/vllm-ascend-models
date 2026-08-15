# Qwen-VL-Dense

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen-VL-Dense.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 15
- `vllm serve` snippets: 3
- API or client verification snippets: 1

## Snippets

### 1. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:|vllm_ascend_version|-#TODO
export NAME=vllm-ascend

docker run --rm \
--name $NAME \
--net=host \
--shm-size=1g \
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
--device /dev/hisi_hdc \
--device /dev/ummu \
--device /dev/uburma \
-v /usr/local/Ascend/driver:/usr/local/Ascend/driver \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /etc/hccl_rootinfo.json:/etc/hccl_rootinfo.json \
-v /etc/hixlep/:/etc/hixlep/ \
-v /root/.cache:/root/.cache \
-v /usr/local/sbin:/usr/local/sbin \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/sbin/npu-smi:/usr/local/sbin/npu-smi \
-v /usr/bin/urma_admin:/usr/bin/urma_admin \
-v /lib/route.conf:/lib/route.conf \
-v /usr/lib64:/usr/lib64 \
-itd $IMAGE bash
```

### 2. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 4 Installation > 4.1 Docker Image Installation

```bash
# Update the vllm-ascend image
# A2: quay.io/ascend/vllm-ascend:v0.22.1rc1
# A3: quay.io/ascend/vllm-ascend:v0.22.1rc1-a3
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1

docker run --rm \
--name vllm-ascend \
--shm-size=1g \
--device /dev/davinci0 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-p 8000:8000 \
-it $IMAGE bash
```

### 3. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 4 Installation > 4.1 Docker Image Installation

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
-p 8000:8000 \
-it $IMAGE bash
```

### 4. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 4 Installation > 4.1 Docker Image Installation

```bash
docker ps | grep vllm-ascend
```

### 5. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 4 Installation > 4.1 Docker Image Installation

```bash
pip show vllm-ascend
```

### 6. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 4 Installation > 4.2 Source Code Installation

```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm
pip install -e .
```

### 7. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 4 Installation > 4.2 Source Code Installation

```bash
git clone https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
pip install -e .
```

### 8. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 4 Installation > 4.2 Source Code Installation

```bash
pip uninstall -y triton-ascend triton
```

### 9. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 4 Installation > 4.2 Source Code Installation

```bash
pip show vllm vllm-ascend
```

### 10. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export TASK_QUEUE_ENABLE=1
export ASCEND_RT_VISIBLE_DEVICES=$1

vllm serve Qwen/Qwen3-VL-8B-Instruct \
  --host 0.0.0.0 \
  --port $2 \
  --quantization ascend \
  --served-model-name qwen3vl \
  --no-enable-prefix-caching \
  --data-parallel-size $3 \
  --tensor-parallel-size $4 \
  --trust-remote-code \
  --max-num-seqs 128 \
  --max-model-len 32768 \
  --max-num-batched-tokens 16384 \
  --gpu-memory-utilization 0.91 \
  --async-scheduling \
  --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,2,4,8,16,32]}' \
  --mm-processor-cache-gb 0
```

### 11. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export TASK_QUEUE_ENABLE=1
export ASCEND_RT_VISIBLE_DEVICES=$1

vllm serve Qwen/Qwen3-VL-8B-Instruct \
--host 0.0.0.0 \
--port $2 \
--dtype bfloat16 \
--served-model-name qwen3vl \
--no-enable-prefix-caching \
--data-parallel-size $3 \
--tensor-parallel-size $4 \
--trust-remote-code \
--max-num-seqs 128 \
--max-model-len 32768 \
--max-num-batched-tokens 16384 \
--gpu-memory-utilization 0.91 \
--async-scheduling \
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,2,4,8,16,32]}' \
--mm-processor-cache-gb 0
```

### 12. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export TASK_QUEUE_ENABLE=1
export ASCEND_RT_VISIBLE_DEVICES=$1

vllm serve Qwen/Qwen3-VL-8B-Instruct \
--dtype float16 \
--max_model_len 16384 \
--host 0.0.0.0 \
--port $2 \
--dtype bfloat16 \
--served-model-name qwen3vl \
--no-enable-prefix-caching \
--data-parallel-size $3 \
--tensor-parallel-size $4 \ 
--trust-remote-code \
--max-num-seqs 128 \
--max-model-len 32768 \
--max-num-batched-tokens 16384 \
--gpu-memory-utilization 0.91 \
--async-scheduling \
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,2,4,8,16,32]}' \
--additional-config '{"ascend_compilation_config": {"enable_npugraph_ex":false}}' \
--mm-processor-cache-gb 0
```

### 13. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
INFO:     Started server process [2736]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 14. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 6 Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
    "model": "Qwen/Qwen3-VL-8B-Instruct",
    "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": "https://modelscope.oss-cn-beijing.aliyuncs.com/resource/qwen.png"}},
        {"type": "text", "text": "What is the text in the illustration?"}
    ]}
    ]
    }'
```

### 15. Qwen-VL-Dense(Qwen3-VL-8B/32B) > 6 Functional Verification

```json
{"id":"chatcmpl-d3270d4a16cb4b98936f71ee3016451f","object":"chat.completion","created":1764924127,"model":"Qwen/Qwen3-VL-8B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"The text in the illustration is: **TONGYI Qwen**","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning_content":null},"logprobs":null,"finish_reason":"stop","stop_reason":null,"token_ids":null}],"service_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":107,"total_tokens":123,"completion_tokens":16,"prompt_tokens_details":null},"prompt_logprobs":null,"prompt_token_ids":null,"kv_transfer_params":null}
```
