# Analysis: AIMET_wiki-gen-skill.md (Skill Check Re-ingest)
**Nguồn**: `3-resources/raw/sources/AIMET_wiki-gen-skill.md`
**Phân tích bởi**: @scout | **Ngày**: 2026-05-02

## Mining Stats
| Chỉ số | Số lượng |
|:---|:---:|
| Key Concepts phát hiện | 17 |
| Entities phát hiện | 1 |
| Connections với wiki hiện tại | 19 |
| Atoms đề xuất tạo mới | 3 |

## Tóm tắt cốt lõi
- Vòng re-ingest trước đã phủ tốt các khối `absorb`, `cleanup`, `query`, `breakdown`, `status`, `taxonomy`, `tone`, `granularity`, `narrative`, và `index/backlinks`.
- Các phần còn thiếu rõ nhất trong source hiện tại nằm ở `reorganize`, `quote discipline`, và `length targets`.
- Local skill `wiki-ingest` đã lộ một mismatch thật: `SKILL.md` yêu cầu `--scan` nhưng helper chưa hỗ trợ; vòng này đã vá helper để workflow skill chạy khớp thực tế.
- Tài liệu nguồn không chỉ dạy “cách viết” mà còn cung cấp các ngưỡng vận hành cụ thể để kiểm soát việc tái cấu trúc wiki và độ dài bài viết.
- Đợt này phù hợp để kiểm tra skill mới theo đúng chu trình: guide + template + raw + scan + ingest + finalize.

## Atoms đề xuất

### Concepts (wiki/concepts/)
- [x] `CONCEPT_META_Wiki_Reorganization.md` — Tư duy tái tổ chức wiki ở cấp cấu trúc sống: merge, split, reclassify, rename và rebuild.
- [x] `CONCEPT_META_Wiki_Quote_Discipline.md` — Quy tắc kiểm soát trích dẫn trực tiếp để giữ article voice trung tính và tránh lạm dụng quote.
- [x] `CONCEPT_META_Wiki_Article_Length_Targets.md` — Bộ ngưỡng độ dài theo type để cân bằng anti-cramming và anti-thinning.

### Entities (wiki/entities/)
- [ ] Không đề xuất entity mới. `ENTITY_TOOL_Claude_Code_Wiki_Gen.md` vẫn bao quát thực thể công cụ.

### Source Summary (wiki/sources/)
- [x] `SOURCE_META_WIKI_GEN_CLONE.md` — cập nhật coverage để phản ánh 3 atom mới.

## Connections với Wiki hiện tại
- `[[CONCEPT_META_Wiki_Index_Synchronization]]` — `reorganize` phụ thuộc vào lớp đồng bộ index/backlinks sau khi tái cấu trúc.
- `[[CONCEPT_META_Wiki_Granularity_Control]]` — `length targets` là lớp ngưỡng định lượng cụ thể hóa anti-cramming và anti-thinning.
- `[[CONCEPT_META_Wiki_Writing_Tone]]` — `quote discipline` là lớp kiểm soát giọng văn nằm bên trong writing standards.
- `[[CONCEPT_META_Wiki_Directory_Taxonomy]]` — `reorganize` là thao tác vận hành trên taxonomy sống.
- `[[CONCEPT_META_Wiki_The_Steve_Jobs_Test]]` — thường là heuristic dùng trong cleanup và reorganize để quyết định khi nào cần viết lại cấu trúc bài.

## Mâu thuẫn (Contradictions & Tensions)
- `SKILL.md` của local skill mô tả `--scan`, nhưng helper gốc chưa có flag đó; đây là mismatch đã được xác nhận bằng tool call.
- Source gốc xem `reorganize` là command riêng, trong khi repo hiện mới rải tri thức tái cấu trúc giữa nhiều concept khác nhau.
- `length targets` được nêu như ngưỡng thực hành, nhưng repo hiện chưa có một atom riêng để làm chuẩn review.

## Master Files cần bồi đắp (Rule 3)
- `3-resources/wiki/sources/SOURCE_META_WIKI_GEN_CLONE.md` — mở rộng danh sách concept đã trích xuất.
- `3-resources/wiki/index.md` — tái tạo để nhận diện các atom mới.

## Câu hỏi đào sâu (Deep Research Queries)
- Có nên tách thêm một atom riêng cho `The Golden Rule` như thesis-level principle của toàn bộ wiki-gen system không?
- Có nên đưa `length targets` vào lint rule hoặc audit script để tự cảnh báo bài quá ngắn/quá dài?
- Có nên mở rộng helper `--scan` để phát hiện file raw chưa ingest thay vì chỉ báo thống kê wiki?

## Ghi chú thực thi
- Vòng này dùng local skill `wiki-ingest` làm đối tượng kiểm tra thực chiến, không chỉ ingest nội dung nguồn.
- User request được dùng như approval cho một vòng skill-check end-to-end thay vì dừng sau analysis.
