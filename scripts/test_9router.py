import litellm
import os
from dotenv import load_dotenv

load_dotenv("D:/01_Workspaces/SmartProxyHub/.env")
key = os.getenv("NINEROUTER_API_KEY")
url = "http://localhost:20128/v1"

# Danh sÃ¡ch test nomenclature
test_models = [
    "google/gemini-2.0-flash-exp:free",
    "openrouter/google/gemini-2.0-flash-exp:free",
    "gemini-2.0-flash-exp",
    "nvidia/llama-3.1-nemotron-70b-instruct:free"
]

for model in test_models:
    print(f"\n--- Testing Model Name: {model} ---")
    try:
        response = litellm.completion(
            model=f"openai/{model}",
            messages=[{"role": "user", "content": "hi"}],
            api_base=url,
            api_key=key,
            custom_llm_provider="openai",
            timeout=10
        )
        print(f"SUCCESS with {model}!")
        print(f"Provider: {response.get('provider', 'unknown')}")
    except Exception as e:
        print(f"FAILED: {e}")
