import os
import argparse
import shutil
import tempfile
from pathlib import Path
from datetime import date
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    AcceleratorOptions,
    AcceleratorDevice,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc.document import PictureItem


def _is_scanned(pdf_path: str) -> bool:
    """Returns True if PDF has no extractable text (scanned)."""
    try:
        import pypdf
        reader = pypdf.PdfReader(pdf_path)
        sample_pages = reader.pages[:3]
        text = "".join(p.extract_text() or "" for p in sample_pages)
        return len(text.strip()) < 100
    except Exception:
        return True


def slice_pdf(pdf_path, start_page, end_page, temp_dir):
    """Slices a PDF and returns the path to the temporary slice."""
    import pypdf
    reader = pypdf.PdfReader(pdf_path)
    writer = pypdf.PdfWriter()
    
    # end_page is exclusive in slicing logic
    actual_end = min(end_page, len(reader.pages))
    for i in range(start_page, actual_end):
        writer.add_page(reader.pages[i])
    
    slice_name = f"temp_slice_{start_page}_{actual_end}.pdf"
    slice_path = os.path.join(temp_dir, slice_name)
    with open(slice_path, "wb") as f:
        writer.write(f)
    return slice_path


def convert_pdf_to_hd_markdown(pdf_path, output_dir, chunk_info=None):
    """
    Converts a PDF (or slice) to High-Fidelity Markdown.
    chunk_info: dict with {'index': int, 'start': int, 'end': int}
    """
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    if chunk_info:
        # Use the original PDF name for the folder, but chunk name for file
        orig_name = chunk_info['orig_name']
        final_output_dir = os.path.join(output_dir, orig_name)
        suffix = f"_CHUNK_{chunk_info['index']:02d}_P{chunk_info['start']+1:03d}-{chunk_info['end']:03d}"
    else:
        final_output_dir = os.path.join(output_dir, base_name)
        suffix = ""

    image_subfolder = "images"
    os.makedirs(os.path.join(final_output_dir, image_subfolder), exist_ok=True)
    
    _ocr = _is_scanned(pdf_path)
    
    # 1. Setup Docling HD Options
    pipeline_options = PdfPipelineOptions()
    pipeline_options.images_scale = 1.0
    pipeline_options.generate_page_images = True
    pipeline_options.generate_picture_images = True
    pipeline_options.do_table_structure = True
    pipeline_options.accelerator_options = AcceleratorOptions(
        num_threads=4,
        device=AcceleratorDevice.CUDA if shutil.which("nvidia-smi") else AcceleratorDevice.CPU,
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
                # Đặt tên ảnh theo prefix chuẩn của sách để nhận dạng trong raw_assets
                if chunk_info:
                    img_prefix = f"{chunk_info['orig_name']}_CHUNK_{chunk_info['index']:02d}_fig_"
                else:
                    img_prefix = f"{base_name}_fig_"
                img_name = f"{img_prefix}{img_count:02d}.png"
                img_rel_path = f"{image_subfolder}/{img_name}"
                img_full_path = os.path.join(final_output_dir, img_rel_path)
                
                item.image.pil_image.save(img_full_path)
                
                # Dùng Obsidian wikilink format để Obsidian resolve tự động
                md_link = f"\n![[{img_name}]]\n"
                md_content = md_content.replace("<!-- image -->", md_link, 1)
                img_count += 1
                
    # 4. Save Final Output
    today = date.today().strftime("%Y-%m-%d")
    final_stem = chunk_info['orig_name'] if chunk_info else base_name
    output_filename = f"RAW_{today}_{final_stem}{suffix}.md"
    output_md_path = os.path.join(final_output_dir, output_filename)
    
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(f"# HD SOURCE: {final_stem}{suffix}\n")
        source_pdf_name = f"{chunk_info['orig_name']}.pdf" if chunk_info else os.path.basename(pdf_path)
        f.write(f"Source PDF: {source_pdf_name}\n")
        f.write(f"Extracted Images: {img_count}\n")
        if chunk_info:
            f.write(f"Chunk Range: Pages {chunk_info['start']+1} to {chunk_info['end']}\n")
        f.write("---\n\n")
        f.write(md_content)
        
    print(f"[OK] Saved: {output_filename} ({img_count} imgs)")
    return output_md_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Docling HD PDF to Markdown Converter")
    parser.add_argument("pdf_path", help="Path to source PDF file")
    parser.add_argument("--output", default="00_Inbox/Converted_Sources", help="Output root directory")
    parser.add_argument("--chunk-size", type=int, default=0, help="Number of pages per chunk (0 = no chunking)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.pdf_path):
        print(f"[ERROR] File not found: {args.pdf_path}")
        sys.exit(1)

    import pypdf
    reader = pypdf.PdfReader(args.pdf_path)
    total_pages = len(reader.pages)
    
    if args.chunk_size > 0 and total_pages > args.chunk_size:
        print(f"[*] Large PDF detected ({total_pages} pages). Starting HD Chunking (Size: {args.chunk_size})...")
        orig_stem = Path(args.pdf_path).stem
        
        with tempfile.TemporaryDirectory() as tmpdir:
            for i in range(0, total_pages, args.chunk_size):
                start = i
                end = min(i + args.chunk_size, total_pages)
                chunk_idx = (i // args.chunk_size) + 1
                
                print(f"\n[Chunk {chunk_idx}] Slicing pages {start+1} to {end}...")
                slice_path = slice_pdf(args.pdf_path, start, end, tmpdir)
                
                chunk_info = {
                    'index': chunk_idx,
                    'start': start,
                    'end': end,
                    'orig_name': orig_stem
                }
                convert_pdf_to_hd_markdown(slice_path, args.output, chunk_info)
    else:
        convert_pdf_to_hd_markdown(args.pdf_path, args.output)
