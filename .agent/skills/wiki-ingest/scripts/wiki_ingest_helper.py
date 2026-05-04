import datetime
import io
import os
import re
import shutil
import subprocess
import sys
import hashlib
import sqlite3
import json

# Force UTF-8 stdout/stderr
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Path Configuration
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
WIKI_DIR = os.path.join(REPO_ROOT, "3-resources", "wiki")
DB_PATH = os.path.join(WIKI_DIR, "wiki_brain.db")
RAW_SOURCES_DIR = os.path.join(REPO_ROOT, "3-resources", "raw", "sources")

def get_magika_route(file_path):
    """Sử dụng Magika để định tuyến parser dựa trên nội dung thực tế hoặc URL."""
    if file_path.startswith(('http://', 'https://')):
        return "web_scrape"
        
    try:
        from magika import Magika
        m = Magika()
        result = m.identify_path(file_path)
        label = result.output.ct_label
        score = result.score
        print(f"[*] Magika ID: {label} (Confidence: {score:.2f})")
        
        if label == 'pdf':
            return "docling"
        elif label in ['docx', 'pptx', 'xlsx']:
            return "markitdown"
        elif label in ['markdown', 'text', 'code']:
            return "native"
        else:
            return "unknown"
    except Exception:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.pdf': return "docling"
        if ext in ['.docx', '.pptx', '.xlsx']: return "markitdown"
        return "native"

def convert_file(input_path):
    route = get_magika_route(input_path)
    print(f"[*] Routing to: {route}")
    
    if route == "web_scrape":
        output_name = f"WEBSITE_{hashlib.md5(input_path.encode()).hexdigest()[:8]}.md"
        output_path = os.path.join(REPO_ROOT, "00_Inbox", output_name)
        print(f"[*] Đang cào URL: {input_path} -> {output_path}")
        scrape_script = os.path.join(REPO_ROOT, ".agent", "skills", "wiki-web-scrape", "scripts", "lightpanda_scrape.py")
        subprocess.run([sys.executable, scrape_script, "--url", input_path, "--output", output_path], check=True)
        return output_path

    elif route == "docling":
        output_path = input_path + ".md"
        print(f"[*] Đang dùng Docling xử lý PDF: {input_path}...")
        try:
            from docling.document_converter import DocumentConverter
            converter = DocumentConverter()
            result = converter.convert(input_path)
            md_output = result.document.export_to_markdown()
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(md_output)
            return output_path
        except Exception as e:
            print(f"[!] Lỗi Docling: {e}")
            return None

    elif route == "markitdown":
        output_path = input_path + ".md"
        print(f"[*] Đang dùng MarkItDown xử lý Office: {input_path}...")
        try:
            from markitdown import MarkItDown
            md = MarkItDown()
            result = md.convert(input_path)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result.text_content)
            return output_path
        except Exception as e:
            print(f"[!] Lỗi MarkItDown: {e}")
            return None
    else:
        print(f"[*] File {input_path} đã sẵn sàng. Không cần convert.")
        return input_path

def verify_rgr(query, expected_atom):
    """Giai đoạn REFACTOR: Kiểm tra xem tri thức mới đã được tìm thấy chưa."""
    print(f"[*] Giai đoạn REFACTOR: Đang xác minh tri thức với query: '{query}'")
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # Tìm kiếm trong FTS5
        cursor.execute("SELECT path, snippet(nodes_fts, 2, '<b>', '</b>', '...', 10) FROM nodes_fts WHERE content MATCH ? LIMIT 1", (query,))
        result = cursor.fetchone()
        conn.close()

        if result:
            found_path, snippet = result
            print(f"[+] THÀNH CÔNG: Tìm thấy tri thức tại {found_path}")
            print(f"    Snippet: {snippet}")
            if expected_atom in found_path:
                print("✅ REFACTOR PASSED: Tri thức đã được đồng bộ chính xác.")
                return True
        print("❌ REFACTOR FAILED: Không tìm thấy tri thức hoặc kết quả không khớp.")
        return False
    except Exception as e:
        print(f"[!] Lỗi verify: {e}")
        return False

def check_contradictions(content):
    """Kiểm tra mâu thuẫn tri thức sơ khởi (Semantic check via Smart Spine)."""
    # Placeholder cho logic so sánh ngữ nghĩa nâng cao
    # Hiện tại: Check trùng lặp tiêu đề/metadata quan trọng
    pass

if __name__ == "__main__":
    if "--route" in sys.argv:
        print(get_magika_route(sys.argv[2]))
    elif "--url" in sys.argv:
        convert_file(sys.argv[2])
    elif "--verify" in sys.argv:
        verify_rgr(sys.argv[2], sys.argv[3])
    elif len(sys.argv) > 1:
        convert_file(sys.argv[1])

