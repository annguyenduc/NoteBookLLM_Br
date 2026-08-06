# HD SOURCE: ARCH_BMAD_Method_FRONT_137_P165-165
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_137
Part Title: NONE
Chapter Title: NONE
Section Title: Khi nào cài module TEA
Chunk Range: Pages 165 to 165
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

| **P0**   | Chặn release - bắt buộc phải pass       | Xác thực, xử lýthanh toán, tính toàn vẹn dữ liệu   |
|----------|-------------------------------------------------|-------------------------------------------------------------|
| **P1**   | Rủi ro cao - nên pass                         | Core user flows, data validation                            |
| **P2**   | Rủi ro trung bình - sửa trong sprint tiếp | Edge cases, UI inconsistencies                              |
| **P3**   | Rủi ro thấp - theo dõi trong tương lai      | Nice-to-have, cosmetic issues                               |

Khi Murat đề xuất release gate decision, nó rõ ràng phân biệt: "P0 tests đều pass. Một P1 fail là [tên test] với impact [môtả ]. Khuyến nghị : Delay release 24 giờ để sửa P1 này."

## Playwright utils vàMCP integrations

## Playwright Utils:

Tạo scaffold E2E tests với Playwright Tạo Page Object Model structure Cài đặt visual regression testing

## MCP Integrations:

Tích hợp vớCho phép test agents tương tác với Model Context Protocol i external test systems

## Khi nào cài module TEA

| Tình huống                                              | Nên cài TEA         |
|-----------------------------------------------------------|---------------------|
| Lĩnh vực được quản lý (y tế HIPAA, tài chính PCI-DSS) | Bắt buộc        |
| Sản phẩm enterprise với hàng trăm requirements       | Có                  |
| Team không có QA chuyên biệt nhưng cần testing strategy | Có                  |
| Muốn ATDD từngày đầu của development               | Có                  |
| Project nhỏ của developer độc lập                    | Cóthể không cần |