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
