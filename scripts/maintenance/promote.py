import os
import shutil
import re
import pathlib
from datetime import datetime, date
import argparse
import sys

# ---------------------------------------------------------------------------
# CONFIGURATION & RULES
# ---------------------------------------------------------------------------
ROOT_DIR = pathlib.Path("d:/NoteBookLLM_Br")
INBOX_DIR = ROOT_DIR / "00_Inbox"
RAW_INGEST = ROOT_DIR / "3-resources/raw_ingest"
RAW_SOURCES = ROOT_DIR / "3-resources/raw_sources"
RAW_ASSETS = ROOT_DIR / "3-resources/raw_assets"
WIKI_CONCEPTS = ROOT_DIR / "3-resources/wiki/concepts"
WIKI_ENTITIES = ROOT_DIR / "3-resources/wiki/entities"
WIKI_SOURCES = ROOT_DIR / "3-resources/wiki/sources"

WIKI_COMPARISONS = ROOT_DIR / "3-resources/wiki/comparisons"
WIKI_SYNTHESIS = ROOT_DIR / "3-resources/wiki/synthesis"
WIKI_DECISIONS = ROOT_DIR / "3-resources/wiki/decisions"
WIKI_QUERIES = ROOT_DIR / "3-resources/wiki/queries"
WIKI_INSIGHTS = ROOT_DIR / "3-resources/wiki/session_insights"

# ---------------------------------------------------------------------------
# 1. CIRCUIT BREAKER GATE (REQ-CB)
# ---------------------------------------------------------------------------
if os.environ.get("KIRO_CB_ACTIVE") != "1":
    print("\n[GATE KEEPER] BLOCKED: Direct promotion is FORBIDDEN.", file=sys.stderr)
    print("[GATE KEEPER] REASON: You must execute via Circuit Breaker: python .kiro/circuit_breaker.py promote <path>", file=sys.stderr)
    sys.exit(1)

# --- SESSION LOCK GATE ---
LOCK_FILE = ROOT_DIR / ".kiro" / "session.lock"
if not LOCK_FILE.exists():
    print("\n[GATE KEEPER] BLOCKED: Session Lock missing.", file=sys.stderr)
    print("[GATE KEEPER] REASON: Execution detected outside an authorized Circuit Breaker session.", file=sys.stderr)
    sys.exit(1)

def get_audit_info(md_path):
    """Parses the audit stamp from Markdown frontmatter/header."""
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Regex to find audit block in YAML frontmatter
        audit_match = re.search(r'audit:\s*\n\s*score:\s*([\d\.]+)\s*\n\s*date:\s*"(.*?)"\s*\n\s*status:\s*"(.*?)"', content, re.MULTILINE)
        if not audit_match:
            return None
        
        sig_match = re.search(r'audit:.*?signature:\s*"([a-f0-9]+)"', content, re.DOTALL)
        
        return {
            "score": float(audit_match.group(1)),
            "date": audit_match.group(2),
            "status": audit_match.group(3),
            "signature": sig_match.group(1) if sig_match else None
        }
    except Exception:
        return None

