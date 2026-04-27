import sys
from pathlib import Path

# ThÃªm root vÃ o path Ä‘á»ƒ import libs
root = Path(__file__).resolve().parent.parent
sys.path.append(str(root))

from libs.core.llm_client import call_worker

print("--- Testing Swarm v4.7 Supreme Integration (9Router) ---")
try:
    # Gá» i AI qua luá»“ng 9Router má»›i
    response = call_worker([{"role": "user", "content": "Say hello and identify which model are you?"}], model="test-9router")
    print(f"\n[AI RESPONSE]: {response}")
    print("\nâœ“ STATUS: 9Router is working perfectly and routing requests!")
except Exception as e:
    print(f"\nâœ— STATUS: Failed to communicate via 9Router. Error: {e}")
