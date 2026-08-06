# HD SOURCE: ARCH_BMAD_Method_FRONT_125_P152-152
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_125
Part Title: NONE
Chapter Title: NONE
Section Title: Khi nào dùng
Chunk Range: Pages 152 to 152
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
bmad-create-architecture "Đây là dự án đang tồn tại. Trước khi design, hãy: 1. Đọc docs/architecture.md (kiến trúc hiện có) 2. Đọc _bmad-output/project-context.md 3. Quét cấu trúc /src để hiểu patterns hiện tại 4. Kiểm tra package.json vềexact versions Tính năng cần implement: [môtả ] Ràng buộc: Phải nhất quán với patterns hiện có"
```

## 13.5 bmad-document-project  -  auto-document legacy codebase

bmad-document-project

## Tài liệu chính thức:

"Với các dự án phức tạp, cân nhắc dùng workflow bmad-document-project. Nócung cấp các runtime variants sẽ quét toàn bộ dự án và document trạng thái hiện tại thực tếcủa nó."

## Tại sao "trạng thái thực tế "?

Điểm khác biệt quan trọng: Tool này document từ CODE THỰC TẾ , không phải từ tài liệu cũ (cóthể đã lỗi thời).

Legacy codebase thường có:

README nói một đằng, code làm một nẻo Architecture docs từ ba năm trước không phảnánh refactoring đã xảy ra API docs thiếu endpoints mới được thêm vào

bmad-document-project đọc code và tạo documentation phảnánh what the system actually does right now -  không phảiý định ban đầu, không phải docs cũ.

## Đầu ra

Tài liệu comprehensive trong thưmục docs/ :

Tổng quan kiến trúc hệthống (từ code thực tế ) Luồng dữ liệu (traced từ code) Hợp đồng API (generated từ routes/endpoints) Business rules được nhúng trong code Điểm tích hợp với services bên ngoài

## Khi nào dùng