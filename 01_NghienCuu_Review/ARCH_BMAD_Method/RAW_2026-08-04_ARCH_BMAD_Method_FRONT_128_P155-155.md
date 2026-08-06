# HD SOURCE: ARCH_BMAD_Method_FRONT_128_P155-155
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_128
Part Title: NONE
Chapter Title: NONE
Section Title: Tóm tắt chương 13
Chunk Range: Pages 155 to 155
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
# Bước 1: Cài BMad vào dự án hiện cócd /đường/dẫn/đến/dự -án-hiện-cónpx bmad-method install --modules bmm --tools claude-code --yes # Bước 2: Tạo project context tự động bmad-generate-project-context # Bước 3: Review và bổ sung những gìAI bỏ sót # Mở _bmad-output/project-context.md # Thêm: Conventions không visible từ code, team agreements, bài học kinh nghiệm # Bước 4: Lấy hướng dẫn bmad-help Tôi cómột dự án [ngôn ngữ /framework] hiện có. Tôi nên làm gì tiếp theo?
```

## Tóm tắt chương 13

- Thách thức cốt lõi của dự án hiện có: Agents không biết conventions hiện tại → Quyết định không nhất quán
- Ba bước chính thức: Dọn dẹp artifacts cũ → Tạo project context → Lấy hướng dẫn
- Bước 1: Archive hoặc xóa completed planning artifacts  không để cũ lẫn mới gây nhầm lẫn
- Bước 2 (Quan trọng nhất): bmad-generate-project-context -quét codebase → bổ sung những gìAI bỏ sót → "điều lệ " cho mọi agent
- Bước 3: bmad-help -  la bàn sau khi setup
- Quick Flow cho dự án hiện có: Tự động phát hiện tech stack, phân tích patterns, hỏi xác nhận conventions  -  hoàn hảo cho bug fixes và tính năng nhỏ
- Hướng dẫn agents rõ ràng: "Trước khi bắt đầu, hãy đọc..." khi khởi động bất kỳworkflow nào
- `bmad-document-project`: Auto-document từ code thực tế , không phải stale docs  dùng cho legacy codebase không có documentation
- Bốn thói quen duy trì: Cập nhật project-context, archive artifacts, dùng bmad-help, fresh chat per workflow