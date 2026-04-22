import os
import sys
import re
from pathlib import Path

# Cấu hình đường dẫn v3.6
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DISTILLED_DIR = PROJECT_ROOT / "brain/distilled"

# Ép hệ thống sử dụng UTF-8 cho stdout/stderr một cách an toàn
for stream in [sys.stdout, sys.stderr]:
    if hasattr(stream, 'reconfigure'):
        try:
            stream.reconfigure(encoding='utf-8')
        except Exception:
            pass

def search_knowledge(query):
    print(f"[SEARCH] Đang tìm kiếm tri thức v3.6 cho: '{query}'...")
    results = []
    
    if not DISTILLED_DIR.exists():
        print(f"❌ Lỗi: Thư mục tri thức không tồn tại tại {DISTILLED_DIR}")
        return

    # Duyệt qua các file .md trong distilled
    for fpath in DISTILLED_DIR.glob("LMS_KB_*.md"):
        with open(fpath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if query.lower() in line.lower():
                    # Trích xuất nguồn (hỗ trợ cả [Nguồn: X] và [X])
                    source_match = re.search(r"\[(Nguồn:\s*)?([^\]]+)\]", line)
                    source_text = source_match.group(2) if source_match else "N/A"
                    
                    results.append({
                        "file": fpath.name,
                        "line": i + 1,
                        "content": line.strip(),
                        "source": source_text
                    })

    if not results:
        print("⚠️ Không tìm thấy kết quả nào khớp với từ khóa.")
        return

    print(f"✅ Tìm thấy {len(results)} kết quả:\n")
    for res in results:
        print(f"📄 File: {res['file']} (Dòng {res['line']})")
        print(f"   💡 Nội dung: {res['content']}")
        print(f"   ⚓ Nguồn dẫn: {res['source']}")
        print("-" * 50)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Vui lòng nhập từ khóa tìm kiếm. HD: python tools/qmd_search.py \"từ khóa\"")
    else:
        search_query = sys.argv[1]
        search_knowledge(search_query)
