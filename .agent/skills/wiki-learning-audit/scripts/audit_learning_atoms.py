"""
audit_learning_atoms.py  (v1.2 — schema-corrected & path-resolved)
==================================================================
Scan vault DB for Atoms where learning_source=1 (DB column, not metadata JSON)
and status != SYNTHESIZED, then push them into review_queue for human verification.

Schema confirmed from wiki_brain.db:
  atoms(file_id, title, type, status, confidence, learning_source INTEGER,
        file_hash, agent_id, human_review_flag, last_modified, metadata, summary)
  review_queue(item_id, reason)
  task_logs(agent_id, action, target_file, status, details)

Usage:
    python audit_learning_atoms.py [--dry-run] [--limit N] [--domain SLUG] [--since DATE]

Options:
    --dry-run       Print affected Atoms, make no changes (always run this first)
    --limit N       Override max_items cap (default: 10)
    --domain SLUG   Filter by domain tag inferred from file_id path or metadata
    --since DATE    Only flag Atoms last_modified after this date (YYYY-MM-DD)
    --show-patch    Print ingest.py patch instructions and exit
"""

import os
import sys
import json
import sqlite3
import argparse
from datetime import datetime

if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

# ── Paths ──────────────────────────────────────────────────────────────────────
ROOT_DIR = os.getenv(
    "NOTEBOOKLLM_ROOT",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
WIKI_DIR = os.path.join(ROOT_DIR, "3-resources", "wiki")
DB_PATH  = os.path.join(WIKI_DIR, "wiki_brain.db")
LOG_FILE = os.path.join(WIKI_DIR, "log.md")

# ── Constants ──────────────────────────────────────────────────────────────────
DEFAULT_LIMIT      = 10
CONFIDENCE_PENALTY = 0.1
CONFIDENCE_FLOOR   = 0.5
SKIP_STATUS        = "SYNTHESIZED"   # human-verified, never touch
QUEUE_REASON       = "learning_unverified"


# ── Helpers ────────────────────────────────────────────────────────────────────

def log_wiki(cursor, action: str, file_id: str, reason: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = (
        f"\n## [{now}] {action.upper()} | wiki-learning-audit | {reason}\n"
        f"- File: {file_id}\n"
        f"- Lý do: {reason}\n"
    )
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
    except OSError:
        pass  # log is best-effort

    try:
        cursor.execute(
            "INSERT INTO task_logs (agent_id, action, target_file, status, details)"
            " VALUES (?, ?, ?, ?, ?)",
            ("wiki-learning-audit", action, file_id, "flagged", reason),
        )
    except sqlite3.OperationalError:
        pass  # graceful if task_logs schema differs


def new_confidence(current) -> float:
    """Apply penalty, respect floor."""
    base = float(current) if current is not None else 0.7
    return max(round(base - CONFIDENCE_PENALTY, 4), CONFIDENCE_FLOOR)


def already_in_queue(cursor, file_id: str) -> bool:
    """Avoid double-inserting the same Atom."""
    cursor.execute(
        "SELECT 1 FROM review_queue WHERE item_id = ? AND reason = ?",
        (file_id, QUEUE_REASON),
    )
    return cursor.fetchone() is not None


def matches_domain(file_id: str, metadata_json, domain: str | None) -> bool:
    """
    Return True if no filter given.
    Checks metadata JSON domain/tags field first, then falls back to file_id path.
    """
    if not domain:
        return True
    d = domain.lower()

    if metadata_json:
        try:
            meta = json.loads(metadata_json)
            tags = meta.get("domain", meta.get("tags", []))
            if isinstance(tags, str):
                tags = [tags]
            if any(d in t.lower() for t in tags):
                return True
        except (json.JSONDecodeError, AttributeError):
            pass

    return d in file_id.lower()


def update_frontmatter_flag(file_id: str) -> bool:
    """
    Best-effort: inject needs_practice_verification: true into markdown frontmatter.
    Resolves candidates based on NoteBookLLM_Br directory structure.
    Returns True if file was patched.
    """
    candidates = []
    # If absolute path is given and exists
    if os.path.isabs(file_id):
        path = file_id if file_id.endswith(".md") else file_id + ".md"
        candidates.append(path)
    
    # Try relative inside Wiki subdirectories
    for sub in ("concepts", "entities", "sources", "review_queue"):
        base = file_id if file_id.endswith(".md") else file_id + ".md"
        candidates.append(os.path.join(WIKI_DIR, sub, os.path.basename(base)))
        candidates.append(os.path.join(WIKI_DIR, sub, base))

    path = next((p for p in candidates if os.path.isfile(p)), None)
    if not path:
        return False

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if "needs_practice_verification: true" in content:
        return True  # already set

    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            new_content = (
                content[:end]
                + "needs_practice_verification: true\n"
                + content[end:]
            )
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True

    return False


# ── Core audit ────────────────────────────────────────────────────────────────

def run_audit(
    dry_run: bool = True,
    limit: int = DEFAULT_LIMIT,
    domain: str | None = None,
    since: str | None = None,
) -> list[dict]:
    """
    Find eligible Atoms (learning_source=1, status != SYNTHESIZED)
    and (if not dry_run) flag them into review_queue.
    Returns list of affected Atom dicts for reporting.
    """
    if not os.path.isfile(DB_PATH):
        print(f"[ERROR] DB not found: {DB_PATH}")
        print("        Set NOTEBOOKLLM_ROOT env var or run from vault root.")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Use DB column directly — no JSON parsing needed for primary filter
    sql = """
        SELECT file_id, title, status, confidence, metadata, last_modified
        FROM atoms
        WHERE learning_source = 1
          AND status != ?
        ORDER BY last_modified ASC
    """
    rows = cursor.execute(sql, (SKIP_STATUS,)).fetchall()

    # Python-side filters: domain + since
    eligible = []
    for row in rows:
        if not matches_domain(row["file_id"], row["metadata"], domain):
            continue
        if since:
            modified = (row["last_modified"] or "")[:10]
            if modified and modified < since:
                continue
        eligible.append(dict(row))

    eligible = eligible[:limit]

    if not eligible:
        print("✓ No unverified learning Atoms found matching the criteria.")
        conn.close()
        return []

    # ── Dry run: report only ───────────────────────────────────────────────────
    if dry_run:
        print(f"\n[DRY RUN] {len(eligible)} Atom(s) would be flagged:\n")
        print(f"  {'#':<4} {'title':<38} {'status':<12} {'conf':<8} {'last_modified'}")
        print("  " + "-" * 90)
        for i, a in enumerate(eligible, 1):
            conf = f"{float(a['confidence']):.2f}" if a["confidence"] is not None else "n/a"
            mod  = (a["last_modified"] or "")[:16]
            print(f"  {i:<4} {str(a['title']):<38} {str(a['status']):<12} {conf:<8} {mod}")
        print(f"\n  Re-run without --dry-run to apply changes.")
        conn.close()
        return eligible

    # ── Execute ────────────────────────────────────────────────────────────────
    flagged = []
    skipped_queue = 0

    for atom in eligible:
        fid      = atom["file_id"]
        title    = atom["title"]
        conf     = atom["confidence"]
        new_conf = new_confidence(conf)

        # 1. Update confidence + set human_review_flag
        cursor.execute(
            "UPDATE atoms SET confidence = ?, human_review_flag = 1 WHERE file_id = ?",
            (new_conf, fid),
        )

        # 2. Push to review_queue (idempotent)
        if already_in_queue(cursor, fid):
            skipped_queue += 1
        else:
            cursor.execute(
                "INSERT INTO review_queue (item_id, reason) VALUES (?, ?)",
                (fid, QUEUE_REASON),
            )

        # 3. Patch frontmatter on disk (best-effort, non-blocking)
        patched = update_frontmatter_flag(fid)

        # 4. Log
        conf_str = f"{float(conf):.2f}" if conf is not None else "n/a"
        log_wiki(
            cursor, "FLAG", fid,
            f"learning_unverified | conf {conf_str} → {new_conf:.2f} | md_patched={patched}",
        )

        flagged.append({**atom, "new_confidence": new_conf, "frontmatter_patched": patched})
        print(f"  [FLAGGED] {title} | conf {conf_str} → {new_conf:.2f} | md={'✓' if patched else '✗'}")

    conn.commit()
    conn.close()
    return flagged


# ── Report ────────────────────────────────────────────────────────────────────

def print_report(flagged: list[dict]):
    if not flagged:
        return

    domains: dict[str, int] = {}
    for a in flagged:
        parts = a["file_id"].replace("\\", "/").lower().split("/")
        d = next(
            (p for p in reversed(parts)
             if p not in {"wiki", "3-resources", "atoms", "concepts", "entities", ""}),
            "unknown"
        )
        domains[d] = domains.get(d, 0) + 1

    oldest = min(
        (a for a in flagged if a.get("last_modified")),
        key=lambda a: a["last_modified"],
        default=None,
    )

    print(f"\n{'='*62}")
    print(f"  AUDIT COMPLETE — {len(flagged)} Atom(s) pushed to review queue")
    print(f"{'='*62}")
    print(f"  Domains  : {', '.join(f'{k}({v})' for k, v in domains.items())}")
    if oldest:
        print(f"  Oldest   : {oldest['title']} ({(oldest['last_modified'] or '')[:10]})")
    print(f"  Queue tag: {QUEUE_REASON}")
    print(f"  Next step: weekly review → verify through practice → SYNTHESIZED")
    print(f"{'='*62}\n")


# ── Ingest patch hint ─────────────────────────────────────────────────────────

def print_ingest_patch_hint():
    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INGEST PIPELINE PATCH NEEDED
  File: .agent/skills/wiki-ingest/scripts/ingest.py

  Current code is likely defaulting learning_source to 0.

  Patch — add --learning flag to ingest.py CLI:
  
  Usage after patch:
    python ingest.py <file> --learning   # research/reading source → auditable
    python ingest.py <file>              # practice-verified source → default
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")


# ── CLI ───────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(
        description="Audit learning_source Atoms and push to review queue."
    )
    p.add_argument("--dry-run", action="store_true", default=False,
                   help="Preview only — make no changes")
    p.add_argument("--limit", type=int, default=DEFAULT_LIMIT,
                   help=f"Max Atoms to flag per run (default {DEFAULT_LIMIT})")
    p.add_argument("--domain", type=str, default=None,
                   help="Filter by domain (path substring or metadata tag)")
    p.add_argument("--since", type=str, default=None,
                   help="Only flag Atoms with last_modified >= YYYY-MM-DD")
    p.add_argument("--show-patch", action="store_true", default=False,
                   help="Print ingest.py patch instructions and exit")
    return p.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.show_patch:
        print_ingest_patch_hint()
        sys.exit(0)

    mode = "DRY RUN" if args.dry_run else "LIVE"
    print(f"\n[wiki-learning-audit v1.2] Mode={mode} | limit={args.limit}"
          + (f" | domain={args.domain}" if args.domain else "")
          + (f" | since={args.since}" if args.since else "")
          + "\n")

    flagged = run_audit(
        dry_run=args.dry_run,
        limit=args.limit,
        domain=args.domain,
        since=args.since,
    )

    if not args.dry_run:
        print_report(flagged)

    # Always hint about ingest patch when 0 atoms found
    if not flagged and not args.show_patch:
        print_ingest_patch_hint()
