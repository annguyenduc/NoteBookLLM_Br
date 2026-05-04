---
name: wiki-query
description: "TRIGGER: query wiki, ask wiki, retrieve knowledge, answer from wiki, synthesize pages. Truy xuất tri thức từ Wiki NoteBookLLM_Br với source integrity và query standardization. Use for answering questions from existing wiki pages. Do not use for ingest or lint."
---

# Wiki Query Protocol (Local Version)

This skill overrides the global query behavior to ensure accurate retrieval and compounding of knowledge in NoteBookLLM_Br.

## Search & Retrieval Cascade
1. **Search Index**: Read `3-resources/wiki/index.md` first.
2. **Read Wiki Pages**: Follow `[[wikilinks]]` to related concepts/entities.
3. **Verify Raw (Rule 14)**: Khi trả lời các câu hỏi quan trọng, BẮT BUỘC mở file raw trong `3-resources/raw/sources/` để đối soát sự thực.
    - Không trả lời từ trí nhớ LLM nếu Wiki không có thông tin.
    - Nếu không thấy trong hệ thống → ghi `[KHÔNG TÌM THẤY NGUỒN]`.

## Response Standard
- Sử dụng `[[wikilinks]]` cho mọi tham chiếu.
- Cấu trúc câu trả lời theo yêu cầu: Bảng so sánh (Comparison), Danh sách (List), hoặc Diễn giải (Narrative).

## Compounding Valuable Answers (Rule 19)
Nếu câu trả lời có giá trị bồi đắp tri thức lâu dài (synthesis, research mới):
1. **Save to Wiki**: Tạo file mới trong `3-resources/wiki/queries/` hoặc `wiki/synthesis/`.
2. **Prefix Standard**: Dùng prefix `QUERY_` và tuân thủ `d:\NoteBookLLM_Br\.agent\skills\wiki-query\resources\QUERY_template.md`.
3. **Metadata**: Bắt buộc có `type: query`, `title`, `tags`, `related`, `source_tool`.

## Logging
Ghi nhận mọi lần bồi đắp tri thức vào `3-resources/wiki/log.md`.
- PowerShell: Bắt buộc thêm `-Encoding UTF8`.

## Related Rules
- **Rule 14**: Source Integrity.
- **Rule 19**: Query Standardization.
- **Rule 3**: Knowledge Compounding.
