import os
import glob

BASE_DIR = r"d:\NoteBookLLM_Br"
RAW_DIR = os.path.join(BASE_DIR, "brain", "raw")
INDEX_PATH = os.path.join(RAW_DIR, "MASTER_SOURCE_INDEX.md")

def update_index():
    md_files = glob.glob(os.path.join(RAW_DIR, "LMS_RAW_*.md"))
    # Also include the rare .txt or other raw files if any
    other_files = glob.glob(os.path.join(RAW_DIR, "*"))
    other_files = [f for f in other_files if not f.endswith(".md") and os.path.isfile(f)]
    
    all_files = sorted(md_files + other_files)
    
    # Categorization masks
    categories = {
        "📡 IoT & Tự động hóa": ["Arduino", "IOT", "Halocode", "Yolobit"],
        "🤖 Trí tuệ nhân tạo (AI)": ["AI", "Khoa học máy tính AI"],
        "🚗 Robotics": ["Robotics", "mBot", "Codey", "Rover", "GBot", "xBot", "Unplugged"],
        "💻 Lập trình": ["Python", "Scratch", "Tynker"],
        "🎨 Multimedia & 3D": ["3D", "Tinkercad", "Canva", "Maker Empire", "Wordpress", "Media"],
        "🧪 Đóng gói & Khác": [] # Fallback
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
        if not found_cat:
            categorized["🧪 Đóng gói & Khác"].append(f_name)

    # Build MD
    md = []
    md.append("# 📚 MASTER SOURCE INDEX (LOM v4.4 - Swarm Supreme)")
    md.append(f"\nĐây là danh mục quản lý nguồn tin cậy đã được làm phẳng (Absolute Flatness). Tổng số file: {len(all_files)}\n")
    
    tag_counters = {"IOT": 1, "AI": 1, "ROB": 1, "CODE": 1, "MEDIA": 1, "SYS": 1}
    cat_to_tag = {
        "📡 IoT & Tự động hóa": "IOT",
        "🤖 Trí tuệ nhân tạo (AI)": "AI",
        "🚗 Robotics": "ROB",
        "💻 Lập trình": "CODE",
        "🎨 Multimedia & 3D": "MEDIA",
        "🧪 Đóng gói & Khác": "SYS"
    }
    
    for cat, files in categorized.items():
        if not files: continue
        md.append(f"## {cat}\n")
        md.append("| Tag | File Path | Tên File |")
        md.append("| :--- | :--- | :--- |")
        tag_prefix = cat_to_tag.get(cat, "SYS")
        
        for f_name in files:
            tag = f"**[{tag_prefix}_{tag_counters[tag_prefix]:03d}]**"
            tag_counters[tag_prefix] += 1
            md.append(f"| {tag} | [`{f_name}`](./{f_name}) | {f_name} |")
        md.append("")

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    
    print(f"Index updated: {len(all_files)} files indexed.")

if __name__ == "__main__":
    update_index()
