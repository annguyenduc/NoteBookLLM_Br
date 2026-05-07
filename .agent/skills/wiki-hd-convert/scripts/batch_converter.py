import os
import argparse
import fitz  # PyMuPDF
from tqdm import tqdm
import logging
import pathlib
import shutil
import torch
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions, AcceleratorOptions, AcceleratorDevice
from docling.datamodel.base_models import InputFormat
from docling_core.types.doc.document import PictureItem

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class StrategicConverter:
    def __init__(self, output_root):
        self.output_root = pathlib.Path(output_root)

    def audit_pdf(self, pdf_path):
        """Tầng 1: Phân tích đặc tính PDF (Sampling 3 trang) để chọn Strategy."""
        pdf_path = pathlib.Path(pdf_path)
        size_mb = pdf_path.stat().st_size / (1024 * 1024)
        
        try:
            doc = fitz.open(pdf_path)
            total_pages = len(doc)
            
            # Smart Sampling: Đầu, Giữa, Cuối
            sample_indices = [0, total_pages // 2, total_pages - 1] if total_pages > 2 else range(total_pages)
            total_chars = 0
            total_images = 0
            
            for i in sample_indices:
                page = doc[i]
                total_chars += len(page.get_text())
                total_images += len(page.get_images())
            
            doc.close()
            
            # Decision Logic
            chars_per_page = total_chars / len(sample_indices)
            images_per_page = total_images / len(sample_indices)
            
            if chars_per_page > 200:
                ocr_needed = False
                reason = "TEXT-BASED"
            elif images_per_page > 0.5:
                ocr_needed = True
                reason = "IMAGE-BASED"
            else:
                ocr_needed = True
                reason = "AMBIGUOUS"
                
        except Exception as e:
            logging.error(f"Failed to audit {pdf_path.name}: {e}")
            return None

        strategy = self._assign_strategy(size_mb, chars_per_page, total_pages)
        return {
            "file": pdf_path.name,
            "path": pdf_path,
            "size_mb": round(size_mb, 1),
            "pages": total_pages,
            "ocr_needed": ocr_needed,
            "reason": reason,
            "chars_per_page": round(chars_per_page),
            "strategy": strategy
        }

    def _assign_strategy(self, size_mb, chars_per_page, pages):
        if size_mb > 50 or pages > 100:
            return "CHUNK_MEDIUM"
        else:
            return "DIRECT"

    def make_converter(self, do_ocr=False):
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_ocr = do_ocr
        pipeline_options.do_table_structure = True
        pipeline_options.images_scale = 2.0
        pipeline_options.generate_picture_images = True
        
        if torch.cuda.is_available():
            logging.info("[GPU] CUDA detected. Enabling hardware acceleration.")
            pipeline_options.accelerator_options = AcceleratorOptions(
                num_threads=4,
                device=AcceleratorDevice.CUDA
            )
        else:
            logging.info("[CPU] CUDA not found. Running on CPU mode.")
        
        return DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
            }
        )

    def convert_chunk(self, pdf_path, start_page, end_page, do_ocr, final_output_dir, temp_dir, converter):
        """Chuyển đổi một phần của PDF và trích xuất ảnh."""
        base_name = pdf_path.stem
        chunk_pdf_path = temp_dir / f"chunk_{start_page}_{end_page}.pdf"
        
        # 1. Trích xuất trang thành file tạm
        src_doc = fitz.open(pdf_path)
        chunk_doc = fitz.open()
        chunk_doc.insert_pdf(src_doc, from_page=start_page, to_page=end_page-1)
        chunk_doc.save(chunk_pdf_path)
        chunk_doc.close()
        src_doc.close()

        # 2. Chuyển đổi Docling (Dùng converter inject vào)
        result = converter.convert(chunk_pdf_path)
        doc = result.document
        md_content = doc.export_to_markdown()
        
        # 3. Trích xuất ảnh (Đảm bảo tên không trùng)
        image_dir = final_output_dir / "images"
        image_dir.mkdir(exist_ok=True)
        
        img_count = 0
        for item, level in doc.iterate_items():
            if isinstance(item, PictureItem):
                if item.image:
                    img_name = f"fig_p{start_page}_n{img_count}.png"
                    img_path = image_dir / img_name
                    item.image.pil_image.save(img_path)
                    
                    md_link = f"\n![Biểu đồ {start_page}_{img_count}](images/{img_name})\n"
                    md_content = md_content.replace("<!-- image -->", md_link, 1)
                    img_count += 1
        
        return md_content

    def process_file(self, info, dry_run=True):
        if dry_run:
            return
            
        pdf_path = info['path']
        strategy = info['strategy']
        do_ocr = info['ocr_needed']
        reason = info['reason']
        base_name = pdf_path.stem
        final_output_dir = self.output_root / base_name
        final_output_dir.mkdir(parents=True, exist_ok=True)
        
        chunk_size = 10 
        total_pages = info['pages']
        
        logging.info(f"[*] Starting {strategy} conversion for {base_name}...")
        
        # Khởi tạo Converter MỘT LẦN DUY NHẤT cho toàn file
        logging.info(f"[*] Initializing {reason} converter (OCR={'ON' if do_ocr else 'OFF'})...")
        converter = self.make_converter(do_ocr)
        
        temp_dir = final_output_dir / "temp_chunks"
        temp_dir.mkdir(parents=True, exist_ok=True)
        
        full_md = []
        ranges = range(0, total_pages, chunk_size)
        
        for start in tqdm(ranges, desc=f"Converting {base_name}"):
            end = min(start + chunk_size, total_pages)
            chunk_md = self.convert_chunk(pdf_path, start, end, do_ocr, final_output_dir, temp_dir, converter)
            if chunk_md:
                full_md.append(chunk_md)
            
        final_md_path = final_output_dir / f"{base_name}_HD.md"
        with open(final_md_path, "w", encoding="utf-8") as f:
            f.write(f"# HD SOURCE: {base_name}\n")
            f.write(f"Source PDF: {pdf_path.name}\n")
            f.write(f"Classify: {reason} ({info['chars_per_page']} chars/page)\n")
            f.write(f"OCR: {'ON' if do_ocr else 'OFF'}\n")
            f.write(f"Strategy: {strategy}\n")
            f.write("---\n\n")
            f.write("\n\n---\n\n".join(full_md))
            
        logging.info(f"[OK] Completed: {final_md_path}")
        
        try:
            for f in temp_dir.glob("*.pdf"):
                f.unlink()
            temp_dir.rmdir()
        except Exception as e:
            logging.warning(f"Failed to cleanup temp dir: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Strategic Batch PDF Converter")
    parser.add_argument("--source", default="3-resources/raw_sources", help="Source directory")
    parser.add_argument("--output", default="00_Inbox/Converted_Sources", help="Output root")
    parser.add_argument("--dry-run", action="store_true", help="Audit only, no conversion")
    parser.add_argument("--filter", help="Filter by filename (e.g. THINK)")
    
    args = parser.parse_args()
    base_dir = pathlib.Path("d:/NoteBookLLM_Br")
    source_path = base_dir / args.source
    output_path = base_dir / args.output
    
    sc = StrategicConverter(output_path)
    
    files = [f for f in source_path.glob("*.pdf")]
    if args.filter:
        files = [f for f in files if args.filter in f.name]
        
    audit_results = []
    print(f"\n--- PDF Audit Report ({len(files)} files) ---")
    print(f"{'FILE':<40} | {'CLASSIFY':<12} | {'OCR':<5} | {'SIZE':<8} | {'PAGES':<5}")
    print("-" * 85)
    
    for f in files:
        info = sc.audit_pdf(f)
        if info:
            audit_results.append(info)
            print(f"{info['file'][:40]:<40} | {info['reason']:<12} | {'ON' if info['ocr_needed'] else 'OFF':<5} | {info['size_mb']:>5} MB | {info['pages']:>5}")

    if not args.dry_run:
        print(f"\n--- Executing Strategic Conversion ---")
        for info in audit_results:
            sc.process_file(info, dry_run=False)
    else:
        print("\n[NOTE] Dry-run mode: No files were converted.")
