import sys
import os
import re
from libs.core.llm_client import call_pedagogical_agent

# Đảm bảo output luôn là utf-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.append(os.getcwd())

def distill_volume(volume_id):
    path = f"brain/raw/optimized_part_1_{volume_id}.md"
    if not os.path.exists(path):
        print(f"File {path} không tồn tại.")
        return

    print(f"--- 🛠️ CHƯNG CẤT NGHIÊM NGẶT VOLUME {volume_id} (IoT Focus) ---")
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into chunks of ~10k tokens (or ~30k chars) to fit LLM window effectively
    chunk_size = 30000
    chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]

    for idx, chunk in enumerate(chunks):
        print(f"Processing Chunk {idx+1}/{len(chunks)}...")
        
        prompt = [
            {"role": "system", "content": f"""Bạn là @scout chuyên trách chưng cất tri thức kỹ thuật.
NGUỒN CUNG CẤP: Volume {volume_id}
NHIỆM VỤ: Trích xuất các sự kiện (Facts) về IoT, Arduino, YoloBit, Robotics, AI.

QUY TẮC NGHIÊM NGẶT (LOM v4.1):
1. PROVENANCE: Mỗi Fact phải ghi rõ trích dẫn dòng hoặc đoạn. Ví dụ: (v01 - Section: Arduino Setup).
2. CITATION: Sử dụng tag từ MASTER_SOURCE_INDEX nếu biết. Nếu không, dùng tag [v{volume_id}].
3. NO HALLUCINATION: Nếu thông tin không có trong text nhưng bạn bổ sung từ kiến thức cá nhân, BẮT BUỘC gắn nhãn [Unverified_Source].
4. FORMAT: 
- Fact: [CONV] [Nội dung ngắn gọn, súc tích]
- Source: [Vị trí trong file raw]
- Tag: [Tag trích dẫn]
--------------------------------------------------"""},
            {"role": "user", "content": f"DỮ LIỆU RAW:\n{chunk}"}
        ]
        
        # We use a high-capacity model for distillation
        atomic_out, model = call_pedagogical_agent("scout", prompt)
        
        output_file = f"brain/distilled/atomic/CONV_atoms_{volume_id}_{idx+1}.md"
        with open(output_file, "w", encoding="utf-8") as out_f:
            out_f.write(atomic_out)
        
        print(f"  > Saved to {output_file} (Model: {model})")

if __name__ == "__main__":
    # Khoảng Volume từ 01 đến 31
    for i in range(1, 32):
        volume_id = f"v{i:02d}"
        distill_volume(volume_id)

    # Merge all distilled files
    print("--- 🔗 MERGING ALL ATOMS ---")
    merged_content = ""
    output_dir = "brain/distilled/atomic/"
    files = sorted([f for f in os.listdir(output_dir) if f.startswith("CONV_atoms_")])
    
    for filename in files:
        with open(os.path.join(output_dir, filename), "r", encoding="utf-8") as f:
            merged_content += f.read() + "\n\n"
            
    with open("brain/distilled/MASTER_CONV_ATOMS.md", "w", encoding="utf-8") as f:
        f.write(merged_content)
    print("--- ✅ MERGE COMPLETE: brain/distilled/MASTER_CONV_ATOMS.md ---")
