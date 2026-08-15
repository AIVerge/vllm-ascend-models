# Dots3 Note

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Dots3-Note.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 19
- `vllm serve` snippets: 4
- API or client verification snippets: 4

## Snippets

### 1. Dots3 Note > 4 Installation > 4.2 Image Acquisition and Build

```bash
export IMAGE=quay.io/ascend/vllm-ascend:dots3-note-prev-a3-openeuler
docker pull "$IMAGE"
```

### 2. Dots3 Note > 4 Installation > 4.2 Image Acquisition and Build

```bash
export HOST_MODEL_PATH=/path/to/dots3_note
test -d "$HOST_MODEL_PATH"
```

### 3. Dots3 Note > 4 Installation > 4.2 Image Acquisition and Build

```bash
docker run -it --rm \
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
    -v "$HOST_MODEL_PATH":/models/dots3_note:ro \
    "$IMAGE" bash
```

### 4. Dots3 Note > 4 Installation > 4.2 Image Acquisition and Build

```bash
export MODEL_PATH=/models/dots3_note
export SERVED_NAME=dots3_note
```

### 5. Dots3 Note > 4 Installation > 4.2 Image Acquisition and Build

```bash
npu-smi info
python -c "import vllm, vllm_ascend, torch_npu; print(vllm.__version__)"
pip show vllm vllm-ascend torch-npu
test -d "$MODEL_PATH"
```

### 6. Dots3 Note > 4 Installation > 4.3 Environment Variables

```bash
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
export LD_PRELOAD=/usr/lib64/libjemalloc.so.2
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export TASK_QUEUE_ENABLE=1
export CPU_AFFINITY_CONF=1
export HCCL_OP_EXPANSION_MODE=AIV
```

### 7. Dots3 Note > 4 Installation > 4.3 Environment Variables

```bash
test -f /usr/lib64/libjemalloc.so.2
echo "$ASCEND_RT_VISIBLE_DEVICES"
```

### 8. Dots3 Note > 5 Online Service Deployment > 5.1 Deployment Modes

```bash
test -d "$MODEL_PATH"
npu-smi info
```

### 9. Dots3 Note > 5 Online Service Deployment > 5.1 Deployment Modes

```bash
pgrep -af 'VLLM::Worker|vllm serve'
pkill -TERM -f 'VLLM::Worker'

# Last resort when the process still cannot exit
pkill -9 -f VLLM::Worker
```

### 10. Dots3 Note > 5 Online Service Deployment > 5.2 text-only Online Deployment

```bash
vllm serve "$MODEL_PATH" \
    --served-model-name "$SERVED_NAME" \
    --tensor-parallel-size 16 \
    --enable-expert-parallel \
    --speculative-config \
      '{"method":"mtp","num_speculative_tokens":3,"enforce_eager":true}' \
    --additional-config \
      '{"enable_flashcomm1":true,"enable_fused_mc2":1}' \
    --max-model-len 32768 \
    --gpu-memory-utilization 0.92 \
    --safetensors-load-strategy lazy \
    --enable-prefix-caching \
    --enable-chunked-prefill \
    --async-scheduling \
    --language-model-only \
    --max-num-batched-tokens 8192 \
    --max-num-seqs 4 \
    --default-chat-template-kwargs '{"enable_thinking":false}' \
    --generation-config vllm \
    --compilation-config \
      '{"mode":"VLLM_COMPILE","cudagraph_mode":"FULL_DECODE_ONLY","cudagraph_capture_sizes":[16],"max_cudagraph_capture_size":16}' \
    --port 8000
```

### 11. Dots3 Note > 5 Online Service Deployment > 5.3 image Online Deployment

```bash
export MEDIA_DIR=/path/to/local-image-root   # Local image media root directory (whitelist)
test -d "$MEDIA_DIR"
```

### 12. Dots3 Note > 5 Online Service Deployment > 5.3 image Online Deployment

