# Qwen3.5-Dense (2B/4B/9B)

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3.5-Dense.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 12
- `vllm serve` snippets: 3
- API or client verification snippets: 2

## Snippets

### 1. Qwen3.5-Dense (Qwen3.5-2B/4B/9B) > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=m.daocloud.io/quay.io/ascend/vllm-ascend:v0.22.1rc1-310p
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

### 2. Qwen3.5-Dense (Qwen3.5-2B/4B/9B) > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-310p

docker run --rm \
--privileged \
--name vllm-ascend \
--shm-size=10g \
--device=/dev/davinci0:/dev/davinci0 \
--device=/dev/davinci_manager \
--device=/dev/ascend_manager \
--device=/dev/user_config \
-v /etc/sys_version.conf:/etc/sys_version.conf \
-v /etc/ld.so.conf.d/mind_so.conf:/etc/ld.so.conf.d/mind_so.conf \
-v /etc/hdcBasic.cfg:/etc/hdcBasic.cfg \
-v /var/dmp_daemon:/var/dmp_daemon \
-v /usr/lib64/libmmpa.so:/usr/lib64/libmmpa.so \
-v /usr/lib64/libcrypto.so.1.1:/usr/lib64/libcrypto.so.1.1 \
-v /usr/local/sbin/npu-smi:/usr/local/sbin/npu-smi \
-v /usr/lib64/libstackcore.so:/usr/lib64/libstackcore.so \
-v /usr/lib/aarch64-linux-gnu/libyaml-0.so.2:/usr/lib64/libyaml-0.so.2 \
-v /etc/slog.conf:/etc/slog.conf \
-v /var/slogd:/var/slogd \
-v /usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64 \
-v /usr/lib64/libtensorflow.so:/usr/lib64/libtensorflow.so \
-v /root/.cache:/root/.cache \
-p 8080:8080 \
-it $IMAGE bash
```

### 3. Qwen3.5-Dense (Qwen3.5-2B/4B/9B) > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-310p-openeuler

docker run --rm \
--privileged \
--name vllm-ascend \
--shm-size=10g \
--device=/dev/davinci0:/dev/davinci0 \
--device=/dev/davinci_manager \
--device=/dev/ascend_manager \
--device=/dev/user_config \
-v /etc/sys_version.conf:/etc/sys_version.conf \
-v /etc/ld.so.conf.d/mind_so.conf:/etc/ld.so.conf.d/mind_so.conf \
-v /etc/hdcBasic.cfg:/etc/hdcBasic.cfg \
-v /var/dmp_daemon:/var/dmp_daemon \
-v /usr/lib64/libsemanage.so.2:/usr/lib64/libsemanage.so.2 \
-v /usr/lib64/libmmpa.so:/usr/lib64/libmmpa.so \
-v /usr/lib64/libcrypto.so.1.1:/usr/lib64/libcrypto.so.1.1 \
-v /usr/lib64/libyaml-0.so.2.0.9:/usr/lib64/libyaml-0.so.2 \
-v /usr/local/sbin/npu-smi:/usr/local/sbin/npu-smi \
-v /usr/lib64/libstackcore.so:/usr/lib64/libstackcore.so \
-v /etc/slog.conf:/etc/slog.conf \
-v /var/slogd:/var/slogd \
-v /usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64 \
-v /usr/lib64/libtensorflow.so:/usr/lib64/libtensorflow.so \
-v /root/.cache:/root/.cache \
-p 8080:8080 \
-it $IMAGE bash
```

### 4. Qwen3.5-Dense (Qwen3.5-2B/4B/9B) > 4 Installation > 4.2 Source Code Installation

```bash
git clone https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
pip install -e .
```

### 5. Qwen3.5-Dense (Qwen3.5-2B/4B/9B) > 4 Installation > 4.2 Source Code Installation

```bash
pip uninstall -y triton-ascend triton
```

### 6. Qwen3.5-Dense (Qwen3.5-2B/4B/9B) > 4 Installation > 4.2 Source Code Installation

```bash
pip show vllm-ascend
```

### 7. Qwen3.5-Dense (Qwen3.5-2B/4B/9B) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
#!/bin/sh
# Load model from ModelScope to speed up download
export VLLM_USE_MODELSCOPE=True

# Model weight path; can be a ModelScope model id or a local directory path
export MODEL_PATH=Qwen/Qwen3.5-2B

vllm serve $MODEL_PATH \
--host 127.0.0.1 \
--port 1025 \
--tensor-parallel-size 1 \
--served-model-name qwen3.5 \
--max-num-seqs 32 \
--max-model-len 16384 \
--trust-remote-code \
--gpu-memory-utilization 0.90 \
--mamba-ssm-cache-dtype float16 \
--dtype float16 \
--speculative-config '{"method": "qwen3_5_mtp","num_speculative_tokens":1}' \
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,2,4,8,16]}' \
--additional-config '{"ascend_compilation_config": {"enable_npugraph_ex": false}}'
```

### 8. Qwen3.5-Dense (Qwen3.5-2B/4B/9B) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
#!/bin/sh
# Load model from ModelScope to speed up download
export VLLM_USE_MODELSCOPE=True

# Model weight path; can be a ModelScope model id or a local directory path
export MODEL_PATH=Qwen/Qwen3.5-4B

vllm serve $MODEL_PATH \
--host 127.0.0.1 \
--port 1025 \
--tensor-parallel-size 1 \
--served-model-name qwen3.5 \
--max-num-seqs 32 \
--max-model-len 16384 \
--trust-remote-code \
--gpu-memory-utilization 0.90 \
--mamba-ssm-cache-dtype float16 \
--dtype float16 \
--speculative-config '{"method": "qwen3_5_mtp","num_speculative_tokens":1}' \
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,2,4,8,16]}' \
--additional-config '{"ascend_compilation_config": {"enable_npugraph_ex": false}}'
```

### 9. Qwen3.5-Dense (Qwen3.5-2B/4B/9B) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
#!/bin/sh
# Load model from ModelScope to speed up download
export VLLM_USE_MODELSCOPE=True

# Model weight path; can be a ModelScope model id or a local directory path
export MODEL_PATH=Qwen/Qwen3.5-9B

vllm serve $MODEL_PATH \
--host 127.0.0.1 \
--port 1025 \
--tensor-parallel-size 1 \
--served-model-name qwen3.5 \
--max-num-seqs 32 \
--max-model-len 16384 \
--trust-remote-code \
--gpu-memory-utilization 0.90 \
--mamba-ssm-cache-dtype float16 \
--dtype float16 \
--speculative-config '{"method": "qwen3_5_mtp","num_speculative_tokens":1}' \
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,2,4,8,16]}' \
--additional-config '{"ascend_compilation_config": {"enable_npugraph_ex": false}}'
```

### 10. Qwen3.5-Dense (Qwen3.5-2B/4B/9B) > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
(APIServer pid=<pid>) INFO:     Started server process [<pid>]
(APIServer pid=<pid>) INFO:     Waiting for application startup.
(APIServer pid=<pid>) INFO:     Application startup complete.
```

### 11. Qwen3.5-Dense (Qwen3.5-2B/4B/9B) > 6 Functional Verification

```bash
curl http://127.0.0.1:1025/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen3.5",
        "prompt": "The future of AI is",
        "max_completion_tokens": 50,
        "temperature": 0
    }'
```

### 12. Qwen3.5-Dense (Qwen3.5-2B/4B/9B) > 6 Functional Verification

```bash
curl http://127.0.0.1:1025/v1/chat/completions \
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
