# Qwen3-Omni-30B-A3B-Thinking

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3-Omni-30B-A3B-Thinking.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 14
- `vllm serve` snippets: 1
- API or client verification snippets: 1

## Snippets

### 1. Qwen3-Omni-30B-A3B-Thinking > 4 Installation > 4.1 Docker Image Installation

```bash
docker pull quay.io/ascend/vllm-ascend:v0.22.1rc1
```

### 2. Qwen3-Omni-30B-A3B-Thinking > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1

docker run \
    --name vllm-ascend-env \
    --shm-size=128g \
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
    -v /etc/hccn.conf:/etc/hccn.conf \
    -it -d $IMAGE bash
```

### 3. Qwen3-Omni-30B-A3B-Thinking > 4 Installation > 4.1 Docker Image Installation

```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.22.1rc1

docker run \
    --name vllm-ascend-env \
    --shm-size=128g \
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
    -v /etc/hccn.conf:/etc/hccn.conf \
    -it -d $IMAGE bash
```

### 4. Qwen3-Omni-30B-A3B-Thinking > 4 Installation > 4.1 Docker Image Installation

```bash
docker ps | grep vllm-ascend-env
```

### 5. Qwen3-Omni-30B-A3B-Thinking > 4 Installation > 4.1 Docker Image Installation

```bash
pip show vllm-ascend
```

### 6. Qwen3-Omni-30B-A3B-Thinking > 4 Installation > 4.2 Source Code Installation

```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm
pip install -e .
```

### 7. Qwen3-Omni-30B-A3B-Thinking > 4 Installation > 4.2 Source Code Installation

```bash
git clone https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
pip install -e .
```

### 8. Qwen3-Omni-30B-A3B-Thinking > 4 Installation > 4.2 Source Code Installation

```bash
pip show vllm vllm-ascend
```

### 9. Qwen3-Omni-30B-A3B-Thinking > 4 Installation > 4.2 Source Code Installation

```bash
pip install qwen_omni_utils modelscope
# Used for audio processing.
apt-get update && apt-get install -y ffmpeg
# Check the installation.
ffmpeg -version
```

### 10. Qwen3-Omni-30B-A3B-Thinking > 4 Installation > 4.2 Source Code Installation

```bash
export HCCL_OP_EXPANSION_MODE="AIV"
```

### 11. Qwen3-Omni-30B-A3B-Thinking > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3
export HCCL_OP_EXPANSION_MODE="AIV"  # not needed on A2
export HCCL_BUFFSIZE=1024
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

vllm serve your_model_path \
    --served-model-name qwen3-omni \
    --trust-remote-code \
    --max-num-seqs 100 \
    --max-model-len 40960 \
    --max-num-batched-tokens 16384 \
    --tensor-parallel-size 4 \
    --enable-expert-parallel \
    --quantization ascend \
    --distributed_executor_backend "mp" \
    --no-enable-prefix-caching \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \
    --gpu-memory-utilization 0.95 \
    --additional-config '{"enable_flashcomm1": false, "weight_nz_mode": 2}' \
    --port 8000
```

### 12. Qwen3-Omni-30B-A3B-Thinking > 5 Online Service Deployment > 5.1 Single-Node Online Deployment

```bash
(APIServer pid=<pid>) INFO:     Started server process [<pid>]
(APIServer pid=<pid>) INFO:     Waiting for application startup.
(APIServer pid=<pid>) INFO:     Application startup complete.
```

### 13. Qwen3-Omni-30B-A3B-Thinking > 6 Functional Verification

```bash
curl http://localhost:8000/v1/chat/completions \
-X POST \
-H "Content-Type: application/json" \
-d '{
    "model": "qwen3-omni",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cars.jpg"
                    }
                },
                {
                    "type": "audio_url",
                    "audio_url": {
                        "url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cough.wav"
                    }
                },
                {
                    "type": "video_url",
                    "video_url": {
                        "url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/draw.mp4"
                    }

                },
                {
                    "type": "text",
                    "text":  "Analyze this audio, image, and video together."
                }
            ]
        }
    ]
}'
```

### 14. Qwen3-Omni-30B-A3B-Thinking > 6 Functional Verification

```json
{
  "id": "chatcmpl-8f3a1c2e4b5d4f7a9c0e1d2b3a4f5e6d",
  "object": "chat.completion",
  "created": 1782714240,
  "model": "Qwen/Qwen3-Omni-30B-A3B-Thinking",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "reasoning_content": "Let me examine each modality. The image shows several cars parked in a row — looks like a street or lot, daytime. The audio is short and sharp, sounds like a human cough (a single dry cough). The video appears to show someone drawing/sketching on paper, a hand moving a pen. Now I need to connect them: there isn't a single obvious narrative linking cars + cough + drawing, so I should describe each and then note any plausible shared context (e.g., a person sketching cars while having a cold). I'll keep the synthesis honest rather than forcing a connection.",
        "content": "Here's an analysis of the three inputs together:\n\n**Image** — A row of parked cars photographed outdoors in daylight, likely on a street or in a parking area. The vehicles are of varying colors and models, shot at a slight angle so several are visible in perspective.\n\n**Audio** — A brief, dry human cough: a single forceful exhalation lasting under a second, with no speech or background music. It sounds like an isolated cough rather than a sustained coughing fit.\n\n**Video** — A close-up of a hand drawing/sketching with a pen on paper, the strokes building up a simple illustration over a few seconds.\n\n**Combined interpretation** — The three clips don't share an explicit storyline; they're distinct samples of vision, sound, and motion. If a connecting context is assumed, one plausible scene is a person sketching cars (the drawing in the video, the cars in the image) while momentarily coughing (the audio) — e.g., an artist working outdoors who has a cold. But strictly, each input stands on its own: a static photo of cars, a one-off cough sound, and a short hand-drawing clip.",
        "tool_calls": []
      },
      "logprobs": null,
      "finish_reason": "stop",
      "stop_reason": null
    }
  ],
  "usage": {
    "prompt_tokens": 8423,
    "total_tokens": 8712,
    "completion_tokens": 289,
    "prompt_tokens_details": null
  },
  "prompt_logprobs": null
}
```
