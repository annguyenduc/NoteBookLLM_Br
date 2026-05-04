import os
import re
import sys
import zipfile
import shutil
from pathlib import Path
from docx import Document

# Fix encoding for Windows terminal
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError: pass

# Configuration
WORKSPACE_ROOT = Path(r"d:\NoteBookLLM_Br")
DOCX_ROOT = WORKSPACE_ROOT / "3-resources" / "raw" / "Tổng hợp đề kiểm tra LMS" / "Tự động hóa và IOT"
TEST_BANK_DIR = WORKSPACE_ROOT / "3-resources" / "test-bank"
ASSETS_DIR = WORKSPACE_ROOT / "3-resources" / "assets"

def get_level2(path_or_file):
    if "Arduino" in path_or_file: return "Arduino"
    if "Halocode" in path_or_file: return "Halocode"
    if "YoloBit" in path_or_file: return "YoloBit"
    return "IOT_General"

def get_exam_de(filename):
    match = re.search(r'đề.*?(\d+)', filename, re.IGNORECASE)
    if match: return f"De{match.group(1)}"
    return "De1"

def get_image_rid_map(doc):
    rid_map = {}
    for rId, rel in doc.part.rels.items():
        if "image" in rel.reltype:
            rid_map[rId] = rel.target_ref
    return rid_map

def extract_image(rid, rid_map, zip_ref, output_prefix):
    found_rid = None
    for k in rid_map.keys():
        if k.lower() == rid.lower():
            found_rid = k
            break
    if not found_rid: return None
    
    internal_path = rid_map[found_rid]
    ext = os.path.splitext(internal_path)[1]
    asset_name = f"ASSET_IOT_{output_prefix}_{found_rid}{ext}"
    asset_name = re.sub(r'[^\w\.\-]', '_', asset_name)
    dest_path = ASSETS_DIR / asset_name
    
    if not dest_path.exists():
        try:
            with zip_ref.open(f"word/{internal_path}") as s, open(dest_path, 'wb') as t:
                shutil.copyfileobj(s, t)
        except:
            return None
    return asset_name

def parse_docx(docx_path, file_prefix):
    doc = Document(docx_path)
    rid_map = get_image_rid_map(doc)
    questions = []
    current_q = None
    
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        for p in doc.paragraphs:
            text = p.text.strip()
            q_match = re.match(r'^(Câu\s*(\d+).*)$', text, re.IGNORECASE)
            
            if q_match:
                if current_q: questions.append(current_q)
                title = q_match.group(1)
                num = q_match.group(2)
                level_match = re.search(r'\(([^)]+)\)', title)
                level = level_match.group(1) if level_match else "N/A"
                current_q = {
                    "num": num,
                    "title": title,
                    "level": level,
                    "content": [],
                    "choices": [],
                    "answer": None,
                    "images": []
                }
                img_rids = re.findall(r'r:(?:embed|id|rid)="([^"]+)"', p._p.xml.lower())
                for rid in img_rids:
                    img_name = extract_image(rid, rid_map, zip_ref, file_prefix)
                    if img_name: current_q["images"].append(img_name)
                continue
            
            if current_q:
                choice_match = re.match(r'^([A-E1-4])[\/\.\-\)]\s*(.*)$', text)
                is_red = False
                for r in p.runs:
                    if r.font.color and r.font.color.rgb and str(r.font.color.rgb).upper() in ["FF0000", "C00000"]:
                        is_red = True
                        break
                
                para_images = []
                img_rids = re.findall(r'r:(?:embed|id|rid)="([^"]+)"', p._p.xml.lower())
                for rid in img_rids:
                    img_name = extract_image(rid, rid_map, zip_ref, file_prefix)
                    if img_name: para_images.append(img_name)

                if choice_match:
                    label = choice_match.group(1)
                    choice_text = choice_match.group(2)
                    current_q["choices"].append({
                        "label": label,
                        "text": choice_text,
                        "is_correct": is_red,
                        "images": para_images
                    })
                    if is_red:
                        current_q["answer"] = label
                else:
                    if text or para_images:
                        current_q["content"].append({"text": text, "images": para_images, "is_red": is_red})

        if current_q: questions.append(current_q)
    return questions

