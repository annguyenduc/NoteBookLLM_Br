import sys
import os
import time

# Ensure libs/core is findable
sys.path.append(os.getcwd())

from libs.core.llm_client import _call_9router_audit
from libs.core.logger import get_logger

logger = get_logger("discovery_ping")

# The list discovered from /models endpoint
DISCOVERED_MODELS = [
    "nvidia/moonshotai/kimi-k2.5",
    "nvidia/z-ai/glm4.7",
    "gc/gemini-3-flash-preview",
    "gc/gemini-3-pro-preview",
    "groq/llama-3.3-70b-versatile",
    "groq/meta-llama/llama-4-maverick-17b-128e-instruct",
    "groq/qwen/qwen3-32b",
    "groq/openai/gpt-oss-120b",
    "qw/qwen3-coder-plus",
    "qw/qwen3-coder-flash",
    "qw/vision-model",
    "qw/coder-model"
]

def ping_test():
    print(f"\n============================================================")
    print(f"9ROUTER DISCOVERY PING - CHECKING ALL ENDPOINTS")
    print(f"============================================================\n")
    
    results = []
    
    for model_id in DISCOVERED_MODELS:
        print(f"Testing: {model_id:50}", end="", flush=True)
        start_time = time.time()
        try:
            content, actual_model = _call_9router_audit(
                messages=[{"role": "user", "content": "ping"}],
                temperature=0.1,
                max_tokens=10,
                requested_model=model_id
            )
            elapsed = time.time() - start_time
            print(f" [OK] ({elapsed:.2f}s)")
            results.append({
                "model": model_id,
                "status": "ONLINE",
                "latency": f"{elapsed:.2f}s"
            })
        except Exception as e:
            elapsed = time.time() - start_time
            error_msg = str(e)
            status = "ERROR"
            if "404" in error_msg: status = "404 NOT FOUND"
            elif "429" in error_msg: status = "429 RATE LIMIT"
            
            print(f" [FAIL] {status}")
            results.append({
                "model": model_id,
                "status": status,
                "latency": f"{elapsed:.2f}s"
            })

    print(f"\n============================================================")
    print(f"DISCOVERY SUMMARY")
    print(f"============================================================")
    for r in results:
        print(f"{r['model']:50} | {r['status']:15} | {r['latency']}")
    print(f"============================================================\n")

if __name__ == "__main__":
    ping_test()
