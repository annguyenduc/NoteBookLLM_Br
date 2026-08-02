---
name: writing-plans
description: "Sử dụng khi đã có spec hoặc yêu cầu cho một multi-step task, trước khi bắt đầu thực hiện — lập kế hoạch chi tiết để agent hoặc người thực thi có thể làm theo từng bước."
---

# Lập Kế Hoạch Thực Thi

## Tổng Quan
Viết kế hoạch toàn diện giả định người thực thi chưa biết gì về codebase và có thể có thị hiếu không nhất quán. Ghi lại mọi thứ cần biết: file nào cần sửa, code mẫu, cách test, commit từng bước nhỏ.

**Thông báo khi bắt đầu:** "Đang dùng skill writing-plans để tạo kế hoạch thực thi."

**Lưu kế hoạch tại:** `docs/superpowers/plans/YYYY-MM-DD-<tên-tính-năng>.md`

## Kiểm Tra Phạm Vi
Nếu spec bao gồm nhiều hệ thống độc lập → đề xuất tách thành nhiều kế hoạch riêng. Mỗi kế hoạch phải tạo ra phần mềm chạy được và test được độc lập.

## Cấu Trúc File
Trước khi định nghĩa task, lập bản đồ file:
- File nào sẽ được tạo mới hoặc chỉnh sửa
- Mỗi file chịu trách nhiệm gì
- File thay đổi cùng nhau → để gần nhau
- Ưu tiên file nhỏ, tập trung — tránh file lớn làm quá nhiều việc

## Kích Thước Task — Từng Bước Nhỏ
**Mỗi bước là 1 hành động (2-5 phút):**
- "Viết test thất bại" — 1 bước
- "Chạy test để xác nhận nó fail" — 1 bước
- "Viết code tối thiểu để test pass" — 1 bước
- "Chạy test xác nhận pass" — 1 bước
- "Commit" — 1 bước

## Header Bắt Buộc Của Kế Hoạch

```markdown
# Kế Hoạch Thực Thi: [Tên Tính Năng]

> **Cho agent:** BẮT BUỘC dùng subagent-driven-development hoặc executing-plans để thực hiện từng task.

**Mục tiêu:** [Một câu mô tả kết quả]
**Kiến trúc:** [2-3 câu về cách tiếp cận]
**Tech Stack:** [Công nghệ/thư viện chính]
---
```

## Cấu Trúc Task

```markdown
### Task N: [Tên Component]

**Files:**
- Tạo: `đường/dẫn/chính/xác/file.py`
- Sửa: `đường/dẫn/chính/xác/existing.py:123-145`
- Test: `tests/đường/dẫn/test.py`

- [ ] **Bước 1: Viết test thất bại**
- [ ] **Bước 2: Chạy test xác nhận fail**
- [ ] **Bước 3: Viết code tối thiểu**
- [ ] **Bước 4: Chạy test xác nhận pass**
- [ ] **Bước 5: Commit**
```

## Cấm Dùng Placeholder
Mọi bước phải có nội dung thực tế. Các mẫu sau là **thất bại của kế hoạch**:
- "TBD", "TODO", "implement later"
- "Add appropriate error handling" (không có code cụ thể)
- "Write tests for the above" (không có code test)
- "Similar to Task N" (lặp lại code đầy đủ)

## Tự Kiểm Tra Sau Khi Viết Xong
1. **Coverage**: Mỗi yêu cầu trong spec có task tương ứng không?
2. **Placeholder scan**: Tìm các từ khóa cấm ở trên
3. **Type consistency**: Tên hàm, method, property có nhất quán giữa các task không?

## Bàn Giao Thực Thi
Sau khi lưu kế hoạch, đề xuất:
- **Subagent-Driven** (khuyến nghị): dispatch agent mới cho mỗi task, review giữa các task
- **Inline Execution**: thực hiện trong phiên này với checkpoint review