import os
import sys
import re
from libs.core.llm_client import call_pedagogical_agent

# Đảm bảo output luôn là utf-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.append(os.getcwd())

def distill_lms_document(full_path):
    filename = os.path.basename(full_path)
    base_name = os.path.splitext(filename)[0]
    
    print(f"--- 💠 CHƯNG CẤT CỐT LÕI LMS: {filename} ---")
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Nhận diện TAG từ tên file (dựa trên MASTER_SOURCE_INDEX logic)
    # Ví dụ: Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_1_... -> [IOT_ARD_M1_T01]
    # Ở đây chúng ta sẽ để LLM tự chọn Tag nếu nó thấy khớp, hoặc dùng tên file làm Tag tạm thời.
    
    prompt = [
        {"role": "system", "content": """Bạn là @scout chuyên trách chưng cất tri thức từ tài liệu đào tạo gốc (LMS).
Nhiệm vụ của bạn là chuyển đổi Đề thi/Giáo án sang 2 định dạng lưu trữ khác nhau.

QUY TẮC CHƯNG CẤT (LOM v4.1):
1. **Fact Bank (Kiến thức chuẩn)**: 
   - Chỉ trích xuất các chân lý kỹ thuật, quy tắc lập trình, thông số linh kiện ĐÚNG.
   - Định dạng: [LMS] [Fact] :: [Giải thích kỹ thuật] :: [Tag trích dẫn]
   - TUYỆT ĐỐI KHÔNG đưa phương án sai vào đây.

2. **Test Bank (Ngân hàng đề)**:
   - Trích xuất nguyên văn Câu hỏi + Tất cả các phương án (A, B, C, D) + Đáp án đúng + Giải thích.
   - Nếu có hình ảnh (dạng ![image](path)), hãy giữ nguyên mã markdown đó trong câu hỏi.
   - Định dạng: 
     ### Question: [Nội dung]
     A. [..]
     B. [..]
     C. [..]
     D. [..]
     Correct: [Answer]
     Explanation: [..]

3. **Hình ảnh**: Phải duy trì liên kết đến file ảnh trong thư mục assets.
--------------------------------------------------"""},
        {"role": "user", "content": f"DỮ LIỆU LMS RAW ({filename}):\n{content}"}
    ]
    
    # Sử dụng model ag/gemini-3-flash theo yêu cầu user
    result, model = call_pedagogical_agent("scout", prompt)
    
    # Tách kết quả dựa trên regex (không phân biệt chữ hoa thường, chấp nhận các ký tự thừa)
    parts = re.split(r"###.*TEST BANK.*", result, flags=re.IGNORECASE)
    
    kb_path = "brain/distilled/LMS_KB_IOT.md"
    test_path = f"brain/distilled/assessments/{base_name}_BANK.md"
    
    os.makedirs("brain/distilled/assessments", exist_ok=True)
    
    # Clean Fact part
    fact_part = parts[0].replace("### 1. FACT BANK (KIẾN THỨC CHUẨN)", "").strip()
    
    # Append Fact vào KB chung
    with open(kb_path, "a", encoding="utf-8") as f_kb:
        f_kb.write(f"\n\n## Source: {filename}\n")
        f_kb.write(fact_part)
        
    # Ghi Test Bank vào file riêng nếu tìm thấy phần 2
    if len(parts) > 1:
        test_part = parts[1].strip()
        with open(test_path, "w", encoding="utf-8") as f_test:
            f_test.write(f"# TEST BANK: {filename}\n\n")
            f_test.write(test_part)
            
    print(f"  > Distilled to KB and {test_path} (Model: {model})")

if __name__ == "__main__":
    SOURCE_DIR = "brain/raw/lms_multi_media_dump"
    # Lấy 5 file IoT tiêu biểu để chạy batch đầu tiên
    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(".md")]
    
    for f in files:
        distill_lms_document(os.path.join(SOURCE_DIR, f))
