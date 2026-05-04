import os
import subprocess
import sys
import re
from pathlib import Path

# Đảm bảo in được tiếng Việt ra console
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

RAW_LMS_ROOT = Path(r"D:\NoteBookLLM_Br\brain\raw\Tổng hợp đề kiểm tra LMS")
WIKI_DIR = Path(r"d:\NoteBookLLM_Br\brain\wiki")
RAW_OUTPUT_DIR = Path(r"d:\NoteBookLLM_Br\brain\raw")

def get_category_info(path):
    parts = [p.lower() for p in path.parts]
    
    # Phân loại Module
    module = "Unknown"
    prefix = "GEN"
    
    if 'khoa học máy tính' in parts:
        prefix = "KHMT"
        if 'ai thcs' in parts: module = "AI_THCS"
        elif 'ai tiểu học' in parts: module = "AI_Tieu_hoc"
        elif 'python' in parts: module = "Python"
        elif 'scratch junior' in parts: module = "Scratch_Jr"
        elif 'scratch' in parts: module = "Scratch"
        elif 'tynker' in parts: module = "Tynker"
        else: module = "KHMT_General"
    elif 'robotics' in parts:
        prefix = "Robot"
        if 'codey' in parts: module = "Codey"
        elif 'gbot' in parts: module = "GBot"
        elif 'mbot' in parts: module = "mBot"
        elif 'rover' in parts: module = "Rover"
        elif 'xbot' in parts: module = "xBot"
        elif 'unplugged' in parts: module = "Unplugged"
        else: module = "Robotics_General"
    elif 'tự động hóa và iot' in parts:
        prefix = "IOT"
        if 'ai arduino' in parts: module = "AI_Arduino"
        elif 'arduino' in parts: module = "Arduino"
        elif 'halocode' in parts: module = "Halocode"
        elif 'yolobit' in parts: module = "YoloBit"
        else: module = "IOT_General"
    elif 'thiết kế và media' in parts:
        prefix = "DESIGN"
        if '3d tinkercad' in parts: module = "3D_Tinkercad"
        elif 'canva' in parts: module = "Canva"
        elif 'maker empire' in parts: module = "Maker_Empire"
        elif 'wordpress' in parts: module = "Wordpress"
        else: module = "Design_General"
        
    return prefix, module

def convert_file(doc_path):
    prefix, module = get_category_info(doc_path)
    filename_lower = doc_path.name.lower()
    
    # 1. Xử lý Đề Thực Hành -> EXAM
    if 'thực hành' in filename_lower:
        print(f"Converting Practical Exam: {doc_path.name}")
        th_match = re.search(r"(\d+)", doc_path.name)
        th_num = th_match.group(1) if th_match else "1"
        target_name = f"EXAM_{prefix}_{module}_TH{th_num}.md"
        target_path = RAW_OUTPUT_DIR / target_name
        
        try:
            subprocess.run(["npx", "-y", "mammoth", str(doc_path), str(target_path), "--output-format=markdown"], check=True, shell=True)
            # Thêm Header
            with open(target_path, "r", encoding="utf-8") as f:
                content = f.read()
            header = (
                "---\n"
                f'file_id: "{target_name[:-3]}"\n'
                f'title: "Đề thực hành {th_num} - {module}"\n'
                'category: "Practical Exam"\n'
                f'source: "[[{doc_path.name}]]"\n'
                'status: "verified"\n'
                "---\n\n"
            )
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(header + content)
            print(f"   -> Created {target_name}")
        except Exception as e:
            print(f"   !! Failed: {e}")

    # 2. Xử lý Đề Trắc Nghiệm -> Atoms (Chỉ xử lý nếu chưa có hoặc là file Scratch M1 De 2 bị thiếu)
    elif 'trắc nghiệm' in filename_lower or 'kiểm tra' in filename_lower:
        # Kiểm tra xem đã có atoms chưa (dựa trên Global Audit Report hoặc check file)
        # Ở đây ta ưu tiên xử lý các file chưa được audit
        print(f"Checking MCQ: {doc_path.name}")
        
        # Đặc biệt xử lý file Scratch M1 De 2 nếu trúng
        is_scratch_m1_de2 = "scratch m1" in filename_lower and "2" in filename_lower
        
        # Nếu muốn convert lại tất cả để đảm bảo đủ, ta có thể bỏ comment dòng dưới
        # process_mcq(doc_path, prefix, module)
        
        if is_scratch_m1_de2:
             process_mcq(doc_path, prefix, module)

def process_mcq(doc_path, prefix, module):
    print(f"   -> Splitting into atoms...")
    temp_md = Path(r"d:\NoteBookLLM_Br\brain\process\temp_split.md")
    try:
        subprocess.run(["npx", "-y", "mammoth", str(doc_path), str(temp_md), "--output-format=markdown"], check=True, shell=True)
    except:
        return

    with open(temp_md, "r", encoding="utf-8") as f:
        content = f.read()

    de_match = re.search(r"[Đđ]?ề\s?(\d+)", doc_path.name)
    if not de_match: de_match = re.search(r"(\d+)", doc_path.name)
    de_num = de_match.group(1) if de_match else "X"

    raw_questions = re.split(r'(?i)(?:\n|^).*?Câu\s?\d+', content)
    questions = [q.strip() for q in raw_questions[1:] if q.strip()]
    
    if not questions:
        raw_questions = re.split(r'\n\s*\d+[\.\:]', content)
        questions = [q.strip() for q in raw_questions[1:] if q.strip()]

    for i, q_text in enumerate(questions):
        q_num = i + 1
        filename = f"{prefix}_MCQ_{module}_De{de_num}_Q{q_num:02d}.md"
        target_path = WIKI_DIR / filename
        
        header = (
            "---\n"
            f'file_id: "{filename[:-3]}"\n'
            f'title: "Câu {q_num} - {module} De{de_num}"\n'
            'category: "Atomic Question"\n'
            f'source: "[[{doc_path.name}]]"\n'
            'status: "draft"\n'
            "---\n\n"
        )
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(header + f"## ❓ Câu hỏi {q_num}\n" + q_text)

def main():
    files = list(RAW_LMS_ROOT.rglob("*.docx"))
    print(f"Total files in RAW LMS: {len(files)}")
    for f in files:
        convert_file(f)
    print("\n--- Done ---")

if __name__ == "__main__":
    main()
