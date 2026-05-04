import requests
import json

URL = "http://localhost:4000/v1/chat/completions"
HEADERS = {
    "Authorization": "Bearer sk-antigravity-secret",
    "Content-Type": "application/json"
}

prompts = {
    "Simple": "Cách tìm đỉnh và trục đối xứng của hàm số bậc hai?",
    "Structured": "Đóng vai chuyên gia Toán học lớp 10. Hãy hướng dẫn cách tìm tọa độ đỉnh và phương trình trục đối xứng của hàm số $y = ax^2 + bx + c$ ($a \\neq 0$). Cung cấp các bước thực hiện rõ ràng, công thức tổng quát và một ví dụ minh họa cụ thể cho hàm $y = 2x^2 + 4x + 1$."
}

engines = ["analyst-engine", "fast-engine", "main-engine"]

results = {}

for engine in engines:
    results[engine] = {}
    for type_p, content in prompts.items():
        print(f"Calling {engine} for {type_p} prompt...")
        payload = {
            "model": engine,
            "messages": [{"role": "user", "content": content}]
        }
        try:
            response = requests.post(URL, headers=HEADERS, json=payload, timeout=60)
            resp_json = response.json()
            if response.status_code == 200:
                results[engine][type_p] = resp_json['choices'][0]['message']['content']
                
                # Ghi log vào manifest để minh xác (Rule 12 & Swarm Protocol)
                from datetime import datetime
                manifest_entry = {
                    "ts": datetime.now().isoformat(),
                    "agent": "engineer", # Giả lập vai trò engineer thực thi
                    "model": engine,
                    "request_id": resp_json.get('id', 'unknown_id')
                }
                with open("d:/NoteBookLLM_Br/storage/execution_manifest.jsonl", "a", encoding="utf-8") as f_manifest:
                    f_manifest.write(json.dumps(manifest_entry) + "\n")
            else:
                results[engine][type_p] = f"Error {response.status_code}: {response.text}"
        except Exception as e:

            results[engine][type_p] = f"Error connection: {str(e)}"

with open("d:/NoteBookLLM_Br/scratch/prompt_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("Done. Results saved to scratch/prompt_results.json")
