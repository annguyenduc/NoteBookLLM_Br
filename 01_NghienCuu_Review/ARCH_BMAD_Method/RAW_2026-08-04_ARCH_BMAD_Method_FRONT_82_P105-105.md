# HD SOURCE: ARCH_BMAD_Method_FRONT_82_P105-105
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_82
Part Title: NONE
Chapter Title: NONE
Section Title: Quick dev trong ngữ cảnh dự án hiện cóChunk Range: Pages 105 to 105
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Nguyên tắc 2  -  Chọn đường đi an toàn nhỏnhất:

Oneshot: Rõ ràng, xác định, ít rủi ro → triển khai toàn bộtrong một lần Đường đi đầy đủ hơn: Phức tạp hơn, nhiều rủi ro hơn → cần checkpoints

## Nguyên tắc 3  -  Chạy lâu hơn tựchủ hơn:

Sau khi đã chọn đường đi, giảm tần suất giám sát. Trust AI để hoạt động trong những ranh giới đã xác định.

## Nguyên tắc 4  -  Chẩn đoán đúng layer:

Khi có vấn đề, xác định vấn đề ở layer nào:

Ý định? (Spec không rõ ràng) Spec? (Cần cụthể hơn) Triển khai? (AI cần hướng dẫn cụthể

)

## Nguyên tắc 5  -  Giảm tối thiểu human-in-the-loop:

Chỉ quay lại yêu cầu giám sát con người tại các điểm thực sự quan trọng  -  khi có quyết định không thể đảo ngược hoặc khi scope mở rộng đáng kể .

## Khi nào dùng quick dev

## Phù hợp:

Bug fix với nguyên nhân gốc rễ đã biết rõ Tính năng nhỏ với requirements hoàn toàn rõ ràng Scripts và công cụmột lần Refactoring trong phạm vi xác định Configuration changes

## Không phù hợp:

Dự án nhiều epics cần phối hợp Khi cóyêu cầu chưa rõ ràng Tính năng cần quyết định kiến trúc Khi cần compliance vàaudit trail

## Quick dev trong ngữ cảnh dự án hiện cóTài liệu chính thức khẳng định: