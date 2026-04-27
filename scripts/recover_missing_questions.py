import os
import re

WIKI_DIR = "brain/wiki"
RAW_DIR = "brain/raw"

MISSING = {
    "DESIGN_Wordpress_de_trac_nghiem_1_-_Wordpress.md": {
        "module": "DESIGN_Wordpress", "de": "De1", "qs": [2, 15, 16]
    },
    "DESIGN_Maker_Empire_3._de_trac_nghiem_3_-_maker_empire.md": {
        "module": "DESIGN_Maker_Empire", "de": "De3", "qs": [15]
    },
    "DESIGN_Maker_Empire_4._de_trac_nghiem_4_-_maker_empire.md": {
        "module": "DESIGN_Maker_Empire", "de": "De4", "qs": [15]
    },
    "IOT_AI_Arduino_de_trac_nghiem_1_-_ai_arduino.md": {
        "module": "IOT_AI_Arduino", "de": "De1", "qs": [13]
    },
    "IOT_Halocode_de_trac_nghiem_1_-_halocode.md": {
        "module": "IOT_Halocode", "de": "De1", "qs": [13, 24, 25, 27, 28, 29, 30]
    },
    "Robot_Rover_de_trac_nghiem_1_-_rover.md": {
        "module": "Robot_Rover", "de": "De1", "qs": [19]
    }
}

def create_question_file(module, de, q_num, content, raw_file):
    q_str = f"Q{q_num:02d}"
    filename = f"NEEDS_REVIEW_QUESTION_{module}_{de}_{q_str}.md"
    file_id = filename.replace(".md", "")
    
    path = os.path.join(WIKI_DIR, filename)
    body = content.strip()
    
    md = f"""---
file_id: "{file_id}"
title: "Câu {q_num}"
category: "Atomic Question"
prefix: "QUESTION"
tags: []
source: "3-resources/raw/{raw_file}"
level: "Unknown"
answer: ""
status: "needs_review"
created: "2026-04-23"
review_reason: "Được khôi phục thủ công từ file RAW gốc. Cần bóc tách lại phần đáp án."
---

# ❓ Câu hỏi
{body}

## 📝 Đáp án lựa chọn
*(Dữ liệu thô đang nằm trong phần Câu hỏi ở trên, vui lòng bóc tách thành các gạch đầu dòng A/ B/ C/ D/)*
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)

def main():
    recovered = 0
    for raw_file, info in MISSING.items():
        raw_path = os.path.join(RAW_DIR, raw_file)
        if not os.path.exists(raw_path):
            print(f"Missing raw file: {raw_file}")
            continue
            
        with open(raw_path, "r", encoding="utf-8") as f:
            raw_content = f.read()
            
        # Tìm từ khóa "Câu X" hoặc "Câu hỏi X"
        pattern = re.compile(r'(?:Câu|Câu hỏi)\s+(\d+)[^\n]*?(.*?)(?=(?:Câu|Câu hỏi)\s+\d+|$)', re.DOTALL | re.IGNORECASE)
        matches = pattern.findall(raw_content)
        
        found_qs = {}
        for match in matches:
            try:
                num = int(match[0])
                found_qs[num] = match[1]
            except:
                pass
                
        for q_num in info["qs"]:
            if q_num in found_qs:
                create_question_file(info["module"], info["de"], q_num, found_qs[q_num], raw_file)
                recovered += 1
            else:
                print(f"Could not find Q{q_num} in {raw_file}")
                
    print(f"Recovered {recovered} questions.")

if __name__ == "__main__":
    main()