def verify_hmac_signature(md_path: pathlib.Path, audit: dict) -> bool:
    import hmac, hashlib
    secret = os.environ.get("KIRO_AUDIT_SECRET")
    if not secret:
        print("BLOCKED: KIRO_AUDIT_SECRET not set.")
        return False
    stored_sig = audit.get("signature")
    if not stored_sig:
        print(f"BLOCKED: No signature in {md_path.name}.")
        return False
    msg = f"{md_path.stem}-{audit['score']:.2f}-{audit['date']}-v1.0".encode("utf-8")
    expected = hmac.new(secret.encode("utf-8"), msg, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(stored_sig, expected):
        print(f"BLOCKED: CRITICAL - Invalid HMAC Signature. Tampering detected on {md_path.name}!")
        return False
    return True

def get_source_pdf(md_path):
    """Detects source PDF name from Markdown body."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Match "Source PDF: filename.pdf"
    pdf_match = re.search(r'^Source PDF:\s*(.*)$', content, re.MULTILINE)
    if pdf_match:
        return pdf_match.group(1).strip()
    return None

def validate_origin(path: pathlib.Path):
    """Ensures the file comes from 00_Inbox."""
    try:
        path.relative_to(INBOX_DIR)
        return True
    except ValueError:
        return False

def promote(md_path_str, dry_run=False):
    md_path = pathlib.Path(md_path_str).resolve()
    
    # --- GATE 1: Existence ---
    if not md_path.exists():
        print(f"ERROR: File not found: {md_path}")
        return False

    # --- GATE 2: Origin (00_Inbox Only) ---
    if not validate_origin(md_path):
        print(f"BLOCKED: Security Violation. File {md_path.name} is outside 00_Inbox.")
        print(f"   Origin must be: {INBOX_DIR}")
        return False

    # --- GATE 3: Audit Stamp ---
    audit = get_audit_info(md_path)
    if not audit:
        print(f"BLOCKED: No valid audit stamp found in {md_path.name}. Run md_auditor.py --fix first.")
        return False
    
    if audit["status"] != "PASSED":
        print(f"BLOCKED: Audit status is '{audit['status']}'. Only 'PASSED' files can be promoted.")
        return False
    
    # Freshness check
    try:
        audit_date = datetime.strptime(audit["date"], "%Y-%m-%d").date()
        if (date.today() - audit_date).days > 7:
            print(f"BLOCKED: Audit stamp is stale ({audit['date']}). Re-audit required.")
            return False
        
        # --- HMAC Signature Check ---
        if not verify_hmac_signature(md_path, audit):
            return False
    except ValueError:
        print(f"ERROR: Malformed audit date: {audit['date']}")
        return False

    # --- ROUTING LOGIC ---
    pdf_name = get_source_pdf(md_path)
    # Search for PDF in 00_Inbox
    pdf_src_path = None
    if pdf_name:
        for p in INBOX_DIR.rglob(pdf_name):
            pdf_src_path = p
            break

    # Define targets with smart routing
    if md_path.name.startswith("CONCEPT_"):
        dest_md = WIKI_CONCEPTS / md_path.name
    elif md_path.name.startswith("ENTITY_"):
        dest_md = WIKI_ENTITIES / md_path.name
    elif md_path.name.startswith("SOURCE_"):
        dest_md = WIKI_SOURCES / md_path.name
    elif md_path.name.startswith("COMPARISON_"):
        dest_md = WIKI_COMPARISONS / md_path.name
    elif md_path.name.startswith("SYNTHESIS_"):
        dest_md = WIKI_SYNTHESIS / md_path.name
    elif md_path.name.startswith("DECISION_"):
        dest_md = WIKI_DECISIONS / md_path.name
    elif md_path.name.startswith("QUERY_"):
        dest_md = WIKI_QUERIES / md_path.name
    elif md_path.name.startswith("INSIGHT_"):
        dest_md = WIKI_INSIGHTS / md_path.name
    else:
        dest_md = RAW_INGEST / md_path.name
        
    dest_pdf = RAW_SOURCES / pdf_name if pdf_name else None
    
    assets_to_move = []
    bad_prefix_assets = []
    for folder_name in ["assets", "images"]:
        local_assets_dir = md_path.parent / folder_name
        if local_assets_dir.exists():
            for asset_file in local_assets_dir.glob("*"):
                if asset_file.is_file():
                    # --- GATE 4: Asset Prefix Validation ---
                    # Tên asset phải bắt đầu bằng tên sách gốc, không phải "chunk_"
                    if asset_file.name.startswith("chunk_"):
                        bad_prefix_assets.append(asset_file.name)
                    else:
                        assets_to_move.append((asset_file, RAW_ASSETS / asset_file.name))

    if bad_prefix_assets:
        print(f"BLOCKED: Asset Prefix Violation — {len(bad_prefix_assets)} file(s) dùng prefix 'chunk_' thay vì tên sách:")
        for name in bad_prefix_assets:
            print(f"  ✗ {name}")
        print("  Fix: Re-run hd_converter.py (đã được fix prefix chuẩn).")
        return False

    if dry_run:
        print(f"\n--- [DRY RUN] Promotion Plan for {md_path.name} ---")
        print(f"[MD]  {md_path.name} -> {dest_md.relative_to(ROOT_DIR)}")
        if pdf_src_path:
            print(f"[SRC] {pdf_name} -> {dest_pdf.relative_to(ROOT_DIR)}")
        for src, dst in assets_to_move:
            print(f"[AST] {src.name} -> {dst.relative_to(ROOT_DIR)}")
        return True

    # --- EXECUTION ---
    try:
        # Create directories if missing
        RAW_INGEST.mkdir(parents=True, exist_ok=True)
        RAW_SOURCES.mkdir(parents=True, exist_ok=True)
        RAW_ASSETS.mkdir(parents=True, exist_ok=True)
        WIKI_CONCEPTS.mkdir(parents=True, exist_ok=True)
        WIKI_ENTITIES.mkdir(parents=True, exist_ok=True)
        WIKI_SOURCES.mkdir(parents=True, exist_ok=True)

        # 1. Move MD
        shutil.move(str(md_path), str(dest_md))
        print(f"PROMOTED MD: {md_path.name}")

        # 2. Move PDF
        if pdf_src_path and pdf_src_path.exists():
            if not dest_pdf.exists():
                shutil.move(str(pdf_src_path), str(dest_pdf))
                print(f"ARCHIVED SRC: {pdf_name}")
            else:
                os.remove(pdf_src_path)

        # 3. Move Assets
        for src, dst in assets_to_move:
            if not dst.exists():
                shutil.move(str(src), str(dst))
                print(f"MOVED ASSET: {src.name}")
            else:
                os.remove(src)

        # 4. Cleanup empty temp folder
        temp_folder = md_path.parent
        if "Converted_Sources" in str(temp_folder):
            if not list(temp_folder.glob("*.md")):
                shutil.rmtree(temp_folder)
                print(f"CLEANED: {temp_folder.name}")
        
        return True

    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Secure Wiki Promotion Gate.")
    parser.add_argument("path", help="Path to the audited Markdown file in 00_Inbox/")
    parser.add_argument("--dry-run", action="store_true", help="Preview actions")
    
    args = parser.parse_args()
    success = promote(args.path, dry_run=args.dry_run)
    sys.exit(0 if success else 1)
