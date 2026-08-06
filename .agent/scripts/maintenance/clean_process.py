"""
clean_process.py — Dọn 3-resources/process/, move đúng file về đúng chỗ
Chạy từ root repo: python scripts/clean_process.py

Logic phân loại:
  Giữ trong process/  → handoff files (Learning_Design, Trainer_Profile, 
                         EXAM_Context, Eval_Report)
  Move → distilled/   → test bank thật sự (có pattern đề trắc nghiệm)
  Move → raw/         → dump/KB thô chưa distill đúng
  Move → docs/        → config, index không phải knowledge
"""

import shutil
from pathlib import Path

# ── CẤU HÌNH ──────────────────────────────────────────────────────────────────
REPO_ROOT = Path(".")
PROCESS   = REPO_ROOT / "3-resources" / "process"
DISTILLED = REPO_ROOT / "3-resources" / "distilled"
RAW       = REPO_ROOT / "3-resources" / "raw"
DOCS      = REPO_ROOT / "docs"
DRY_RUN   = False  # ← Đổi False khi muốn chạy thật

# ── RULES ─────────────────────────────────────────────────────────────────────
# File khớp pattern → move tới dest tương ứng
# Ưu tiên từ trên xuống — khớp rule đầu tiên thì dừng

KEEP_IN_PROCESS = [
    "learning_design_",
    "trainer_profile_",
    "exam_context_",
    "eval_report_",
    "continuity",
]

MOVE_TO_DISTILLED = [
    "_đề_",           # Đề trắc nghiệm tiếng Việt
    "_de_",           # Không dấu
    "trac_nghiem",    # Trắc nghiệm
    "tracnghiem",
    "_bank",          # Test bank
    "lms_tests_",
]

MOVE_TO_DOCS = [
    "agents-index",
    "agents_index",
    "model_index",
    "capacity_index",
]

# Còn lại không khớp gì → RAW (an toàn)

# ── LOGIC ─────────────────────────────────────────────────────────────────────
def classify(filename: str):
    name = filename.lower()

    for pat in KEEP_IN_PROCESS:
        if pat in name:
            return None, "GIỮ — handoff file"

    for pat in MOVE_TO_DISTILLED:
        if pat in name:
            return DISTILLED, "Test bank → distilled/"

    for pat in MOVE_TO_DOCS:
        if pat in name:
            return DOCS, "Config → docs/"

    return RAW, "Không rõ loại → raw/ (an toàn)"

def run():
    print("=" * 60)
    print(f"  clean_process.py — {'DRY RUN' if DRY_RUN else '🚨 CHẠY THẬT'}")
    print("=" * 60)

    if not PROCESS.exists():
        print(f"[LỖI] Không tìm thấy: {PROCESS}")
        return

    files = sorted([f for f in PROCESS.iterdir() if f.is_file()])
    print(f"\n  Tìm thấy {len(files)} files trong process/\n")

    stats = {"keep": 0, "move": 0, "skip": 0}
    summary = {}

    for f in files:
        dest, reason = classify(f.name)

        if dest is None:
            print(f"  ✅ GIỮ     {f.name[:70]}")
            stats["keep"] += 1
            continue

        label = "🔵 [DRY]" if DRY_RUN else "🔵 MOVE "
        print(f"  {label}  {f.name[:60]}")
        print(f"             → {dest.name}/ | {reason}")

        summary.setdefault(dest.name, []).append(f.name)

        if not DRY_RUN:
            dest.mkdir(parents=True, exist_ok=True)
            dest_path = dest / f.name
            if dest_path.exists():
                print(f"             ⚠️  Đã tồn tại — bỏ qua")
                stats["skip"] += 1
            else:
                shutil.move(str(f), str(dest_path))
                stats["move"] += 1
        else:
            stats["move"] += 1

    # ── BÁO CÁO ───────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  KẾT QUẢ")
    print("=" * 60)
    print(f"  ✅ Giữ trong process/ : {stats['keep']} files")
    print(f"  🔵 {'Sẽ' if DRY_RUN else 'Đã'} move          : {stats['move']} files")
    print(f"  ⚠️  Bỏ qua (trùng)    : {stats['skip']} files")

    if summary:
        print("\n  Phân bổ:")
        for dest_name, fnames in summary.items():
            print(f"  → {dest_name}/ : {len(fnames)} files")
            for fn in fnames[:5]:
                print(f"      • {fn[:65]}")
            if len(fnames) > 5:
                print(f"      ... và {len(fnames)-5} files nữa")

    if DRY_RUN:
        print("\n  ⚡ DRY RUN — chưa thay đổi gì.")
        print("  ⚡ Đổi DRY_RUN = False và chạy lại để thực hiện.")
    else:
        print("\n  ✅ Xong. Chạy /lint để verify.")

if __name__ == "__main__":
    run()
