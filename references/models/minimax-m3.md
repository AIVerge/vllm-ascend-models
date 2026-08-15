# MiniMax-M3

Source: https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/MiniMax-M3.html

Use these snippets as the authoritative starting point for this model. Replace only local paths, IP addresses, ports, NIC names, visible devices, and topology sizes required by the target Ascend environment.

## Quick Facts

- Extracted snippets: 23
- `vllm serve` snippets: 8
- API or client verification snippets: 6

## Snippets

### 1. MiniMax-M3 > 4 Installation > 4.1 Docker Image Installation

```bash
docker pull quay.io/ascend/vllm-ascend:{tag}
```

### 2. MiniMax-M3 > 4 Installation > 4.1 Docker Image Installation

```bash
# Set the vLLM Ascend image name.
export IMAGE=quay.io/ascend/vllm-ascend:{tag}
export NAME=minimax-m3-dev

# Start the container with the variables defined above.
# Update --device for your hardware (Atlas A3: /dev/davinci[0-15]; Atlas A2: /dev/davinci[0-7]).
# If you use a Docker bridge network, open the ports required for multi-node communication in advance.
docker run --rm \
--name $NAME \
--net=host \
--shm-size=100g \
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

### 3. MiniMax-M3 > 4 Installation > 4.1 Docker Image Installation

```bash
cd /vllm-workspace/vllm

# Install _rust_tool_parser for the Rust frontend.
pip install setuptools-rust
./build_rust.sh
```

### 4. MiniMax-M3 > 4 Installation > 4.1 Docker Image Installation

```bash
docker ps | grep vllm-ascend-env
```

### 5. MiniMax-M3 > 4 Installation > 4.1 Docker Image Installation

```bash
pip show vllm-ascend
```

### 6. MiniMax-M3 > 5 Online Service Deployment > 5.1 Single-Node Deployment

```bash
export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"
export HCCL_OP_EXPANSION_MODE="AIV"
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

vllm serve ${WEIGHT_PATH} \
  --served-model-name minimax-m3 \
  --trust-remote-code \
  --max-model-len 43008 \
  --tensor-parallel-size 16 \
  --enable-expert-parallel \
  --max-num-seqs 16 \
  --distributed_executor_backend "mp" \
  --gpu-memory-utilization 0.92 \
  --reasoning-parser minimax_m3 \
  --limit-mm-per-prompt '{"image":1}' \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --additional-config '{
      "enable_cpu_binding": true,
      "ascend_compilation_config": {
      "enable_static_kernel": true,
      "fuse_norm_quant": false
      },
      "multistream_overlap_shared_expert": true,
      "weight_nz_mode": 2,
      "enable_flashcomm1": true,
      "enable_reduce_sample": true
  }' \
  --port 11223 > ${LOG_PATH} 2>&1 &
```

### 7. MiniMax-M3 > 5 Online Service Deployment > 5.1 Single-Node Deployment

```bash
export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"
export HCCL_OP_EXPANSION_MODE="AIV"
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

vllm serve ${WEIGHT_PATH} \
--served-model-name minimax-m3 \
--trust-remote-code \
--max-model-len 131072 \
--tensor-parallel-size 4 \
--data-parallel-size 4 --api_server_count 1 \
--max-num-batched-tokens 32768 \
--long-prefill-token-threshold 4096 \
--enable-expert-parallel \
--max-num-seqs 32 \
--distributed_executor_backend "mp" \
--gpu-memory-utilization 0.92 \
--reasoning-parser minimax_m3 \
--limit-mm-per-prompt '{"image":1}' \
--speculative-config '{"model":"${EAGLE3_WEIGHT_PATH}", "method":"eagle3", "num_speculative_tokens":3}' \
--compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
--additional-config '{
    "enable_cpu_binding": true,
    "ascend_compilation_config": {
      "enable_static_kernel": true,
      "fuse_norm_quant": false
    },
    "multistream_overlap_shared_expert": true,
    "enable_shared_expert_dp": true,
    "weight_nz_mode": 2,
    "enable_flashcomm1": true,
    "enable_reduce_sample": true
}' \
--port 11223 > ${LOG_PATH} 2>&1 &
```

### 8. MiniMax-M3 > 5 Online Service Deployment > 5.2 Multi-Node Deployment

```bash
local_ip="${NODE0_IP}"
node0_ip="${NODE0_IP}"

