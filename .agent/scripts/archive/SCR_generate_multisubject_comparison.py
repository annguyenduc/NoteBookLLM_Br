import sys
from pathlib import Path

# Thêm root vào path để import libs
root = Path(__file__).resolve().parent.parent
sys.path.append(str(root))

from libs.core.llm_client import call_worker

MODELS = [
    "ag/gemini-3-flash",
    "groq/llama-3.3-70b-versatile"
]

# Định nghĩa các bài test cho từng môn
TEST_CASES = {
    "Vat Ly": {
        "title": "Vật lý",
        "simple": "Giải bài tập xe chuyển động thẳng biến đổi đều với vận tốc đầu 10m/s, gia tốc 2m/s^2.",
        "rtc": """# ROLE: Giáo viên Vật lý lớp 10
# TASK: Hãy phân tích hiện tượng và giải bài toán sau.
# CONTEXT: Một xe chuyển động thẳng biến đổi đều với vận tốc đầu 10m/s, gia tốc 2m/s^2. Hãy tính quãng đường xe đi được sau 5 giây.
# FORMAT: (1) Tóm tắt đề, (2) Phân tích hiện tượng, (3) Các bước áp dụng công thức."""
    },
    "Hoa hoc": {
        "title": "Hóa học",
        "simple": "Viết cấu hình electron của nguyên tử Magnesium (Z=12) và vị trí của nó.",
        "rtc": """# ROLE: Chuyên gia Hóa học.
# TASK: Giải thích cấu tạo nguyên tử của nguyên tố Magnesium (Z=12) và xác định vị trí của nó trong bảng tuần hoàn. 
# CONTEXT: Học sinh đang làm quen với Bảng tuần hoàn hóa học.
# CONSTRAINT: Trình bày sư phạm, dễ hiểu."""
    },
    "Ngu van": {
        "title": "Ngữ văn",
        "simple": "Lập dàn ý bài văn nghị luận về ảnh hưởng của mạng xã hội đến học sinh.",
        "rtc": """# ROLE: Chuyên gia hướng dẫn tư duy phản biện.
# TASK: Hãy giúp tôi lập dàn ý chi tiết bài văn nghị luận về vấn đề: Ảnh hưởng của mạng xã hội đến học sinh hiện nay.
# STRUCTURE: Mở bài (dẫn dắt), Thân bài (giải thích, chứng minh, bác bỏ), Kết bài (thông điệp)."""
    },
    "Tieng Anh": {
        "title": "Tiếng Anh",
        "simple": "Correct this sentence: I have live here since 5 years.",
        "rtc": """# ROLE: Chuyên gia ngôn ngữ English.
# TASK: Đây là câu tiếng Anh của tôi: 'I have live here since 5 years.' 
# ACTION: Hãy chỉnh sửa lỗi ngữ pháp, giải thích tại sao sai (Past Simple vs Present Perfect) và gợi ý 2 cách viết tự nhiên hơn."""
    }
}

def run_swarm_audit():
    all_results = {}
    
    for key, data in TEST_CASES.items():
        print(f"--- Processing: {key} ---")
        subject_results = {}
        for model in MODELS:
            print(f"  Calling {model}...")
            try:
                res_simple = call_worker([{"role": "user", "content": data["simple"]}], model=model)
                res_rtc = call_worker([{"role": "user", "content": data["rtc"]}], model=model)
                subject_results[model] = {"simple": res_simple, "rtc": res_rtc}
            except Exception as e:
                print(f"  Error: {e}")
                subject_results[model] = {"simple": "ERROR", "rtc": "ERROR"}
        all_results[data["title"]] = subject_results
    
    return all_results

def append_to_comparison(results):
    output_path = root / "brain/atoms/ATOMS_Demo_Prompt_Comparison_K10.md"
    
    new_sections = "\n---\n\n## 💡 3.2. Mở rộng Đa môn (Multi-Subject Expansion)\n\n"
    
    for subject, model_data in results.items():
        new_sections += f"### 📘 Môn học: {subject}\n\n"
        for model, res in model_data.items():
            new_sections += f"#### 🤖 Model: {model}\n"
            new_sections += f"**[Lượt A - Simple]**\n```markdown\n{res['simple']}\n```\n\n"
            new_sections += f"**[Lượt B - RTC]**\n```markdown\n{res['rtc']}\n```\n"
            new_sections += "\n---\n\n"

    with open(output_path, "a", encoding="utf-8") as f:
        f.write(new_sections)
    print(f"Successfully finished all subjects.")

if __name__ == "__main__":
    results = run_swarm_audit()
    append_to_comparison(results)
