import os
import subprocess
import sys
import re
from pathlib import Path

# Đảm bảo in được tiếng Việt ra console
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

RAW_ROOT = Path(r"D:\NoteBookLLM_Br\brain\raw\Tổng hợp đề kiểm tra LMS\Khoa học máy tính")
WIKI_DIR = Path(r"d:\NoteBookLLM_Br\brain\wiki")

def get_module_name(path):
    parts = path.parts
    if 'AI THCS' in parts: return "AI_THCS"
    if 'AI Tiểu học' in parts: return "AI_Tieu_hoc"
    if 'Python' in parts: return "Python"
    if 'Scratch Junior' in parts: return "Scratch_Jr"
    if 'Scratch 1+2' in parts or 'Scratch' in parts: return "Scratch"
    if 'Tynker' in parts: return "Tynker"
    return "Unknown"

def convert():
    files = list(RAW_ROOT.rglob("*.docx"))
    print(f"Total KHMT files to process: {len(files)}")
    
    for doc_path in files:
        module = get_module_name(doc_path)
        if module == "Unknown": continue
        
        de_match = re.search(r"[Đđ]?ề\s?(\d+)", doc_path.name)
        if not de_match:
            de_match = re.search(r"(\d+)", doc_path.name)
        de_num = de_match.group(1) if de_match else "X"
        
        print(f"Processing: {doc_path.name} (Module: {module}, De: {de_num})")
        
        temp_md = Path(r"d:\NoteBookLLM_Br\brain\process\temp_khmt.md")
        try:
            # Dùng format markdown để dễ xử lý hơn HTML
            subprocess.run(["npx", "-y", "mammoth", str(doc_path), str(temp_md), "--output-format=markdown"], check=True, shell=True)
        except:
            print(f"Failed to convert {doc_path.name}")
            continue
            
        with open(temp_md, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Chia theo "Câu X" (Chấp nhận cả escape \-, __, **, ###)
        # Regex tìm: Câu + Khoảng trắng + Số
        raw_questions = re.split(r'(?i)(?:\n|^).*?Câu\s?\d+', content)
        
        questions = [q.strip() for q in raw_questions[1:] if q.strip()]
        
        if not questions:
            # Fallback 2: Nếu vẫn hỏng, thử tách theo số thứ tự dòng đơn thuần
            raw_questions = re.split(r'\n\s*\d+[\.\:]', content)
            questions = [q.strip() for q in raw_questions[1:] if q.strip()]

        for i, q_text in enumerate(questions):
            q_num = i + 1
            filename = f"KHMT_MCQ_{module}_De{de_num}_Q{q_num:02d}.md"
            target_path = WIKI_DIR / filename
            
            header_str = (
                "---\n"
                f'file_id: "{filename[:-3]}"\n'
                f'title: "Câu {q_num} - {module} De{de_num}"\n'
                'category: "Atomic Question"\n'
                'prefix: "KHMT"\n'
                f"tags: ['KHMT', '{module}']\n"
                f'source: "[[{doc_path.name}]]"\n'
                'status: "draft"\n'
                'created: "2026-04-25"\n'
                "---\n\n"
            )
            
            with open(target_path, "w", encoding="utf-8") as f_out:
                f_out.write(header_str)
                f_out.write(f"## ❓ Câu hỏi {q_num}\n")
                f_out.write(q_text)
                
    print("Conversion complete.")

if __name__ == "__main__":
    convert()
