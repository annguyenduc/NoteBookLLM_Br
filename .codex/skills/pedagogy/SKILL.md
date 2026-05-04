---
name: pedagogy
description: "TRIGGER: pedagogy, lesson design, curriculum, learning activity, EdTech extraction. Quy trình thiết kế sư phạm và trích xuất tri thức EdTech cho NoteBookLLM_Br. Use for teaching design, learning sequence, and pedagogical synthesis. Do not use for generic wiki maintenance."
---

# Pedagogy Protocol

Dùng để thiết kế bài giảng, học liệu và trích xuất tri thức từ các nguồn tài liệu sư phạm.

## Rule 16: EXTRACTION_MANDATORY_STATS
Mọi tệp tin trung gian trong `1-projects/[Project]/` PHẢI dùng cấu trúc từ:
`d:\NoteBookLLM_Br\.agent\skills\pedagogy\resources\PROCESS_TEMPLATE.md`.

Bắt buộc có **Bảng thống kê hiệu suất Khai thác (Mining Stats)** ở đầu file.

## Rule 11: Pedagogical Pipeline
Tuân thủ trình tự các bước:
1. `@profiler`: Tạo Trainer Profile.
2. `@designer`: Thiết kế Learning Design.
3. `@engineer`: Viết bài giảng/Code.
4. `@evaluator`: Đánh giá.

## Related
- `wiki-ingest`
- `wiki-query`
