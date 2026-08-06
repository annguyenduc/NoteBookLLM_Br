"""
Script kiểm tra sức khỏe (Health Check) chính thức cho 9Router (Port 20128).
Dùng để xác minh kết nối trước khi chạy Pedagogical Swarm Pipeline.
"""
import sys
import time
from pathlib import Path

# Thêm root vào path để import libs
root = Path(__file__).resolve().parent.parent
sys.path.append(str(root))

# Cấu hình encoding cho terminal Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

try:
    from libs.core.llm_client import call_worker, logger
    from libs.core.logger import get_logger
except ImportError:
    print("❌ LỖI: Không thể tìm thấy libs.core. Hãy chạy script từ thư mục gốc của dự án.")
    sys.exit(1)

def ping_9router():
    print("--- 🔍 Đang kiểm tra 9Router Neural Orchestrator (Port 20128) ---")
    start_time = time.time()
    
    try:
        # Sử dụng call_worker - hàm wrapper chuẩn của dự án
        messages = [{"role": "user", "content": "Ping. Respond with 'PONG' and your model ID."}]
        
        # Gọi qua llm_client (đã được cấu hình trỏ vào 20128)
        response = call_worker(messages, model="ag/gemini-3-flash")
        
        elapsed = time.time() - start_time
        print(f"\n✅ KẾT QUẢ: Thành công ({elapsed:.2f}s)")
        print(f"🤖 PHẢN HỒI: {response}")
        print("\n✨ TRẠNG THÁI: Hạ tầng 9Router đã sẵn sàng phục vụ Swarm Agent.")
        return True
        
    except Exception as e:
        print(f"\n❌ LỖI KẾT NỐI: Không thể thiết lập liên lạc với 9Router.")
        print(f"Chi tiết: {e}")
        print("\n⚠️ CẢNH BÁO: Vui lòng chạy workflow '/start-gateway' để kích hoạt 9Router trước.")
        return False

if __name__ == "__main__":
    success = ping_9router()
    sys.exit(0 if success else 1)
