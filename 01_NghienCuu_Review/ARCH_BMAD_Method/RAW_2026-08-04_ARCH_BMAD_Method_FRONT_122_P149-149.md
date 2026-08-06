# HD SOURCE: ARCH_BMAD_Method_FRONT_122_P149-149
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_122
Part Title: NONE
Chapter Title: NONE
Section Title: Bước 2: Tạo bối cảnh dự án (bước quan trọng nhất)
Chunk Range: Pages 149 to 149
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Tài liệu architecture đang còn relevant PRD nếu còn epics chưa hoàn thành

## Bước 2: Tạo bối cảnh dự án (bước quan trọng nhất)

bmad-generate-project-context

## Tài liệu chính thức:

"Khuyến nghịcho Dự Án Hiện Có: Tạo projectcontext.md đểnắm bắt các patterns và quyước của codebase hiện có. Điều này đảm bảo AI agents tuân theo các practices đã thiết lập của bạn khi thực hiện thay đổi."

Đây là bước quan trọng nhất trong toàn bộ quy trình onboarding. Không cóprojectcontext.md , mỗi agent session bắt đầu từzero.

## Những gì tool quét

bmad-generate-project-context phân tích codebase của bạn để xác định:

```
Cấu trúc dự án: ├── package.json / requirements.txt    → Tech stack và versions ├── tsconfig.json / .eslintrc           → Config và rules ├── Cấu trúc /src                      → Tổ chức code (theo feature? theo layer?) ├── Files hiện có                      → Quyước đặt tên └── Test files                         → Patterns test (vịtrí, đặt tên, frameworks) Database: ├── Schema files                       → Đặt tên columns (snake_case? camelCase?) ├── Migration files                    → Patterns được dùng └── ORM config                         → Cách tiếp cận abstraction Code patterns (sampling): ├── Cách errors được xử lý ├── Cách API calls được cấu trúc ├── Cách components/modules được tổ chức └── Common utility patterns
```

## Review và bổ sung

Auto-generated file cần human review để thêm những gìAI bỏ sót:

nano \_bmad-output/project-context.md

## Thêm những điều không visible từ code:

"Khi thêm table mới vào DB, phải thêm migration + chạy seed script theo thứtự " "PR phải cótest coverage tăng hoặc giữnguyên  -  không bao giờ giảm"