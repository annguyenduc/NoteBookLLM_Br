import os
import re
from docx import Document
import sys
import io

# Setup UTF-8 for terminal
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

RAW_DIR = r"d:\NoteBookLLM_Br\brain\raw"
ASSETS_DIR = r"d:\NoteBookLLM_Br\brain\assets"
DOCX_ROOT = os.path.join(RAW_DIR, "Tổng hợp đề kiểm tra LMS")

# Taxonomy mapping with keywords
TAXONOMY_CONFIG = [
    {
        "keyword": "Khoa học máy tính",
        "cat1": "KHMT",
        "sub_map": {
            "AI THCS": "AI_THCS",
            "AI Tiểu học": "AI_Tieu_hoc",
            "Python": "Python",
            "Scratch 1+2": "Scratch",
            "Scratch Junior": "Scratch_Jr",
            "Tynker": "Tynker"
        }
    },
    {
        "keyword": "Robotics",
        "cat1": "Robot",
        "sub_map": {
            "Codey 1+2": "Codey",
            "GBot": "GBot",
            "mBot 1+2": "mBot",
            "Rover": "Rover",
            "Unplugged Coding - Codey": "Unplugged",
            "Unplugged Coding - Rio": "Unplugged",
            "xBot": "xBot"
        }
    },
    {
        "keyword": "IOT",
        "cat1": "IOT",
        "sub_map": {
            "AI Arduino": "AI_Arduino",
            "Arduino 1+2": "Arduino",
            "Halocode": "Halocode",
            "YoloBit": "YoloBit"
        }
    },
    {
        "keyword": "Media",
        "cat1": "DESIGN",
        "sub_map": {
            "3D Tinkercad 1+2": "3D_Tinkercad",
            "Canva": "Canva",
            "Maker Empire": "Maker_Empire",
            "Web Wordpress": "Wordpress"
        }
    }
]

def slugify(text):
    text = text.lower()
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    text = re.sub(r'[đ]', 'd', text)
    text = re.sub(r'[^a-z0-9_\-\.]', '_', text)
    return re.sub(r'_+', '_', text).strip('_')

def get_taxonomy(root_path):
    for config in TAXONOMY_CONFIG:
        if config["keyword"].lower() in root_path.lower():
            cat1 = config["cat1"]
            # Detect sub-cat
            cat2 = "General"
            for sub_key, sub_val in config["sub_map"].items():
                if sub_key.lower() in root_path.lower():
                    cat2 = sub_val
                    break
            return cat1, cat2
    return None, None

def process_file(docx_path, cat1, cat2):
    filename = os.path.basename(docx_path)
    slug_name = slugify(os.path.splitext(filename)[0])
    md_filename = f"{cat1}_{cat2}_{slug_name}.md"
    md_path = os.path.join(RAW_DIR, md_filename)
    
    doc = Document(docx_path)
    rid_map = {}
    for r in doc.part.rels.values():
        if "image" in r.target_ref:
            rid_map[r.rId] = r.target_ref
            
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: \"{filename}\"\n")
        f.write(f"source: \"[[{filename}]]\"\n")
        f.write(f"category: \"{cat1}\"\n")
        f.write(f"sub_category: \"{cat2}\"\n")
        f.write("type: \"RAW_SOURCE\"\n")
        f.write("---\n\n")
        
        for p in doc.paragraphs:
            para_text = ""
            for run in p.runs:
                run_text = run.text
                color = run.font.color.rgb if run.font.color else None
                if color == (255, 0, 0):
                    run_text += " (Đáp án)"
                para_text += run_text
            
            f.write(para_text + "\n")
            
            img_rids = re.findall(r'r:(?:embed|id|rid)="([^"]+)"', p._p.xml, re.IGNORECASE)
            for rid in img_rids:
                found_rid = None
                for k in rid_map:
                    if k.lower() == rid.lower():
                        found_rid = k
                        break
                
                if found_rid:
                    internal_path = rid_map[found_rid]
                    ext = os.path.splitext(internal_path)[1]
                    asset_name = f"IMG_{cat1}_{cat2}_{slug_name}_{found_rid}{ext}"
                    asset_name = re.sub(r'[^\w\.\-]', '_', asset_name)
                    dest_path = os.path.join(ASSETS_DIR, asset_name)
                    
                    try:
                        import zipfile
                        with zipfile.ZipFile(docx_path) as z:
                            full_internal = internal_path
                            if not full_internal.startswith('word/'):
                                full_internal = 'word/' + full_internal
                            
                            with z.open(full_internal) as img_data:
                                with open(dest_path, "wb") as img_out:
                                    img_out.write(img_data.read())
                        
                        f.write(f"\n![Image](../assets/{asset_name})\n")
                    except Exception as e:
                        pass

    print(f"Created: {md_filename}")

def main():
    target_keyword = "Media"
    for root, dirs, files in os.walk(DOCX_ROOT):
        if target_keyword.lower() in root.lower():
            cat1, cat2 = get_taxonomy(root)
            if not cat1: continue
            
            for f in files:
                if f.endswith(".docx") and not f.startswith("~$"):
                    process_file(os.path.join(root, f), cat1, cat2)

if __name__ == "__main__":
    main()
