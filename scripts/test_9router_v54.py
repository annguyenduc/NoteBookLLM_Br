import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv


def main() -> None:
    proxy_env = Path("D:/01_Workspaces/SmartProxyHub/.env")
    if proxy_env.exists():
        load_dotenv(proxy_env, override=True)

    url = os.getenv("SMART_ROUTER_URL", "http://localhost:20128/v1/chat/completions")
    api_key = os.getenv("NINEROUTER_API_KEY")
    model = os.getenv(
        "SMART_ROUTER_MODEL",
        "ag/gemini-3-flash",
    )

    if not api_key:
        raise RuntimeError("Missing NINEROUTER_API_KEY in environment.")

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": "Reply in one short line with your model name and provider.",
            }
        ],
        "temperature": 0.1,
        "max_tokens": 80,
        "stream": False,
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    print("--- 9Router v5.4 Direct Audit Test ---")
    print(f"URL: {url}")
    print(f"Model Sent: {model}")

    response = requests.post(url, headers=headers, json=payload, timeout=180)
    header_request_id = response.headers.get("x-request-id") or response.headers.get("request-id")

    print(f"Status Code: {response.status_code}")
    print(f"Header Request ID: {header_request_id or 'N/A'}")

    if response.status_code != 200:
        print("Raw Error Body:")
        print(response.text)
        response.raise_for_status()

    body = response.text.strip()
    if "data: [DONE]" in body:
        body = body.split("data: [DONE]")[0].strip()

    data = json.loads(body)
    response_id = data.get("id", "N/A")
    response_model = data.get("model", "N/A")
    content = data["choices"][0]["message"]["content"].strip()

    print(f"Body Request ID: {response_id}")
    print(f"Model Returned: {response_model}")
    print(f"Content: {content}")


if __name__ == "__main__":
    main()
