# Analysis: AIMET_wiki-gen-skill.md (Re-ingest)
**Nguồn**: `3-resources/raw/sources/AIMET_wiki-gen-skill.md`
**Phân tích bởi**: @pm | **Ngày**: 2026-05-02

## Mining Stats
| Chỉ số | Số lượng |
|:---|:---:|
| Key Concepts phát hiện | 14 |
| Entities phát hiện | 1 |
| Connections với wiki hiện tại | 16 |
| Atoms đề xuất tạo mới | 3 |

## Tóm tắt cốt lõi
- Tài liệu mô tả một giao thức wiki mang tính vận hành đầy đủ, không chỉ là prompt viết bài mà là hệ điều hành cho ingest, absorb, query, cleanup, breakdown, rebuild-index và status.
- Cụm concept hiện có đã bao phủ tốt các phần `absorb`, `taxonomy`, `writing tone`, `narrative`, `granularity`, `query`, `breakdown`, và `concurrency`.
- Khoảng trống lớn nhất còn lại nằm ở 3 lệnh vận hành cấp hệ thống: `cleanup`, `rebuild-index`, và `status`.
- Nguồn này cũng nhấn mạnh rằng `_index.md` và `_backlinks.json` không chỉ là artifact phụ, mà là lớp hạ tầng cho query, audit và đồng bộ graph.
- Workflow hiện tại của workspace thiếu `3-resources/WIKI_AGENT_GUIDE.md` và `3-resources/SOURCE_TEMPLATE.md`, nên re-ingest cần dựa vào schema sống từ các file `SOURCE_` và `CONCEPT_` đang tồn tại.

## Atoms đề xuất

### Concepts (wiki/concepts/)
- [x] `CONCEPT_META_Wiki_Cleanup_Audit.md` — Chu trình audit và enrich toàn wiki bằng kiểm tra cấu trúc, tone, links và missing pages.
- [x] `CONCEPT_META_Wiki_Index_Synchronization.md` — Cơ chế đồng bộ `_index.md` và `_backlinks.json` để duy trì khả năng query và tính nhất quán của graph.
- [x] `CONCEPT_META_Wiki_Status_Metrics.md` — Bộ chỉ số vận hành để đọc “sức khỏe” của wiki sống: absorbed, category spread, central pages, orphans, pending.

### Entities (wiki/entities/)
- [ ] Không đề xuất entity mới. `ENTITY_TOOL_Claude_Code_Wiki_Gen.md` đã bao quát thực thể công cụ.

### Source Summary (wiki/sources/)
- [x] `SOURCE_META_WIKI_GEN_CLONE.md` — cập nhật coverage để phản ánh 3 atom mới.

## Connections với Wiki hiện tại
- `[[CONCEPT_META_Wiki_Absorption_Loop]]` — nền tảng của pha absorb, đối ứng với cleanup như một vòng phản tư sau ingest.
- `[[CONCEPT_META_Wiki_Query_Patterns]]` — phụ thuộc vào chất lượng `_index.md` và `_backlinks.json`.
- `[[CONCEPT_META_Wiki_Concurrency_Safety]]` — đã chạm tới “finalize sync”, nhưng chưa tách riêng lớp hạ tầng index/backlinks.
- `[[CONCEPT_META_Wiki_The_Steve_Jobs_Test]]` — là heuristic con nằm bên trong quy trình cleanup.
- `[[CONCEPT_META_Wiki_Signals]]` — có liên hệ với `status`, nhưng chưa biểu diễn dashboard vận hành của toàn wiki.

## Mâu thuẫn (Contradictions & Tensions)
- Tài liệu nguồn giả định tồn tại `3-resources/WIKI_AGENT_GUIDE.md` và `3-resources/SOURCE_TEMPLATE.md`, nhưng workspace hiện tại không còn hai file này.
- Source gốc mô tả `_index.md` và `_backlinks.json` như cặp artifact trung tâm, trong khi repo hiện mới duy trì `index.md` và chưa có `_backlinks.json` thực thi.
- Một phần tri thức của `AIMET_wiki-gen-skill.md` hiện được giữ trong `ENTITY_TOOL_Claude_Code_Wiki_Gen.md` dưới dạng bảng lệnh, chưa được tách hết thành concept atoms.

## Master Files cần bồi đắp (Rule 3)
- `3-resources/wiki/sources/SOURCE_META_WIKI_GEN_CLONE.md` — mở rộng danh sách concept đã trích xuất.
- `3-resources/wiki/index.md` — tái tạo để nhận diện các atom mới.

## Câu hỏi đào sâu (Deep Research Queries)
- Có nên chuẩn hóa `index.md` hiện tại thành mô hình có alias/backlinks như tài liệu nguồn mô tả không?
- Nếu triển khai `_backlinks.json`, script nào nên là nguồn chân lý: `update_wiki_index.py` hay một tool riêng?
- Có nên tách thêm một atom riêng cho `reorganize` như lớp meta-refactor của wiki?

## Ghi chú thực thi
- User đã yêu cầu “ingest thêm một lần nữa”, nên vòng này được xem là approval để thực hiện re-ingest tối thiểu an toàn.
- Do thiếu 2 prerequisite file chuẩn, vòng này dùng “schema sống” từ các file hiện hữu thay cho template gốc.
