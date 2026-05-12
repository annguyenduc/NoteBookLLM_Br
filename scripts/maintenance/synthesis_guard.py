"""
synthesis_guard.py -- R8 Compliance: Human Supremacy Gate
===========================================================
Blocks any status -> SYNTHESIZED change unless run interactively by Human.
Blocks direct writes to 3-resources/wiki/synthesis/ by agents.

Rules applied:
  R8  -- Only Human may set status = SYNTHESIZED
  R17 -- Physical file is Source of Truth

Commands:
  check   -- Verify a write operation is safe (call before any file write)
  approve -- Set SYNTHESIZED interactively (Human only, requires TTY)
  scan    -- Report synthesis/ directory status

Exit codes:
  0 -- OK / approved
  1 -- BLOCKED (R8 violation) or cancelled
  2 -- File not found / read error
"""

from __future__ import annotations

import re
import sys
import pathlib
import argparse
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).parent.parent.parent   # d:\NoteBookLLM_Br
SYNTHESIS_DIR = ROOT / "3-resources" / "wiki" / "synthesis"
LOG_DIR = ROOT / "3-resources" / "wiki" / "logs"
GUARD_LOG = ROOT / ".kiro" / "synthesis_guard_log.md"
WIKI_DIR = ROOT / "3-resources" / "wiki"
SCAN_DIRS = [
    "concepts", "entities", "sources",
    "comparisons", "review_queue", "synthesis"
]

