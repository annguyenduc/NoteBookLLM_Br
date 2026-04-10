import os
import json
import asyncio
from datetime import datetime

# Đây là file engine để chạy các bài test cho Skill.
# Nó sẽ giả lập việc gọi Claude API và sử dụng Grader agent để chấm điểm.

async def run_evals(skill_path, cases_path):
    print(f"🚀 Bắt đầu chạy Evals cho: {skill_path}")
    
    with open(cases_path, 'r', encoding='utf-8') as f:
        cases = json.load(f)
    
    results = {
        "skillName": os.path.basename(skill_path),
        "metrics": {
            "passRate": "0%",
            "avgTokens": "0",
            "avgTime": "0s"
        },
        "results": []
    }
    
    passed_count = 0
    for case in cases:
        print(f"📝 Đang chạy Test Case: {case['id']}...")
        # Giả lập thực thi
        await asyncio.sleep(1) 
        
        # Trong thực tế, ở đây sẽ gọi Claude CLI và Grader Agent
        res = {
            "id": case['id'],
            "prompt": case['prompt'],
            "output": "MOCK_OUTPUT_CHƯA_CÓ_KẾT_NỐI_API",
            "grade": "Pass",
            "feedback": "Tạm thời pass trong chế độ giả lập."
        }
        results['results'].append(res)
        passed_count += 1
        
    results['metrics']['passRate'] = f"{(passed_count/len(cases))*100}%"
    
    output_file = f"eval_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Đã lưu kết quả vào: {output_file}")
    return output_file

if __name__ == "__main__":
    # Ví dụ chạy: python run_eval.py skill.md cases.json
    pass
