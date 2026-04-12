import os
import glob
import sys
import zipfile
import shutil
import re
from docx import Document
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError: pass

BASE_DIR = r"d:\NoteBookLLM_Br"
SOURCE_DOCX_DIR = os.path.join(BASE_DIR, "brain", "archive", "raw_docx")
RAW_DIR = os.path.join(BASE_DIR, "brain", "raw")
ASSETS_DIR = os.path.join(BASE_DIR, "brain", "assets")

def sanitize_filename(name):
    return re.sub(r'[\s\[\]\(\)]', '_', name)

def get_image_rid_map(doc):
    rid_map = {}
    for rId, rel in doc.part.rels.items():
        if "image" in rel.reltype: rid_map[rId] = rel.target_ref
    return rid_map

def extract_and_link_images(xml_content, rid_map, zip_ref, output_prefix):
    links = []
    rids = re.findall(r'r:(?:embed|id|rid)="([^"]+)"', xml_content.lower())
    seen = set()
    for rid_raw in rids:
        # Match case-insensitively but use original key
        found_rid = None
        for k in rid_map.keys():
            if k.lower() == rid_raw.lower():
                found_rid = k
                break
        if found_rid and found_rid not in seen:
            seen.add(found_rid)
            internal_path = rid_map[found_rid]
            asset_name = f"{output_prefix}_{found_rid}{os.path.splitext(internal_path)[1]}"
            asset_name = sanitize_filename(asset_name)
            dest_path = os.path.join(ASSETS_DIR, asset_name)
            if not os.path.exists(dest_path):
                try:
                    with zip_ref.open(f"word/{internal_path}") as s, open(dest_path, 'wb') as t:
                        shutil.copyfileobj(s, t)
                except: pass
            links.append(f"![Image](../assets/{asset_name})")
    return links

def split_and_atomize(text):
    # Regex handles A/ B. C) 1. 2/ and potential trailing whitespace
    # Using a capture group to keep the separator in the split list
    patterns = r'([A-E1-4][/\.\)\\\-]\s*)'
    splits = re.split(patterns, text)
    parts = []
    for s in splits:
        if s.strip(): parts.append(s.strip())
    return parts

def is_choice_label(text):
    return bool(re.match(r'^[A-E1-4][/\.\)\\\-]$', text.strip()))

def convert_to_md(docx_path):
    base_name = os.path.basename(docx_path)
    img_prefix = base_name.replace("LMS_RAW_", "LMS_IMG_").replace(".docx", "")
    doc = Document(docx_path)
    rid_map = get_image_rid_map(doc)
    md_path = os.path.join(RAW_DIR, base_name.replace(".docx", ".md"))
    
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        def process_container(container):
            blocks = []
            parent_elm = container.element.body if container == doc else container._tc
            for child in parent_elm.iterchildren():
                if isinstance(child, CT_P):
                    p = Paragraph(child, container)
                    txt = p.text.strip()
                    imgs = extract_and_link_images(p._p.xml, rid_map, zip_ref, img_prefix)
                    atoms = split_and_atomize(txt)
                    
                    if not atoms and imgs:
                        blocks.append({'kind': 'p', 'text': '', 'imgs': imgs})
                    elif atoms:
                        # QUANTUM ALLOCATION: Local distribution for labels
                        label_indices = [idx for idx, a in enumerate(atoms) if is_choice_label(a)]
                        local_imgs = list(imgs)
                        for i, a in enumerate(atoms):
                            if is_choice_label(a):
                                blocks.append({'kind': 'label', 'content': a})
                                # Give ONE image per label if available
                                if local_imgs:
                                    blocks.append({'kind': 'p', 'text': '', 'imgs': [local_imgs.pop(0)]})
                            else:
                                # Normal text, take images only if it's the very first atom
                                blocks.append({'kind': 'p', 'text': a, 'imgs': [local_imgs.pop(0)] if (i==0 and local_imgs) else []})
                        # Leftover images
                        if local_imgs:
                            blocks.append({'kind': 'p', 'text': '', 'imgs': local_imgs})
                    else:
                        blocks.append({'kind': 'p', 'text': '', 'imgs': []})
                        
                elif isinstance(child, CT_Tbl):
                    tbl = Table(child, container)
                    rows = [[process_container(c) for c in r.cells] for r in tbl.rows]
                    blocks.append({'kind': 'table', 'rows': rows})
            return blocks
        raw_nodes = process_container(doc)

    def flatten(nodes):
        flat = []
        for n in nodes:
            if n['kind'] == 'table':
                if len(n['rows']) <= 4:
                    for r in n['rows']:
                        for c_nodes in r: flat.extend(flatten(c_nodes))
                else:
                    tbl_md = ["\n### Table Data\n"]
                    for r in n['rows']:
                        cells = []
                        for c_nodes in r:
                            c_txt = [" ".join([fn['content'] if fn['kind']=='label' else (fn['text'] + " " + " ".join(fn['imgs'])) 
                                             for fn in flatten(c_nodes)])]
                            cells.append(c_txt[0].replace("\n", " ").replace("|", "\\|"))
                        tbl_md.append(f"| {' | '.join(cells)} |")
                    flat.append({'kind': 'p', 'text': "\n".join(tbl_md), 'imgs': []})
            else: flat.append(n)
        return flat

    atomic_blocks = flatten(raw_nodes)

    final_md = []
    label_queue = []
    
    for b in atomic_blocks:
        if b['kind'] == 'label':
            label_queue.append(len(final_md))
            final_md.append(b['content'])
        else:
            t = b['text'].strip()
            imgs = b['imgs']
            
            if re.match(r'^Câu\s*\d+', t):
                label_queue = []
                final_md.append(t if not imgs else t + "\n\n" + "\n".join(imgs))
                continue

            if label_queue and imgs:
                current_imgs = list(imgs)
                while label_queue and current_imgs:
                    idx = label_queue.pop(0)
                    img = current_imgs.pop(0)
                    if t: 
                        final_md[idx] += " " + t
                        t = "" 
                    final_md[idx] += "\n\n" + img
                if current_imgs:
                    final_md.append("\n\n".join(current_imgs))
            elif label_queue and t and len(t) < 50 and not is_choice_label(t):
                idx = label_queue.pop(0)
                final_md[idx] += " " + t
            else:
                out = []
                if t: out.append(t)
                if imgs: out.extend(imgs)
                if out: 
                    final_md.append("\n\n".join(out))
                    if len(t) > 200: label_queue = []

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"---\ntitle: {base_name}\nsource: [[{base_name}]]\ntype: RAW_SOURCE\n---\n\n")
        f.write("\n\n".join(final_md))

def main():
    docx_files = glob.glob(os.path.join(SOURCE_DOCX_DIR, "LMS_RAW_*.docx"))
    print(f"Executing Engine v14 (Quantum Distribution) on {len(docx_files)} files...")
    for f in docx_files:
        try: convert_to_md(f)
        except Exception as e: print(f"Failed {os.path.basename(f)}: {e}")

if __name__ == "__main__": main()
