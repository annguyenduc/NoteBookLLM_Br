import os
import re

WIKI_DIR = os.path.join("3-resources", "wiki")

def standardize_item_bank():
    # Bộ từ khóa cực kỳ khắt khe để phân biệt Non-MCQ
    non_mcq_pattern = re.compile(r'(nối hình ảnh|dạng ghép nối|hãy ghép|nối tên với|sắp xếp thứ tự|nối cột|nối ô|kéo thả)', re.IGNORECASE)
    
    count_mcq = 0
    count_non_mcq = 0
    
    for filename in os.listdir(WIKI_DIR):
        # Chỉ xử lý các file bài tập
        is_needs_review = filename.startswith("NEEDS_REVIEW_")
        
        # Nhận diện prefix cũ
        if ("QUESTION_" in filename) or ("H5P_" in filename) or ("MCQ_" in filename) or ("NON_MCQ_" in filename):
            if filename == "index.md" or filename.startswith("WIKI_"):
                continue
                
            filepath = os.path.join(WIKI_DIR, filename)
            
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Phân loại dựa trên nội dung thực tế (sửa lỗi phân loại nhầm lúc nãy)
            is_non_mcq = bool(non_mcq_pattern.search(content))
            
            # Khởi tạo prefix đích
            target_prefix_short = "NON_MCQ" if is_non_mcq else "MCQ"
            target_prefix_full = f"NEEDS_REVIEW_{target_prefix_short}_" if is_needs_review else f"{target_prefix_short}_"
            
            # Xóa các rác tiền tố cũ để lấy core name
            core_name = filename
            for p in ["NEEDS_REVIEW_QUESTION_", "NEEDS_REVIEW_H5P_", "NEEDS_REVIEW_NON_MCQ_", "NEEDS_REVIEW_MCQ_", "QUESTION_", "H5P_", "NON_MCQ_", "MCQ_"]:
                if core_name.startswith(p):
                    core_name = core_name[len(p):]
                    break
                    
            new_filename = f"{target_prefix_full}{core_name}"
            new_file_id = new_filename.replace(".md", "")
            
            # --- Xử lý nội dung bên trong file ---
            # 1. Update file_id
            content = re.sub(r'file_id:\s*".*?"', f'file_id: "{new_file_id}"', content)
            
            # 2. Update prefix metadata
            content = re.sub(r'prefix:\s*".*?"', f'prefix: "{target_prefix_short}"', content)
            
            # 3. Update Title Header inside Markdown: # [QUESTION] Câu X -> # [MCQ] Câu X
            content = re.sub(r'# \[(QUESTION|H5P|MCQ|NON_MCQ)\]', f'# [{target_prefix_short}]', content)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
                
            if filename != new_filename:
                new_filepath = os.path.join(WIKI_DIR, new_filename)
                os.replace(filepath, new_filepath)
                
            if is_non_mcq:
                count_non_mcq += 1
            else:
                count_mcq += 1

    print(f"\n✅ Đã chuẩn hóa toàn bộ Item Bank:")
    print(f"   - {count_mcq} câu hỏi trắc nghiệm đa lựa chọn (MCQ)")
    print(f"   - {count_non_mcq} câu hỏi tương tác khác (NON-MCQ)")

if __name__ == "__main__":
    standardize_item_bank()

