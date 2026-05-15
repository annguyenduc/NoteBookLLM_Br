# -*- coding: utf-8 -*-
"""
maint_unify_archives.py — Unified Archive Orchestrator
======================================================
Gom tất cả các thư mục rác, lưu trữ phân mảnh về 4-archive/ theo chuẩn PARA.

Thư mục nguồn (Source) -> Thư mục đích (Destination):
- 00_Inbox/_deprecated/        -> 4-archive/inbox/
- 00_Inbox/Rejected/           -> 4-archive/rejected/
- 00_Inbox/_legacy_rollback_*  -> 4-archive/rollbacks/
- 00_Inbox/trash_archive/      -> 4-archive/inbox/
- 3-resources/_deprecated/     -> 4-archive/resources/
"""

import os
import shutil
import pathlib
import sys

ROOT_DIR = pathlib.Path("d:/NoteBookLLM_Br")
ARCHIVE_ROOT = ROOT_DIR / "4-archive"

MAPPING = [
    (ROOT_DIR / "00_Inbox" / "_deprecated", ARCHIVE_ROOT / "inbox"),
    (ROOT_DIR / "00_Inbox" / "Rejected", ARCHIVE_ROOT / "rejected"),
    (ROOT_DIR / "00_Inbox" / "trash_archive", ARCHIVE_ROOT / "inbox"),
    (ROOT_DIR / "3-resources" / "_deprecated", ARCHIVE_ROOT / "resources"),
    (ROOT_DIR / "3-resources" / "wiki" / "_deprecated", ARCHIVE_ROOT / "resources"),
]

def unify_archives():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("🚀 Bắt đầu quy hoạch lại Archive hệ thống...")
    
    # 1. Xử lý các mapping cố định
    for src, dst in MAPPING:
        if src.exists():
            print(f"[*] Tìm thấy: {src.relative_to(ROOT_DIR)}")
            dst.mkdir(parents=True, exist_ok=True)
            
            # Di chuyển từng item bên trong để tránh lỗi permission nếu folder đích đã tồn tại
            for item in src.iterdir():
                target = dst / item.name
                if target.exists():
                    # Nếu trùng tên, thêm timestamp
                    from datetime import datetime
                    ts = datetime.now().strftime("%H%M%S")
                    target = dst / f"{item.stem}_{ts}{item.suffix}"
                
                print(f"  -> {target.relative_to(ROOT_DIR)}")
                shutil.move(str(item), str(target))
            
            # Xóa thư mục gốc nếu trống
            try:
                src.rmdir()
                print(f"  [OK] Đã xóa thư mục trống: {src.name}")
            except Exception:
                pass

    # 2. Xử lý các pattern động (Rollbacks)
    inbox_dir = ROOT_DIR / "00_Inbox"
    if inbox_dir.exists():
        for folder in inbox_dir.glob("_legacy_rollback_*"):
            if folder.is_dir():
                print(f"[*] Phát hiện Rollback: {folder.name}")
                dst = ARCHIVE_ROOT / "rollbacks" / folder.name
                dst.parent.mkdir(parents=True, exist_ok=True)
                
                if not dst.exists():
                    shutil.move(str(folder), str(dst))
                    print(f"  -> {dst.relative_to(ROOT_DIR)}")
                else:
                    print(f"  [SKIP] {dst.name} đã tồn tại trong archive.")

    print("\n✅ Hoàn tất quy hoạch Archive. Hệ thống hiện đã nhất quán.")

if __name__ == "__main__":
    unify_archives()
