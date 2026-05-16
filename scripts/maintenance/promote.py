import argparse
import os
import pathlib
import re
import shutil
import sys
from datetime import date, datetime

# ---------------------------------------------------------------------------
# CONFIGURATION & RULES
# ---------------------------------------------------------------------------
ROOT_DIR = pathlib.Path("d:/NoteBookLLM_Br")
INBOX_DIR = ROOT_DIR / "00_Inbox"
STAGING_RAW_INGEST = INBOX_DIR / "Staging_Raw_Ingest"
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
ARCHIVE_ROOT = ROOT_DIR / "4-archive"

LOCK_FILE = ROOT_DIR / ".kiro" / "session.lock"
VALID_VERIFY_SCOPES = {"full-source", "chunk", "package"}
STRICT_VERIFY_RESULTS = {"PASS", "WARN", "SKIPPED"}
PERSONAL_VERIFY_RESULTS = {"PASS"}
MIN_AUDIT_SCORE = 0.90


def _check_gatekeeper():
    if os.environ.get("KIRO_CB_ACTIVE") != "1":
        print("\n[GATE KEEPER] BLOCKED: Direct promotion is FORBIDDEN.", file=sys.stderr)
        print("[GATE KEEPER] REASON: You must execute via Circuit Breaker: python .kiro/circuit_breaker.py promote <path>", file=sys.stderr)
        return False

    if not LOCK_FILE.exists():
        print("\n[GATE KEEPER] BLOCKED: Session Lock missing.", file=sys.stderr)
        print("[GATE KEEPER] REASON: Execution detected outside an authorized Circuit Breaker session.", file=sys.stderr)
        return False

    return True

def get_audit_info(md_path):
    """Parses the audit stamp from Markdown frontmatter/header."""
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        if "audit_stamp: true" not in content or "audit:" not in content:
            return None

        audit_lines = []
        in_audit_block = False
        for line in content.splitlines():
            if line.strip() == "audit:":
                in_audit_block = True
                continue
            if in_audit_block:
                if line.startswith("  "):
                    audit_lines.append(line.strip())
                    continue
                break

        audit_map = {}
        for line in audit_lines:
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            audit_map[key.strip()] = value.strip()

        required = {"score", "date", "status"}
        if not required.issubset(audit_map):
            return None

        return {
            "score_str": audit_map["score"],
            "score": float(audit_map["score"]),
            "date": audit_map["date"].strip('"'),
            "status": audit_map["status"].strip('"'),
            "signature": audit_map.get("signature", "").strip('"') or None,
            "verify_result": audit_map.get("verify_result", "").strip('"') or None,
            "verify_scope": audit_map.get("verify_scope", "").strip('"') or None,
        }
    except Exception:
        return None

def verify_hmac_signature(md_path: pathlib.Path, audit: dict) -> bool:
    import hmac, hashlib
    secret = os.environ.get("KIRO_AUDIT_SECRET")
    stored_sig = audit.get("signature")

    # Handle UNSIGNED cases for solo dev
    if stored_sig == "UNSIGNED":
        if not secret:
            print(f"WARNING: Signature is UNSIGNED. Proceeding without HMAC verification for {md_path.name}.")
            return True
        else:
            print(f"BLOCKED: Secret present but signature is UNSIGNED on {md_path.name}. Re-audit required.")
            return False

    if not secret:
        print("BLOCKED: KIRO_AUDIT_SECRET not set.")
        return False
    
    if not stored_sig:
        print(f"BLOCKED: No signature in {md_path.name}.")
        return False
        
    msg = f"{md_path.stem}-{audit['score_str']}-{audit['date']}-v1.0".encode("utf-8")
    expected = hmac.new(secret.encode("utf-8"), msg, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(stored_sig, expected):
        print(f"BLOCKED: CRITICAL - Invalid HMAC Signature. Tampering detected on {md_path.name}!")
        return False
    return True


def resolve_audit_policy(cli_policy: str | None) -> str:
    policy = cli_policy or os.environ.get("AUDIT_POLICY") or "strict"
    return policy


def validate_audit_policy(audit: dict, audit_policy: str) -> bool:
    verify_scope = audit.get("verify_scope")
    verify_result = audit.get("verify_result")
    score = audit.get("score")

    if score is None or score < MIN_AUDIT_SCORE:
        print(f"BLOCKED: Audit score {score} is below threshold {MIN_AUDIT_SCORE:.2f}.")
        return False

    if verify_scope not in VALID_VERIFY_SCOPES:
        print(f"BLOCKED: Invalid verify_scope '{verify_scope}'.")
        return False

    if audit_policy == "personal":
        if verify_result not in PERSONAL_VERIFY_RESULTS:
            print(f"BLOCKED: Personal audit policy requires verify_result PASS. Got '{verify_result}'.")
            return False
        return True

    if verify_result not in STRICT_VERIFY_RESULTS:
        print(f"BLOCKED: Strict audit policy rejected verify_result '{verify_result}'.")
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


def get_package_context(path: pathlib.Path):
    """Return package routing context only for explicit staged package layout."""
    try:
        rel = path.relative_to(STAGING_RAW_INGEST)
    except ValueError:
        return None

    if len(rel.parts) < 2:
        return None

    source_id = rel.parts[0]
    package_rel = pathlib.Path(*rel.parts[1:])
    return {"source_id": source_id, "relative_path": package_rel}


def resolve_package_destination(md_path: pathlib.Path, package_ctx: dict):
    source_id = package_ctx["source_id"]
    relative_path = package_ctx["relative_path"]
    package_root = RAW_INGEST / source_id
    name = md_path.name

    if name.lower() == "outline.md":
        return package_root / "outline.md"
    if name.lower() == "manifest.md" or name.endswith("_MANIFEST.md"):
        return package_root / "manifest.md"
    if name.startswith("RAW_"):
        return package_root / "chunks" / name
    if relative_path.parts and relative_path.parts[0].lower() == "chunks":
        return package_root / "chunks" / name
    return package_root / name

def promote(md_path_str, dry_run=False, audit_policy="strict"):
    if not _check_gatekeeper():
        return False

    md_path = pathlib.Path(md_path_str).resolve()
    audit_policy = resolve_audit_policy(audit_policy)
    print(f"[PROMOTE] audit_policy={audit_policy}")
    
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

        if not validate_audit_policy(audit, audit_policy):
            return False
        if audit_policy == "strict" and not verify_hmac_signature(md_path, audit):
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

    package_ctx = get_package_context(md_path)

    # Define targets with smart routing
    if package_ctx:
        dest_md = resolve_package_destination(md_path, package_ctx)
    elif md_path.name.startswith("CONCEPT_"):
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
        dest_md.parent.mkdir(parents=True, exist_ok=True)

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
    parser.add_argument("--audit-policy", choices=["strict", "personal"], help="Audit policy override")
    
    args = parser.parse_args()
    success = promote(args.path, dry_run=args.dry_run, audit_policy=args.audit_policy)
    sys.exit(0 if success else 1)
