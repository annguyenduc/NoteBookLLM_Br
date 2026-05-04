import os
import sqlite3
import glob
from datetime import datetime

ROOT_DIR = r"d:\NoteBookLLM_Br"
WIKI_DIR = os.path.join(ROOT_DIR, "3-resources", "wiki")
RAW_DIR = os.path.join(ROOT_DIR, "3-resources", "raw")
DB_PATH  = os.path.join(WIKI_DIR, "wiki_brain.db")
WIKI_INDEX_PATH = os.path.join(WIKI_DIR, "index.md")
RAW_INDEX_PATH = os.path.join(RAW_DIR, "MASTER_SOURCE_INDEX.md")

def get_atoms_by_type():
    """Lấy danh sách Atoms phân loại theo Type từ Database."""
    categories = {}
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        rows = cursor.execute("SELECT file_id, title, type, status FROM atoms ORDER BY title ASC").fetchall()
        for file_id, title, atom_type, status in rows:
            if atom_type not in categories:
                categories[atom_type] = []
            categories[atom_type].append({"id": file_id, "title": title, "status": status})
        conn.close()
    except Exception as e:
        print(f"Error reading DB: {e}")
    return categories

def update_wiki_index():
    """Cập nhật file 3-resources/wiki/index.md."""
    print("Updating Wiki Index...")
    categories = get_atoms_by_type()
    lines = [
        "# Wiki Index",
        f"Cập nhật lần cuối: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "\n## Thống kê nhanh",
        f"- Tổng số Atoms: {sum(len(v) for v in categories.values())}",
        "\n---\n"
    ]
    
    order = ["Concept", "Entity", "Source", "Synthesis", "Decision"]
    for cat in order:
        if cat in categories:
            lines.append(f"\n### {cat}s")
            for atom in categories[cat]:
                status_icon = "✅" if atom["status"] in ["VERIFIED", "SYNTHESIZED"] else "📝"
                lines.append(f"- {status_icon} [[{atom['id']}|{atom['title']}]]")
    
    for cat, atoms in categories.items():
        if cat not in order:
            lines.append(f"\n### {cat}")
            for atom in atoms:
                lines.append(f"- [[{atom['id']}|{atom['title']}]]")
                
    with open(WIKI_INDEX_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Successfully updated {WIKI_INDEX_PATH}")

def update_raw_index():
    """Cập nhật file 3-resources/raw/MASTER_SOURCE_INDEX.md (Logic từ update_master_index.py)."""
    print("Updating Master Source Index (Raw)...")
    md_files = [f for f in glob.glob(os.path.join(RAW_DIR, "*.md")) if "MASTER_SOURCE_INDEX.md" not in f]
    other_files = [f for f in glob.glob(os.path.join(RAW_DIR, "*")) if not f.endswith(".md") and os.path.isfile(f)]
    all_files = sorted(md_files + other_files)
    
    categories = {
        "📡 IoT & Tự động hóa": ["Arduino", "IOT", "Halocode", "Yolobit"],
        "🤖 Trí tuệ nhân tạo (AI)": ["AI", "Khoa học máy tính AI"],
        "🚗 Robotics": ["Robotics", "mBot", "Codey", "Rover", "GBot", "xBot", "Unplugged"],
        "💻 Lập trình": ["Python", "Scratch", "Tynker"],
        "🎨 Multimedia & 3D": ["3D", "Tinkercad", "Canva", "Maker Empire", "Wordpress", "Media"],
        "🧪 Đóng gói & Khác": []
    }
    
    categorized = {cat: [] for cat in categories}
    for f_path in all_files:
        f_name = os.path.basename(f_path)
        found_cat = False
        for cat, keywords in categories.items():
            if any(kw.lower() in f_name.lower() for kw in keywords):
                categorized[cat].append(f_name)
                found_cat = True
                break
        if not found_cat: categorized["🧪 Đóng gói & Khác"].append(f_name)

    md = ["# 📚 MASTER SOURCE INDEX", f"\nTổng số file: {len(all_files)}\n"]
    tag_counters = {"IOT": 1, "AI": 1, "ROB": 1, "CODE": 1, "MEDIA": 1, "SYS": 1}
    cat_to_tag = {"📡 IoT & Tự động hóa": "IOT", "🤖 Trí tuệ nhân tạo (AI)": "AI", "🚗 Robotics": "ROB", "💻 Lập trình": "CODE", "🎨 Multimedia & 3D": "MEDIA", "🧪 Đóng gói & Khác": "SYS"}
    
    for cat, files in categorized.items():
        if not files: continue
        md.append(f"## {cat}\n")
        md.append("| Tag | Tên File | Link |")
        md.append("| :--- | :--- | :--- |")
        tag_prefix = cat_to_tag.get(cat, "SYS")
        for f_name in files:
            tag = f"**[{tag_prefix}_{tag_counters[tag_prefix]:03d}]**"
            tag_counters[tag_prefix] += 1
            md.append(f"| {tag} | {f_name} | [`Link`](./{f_name}) |")
        md.append("")

    with open(RAW_INDEX_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"Successfully updated {RAW_INDEX_PATH}")

if __name__ == "__main__":
    update_wiki_index()
    update_raw_index()
