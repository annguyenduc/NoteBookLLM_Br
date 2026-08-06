# HD SOURCE: ARCH_BMAD_Method_FRONT_26_P045-045
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_26
Part Title: NONE
Chapter Title: NONE
Section Title: Mã code modules đầy đủ Chunk Range: Pages 45 to 45
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## 3.3 cài đặt tự động  -  dành cho pipeline và script

Khi cần cài đặt mà không cóngười tương tác (CI/CD pipeline, script khởi tạo dự án):

## Cúpháp cơbản

npx bmad-method install [các-tùy-chọn]

## Tất cả tùy chọn được hỗ trợ

| Tùy chọn          | Giátrị ví dụ               | Môtả                                           |
|---------------------|-------------------------------|--------------------------------------------------|
| `--directory`       | `./` hoặc `/projects/myapp` | Thưmục cài đặt                                 |
| `--modules`         | `bmm,tea,cis`                 | Danh sách modules, phân cách bằng dấu phẩy |
| `--tools`           | `claude-code`                 | Mã code của AI IDE                             |
| `--yes` hoặc `-y` | (không có giátrị )          | Tự động xác nhận tất cả                   |

## Mã code modules đầy đủ

| Mã code   | Tên module                  | Mục đích                                        |
|-----------|-----------------------------|--------------------------------------------------|
| `bmm`     | BMad Method                 | Bộagile cốt lõi - **BẮT BUỘC phải có** |
| `bmb`     | BMad Builder                | Tạo custom agents vàworkflows                 |
| `tea`     | Test Architect              | Kiểmthửenterprise và quality assurance       |
| `gds`     | Game Dev Studio             | Workflows phát triển game                      |
| `cis`     | Creative Intelligence Suite | Công cụ đổi mới và sáng tạo                |

Lưuý quan trọng: Module bmm luôn phải được bao gồm. Các module khác là tùy chọn và cóthể cài thêm bất kỳ lúc nào.