import os
import argparse
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc.document import PictureItem

def convert_pdf_to_hd_markdown(pdf_path, output_dir):
    """
    Converts a PDF to High-Fidelity Markdown with extracted and linked images.
    """
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    final_output_dir = os.path.join(output_dir, base_name)
    image_subfolder = "images"
    
    os.makedirs(os.path.join(final_output_dir, image_subfolder), exist_ok=True)
    
    print(f"[*] Processing: {pdf_path}")
    
    # 1. Setup Docling HD Options
    pipeline_options = PdfPipelineOptions()
    pipeline_options.images_scale = 2.0
    pipeline_options.generate_page_images = True
    pipeline_options.generate_picture_images = True
    pipeline_options.do_table_structure = True
    pipeline_options.do_ocr = True

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
    output_md_path = os.path.join(final_output_dir, f"{base_name}_HD.md")
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(f"# HD SOURCE: {base_name}\n")
        f.write(f"Source PDF: {os.path.basename(pdf_path)}\n")
        f.write(f"Extracted Charts: {img_count}\n")
        f.write("---\n\n")
        f.write(md_content)
        
    print(f"[OK] Saved to: {output_md_path} (Extracted {img_count} images)")
    return output_md_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Docling HD PDF to Markdown Converter")
    parser.add_argument("pdf_path", help="Path to source PDF file")
    parser.add_argument("--output", default="00_Inbox/Converted_Sources", help="Output root directory")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.pdf_path):
        print(f"[ERROR] File not found: {args.pdf_path}")
    else:
        convert_pdf_to_hd_markdown(args.pdf_path, args.output)
