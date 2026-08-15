# PaddleOCR-VL

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/PaddleOCR-VL.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 12
- `vllm serve` snippets: 2
- API or client verification snippets: 1

## Snippets

### 1. PaddleOCR-VL > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1
docker run --rm \
    --name vllm-ascend \
    --shm-size=1g \
    --net=host \
    --device /dev/davinci0 \
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

### 2. PaddleOCR-VL > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1-310p
docker run --rm \
    --name vllm-ascend \
    --shm-size=1g \
    --net=host \
    --device /dev/davinci0 \
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

### 3. PaddleOCR-VL > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
#!/bin/sh
export VLLM_USE_MODELSCOPE=True
export MODEL_PATH="PaddlePaddle/PaddleOCR-VL"
export TASK_QUEUE_ENABLE=1
export CPU_AFFINITY_CONF=1
export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"

vllm serve ${MODEL_PATH} \
          --max-num-batched-tokens 16384 \
          --served-model-name PaddleOCR-VL-0.9B \
          --trust-remote-code \
          --no-enable-prefix-caching \
          --mm-processor-cache-gb 0 \
          --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
          --additional_config '{"enable_cpu_binding":true}' \
          --port 8000
```

### 4. PaddleOCR-VL > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
#!/bin/sh
export VLLM_USE_MODELSCOPE=True
export MODEL_PATH="PaddlePaddle/PaddleOCR-VL"
export TASK_QUEUE_ENABLE=1
export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"

vllm serve ${MODEL_PATH} \
          --max_model_len 16384 \
          --served-model-name PaddleOCR-VL-0.9B \
          --trust-remote-code \
          --no-enable-prefix-caching \
          --mm-processor-cache-gb 0 \
          --dtype float16 \
          --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
          --additional_config '{"enable_cpu_binding":true}' \
          --port 8000
```

### 5. PaddleOCR-VL > 5 Online Service Deployment > 5.3 Special Deployment Modes > 5.3.1 Offline Inference with vLLM and PP-DocLayoutV2

```bash
docker pull ccr-2vdh3abv-pub.cnc.bj.baidubce.com/device/paddle-npu:cann800-ubuntu20-npu-910b-base-aarch64-gcc84
```

### 6. PaddleOCR-VL > 5 Online Service Deployment > 5.3 Special Deployment Modes > 5.3.1 Offline Inference with vLLM and PP-DocLayoutV2

```bash
docker run -it --name paddle-npu-dev -v $(pwd):/work \
    --privileged --network=host --shm-size=128G -w=/work \
    -v /usr/local/Ascend/driver:/usr/local/Ascend/driver \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -e ASCEND_RT_VISIBLE_DEVICES="0,1,2,3,4,5,6,7" \
    ccr-2vdh3abv-pub.cnc.bj.baidubce.com/device/paddle-npu:cann800-ubuntu20-npu-910b-base-$(uname -m)-gcc84 /bin/bash
```

### 7. PaddleOCR-VL > 5 Online Service Deployment > 5.3 Special Deployment Modes > 5.3.1 Offline Inference with vLLM and PP-DocLayoutV2

```bash
python -m pip install paddlepaddle==3.2.0
wget https://paddle-whl.bj.bcebos.com/stable/npu/paddle-custom-npu/paddle_custom_npu-3.2.0-cp310-cp310-linux_aarch64.whl
pip install paddle_custom_npu-3.2.0-cp310-cp310-linux_aarch64.whl
python -m pip install -U "paddleocr[doc-parser]"
pip install safetensors
```

### 8. PaddleOCR-VL > 5 Online Service Deployment > 5.3 Special Deployment Modes > 5.3.1 Offline Inference with vLLM and PP-DocLayoutV2

```bash
The OpenCV component may be missing:

```bash
apt-get update
apt-get install -y libgl1 libglib2.0-0
```

CANN-8.0.0 does not support some versions of NumPy and OpenCV. It is recommended to install the specified versions.

```bash
python -m pip install numpy==1.26.4
python -m pip install opencv-python==3.4.18.65
```
```

### 9. PaddleOCR-VL > 5 Online Service Deployment > 5.3 Special Deployment Modes > 5.3.2 Using vLLM as the backend, combined with PP-DocLayoutV2 for offline inference

```python
from paddleocr import PaddleOCRVL

doclayout_model_path = "/path/to/your/PP-DocLayoutV2/"

pipeline = PaddleOCRVL(vl_rec_backend="vllm-server",
                       vl_rec_server_url="http://localhost:8000/v1",
                       layout_detection_model_name="PP-DocLayoutV2",
                       layout_detection_model_dir=doclayout_model_path,
                       device="npu")

output = pipeline.predict("https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/paddleocr_vl_demo.png")

for i, res in enumerate(output):
    res.save_to_json(save_path=f"output_{i}.json")
    res.save_to_markdown(save_path=f"output_{i}.md")
```

### 10. PaddleOCR-VL > 6 Functional Verification

```bash
INFO:     Started server process [87471]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 11. PaddleOCR-VL > 6 Functional Verification

```python
from openai import OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8000/v1",
    timeout=3600
)

# Task-specific base prompts
TASKS = {
    "ocr": "OCR:",
    "table": "Table Recognition:",
    "formula": "Formula Recognition:",
    "chart": "Chart Recognition:"
}

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://ofasys-multimodal-wlcb-3-toshanghai.oss-accelerate.aliyuncs.com/wpf272043/keepme/image/receipt.png"
                }
            },
            {
                "type": "text",
                "text": TASKS["ocr"]
            }
        ]
    }
]

response = client.chat.completions.create(
    model="PaddleOCR-VL-0.9B",
    messages=messages,
    temperature=0.0,
)
print(f"Generated text: {response.choices[0].message.content}")
```

### 12. PaddleOCR-VL > 6 Functional Verification

```bash
Generated text: CINNAMON SUGAR
1 x 17,000
17,000
SUB TOTAL
17,000
GRAND TOTAL
17,000
CASH IDR
20,000
CHANGE DUE
3,000
```
