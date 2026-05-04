# SKILL: wiki-absorb

Nâng cấp và hòa giải các `DRAFT` atoms thành tri thức chính thức trong Wiki.

## Context (Bối cảnh)
Sau khi `wiki-ingest` nạp dữ liệu thô vào `atoms` table dưới dạng `DRAFT`, `wiki-absorb` sẽ thực hiện việc đối soát với kho tri thức hiện có để quyết định cách tích hợp chúng mà không gây mâu thuẫn hoặc trùng lặp.

## Workflow (Quy trình)

### Tier 1: Phân tích Cấu trúc (Tự động - Không LLM)
1. **Quét**: Lấy danh sách atoms có `status='DRAFT'`.
2. **So sánh Hash**: Nếu hash đã tồn tại ở một atom `VERIFIED/SYNTHESIZED` → Ghi log `DUPLICATE` và bỏ qua.
3. **So sánh Content (Exact Match)**: Nếu nội dung giống hệt (dù hash khác do metadata) → Ghi log `EXACT` và bỏ qua.
4. **Xác định ADDITIVE**: Nếu không có atom nào cùng `title` hoặc `topic` → Nâng cấp lên `VERIFIED`.

### Tier 2: Hòa giải Nhận thức (LLM - Confidence >= 0.85)
1. **Phát hiện mâu thuẫn (CONTRADICTS)**: Nếu cùng `title` nhưng nội dung khác biệt.
2. **LLM Reranking/Reasoning**: Gọi LLM (đọc kèm `USER.md`) để phân tích xem thông tin mới bổ sung hay thay thế thông tin cũ.
3. **Quyết định**:
   - Nếu thông tin mới hay hơn/cập nhật hơn → Nâng cấp lên `VERIFIED`, đánh dấu atom cũ bị `SUPERSEDES`.
   - Nếu thông tin mới chỉ là một góc nhìn khác → Tạo liên kết `RELATED_TO`.

### Tier 3: Quản trị Con người (Human Gate - Confidence < 0.85)
1. **Ghi nhận rủi ro**: Nếu mâu thuẫn lớn nhưng độ tin cậy nguồn thấp.
2. **Tạo Decision File**: Ghi chi tiết mâu thuẫn vào `3-resources/wiki/decisions/DECISION_[ID].md`.
3. **Review Queue**: Đặt `human_review_flag = 1` và thêm vào `review_queue`.

## Constraints (Ràng buộc thép)
- **R8 - Human Gate**: Tuyệt đối KHÔNG set status thành `SYNTHESIZED`. Trạng thái cao nhất script có thể set là `VERIFIED`.
- **R4 - Log Every Write**: Mọi thay đổi DB hoặc file phải log vào `3-resources/wiki/log.md`.
- **Traceability**: Giữ nguyên link dẫn về `raw/` của atom gốc.

## Lệnh thực thi
```bash
python .agent/skills/wiki-absorb/scripts/reconciler.py
```
