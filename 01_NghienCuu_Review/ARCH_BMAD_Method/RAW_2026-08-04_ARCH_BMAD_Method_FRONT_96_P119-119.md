# HD SOURCE: ARCH_BMAD_Method_FRONT_96_P119-119
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_96
Part Title: NONE
Chapter Title: NONE
Section Title: Phương pháp truy vết
Chunk Range: Pages 119 to 119
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## 10.3 edge case hunter  -  truy vết đường đi cơhọc

bmad-review-edge-case-hunter

## Tại sao trực giao với review đối nghịch?

Tài liệu giải thích rõ:

"Chạy cả bmad-review-adversarial-general và bmad-review-edge-case-hunter cùng nhau để cócoverage trực giao. Review đối nghịch bắt các vấn đề chất lượng và tính đầy đủ ; edge case hunter bắt các đường đi chưa được xử lý."

| Review Đối Nghịch   | Edge Case Hunter                 |                              |
|------------------------|----------------------------------|------------------------------|
| Cách tiếp cận      | Thái độ hoài nghi                | Phương pháp cơhọc          |
| Tìm gì                 | Vấn đề toàn diện, thiếu sót | Đường đi logic chưa có guard |
| Đầu ra                | Văn xuôi cóphân loại severity  | Mảng JSON chuẩn          |
| Trùng lặp?           | Rấtít                         | Rấtít                     |

Dùng cả hai cho coverage thực sựtoàn diện.

## Phương pháp truy vết

Quy trình Edge Case Hunter:

```
Bước 1: Liệt kêTẨ T CẢ các điểm phân nhánh trong code: - if/else - switch/case - try/catch - ternary operators - Optional chaining ?. - Nullish coalescing ?? Bước 2: Từmỗi điểm phân nhánh, phân loại cơhọc các edge classes: - Giátrịnull/undefined - Chuỗi rỗng - Mảng rỗng - Sốâm, số 0 - Giátrị ở ranh giới (off-by-one) -Types không mong đợi -Đồng thời (concurrent modifications) Bước 3: Kiểm tra từng edge class với guards hiện có Bước 4: Chỉ report các đường đi CHƯA có guard → Âm thầm bỏ qua các trường hợp đã được xử lý
```