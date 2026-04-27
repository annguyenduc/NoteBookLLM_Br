import os
import re
import sys
from pathlib import Path

# Cấu hình đường dẫn
PROJECT_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = PROJECT_ROOT / "brain" / "wiki"
DISTILLED_DIR = PROJECT_ROOT / "brain" / "distilled"

# Ép hệ thống sử dụng UTF-8 cho stdout/stderr
for stream in [sys.stdout, sys.stderr]:
    if hasattr(stream, 'reconfigure'):
        try:
            stream.reconfigure(encoding='utf-8')
        except Exception:
            pass


def is_base64_line(line: str) -> bool:
    """Phát hiện dòng base64 (ảnh nhúng) để loại khỏi search."""
    stripped = line.strip()
    # Base64 lines: rất dài, không có khoảng trắng, chỉ gồm ký tự base64
    if len(stripped) > 200 and ' ' not in stripped:
        b64_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=')
        ratio = sum(1 for c in stripped if c in b64_chars) / len(stripped)
        return ratio > 0.95
    return False


def score_file(filepath: Path, keywords: list[str]) -> tuple[int, list[str]]:
    """
    Tính điểm relevance của file dựa trên số lần xuất hiện keywords.
    Concept pages (WIKI_/KB_) được boost x3 để ưu tiên hiển thị.
    Trả về (score, danh sách snippet).
    """
    try:
        raw_content = filepath.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return 0, []

    # Lọc bỏ dòng base64 trước khi search
    clean_lines = [line for line in raw_content.splitlines() if not is_base64_line(line)]
    content = '\n'.join(clean_lines)
    content_lower = content.lower()

    score = 0
    snippets = []

    for kw in keywords:
        kw_lower = kw.lower()
        count = content_lower.count(kw_lower)
        if count == 0:
            continue
        score += count

        # Lấy snippet đầu tiên xung quanh keyword
        idx = content_lower.find(kw_lower)
        start = max(0, idx - 60)
        end = min(len(content), idx + len(kw_lower) + 60)
        snippet = content[start:end].replace('\n', ' ').replace('\r', ' ').strip()
        snippets.append(f"...{snippet}...")

    # Boost x3 cho Concept pages (WIKI_*.md, KB_*.md)
    name = filepath.name
    if name.startswith('WIKI_') or name.startswith('KB_'):
        score *= 3

    return score, snippets[:2]


def search_knowledge(query: str, top_k: int = 10):
    """
    Tìm kiếm tri thức theo keywords trong 3-resources/wiki/ và 3-resources/distilled/.
    Xếp hạng theo tổng số lần xuất hiện (BM25-lite).
    """
    keywords = query.strip().split()
    if not keywords:
        print("❌ Vui lòng nhập từ khóa tìm kiếm.")
        return

    print(f"[SEARCH] Đang tìm kiếm: '{query}' ({len(keywords)} từ khóa)...\n")

    # Thu thập tất cả file từ wiki/ và distilled/
    all_files: list[Path] = []
    for search_dir in [WIKI_DIR, DISTILLED_DIR]:
        if search_dir.exists():
            all_files.extend(search_dir.glob("*.md"))

    if not all_files:
        print(f"❌ Không tìm thấy file nào trong 3-resources/wiki/ hoặc 3-resources/distilled/")
        return

    # Tính điểm từng file
    results = []
    for fpath in all_files:
        score, snippets = score_file(fpath, keywords)
        if score > 0:
            results.append({
                "file": fpath.name,
                "path": str(fpath.relative_to(PROJECT_ROOT)),
                "score": score,
                "snippets": snippets
            })

    if not results:
        print("⚠️ Không tìm thấy kết quả nào khớp với từ khóa.")
        return

    # Sắp xếp theo điểm giảm dần
    results.sort(key=lambda x: x["score"], reverse=True)
    top_results = results[:top_k]

    print(f"✅ Tìm thấy {len(results)} kết quả — hiển thị top {len(top_results)}:\n")
    print("-" * 60)

    for i, res in enumerate(top_results, 1):
        print(f"#{i} 📄 {res['file']}  (score: {res['score']})")
        print(f"   📂 {res['path']}")
        for snippet in res["snippets"]:
            print(f"   💡 {snippet}")
        print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("HD: python tools/qmd_search.py \"từ khóa tìm kiếm\"")
        print("VD: python tools/qmd_search.py \"cảm biến siêu âm\"")
    else:
        search_knowledge(sys.argv[1])
