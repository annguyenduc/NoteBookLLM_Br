import os
import re

WIKI_DIR = r"d:\NoteBookLLM_Br\brain\wiki"

def get_device(content):
    if "Halocode" in content or "halocode" in content:
        return "Halocode"
    if "YOLOBIT" in content or "Yolobit" in content or "YoloBit" in content:
        return "Yolobit"
    if "Arduino" in content or "arduino" in content:
        return "Arduino"
    return "IOT"

def sanitize():
    files = [f for f in os.listdir(WIKI_DIR) if f.startswith("MCQ_IOT_De")]
    print(f"Found {len(files)} ambiguous files.")
    
    for filename in files:
        path = os.path.join(WIKI_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Trích xuất thông tin từ tệp
        device = get_device(content)
        
        # Tìm Đề và Câu từ tên tệp hoặc nội dung
        match = re.search(r"De(\d+)_Q(\d+)", filename)
        if not match:
            continue
            
        de_num = match.group(1)
        q_num = match.group(2)
        
        new_filename = f"MCQ_{device}_De{de_num}_Q{q_num}.md"
        new_path = os.path.join(WIKI_DIR, new_filename)
        
        # Nếu file mới đã tồn tại (do có bản v2, v3...), chúng ta cần kiểm tra nội dung
        if os.path.exists(new_path):
            # Tạm thời append _v nếu thực sự khác nhau, hoặc skip nếu trùng
            # Trong trường hợp này, vì chúng ta đang dọn dẹp, tôi sẽ ưu tiên giữ bản có nội dung dài nhất 
            # hoặc bản mới nhất.
            with open(new_path, "r", encoding="utf-8") as f_existing:
                existing_content = f_existing.read()
            
            if len(content) > len(existing_content):
                # Thay thế bản cũ bằng bản mới tốt hơn
                os.remove(new_path)
            else:
                # Bản cũ tốt hơn hoặc bằng, xóa bản hiện tại (bản đang loop)
                os.remove(path)
                continue

        # Cập nhật file_id trong nội dung
        new_content = content.replace(f'file_id: "{filename[:-3]}"', f'file_id: "{new_filename[:-3]}"')
        
        # Ghi file mới và xóa file cũ
        with open(new_path, "w", encoding="utf-8") as f_out:
            f_out.write(new_content)
        
        if path != new_path:
            os.remove(path)
            print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    sanitize()
