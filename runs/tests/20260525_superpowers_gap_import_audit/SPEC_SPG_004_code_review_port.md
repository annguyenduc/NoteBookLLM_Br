# SPEC-SPG-004: Adopt Superpowers code review pair (requesting & receiving review)

> **Trạng thái:** DỰ THẢO (Chờ phê duyệt - Requires AN GO)
> **Mã hiệu:** SPEC-SPG-004
> **Giai đoạn:** Giai đoạn 4 — Parallel Subagents & Review Mechanics
> **Mục tiêu:** Port và chuẩn hóa bộ đôi kỹ năng `requesting-code-review` và `receiving-code-review` của Superpowers làm chuẩn rà soát chính thức của vault, gộp logic của `cm-code-review` cũ thành phần thích nghi (adaptation section) cho môi trường chat cục bộ không sử dụng PR tự động.

---

## 1. Bối cảnh & Lý do
Quy trình rà soát code giúp phát hiện sớm các lỗ hổng logic, lỗi hồi quy và đảm bảo mã nguồn đạt tiêu chuẩn tối ưu trước khi chốt task.

Trong môi trường Antigravity, do cấm tuyệt đối các hành động tự động commit, push code hay tạo GitHub PR lên remote, chúng ta sẽ **thích nghi hoàn toàn bộ đôi này sang môi trường trò chuyện cục bộ (local chat review)**. Đồng thời, triết lý "Chống xã giao performative" (No Performative Agreement) và "Phản biện thực chứng" (Verify before implementing) của Superpowers sẽ được thiết lập làm kim chỉ nam vận hành.

---

## 2. Mã nguồn nguồn & Đích đến
*   **Mã nguồn tham chiếu (Source):**
    - `workspaces/refs/superpowers/skills/requesting-code-review/SKILL.md`
    - `workspaces/refs/superpowers/skills/receiving-code-review/SKILL.md`
*   **Tệp tin cũ gộp vào (Legacy Source):** `.agent/skills/cm-code-review/SKILL.md`
*   **Tệp tin đích (Target Destination):**
    - `.agent/skills/requesting-code-review/SKILL.md` [NEW]
    - `.agent/skills/receiving-code-review/SKILL.md` [NEW]

---

## 3. Nội dung thiết kế kỹ thuật (Implementation Details)

### A. Triết lý gốc (Canonical Standard)
- **`requesting-code-review`**: Rà soát sớm, rà soát thường xuyên. Phân loại feedback thành Critical (Sửa ngay), Important (Sửa trước khi đi tiếp) và Minor.
- **`receiving-code-review`**: Đòi hỏi thực chứng kỹ thuật và kỷ luật, cấm biểu diễn xã giao (No Performative Agreement - cấm "You're absolutely right!", "Great point!"), cấm đồng ý mù quáng. Thực hiện triết lý "Verify before implementing" và "Actions speak louder than words" (chỉ sửa và báo cáo thực tế).

### B. Lớp thích nghi Antigravity & gộp `cm-code-review`
1.  **PR-Free Manual Chat Review (Rà soát trực tiếp trong Chat)**:
    - Loại bỏ hoàn toàn các giả định về việc tự động tạo GitHub PR, push code hay merge tự động.
    - Thay vào đó, Agent tự thu thập và trình bày một bản so sánh diff sạch sẽ (clean diff representation) thông qua `git diff` trực tiếp trong cuộc chat để bạn duyệt.
2.  **Khung phản hồi feedback (Response Framework từ `cm-code-review`)**:
    - Khi nhận phản biện:
        - *Đúng:* Sửa Fact ngay lập tức và báo cáo thực tế: *"Đã sửa lỗi X tại file Y. Chạy test suite pass."* (Tuyệt đối không cảm ơn xã giao hay dài dòng xin lỗi).
        - *Chưa rõ:* Hỏi rõ từng điểm nghi vấn, cấm tự suy diễn.
        - *Tranh chấp:* Phản biện Fact bằng bằng chứng kỹ thuật (Tests/Code/Docs thực tế), cấm đồng ý mù quáng để đối phó.
