import os
import re
import sys
import pypdf
from typing import List, Tuple

def verify(pdf_path: str, md_path: str) -> bool:
    """
    Compares original PDF vs converted Markdown across 4 metrics.
    Prints a report and returns True if PASS, False otherwise.
    """
    if not os.path.exists(pdf_path):
        print(f"[ERROR] PDF not found: {pdf_path}")
        return False
    if not os.path.exists(md_path):
        print(f"[ERROR] Markdown not found: {md_path}")
        return False

    try:
        # --- PDF Analysis ---
        reader = pypdf.PdfReader(pdf_path)
        pdf_pages = len(reader.pages)
        pdf_chars = 0
        pdf_images = 0
        
        for page in reader.pages:
            pdf_chars += len(page.extract_text() or "")
            pdf_images += len(page.images)
            
        # --- MD Analysis ---
        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        # Metric 1: Page Coverage
        md_sections = len(re.findall(r'^## ', md_content, re.MULTILINE))
        coverage = (md_sections / pdf_pages * 100) if pdf_pages > 0 else 100
        
        status_cov = "✅" if coverage >= 80 else ("⚠️" if coverage >= 50 else "❌")

        # Metric 2: Text Retention
        # Strip frontmatter (everything before first ---\n\n)
        parts = md_content.split("---\n\n", 1)
        stripped_md = parts[1] if len(parts) > 1 else md_content
        md_chars = len(stripped_md)
        
        retention = (md_chars / pdf_chars * 100) if pdf_chars > 0 else 0
        
        if pdf_chars == 0:
            status_ret = "ℹ️"
            ret_label = "SCANNED"
        else:
            status_ret = "✅" if retention >= 70 else ("⚠️" if retention >= 50 else "❌")
            ret_label = f"{retention:.0f}%"

        # Metric 3: Image Coverage
        md_images = len(re.findall(r'!\[.*?\]\(.*?\)', md_content))
        
        is_pymupdf = 'converted_by: "pymupdf4llm"' in md_content
        
        if is_pymupdf:
            status_img = "ℹ️" # By design
        elif pdf_images == 0:
            status_img = "✅"
        elif md_images >= pdf_images * 0.8:
            status_img = "✅"
        elif md_images >= pdf_images * 0.5:
            status_img = "⚠️"
        else:
            status_img = "❌"

        # Metric 4: Gap Detection
        sections = re.split(r'^## ', md_content, flags=re.MULTILINE)
        # Skip the first part (pre-first-header) if it's just meta
        section_lengths = [len(s) for s in sections[1:]]
        
        flagged_titles = []
        if section_lengths:
            avg_len = sum(section_lengths) / len(section_lengths)
            threshold = avg_len * 0.2
            
            # Find titles of short sections
            # re.findall gives titles
            titles = re.findall(r'^## (.*)$', md_content, re.MULTILINE)
            for i, length in enumerate(section_lengths):
                if length < threshold and i < len(titles):
                    flagged_titles.append(titles[i].strip())
        
        gap_list = ", ".join(flagged_titles[:5])
        status_gap = "⚠️" if flagged_titles else "✅"

        # --- Final Report ---
        def safe_print(msg):
            try:
                print(msg)
            except UnicodeEncodeError:
                # Fallback for terminals that don't support UTF-8 (like Windows CMD)
                clean_msg = msg.replace("✅", "[PASS]").replace("⚠️", "[WARN]").replace("❌", "[FAIL]").replace("→", "->").replace("ℹ️", "[INFO]")
                print(clean_msg)

        pdf_basename = os.path.basename(pdf_path)
        safe_print(f"\n  [VERIFY] {pdf_basename}")
        safe_print(f"    Pages:  {pdf_pages} PDF -> {md_sections} sections MD  {status_cov} ({coverage:.1f}%)")
        safe_print(f"    Text:   {pdf_chars:,} chars -> {md_chars:,} chars MD  {status_ret} ({ret_label})")
        safe_print(f"    Images: {pdf_images} PDF -> {md_images} MD  {status_img}{' (By Design)' if is_pymupdf else ''}")
        safe_print(f"    Gaps:   {gap_list or 'None'} {status_gap if flagged_titles else ''}")

        # Result logic
        # Exclude status_img from checks if it's PyMuPDF
        img_check_status = "✅" if is_pymupdf else status_img
        
        all_ok = all(s == "✅" for s in [status_cov, status_ret if pdf_chars > 0 else "✅", img_check_status]) and not flagged_titles
        any_fail = any(s == "❌" for s in [status_cov, status_ret, status_img])
        
        if any_fail:
            res = "FAIL"
        elif all_ok:
            res = "PASS"
        else:
            res = "WARN"
            
        safe_print(f"\n  RESULT: {res}")
        
        if res != "PASS":
            reasons = []
            if status_cov == "❌": reasons.append("Critical page loss")
            if status_ret == "❌": reasons.append("Critical text loss")
            if status_img == "❌": reasons.append("Critical image loss")
            if flagged_titles: reasons.append(f"Suspiciously short sections detected ({len(flagged_titles)})")
            if reasons:
                safe_print(f"  Reason: {'; '.join(reasons)}")
        
        return {
            "result": res,
            "gaps": flagged_titles[:5]
        }

    except Exception as e:
        print(f"[ERROR] Verification failed: {e}")
        return {"result": "ERROR", "gaps": []}

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python verify_convert.py <pdf_path> <md_path>")
        sys.exit(1)
    
    # Optional: Force UTF-8 for stdout if supported
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except:
            pass

    success = verify(sys.argv[1], sys.argv[2])
    sys.exit(0 if success else 0) 
# User didn't specify exit code for FAIL, but usually 1 is better. 
    # However, for scripts integrated into pipelines, sometimes you want to continue.
    # Re-reading: "exit with code 1" only mentioned if pypdf fails to read PDF.
