import os
import sys
from docx import Document

# Cau hinh UTF-8 cho console
try:
    sys.stdout.reconfigure(encoding='utf-8')
except:
    pass

def extract_text(docx_path):
    try:
        doc = Document(docx_path)
        return "\n".join([p.text for p in doc.paragraphs])
    except:
        return ""

def restandardize_raw():
    recovery_dir = r"D:\NoteBookLLM_Br\brain\raw_recovery"
    target_raw_dir = r"D:\NoteBookLLM_Br\brain\raw"
    
    # Tao thu muc neu chua co
    if not os.path.exists(target_raw_dir):
        os.makedirs(target_raw_dir)
    
    for root, dirs, files in os.walk(recovery_dir):
        for f in files:
            if not f.endswith(".docx"): continue
            
            docx_path = os.path.join(root, f)
            # Giu nguyen ten file .md nhu cu (f + .md)
            md_name = f + ".md"
            target_path = os.path.join(target_raw_dir, md_name)
            
            content = extract_text(docx_path)
            if not content: continue
            
            # YAML tieu chuan
            md_content = f"--- \ntitle: {f}\nsource: [[{f}]]\ntype: RAW_SOURCE\n---\n\n"
            md_content += content
            
            with open(target_path, "w", encoding="utf-8") as out:
                out.write(md_content)

if __name__ == "__main__":
    restandardize_raw()
