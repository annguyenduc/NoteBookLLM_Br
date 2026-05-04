---
name: Ingesting-Wiki
description: Nạp nguồn tri thức mới vào Wiki. Dùng khi user thêm file vào raw/, nói 'ingest cái này', 'xử lý nguồn này', hoặc muốn tích hợp tài liệu mới vào knowledge base.
---

# Ingesting Wiki (V3.1)

## Overview
Quy trình nạp tri thức có cấu trúc, đảm bảo tính nguyên tử và nguồn gốc tuyệt đối (Traceability). Hệ thống sử dụng Magika để định danh nội dung và Docling/MarkItDown để parse dữ liệu.

## Workflow: The Two Gates

### Gate -1: Content-Aware Routing
- **Tool**: `magika_router.py`
- **Action**: Xác định loại nội dung thực tế (không chỉ dựa vào extension).
- **Outputs**: MIME-type và Parser đề xuất.

### Gate 0: Atomic Ingestion
- **Tool**: `ingest.py`
- **Action**: 
    1. Trích xuất nội dung văn bản.
    2. Tính toán Hash (SHA-256) của file gốc.
    3. Kiểm tra trùng lặp trong `wiki_brain.db`.
    4. Tạo bản ghi PENDING trong `review_queue`.
    5. Tạo Atom DRAFT với: `confidence`, `learning_source`, `status='DRAFT'`.

## Constraints (Hard Stop)
- **R1 - Raw is IMMUTABLE**: Tuyệt đối không ghi đè vào `3-resources/raw/`.
- **R8 - Human Gate**: Mọi Atom mới đều ở trạng thái `DRAFT`. Không tự ý set `SYNTHESIZED`.
- **R3 - Source Tracing**: Mọi Atom phải có link dẫn về file trong `raw/`.

## Usage
```powershell
# Định tuyến file
python .agent/skills/wiki-ingest/scripts/magika_router.py "path/to/file"

# Nạp file vào hệ thống
python .agent/skills/wiki-ingest/scripts/ingest.py "path/to/file"
```

## Success Metrics
- **Duplicate Detection**: 100% (không nạp file trùng hash).
- **MIME Accuracy**: >95% nhờ Magika.
- **Traceability**: 100% Atom có nguồn dẫn hợp lệ.
