import os
import time
import sys
import subprocess
import argparse
import pathlib
from datetime import datetime

# ROOT_DIR: NoteBookLLM_Br/
ROOT_DIR = pathlib.Path(__file__).parent.parent.parent
LOCK_DIR = ROOT_DIR / ".kiro"
LOCK_FILE = LOCK_DIR / "vram.lock"


def _read_lock_pid():
    try:
        return int(LOCK_FILE.read_text(encoding="utf-8").strip())
    except (OSError, ValueError):
        return None


def _pid_is_alive(pid):
    if pid is None or pid <= 0:
        return False
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False

def acquire_lock(timeout=300):
    """Chờ và lấy quyền sử dụng VRAM bằng cơ chế atomic (O_EXCL)."""
    # Đảm bảo thư mục .kiro tồn tại (Rule R22/R4)
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    
    start_time = time.time()
    while True:
        try:
            # os.O_EXCL đảm bảo file chỉ được tạo nếu nó chưa tồn tại (atomic)
            fd = os.open(str(LOCK_FILE), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode())
            os.close(fd)
            return True  # Lock acquired atomically
        except FileExistsError:
            stale_pid = _read_lock_pid()
            if not _pid_is_alive(stale_pid):
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Removing stale VRAM lock{f' (pid {stale_pid})' if stale_pid else ''}...")
                try:
                    LOCK_FILE.unlink()
                    continue
                except OSError:
                    pass
            # Lock đã tồn tại — kiểm tra timeout
            if time.time() - start_time > timeout:
                print(f"ERROR: VRAM Guard Timeout after {timeout}s.")
                return False
            print(f"[{datetime.now().strftime('%H:%M:%S')}] VRAM in use. Waiting 10s...")
            time.sleep(10)

def release_lock():
    """Giải phóng VRAM."""
    if LOCK_FILE.exists():
        try:
            LOCK_FILE.unlink()
        except OSError:
            pass

def main():
    parser = argparse.ArgumentParser(description="VRAM Resource Guard for GTX 1650 (Atomic Lock)")
    parser.add_argument("command", nargs=argparse.REMAINDER, help="Lệnh AI cần chạy")
    parser.add_argument("--timeout", type=int, default=300, help="Thời gian chờ tối đa (giây)")
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if acquire_lock(timeout=args.timeout):
        try:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Executing with VRAM Guard: {' '.join(args.command)}")
            # Chạy lệnh và truyền trực tiếp stdout/stderr về terminal
            subprocess.run(args.command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"ERROR: Command failed with exit code {e.returncode}")
            sys.exit(e.returncode)
        except KeyboardInterrupt:
            print("\nInterrupted by user. Releasing VRAM...")
            sys.exit(130)
        finally:
            release_lock()
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
