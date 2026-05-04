
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

import json
import io

# Fix Unicode output issues in Windows console
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Danh sách nội dung cần lấy phản hồi
prompts = [
    # ENGLISH 10
    {
        "subject": "English 10",
        "topic": "Passive Voice",
        "non_rtc": "Explain Passive Voice and translate: 'They have built a new school in this area.'",
        "rtc": "Bạn là gia sư Tiếng Anh lớp 10. Hãy hướng dẫn mình chuyển câu: 'They have built a new school in this area' sang dạng bị động (Unit 7 - Global Success). Hãy dùng phương pháp Guided Learning: đưa ra cấu trúc mẫu và yêu cầu mình tự xác định S, V, O trước."
    },
    {
        "subject": "English 10",
        "topic": "Reported Speech",
        "non_rtc": "Change to reported speech: 'I am using a tablet for my project,' said Nam.",
        "rtc": "Bạn là giáo viên Tiếng Anh. Hãy giúp mình chuyển câu trực tiếp sau sang gián tiếp (Unit 8 - New Ways to Learn): 'I am using a tablet for my project,' said Nam. Hãy lưu ý mình 3 thành phần cần thay đổi (Person, Tense, Time) và để mình tự điền kết quả."
    },
    # LITERATURE 10
    {
        "subject": "Literature 10",
        "topic": "Symbolism in Đất nước",
        "non_rtc": "Ý nghĩa hình ảnh đất nước trong bài thơ Đất nước của Nguyễn Đình Thi.",
        "rtc": "Bạn là giáo viên Ngữ Văn lớp 10. Hãy gợi ý cho mình cách phân tích hình ảnh 'Đất nước' trong những câu thơ đầu bài thơ của Nguyễn Đình Thi. Đừng viết văn mẫu, hãy đặt ra các câu hỏi về âm hưởng ('rướm máu' vs 'ngời sáng') để mình tự suy nghĩ."
    },
    {
        "subject": "Literature 10",
        "topic": "Essay Outline",
        "non_rtc": "Lập dàn ý phân tích bài thơ Khoảng trời hố bom.",
        "rtc": "Đóng vai giáo viên hướng dẫn. Hãy cùng mình lập dàn ý cho bài văn nghị luận phân tích bài thơ 'Khoảng trời, hố bom' (Lâm Thị Mỹ Dạ). Đầu tiên, thầy/cô hãy gợi ý cho em cách đặt vấn đề (Mở bài) sao cho gắn kết được với sự hy sinh của thanh niên xung phong."
    }
]

results = []

print("Starting AI response collection via llm_client (ag/gemini-3-flash)...")

for p in prompts:
    print(f"Processing: {p['subject']} - {p['topic']}")
    
    try:
        # Call Non-RTC
        print(f"  Calling Non-RTC...")
        res_non = call_worker([{"role": "user", "content": p['non_rtc']}], model="ag/gemini-3-flash")
        
        # Call RTC
        print(f"  Calling RTC...")
        res_rtc = call_worker([{"role": "user", "content": p['rtc']}], model="ag/gemini-3-flash")
        
        results.append({
            "subject": p['subject'],
            "topic": p['topic'],
            "non_rtc_prompt": p['non_rtc'],
            "non_rtc_response": res_non,
            "rtc_prompt": p['rtc'],
            "rtc_response": res_rtc
        })
    except Exception as e:
        print(f"  Error: {e}")

# Ghi kết quả ra file JSON
output_file = root / "3-resources/process/ai_comparison_results_anh_van.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"Done! Results saved to {output_file}")
