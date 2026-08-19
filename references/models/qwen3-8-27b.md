# Qwen3.8-27B

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3.8-27B.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 10
- `vllm serve` snippets: 4
- API or client verification snippets: 2

## Snippets

### 1. Qwen3.8-27B > 4 Installation > 4.1 Docker Image Installation

```bash
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

### 2. Qwen3.8-27B > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-a5
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
    -v /usr/lib64:/usr/lib64 \
    -it $IMAGE bash
```

### 3. Qwen3.8-27B > 4 Installation > 4.1 Docker Image Installation

```bash
python -c "import vllm, vllm_ascend; print('vllm and vllm_ascend are ready')"
```

### 4. Qwen3.8-27B > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

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

# Model weight path; can be a ModelScope model id (e.g., Eco-Tech/Qwen3.8-27B-w8a8) or a local directory path
export MODEL_PATH=Eco-Tech/Qwen3.8-27B-w8a8

vllm serve $MODEL_PATH \
    --host 0.0.0.0 \
    --port 8000 \
    --data-parallel-size 1 \
    --tensor-parallel-size 2 \
    --quantization ascend \
    --served-model-name qwen3.8 \
    --max-num-seqs 32 \
    --max-model-len 131072 \
    --max-num-batched-tokens 16384 \
    --trust-remote-code \
    --enable-prefix-caching \
    --gpu-memory-utilization 0.85 \
    --speculative-config '{"method": "qwen3_5_mtp", "num_speculative_tokens": 3, "enforce_eager": true}' \
    --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
    --additional-config '{"enable_cpu_binding":true}'
```

### 5. Qwen3.8-27B > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

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

# Model weight path; can be a ModelScope model id (e.g., Eco-Tech/Qwen3.8-27B-w8a8-mxfp8) or a local directory path
export MODEL_PATH=Eco-Tech/Qwen3.8-27B-w8a8-mxfp8

vllm serve $MODEL_PATH \
    --host 0.0.0.0 \
    --port 8000 \
    --data-parallel-size 1 \
    --tensor-parallel-size 1 \
    --quantization ascend \
    --served-model-name qwen3.8 \
    --max-num-seqs 32 \
    --max-model-len 131072 \
    --max-num-batched-tokens 16384 \
    --trust-remote-code \
    --enable-prefix-caching \
    --gpu-memory-utilization 0.85 \
    --speculative-config '{"method": "qwen3_5_mtp", "num_speculative_tokens": 3, "enforce_eager": true}' \
    --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
    --additional-config '{"enable_cpu_binding":true}'
```

### 6. Qwen3.8-27B > 6 Functional Verification

```bash
curl http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen3.8",
        "prompt": "The future of AI is",
        "max_tokens": 50,
        "temperature": 0.7
    }'
```

### 7. Qwen3.8-27B > 6 Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen3.8",
        "messages": [
            {"role": "user", "content": "The future of AI is"}
        ],
        "max_completion_tokens": 1024,
        "temperature": 1.0,
        "top_p": 0.95
    }'
```

### 8. Qwen3.8-27B > 6 Functional Verification

```json
{
    "id": "cmpl-xxxxxxxxxxxxx",
    "object": "text_completion",
    "created": 1780971952,
    "model": "qwen3.8",
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

### 9. Tuned Single-Node Deployment — 2 NPU (recommended)

Operator-tuned parameter set for Qwen3.8-27B (w8a8) on Ascend 910B. **2 NPU cards are sufficient** (`--tensor-parallel-size 2`); the parameters below are raised for long context (256K) and higher throughput compared to the stock tutorial snippet (snippet 4). Includes the performance-critical flags that must not be dropped: `--enable-prefix-caching`, `--speculative-config` (qwen3_5_mtp), `--compilation-config` (FULL_DECODE_ONLY), `--additional-config` (cpu binding), plus tool calling and Qwen3 thinking-mode parsing.

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

# Model weight path; can be a ModelScope model id (e.g., Eco-Tech/Qwen3.8-27B-w8a8) or a local directory path
export MODEL_PATH=Eco-Tech/Qwen3.8-27B-w8a8

vllm serve $MODEL_PATH \
    --host 0.0.0.0 \
    --port 8000 \
    --data-parallel-size 1 \
    --tensor-parallel-size 2 \
    --served-model-name qwen3.8 \
    --max-model-len 262144 \
    --max-num-batched-tokens 32768 \
    --max-num-seqs 16 \
    --gpu-memory-utilization 0.90 \
    --trust-remote-code \
    --enable-prefix-caching \
    --enable-auto-tool-choice \
    --tool-call-parser qwen3_coder \
    --reasoning-parser qwen3 \
    --speculative-config '{"method": "qwen3_5_mtp", "num_speculative_tokens": 3, "enforce_eager": true}' \
    --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
    --additional-config '{"enable_cpu_binding":true}'
```

### 10. Tuned Single-Node Deployment — 4 NPU (verified in production)

Same tuned parameter set scaled to `--tensor-parallel-size 4`, as verified in the production deployment (Ascend 910B, 4 NPU). Use this variant only when extra KV-cache/context headroom is required; **2 NPU cards are enough for the default 256K-context service**.

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

# Model weight path; can be a ModelScope model id (e.g., Eco-Tech/Qwen3.8-27B-w8a8) or a local directory path
export MODEL_PATH=Eco-Tech/Qwen3.8-27B-w8a8

vllm serve $MODEL_PATH \
    --host 0.0.0.0 \
    --port 8000 \
    --data-parallel-size 1 \
    --tensor-parallel-size 4 \
    --served-model-name qwen3.8 \
    --max-model-len 262144 \
    --max-num-batched-tokens 32768 \
    --max-num-seqs 16 \
    --gpu-memory-utilization 0.90 \
    --trust-remote-code \
    --enable-prefix-caching \
    --enable-auto-tool-choice \
    --tool-call-parser qwen3_coder \
    --reasoning-parser qwen3 \
    --speculative-config '{"method": "qwen3_5_mtp", "num_speculative_tokens": 3, "enforce_eager": true}' \
    --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
    --additional-config '{"enable_cpu_binding":true}'
```

## Tuned Deployment Notes

- The tuned snippets (9, 10) mirror the production GPUStack deployment parameters for `qwen3.8-27b-2npu` (vLLM Ascend v0.22.1rc1-custom): raised `--max-model-len 262144`, `--max-num-batched-tokens 32768`, `--max-num-seqs 16`, `--gpu-memory-utilization 0.90`, plus tool calling (`--enable-auto-tool-choice`, `--tool-call-parser qwen3_coder`) and Qwen3 thinking-mode parsing (`--reasoning-parser qwen3`).
- Do not drop the performance flags: `--enable-prefix-caching`, `--speculative-config '{"method": "qwen3_5_mtp", ...}'`, `--compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}'`, `--additional-config '{"enable_cpu_binding":true}'`, and the env vars `PYTORCH_NPU_ALLOC_CONF=expandable_segments:True`, `HCCL_BUFFSIZE=512`, `OMP_PROC_BIND=false`, `OMP_NUM_THREADS=1`.
- GPUStack injects `--enable-prompt-tokens-details`, `--served-model-name=<model>`, `--host`/`--port` automatically; served model name on the managed instance is `qwen3.8-27b-2npu`.
