import os
import re
from pathlib import Path

def split_into_chunks(input_file, output_dir, max_chars_per_chunk=30000):
    """
    Đọc file text lịch sử hội thoại và tách ra thành các file .md nhỏ.
    :param max_chars_per_chunk: Kích thước ký tự tối đa cho mỗi file chunk (30k chars ~ 5k-8k tokens).
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    # Xóa các file chunk cũ nếu có
    for f in out_path.glob("chunk_*_*.md"):
        f.unlink()

    print(f"📦 Đang đọc file gốc: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Cắt theo separator
    # Vì file có dấu bằng (==================================================) để ngăn cách
    blocks = re.split(r'={20,}', content)
    
    chunk_index = 1
    current_chunk_content = ""
    total_conversations_saved = 0
    valid_blocks = 0
    
    for block in blocks:
        block = block.strip()
        if len(block) < 50: 
            continue # Bỏ qua block rác
            
        valid_blocks += 1
        current_chunk_content += "==================================================\n" + block + "\n\n"
        
        # Nếu block hiện tại đã đủ lớn, chốt lại thành 1 file chunk
        if len(current_chunk_content) >= max_chars_per_chunk:
            file_name = out_path / f"chunk_gemini_{chunk_index:03d}.md"
            with open(file_name, "w", encoding="utf-8") as out:
                out.write(f"# Khối hội thoại - Phần {chunk_index}\n\n")
                out.write(current_chunk_content)
            
            total_conversations_saved += 1
            chunk_index += 1
            current_chunk_content = ""
            
    # Ghi phần thừa còn lại (nếu có)
    if len(current_chunk_content.strip()) > 0:
        file_name = out_path / f"chunk_gemini_{chunk_index:03d}.md"
        with open(file_name, "w", encoding="utf-8") as out:
            out.write(f"# Khối hội thoại - Phần {chunk_index}\n\n")
            out.write(current_chunk_content)
        total_conversations_saved += 1

    print(f"✅ Quá trình phân chia hoàn tất.")
    print(f"📊 Thống kê:")
    print(f"  - Số block hội thoại quét được: {valid_blocks}")
    print(f"  - Số lượng file chunk đã tạo ra: {total_conversations_saved}")
    print(f"  - Lưu tại thư mục: {output_dir}")

if __name__ == "__main__":
    # Nằm trong input/gemini_sync/
    base_dir = Path(__file__).resolve().parent
    input_file_path = base_dir / "2. MyActivity_Conversation.txt"
    batches_dir = base_dir / "batches_gemini"
    
    if input_file_path.exists():
        split_into_chunks(input_file_path, batches_dir)
    else:
        print(f"❌ Lỗi: Không tìm thấy {input_file_path}")
