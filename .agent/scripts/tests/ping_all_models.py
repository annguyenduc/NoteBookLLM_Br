import sys
import os
import time

# Ensure libs/core is findable
sys.path.append(os.getcwd())

from libs.core.llm_client import _call_9router_audit
from libs.core.logger import get_logger

logger = get_logger("ping_test")

MODELS = [
    "ag/gemini-3-flash",
    "ag/gemini-3.1-pro-low",
    "ag/claude-sonnet-4-6",
    "ag/claude-opus-4-6-thinking",
    "groq/llama-3.3-70b-versatile",
    "groq/qwen/qwen3-32b",
    "nvidia/moonshotai/kimi-k2.5"
]

def ping_test():
    print(f"\n{'='*60}")
    print(f"9ROUTER PING TEST - DETECTING ACTIVE MODELS")
    print(f"{'='*60}\n")
    
    results = []
    
    for model_id in MODELS:
        print(f"Testing: {model_id:35}", end="", flush=True)
        start_time = time.time()
        try:
            # Bypass fallback logic to test SPECIFIC model
            content, actual_model = _call_9router_audit(
                messages=[{"role": "user", "content": "Respond with one word: 'READY'"}],
                temperature=0.1,
                max_tokens=10,
                requested_model=model_id
            )
            elapsed = time.time() - start_time
            print(f" [OK] ({elapsed:.2f}s)")
            results.append({
                "model": model_id,
                "status": "ONLINE",
                "latency": f"{elapsed:.2f}s",
                "actual": actual_model,
                "error": None
            })
        except Exception as e:
            elapsed = time.time() - start_time
            error_msg = str(e)
            if "404" in error_msg:
                status = "404 NOT FOUND"
            elif "429" in error_msg:
                status = "429 RATE LIMIT"
            else:
                status = "ERROR"
            
            print(f" [FAIL] {status}")
            results.append({
                "model": model_id,
                "status": status,
                "latency": f"{elapsed:.2f}s",
                "actual": "N/A",
                "error": error_msg[:100]
            })

    print(f"\n{'='*60}")
    print(f"SUMMARY REPORT")
    print(f"{'='*60}")
    print(f"{'MODEL ID':35} | {'STATUS':15} | {'LATENCY'}")
    print(f"{'-'*35}-+-{'-'*15}-+-{'-'*8}")
    for r in results:
        print(f"{r['model']:35} | {r['status']:15} | {r['latency']}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    ping_test()