export HCCL_IF_IP=$local_ip
export IFNAME="${NETWORK_INTERFACE}"
export GLOO_SOCKET_IFNAME="$IFNAME"
export TP_SOCKET_IFNAME="$IFNAME"
export HCCL_SOCKET_IFNAME="$IFNAME"
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export VLLM_ENGINE_READY_TIMEOUT_S=3600
export HCCL_CONNECT_TIMEOUT=7200
export ASCEND_CONNECT_TIMEOUT=10000
export ASCEND_TRANSFER_TIMEOUT=10000
export VLLM_RPC_TIMEOUT=1800000
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_OP_EXPANSION_MODE="AIV"
export TASK_QUEUE_ENABLE=1
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

vllm serve ${WEIGHT_PATH} \
  --host 0.0.0.0 \
  --served-model-name minimax-m3 \
  --trust-remote-code \
  --max-model-len 40960 \
  --tensor-parallel-size 8 \
  --enable-expert-parallel \
  --max-num-seqs 8 \
  --data-parallel-size 2 \
  --data-parallel-size-local 1 \
  --data-parallel-start-rank 0 \
  --data-parallel-address $node0_ip \
  --distributed_executor_backend "mp" \
  --gpu-memory-utilization 0.94 \
  --reasoning-parser minimax_m3 \
  --limit-mm-per-prompt '{"image":1}' \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --additional-config '{"enable_cpu_binding":true, "ascend_compilation_config":{"fuse_norm_quant":false}, "multistream_overlap_shared_expert": true, "weight_nz_mode": 2}' \
  --port 11223 > ${LOG_PATH} 2>&1 &
```

### 9. MiniMax-M3 > 5 Online Service Deployment > 5.2 Multi-Node Deployment

```bash
local_ip="${NODE1_IP}"
node0_ip="${NODE0_IP}"

export HCCL_IF_IP=$local_ip
export IFNAME="${NETWORK_INTERFACE}"
export GLOO_SOCKET_IFNAME="$IFNAME"
export TP_SOCKET_IFNAME="$IFNAME"
export HCCL_SOCKET_IFNAME="$IFNAME"
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export VLLM_ENGINE_READY_TIMEOUT_S=3600
export HCCL_CONNECT_TIMEOUT=7200
export ASCEND_CONNECT_TIMEOUT=10000
export ASCEND_TRANSFER_TIMEOUT=10000
export VLLM_RPC_TIMEOUT=1800000
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_OP_EXPANSION_MODE="AIV"
export TASK_QUEUE_ENABLE=1
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

vllm serve ${WEIGHT_PATH} \
  --host 0.0.0.0 \
  --served-model-name minimax-m3 \
  --trust-remote-code \
  --headless \
  --max-model-len 40960 \
  --tensor-parallel-size 8 \
  --enable-expert-parallel \
  --max-num-seqs 8 \
  --data-parallel-size 2 \
  --data-parallel-size-local 1 \
  --data-parallel-start-rank 1 \
  --data-parallel-address $node0_ip \
  --distributed_executor_backend "mp" \
  --gpu-memory-utilization 0.94 \
  --reasoning-parser minimax_m3 \
  --limit-mm-per-prompt '{"image":1}' \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --additional-config '{"enable_cpu_binding":true, "ascend_compilation_config":{"fuse_norm_quant":false}, "multistream_overlap_shared_expert": true, "weight_nz_mode": 2}' \
  --port 11223 > ${LOG_PATH} 2>&1 &
```

### 10. MiniMax-M3 > 5 Online Service Deployment > 5.2 Multi-Node Deployment

```bash
local_ip="${NODE0_IP}"
node0_ip="${NODE0_IP}"

export HCCL_IF_IP=$local_ip
export IFNAME="${NETWORK_INTERFACE}"
export GLOO_SOCKET_IFNAME="$IFNAME"
export TP_SOCKET_IFNAME="$IFNAME"
export HCCL_SOCKET_IFNAME="$IFNAME"
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export VLLM_ENGINE_READY_TIMEOUT_S=3600
export HCCL_CONNECT_TIMEOUT=7200
export ASCEND_CONNECT_TIMEOUT=10000
export ASCEND_TRANSFER_TIMEOUT=10000
export VLLM_RPC_TIMEOUT=1800000
export VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS=30000
export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"
export HCCL_OP_EXPANSION_MODE="AIV"
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

