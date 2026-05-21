"""
gap_check_batch.py — Batch runner cho gap_check trên toàn bộ chunks của một source.

Usage:
    python scripts/ingest/gap_check_batch.py --source-id arch_thinking_in_systems [--delay 2] [--dry-run]

Reads chunks từ: 3-resources/raw_ingest/<source_id>/chunks/
Writes output vào: 00_Inbox/gap_candidates/

Non-blocking: từng chunk chạy độc lập, lỗi chunk nào thì log DLQ chunk đó,
không dừng batch.
"""

import os
import sys
import time
import argparse
import subprocess
import logging
from pathlib import Path

# --- Config ---
CANONICAL_ROOT = r"D:\NoteBookLLM_Br"
ROOT_DIR = os.getenv("NOTEBOOKLLM_ROOT", CANONICAL_ROOT if os.path.exists(CANONICAL_ROOT) else str(Path(__file__).parent.parent.parent))
GAP_CHECK_SCRIPT = os.path.join(ROOT_DIR, ".agent", "skills", "wiki-ingest", "scripts", "gap_check.py")
PYTHON = os.path.join(ROOT_DIR, ".venv", "Scripts", "python.exe")

logging.basicConfig(
    level=logging.INFO,
    format="[gap_batch] %(levelname)s: %(message)s",
    handlers=[logging.StreamHandler(
        open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1, closefd=False)
    )]
)
log = logging.getLogger(__name__)


def get_chunks(source_id: str) -> list[Path]:
    chunk_dir = Path(ROOT_DIR) / "3-resources" / "raw_ingest" / source_id / "chunks"
    if not chunk_dir.exists():
        log.error(f"Chunk dir not found: {chunk_dir}")
        sys.exit(1)
    chunks = sorted(chunk_dir.glob("*.md"))
    return chunks


def run_gap_check(chunk_path: Path, source_id: str, chunk_num: int, dry_run: bool) -> bool:
    """Chạy gap_check cho một chunk. Trả về True nếu thành công."""
    if dry_run:
        log.info(f"[DRY-RUN] Would check: {chunk_path.name} (chunk #{chunk_num})")
        return True

    cmd = [
        PYTHON, GAP_CHECK_SCRIPT,
        "--chunk", str(chunk_path),
        "--atoms", "[]",          # Batch mode: không có extracted atoms trước, gemma3 tự tìm hoàn toàn
        "--source", source_id,
        "--chunk-num", str(chunk_num),
    ]
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", env=env, timeout=120)
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if stdout:
            for line in stdout.splitlines():
                log.info(f"  [{chunk_path.name}] {line}")
        if stderr:
            for line in stderr.splitlines():
                log.warning(f"  [{chunk_path.name}] STDERR: {line}")

        return result.returncode == 0
    except subprocess.TimeoutExpired:
        log.warning(f"Timeout (120s) for chunk #{chunk_num}: {chunk_path.name}. DLQ logged by gap_check.")
        return False
    except Exception as e:
        log.error(f"Unexpected error for chunk #{chunk_num}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Batch gap-check runner trên toàn bộ chunks của một source.")
    parser.add_argument("--source-id", required=True, help="source_id, ví dụ: arch_thinking_in_systems")
    parser.add_argument("--delay", type=float, default=1.0, help="Giây chờ giữa các chunk (mặc định: 1s, để tránh quá tải Ollama)")
    parser.add_argument("--dry-run", action="store_true", help="Chỉ liệt kê chunks, không gọi Ollama")
    parser.add_argument("--start-from", type=int, default=1, help="Bắt đầu từ chunk số N (để resume)")
    args = parser.parse_args()

    chunks = get_chunks(args.source_id)
    if not chunks:
        log.error(f"Không tìm thấy chunk nào trong source: {args.source_id}")
        sys.exit(1)

    log.info(f"Source: {args.source_id} | Total chunks: {len(chunks)} | Start from: #{args.start_from} | Delay: {args.delay}s")
    if args.dry_run:
        log.info("[DRY-RUN mode] Không gọi Ollama.")

    success_count = 0
    skip_count = 0
    fail_count = 0

    for i, chunk_path in enumerate(chunks, start=1):
        if i < args.start_from:
            skip_count += 1
            continue

        log.info(f"--- Chunk #{i}/{len(chunks)}: {chunk_path.name} ---")
        ok = run_gap_check(chunk_path, args.source_id, i, args.dry_run)

        if ok:
            success_count += 1
        else:
            fail_count += 1

        if i < len(chunks) and not args.dry_run:
            time.sleep(args.delay)

    log.info(f"=== Batch complete === success={success_count} | skipped={skip_count} | fail={fail_count} | total={len(chunks)}")


if __name__ == "__main__":
    main()
