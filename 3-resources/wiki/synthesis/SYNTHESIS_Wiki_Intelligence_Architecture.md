---
file_id: SYNTHESIS_Wiki_Intelligence_Architecture
title: "SYNTHESIS: Wiki Intelligence Architecture V3.0 (Master Blueprint)"
type: synthesis
kwsr_type: "knowledge"  # knowledge | workflow | skill | rule
status: VERIFIED
tags: 
  - "Architecture"
  - "System-Design"
ai-first: true
confidence: 1.0
last_reconciled: 2026-05-08
created: 2026-05-02
last_updated: 2026-05-08
sources:
  - "[[log_2026_05_08]]"
---

# Wiki Intelligence Architecture (Bản thiết kế Hệ thống Wiki Thông minh)

## 1. Tổng quan kiến trúc
Hệ thống Wiki Intelligence 2.0 được thiết kế như một **Cơ thể sống** có khả năng tự hấp thụ, tự làm sạch và tự phát triển. Kiến trúc này không chỉ lưu trữ thông tin mà còn lưu trữ cả **Mạch truyện (Narrative)** và **Lập luận (Reasoning)** đằng sau thông tin đó.

## 2. Các Module lõi (Core Modules)

### A. Module Ingest (Cửa ngõ tri thức)
- **Chức năng**: Chuyển đổi dữ liệu thô (`raw/`) thành các Entry Markdown có cấu trúc.
- **Quy tắc chi phối**: [[CONCEPT_META_Wiki_Directory_Taxonomy]] (Phân loại thư mục) và [[CONCEPT_META_Wiki_Granularity_Control]] (Kiểm soát độ hạt).
- **Trạng thái**: Cần chuẩn hóa script `ingest.py`.

### B. Module Absorption (Vòng lặp Hấp thụ)
- **Chức năng**: Rewrite và tích hợp các Entry mới vào các bài viết hiện có.
- **Tiêu chuẩn**: [[CONCEPT_META_Wiki_Narrative_Coherence]] (Tính mạch lạc) và [[CONCEPT_META_Wiki_The_Steve_Jobs_Test]] (Cấu trúc Wikipedia-style).
- **Quy trình**: [[CONCEPT_META_Wiki_Absorption_Loop]].

### C. Module Intelligence (Truy vấn & Phân tích)
- **Chức năng**: Trả lời câu hỏi và phát hiện lỗ hổng tri thức.
- **Công nghệ**: CONCEPT_META_Wiki_Query_Patterns và [[CONCEPT_META_Wiki_Gap_Analysis]].
- **Hành động**: `/wiki query` và `/wiki query --gap`.
- **Phân biệt với Mining**: Khác với Breakdown (chia tách dữ liệu), Module này tập trung vào **Logic** và **Sự nhất quán** (tìm điểm hụt trong lập luận).

### D. Module Mining & Breakdown (Khai thác & Chia tách)
- **Chức năng**: Đào bới các thực thể mới và chia nhỏ bài viết.
- **Công nghệ**: [[CONCEPT_META_Wiki_Breakdown_Mining]] (Concrete Noun Test).
- **Hành động**: `/wiki breakdown`.
- **Phân biệt với Intelligence**: Tập trung vào **Cấu trúc** và **Độ hạt** (tìm danh từ chưa có trang hoặc bài viết quá dài).

### E. Module Maintenance (Bảo trì & Audit)
- **Chức năng**: Sửa link, chuẩn hóa Tone, và đồng bộ Index.
- **Quy tắc**: [[CONCEPT_META_Wiki_Concurrency_Safety]] và [[CONCEPT_META_Wiki_Index_Synchronization]].
- **Hành động**: `/wiki cleanup` và `/wiki rebuild-index`.

## 3. Tiêu chuẩn viết lách (Writing Standards)
Mọi output của hệ thống phải tuân thủ:
- **Tone**: [[CONCEPT_META_Wiki_Writing_Tone]] (Khách quan, không mỹ từ).
- **Nguồn**: [[CONCEPT_META_Wiki_Quote_Discipline]] (Hạn chế trích dẫn trực tiếp quá dài).
- **Độ dài**: [[CONCEPT_META_Wiki_Article_Length_Targets]] (Tùy biến theo loại bài viết).

## 4. Kế hoạch chuẩn hóa Skills (Standardization Plan)

| Skill Module | Lệnh tương ứng | Trọng tâm chuẩn hóa (Standardization Focus) |
||---|
| **`wiki-ingest`** | `/wiki ingest` | **Parsing**: Tự động gán Taxonomy và tách Atom từ nguồn thô (JSON, CSV, MD). |
| **`wiki-absorb`** | `/wiki absorb` | **Synthesis**: Áp dụng Rewrite Engine để tích hợp tri thức vào các trang hiện có. |
| **`wiki-query`** | `/wiki query` | **Discovery**: Truy vấn đồ thị (Graph Traversal) và tổng hợp đa nguồn. |
| **`wiki-cleanup`** | `/wiki cleanup` | **Quality**: Thực hiện "Steve Jobs Test", sửa link và chuẩn hóa Tone Wikipedia. |
| **`wiki-breakdown`** | `/wiki breakdown`| **Mining**: Phát hiện lỗ hổng tri thức bằng "Concrete Noun Test". |
| **`wiki-status`** | `/wiki status` | **Metrics**: Đo lường mật độ liên kết, tỷ lệ hấp thụ và sức khỏe hệ thống. |
| **`wiki-index`** | `/wiki rebuild` | **Synchronization**: Đồng bộ hóa `_index.md` và `_backlinks.json`. |

## 5. Phản tư sư phạm (4F)
- **Facts**: Chúng ta đã có đủ các "nguyên tử" lý thuyết mạnh nhất từ Karpathy và Nashsu.
- **Feelings**: Thấy tự tin vì hệ thống có cấu trúc logic rất chặt chẽ.
- **Findings**: Khó khăn lớn nhất không nằm ở việc lưu file, mà nằm ở việc **Rewrite** để giữ mạch truyện (Narrative).
- **Futures**: Ưu tiên xây dựng `wiki_engine_core.py` để làm thư viện dùng chung cho tất cả các skill.

## 6. Trích dẫn nguồn
- **Nguồn**: [[SOURCE_META_WIKI_GEN_CLONE]] — Toàn bộ tài liệu.
- **Nguồn**: [[SOURCE_META_LLM_WIKI_V2]] — Tầng hợp nhất (Consolidation Tiers).


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: