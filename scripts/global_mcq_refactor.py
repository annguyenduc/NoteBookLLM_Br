import os
import re

WIKI_DIR = r"d:\NoteBookLLM_Br\brain\wiki"

def get_device(content, filename):
    content_lower = content.lower()
    if "halocode" in content_lower: return "Halocode"
    if "yolobit" in content_lower or "yolo bit" in content_lower: return "Yolobit"
    if "arduino" in content_lower: return "Arduino"
    return "Unknown"

def refactor():
    # Lấy tất cả tệp trắc nghiệm (bắt đầu bằng MCQ_ hoặc IOT_MCQ_)
    files = [f for f in os.listdir(WIKI_DIR) if f.startswith("MCQ_") or f.startswith("IOT_MCQ_")]
    print(f"Total MCQ files found: {len(files)}")
    
    mapping_store = {} # (Device, De, Q) -> [list of (filepath, version, length)]

    for filename in files:
        path = os.path.join(WIKI_DIR, filename)
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except:
            continue
            
        device = get_device(content, filename)
        if device == "Unknown":
            continue
            
        # Tìm Đề và Câu
        match = re.search(r"De(\d+)_Q(\d+)", filename)
        if not match:
            continue
        de_num = int(match.group(1))
        q_num = int(match.group(2))
        
        # Tìm version nếu có (_vX)
        v_match = re.search(r"_v(\d+)", filename)
        version = int(v_match.group(1)) if v_match else 0
        
        key = (device, de_num, q_num)
        if key not in mapping_store:
            mapping_store[key] = []
        mapping_store[key].append({
            "path": path,
            "filename": filename,
            "version": version,
            "length": len(content),
            "content": content
        })

    # Xử lý dọn dẹp và đổi tên
    for key, variants in mapping_store.items():
        device, de, q = key
        # Chọn bản tốt nhất (ưu tiên version cao nhất, sau đó là nội dung dài nhất)
        best = sorted(variants, key=lambda x: (x["version"], x["length"]), reverse=True)[0]
        
        new_filename = f"IOT_MCQ_{device}_De{de}_Q{q:02d}.md" # Q01 thay vì Q1 để sort đẹp hơn
        new_path = os.path.join(WIKI_DIR, new_filename)
        
        # Cập nhật nội dung (file_id)
        new_content = best["content"].replace(f'file_id: "{best["filename"][:-3]}"', f'file_id: "{new_filename[:-3]}"')
        
        # Lưu bản tốt nhất
        with open(new_path, "w", encoding="utf-8") as f_out:
            f_out.write(new_content)
        
        # Xóa tất cả các bản cũ (bao gồm cả bản vừa copy nếu tên khác)
        for v in variants:
            if v["path"] != new_path:
                try:
                    os.remove(v["path"])
                except:
                    pass

    print("Refactoring complete.")

if __name__ == "__main__":
    refactor()
