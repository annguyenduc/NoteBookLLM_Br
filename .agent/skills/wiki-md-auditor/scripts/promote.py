import os
import shutil
import re
import pathlib
from datetime import datetime, date
import argparse
import sys

def get_audit_info(md_path):
    """Parses the audit stamp from Markdown frontmatter/header."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Simple regex to find audit block
    audit_match = re.search(r'audit:\s*\n\s*score:\s*([\d\.]+)\s*\n\s*date:\s*"(.*?)"\s*\n\s*status:\s*"(.*?)"', content, re.MULTILINE)
    if not audit_match:
        return None
    
    return {
        "score": float(audit_match.group(1)),
        "date": audit_match.group(2),
        "status": audit_match.group(3)
    }

def get_source_pdf(md_path):
    """Detects source PDF name from Markdown body."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    pdf_match = re.search(r'^Source PDF:\s*(.*)$', content, re.MULTILINE)
    if pdf_match:
        return pdf_match.group(1).strip()
    return None

def promote(md_path_str, dry_run=False):
    md_path = pathlib.Path(md_path_str)
    if not md_path.exists():
        print(f"ERROR: Markdown file not found: {md_path}")
        return False

    # 1. Validate Audit Stamp
    audit = get_audit_info(md_path)
    if not audit:
        print(f"BLOCKED: No audit stamp found in {md_path.name}. Run md_auditor.py --fix first.")
        return False
    
    if audit["status"] != "PASSED":
        print(f"BLOCKED: audit.status is {audit['status']}. Re-run md_auditor.py --fix first.")
        return False
    
    # Check date freshness (within 7 days)
    try:
        audit_date = datetime.strptime(audit["date"], "%Y-%m-%d").date()
        days_diff = (date.today() - audit_date).days
        if days_diff > 7:
            print(f"BLOCKED: audit.date is {audit['date']} ({days_diff} days ago). Re-audit required.")
            return False
    except ValueError:
        print(f"ERROR: Invalid audit date format: {audit['date']}")
        return False

    # 2. Detect source PDF
    pdf_name = get_source_pdf(md_path)
    pdf_src_path = pathlib.Path("00_Inbox") / pdf_name if pdf_name else None
    
    # 3. Define targets
    target_ingest_dir = pathlib.Path("3-resources/raw_ingest")
    target_sources_dir = pathlib.Path("3-resources/raw_sources")
    temp_folder = md_path.parent # The folder in Converted_Sources
    
    dest_md = target_ingest_dir / md_path.name
    dest_pdf = target_sources_dir / pdf_name if pdf_name else None

    if dry_run:
        print(f"\n--- [DRY RUN] Promotion Plan for {md_path.name} ---")
        print(f"[PLAN] Move MD:  {md_path} -> {dest_md}")
        if pdf_src_path and pdf_src_path.exists():
            print(f"[PLAN] Move PDF: {pdf_src_path} -> {dest_pdf}")
        elif pdf_src_path:
            print(f"[WARN] PDF not found: {pdf_src_path} (Will skip PDF move)")
        if temp_folder.exists() and "Converted_Sources" in str(temp_folder):
            print(f"[PLAN] Delete:   {temp_folder}")
        return True

    # 4. Atomic Promotion
    try:
        # a) Move MD
        target_ingest_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(md_path), str(dest_md))
        print(f"PROMOTED: {dest_md}")

        # b) Move PDF
        if pdf_src_path and pdf_src_path.exists():
            target_sources_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(pdf_src_path), str(dest_pdf))
            print(f"ARCHIVED: {dest_pdf}")
        elif pdf_src_path:
            print(f"WARNING: Source PDF {pdf_name} not found in 00_Inbox. Skipping archive step.")

        # c) Cleanup temp folder
        if temp_folder.exists() and "Converted_Sources" in str(temp_folder):
            shutil.rmtree(str(temp_folder))
            print(f"CLEANED:  {temp_folder}")
        
        return True

    except Exception as e:
        print(f"CRITICAL ERROR during promotion: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Promote audited Markdown and archive original PDF.")
    parser.add_argument("path", help="Path to the audited Markdown file in 00_Inbox/Converted_Sources/")
    parser.add_argument("--dry-run", action="store_true", help="Preview actions without executing")
    
    args = parser.parse_args()
    success = promote(args.path, dry_run=args.dry_run)
    sys.exit(0 if success else 1)