```bash
vllm serve "$MODEL_PATH" \
    --served-model-name "$SERVED_NAME" \
    --tensor-parallel-size 16 \
    --enable-expert-parallel \
    --additional-config \
      '{"enable_flashcomm1":true,"enable_fused_mc2":1}' \
    --max-model-len 32768 \
    --kv-cache-memory-bytes 2816M \
    --safetensors-load-strategy lazy \
    --enable-prefix-caching \
    --enable-chunked-prefill \
    --async-scheduling \
    --allowed-local-media-path "$MEDIA_DIR" \
    --limit-mm-per-prompt '{"image":7,"video":0,"audio":0}' \
    --mm-processor-cache-gb 0 \
    --mm-encoder-tp-mode data \
    --skip-mm-profiling \
    --max-num-batched-tokens 1024 \
    --max-num-seqs 16 \
    --generation-config vllm \
    --compilation-config \
      '{"mode":"VLLM_COMPILE","cudagraph_mode":"FULL_DECODE_ONLY","cudagraph_capture_sizes":[16]}' \
    --port 8000
```

### 13. Dots3 Note > 5 Online Service Deployment > 5.4 audio Online Deployment

```bash
export MEDIA_ROOT=/path/to/local-audio-root   # Local audio media root directory (whitelist)
test -d "$MEDIA_ROOT"
```

### 14. Dots3 Note > 5 Online Service Deployment > 5.4 audio Online Deployment

```bash
vllm serve "$MODEL_PATH" \
    --served-model-name "$SERVED_NAME" \
    --tensor-parallel-size 16 \
    --enable-expert-parallel \
    --speculative-config \
      '{"method":"mtp","num_speculative_tokens":3,"enforce_eager":true}' \
    --additional-config \
      '{"enable_flashcomm1":true,"enable_fused_mc2":1}' \
    --max-model-len 4096 \
    --kv-cache-memory-bytes 4G \
    --safetensors-load-strategy lazy \
    --enable-prefix-caching \
    --enable-chunked-prefill \
    --async-scheduling \
    --limit-mm-per-prompt '{"image":0,"video":0,"audio":1}' \
    --allowed-local-media-path "$MEDIA_ROOT" \
    --mm-encoder-tp-mode data \
    --max-num-batched-tokens 4096 \
    --max-num-seqs 4 \
    --default-chat-template-kwargs '{"enable_thinking":false}' \
    --generation-config vllm \
    --compilation-config \
      '{"mode":"VLLM_COMPILE","cudagraph_mode":"FULL_DECODE_ONLY","cudagraph_capture_sizes":[4,8,16],"max_cudagraph_capture_size":16}' \
    --port 8000
```

### 15. Dots3 Note > 5 Online Service Deployment > 5.6 Service Verification

```bash
GPU KV cache size: <tokens>
Maximum concurrency for ... tokens per request: ...
Graph capturing finished ...
Application startup complete.
```

### 16. Dots3 Note > 5 Online Service Deployment > 5.6 Service Verification

```bash
curl -sf http://127.0.0.1:8000/v1/models
```

### 17. Dots3 Note > 6 Functional Verification > 6.1 text-only

```bash
curl http://127.0.0.1:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "dots3_note",
        "messages": [{"role": "user", "content": "What is the capital of France?"}],
        "temperature": 0,
        "max_tokens": 640
    }'
```

### 18. Dots3 Note > 6 Functional Verification > 6.2 image

```bash
curl http://127.0.0.1:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "dots3_note",
        "messages": [{
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": "file:///path/to/image.png"}},
                {"type": "text", "text": "What is shown in this image?"}
            ]
        }],
        "temperature": 0,
        "max_tokens": 256
    }'
```

### 19. Dots3 Note > 6 Functional Verification > 6.3 audio

```bash
curl -s http://127.0.0.1:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d @<(printf '{
        "model":"dots3_note",
        "messages":[{
            "role":"user",
            "content":[
                {"type":"audio_url","audio_url":{"url":"data:audio/wav;base64,'; base64 -w0 /path/to/audio.wav; printf '"}},
                {"type":"text","text":"What does the speaker say?"}
            ]
        }],
        "temperature":0,
        "max_tokens":1024
    }')
```
