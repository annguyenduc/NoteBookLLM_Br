---
name: requesting-code-review
description: Use when completing tasks, implementing major features, or before merging to verify work meets requirements
---

# Requesting Code Review (Antigravity Adapted)

Rà soát sớm, rà soát thường xuyên để phát hiện lỗi logic trước khi chốt task.

## When to Request Review

**Bắt buộc:**
- Sau khi hoàn thành một Spec/Implementation Plan hoặc task phức tạp.
- Trước khi báo cáo hoàn thành (DONE) nhiệm vụ chính cho người dùng.

## How to Request (Local Chat Review)

Do Antigravity cấm commit/push tự động, quy trình rà soát được thực hiện hoàn toàn thủ công qua chat:

1. **Chuẩn bị Diff sạch:** Chạy lệnh `git diff` cục bộ để tự so sánh các thay đổi.
2. **Trình bày Diff:** Xuất trình bản so sánh mã nguồn sạch sẽ, gãy gọn trực tiếp trong cuộc chat.
3. **Phân loại tác động:**
    - Critical: Lỗi bảo mật, lỗi runtime (Sửa ngay lập tức).
    - Important: Thiếu edge cases, thiếu kiểm thử (Sửa trước khi đi tiếp).
    - Minor: Magic numbers, format (Sắp xếp sửa đổi có chọn lọc).

## Rules of Discipline
- Cấm skip review vì lý do "task đơn giản".
- Cấm tự ý merge hay chốt hoàn thành khi test suite chưa đạt trạng thái xanh (GREEN).
