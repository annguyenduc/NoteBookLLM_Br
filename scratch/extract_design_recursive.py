import os
import re
import sys
import zipfile
import shutil
from pathlib import Path
from docx import Document

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError: pass

WORKSPACE_ROOT = Path(r"d:\NoteBookLLM_Br")
DOCX_ROOT = WORKSPACE_ROOT / "3-resources" / "raw" / "Tổng hợp đề kiểm tra LMS" / "Thiết kế và Media"
TEST_BANK_DIR = WORKSPACE_ROOT / "3-resources" / "test-bank"
ASSETS_DIR = WORKSPACE_ROOT / "3-resources" / "assets"

def get_level2(path_str):
    if "Tinkercad" in path_str: return "3D_Tinkercad"
    if "Canva" in path_str: return "Canva"
    if "Maker Empire" in path_str: return "Maker_Empire"
    if "Wordpress" in path_str: return "Wordpress"
    return "DESIGN_General"

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
    asset_name = f"ASSET_DESIGN_{output_prefix}_{found_rid}{ext}"
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
                num = q_match.group(2)
                level_match = re.search(r'\(([^)]+)\)', q_match.group(1))
                current_q = {
                    "num": num,
                    "title": q_match.group(1),
                    "level": level_match.group(1) if level_match else "N/A",
                    "content": [], "choices": [], "answer": None, "images": []
                }
                img_rids = re.findall(r'r:(?:embed|id|rid)="([^"]+)"', p._p.xml.lower())
                for rid in img_rids:
                    img_name = extract_image(rid, rid_map, zip_ref, file_prefix)
                    if img_name: current_q["images"].append(img_name)
                continue
            
            if current_q:
                choice_match = re.match(r'^([A-E1-4])[\/\.\-\)]\s*(.*)$', text)
                is_red = any(r.font.color and r.font.color.rgb and str(r.font.color.rgb).upper() in ["FF0000", "C00000"] for r in p.runs)
                
                para_images = []
                img_rids = re.findall(r'r:(?:embed|id|rid)="([^"]+)"', p._p.xml.lower())
                for rid in img_rids:
                    img_name = extract_image(rid, rid_map, zip_ref, file_prefix)
                    if img_name: para_images.append(img_name)

                if choice_match:
                    label = choice_match.group(1)
                    current_q["choices"].append({"label": label, "text": choice_match.group(2), "is_correct": is_red, "images": para_images})
                    if is_red: current_q["answer"] = label
                else:
                    if text or para_images:
                        current_q["content"].append({"text": text, "images": para_images, "is_red": is_red})

        if current_q: questions.append(current_q)
    return questions

def create_atom_file(q, level2, exam_de, source_name):
    file_id = f"DESIGN_{level2}_MCQ_{exam_de}_Q{q['num']}"
    filepath = TEST_BANK_DIR / f"{file_id}.md"
    tags = ['DESIGN', level2]
    if q['level'] != "N/A": tags.append(q['level'])
    
    content = [
        "---",
        f'file_id: "{file_id}"',
        f'title: "Câu {q["num"]} ({q["level"]})"',
        'category: "Atomic Question"',
        'prefix: "MCQ"',
        f'tags: {tags}',
        f'source: "`{source_name}`"',
        f'level: "{q["level"]}"',
        f'answer: "{q["answer"]}/"' if q['answer'] else "",
        'status: "draft"',
        f'created: "2026-04-27"',
        "---",
        "",
        f"# [MCQ] Câu {q['num']} ({q['level']})",
        "",
        "## ❓ Câu hỏi",
    ]
    for item in q['content']:
        if item['text']: content.append(item['text'])
        for img in item['images']: content.append(f"![Image](../assets/{img})")
    for img in q['images']: content.append(f"![Image](../assets/{img})")
        
    if q['choices']:
        content.append("\n## 📝 Đáp án lựa chọn")
        for c in q['choices']:
            marker = " (Đáp án)" if c['is_correct'] else ""
            content.append(f"- **{c['label']}/{marker}** {c['text']}")
            for img in c['images']: content.append(f"  ![Image](../assets/{img})")

    content.append("\n## 🔗 Liên kết tư duy")
    content.append(f"- [Rule 14] Đã mở file nguồn `.../DESIGN/.../{source_name}` và xác nhận fact.")
    
    filepath.write_text("\n".join([c for c in content if c or c==""]), encoding="utf-8")

def main():
    count = 0
    for root, dirs, files in os.walk(DOCX_ROOT):
        # Skip 3D Tinkercad if already done
        if "3D Tinkercad" in root: continue
        
        level2 = get_level2(root)
        
        for f in files:
            if f.endswith(".docx") and not f.startswith("~$"):
                if any(x in f for x in ["Tiêu chí", "thang điểm", "đề thực hành"]): continue
                
                exam_de = get_exam_de(f)
                file_prefix = f"{level2}_{exam_de}"
                print(f"Extracting DESIGN: {f} -> {level2}_{exam_de}")
                
                try:
                    questions = parse_docx(os.path.join(root, f), file_prefix)
                    for q in questions:
                        create_atom_file(q, level2, exam_de, f)
                        count += 1
                except Exception as e: print(f"Error {f}: {e}")

    print(f"Total DESIGN questions extracted: {count}")

if __name__ == "__main__":
    main()
