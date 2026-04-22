import os
import sys
import logging
from pathlib import Path

# --- START SANITY CHECK ---
sys.stderr.write(f"[DEBUG] Starting Gemini Sync MCP: {sys.executable}\n")
sys.stderr.write(f"[DEBUG] Working Directory: {os.getcwd()}\n")
# --- END SANITY CHECK ---

# Thêm Root và libs/mcp vào PYTHONPATH để tránh import cache sai đường dẫn
_ROOT = Path(__file__).resolve().parent.parent.parent  # Thư mục gốc Project
_MCP_DIR = Path(__file__).resolve().parent            # Thư mục chứa MCP logic
sys.path.insert(0, str(_ROOT))
sys.path.insert(1, str(_MCP_DIR))

from mcp.server.fastmcp import FastMCP

# CHỐT CHẶN: Ép tất cả đầu ra (print, logging) sang stderr
logging.basicConfig(level=logging.ERROR, stream=sys.stderr)
logging.getLogger().setLevel(logging.CRITICAL)

# MONKEY-PATCH: Vô hiệu hóa việc thêm handler in ra stdout
def mcp_no_op_handler(self, hdlr):
    # Chỉ cho phép handler in ra stderr hoặc file, 
    # nhưng ở đây ta cấm luôn để an toàn tuyệt đối cho stdio
    pass
logging.Logger.addHandler = mcp_no_op_handler

# Chặn print mặc định sang stderr
import builtins
def mcp_stderr_print(*args, **kwargs):
    kwargs["file"] = sys.stderr
    orig_print = getattr(builtins, 'original_print', print)
    orig_print(*args, **kwargs)

if not hasattr(builtins, "original_print"):
    builtins.original_print = builtins.print
builtins.print = mcp_stderr_print

# Ép Console của rich sang stderr
try:
    from rich.console import Console
    import libs.core.logger
    libs.core.logger.console = Console(stderr=True) 
except:
    pass

# PYTHONPATH đã được thiết lập ở trên

# Import logic (sync_manager đã chuyển sang libs/core/, context_distiller nằm ở tools/pipeline/)
from libs.core.sync_manager import SyncManager
from tools.pipeline_context_distiller import ContextDistiller

# Khởi tạo FastMCP Server
mcp = FastMCP("Gemini Sync")

ROOT_DIR = str(Path(__file__).resolve().parent.parent.parent)

@mcp.tool()
def sync_gemini():
    """
    Thực hiện đồng bộ dữ liệu từ Gemini (input/gemini_sync/) và tóm tắt chúng bằng AI.
    """
    try:
        # Chạy logic đồng bộ với absolute path
        manager = SyncManager(project_root=ROOT_DIR)
        manager.run()
        
        # Chạy logic chưng cất (Summarization)
        distiller = ContextDistiller(project_root=ROOT_DIR)
        distiller.distill()
        
        return "✅ Đồng bộ và chưng cất dữ liệu thành công! Bản tóm tắt đã sẵn sàng."
    except Exception as e:
        return f"❌ Lỗi: {str(e)}"

@mcp.resource("gemini://latest-context")
def get_latest_context() -> str:
    """Trả về nội dung ngữ cảnh đã được tinh lọc mới nhất."""
    path = Path(ROOT_DIR) / "storage" / "optimized_context.md"
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return "⚠️ Chưa có ngữ cảnh nào được tối ưu hóa. Hãy bảo bot chạy tool 'sync_gemini' trước."

if __name__ == "__main__":
    mcp.run()
