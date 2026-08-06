import os
import re
from docx import Document

def extract_from_docx(docx_path):
    doc = Document(docx_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)

def process_arduino_m1():
    raw_dir = r"D:\NoteBookLLM_Br\brain\raw_recovery"
    atom_dir = r"D:\NoteBookLLM_Br\brain\atoms"
    
    m1_file = ""
    for root, dirs, files in os.walk(raw_dir):
        for f in files:
            if "Arduino module 1" in f and f.endswith(".docx"):
                m1_file = os.path.join(root, f)
                break
    
    if not m1_file:
        print("Không tìm thấy file Module 1")
        return

    content = extract_from_docx(m1_file)
    current_level = "Thông hiểu"
    sections = re.split(r"(Phần\s+\d+:.*?|Câu\s+\d+:)", content, flags=re.IGNORECASE)
    
    for i in range(1, len(sections), 2):
        header = sections[i].strip()
        body = sections[i+1].strip() if i+1 < len(sections) else ""
        
        if header.lower().startswith("phần"):
            if "nhận biết" in header.lower(): current_level = "Nhận biết"
            elif "thông hiểu" in header.lower(): current_level = "Thông hiểu"
            continue
            
        if header.lower().startswith("câu"):
            match = re.search(r"(\d+)", header)
            if not match: continue
            q_num = match.group(1).zfill(2)
            
            q_text_raw = header.split(":", 1)[1].strip() if ":" in header else ""
            lines = body.split("\n")
            options = []
            for line in lines:
                if re.match(r"^[A-F][\./]", line.strip()):
                    options.Add(line.strip()) if hasattr(options, 'Add') else options.append(line.strip())
                elif line.strip():
                    q_text_raw += "\n" + line.strip()
            
            file_id = f"QUESTION_IOT_Arduino_M1_D1_{q_num}"
            file_path = os.path.join(atom_dir, f"{file_id}.md")
            
            q_title = q_text_raw[:40].replace('\n', ' ')
            
            template = """---
file_id: "{0}"
title: "Câu {1}: {2}..."
category: "Atomic Question"
prefix: "QUESTION"
tags: ["Arduino", "Module 1", "{3}"]
source: "[[{4}]]"
level: "{3}"
status: "verified"
created: "2026-04-22"
---

# ❓ Câu hỏi
{5}

## 📝 Đáp án lựa chọn
"""
            atom_content = template.format(file_id, q_num, q_title, current_level, os.path.basename(m1_file), q_text_raw.strip())
            for opt in options:
                atom_content += f"- {opt}\n"
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(atom_content)
            print(f"Cập nhật: {file_id}")

if __name__ == "__main__":
    process_arduino_m1()
