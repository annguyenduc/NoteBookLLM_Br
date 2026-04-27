import os
import sys
import zipfile
from docx import Document
from lxml import etree

# Đảm bảo output luôn là utf-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def extract_media(docx_path, output_media_dir):
    """Trích xuất hình ảnh từ file .docx (ZIP structure)."""
    if not os.path.exists(output_media_dir):
        os.makedirs(output_media_dir)
    
    media_map = {}
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.startswith('word/media/'):
                filename = os.path.basename(file)
                # Để tránh trùng lặp giữa các file Word, thêm prefix tên file docx
                safe_name = f"{os.path.basename(docx_path).replace(' ', '_')}_{filename}"
                target_path = os.path.join(output_media_dir, safe_name)
                with open(target_path, 'wb') as f:
                    f.write(zip_ref.read(file))
                media_map[filename] = target_path
    return media_map

def convert_docx_to_md(docx_path, output_dir):
    """Chuyển đổi Word sang Markdown kèm trích xuất hình ảnh."""
    doc_filename = os.path.basename(docx_path)
    base_name = os.path.splitext(doc_filename)[0]
    
    # Tạo thư mục assets cho file này
    assets_dir = os.path.join(output_dir, "assets")
    media_map = extract_media(docx_path, assets_dir)
    
    doc = Document(docx_path)
    md_content = f"# SOURCE: {doc_filename}\n\n"
    
    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            md_content += text + "\n\n"
        
        # Kiểm tra xem có inline shapes (hình ảnh) không
        # Lưu ý: python-docx chưa hỗ trợ tốt việc xác định vị trí chính xác của ảnh trong text
        # nên chúng ta sẽ liệt kê các ảnh tìm thấy trong paragraph nếu có logic phức tạp hơn
        pass

    # Phụ lục hình ảnh (do vị trí inline khó xác định chính xác bằng python-docx thuần)
    if media_map:
        md_content += "## 🖼️ MEDIA ASSETS\n"
        for original, local in media_map.items():
            rel_path = os.path.relpath(local, output_dir)
            md_content += f"![{original}]({rel_path})\n\n"

    output_path = os.path.join(output_dir, f"{base_name}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    
    return output_path

def process_lms_folder(input_root, output_root):
    """Duyệt và xử lý toàn bộ folder LMS."""
    target_keywords = ["Arduino", "IOT", "YoloBit", "Halocode"]
    
    for root, dirs, files in os.walk(input_root):
        for file in files:
            if file.endswith(".docx") and not file.startswith("~$"):
                # Lọc theo từ khóa trong tên file hoặc đường dẫn thư mục
                is_target = any(kw.lower() in file.lower() for kw in target_keywords) or \
                            any(kw.lower() in root.lower() for kw in target_keywords)
                
                if is_target:
                    full_path = os.path.join(root, file)
                    print(f"Processing: {file}...")
                    try:
                        out_file = convert_docx_to_md(full_path, output_root)
                        print(f"  > Exported to: {out_file}")
                    except Exception as e:
                        print(f"  [ERROR] {file}: {e}")

if __name__ == "__main__":
    LMS_ROOT = "brain/raw/Tổng hợp đề kiểm tra LMS"
    EXPORT_DIR = "brain/raw/lms_multi_media_dump"
    
    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)
        
    process_lms_folder(LMS_ROOT, EXPORT_DIR)
