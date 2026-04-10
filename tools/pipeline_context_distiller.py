import os
import sys
from pathlib import Path

# Thêm Root (d:\Burn_Token) vào PYTHONPATH
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from libs.core.llm_client import call_worker
from libs.core.logger import get_logger

logger = get_logger("distiller")

# Ép hệ thống sử dụng UTF-8 cho stdout/stderr một cách an toàn
for stream in [sys.stdout, sys.stderr]:
    if hasattr(stream, 'reconfigure'):
        try:
            stream.reconfigure(encoding='utf-8')
        except Exception:
            pass

class ContextDistiller:
    """
    Sử dụng AI để chưng cất (summarize) dữ liệu thô từ Gemini thành ngữ cảnh tinh gọn.
    """
    def __init__(self, project_root=None):
        # Nếu không truyền project_root, tự động tìm root dựa trên vị trí file này (tools/pipeline_context_distiller.py)
        if project_root is None:
            self.root = Path(__file__).resolve().parent.parent
        else:
            self.root = Path(project_root)
            
        self.input_file = self.root / "brain/raw/raw_context.md"
        self.output_file = self.root / "brain/optimized_context.md"

    def distill(self):
        if not self.input_file.exists():
            # Fallback check for any raw logs in brain/raw
            raw_logs = list((self.root / "brain/raw").glob("*.md"))
            if not raw_logs:
                logger.error(f"❌ Không tìm thấy file dữ liệu thô tại: {self.input_file}")
                return
            self.input_file = raw_logs[0] # Lấy file đầu tiên nếu không có file đích danh

        with open(self.input_file, "r", encoding="utf-8") as f:
            raw_content = f.read()

        if len(raw_content.strip()) < 50:
            logger.warning("⚠️ Dữ liệu thô quá ngắn, bỏ qua việc chưng cất.")
            return

        prompt = f"""
BẠN LÀ MỘT EXPERT CONTEXT ARCHITECT & SOP WRITER.
NHIỆM VỤ: Chưng cất nội dung hội thoại thô sau đây thành một bản tóm tắt tri thức chiến lược (Kernel) CỰC KỲ TINH GỌN.

DỮ LIỆU THÔ:
---
{raw_content}
---

YÊU CẦU ĐẦU RA (Markdown):
1. **Mục tiêu & Tiến độ**: (Tóm tắt ngắn gọn trạng thái dự án).
2. **Quy trình chuẩn (SOP)**: (Trích xuất các quy trình làm việc/SOP quan trọng đã chốt).
3. **Quyết định Kỹ thuật**: (Các lựa chọn kiến trúc, logic lõi cần nhớ).
4. **Hạ tầng & Tooling**: (Trạng thái Gateway, Scripts, MCP Servers).
5. **Next Actions**: (Các bước thực hiện kế tiếp).

LƯU Ý: 
- Tập trung vào TRI THỨC CÓ THỂ TÁI SỬ DỤNG (Actionable Knowledge).
- Loại bỏ boilerplate, chào hỏi.
- Ngôn ngữ: TIẾNG VIỆT (Technical Terms giữ Tiếng Anh).
"""
        
        logger.info("🚀 Đang gửi dữ liệu thô sang Smart Proxy (main-engine) để chưng cất...")
        
        messages = [
            {"role": "system", "content": "You are a senior developer who summarizes technical context efficiently."},
            {"role": "user", "content": prompt}
        ]
        
        try:
            optimized_content = call_worker(messages, model="main-engine", temperature=0.1, max_tokens=2000)
            
            with open(self.output_file, "w", encoding="utf-8") as out:
                out.write(f"<!-- LAST UPDATED: {os.popen('date /t').read().strip()} -->\n")
                out.write(optimized_content)
            
            logger.info(f"✅ Đã tạo file ngữ cảnh tối ưu tại: {self.output_file}")
        except Exception as e:
            logger.error(f"❌ Lỗi khi chưng cất dữ liệu: {e}")

if __name__ == "__main__":
    distiller = ContextDistiller()
    distiller.distill()
