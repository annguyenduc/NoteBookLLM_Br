# 📝 SOP: Quy trình File-back (Knowledge Compounding)

> **Mã quy trình**: SOP-OPS-001 | **Phiên bản**: 1.0 (v3.6)
> **Mục tiêu**: Đảm bảo mọi "insight" hoặc giải pháp có giá trị trong hội thoại được lưu trữ vĩnh viễn vào Wiki để tránh thất thoát tri thức.

## 1. Khi nào cần thực hiện File-back?
Thực hiện ngay khi kết thúc một tác vụ phức tạp hoặc sau một chuỗi lập luận sâu sắc (Deep Reasoning) mà:
- Giải quyết được một lỗi kỹ thuật khó.
- Thiết kế được một cấu trúc/mô hình mới.
- Tổng hợp được thông tin từ nhiều nguồn khác nhau.
- Người dùng yêu cầu "Lưu lại cái này".

## 2. Các bước thực hiện (@librarian)

### Bước 1: Trích xuất (Extract)
- Tóm tắt lại giải pháp đã thực hiện.
- Chắt lọc các đoạn code quan trọng hoặc sơ đồ kiến trúc.

### Bước 2: Tạo tệp Insight mới
- Tạo file tại `brain/distilled/insights/YYYY-MM-DD_Ten_Insight.md`.
- Sử dụng Frontmatter chuẩn:
```markdown
---
title: [Tiêu đề Insight]
date: YYYY-MM-DD
source: [Hội thoại ID hoặc Chủ đề]
tags: [Kỹ thuật, Sư phạm, DevOps...]
confidence: [90% - Cao | 70% - Vừa]
---
```

### Bước 3: Gắn kết (Crossing)
- Luôn liên kết ít nhất 2 Master KIs có liên quan bằng `[[Wikilinks]]`.
- Cập nhật mục `Related Insights` trong các Master KIs đó.

### Bước 4: Cập nhật Nhật ký
- Thêm dòng vào `brain/log.md` với tiền tố `consolidate | File-back insight: [Tên]`.

## 3. Quy tắc "Vàng"
1. **No Duplication**: Trước khi lưu, kiểm tra xem nội dung đã có trong Master KI chưa. Nếu có rồi thì chỉ cập nhật Master KI.
2. **Context Preservation**: Luôn ghi lại "tại sao" chúng ta làm điều này (Rationale).
3. **Double Check**: Chạy `brain_lint.py` ngay sau khi tạo file mới.

---
*Phát hành bởi @pm | NoteBookLLM_Br v3.6*
