import sys
import time
from pathlib import Path

# ThÃªm root vÃ o path Ä‘á»ƒ import libs
root = Path(__file__).resolve().parent.parent
sys.path.append(str(root))

from libs.core.llm_client import call_worker

print("--- 9Router Swarm Swarm-Flow Test: Calling Models Sequetially ---")
print("Sending 10 sequential requests with 1.5s gap to 9Router...\n")

start_time = time.time()
engines_seen = set()

for i in range(1, 11):
    try:
        print(f"Requesting AI #{i}...")
        # Gá» i AI vÃ  yÃªu cáº§u tá»± Ä‘á»‹nh danh
        response = call_worker([{"role": "user", "content": "Short identify: What is your model name and the creator company?"}], model="flow-test")
        
        # Cá»‘ gáº¯ng trÃ­ch xuáº¥t tÃªn model tá»« cÃ¢u tráº£ lá» i Ä‘á»ƒ xem cÃ³ khÃ¡c nhau khÃ´ng
        first_line = response.split('\n')[0][:100]
        print(f"[AI #{i} Response]: {first_line}")
        print("-" * 50)
        
        # Nghá»‰ 1.5 giÃ¢y Ä‘á»ƒ gateway Ä‘iá» u phá»‘i mÆ°á»£t mÃ 
        time.sleep(1.5)
    except Exception as e:
        print(f"[AI #{i} Failed]: {e}")

elapsed = time.time() - start_time
print(f"\nâœ“ SWARM-FLOW COMPLETE in {elapsed:.1f}s")
print("Check the responses above to see the diversity of models used by 9Router!")
