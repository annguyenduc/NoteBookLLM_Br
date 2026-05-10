import os
import argparse
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    AcceleratorOptions,
    AcceleratorDevice,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc.document import PictureItem


def _is_scanned(pdf_path: str) -> bool:
    """Returns True if PDF has no extractable text (scanned).
    Uses pypdf instead of pdftotext for Windows compatibility."""
    try:
        import pypdf
        reader = pypdf.PdfReader(pdf_path)
        sample_pages = reader.pages[:3]
        text = "".join(p.extract_text() or "" for p in sample_pages)
        return len(text.strip()) < 100
    except Exception:
        return True  # fallback: assume scanned if detection fails



def convert_pdf_to_hd_markdown(pdf_path, output_dir):
    """
    Converts a PDF to High-Fidelity Markdown with extracted and linked images.
    """
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    final_output_dir = os.path.join(output_dir, base_name)
    image_subfolder = "images"
    
    os.makedirs(os.path.join(final_output_dir, image_subfolder), exist_ok=True)
    
    _ocr = _is_scanned(pdf_path)
    print(f"[*] Processing: {pdf_path}")
    print(f"    OCR: {'ON (scanned PDF)' if _ocr else 'OFF (text PDF)'}")
    print(f"    Accelerator: CUDA")
    
    # 1. Setup Docling HD Options
    pipeline_options = PdfPipelineOptions()
    pipeline_options.images_scale = 1.0
    pipeline_options.generate_page_images = True
    pipeline_options.generate_picture_images = True
    pipeline_options.do_table_structure = True
    pipeline_options.accelerator_options = AcceleratorOptions(
        num_threads=4,
        device=AcceleratorDevice.CUDA,
    )
    pipeline_options.do_ocr = _ocr

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )
    
    # 2. Convert
    result = converter.convert(pdf_path)
    doc = result.document
    md_content = doc.export_to_markdown()
    
    # 3. Extract Pictures and Update MD
    img_count = 0
    for item, level in doc.iterate_items():
        if isinstance(item, PictureItem):
            if item.image:
                img_name = f"chart_{img_count}.png"
                img_rel_path = f"{image_subfolder}/{img_name}"
                img_full_path = os.path.join(final_output_dir, img_rel_path)
                
                item.image.pil_image.save(img_full_path)
                
                # Replace placeholder with Markdown link
                md_link = f"\n![Biểu đồ {img_count}]({img_rel_path})\n"
                md_content = md_content.replace("<!-- image -->", md_link, 1)
                img_count += 1
                
    # 4. Save Final Output
    from datetime import date
    from pathlib import Path
    today = date.today().strftime("%Y-%m-%d")
    stem = Path(pdf_path).stem
    output_filename = f"RAW_{today}_{stem}.md"
    output_md_path = os.path.join(final_output_dir, output_filename)
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(f"# HD SOURCE: {base_name}\n")
        f.write(f"Source PDF: {os.path.basename(pdf_path)}\n")
        f.write(f"Extracted Charts: {img_count}\n")
        f.write("---\n\n")
        f.write(md_content)
        
    print(f"[OK] Saved to: {output_md_path} (Extracted {img_count} images)")
    
    # Auto-verify after conversion
    import importlib.util, pathlib
    _verify_script = pathlib.Path(__file__).parent / "verify_convert.py"
    if _verify_script.exists():
        spec = importlib.util.spec_from_file_location("verify_convert", _verify_script)
        vc = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(vc)
        vc.verify(pdf_path, output_md_path)

    return output_md_path

if __name__ == "__main__":
    # NOTE: For automatic PDF type detection, use pdf_router.py instead.
    # hd_converter.py always uses Docling (for chart-heavy/scanned PDFs).
    parser = argparse.ArgumentParser(description="Docling HD PDF to Markdown Converter")
    parser.add_argument("pdf_path", help="Path to source PDF file")
    parser.add_argument("--output", default="00_Inbox/Converted_Sources", help="Output root directory")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.pdf_path):
        print(f"[ERROR] File not found: {args.pdf_path}")
    else:
        convert_pdf_to_hd_markdown(args.pdf_path, args.output)
