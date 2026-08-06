# HD SOURCE: ARCH_BMAD_Method_FRONT_66_P087-087
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_66
Part Title: NONE
Chapter Title: NONE
Section Title: 7.2 hệ sốchi phí 10x
Chunk Range: Pages 87 to 87
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Chương 7: Giai đoạn 3  -  thiết kế giải pháp: tại sao đây là giai đoạn không thể bỏ qua

## Bạn sẽ học được gì?

Sau khi đọc chương này, bạn sẽ hiểu:

Tại sao Thiết kế giải pháp tồn tại và chi phícủa việc bỏ qua nó Ba loại xung đột agent xảy ra khi thiếu kiến trúc chung Architecture Document: cấu trúc và các ADR quan trọng Chiến lược ngăn ngừa xung đột agent: ADRs, tài liệu FR/NFR, tiêu chuẩn Epics và Stories và Kiểm tra sẵn sàng triển khai Project Context  "điều lệ " của dự án

## 7.1 vấn đềmà thiết kế giải pháp giải quyết

Hãy xem xét kịch bản không có giai đoạn này:

```
PRD.md: "Build hệthống analytics dashboard SaaS" Agent 1 triển khai Epic 1 (Data Ingestion): → "Tôi sẽ dùng REST API, PostgreSQL, đặt tên cột camelCase" Agent 2 triển khai Epic 2 (Visualization): → "Tôi sẽ dùng GraphQL, MongoDB, đặt tên cột snake_case" Agent 3 triển khai Epic 3 (Reporting): → "Tôi sẽ dùng REST API, PostgreSQL, đặt tên cột PascalCase" Kết quả : Ác mộng khi tích hợp  -  kiểu API xung đột, database schema không tương thích, quyước đặt tên hỗn độn không thể reconcile
```

Đây là "Xung đột Agent" -  một vấn đề đặc thù của phát triển hướng AI mà các phương pháp truyền thống không cần xử lý vì con người trong đội thường giao tiếp liên tục.

Trong môi trường AI-driven, nhiều agent làm việc trong các session riêng biệt, không có khảnăng "nghe" nhau. Không có kiến trúc chung → Mỗi agent ra quyết định độc lập theo những gìnócho là tốt nhất → Kết quả không nhất quán.

## 7.2 hệ sốchi phí 10x

Tài liệu chính thức khẳng định: