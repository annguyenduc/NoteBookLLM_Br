import os
import sys
import re
from pathlib import Path

# Đảm bảo output luôn là utf-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Đảm bảo PYTHONPATH trỏ tới d:/NoteBookLLM_Br
# Chèn vào đầu sys.path để ưu tiên libs cục bộ
WORKSPACE_ROOT = Path("d:/NoteBookLLM_Br")
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from libs.core.llm_client import call_pedagogical_agent

# CONFIGURATION
RAW_DIR = WORKSPACE_ROOT / "brain/raw"
DISTILLED_DIR = WORKSPACE_ROOT / "brain/distilled"
DISTILLED_DIR.mkdir(parents=True, exist_ok=True)

def distill_lms_document(filename):
    full_path = RAW_DIR / filename
    base_name = os.path.splitext(filename)[0]
    # Remove prefix LMS_RAW_ if exists to avoid double prefix in distilled
    clean_name = base_name.replace("LMS_RAW_", "")
    output_filename = f"LMS_DIST_{clean_name}.md"
    output_path = DISTILLED_DIR / output_filename

    if output_path.exists():
        print(f"  > [SKIP] {output_filename} already exists.")
        return

    print(f"--- 💠 BATCH DISTILL v4.4: {filename} -> {output_filename} ---")
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    prompt = [
        {"role": "system", "content": """Bạn là @scout chuyên trách chưng cất tri thức từ tài liệu đào tạo gốc (LMS).
Nhiệm vụ của bạn là chuyển đổi dữ liệu thô (RAW) sang định dạng tri thức nguyên tử (DISTILLED).

QUY TẮC CHƯNG CẤT (LOM v4.4 Supreme):
1. **Phần 1: FACT BANK (Kiến thức chuẩn)**: 
   - Trích xuất các chân lý kỹ thuật, quy tắc lập trình, thông số linh kiện ĐÚNG.
   - Định dạng: [LMS] [Fact] :: [Giải thích kỹ thuật] :: [[Tag trích dẫn nguồn RAW]]
   - TUYỆT ĐỐI KHÔNG đưa phương án sai vào đây.

2. **Phần 2: TEST BANK (Ngân hàng đề)**:
   - Trích xuất nguyên văn Câu hỏi + Tất cả các phương án (A, B, C, D) + Đáp án đúng + Giải thích.
   - GIỮ NGUYÊN các liên kết hình ảnh Markdown (ví dụ: ![Image](../assets/...)).
   - Định dạng: 
     ### Question: [Nội dung]
     A. [..]
     B. [..]
     C. [..]
     D. [..]
     Correct: [Answer]
     Explanation: [..]

3. **Hình ảnh (Clickable Images)**: 
   - PHẢI duy trì liên kết đến file ảnh trong thư mục assets.
   - PHẢI bao bọc mã hình ảnh trong một liên kết tuyệt đối file:/// để người dùng có thể click mở ảnh.
   - Định dạng bắt buộc: `[![Image](../assets/FILENAME.png)](file:///d:/NoteBookLLM_Br/brain/assets/FILENAME.png)`

4. **Ngôn ngữ**: Phải là Tiếng Việt đúng chuyên môn sư phạm.
5. **Cấu trúc File**: Cả 2 phần phải nằm trong cùng một file .md.
--------------------------------------------------"""},
        {"role": "user", "content": f"DỮ LIỆU LMS RAW ({filename}):\n{content}"}
    ]
    
    # Sử dụng model gemini-2.0-flash-exp:free (via gateway)
    try:
        result, model = call_pedagogical_agent("scout", prompt)
        
        with open(output_path, "w", encoding="utf-8") as f_out:
            f_out.write(f"# DISTILLED KNOWLEDGE: {clean_name}\n\n")
            
            # Triple-Link for Human and Agent
            raw_uri = f"file:///d:/NoteBookLLM_Br/brain/raw/{filename}"
            f_out.write(f"Source: [[{filename}]] — [🚀 Xem RAW]({raw_uri})\n\n")
            
            f_out.write(result)
            
        print(f"  > Success: {output_filename} (Model: {model})")
    except Exception as e:
        print(f"  > [ERROR] Failed to distill {filename}: {str(e)}")

if __name__ == "__main__":
    # Wave 2: Robotics (Codey, mBot, Rover, GBot...) - 20 files
    robotics_files = [
        "LMS_RAW_Robotics_Codey_1+2_Codey_1_Đề_trắc_nghiệm_1_-_Codey_M1.md",
        "LMS_RAW_Robotics_Codey_1+2_Codey_2_Đề_trắc_nghiệm_1_-_Codey_M2.md",
        "LMS_RAW_Robotics_Codey_1+2_Đề_trắc_nghiệm_2_-_Môn_Codey_.md",
        "LMS_RAW_Robotics_Codey_1+2_Đề_trắc_nghiệm_3_-_Môn_Codey_.md",
        "LMS_RAW_Robotics_Codey_1+2_Đề_trắc_nghiệm_4_-_Môn_Codey_.md",
        "LMS_RAW_Robotics_GBot_Đề_trắc_nghiệm_1_-_GBot_v1.md",
        "LMS_RAW_Robotics_GBot_Đề_trắc_nghiệm_1_-_GBot_v2.md",
        "LMS_RAW_Robotics_mBot_1+2_mBot_1_Đề_trắc_nghiệm_1_-_mBot_M1.md",
        "LMS_RAW_Robotics_mBot_1+2_mBot_2_Đề_trắc_nghiệm_1_-_mBot_M2.md",
        "LMS_RAW_Robotics_mBot_1+2_Đề_trắc_nghiệm_1_-_Môn_mBot_M1+2.md",
        "LMS_RAW_Robotics_mBot_1+2_Đề_trắc_nghiệm_2_-_Môn_mBot_M1+2.md",
        "LMS_RAW_Robotics_mBot_1+2_Đề_trắc_nghiệm_3_-_Môn_mBot_M1+2.md",
        "LMS_RAW_Robotics_Rover_Đề_trắc_nghiệm_1_-_Rover.md",
        "LMS_RAW_Robotics_Rover_Đề_trắc_nghiệm_2_-_Rover_-_Rút_gọn.md",
        "LMS_RAW_Robotics_Rover_Đề_trắc_nghiệm_3_-_Rover.md",
        "LMS_RAW_Robotics_Rover_Đề_trắc_nghiệm_4_-_Rover.md",
        "LMS_RAW_Robotics_Rover_Đề_trắc_nghiệm_5_-_Rover.md",
        "LMS_RAW_Robotics_Unplugged_Coding_-_Codey_Đề_trắc_nghiệm_1_-_Unplugged_Coding_(Codey).md",
        "LMS_RAW_Robotics_Unplugged_Coding_-_Rio_Đề_trắc_nghiệm_1_-_Unplugged_Coding_(Rio).md",
        "LMS_RAW_Robotics_xBot_Đề_trắc_nghiệm_1_-_xBot.md"
    ]
    
    for f in robotics_files:
        distill_lms_document(f)