3.  **Kỷ luật Continuity**:
    - Chỉ được phép xin phép bạn cập nhật các bài học đắt giá vào `CONTINUITY.md` sau khi chu kỳ review hoàn tất, tuyệt đối cấm tự ý ghi đè.

---

## 4. Dự thảo nội dung tệp tin đích

### Tệp 1: `.agent/skills/requesting-code-review/SKILL.md`
```markdown
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
- Cấm tự ý merge hay chốt hoàn thành khi test suite chưa đạt GREEN.
```

---

### Tệp 2: `.agent/skills/receiving-code-review/SKILL.md`
```markdown
---
name: receiving-code-review
description: Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation
---

# Code Review Reception (Antigravity Adapted)

Code review đòi hỏi năng lực kỹ thuật và thực chứng, cấm biểu diễn xã giao hay đồng ý mù quáng.

**Core principle:** Verify before implementing. Ask before assuming. Technical correctness over social comfort.

## The Response Pattern
Khi nhận phản hồi review từ người dùng:
1. Đọc kĩ toàn bộ feedback, không phản ứng cảm tính.
2. Nhắc lại yêu cầu kỹ thuật theo cách hiểu của mình (hoặc hỏi nếu chưa rõ).
3. Xác minh thực tế đối chiếu với codebase.
4. Đánh giá tính khả thi và rủi ro breaking changes.
5. Phản hồi thực tế (fact-based) hoặc phản biện kèm bằng chứng.
6. Triển khai sửa đổi từng mục một và chạy test kiểm định.

## Cấm biểu diễn xã giao (No Performative Agreement)
Tuyệt đối cấm sử dụng các câu nói xã giao performative:
- ❌ *"Bạn hoàn toàn đúng!"*
- ❌ *"Ý kiến tuyệt vời!"*
- ❌ *"Cảm ơn bạn đã phát hiện lỗi này!"*
- ❌ Bất kỳ hình thức bày tỏ lòng biết ơn xã giao nào.

**Thay vào đó, hãy tập trung vào Fact và Hành động:**
- ✅ *"Đã sửa lỗi X tại file Y. Chạy test suite pass."*
- ✅ *"Good catch - lỗi logic X đã được fix tại [location]."*
- ✅ [Chỉ sửa lỗi và hiển thị mã nguồn đã sửa]

## Phản biện thực chứng (When to Push Back)
Agent bắt buộc phải phản biện lại nếu feedback của người dùng có nguy cơ:
- Phá vỡ các tính năng đang hoạt động bình thường (Breaking Changes).
- Vi phạm nguyên lý YAGNI (thêm tính năng thừa không dùng tới).
- Vi phạm các quyết định kiến trúc cốt lõi của vault hoặc AGENTS.md.

**Cách thức phản biện:**
- Trình bày thực tế kỹ thuật rõ ràng, lịch sự, không tự vệ cảm tính.
- Reference trực tiếp đến các tệp tin test case hoặc mã nguồn chạy thực tế để chứng minh.
```

---

## 5. Kế hoạch khôi phục (Rollback Plan)
*   **Backup**: Vì đây là hai tệp tin mới tinh (`[NEW]`), phương án khôi phục đơn giản là xóa hai tệp tin mới tạo:
    - `.agent/skills/requesting-code-review/SKILL.md`
    - `.agent/skills/receiving-code-review/SKILL.md`
    và dọn dẹp thư mục nếu rỗng.

---

## 6. Kế hoạch kiểm thử (Test Plan)
Sau khi port thành công, Agent bắt buộc phải kiểm tra lại hệ thống định tuyến bằng cách:
1.  Xác nhận Agent nhận diện chính xác bộ đôi kỹ năng review khi người dùng ra lệnh rà soát.
2.  Chạy thử kịch bản dry-run tự so sánh và trình bày diff sạch trong chat mà không gây ra bất kỳ tác vụ write canonical nào lên `3-resources/`.
