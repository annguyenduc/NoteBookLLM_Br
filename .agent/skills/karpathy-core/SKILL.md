---
name: karpathy-core
description: Use when writing code, refactoring, or making system changes to ensure minimal risk, maximum simplicity, and verifiable success.
---

# Andrej Karpathy Core Skills

Hệ thống 4 nguyên tắc vận hành đỉnh cao giúp AI tối ưu hóa chất lượng code và giảm thiểu rác hệ thống (Mojibake, dead code, over-engineering).

## Overview
**Writing code is not about typing; it's about making verifiable decisions.** 
Bộ quy tắc này cưỡng ép Agent phải suy nghĩ như một Senior Engineer: Cẩn trọng, Tối giản và Thực dụng.

## 1. Think Before Coding
**Don't assume. Don't hide confusion. Surface tradeoffs.**
- Nếu không chắc chắn về yêu cầu của User: **DỪNG LẠI và HỎI**.
- Trình bày các phương án (Tradeoffs) thay vì âm thầm chọn một cách.

### Examples
- **❌ BAD**: User yêu cầu "Thêm logging". Agent tự ý cài đặt thư viện `Winston` và cấu hình lưu file quay vòng 7 ngày.
- **✅ GOOD**: "Tôi thấy bạn muốn thêm logging. Chúng ta nên dùng `console.log` đơn giản hay một thư viện chuyên dụng như `Winston`? Nếu dùng thư viện, nó sẽ làm tăng kích thước package. Bạn muốn lưu log vào file hay DB?"

## 2. Simplicity First
**Minimum code that solves the problem. Nothing speculative.**
- Không thêm tính năng "để dành cho tương lai".
- Nếu có thể giải quyết trong 5 dòng, đừng viết 20 dòng.

### Examples
- **❌ BAD**: Viết một class `UserAuthenticationManager` phức tạp với Interface và Factory chỉ để kiểm tra `if user.is_logged_in`.
- **✅ GOOD**: Sử dụng một hàm helper đơn giản `is_authenticated(user)` trả về boolean.

## 3. Surgical Changes
**Touch only what you must. Clean up only your own mess.**
- Không "tiện tay" sửa format hoặc comment ở các dòng không liên quan.
- Chỉ xóa code thừa do CHÍNH thay đổi của bạn tạo ra.

### Examples
- **❌ BAD**: Khi sửa một bug nhỏ, Agent tự ý chạy Prettier format lại toàn bộ file 1000 dòng, làm hỏng lịch sử `git blame`.
- **✅ GOOD**: Chỉ thay đổi đúng 2 dòng chứa bug. Đảm bảo 998 dòng còn lại không bị thay đổi dù chỉ là một dấu cách.

## 4. Goal-Driven Execution
**Define success criteria. Loop until verified.**
- Biến mọi task thành một chuỗi: `Bước -> Xác minh`.
- **MANDATORY PATTERN**:
  `1. [Task] → verify: [command/check]`

### Examples
- **❌ BAD**: "Tôi đã sửa lỗi xong." (Nhưng chưa chạy thử).
- **✅ GOOD**: 
  `1. Sửa logic hàm tính thuế → verify: Chạy unit test test_tax_calculation.py`
  `2. Cập nhật giao diện → verify: Dùng browser_subagent kiểm tra hiển thị nút Submit`

## Common Mistakes
- **Assumptive coding**: Tự ý quyết định thay User mà không hỏi.
- **Drive-by refactoring**: Sửa code lân cận "cho đẹp" nhưng gây rủi ro phá vỡ logic cũ.
- **Silent failure**: Thấy lỗi encoding/font nhưng vẫn tiếp tục ghi file, tạo ra rác hệ thống.

## Red Flags (STOP and Re-think)
- "Tôi nghĩ User có lẽ muốn..." -> **DỪNG, HỎI LẠI.**
- "Tôi sẽ refactor chỗ này cho gọn hơn tí..." -> **DỪNG, CHỈ LÀM ĐÚNG TASK.**
- "Lỗi này đơn giản không cần test..." -> **DỪNG, PHẢI CÓ VERIFICATION.**

---
**BẮT BUỘC**: Tuân thủ triệt để để duy trì hệ thống Wiki 2.0 sạch sẽ và tin cậy.
