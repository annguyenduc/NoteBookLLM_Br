import sys
import os
from libs.core.llm_client import call_profiler, call_designer, call_pedagogical_engineer, call_auditor

# Đảm bảo output luôn là utf-8 để tránh lỗi trên Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Đảm bảo PYTHONPATH trỏ về gốc dự án
sys.path.append(os.getcwd())

def run_strict_pipeline():
    print("--- 🛡️ KHỞI CHẠY SWARM STRICT INTEGRITY PIPELINE ---")
    
    # 1. @profiler
    print("\n[STEP 1] @profiler is analyzing...")
    profile_input = [
        {"role": "user", "content": "Phân tích trình độ giáo viên sơ cấp học Arduino 1. Tập trung vào các thuật ngữ chuẩn trong KB."}
    ]
    profile_out, p_model = call_profiler(profile_input)
    print(f"  > Profile generated (Model: {p_model})")
    
    # 2. @designer
    print("\n[STEP 2] @designer is planning (Strict Mode)...")
    with open("3-resources/distilled/LMS_KB_IOT_DEEP.md", "r", encoding="utf-8") as f:
        kb_content = f.read()

    design_input = [
        {"role": "system", "content": f"Trainer Profile:\n{profile_out}\n\nGROUND TRUTH KNOWLEDGE BASE:\n{kb_content}"},
        {"role": "user", "content": "Thiết kế ma trận 10 câu trắc nghiệm Arduino 1. Chỉ sử dụng thông tin có trong Ground Truth. Phải liệt kê Section/Line tham chiếu cho từng câu."}
    ]
    design_out, d_model = call_designer(design_input)
    print(f"  > Learning Design generated (Model: {d_model})")
    
    # 3. @engineer
    print("\n[STEP 3] @engineer is building (Anti-Hallucination)...")
    engineer_input = [
        {"role": "system", "content": f"Learning Design & References:\n{design_out}\n\nGROUND TRUTH:\n{kb_content}"},
        {"role": "user", "content": "Viết đề kiểm tra hoàn chỉnh. BẮT BUỘC: Mỗi câu hỏi phải kết thúc bằng tag [Nguồn: Section/Reference]. Nếu không có dẫn chứng trong Ground Truth, KHÔNG ĐƯỢC phép viết."}
    ]
    engineer_out, e_model = call_pedagogical_engineer(engineer_input)
    print(f"  > Content generated (Model: {e_model})")
    
    # 4. @auditor
    print("\n[STEP 4] @auditor is verifying...")
    auditor_input = [
        {"role": "system", "content": f"GROUND TRUTH:\n{kb_content}"},
        {"role": "user", "content": f"Hãy kiểm tra đề sau đây. Xoá bỏ bất kỳ câu hỏi nào không có căn cứ trong GROUND TRUTH hoặc sai thuật ngữ. Tranh bịa đặt thông tin.\n\nĐỀ CẦN KIỂM TRA:\n{engineer_out}"}
    ]
    auditor_out, a_model = call_auditor(auditor_input)
    print(f"  > Audit completed (Model: {a_model})")
    
    # Save output
    output_path = "3-resources/distilled/LMS_Tests_Arduino_M1_Swarm_Strict.md"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(auditor_out)
    
    print(f"\n✅ Pipeline hoàn thành! Kết quả tại: {output_path}")

if __name__ == "__main__":
    run_strict_pipeline()