vllm serve ${WEIGHT_PATH} \
  --host 0.0.0.0 \
  --served-model-name minimax-m3 \
  --trust-remote-code \
  --max-model-len 131072 \
  --tensor-parallel-size 8 \
  --enable-expert-parallel \
  --max-num-seqs 8 \
  --data-parallel-size 2 \
  --data-parallel-size-local 1 \
  --data-parallel-start-rank 0 \
  --data-parallel-address $node0_ip \
  --distributed_executor_backend "mp" \
  --gpu-memory-utilization 0.92 \
  --reasoning-parser minimax_m3 \
  --limit-mm-per-prompt '{"image":1}' \
  --speculative-config '{"model":"${EAGLE3_WEIGHT_PATH}", "method":"eagle3", "num_speculative_tokens":3}' \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --additional-config '{"enable_cpu_binding":true, "ascend_compilation_config":{"fuse_norm_quant":false}, "multistream_overlap_shared_expert": false, "weight_nz_mode": 2, "enable_flashcomm1": true}' \
  --port 11223 > ${LOG_PATH} 2>&1 &
```

### 11. MiniMax-M3 > 5 Online Service Deployment > 5.2 Multi-Node Deployment

```bash
local_ip="${NODE1_IP}"
node0_ip="${NODE0_IP}"

export HCCL_IF_IP=$local_ip
export IFNAME="${NETWORK_INTERFACE}"
export GLOO_SOCKET_IFNAME="$IFNAME"
export TP_SOCKET_IFNAME="$IFNAME"
export HCCL_SOCKET_IFNAME="$IFNAME"
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export VLLM_ENGINE_READY_TIMEOUT_S=3600
export HCCL_CONNECT_TIMEOUT=7200
export ASCEND_CONNECT_TIMEOUT=10000
export ASCEND_TRANSFER_TIMEOUT=10000
export VLLM_RPC_TIMEOUT=1800000
export VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS=30000
export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"
export HCCL_OP_EXPANSION_MODE="AIV"
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

vllm serve ${WEIGHT_PATH} \
  --host 0.0.0.0 \
  --served-model-name minimax-m3 \
  --trust-remote-code \
  --headless \
  --max-model-len 131072 \
  --tensor-parallel-size 8 \
  --enable-expert-parallel \
  --max-num-seqs 8 \
  --data-parallel-size 2 \
  --data-parallel-size-local 1 \
  --data-parallel-start-rank 1 \
  --data-parallel-address $node0_ip \
  --distributed_executor_backend "mp" \
  --gpu-memory-utilization 0.92 \
  --reasoning-parser minimax_m3 \
  --limit-mm-per-prompt '{"image":1}' \
  --speculative-config '{"model":"${EAGLE3_WEIGHT_PATH}", "method":"eagle3", "num_speculative_tokens":3}' \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --additional-config '{"enable_cpu_binding":true, "ascend_compilation_config":{"fuse_norm_quant":false}, "multistream_overlap_shared_expert": false, "weight_nz_mode": 2, "enable_flashcomm1": true}' \
  --port 11223 > ${LOG_PATH} 2>&1 &
```

### 12. MiniMax-M3 > 5 Online Service Deployment > 5.3 Multimodal and ViT DP (Optional)

```bash
--mm-encoder-tp-mode data
```

### 13. MiniMax-M3 > 5 Online Service Deployment > 5.3 Multimodal and ViT DP (Optional)

```bash
# one video
--limit-mm-per-prompt '{"video":1}'

# one image and one video
--limit-mm-per-prompt '{"image":1, "video":1}'
```

### 14. MiniMax-M3 > 5 Online Service Deployment > 5.3 Multimodal and ViT DP (Optional)

```bash
--allowed-local-media-path /
```

### 15. MiniMax-M3 > 5 Online Service Deployment > 5.3 Multimodal and ViT DP (Optional)

```bash
# Enable FLASHCOMM1.
--additional-config '{"enable_flashcomm1": true}'

