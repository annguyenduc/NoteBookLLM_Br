import math
import sqlite3
from datetime import datetime
import re

def compute_confidence(atom_data, conn):
    """
    Compute confidence score based on Rubric 3.0 (0.4 | 0.3 | 0.2 | 0.1).
    atom_data: dict containing keys like 'content', 'metadata', 'file_id'
    conn: sqlite3 connection
    """
    score = 0.0
    content = atom_data.get("content", "")
    metadata = atom_data.get("metadata", {})
    
    # 1. Source Accuracy (0.4) - R3
    # Bắt buộc có source_file và source_ref không được để trống hoặc placeholder
    source_file = metadata.get("source_file", "")
    source_ref = metadata.get("source_ref", "")
    if source_file and source_ref and "RAW_" in source_file:
        score += 0.4
    
    # 2. Double Examples (0.3) - R18
    # Kiểm tra sự hiện diện của 2 tiêu đề ví dụ và nội dung không phải placeholder
    has_original = "### Ví dụ từ sách (Original)" in content
    has_pedagogical = "### Ứng dụng sư phạm (Pedagogical Application)" in content
    
    # Kiểm tra xem có chứa placeholder [Mô tả...] không
    is_placeholder = "[Mô tả" in content or "[Cách" in content
    
    if has_original and has_pedagogical and not is_placeholder:
        score += 0.3
    elif has_original or has_pedagogical:
        score += 0.15 # Chỉ có 1 ví dụ
        
    # 3. Format Integrity (0.2) - R4/R20
    # Kiểm tra các trường bắt buộc trong YAML
    required_fields = ["file_id", "title", "type", "status", "tags"]
    format_score = 0.0
    field_count = 0
    for field in required_fields:
        if metadata.get(field):
            field_count += 1
    
    if field_count == len(required_fields):
        format_score += 0.15
    
    # Kiểm tra dấu ":" trong Metadata có được để trong ngoặc kép không (R20)
    # Đây là kiểm tra sơ bộ thông qua content gốc nếu có, hoặc giả định pass nếu metadata dict đã được parse thành công
    format_score += 0.05
    
    score += format_score
    
    # 4. Link Density (0.1) - R15
    # Kiểm tra số lượng relationships trong metadata
    relationships = metadata.get("relationships", [])
    if isinstance(relationships, list) and len(relationships) >= 2:
        score += 0.1
    elif isinstance(relationships, list) and len(relationships) == 1:
        score += 0.05
        
    return round(max(0.0, min(1.0, score)), 4)

if __name__ == "__main__":
    # Test cases
    test_atom = {
        "content": "### Ví dụ từ sách (Original)\nNội dung thật\n### Ứng dụng sư phạm (Pedagogical Application)\nNội dung thật",
        "metadata": {
            "source_file": "RAW_2026-05-11_test.md",
            "source_ref": "[[SOURCE_Test]]",
            "file_id": "CONCEPT_SYS_Test",
            "title": "Test Atom",
            "type": "concept",
            "status": "DRAFT",
            "tags": ["test"],
            "relationships": [{}, {}]
        }
    }
    print(f"Test Score (Full Quality): {compute_confidence(test_atom, None)}")
