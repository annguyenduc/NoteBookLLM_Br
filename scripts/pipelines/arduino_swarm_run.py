import sys
import os

# Đảm bảo output luôn là utf-8 để tránh lỗi trên Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from libs.core.llm_client import call_profiler, call_designer, call_pedagogical_engineer

# Đảm bảo PYTHONPATH trỏ về gốc dự án
sys.path.append(os.getcwd())

def run_pipeline():
    print("--- KHỞI CHẠY SWARM PEDAGOGICAL PIPELINE ---")
    
    # 1. @profiler
    print("\n[STEP 1] @profiler is analyzing...")
    profile_input = [
        {"role": "user", "content": "Phân tích trình độ giáo viên mới bắt đầu học Arduino 1 (board Uno, LED, Breadboard, Servo MG90S)."}
    ]
    profile_out, p_model = call_profiler(profile_input)
    print(f"  > Profile generated (Model: {p_model})")
    
    # 2. @designer
    print("\n[STEP 2] @designer is planning...")
    design_input = [
        {"role": "system", "content": f"Trainer Profile:\n{profile_out}"},
        {"role": "user", "content": "Thiết kế ma trận đề 10 câu hỏi Arduino 1 bám sát LMS_KB_IOT_DEEP.md. Cấu trúc Bloom: 4-4-2."}
    ]
    design_out, d_model = call_designer(design_input)
    print(f"  > Learning Design generated (Model: {d_model})")
    
    # 3. @engineer
    print("\n[STEP 3] @engineer is building...")
    engineer_input = [
        {"role": "system", "content": f"Learning Design:\n{design_out}"},
        {"role": "user", "content": "Hãy viết đề kiểm tra hoàn chỉnh định dạng Markdown. Bám sát terminologies trong KB."}
    ]
    engineer_out, e_model = call_pedagogical_engineer(engineer_input)
    print(f"  > Content generated (Model: {e_model})")
    
    # Save output
    output_path = "3-resources/distilled/LMS_Tests_Arduino_M1_Swarm_Demo.md"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(engineer_out)
    
    print(f"✅ Pipeline hoàn thành! Kết quả tại: {output_path}")

if __name__ == "__main__":
    run_pipeline()