PROTECTED_STATUS = {"SYNTHESIZED"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _append_guard_log(action: str, file_path: str, result: str, note: str = "") -> None:
    """Append-only audit trail."""
    GUARD_LOG.parent.mkdir(parents=True, exist_ok=True)
    entry = (
        f"\n- timestamp: {_now_iso()}\n"
        f"  action: {action}\n"
        f"  file: {file_path}\n"
        f"  result: {result}\n"
        f"  note: {note or '~'}\n"
    )
    with GUARD_LOG.open("a", encoding="utf-8") as f:
        f.write(entry)


def _read_frontmatter_status(file_path: pathlib.Path) -> str | None:
    """Extract status field from YAML frontmatter."""
    if not file_path.exists():
        return None
    try:
        content = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None
    match = re.search(r'^status:\s*["\']?(\w+)["\']?', content, re.MULTILINE)
    return match.group(1).upper() if match else None


def _is_in_synthesis_dir(file_path: pathlib.Path) -> bool:
    try:
        file_path.resolve().relative_to(SYNTHESIS_DIR.resolve())
        return True
    except ValueError:
        return False


# ---------------------------------------------------------------------------
# check command
# ---------------------------------------------------------------------------

def cmd_check(file_path_str: str, proposed_content: str | None = None) -> int:
    """
    Verify a write operation is safe before executing it.

    Three checks:
      1. File is not inside synthesis/ directory
      2. Existing file does not already have status=SYNTHESIZED
      3. Proposed content does not contain status=SYNTHESIZED

    Check 3 is the critical one -- it catches agents trying to write
    SYNTHESIZED into concepts/, entities/, or any other wiki directory.
    """
    file_path = pathlib.Path(file_path_str).resolve()

    # Check 1: synthesis/ directory is off-limits for agents
    if _is_in_synthesis_dir(file_path):
        print(
            "[SYNTHESIS GUARD] BLOCKED -- R8 VIOLATION\n"
            f"  File  : {file_path}\n"
            "  Reason: Direct write to synthesis/ is blocked for agents.\n"
            "  Fix   : Have the Human edit this file directly in Obsidian.",
            file=sys.stderr
        )
        _append_guard_log("check", str(file_path), "BLOCKED",
                          "Write to synthesis/ by agent")
        return 1

    # Check 2: cannot modify an already-SYNTHESIZED atom
    if file_path.exists():
        current = _read_frontmatter_status(file_path)
        if current in PROTECTED_STATUS:
            print(
                "[SYNTHESIS GUARD] BLOCKED -- R8 VIOLATION\n"
                f"  File   : {file_path}\n"
                f"  Status : {current} (protected)\n"
                "  Reason : Cannot modify a SYNTHESIZED atom.\n"
                "  Fix    : Human must revert status to VERIFIED first.",
                file=sys.stderr
            )
            _append_guard_log("check", str(file_path), "BLOCKED",
                              "Attempt to modify SYNTHESIZED atom")
            return 1

    # Check 3: proposed content must not set status=SYNTHESIZED
    if proposed_content is not None:
        m = re.search(r'^status:\s*["\']?(\w+)["\']?', proposed_content, re.MULTILINE)
        if m and m.group(1).upper() in PROTECTED_STATUS:
            print(
                "[SYNTHESIS GUARD] BLOCKED -- R8 VIOLATION\n"
                f"  File            : {file_path}\n"
                f"  Proposed status : {m.group(1).upper()}\n"
                "  Reason          : Agents cannot set status=SYNTHESIZED on ANY Atom.\n"
                "                    This applies to concepts/, entities/, review_queue/, etc.\n"
                "  Fix             : Use status=VERIFIED instead.\n"
                "                    Only the Human may set SYNTHESIZED.",
                file=sys.stderr
            )
            _append_guard_log("check", str(file_path), "BLOCKED",
                              f"Proposed SYNTHESIZED in {file_path.parent.name}/")
            return 1

    print(f"[SYNTHESIS GUARD] OK -- {file_path.name} is safe to write.")
    _append_guard_log("check", str(file_path), "OK")
    return 0


# ---------------------------------------------------------------------------
# approve command
# ---------------------------------------------------------------------------

def cmd_approve(file_path_str: str) -> int:
    """
    TERMINAL-ONLY. Requires keyboard input from a human.
    Cannot be called from scripts, agents, or subprocesses.
    This is not an automation endpoint. There is no bypass.

    Human usage (run directly in terminal):
      python scripts/maintenance/synthesis_guard.py approve <file>
    """
    # TTY gate: block non-interactive callers (agents, pipelines, subprocesses)
    if not sys.stdin.isatty():
        print(
            "[SYNTHESIS GUARD] BLOCKED -- R8 VIOLATION\n"
            "  The 'approve' command requires an interactive terminal.\n"
            "  Agents cannot run this command -- it is for the Human only.\n"
            "\n"
            "  To approve, open a terminal and run:\n"
            f"    python scripts/maintenance/synthesis_guard.py approve \"{file_path_str}\"",
            file=sys.stderr
        )
        _append_guard_log("approve", file_path_str, "BLOCKED",
                          "Non-interactive context -- agent attempted approve")
        return 1

    file_path = pathlib.Path(file_path_str).resolve()

    if not file_path.exists():
        print(f"[SYNTHESIS GUARD] ERROR -- File not found: {file_path}", file=sys.stderr)
        return 2

    # Interactive confirmation
    print(f"\n[SYNTHESIS GUARD] Human Approval Required")
    print(f"  File   : {file_path.name}")
    print(f"  Action : Set status = SYNTHESIZED")
    print(f"  This confirms YOU have reviewed and approved this Atom.")
    confirm = input("\n  Type 'YES' to confirm: ").strip()
    if confirm != "YES":
        print("[SYNTHESIS GUARD] Cancelled -- status unchanged.")
        _append_guard_log("approve", str(file_path), "CANCELLED",
                          "Human did not confirm")
        return 1

    # Read file
    try:
        content = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            content = file_path.read_text(encoding="utf-16")
        except Exception as e:
            print(f"[SYNTHESIS GUARD] ERROR -- Cannot read file: {e}", file=sys.stderr)
            return 2

    # Update status
    if re.search(r'^status:', content, re.MULTILINE):
        new_content = re.sub(
            r'^(status:\s*)["\']?\w+["\']?',
            r'\1SYNTHESIZED',
            content,
            flags=re.MULTILINE
        )
    else:
        new_content = content.replace("---\n", "---\nstatus: SYNTHESIZED\n", 1)

    file_path.write_text(new_content, encoding="utf-8")

    # Daily log entry
    today = datetime.now().strftime("%Y_%m_%d")
    log_file = LOG_DIR / f"log_{today}.md"
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_entry = (
        f"\n## {_now_iso()} -- SYNTHESIZED approved\n"
        f"- file: `{file_path.name}`\n"
        f"- action: status set to SYNTHESIZED by Human via synthesis_guard.py\n"
        f"- path: `{file_path}`\n"
    )
    with log_file.open("a", encoding="utf-8") as f:
        f.write(log_entry)

    print(f"[SYNTHESIS GUARD] APPROVED -- {file_path.name} -> status: SYNTHESIZED")
    print(f"  Log entry written to: {log_file.name}")
    _append_guard_log("approve", str(file_path), "APPROVED",
                      "Human-approved SYNTHESIZED transition")
    return 0


# ---------------------------------------------------------------------------
# scan command
# ---------------------------------------------------------------------------

def cmd_scan() -> int:
    """
    Scan ALL wiki/ subdirectories for unauthorized SYNTHESIZED atoms.
    Any SYNTHESIZED atom outside synthesis/ without audit trail
    is flagged as R8 violation and auto-reverted to VERIFIED.
    """
    if not WIKI_DIR.exists():
        print(f"[SYNTHESIS GUARD] wiki/ not found: {WIKI_DIR}")
        return 0

    files = []
    for subdir in SCAN_DIRS:
        scan_path = WIKI_DIR / subdir
        if scan_path.exists():
            files.extend(scan_path.glob("*.md"))

    if not files:
        print("[SYNTHESIS GUARD] All wiki subdirectories are empty.")
        return 0

    approved_files: set[str] = set()
    if GUARD_LOG.exists():
        log_content = GUARD_LOG.read_text(encoding="utf-8")
        for m in re.finditer(r'action: approve.*?file: (.+)', log_content, re.DOTALL):
            approved_files.add(m.group(1).strip())

    print(f"\n[SYNTHESIS GUARD] Scan: {WIKI_DIR}")
    print("=" * 60)

    issues = 0
    for f in sorted(files, key=lambda x: (x.parent.name, x.name)):
        status = _read_frontmatter_status(f) or "UNKNOWN"
        has_trail = str(f.resolve()) in approved_files

        # Auto-revert: SYNTHESIZED ngoài synthesis/ mà không có audit trail
        if status == "SYNTHESIZED" and not has_trail:
            if not _is_in_synthesis_dir(f):
                try:
                    content = f.read_text(encoding="utf-8")
                    new_content = re.sub(
                        r'^(status:\s*)["\']?SYNTHESIZED["\']?',
                        r'\1VERIFIED',
                        content,
                        flags=re.MULTILINE
                    )
                    f.write_text(new_content, encoding="utf-8")
                    print(f"  [REVERT] {f.parent.name}/{f.name} -- SYNTHESIZED->VERIFIED (unauthorized)")
                    _append_guard_log("auto-revert", str(f), "REVERTED",
                                      f"Unauthorized SYNTHESIZED in {f.parent.name}/")
                    issues += 1
                except Exception as e:
                    print(f"  [ERROR] Could not revert {f.name}: {e}")
            else:
                print(f"  [WARN] {f.parent.name}/{f.name} -- SYNTHESIZED -- no audit trail")
                issues += 1
        elif status == "SYNTHESIZED":
            print(f"  [OK]   {f.parent.name}/{f.name} -- {status} -- audit trail OK")

    print("=" * 60)
    print(f"  Total Files Scanned: {len(files)} | Issues/Reverts: {issues}")
    return 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="synthesis_guard.py -- R8 Compliance: Human Supremacy Gate"
    )
    subparsers = parser.add_subparsers(dest="command")

    p_check = subparsers.add_parser("check", help="Verify write is safe (R8)")
    p_check.add_argument("file", help="Path to file being written")
    p_check.add_argument("--content", default=None,
                         help="Proposed content to write (checks for SYNTHESIZED)")

    p_approve = subparsers.add_parser(
        "approve",
        help="[HUMAN ONLY] Set status=SYNTHESIZED interactively"
    )
    p_approve.add_argument("file", help="Path to Atom file")

    subparsers.add_parser("scan", help="Report synthesis/ directory status")

    args = parser.parse_args()

    if args.command == "check":
        sys.exit(cmd_check(args.file, proposed_content=args.content))
    elif args.command == "approve":
        sys.exit(cmd_approve(args.file))
    elif args.command == "scan":
        sys.exit(cmd_scan())
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
