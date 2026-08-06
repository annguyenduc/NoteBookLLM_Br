import sys
import os
from libs.core.llm_client import call_pedagogical_agent

# Đảm bảo output luôn là utf-8 để tránh lỗi trên Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Đảm bảo PYTHONPATH trỏ về gốc dự án
sys.path.append(os.getcwd())

def finalize_test():
    print("--- 🏁 HOÀN TẤT ĐỀ KIỂM TRA CHUẨN (STRICT REFINE) ---")
    
    with open("3-resources/distilled/LMS_KB_IOT_DEEP.md", "r", encoding="utf-8") as f:
        kb_content = f.read()

    # Re-generating from scratch with all auditor feedback incorporated into the prompt
    final_prompt = [
        {"role": "system", "content": f"GROUND TRUTH KB:\n{kb_content}"},
        {"role": "user", "content": """Hãy viết đề kiểm tra trắc nghiệm 10 câu cho Arduino 1.
Yêu cầu bắt buộc:
1. Chỉ dùng thông tin trong KB.
2. Tuyệt đối không bịa màu sắc LED (ghi là 'Đèn LED'), không bịa vận tốc Servo (ghi là 'quay góc cố định').
3. Cần nhắc đến: Chân D0/D1 nên hạn chế dùng [Arduino_M1], giá trị Joystick nghỉ ~512 [Joystick_M1], phân biệt cực LED bằng bản cực to/nhỏ [Arduino_M1].
4. Mỗi câu hỏi PHẢI có tag [Nguồn: ...] ở cuối.
5. Định dạng Markdown chuyên nghiệp."""}
    ]
    
    content, model = call_pedagogical_agent("finalizer", final_prompt, model="groq/llama-3.3-70b-versatile")
    
    output_path = "3-resources/distilled/LMS_Tests_Arduino_M1_FINAL.md"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ Đề kiểm tra cuối cùng đã sẵn sàng tại: {output_path}")

if __name__ == "__main__":
    finalize_test()
