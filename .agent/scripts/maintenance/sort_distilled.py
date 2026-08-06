"""
sort_distilled.py — Tự động sort 3-resources/distilled/ vào đúng folder
Chạy từ root của repo: python scripts/sort_distilled.py

Quy tắc phân loại:
  LMS_Tests_*       → 3-resources/distilled/   (giữ nguyên - test bank thực sự)
  EXAM_Context_*    → 3-resources/process/     (handoff file)
  Trainer_Profile_* → 3-resources/process/     (handoff file)
  Learning_Design_* → 3-resources/process/     (handoff file)
  Eval_Report_*     → 3-resources/process/     (handoff file)
  agents-index*     → docs/              (config file)
  CONV_Atoms_*      → 3-resources/raw/         (raw data, chưa distill đúng)
  *_atoms_*         → 3-resources/raw/         (raw data)
  Còn lại           → 3-resources/process/     (mặc định an toàn - không xóa)
"""

import os
import shutil
from pathlib import Path

# ── CẤU HÌNH ──────────────────────────────────────────────────────────────────
REPO_ROOT = Path(".")   # Chạy từ root repo
DISTILLED  = REPO_ROOT / "3-resources" / "distilled"
RAW        = REPO_ROOT / "3-resources" / "raw"
ATOMS      = REPO_ROOT / "3-resources" / "atoms"
PROCESS    = REPO_ROOT / "3-resources" / "process"
DOCS       = REPO_ROOT / "docs"
DRY_RUN    = False      # ← ĐỔI THÀNH False KHI MUỐN CHẠY THẬT

# ── QUY TẮC PHÂN LOẠI ─────────────────────────────────────────────────────────
# (pattern_lowercase, destination_folder, lý do)
RULES = [
    ("lms_tests_",        DISTILLED,  "Test bank — giữ nguyên"),
    ("exam_context_",     PROCESS,    "Handoff: scout → engineer"),
    ("trainer_profile_",  PROCESS,    "Handoff: profiler → designer"),
    ("learning_design_",  PROCESS,    "Handoff: designer → engineer"),
    ("eval_report_",      PROCESS,    "Handoff: evaluator output"),
    ("agents-index",      DOCS,       "Config file — không phải knowledge"),
    ("conv_atoms_",       RAW,        "Raw chat data — chưa distill đúng"),
    ("_atoms_",           RAW,        "Raw atoms — chưa qua atomic template"),
    ("lms_kb_",           RAW,        "KB dump — là raw data"),
    ("master_conv_",      RAW,        "Master conv dump — là raw data"),
]
DEFAULT_DEST = PROCESS   # File không khớp rule nào → process (an toàn)

# ── THỰC THI ───────────────────────────────────────────────────────────────────
def classify(filename: str):
    name_lower = filename.lower()
    for pattern, dest, reason in RULES:
        if pattern in name_lower:
            return dest, reason
    return DEFAULT_DEST, "Không khớp rule — mặc định process"

def ensure_dirs():
    for d in [ATOMS, PROCESS, DOCS]:
        d.mkdir(parents=True, exist_ok=True)
        print(f"  [DIR] Đảm bảo tồn tại: {d}")

def run():
    print("=" * 60)
    print(f"  sort_distilled.py — {'DRY RUN (xem trước)' if DRY_RUN else '🚨 CHẠY THẬT'}")
    print("=" * 60)

    if not DISTILLED.exists():
        print(f"[LỖI] Không tìm thấy: {DISTILLED}")
        return

    if not DRY_RUN:
        ensure_dirs()

    files = [f for f in DISTILLED.iterdir() if f.is_file() and f.suffix == ".md"]
    print(f"\n  Tìm thấy {len(files)} file .md trong {DISTILLED}\n")

    stats = {"keep": 0, "move": 0, "skip": 0}
    moves = {}   # dest → [filenames]

    for f in sorted(files):
        dest, reason = classify(f.name)

        # Nếu dest là distilled và file đã ở đó → giữ nguyên
        if dest == DISTILLED:
            print(f"  ✅ GIỮ    {f.name}")
            print(f"           Lý do: {reason}")
            stats["keep"] += 1
            continue

        dest_path = dest / f.name
        tag = "🔵 MOVE  " if not DRY_RUN else "🔵 [DRY]  "
        print(f"  {tag} {f.name}")
        print(f"           → {dest}/{f.name}")
        print(f"           Lý do: {reason}")

        moves.setdefault(str(dest), []).append(f.name)

        if not DRY_RUN:
            if dest_path.exists():
                print(f"           ⚠️  File đã tồn tại ở dest — bỏ qua")
                stats["skip"] += 1
            else:
                shutil.move(str(f), str(dest_path))
                stats["move"] += 1
        else:
            stats["move"] += 1

    # ── BÁO CÁO ───────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  BÁO CÁO TỔNG KẾT")
    print("=" * 60)
    print(f"  ✅ Giữ nguyên trong distilled/ : {stats['keep']} files")
    print(f"  🔵 {'Sẽ move' if DRY_RUN else 'Đã move'}            : {stats['move']} files")
    print(f"  ⚠️  Bỏ qua (trùng)             : {stats['skip']} files")

    if moves:
        print("\n  Phân bổ files sẽ move:")
        for dest_str, fnames in moves.items():
            print(f"  → {dest_str}/ ({len(fnames)} files)")

    if DRY_RUN:
        print("\n  ⚡ Đây là DRY RUN — chưa có gì thay đổi.")
        print("  ⚡ Đổi DRY_RUN = False và chạy lại để thực hiện thật.")
    else:
        print("\n  ✅ Hoàn tất. Kiểm tra lại bằng /lint")

if __name__ == "__main__":
    run()
