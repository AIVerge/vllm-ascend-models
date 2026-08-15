# Qwen3-Dense

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3-Dense.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 15
- `vllm serve` snippets: 5
- API or client verification snippets: 1

## Snippets

### 1. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 4 Installation > 4.1 Docker Image Installation

```bash
docker pull quay.io/ascend/vllm-ascend:v0.22.1rc1
```

### 2. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-a3

docker run --rm \
    --name vllm-ascend-env \
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

### 3. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1

docker run --rm \
    --name vllm-ascend-env \
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

### 4. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 4 Installation > 4.1 Docker Image Installation

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

### 5. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 4 Installation > 4.1 Docker Image Installation

```bash
docker ps | grep vllm-ascend-env
```

### 6. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 4 Installation > 4.1 Docker Image Installation

```bash
pip show vllm-ascend
```

### 7. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 4 Installation > 4.2 Source Code Installation

```bash
pip uninstall -y triton-ascend triton
```

### 8. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 4 Installation > 4.2 Source Code Installation

```bash
pip show vllm-ascend
```

### 9. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export TASK_QUEUE_ENABLE=1
export HCCL_OP_EXPANSION_MODE="AIV"

vllm serve your_model_path \
    --served-model-name qwen3 \
    --trust-remote-code \
    --quantization ascend \
    --distributed-executor-backend mp \
    --tensor-parallel-size 4 \
    --max-model-len 5500 \
    --max-num-batched-tokens 40960 \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \
    --port <port> \
    --gpu-memory-utilization 0.9 \
    --additional-config '{"enable_flashcomm1": true}'
```

### 10. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
export ASCEND_RT_VISIBLE_DEVICES=0,1
export VLLM_USE_V1=1
export TASK_QUEUE_ENABLE=1
export HCCL_BUFFSIZE=1024
vllm serve your_model_path \
    --port 8004 \
    --data-parallel-size 1 \
    --tensor-parallel-size 2 \
    --served-model-name qwen3 \
    --distributed-executor-backend "mp" \
    --max-model-len 40960 \
    --max-num-batched-tokens 16384 \
    --max-num-seqs 64 \
    --trust-remote-code \
    --gpu-memory-utilization 0.9 \
    --quantization ascend \
    --compilation-config '{"cudagraph_capture_sizes": [64]}' \
    --additional-config '{"enable_flashcomm1": true, "ascend_compilation_config": {"fuse_norm_quant": false}}'
```

### 11. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
export VLLM_USE_MODELSCOPE=True
export ASCEND_RT_VISIBLE_DEVICES=0

vllm serve Eco-Tech/Qwen3-8B-w8a8sc-310-vllm/TP1/Qwen3-8B-w8a8sc-310-vllm-tp1 \
    --host 127.0.0.1 \
    --port 8080 \
    --tensor-parallel-size 1 \
    --gpu-memory-utilization 0.90 \
    --max-num-seqs 32 \
    --served-model-name qwen3 \
    --dtype float16 \
    --additional-config '{"ascend_compilation_config": {"enable_npugraph_ex":false}}' \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,2,4,8,16,32]}' \
    --quantization ascend \
    --max-model-len 20480 \
    --no-enable-prefix-caching \
    --load-format sharded_state
```

### 12. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
export VLLM_USE_MODELSCOPE=True
export ASCEND_RT_VISIBLE_DEVICES=0

vllm serve Eco-Tech/Qwen3-14B-w8a8sc-310-vllm/TP1/Qwen3-14B-w8a8sc-310-vllm-tp1 \
    --host 127.0.0.1 \
    --port 8080 \
    --tensor-parallel-size 1 \
    --gpu-memory-utilization 0.90 \
    --max-num-seqs 16 \
    --served-model-name qwen3 \
    --dtype float16 \
    --additional-config '{"ascend_compilation_config": {"enable_npugraph_ex":false}}' \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,2,4,8,16]}' \
    --quantization ascend \
    --max-model-len 20480 \
    --no-enable-prefix-caching \
    --load-format sharded_state
```

### 13. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
export VLLM_USE_MODELSCOPE=True
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3

vllm serve Eco-Tech/Qwen3-32B-w8a8sc-310-vllm/TP4/Qwen3-32B-w8a8sc-310-vllm-tp4 \
    --host 127.0.0.1 \
    --port 8080 \
    --tensor-parallel-size 4 \
    --gpu-memory-utilization 0.90 \
    --max-num-seqs 32 \
    --served-model-name qwen3 \
    --dtype float16 \
    --additional-config '{"ascend_compilation_config": {"enable_npugraph_ex":false}}' \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [16,32]}' \
    --quantization ascend \
    --max-model-len 20480 \
    --no-enable-prefix-caching \
    --load-format sharded_state
```

### 14. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
(APIServer pid=<pid>) INFO:     Started server process [<pid>]
(APIServer pid=<pid>) INFO:     Waiting for application startup.
(APIServer pid=<pid>) INFO:     Application startup complete.
```

### 15. Qwen3-Dense (Qwen3-0.6B/1.7B/4B/8B/14B/32B, W8A8, W4A4, W8A8SC-310) > 6 Functional Verification

```bash
curl http://localhost:<port>/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen3",
        "messages": [
            {"role": "user", "content": "Give me a short introduction to large language models."}
        ],
        "temperature": 0.6,
        "top_p": 0.95,
        "top_k": 20,
        "max_completion_tokens": 4096
    }'
```
