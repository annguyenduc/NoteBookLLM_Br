# HD SOURCE: ARCH_BMAD_Method_FRONT_21_P040-040
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_21
Part Title: NONE
Chapter Title: NONE
Section Title: Thực hành ngay
Chunk Range: Pages 40 to 40
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## 2.9 đặc điểm của tài liệu đầu ra Để làm việc hiệu quả với BMad, bạn cần biết quyước đặt tên của các tài liệu đầu ra:

| Tài liệu                        | Tên file chính xác       | Tạo bởi                                             |
|-----------------------------------|--------------------------|---------------------------------------------------------|
| Tài liệu yêu cầu sản phẩm | `PRD.md`                 | `bmad-create-prd`                                       |
| Đặc tảUX                       | `ux-spec.md`             | `bmad-create-ux-design`                                 |
| Tài liệu kiến trúc            | `architecture.md`        | `bmad-create-architecture`                              |
| Tóm tắt concept sản phẩm    | `product-brief.md`       | `bmad-product-brief`                                    |
| Phân tích theo phương pháp Amazon | `prfaq-{tên-dự -án}.md` | `bmad-prfaq`                                            |
| Trạng thái sprint               | `sprint-status.yaml`     | `bmad-sprint-planning`                                  |
| File story                        | `story-{tên-story}.md`   | `bmad-create-story`                                     |
| Bối cảnh dự án               | `project-context.md`     | `bmad-generate-project- context` hoặc tạo thủ công |

Lưuý quan trọng: Đặc tảUX làux-spec.md , không phải ux-design.md . Đây là sựthay đổi trong phiên bản 6  -  nếu bạn đang nâng cấp từ phiên bản cũ hơn, cần lưuý điều này.

## Thực hành ngay

Bài tập thực hành đơn giản để kiểm tra sự hiểu biết của bạn:

Sau khi cài BMad (hoặc nếu đã cài rồi), hãy làm ba việc sau:

## Bài tập 1  -  Khám phácấu trúc thưmục:

```
ls _bmad/ ls _bmad/_config/agents/ ls _bmad-output/
```

Đọc nội dung của một file .customize.yaml bất kỳ để hiểu cấu trúc của nó.

## Bài tập 2  -  Kiểm tra skill integration:

Trong IDE của bạn, gõ bmad-help và quan sát output. Đây là cách xác nhận rằng BMad đã được tích hợp đúng cách vào IDE.