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

TOPIC = "Toán lớp 10: Phương trình bậc hai và hệ thức Vi-ét"

PROMPT_NO_STRUCTURE = "Giải phương trình x^2 - 5x + 6 = 0 và tính tổng, tích các nghiệm."

PROMPT_STRUCTURED = """
# ROLE: Giáo viên Toán K-12
# CONTEXT: Đang hướng dẫn học sinh lớp 10 học về hệ thức Vi-ét.
# TASK: Giải phương trình bậc hai và chứng minh kết quả bằng hệ thức Vi-ét.
# TOPIC: x^2 - 5x + 6 = 0
# FORMAT: 
1. Giải từng bước bằng Delta.
2. Áp dụng Vi-ét để kiểm tra lại.
3. Kết luận ngắn gọn.
# CONSTRAINT: Ngôn ngữ Tiếng Việt, trình bày sư phạm, dễ hiểu.
"""

def get_comparison():
    results = {}
    
    for model in MODELS:
        print(f"--- Calling {model} ---")
        # Run No Structure
        res_simple = call_worker([{"role": "user", "content": PROMPT_NO_STRUCTURE}], model=model)
        # Run Structured
        res_structured = call_worker([{"role": "user", "content": PROMPT_STRUCTURED}], model=model)
        
        results[model] = {
            "simple": res_simple,
            "structured": res_structured
        }
    
    return results

def save_to_md(results):
    output_path = root / "brain/atoms/ATOMS_Demo_Prompt_Comparison_Math.md"
    
    md_content = f"""# So sánh Prompting: Có cấu trúc vs. Không cấu trúc (Toán 10)

> [!NOTE]
> Tài liệu này minh họa sự khác biệt giữa việc đặt câu hỏi ngắn (Simple) và việc sử dụng cấu trúc RTC (Role-Task-Context) đối với các model AI khác nhau qua hạ tầng 9Router.

## 1. Dữ liệu thử nghiệm
- **Chủ đề**: {TOPIC}
- **Model sử dụng**: {', '.join(MODELS)}

## 2. Kết quả so sánh

"""

    for model, res in results.items():
        md_content += f"### 🤖 Model: {model}\n\n"
        md_content += "#### ❌ Prompt không cấu trúc (Simple)\n"
        md_content += f"*Nội dung hỏi: {PROMPT_NO_STRUCTURE}*\n\n"
        md_content += f"```markdown\n{res['simple']}\n```\n\n"
        
        md_content += "#### ✅ Prompt có cấu trúc (RTC)\n"
        md_content += f"*Nội dung hỏi: {PROMPT_STRUCTURED.strip()}*\n\n"
        md_content += f"```markdown\n{res['structured']}\n```\n\n"
        md_content += "---\n\n"

    md_content += """## 3. Nhận định Sư phạm (@pm audit)
- **Prompt đơn giản**: Thường cho kết quả đúng nhưng trình bày khô khan, đôi khi bỏ qua các bước diễn giải quan trọng cho học sinh.
- **Prompt cấu trúc (RTC)**: Model đóng vai giáo viên, có các bước scaffolding rõ ràng, áp dụng đúng Delta và Vi-ét, phù hợp với mục tiêu bài giảng lớp 10.
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"✅ Đã tạo file demo tại: {output_path}")

if __name__ == "__main__":
    data = get_comparison()
    save_to_md(data)
