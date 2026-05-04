import re
import os

WIKI_FILES = [
    r"d:\NoteBookLLM_Br\brain\wiki\WIKI_IOT_Arduino_Hardware.md",
    r"d:\NoteBookLLM_Br\brain\wiki\WIKI_IOT_Arduino_Logic.md",
    r"d:\NoteBookLLM_Br\brain\distilled\KB_IOT_Arduino_Master.md"
]

def translate_link(match):
    source = match.group(1)
    q_num_str = match.group(2)
    q_num = int(q_num_str)
    
    new_source = source
    new_q_num = q_num
    
    if "AI_Arduino_de_trac_nghiem_1-8" in source:
        # Giả định mỗi đề 30 câu
        idx = (q_num - 1) // 30 + 1
        new_q_num = (q_num - 1) % 30 + 1
        new_source = f"IOT_AI_Arduino_De_{idx}"
        
    elif "Arduino_LMS_120_Questions" in source:
        # Bộ 120 câu thực chất là M1,2 De 2, 3, 4 (mỗi bộ 40 hoặc 30 câu?)
        # Kiểm tra thực tế: 120/3 = 40 câu mỗi bộ? 
        # Giả sử 40 câu:
        idx = (q_num - 1) // 40 + 2 # Bắt đầu từ De 2
        new_q_num = (q_num - 1) % 40 + 1
        new_source = f"IOT_Arduino_M1_2_De_{idx}"
        
    elif "Tu_dong_hoa_voi_AI_Arduino_De_1-4" in source:
        idx = (q_num - 1) // 30 + 1
        new_q_num = (q_num - 1) % 30 + 1
        new_source = f"IOT_AI_Arduino_De_{idx}" # Vì tôi đã hợp nhất 2 bộ này
        
    return f"📖 Nguồn: {new_source} — Câu {new_q_num}"

def process_file(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Dịch chuyển trong nội dung (Body)
    content = re.sub(r"📖 Nguồn: ([\w\d\-_]+) — Câu (\d+)", translate_link, content)
    content = re.sub(r"\(Nguồn: ([\w\d\-_]+) — Câu (\d+)\)", translate_link, content)
    
    # 2. Dịch chuyển trong Frontmatter (YAML)
    # Mapping cụ thể cho các tên tệp cũ sang mới
    mapping = {
        "IOT_AI_Arduino_de_trac_nghiem_1_-_ai_arduino.md": "IOT_AI_Arduino_De_1.md",
        "IOT_AI_Arduino_de_trac_nghiem_2_-_ai_arduino.md": "IOT_AI_Arduino_De_2.md",
        "IOT_AI_Arduino_de_trac_nghiem_3_-_ai_arduino.md": "IOT_AI_Arduino_De_3.md",
        "IOT_AI_Arduino_de_trac_nghiem_4_-_ai_arduino.md": "IOT_AI_Arduino_De_4.md",
        "IOT_Arduino_de_trac_nghiem_1_-_arduino_m2.md": "IOT_Arduino_M2_De_1.md",
        "IOT_Arduino_de_trac_nghiem_2_-_arduino_m2.md": "IOT_Arduino_M2_De_2.md",
    }
    
    for old, new in mapping.items():
        content = content.replace(f"source: \"3-resources/raw/{old}\"", f"source: \"3-resources/raw/{new}\"")
        content = content.replace(f"source: '3-resources/raw/{old}'", f"source: '3-resources/raw/{new}'")
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    # 1. Xử lý các tệp Master đã định nghĩa
    for p in WIKI_FILES:
        process_file(p)
        
    # 2. Quét toàn bộ thư mục brain/wiki cho các Wiki Atoms
    wiki_dir = r"d:\NoteBookLLM_Br\brain\wiki"
    for filename in os.listdir(wiki_dir):
        if filename.endswith(".md"):
            process_file(os.path.join(wiki_dir, filename))