# Enable language-model-only mode.
--language-model-only
```

### 16. MiniMax-M3 > 6 Thinking and Parser Configuration > 6.1 Thinking Mode > 6.1.1 Request Examples

```bash
curl http://{ip}:{port}/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "minimax-m3",
    "messages": [{"role": "user", "content": "who are you?"}],
    "max_tokens": 100,
    "stream": false,
    "top_p": 0.95,
    "top_k": 40,
    "temperature": 1.0,
    "chat_template_kwargs": {"thinking_mode": "disabled"}
  }'
```

### 17. MiniMax-M3 > 6 Thinking and Parser Configuration > 6.2 Reasoning Parser > 6.2.1 Server Configuration

```bash
vllm serve ${WEIGHT_PATH} \
  --reasoning-parser minimax_m3 \
  ...
```

### 18. MiniMax-M3 > 6 Thinking and Parser Configuration > 6.3 Tool Call Parser > 6.3.1 Server Configuration

```bash
vllm serve ${WEIGHT_PATH} \
  --reasoning-parser minimax_m3 \
  --enable-auto-tool-choice \
  --tool-call-parser minimax_m3 \
  ...
```

### 19. MiniMax-M3 > 6 Thinking and Parser Configuration > 6.3 Tool Call Parser > 6.3.4 Request Example (curl)

```bash
curl http://{ip}:{port}/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "minimax-m3",
    "messages": [{"role": "user", "content": "What's the weather like in Shanghai?"}],
    "max_tokens": 300,
    "stream": false,
    "tool_choice": "auto",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get current weather for a city",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "City or country name"
                        }
                    },
                    "required": ["location"],
                    "additionalProperties": false
                }
            }
        }
    ],
    "chat_template_kwargs": {"thinking_mode": "disabled"}
  }'
```

### 20. MiniMax-M3 > 7 Functional Verification > 7.1 Text

```bash
curl http://{ip}:{port}/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "model": "minimax-m3",
  "messages": [
    {
      "role": "user",
      "content": "Answer the following multiple choice question. The last line of your response should be of the following format: 'Answer: LETTER' (without quotes) where LETTER is one of ABCD. Think step by step before answering.\n\nA student regrets that he fell asleep during a lecture in electrochemistry, facing the following incomplete statement in a test:\nThermodynamically, oxygen is a …… oxidant in basic solutions. Kinetically, oxygen reacts …… in acidic solutions.\nWhich combination of weaker/stronger and faster/slower is correct?\n\nA) weaker – faster\nB) stronger – faster\nC) weaker - slower\nD) stronger – slower"
    }
  ],
  "max_tokens": 8000,
  "temperature": 1.0
}
EOF
```

### 21. MiniMax-M3 > 7 Functional Verification > 7.2 Single Image

```bash
IMAGE_PATH=/path/to/image.jpg
IMAGE_BASE64="$(base64 -w 0 "${IMAGE_PATH}")"

curl http://{ip}:{port}/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "model": "minimax-m3",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,${IMAGE_BASE64}"}},
        {"type": "text", "text": "Briefly describe this image."}
      ]
    }
  ],
  "max_tokens": 512,
  "temperature": 0
}
EOF
```

### 22. MiniMax-M3 > 7 Functional Verification > 7.3 Single Video

```bash
curl http://{ip}:{port}/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "minimax-m3",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "video_url",
            "video_url": {
              "url": "file:///path/to/video.mp4"
            }
          },
          {
            "type": "text",
            "text": "Briefly describe the main content of this video."
          }
        ]
      }
    ],
    "max_tokens": 512,
    "temperature": 0
  }'
```

### 23. MiniMax-M3 > 7 Functional Verification > 7.4 Mixed Image and Video Request

```bash
IMAGE_BASE64="$(base64 -w 0 /path/to/image.jpg)"

curl http://{ip}:{port}/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "model": "minimax-m3",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,${IMAGE_BASE64}"}},
        {"type": "video_url", "video_url": {"url": "file:///path/to/video.mp4"}},
        {"type": "text", "text": "Describe the image and video separately, and explain whether they are related."}
      ]
    }
  ],
  "max_tokens": 512,
  "temperature": 0
}
EOF
```