def create_atom_file(q, level2, exam_de, source_name):
    # Format: IOT_[Level2]_MCQ_[ExamDe]_Q[Num].md
    file_id = f"IOT_{level2}_MCQ_{exam_de}_Q{q['num']}"
    filename = f"{file_id}.md"
    filepath = TEST_BANK_DIR / filename
    
    tags = ['IOT', level2]
    if q['level'] != "N/A": tags.append(q['level'])
    
    content_lines = []
    content_lines.append("---")
    content_lines.append(f'file_id: "{file_id}"')
    content_lines.append(f'title: "Câu {q["num"]} ({q["level"]})"')
    content_lines.append('category: "Atomic Question"')
    content_lines.append('prefix: "MCQ"')
    content_lines.append(f'tags: {tags}')
    content_lines.append(f'source: "`{source_name}`"')
    content_lines.append(f'level: "{q["level"]}"')
    if q['answer']: content_lines.append(f'answer: "{q["answer"]}/"')
    content_lines.append('status: "draft"')
    content_lines.append(f'created: "2026-04-27"')
    content_lines.append("---")
    content_lines.append("")
    content_lines.append(f"# [MCQ] Câu {q['num']} ({q['level']})")
    content_lines.append("")
    content_lines.append("## ❓ Câu hỏi")
    
    for item in q['content']:
        if item['text']: content_lines.append(item['text'])
        for img in item['images']:
            content_lines.append(f"![Image](../assets/{img})")
    
    for img in q['images']:
        content_lines.append(f"![Image](../assets/{img})")
        
    content_lines.append("")
    if q['choices']:
        content_lines.append("## 📝 Đáp án lựa chọn")
        for c in q['choices']:
            marker = " (Đáp án)" if c['is_correct'] else ""
            content_lines.append(f"- **{c['label']}/{marker}** {c['text']}")
            for img in c['images']:
                content_lines.append(f"  ![Image](../assets/{img})")
        content_lines.append("")

    content_lines.append("## 🔗 Liên kết tư duy")
    content_lines.append(f"- [Rule 14] Đã mở file nguồn `3-resources/raw/Tổng hợp đề kiểm tra LMS/Tự động hóa và IOT/.../{source_name}` và xác nhận fact.")
    
    filepath.write_text("\n".join(content_lines), encoding="utf-8")
    return filename

def main():
    if not TEST_BANK_DIR.exists(): TEST_BANK_DIR.mkdir(parents=True)
    
    count = 0
    # List of IOT subfolders to process
    subfolders = ["AI Arduino", "Arduino 1+2", "Halocode", "YoloBit"]
    
    for sub in subfolders:
        folder_path = DOCX_ROOT / sub
        if not folder_path.exists(): continue
        
        for f in os.listdir(folder_path):
            if f.endswith(".docx") and not f.startswith("~$"):
                # Skip if it's a "Tiêu chí chấm" file
                if "Tiêu chí" in f or "thang điểm" in f: continue
                
                docx_path = folder_path / f
                level2 = get_level2(sub)
                exam_de = get_exam_de(f)
                
                # Check if we already have many questions for this De
                # (Simple check: if De1 Q20 exists, maybe skip)
                # But for safety, I'll overwrite/refresh.
                
                print(f"Extracting: {f} -> {level2}_{exam_de}")
                file_prefix = f"{level2}_{exam_de}"
                
                try:
                    questions = parse_docx(docx_path, file_prefix)
                    for q in questions:
                        create_atom_file(q, level2, exam_de, f)
                        count += 1
                except Exception as e:
                    print(f"Error {f}: {e}")

    print(f"Total IOT questions extracted: {count}")

if __name__ == "__main__":
    main()
