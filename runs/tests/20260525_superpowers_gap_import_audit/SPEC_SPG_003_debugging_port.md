# SPEC-SPG-003: Adopt Superpowers systematic-debugging as main debugging skill

> **Trạng thái:** DỰ THẢO (Chờ phê duyệt - Requires AN GO)
> **Mã hiệu:** SPEC-SPG-003
> **Giai đoạn:** Giai đoạn 3 — Verification, TDD & Systematic Debugging
> **Mục tiêu:** Port và chuẩn hóa `systematic-debugging` của Superpowers làm kỹ năng chẩn đoán chính thức của vault, gộp logic chẩn đoán lỗi đặc thù của `cm-debugging` cũ thành phần thích nghi (adaptation section).

---

## 1. Bối cảnh & Lý do
Quy trình chẩn đoán lỗi ngẫu nhiên ("Guess & Check") gây hao tổn Token Budget nghiêm trọng và dễ làm phát sinh thêm bug mới. Việc di trú sang chuẩn `systematic-debugging` của Superpowers thiết lập quy trình khoa học 4 Phase giúp Agent chẩn đoán chính xác nguyên nhân gốc rễ trước khi sửa.

Đồng thời, phương pháp cô lập kiểm thử đệ quy (**Recursive Hypothesis Testing**) và chốt chặn an ninh (**Permission Gate**) của `cm-debugging` cũ sẽ được gộp vào làm lớp thích nghi để Agent vận hành tự chủ và an toàn.

---

## 2. Mã nguồn nguồn & Đích đến
*   **Mã nguồn tham chiếu (Source):** `workspaces/refs/superpowers/skills/systematic-debugging/SKILL.md`
*   **Tệp tin cũ gộp vào (Legacy Source):** `.agent/skills/cm-debugging/SKILL.md`
*   **Tệp tin đích (Target Destination):** `.agent/skills/systematic-debugging/SKILL.md`

---

## 3. Nội dung thiết kế kỹ thuật (Implementation Details)

Tệp tin đích `.agent/skills/systematic-debugging/SKILL.md` sẽ lấy 100% triết lý và 4 Phase chẩn đoán của Superpowers làm nền tảng, đồng thời gộp các phần thích nghi sau:

### A. Triết lý gốc (Canonical Standard)
- Luật sắt: **`NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST`** (Không sửa đổi khi chưa chẩn đoán xong).
- Tuân thủ quy trình 4 Phase: Root Cause Investigation -> Pattern Analysis -> Hypothesis & Testing -> Implementation.
- **Bộ ngắt mạch kiến trúc (Architectural Circuit Breaker):** Nếu thử quá **3 lần vá lỗi thất bại**, Agent bắt buộc phải **DỪNG LẠI** và phản biện nền tảng kiến trúc (Question Architecture), cấm tiếp tục sửa đổi mò mẫm.

### B. Lớp thích nghi cục bộ (Adaptation Layer từ `cm-debugging`)
1.  **Recursive Hypothesis Testing (Kiểm định giả định đệ quy)**:
    - Đối với các bug khó, cho phép Agent cô lập hàm nghi ngờ ra file nháp độc lập (sandbox) để chạy thử nghiệm các giá trị biên (edge cases).
2.  **Permission Gate & Security (Chốt chặn an toàn)**:
    - Yêu cầu xác thực rõ ràng trước khi truy cập tệp tin cấu hình môi trường hoặc log hệ thống nhạy cảm, tránh rò rỉ dữ liệu.
3.  **Atomic Changes (Vá lỗi đơn lẻ)**:
    - Sửa đổi đúng 1 bug duy nhất trên mỗi lượt patch, cấm tự ý dọn dẹp refactoring "tiện tay" gây nhiễu lịch sử vết.

---

## 4. Dự thảo nội dung tệp tin đích `.agent/skills/systematic-debugging/SKILL.md`

```markdown
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
```

---

## 5. Kế hoạch khôi phục (Rollback Plan)
*   **Backup**: Trước khi thực hiện ghi đè tệp tin đích `.agent/skills/systematic-debugging/SKILL.md`, Agent bắt buộc phải sao lưu tệp tin hiện tại sang:
    `.agent/skills/systematic-debugging/SKILL.md.bak` bằng công cụ tạo file.
*   **Restore**: Nếu gặp lỗi định tuyến hoặc Agent vận hành không ổn định, thực hiện khôi phục nguyên trạng tệp tin cũ bằng cách ghi đè nội dung từ `.agent/skills/systematic-debugging/SKILL.md.bak` quay lại `.agent/skills/systematic-debugging/SKILL.md` và xóa tệp tin backup.

---

## 6. Kế hoạch kiểm thử (Test Plan)
Sau khi port thành công, Agent bắt buộc phải kiểm tra lại hệ thống định tuyến bằng cách:
1.  Chạy/đọc kịch bản test case **`T002_debugging_trigger.md`** dưới `.agent/tests/skill-triggering/` để xác nhận Agent tự động gọi `systematic-debugging` chuẩn Phase 3 khi phát hiện lỗi hệ thống.
2.  Xác nhận Agent nạp chính xác chốt mạch kiến trúc và **tuyệt đối không kích hoạt bất kỳ canonical write nào** lên `3-resources/` khi chạy thử kịch bản test.
