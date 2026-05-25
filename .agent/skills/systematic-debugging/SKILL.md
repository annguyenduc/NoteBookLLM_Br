---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
---

# Systematic Debugging

Random fixes waste time and create new bugs. Quick patches mask underlying issues.

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

<EXTREMELY-IMPORTANT>
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST

Nếu chưa hoàn thành Phase 1 (Chẩn đoán nguyên nhân gốc), agent tuyệt đối cấm đề xuất hoặc áp dụng bản vá.
</EXTREMELY-IMPORTANT>

## The Four Phases of Diagnostic Workflow

### Phase 1: Root Cause Investigation
**Trước khi áp dụng bất kỳ bản vá nào, agent bắt buộc phải:**
1. **Đọc kĩ log lỗi & Stack Traces:** Ghi nhận chính xác line numbers, file paths, error codes.
2. **Tái hiện lỗi:** Xác định các bước kích hoạt lỗi một cách nhất quán.
3. **Kiểm tra thay đổi gần đây:** Tra Git diff, commits gần nhất, dependency mới.
4. **Diagnostic Instrumentation (Hệ thống nhiều layer):** Thêm log đầu vào/đầu ra tại từng ranh giới module để khoanh vùng WHERE & WHY lỗi xảy ra.
5. **Recursive Hypothesis Testing (sandbox):** Cho phép cô lập hàm nghi vấn ra file nháp độc lập (ví dụ `/scratch/debug_x.py`) để chạy thử các giá trị biên.

### Phase 2: Pattern Analysis
**Tìm quy luật trước khi sửa:**
1. Tìm các ví dụ code đang hoạt động ổn định và so sánh.
2. Đọc toàn bộ tài liệu tham chiếu (Reference) của pattern đang áp dụng.
3. Liệt kê mọi sự khác biệt dù là nhỏ nhất giữa code chạy đúng và code lỗi.

### Phase 3: Hypothesis and Testing
**Phương pháp khoa học:**
1. Đưa ra duy nhất 1 giả định rõ ràng: *"Tôi nghĩ X là nguyên nhân gốc vì Y"*.
2. Thực hiện sửa đổi tối thiểu (1 biến duy nhất mỗi lần) để kiểm chứng giả định.
3. Kiểm thử GREEN trước khi chuyển sang Phase 4.

### Phase 4: Implementation
**Sửa tận gốc, cấm sửa ngọn:**
1. Tạo kịch bản test case RED trước tiên bằng kỹ năng `test-driven-development`.
2. Áp dụng bản vá đơn lẻ (**Atomic Changes**) cho đúng nguyên nhân gốc, cấm bundled refactoring "tiện tay".
3. Xác minh test suite GREEN.
4. **Architectural Circuit Breaker:** Nếu thử quá **3 lần sửa lỗi liên tiếp thất bại**, Agent bắt buộc phải **DỪNG LẠI** và phản biện nền tảng kiến trúc (Question Architecture), thảo luận trực tiếp với con người, cấm tự vá lần thứ 4.

## Safe Execution Rules
- **Permission Gate:** Xác thực an toàn trước khi truy cập logs hoặc config hệ thống nhạy cảm.
- **Check before Write:** Luôn sử dụng `grep` hoặc `view_file` trước khi sửa đổi code.

## Quality Gate (Red Flags - STOP & Re-analyze)
- ❌ **Guess & Check:** Thử thay đổi mò mẫm để xem có chạy được hay không (Strictly Forbidden).
- ❌ **No Regression Test:** Sửa lỗi nhưng không có test case chứng minh lỗi sẽ không tái phát.
