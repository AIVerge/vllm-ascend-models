# Qwen3-ASR-1.7B

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3-ASR-1.7B.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 8
- `vllm serve` snippets: 2
- API or client verification snippets: 1

## Snippets

### 1. Qwen3-ASR-1.7B > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1

docker run --rm \
    --name vllm-ascend \
    --shm-size=1g \
    --net host \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64 \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /root/.cache:/root/.cache \
    -it -d $IMAGE bash
```

### 2. Qwen3-ASR-1.7B > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-310p

docker run --rm \
    --name vllm-ascend \
    --shm-size=10g \
    --net host \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64 \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /root/.cache:/root/.cache \
    -it -d $IMAGE bash
```

### 3. Qwen3-ASR-1.7B > 4 Installation > 4.1 Docker Image Installation

```bash
docker ps --filter name=vllm-ascend
pip show vllm vllm-ascend
```

### 4. Qwen3-ASR-1.7B > 4 Installation > 4.2 Source Code Installation

```bash
pip uninstall -y triton-ascend triton
```

### 5. Qwen3-ASR-1.7B > 4 Installation > 4.2 Source Code Installation

```bash
pip show vllm-ascend
```

### 6. Qwen3-ASR-1.7B > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
vllm serve your_model_path \
  --served-model-name qwen3-asr \
  --tensor-parallel-size 1 \
  --max-model-len 4096 \
  --gpu-memory-utilization 0.9 \
  --enforce-eager \
  --port 8000
```

### 7. Qwen3-ASR-1.7B > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
vllm serve your_model_path \
  --served-model-name qwen3-asr \
  --tensor-parallel-size 1 \
  --gpu-memory-utilization 0.9 \
  --dtype float16 \
  --max-model-len 4096 \
  --additional-config '{"ascend_compilation_config": {"fuse_norm_quant": false,"enable_npu_graph_ex":false}}' \
  --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,4]}' \
  --port 8000
```

### 8. Qwen3-ASR-1.7B > 6 Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen3-asr",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "audio_url",
                        "audio_url": {
                            "url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-ASR-Repo/asr_en.wav"
                        }
                    }
                ]
            }
        ]
    }'
```
