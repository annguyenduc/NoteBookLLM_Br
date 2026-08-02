from libs.core.llm_client import call_profiler
import sys

def test():
    print("Testing @profiler call...")
    try:
        messages = [{"role": "user", "content": "Test profile for teacher A."}]
        content, model = call_profiler(messages, max_tokens=100)
        print(f"Response received from {model}")
        print(f"Content length: {len(content)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test()
