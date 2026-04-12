# 📝 SOP: Quy trình File-back (Knowledge Compounding)

> **Mã quy trình**: SOP-OPS-001 | **Phiên bản**: v3.6
> **Mục tiêu**: Đảm bảo mọi "insight" hoặc giải pháp có giá trị trong hội thoại được lưu trữ vĩnh viễn vào Wiki để tránh thất thoát tri thức.

## 1. Khi nào cần thực hiện File-back?
Thực hiện ngay khi kết thúc một tác vụ phức tạp hoặc sau một chuỗi lập luận sâu sắc (Deep Reasoning) mà:
- Giải quyết được một lỗi kỹ thuật khó.
- Thiết kế được một cấu trúc/mô hình mới.
- Tổng hợp được thông tin từ nhiều nguồn khác nhau.
- Người dùng yêu cầu "Lưu lại cái này".

## 2. Các bước thực hiện (@librarian)

### Bước 0: Kiểm tra trùng lặp (Deduplication) - QUAN TRỌNG
- Trước khi tạo bất kỳ nội dung nào, phải kiểm tra các **Master KIs** trỏ đến chủ đề đó.
- Nếu nội dung mới chỉ là phần cập nhật nhỏ cho kiến thức đã có $\rightarrow$ **Cập nhật trực tiếp** vào Master KI thay vì tạo file mới.

### Bước 1: Trích xuất (Extract)
- Tóm tắt lại giải pháp đã thực hiện trong phiên làm việc.
- Chắt lọc các đoạn code quan trọng hoặc sơ đồ kiến trúc (format Mermaid).

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

## 4. Danh sách Master KIs (Cần liên kết)
Mọi Insight mới PHẢI liên kết tới ít nhất 2 trong các Master KIs sau:
- [[PEDAGOGY_Master_Handbook]]: Tri thức sư phạm gốc.
- [[STEAM_Project_Ideas]]: Ý tưởng và kỹ thuật dự án.
- [[LMS_KB_INDEX]]: Mục lục tri thức hệ thống.
- [[Directory_Architecture_AI_Era]]: Quy định về cấu trúc.

---
*Phát hành bởi @pm | NoteBookLLM_Br v3.6*
