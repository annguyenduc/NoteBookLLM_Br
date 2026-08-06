import json
import sys
import os
from pathlib import Path
from typing import List, Dict

# Rule 11 mandated sequence
REQUIRED_SEQUENCE = ["profiler", "designer", "engineer"]

MANIFEST_PATH = Path("storage/execution_manifest.jsonl")

# Ensure output is utf-8 to avoid encoding errors on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def load_manifest() -> List[Dict]:
    """Load entries from the execution manifest."""
    if not MANIFEST_PATH.exists():
        return []
    
    entries = []
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return entries

def verify_sequence(entries: List[Dict]) -> bool:
    """Check if the required agents ran in the correct order."""
    if not entries:
        print("[FAIL] Manifest trống. Không có agent nào được thực thi.")
        return False

    agents_ran = [e["agent"] for e in entries]
    print(f"Pipeline thực tế: {' -> '.join(agents_ran)}")

    # Sequence check logic
    idx = 0
    missing = []
    for required in REQUIRED_SEQUENCE:
        found = False
        while idx < len(agents_ran):
            if agents_ran[idx] == required:
                found = True
                idx += 1
                break
            idx += 1
        
        if not found:
            missing.append(required)
    
    if missing:
        print(f"[FAIL] Thiếu agent hoặc sai thứ tự: {', '.join(missing)}")
        return False
    
    print("[PASS] Pipeline sequence verified (Rule 11 compliant)")
    return True

def clean_manifest():
    """Delete the manifest file."""
    if MANIFEST_PATH.exists():
        os.remove(MANIFEST_PATH)
        print("Đã xóa execution manifest cũ.")
    else:
        print("Không tìm thấy manifest cũ để xóa.")

def main():
    if "--clean" in sys.argv:
        clean_manifest()
        return

    print("--- SWARM ORCHESTRATION VERIFIER ---")
    entries = load_manifest()
    
    if not entries:
        print(f"⚠️ Không tìm thấy dữ liệu trong {MANIFEST_PATH}")
        return

    # Print summary table
    print(f"{'Timestamp':<20} | {'Agent':<15} | {'Model':<30} | {'Request ID'}")
    print("-" * 90)
    for e in entries:
        print(f"{e.get('ts', 'N/A'):<20} | {e.get('agent', 'N/A'):<15} | {e.get('model', 'N/A')[:30]:<30} | {e.get('request_id', 'N/A')}")
    print("-" * 90)

    success = verify_sequence(entries)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
