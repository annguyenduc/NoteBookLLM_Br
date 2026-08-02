import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="D:/01_Workspaces/SmartProxyHub/.env")

url = os.getenv("SMART_ROUTER_URL", "http://localhost:20128/v1/models")
# Usually, models endpoint is /models, not /chat/completions
if "/chat/completions" in url:
    url = url.replace("/chat/completions", "/models")

key = os.getenv("NINEROUTER_API_KEY")

try:
    response = requests.get(url, headers={"Authorization": f"Bearer {key}"})
    if response.status_code == 200:
        models = response.json()
        print("Available Models:")
        for model in models.get("data", []):
            print(f"- {model['id']}")
    else:
        print(f"Failed to fetch models: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"Error: {e}")
