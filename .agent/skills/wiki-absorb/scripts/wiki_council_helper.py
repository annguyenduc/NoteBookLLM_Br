import os
import json
import requests
from typing import List, Dict

# Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# The Council Models
MODELS = [
    "google/gemini-2.0-flash-exp:free",
    "anthropic/claude-3.5-sonnet",
    "openai/gpt-4o-mini"
]

def call_model(model: str, prompt: str) -> str:
    """Gọi một model cụ thể qua OpenRouter."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Error calling {model}: {str(e)}"

def run_council(case_description: str, atom_a_content: str, atom_b_content: str):
    """Triệu tập Hội đồng để xử lý mâu thuẫn tri thức."""
    print(f"--- 🏛️ TRIỆU TẬP WIKI-COUNCIL ---")
    
    prompt = f"""
    Bạn là một thành viên trong Hội đồng Tri thức Wiki (Wiki-Council).
    Nhiệm vụ: Phân xử mâu thuẫn giữa hai mẩu tri thức (Atoms).
    
    Bối cảnh: {case_description}
    
    [ATOM A]:
    {atom_a_content}
    
    [ATOM B]:
    {atom_b_content}
    
    Hãy đưa ra phán quyết:
    1. Tri thức nào chính xác/cập nhật hơn?
    2. Chúng mâu thuẫn hoàn toàn hay bổ sung cho nhau?
    3. Đề xuất hành động: SUPERSEDES A, SUPERSEDES B, MERGE, hoặc KEEP BOTH.
    
    Trình bày ngắn gọn, tập trung vào bằng chứng.
    """

    results = {}
    for model in MODELS:
        print(f"[*] Đang hỏi ý kiến: {model}...")
        results[model] = call_model(model, prompt)
    
    return results

if __name__ == "__main__":
    # Test stub hoặc thực thi khi được gọi từ wiki-absorb
    # Dữ liệu sẽ được truyền qua stdin hoặc args
    pass
