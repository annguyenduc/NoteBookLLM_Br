from docling.document_converter import DocumentConverter
import os

pdf_path = "00_Inbox/Attention_Paper.pdf"
output_path = "00_Inbox/Attention_Docling.md"

print(f"[*] Starting Docling conversion for {pdf_path}...")
try:
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    md_output = result.document.export_to_markdown()
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_output)
    
    print(f"[+] Successfully converted to {output_path}")
    print(f"[*] Preview (first 500 chars):\n{md_output[:500]}")
except Exception as e:
    print(f"[!] Error during conversion: {e}")
    import traceback
    traceback.print_exc()
