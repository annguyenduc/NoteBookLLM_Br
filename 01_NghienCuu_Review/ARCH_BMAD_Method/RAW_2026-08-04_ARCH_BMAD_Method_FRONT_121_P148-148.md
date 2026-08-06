# HD SOURCE: ARCH_BMAD_Method_FRONT_121_P148-148
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_121
Part Title: NONE
Chapter Title: NONE
Section Title: Bước 1: Dọn dẹp tài liệu lập kế hoạch đã hoàn thành
Chunk Range: Pages 148 to 148
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

API dùng REST → Agent không biết → Đề xuất thêm GraphQL → Architectural conflict Error handling cópattern cụthể → Agent viết code không theo pattern → Technical debt ngay lập tức

Giải pháp: project-context.md kết hợp với ba bước onboarding chính thức.

## 13.2 ba bước chính thức (từ tài liệu)

Tài liệu chính thức document rõ ràng ba bước đểonboard BMad vào dự án hiện có:

```
Bước 1: Dọn dẹp các tài liệu lập kế hoạch đã hoàn thành ↓ Bước 2: Tạo bối cảnh dự án ↓ Bước 3: Lấy hướng dẫn
```

## Bước 1: Dọn dẹp tài liệu lập kế hoạch đã hoàn thành

Tài liệu chính thức:

"Nếu bạn đã hoàn thành tất cả PRD epics và stories qua quy trình BMad, hãy dọn dẹp các files đó. Archive chúng, xóa chúng, hoặc rely vào version history nếu cần."

## Tại sao phải dọn?

Tài liệu lập kế hoạch cũ gây nhầm lẫn cho agents:

Agent đọc cả stories đã hoàn thành (done) lẫn stories đang chờ (pending)

Không phân biệt được trạng thái thực sựcủa dự án Đưa ra đề xuất based on outdated context

## Cách thực hiện:

```
# Phươngán 1: Archive mkdir _bmad-output/archive/ mv _bmad-output/planning-artifacts/* _bmad-output/archive/ # Phươngán 2: Xóa và dựa vào git history git add -A && git commit -m "Archive planning artifacts for v1.0" rm -rf _bmad-output/planning-artifacts/* # Phươngán 3: Tag rồi archive git tag v1.0-completed git commit -m "Archive all completed sprint artifacts" mv _bmad-output/planning-artifacts/* _bmad-output/archive/
```

## Giữ lại:

```
project-context.md -  Không bao giờ xóa
```