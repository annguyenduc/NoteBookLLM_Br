import os
import re
import sys
import zipfile
import shutil
from pathlib import Path
from docx import Document
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph

# Fix encoding for Windows terminal
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError: pass

# Configuration
WORKSPACE_ROOT = Path(r"d:\NoteBookLLM_Br")
DOCX_ROOT = WORKSPACE_ROOT / "brain" / "raw" / "Tổng hợp đề kiểm tra LMS"
ATOMS_DIR = WORKSPACE_ROOT / "brain" / "atoms"
ASSETS_DIR = WORKSPACE_ROOT / "brain" / "assets"
LOG_FILE = WORKSPACE_ROOT / "brain" / "log.md"

# Categories mapping
CATEGORY_MAP = {
    "AI": "AI",
    "Robotics": "ROBOT",
    "mBot": "ROBOT",
    "Codey": "ROBOT",
    "Rover": "ROBOT",
    "xBot": "ROBOT",
    "Thiết kế và Media": "MEDIA",
    "3D": "MEDIA",
    "Canva": "MEDIA",
    "Maker Empire": "MEDIA",
    "Tinkercad": "MEDIA",
    "Wordpress": "MEDIA",
    "Tự động hóa và IOT": "IOT",
    "Arduino": "IOT",
    "Halocode": "IOT",
    "YoloBit": "IOT",
    "Python": "CODE",
    "Scratch": "CODE",
    "Tynker": "CODE"
}

def get_category(path):
    # Check all parts of the path for keywords
    path_parts = path.replace("\\", "/").split("/")
    for part in reversed(path_parts):
        for key, code in CATEGORY_MAP.items():
            if key.lower() in part.lower():
                return code
    return "SYS"

def slugify(text):
    text = text.lower()
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    text = re.sub(r'[đ]', 'd', text)
    text = re.sub(r'[^a-z0-9\s-]', '_', text)
    text = re.sub(r'[\s_]+', '_', text).strip('_')
    return text

def get_image_rid_map(doc):
    rid_map = {}
    for rId, rel in doc.part.rels.items():
        if "image" in rel.reltype:
            rid_map[rId] = rel.target_ref
    return rid_map

def extract_image(rid, rid_map, zip_ref, output_prefix):
    # Case-insensitive lookup
    found_rid = None
    for k in rid_map.keys():
        if k.lower() == rid.lower():
            found_rid = k
            break
    if not found_rid: return None
    
    internal_path = rid_map[found_rid]
    ext = os.path.splitext(internal_path)[1]
    asset_name = f"IMG_{output_prefix}_{found_rid}{ext}"
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
            # Detect Question Start: "Câu 1", "Câu 1:", "Câu 1."
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
                # Check for images in the question line
                img_rids = re.findall(r'r:(?:embed|id|rid)="([^"]+)"', p._p.xml.lower())
                for rid in img_rids:
                    img_name = extract_image(rid, rid_map, zip_ref, file_prefix)
                    if img_name: current_q["images"].append(img_name)
                continue
            
            if current_q:
                # Detect Choice: "A/", "B.", "C-", "1/", "2."
                choice_match = re.match(r'^([A-E1-4])[\/\.\-\)]\s*(.*)$', text)
                
                # Detect Answer color in runs
                is_red = False
                for r in p.runs:
                    if r.font.color and r.font.color.rgb and str(r.font.color.rgb).upper() in ["FF0000", "C00000"]:
                        is_red = True
                        break
                
                # Also check images in this paragraph
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
                        if is_red and not current_q["answer"]:
                            # If non-choice text is red, it might be the answer marker
                            pass

        if current_q: questions.append(current_q)
    return questions

def create_atom_file(q, cat_code, file_slug, source_name):
    file_id = f"QUESTION_{cat_code}_{file_slug}_{q['num']}"
    filename = f"{file_id}.md"
    filepath = ATOMS_DIR / filename
    
    # Metadata
    tags = [cat_code, file_slug.split('_')[0]]
    if q['level'] != "N/A": tags.append(q['level'])
    
    content_lines = []
    content_lines.append("---")
    content_lines.append(f'file_id: "{file_id}"')
    content_lines.append(f'title: "{q["title"]}"')
    content_lines.append('category: "Atomic Question"')
    content_lines.append('prefix: "QUESTION"')
    content_lines.append(f'tags: {tags}')
    content_lines.append(f'source: "[[{source_name}]]"')
    content_lines.append(f'level: "{q["level"]}"')
    if q['answer']: content_lines.append(f'answer: "{q["answer"]}/"')
    content_lines.append('status: "draft"')
    content_lines.append(f'created: "2026-04-22"')
    content_lines.append("---")
    content_lines.append("")
    content_lines.append(f"# [QUESTION] {q['title']}")
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
    content_lines.append(f"- Kiến thức liên quan: [[WIKI_{cat_code}]]")
    content_lines.append("")
    content_lines.append("## 📖 Nguồn")
    content_lines.append(f"`📖 Nguồn: [{source_name}] — {q['num']}`")
    
    new_content = "\n".join(content_lines)
    
    # Audit logic
    if filepath.exists():
        old_content = filepath.read_text(encoding="utf-8")
        # Simple heuristic: if question text or choices changed, update
        # For now, just update and mark as draft if it was modified
        if "status: \"verified\"" in old_content:
            # Preserve verified status but update content? 
            # Or keep old if verified? User said "audit lại nội dung và wiki".
            # I'll update the content but keep the status for now, adding a note.
            new_content = new_content.replace('status: "draft"', 'status: "verified"')
            new_content += "\n\n<!-- [AUDIT] Updated content from re-extraction 2026-04-22 -->"
        
    filepath.write_text(new_content, encoding="utf-8")
    return filename

def main():
    if not ATOMS_DIR.exists(): ATOMS_DIR.mkdir(parents=True)
    if not ASSETS_DIR.exists(): ASSETS_DIR.mkdir(parents=True)
    
    count = 0
    for root, dirs, files in os.walk(DOCX_ROOT):
        cat_code = get_category(root)
        
        for f in files:
            if f.endswith(".docx") and not f.startswith("~$"):
                docx_path = os.path.join(root, f)
                file_slug = slugify(os.path.splitext(f)[0])
                print(f"Processing: {f} ({cat_code})")
                
                try:
                    questions = parse_docx(docx_path, file_slug)
                    for q in questions:
                        fname = create_atom_file(q, cat_code, file_slug, f)
                        count += 1
                except Exception as e:
                    print(f"Error processing {f}: {e}")

    print(f"Successfully processed {count} questions.")

if __name__ == "__main__":
    main()
