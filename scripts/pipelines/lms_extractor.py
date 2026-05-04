import os
import sys
import re
from docx import Document
from docx.document import Document as _Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph

def slugify(text):
    text = text.lower()
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    text = re.sub(r'[đ]', 'd', text)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text).strip('-')
    return text

def extract_content(doc_path, output_dir):
    if not os.path.exists(doc_path): return None
    doc = Document(doc_path)
    original_name = os.path.splitext(os.path.basename(doc_path))[0]
    safe_name = slugify(original_name)
    rel_media_path = os.path.join("media", safe_name)
    abs_media_dir = os.path.join(output_dir, rel_media_path)
    os.makedirs(abs_media_dir, exist_ok=True)
    content = []
    rid_to_file = {}
    for rel in doc.part.rels.values():
        if "image" in rel.target_ref:
            img_data = rel.target_part.blob
            img_ext = os.path.splitext(rel.target_ref)[1]
            img_name = f"{rel.rId}{img_ext}"
            with open(os.path.join(abs_media_dir, img_name), "wb") as f:
                f.write(img_data)
            rid_to_file[rel.rId] = f"media/{safe_name}/{img_name}".replace("\\", "/")

    def iter_block_items(parent):
        if isinstance(parent, _Document): parent_elm = parent.element.body
        elif isinstance(parent, _Cell): parent_elm = parent._tc
        else: raise ValueError("Invalid parent")
        for child in parent_elm.iterchildren():
            if isinstance(child, CT_P): yield Paragraph(child, parent)
            elif isinstance(child, CT_Tbl): yield Table(child, parent)

    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            images = []
            for run in block.runs:
                rids = re.findall(r'r:embed="(rId\d+)"', run._element.xml)
                for rid in rids:
                    if rid in rid_to_file: images.append(f"![Visual]({rid_to_file[rid]})")
            text = block.text.strip()
            if text: content.append(text)
            if images: content.extend(images)
        elif isinstance(block, Table):
            rows = [" | ".join([cell.text.strip() for cell in r.cells]) for r in block.rows]
            content.append("\n" + "\n".join(rows) + "\n")
    return "\n".join(content)

if __name__ == "__main__":
    if len(sys.argv) < 3: sys.exit(1)
    target_dir = sys.argv[2]
    original_name = os.path.splitext(os.path.basename(sys.argv[1]))[0]
    safe_output_name = slugify(original_name) + ".md"
    output_path = os.path.join(target_dir, safe_output_name)
    raw_content = extract_content(sys.argv[1], target_dir)
    if raw_content:
        lines = raw_content.split('\n')
        processed = []
        for line in lines:
            if re.match(r'^C\u00e2u \d+[:.]', line, re.IGNORECASE): processed.append(f"\n### {line}")
            elif re.match(r'^[A-D][:./]', line): processed.append(f"- {line}")
            else: processed.append(line)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(processed))
        # Không print output_path trực tiếp vì lỗi Unicode terminal
        print("Done.")
