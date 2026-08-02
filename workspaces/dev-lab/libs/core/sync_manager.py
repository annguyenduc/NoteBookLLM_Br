import os
import sys
import shutil
from pathlib import Path
from datetime import datetime

# Ép hệ thống sử dụng UTF-8 cho stdout/stderr một cách an toàn
for stream in [sys.stdout, sys.stderr]:
    if hasattr(stream, 'reconfigure'):
        try:
            stream.reconfigure(encoding='utf-8')
        except Exception:
            pass

class SyncManager:
    """
    Quản lý việc đồng bộ và chuẩn bị dữ liệu ngữ cảnh thô từ Gemini.
    """
    def __init__(self, project_root=None):
        # Nếu không truyền project_root, tự động tìm root dựa trên vị trí file này (libs/core/sync_manager.py)
        if project_root is None:
            self.root = Path(__file__).resolve().parent.parent.parent
        else:
            self.root = Path(project_root)
            
        self.sync_dir = self.root / "input/gemini_sync"
        self.processed_dir = self.root / "storage/processed"
        self.raw_output = self.root / "storage/raw_context.md"
        
        # Đảm bảo thư mục tồn tại
        self.sync_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)

    def run(self, exclude_patterns=None):
        files = sorted(list(self.sync_dir.glob("*.md")))
        if not files:
            print("🚀 Không tìm thấy file mới trong input/gemini_sync.")
            return

        print(f"📦 Đang xử lý {len(files)} file đồng bộ...")
        
        all_content = []
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        all_content.append(f"# Gemini Raw Context - {timestamp}\n")

        if exclude_patterns is None:
            exclude_patterns = []
        
        for fpath in files:
            if any(pattern in fpath.name for pattern in exclude_patterns):
                continue
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
                all_content.append(f"## --- SOURCE: {fpath.name} ---\n")
                all_content.append(content)
                all_content.append("\n\n")
            
            # Di chuyển vào folder backup sau khi xử lý thành công
            dest = self.processed_dir / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{fpath.name}"
            shutil.move(str(fpath), str(dest))

        # Ghi file tổng hợp
        with open(self.raw_output, "w", encoding="utf-8") as out:
            out.write("\n".join(all_content))

        print(f"✅ Đã tổng hợp dữ liệu tại: {self.raw_output}")
        print(f"📁 Các file gốc đã được di chuyển vào: {self.processed_dir}")

if __name__ == "__main__":
    manager = SyncManager()
    manager.run()
