import requests
import json

BASE_URL = "http://localhost:4000/v1"

def test_short_prompt():
    print("--- Testing Short Prompt (< 800 tokens) ---")
    payload = {
        "messages": [{"role": "user", "content": "Hello, how are you?"}],
        "model": "main", # Any model name will do as the router decides
        "temperature": 0
    }
    response = requests.post(f"{BASE_URL}/chat/completions", json=payload)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print("Response received successfully!")
        # In a real TDD, we would check the server logs for "Mapping: ... -> fast-engine"
    else:
        print(f"Error: {response.text}")

def test_long_prompt():
    print("\n--- Testing Long Prompt (>= 800 tokens) ---")
    # Generate a long text
    long_text = "lorem ipsum " * 200 # roughly 1000+ tokens
    payload = {
        "messages": [{"role": "user", "content": long_text}],
        "model": "main",
        "temperature": 0
    }
    response = requests.post(f"{BASE_URL}/chat/completions", json=payload)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print("Response received successfully!")
    else:
        print(f"Error: {response.text}")

if __name__ == "__main__":
    try:
        test_short_prompt()
        test_long_prompt()
    except Exception as e:
        print(f"Connection failed: {e}")
