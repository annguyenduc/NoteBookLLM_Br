import os
import sys
import pypdf
import datetime
import pathlib
import importlib.util
import argparse
import logging
import re

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def get_pdf_signals(pdf_path):
    """Returns sparse_ratio, avg_images (sample), and total_images (full)."""
    try:
        reader = pypdf.PdfReader(pdf_path)
        num_pages = len(reader.pages)
        sample_size = min(20, num_pages)
        sample_pages = reader.pages[:sample_size]
        
        sparse_count = 0
        sample_images = 0
        
        # Signal 1 & 2: Sample analysis
        for page in sample_pages:
            text = page.extract_text() or ""
            if len(text.strip()) < 100:
                sparse_count += 1
            sample_images += len(page.images)
            
        sparse_ratio = sparse_count / sample_size if sample_size > 0 else 0
        avg_images = sample_images / sample_size if sample_size > 0 else 0
        
        # Signal 3: Global image count (important for large books)
        total_images = 0
        for page in reader.pages:
            total_images += len(page.images)
        
        return sparse_ratio, avg_images, num_pages, total_images
    except Exception as e:
        logging.error(f"Error analyzing PDF: {e}")
        return 1.0, 0, 0, 0 # Fallback to docling (safer)

def pymupdf_convert(pdf_path, output_dir):
    """Converts text-based PDF using pymupdf4llm."""
    import pymupdf4llm
    
    pdf_path_obj = pathlib.Path(pdf_path)
    pdf_stem = pdf_path_obj.stem
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    target_dir = pathlib.Path(output_dir) / pdf_stem
    target_dir.mkdir(parents=True, exist_ok=True)
    
    output_filename = f"RAW_{today}_{pdf_stem}.md"
    output_path = target_dir / output_filename
    
    md_content = pymupdf4llm.to_markdown(str(pdf_path))
    
    frontmatter = f"""---
source_pdf: "{pdf_path_obj.name}"
converted_by: "pymupdf4llm"
converted_date: "{today}"
pdf_mode: "TEXT"
---

"""
    final_content = frontmatter + f"Source PDF: {pdf_path_obj.name}\n\n" + md_content
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_content)
        
    return str(output_path)

def docling_convert(pdf_path, output_dir):
    """Converts complex PDF using hd_converter (docling)."""
    v_script = pathlib.Path(__file__).parent / "hd_converter.py"
    if not v_script.exists():
        logging.warning("hd_converter.py not found. Falling back to pymupdf.")
        return pymupdf_convert(pdf_path, output_dir)
        
    spec = importlib.util.spec_from_file_location("hd_converter", v_script)
    hd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hd)
    
    return hd.convert_pdf_to_hd_markdown(pdf_path, output_dir)

def route_and_convert(pdf_path, output_dir, dry_run=False):
    """Detects mode and routes to the appropriate engine."""
    sparse_ratio, avg_images, num_pages, total_images = get_pdf_signals(pdf_path)
    
    # Logic Decision
    if sparse_ratio > 0.6:
        mode = "SCANNED"
        reason = f"High sparse ratio ({sparse_ratio:.0%})"
    elif avg_images > 2.0:
        mode = "CHART-HEAVY"
        reason = f"High image density in sample ({avg_images:.1f} imgs/page)"
    elif total_images > 50:
        mode = "CHART-HEAVY"
        reason = f"High total image count ({total_images} images)"
    else:
        mode = "TEXT"
        reason = "Clean text-based PDF with few images"
        
    pdf_basename = os.path.basename(pdf_path)
    engine = "docling" if mode in ["SCANNED", "CHART-HEAVY"] else "pymupdf4llm"
    
    print(f"\n[ROUTER] Decision for {pdf_basename}:")
    print(f"  - Pages: {num_pages}")
    print(f"  - Signals: sparse={sparse_ratio:.0%}, sample_avg_imgs={avg_images:.1f}, total_imgs={total_images}")
    print(f"  - Mode: {mode}")
    print(f"  - Reason: {reason}")
    print(f"  - Engine: {engine}")

    if dry_run:
        print("  [DRY-RUN] Skipping execution.")
        return None
    
    # Handle missing docling
    try:
        if engine == "docling":
            import docling
    except ImportError:
        logging.warning("[ROUTER] docling not available. Falling back to pymupdf4llm.")
        engine = "pymupdf4llm"
    
    if engine == "docling":
        output_path = docling_convert(pdf_path, output_dir)
    else:
        output_path = pymupdf_convert(pdf_path, output_dir)
        
    print(f"  [OK] Saved to: {output_path}")
    
    # Auto-verify
    verify_script = pathlib.Path(__file__).parent / "verify_convert.py"
    if verify_script.exists():
        spec = importlib.util.spec_from_file_location("verify_convert", verify_script)
        vc = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(vc)
        vc.verify(pdf_path, output_path)
        
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto-routing PDF Converter")
    parser.add_argument("pdf_path", help="Path to PDF file")
    parser.add_argument("--output", default="00_Inbox/Converted_Sources", help="Output root directory")
    parser.add_argument("--dry-run", action="store_true", help="Show decision without converting")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.pdf_path):
        logging.error(f"File not found: {args.pdf_path}")
        sys.exit(1)
        
    route_and_convert(args.pdf_path, args.output, dry_run=args.dry_run)
