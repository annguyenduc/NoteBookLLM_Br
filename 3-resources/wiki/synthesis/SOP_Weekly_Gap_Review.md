# SOP: Weekly Gap Review Workflow (Wiki 2.0)

## 1. Mục đích
Quy trình này hướng dẫn cách xử lý các "khoảng trống tri thức" (knowledge gaps) được phát hiện bởi Local LLM (Gemma3) trong quá trình ingestion. Mục tiêu là đảm bảo không bỏ sót tri thức quan trọng nhưng vẫn giữ cho Wiki sạch sẽ, không bị "rác" metadata.

## 2. Thông tin chung
- **Chu kỳ:** Hàng tuần (Weekly).
- **Vị trí dữ liệu đầu vào:** `00_Inbox/gap_candidates/`.
- **Vai trò thực hiện:** `@librarian` (Agent) + `@human` (User).

## 3. Các bước thực hiện

### Bước 1: Tổng hợp danh sách (Scout Summary)
User yêu cầu Agent: `"Review các gap candidates tuần này"`.
Agent thực hiện:
1. Quét toàn bộ file `.md` trong `00_Inbox/gap_candidates/`.
2. Phân loại theo nguồn (Source) và loại tri thức (Concept/Entity/Source).
3. Hiển thị bảng tóm tắt kèm mô tả ngắn.

### Bước 2: Phê duyệt (Human-in-the-loop)
User phản hồi dựa trên danh sách:
- **KEEP [Tên]**: Giữ lại và thăng cấp thành Atom.
- **REJECT [Tên]**: Loại bỏ vì là noise (metadata rác, thông tin không quan trọng).
- **BATCH KEEP ALL**: Thăng cấp toàn bộ (thận trọng).

### Bước 3: Thăng cấp & Lưu trữ (Promotion)
Với các mục được **KEEP**, Agent thực hiện:
1. Check trùng lặp: Kiểm tra xem concept/entity đã tồn tại trong `3-resources/wiki/` chưa.
2. Tạo file Atom nháp: Lưu vào `3-resources/wiki/review_queue/` với `status: DRAFT`.
3. Gán Metadata:
   - `learning_source: true`
   - `source_file: [Link tới file gốc]`
   - `created: [Ngày hiện tại]`

### Bước 4: Dọn dẹp (Cleanup)
Agent xóa toàn bộ các file trong `00_Inbox/gap_candidates/` đã xử lý để chuẩn bị cho chu kỳ ingest tiếp theo.

## 4. Các lệnh hỗ trợ (Dự kiến)
- `/gap-summary`: Hiển thị bảng candidates hiện tại.
- `/gap-promote [name]`: Thăng cấp nhanh một candidate.
- `/gap-cleanup`: Xóa sạch inbox gap candidates.

---
*Phiên bản 1.0 — Thiết lập bởi @engineer (Antigravity)*
