# HD SOURCE: ARCH_BMAD_Method_FRONT_45_P064-064
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_45
Part Title: NONE
Chapter Title: NONE
Section Title: Môtả Chunk Range: Pages 64 to 64
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

"Dùng khi một file markdown đã phát triển quá lớn để quản lý hiệu quả (hơn năm trăm dòng)."

Tài liệu lớn gây ra hai vấn đề chính:

Đối với LLM: Context window giới hạn cónghĩa làagent không thể load toàn bộtài liệu  chỉ đọc một phần, dẫn đến quyết định không đầy đủ .

Đối với con người: Khómaintain, khó review thay đổi, xung đột version control khi nhiều người cùng chỉnh sửa.

## Cơchế hoạt động

Công cụchia file tại các tiêu đề cấp hai ( ## ):

```
# PRD analytics dashboard ← cấp một (không chia) ## 1. tổng quan ← cấp hai (điểm chia) ## 2. personas người dùng ← cấp hai (điểm chia) ### 2.1 persona chính ← cấp ba (không chia, nằm trong section) ## 3. requirements ← cấp hai (điểm chia)
```

## Đầu ra

```
PRD/ ├── index.md            ← Danh sách sections với liên kết ├── 01 -tongquan.md     ← Section 1 ├── 02 -personas.md      ← Section 2 ├── 03 -requirements.md  ← Section 3 └── 04 -metrics.md       ← Section 4
```

## Sau khi chia

Công cụ hỏi bạn muốn làm gì với file gốc:

Xóa file gốc (các sections đã được đặt trong thưmục)

Archive file gốc (đổi tên thành .archive )

Giữnguyên file gốc (duy trì cả hai)

Khuyến nghị : Xóa hoặc archive để tránh nhầm lẫn hai nguồn thông tin.

## 4.12 bmad-index-docs  -  tạo chỉmục thưmục

Môtả