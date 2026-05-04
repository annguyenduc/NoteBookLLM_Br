import os
import sqlite3
from datetime import datetime

ROOT_DIR = r"d:\NoteBookLLM_Br"
WIKI_DIR = os.path.join(ROOT_DIR, "3-resources", "wiki")
DB_PATH  = os.path.join(WIKI_DIR, "wiki_brain.db")
INDEX_PATH = os.path.join(WIKI_DIR, "index.md")

def get_atoms_by_type():
    """Lấy danh sách Atoms phân loại theo Type từ Database."""
    categories = {} # {type: [atoms]}
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

def generate_index_content(categories):
    """Tạo nội dung cho file index.md."""
    lines = [
        "# Wiki Index",
        f"Cập nhật lần cuối: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "\n## Thống kê nhanh",
        f"- Tổng số Atoms: {sum(len(v) for v in categories.values())}",
        "\n---\n"
    ]
    
    # Order of display
    order = ["Concept", "Entity", "Source", "Synthesis", "Decision"]
    
    for cat in order:
        if cat in categories:
            lines.append(f"\n### {cat}s")
            for atom in categories[cat]:
                status_icon = "✅" if atom["status"] in ["VERIFIED", "SYNTHESIZED"] else "📝"
                lines.append(f"- {status_icon} [[{atom['id']}|{atom['title']}]]")
        elif cat.lower() + "s" in categories: # Handle plural/lowercase variants
             pass 

    # Handle remaining types
    for cat, atoms in categories.items():
        if cat not in order:
            lines.append(f"\n### {cat}")
            for atom in atoms:
                lines.append(f"- [[{atom['id']}|{atom['title']}]]")
                
    return "\n".join(lines)

def write_index():
    """Ghi nội dung vào file index.md."""
    print("Generating Index...")
    categories = get_atoms_by_type()
    content = generate_index_content(categories)
    
    try:
        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully updated {INDEX_PATH}")
    except Exception as e:
        print(f"Error writing index: {e}")

if __name__ == "__main__":
    write_index()
