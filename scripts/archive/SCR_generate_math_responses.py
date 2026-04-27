import sys
import os
from pathlib import Path

# Path to the project root
root = Path("d:/NoteBookLLM_Br")
sys.path.append(str(root))

try:
    from libs.core.llm_client import call_worker
except ImportError:
    print("Error: Could not find libs.core.")
    sys.exit(1)

# Using English keys to avoid UnicodeEncodeError on Windows console
prompts = [
    {
        "id": "Newton",
        "topic_vn": "Nhị thức Newton",
        "non_rtc": "Giải hộ mình bài Nhị thức Newton $(x+2)^5$.",
        "rtc": "Bạn là gia sư Toán. Hãy hướng dẫn mình khai triển $(x+2)^5$ theo công thức Nhị thức Newton. Đừng cho đáp án ngay, hãy gợi ý cho mình cách xác định các hệ số $C_n^k$ trước."
    },
    {
        "id": "Inequality",
        "topic_vn": "Bất phương trình",
        "non_rtc": "Cách giải $x^2 - 5x + 6 > 0$?",
        "rtc": "Đóng vai giáo viên Toán. Hãy giải thích cho mình các bước xét dấu tam thức bậc hai $x^2 - 5x + 6$. Hãy liệt kê các lỗi sai phổ biến học sinh hay mắc ở phần này khi giải bất phương trình."
    },
    {
        "id": "Probability",
        "topic_vn": "Xác suất",
        "non_rtc": "Bảng xác suất lấy 2 thẻ từ 10 thẻ.",
        "rtc": "Bạn là giáo viên Toán giàu kinh nghiệm. Trong bài toán lấy ngẫu nhiên 2 thẻ từ 10 thẻ đánh số từ 1 đến 10, hãy giúp mình liệt kê 'Không gian mẫu' và hướng dẫn mình cách tính xác suất tổng điểm 2 thẻ là số lẻ theo phương pháp sư phạm gợi mở từng bước."
    },
    {
        "id": "Circle",
        "topic_vn": "Đường tròn",
        "non_rtc": "Lập phương trình đường tròn đi qua A(1,1) và B(3,3).",
        "rtc": "Đóng vai gia sư hình học. Hãy hướng dẫn mình các bước xác định tâm I và bán kính R để lập phương trình đường tròn đi qua A(1,1) và B(3,3). Hãy dùng ví dụ này để ôn tập kiến thức về vectơ pháp tuyến."
    }
]

def get_responses():
    results = []
    print("Starting AI response generation (Unicode safe)...")
    for item in prompts:
        topic_id = item["id"]
        print(f"Generating for: {topic_id}")
        
        try:
            # Non-RTC
            res_non = call_worker([{"role": "user", "content": item["non_rtc"]}], model="ag/gemini-3-flash")
            
            # RTC
            res_rtc = call_worker([{"role": "user", "content": item["rtc"]}], model="ag/gemini-3-flash")
            
            results.append({
                "topic": item["topic_vn"],
                "non_rtc_ans": res_non,
                "rtc_ans": res_rtc
            })
        except Exception as e:
            print(f"Error calling AI for {topic_id}: {e}")
            continue
    
    # Save results to a file (UTF-8)
    output_path = root / "brain/process/ai_comparison_results.md"
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("# Phản hồi thực tế từ AI (Gemini-3-Flash)\n\n")
            for res in results:
                f.write(f"## Chủ đề: {res['topic']}\n\n")
                f.write("### ❌ Prompt Non-RTC (Kết quả thụ động)\n")
                f.write(f"{res['non_rtc_ans']}\n\n")
                f.write("### ✅ Prompt RTC (Kết quả dẫn dắt - Guided Learning)\n")
                f.write(f"{res['rtc_ans']}\n\n")
                f.write("---\n\n")
        print(f"Success! Output saved to: {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    get_responses()
