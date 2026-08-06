# HD SOURCE: ARCH_BMAD_Method_FRONT_60_P081-081
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_60
Part Title: NONE
Chapter Title: NONE
Section Title: Làm việc với tài liệu phân tích có sẵn
Chunk Range: Pages 81 to 81
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Giai đoạn D  -  Chỉ sốthành công:

nào sau sáu tháng?"

```
"Dự án thành công trông nhưthế "Bạn sẽ theo dõi những chỉ sốnào?" "Chỉ sốnào quan trọng nhất?"
```

## Giai đoạn E  -  Checkpoint Previews vàAdvanced Elicitation:

Tại các điểm quyết định, PM Agent cung cấp Checkpoint Preview và tùy chọn Advanced Elicitation.

## Cấu trúc chuẩn của PRD

Tài liệu PRD được tạo theo template cố định:

```
án]
```

```
# Tài liệu yêu cầu sản phẩm  -  [tên dự ## 1. tổng quan dự án ## 2. bối cảnh và bối cảnh nền - Phát biểu vấn đề - Phân tích trạng thái hiện tại ## 3. mục tiêu và chỉ sốthành công - Mục tiêu kinh doanh - Mục tiêu người dùng - Chỉ sốthành công (cóthể đo lường) ## 4. đối tượng người dùng / personas - Persona 1: [Tên, Vai trò, Bối cảnh] - Persona 2: ... ## 5. requirements chức năng - Phải có (MVP) - Nên có (v1) - Không có (explicitly excluded) ## 6. requirements phi chức năng (nfrs) - Mục tiêu hiệu năng - Yêu cầu bảo mật - Nhu cầu scalability - Yêu cầu tuân thủ ## 7. nguyên tắc trải nghiệm người dùng ## 8. ràng buộc kỹ thuật ## 9. giả định và phụthuộc ## 10. phụ lục
```

## Làm việc với tài liệu phân tích có sẵn

Khi bạn đã cótài liệu từ Giai đoạn Phân tích, có hai chiến lược:

## Chiến lược tốiưu -  Nén rồi load:

```
bmad-distillator ./analysis/     # Nén tất cả tài liệu phân tích # → tạo distillate file để load vào phiên tạo PRD
```

## Chiến lược trực tiếp  -  Load ngay: