import os
import re
import sys
from docx import Document

# Ép đầu ra console sang UTF-8 để không bị lỗi print
sys.stdout.reconfigure(encoding='utf-8')

def extract_from_docx(docx_path):
    doc = Document(docx_path)
    return "\n".join([p.text for p in doc.paragraphs])

def process_exams():
    raw_dir = r"D:\NoteBookLLM_Br\brain\raw_recovery"
    atom_dir = r"D:\NoteBookLLM_Br\brain\atoms"
    
    # Quét tất cả file docx trong recovery
    for root, dirs, files in os.walk(raw_dir):
        for f in files:
            if not f.endswith(".docx") or "Arduino" not in f:
                continue
            
            docx_path = os.path.join(root, f)
            print(f"Xu ly: {f}")
            content = extract_from_docx(docx_path)
            
            # Xác định Module
            mod = "M1"
            if "M2" in f or "Arduino 2" in f: mod = "M2"
            
            # Xác định Đề
            exam_num = "D1"
            match_e = re.search(r"(\d+)", f)
            if match_e: exam_num = "D" + match_e.group(1)

            current_level = "Thông hiểu"
            sections = re.split(r"(Ph.*?n\s+\d+:.*?|C.*?u\s+\d+:)", content, flags=re.IGNORECASE)
            
            for i in range(1, len(sections), 2):
                header = sections[i].strip()
                body = sections[i+1].strip() if i+1 < len(sections) else ""
                
                if "Phần" in header or "Ph" in header:
                    if "nhận biết" in header.lower(): current_level = "Nhận biết"
                    elif "thông hiểu" in header.lower(): current_level = "Thông hiểu"
                    continue
                
                if "Câu" in header or "C" in header:
                    match_q = re.search(r"(\d+)", header)
                    if not match_q: continue
                    q_num = match_q.group(1).zfill(2)
                    
                    q_text = header.split(":", 1)[1].strip() if ":" in header else ""
                    lines = body.split("\n")
                    options = []
                    for l in lines:
                        if re.match(r"^[A-F][\./]", l.strip()):
                            options.append(l.strip())
                        elif l.strip():
                            q_text += "\n" + l.strip()
                    
                    file_id = f"QUESTION_IOT_Arduino_{mod}_{exam_num}_{q_num}"
                    file_path = os.path.join(atom_dir, f"{file_id}.md")
                    
                    # Tạo nội dung Atom chuẩn
                    atom_content = f"--- \nfile_id: \"{file_id}\"\n"
                    atom_content += f"title: \"Câu {q_num}: {q_text[:40].replace(chr(10), ' ')}...\"\n"
                    atom_content += f"category: \"Atomic Question\"\nprefix: \"QUESTION\"\n"
                    atom_content += f"tags: [\"Arduino\", \"Module {mod}\", \"{current_level}\"]\n"
                    atom_content += f"source: \"[[{f}]]\"\nlevel: \"{current_level}\"\n"
                    atom_content += f"status: \"verified\"\ncreated: \"2026-04-22\"\n---\n\n"
                    atom_content += f"# ❓ Câu hỏi\n{q_text.strip()}\n\n## 📝 Đáp án lựa chọn\n"
                    for opt in options:
                        atom_content += f"- {opt}\n"
                    
                    with open(file_path, "w", encoding="utf-8") as out:
                        out.write(atom_content)

if __name__ == "__main__":
    process_exams()
