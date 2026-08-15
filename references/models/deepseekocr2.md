# DeepSeekOCR2

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/DeepSeekOCR2.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 5
- `vllm serve` snippets: 1
- API or client verification snippets: 1

## Snippets

### 1. DeepSeek-OCR-2 > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=m.daocloud.io/quay.io/ascend/vllm-ascend:v0.22.1rc1
export NAME=vllm-ascend

# Run the container using the defined variables
# Note: If you are running bridge network with docker, please expose available ports for multiple nodes communication in advance.
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

### 2. DeepSeek-OCR-2 > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=m.daocloud.io/quay.io/ascend/vllm-ascend:v0.22.1rc1
export NAME=vllm-ascend

# Run the container using the defined variables
# Note: If you are running bridge network with docker, please expose available ports for multiple nodes communication in advance.
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

### 3. DeepSeek-OCR-2 > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
#!/bin/sh

export VLLM_USE_V1=1
export VLLM_ASCEND_ENABLE_NZ=0
export TOKENIZERS_PARALLELISM=false
export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"
export TASK_QUEUE_ENABLE=1
export TOKENIZERS_PARALLELISM=false

vllm serve /root/.cache/DeepSeek-OCR-2 \
    --served-model-name deepseekocr2 \
    --trust-remote-code \
    --tensor-parallel-size 1  \
    --port 1055 \
    --max_model_len 8192 \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.8 \
    --allowed-local-media-path / \
    --additional-config '{
      "enable_cpu_binding": true,
      "multistream_overlap_shared_expert": true,
      "ascend_compilation_config": {"fuse_qknorm_rope": false}
    }' \
    --mm-processor-cache-gb 0
```

### 4. DeepSeek-OCR-2 > 6 Functional Verification

```bash
INFO:     Started server process [87471]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 5. DeepSeek-OCR-2 > 6 Functional Verification

```bash
curl http://<node0_ip>:<port>/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "deepseekocr2",
        "prompt": "The future of AI is",
        "max_completion_tokens": 50,
        "temperature": 0
    }'
```
