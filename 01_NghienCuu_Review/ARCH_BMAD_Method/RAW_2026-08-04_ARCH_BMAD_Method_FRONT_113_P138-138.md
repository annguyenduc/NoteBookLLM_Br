# HD SOURCE: ARCH_BMAD_Method_FRONT_113_P138-138
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_113
Part Title: NONE
Chapter Title: NONE
Section Title: Quyết định vềfile gốc
Chunk Range: Pages 138 to 138
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Khi nào cần

Tài liệu chính thức:

"Dùng khi một file markdown đã phát triển quá lớn để quản lý hiệu quả (hơn năm trăm dòng)."

Ngưỡng năm trăm dòng là hướng dẫn, không phải quy tắc cứng. Dấu hiệu thực tếcần chia nhỏ :

Agent thường xuyên đọc sai phần hoặc bỏ sót section quan trọ Việc tìm kiếm một thông tin cụthểmất nhiều thờFile đang được nhiều người cùng chỉnh sửa → merge conflicts thườ

## Cơchế : Chia tại tiêu đề cấp hai

Công cụphân tích tài liệu và chia tại các tiêu đề ## -tiêu đề cấp hai:

```
# Tài liệu kiến trúc ← tiêu đề cấp một: Không chia ## 1. tổng quan ← tiêu đề cấp hai: Điểm chia ... ## 2. tech stack ← tiêu đề cấp hai: Điểm chia ... ### 2.1 backend ← tiêu đề cấp ba: Không chia (nằm trong section) ... ## 3. adrs ← tiêu đề cấp hai: Điểm chia ...
```

## Đầu ra

File ban đầu architecture.md được biến thành thưmục:

```
architecture/ ├── index.md              ← Tổng quan vànavigation links ├── 01 -tongquan.md       ← Section "Tổng Quan" ├── 02 -techstack.md      ← Section "Tech Stack" ├── 03 -adrs.md            ← Section "ADRs" ├── 04 -database.md        ← Section tiếp theo └── ...
```

File index.md tự động được tạo với danh sách tất cả sections, tên vàmôtảngắn gọn.

## Quyết định vềfile gốc

Sau khi chia xong, công cụ hỏi bạn muốn làm gì với file gốc:

ng i gian ng xuyên