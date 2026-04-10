import os
import sys
import re
from pathlib import Path
from typing import List, Dict

# Add project root to sys.path to import libs
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from libs.core.llm_client import call_worker
from libs.core.logger import get_logger

logger = get_logger("brain_lint")

BRAIN_DISTILLED_DIR = project_root / "brain" / "distilled"

def get_wiki_files() -> List[Path]:
    """Lấy danh sách các tệp markdown trong thư mục distilled."""
    return list(BRAIN_DISTILLED_DIR.glob("*.md"))

def read_file_content(path: Path) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def check_broken_links(content: str, all_filenames: List[str]) -> List[str]:
    """Kiểm tra các [[wikilinks]] không tồn tại."""
    links = re.findall(r"\[\[(.*?)\]\]", content)
    broken = []
    for link in links:
        # Giả định link là tên file không có phần mở rộng
        if link not in all_filenames and f"{link}.md" not in all_filenames:
            broken.append(link)
    return broken

def lint_file_content(filename: str, content: str) -> str:
    """Sử dụng LLM để tìm lỗi phản logic hoặc mâu thuẫn trong nội dung."""
    prompt = f"""
Bạn là một chuyên gia quản lý tri thức (Knowledge Librarian).
Hãy kiểm tra tệp tin Wiki sau đây để tìm:
1. Mâu thuẫn logic (Contradictions).
2. Thông tin lặp lại không cần thiết.
3. Các lỗ hổng kiến thức (Knowledge Gaps) quan trọng.

Tên tệp: {filename}
Nội dung:
---
{content}
---

Hãy trả về báo cáo ngắn gọn bằng tiếng Việt. Nếu không có lỗi, hãy ghi "OK".
"""
    messages = [{"role": "user", "content": prompt}]
    try:
        response = call_worker(messages, model="fast-engine")
        return response
    except Exception as e:
        return f"Lỗi gọi LLM: {e}"

def main():
    logger.info("START: Brain Linting...")
    files = get_wiki_files()
    all_filenames = [f.name for f in files]
    
    report = []
    report.append(f"# Brain Lint Report - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    for file_path in files:
        if file_path.name.startswith("_"): continue # Bỏ qua index
        
        logger.info(f"LINTING: {file_path.name}")
        content = read_file_content(file_path)
        
        # 1. Kiểm tra link hỏng
        broken = check_broken_links(content, all_filenames)
        
        # 2. Kiểm tra nội dung qua LLM
        lint_result = lint_file_content(file_path.name, content[:3000]) # Giới hạn 3000 ký tự để tiết kiệm token
        
        report.append(f"## 📄 {file_path.name}")
        if broken:
            report.append(f"- **Broken Links:** {', '.join(broken)}")
        else:
            report.append("- **Broken Links:** None")
            
        report.append(f"- **AI Analysis:**\n{lint_result}\n")
        report.append("---")
        
        # Thêm sleep để tránh Rate Limit (429)
        time.sleep(5)

    report_path = project_root / "brain" / "lint_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report))
        
    logger.info(f"DONE! Report saved at: {report_path}")

if __name__ == "__main__":
    import time
    main()
