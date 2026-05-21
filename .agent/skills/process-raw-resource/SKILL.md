---
name: process-raw-resource
description: "Use when the user wants source-preview behavior: preview, triage, or learn quickly from a local source before official ingest. Kích hoạt khi user nói kiểu đọc nhanh, tóm tắt nhanh, có đáng học không, có nên ingest không, preview tài liệu, learning map, quick summary, keyword, câu hỏi chính, hoặc khi một file trong 00_Inbox/ hay một local source cần đi qua một lượt PREVIEW_ONLY. Do NOT use for /ingest, official ingest, atom creation, audit promotion, index rebuild, or any request to write into 3-resources/ or wiki/."
---

# Process Raw Resource

## Overview

Skill này được hạ vai thành `source-preview`: đường nhẹ của workspace để đọc nhanh và quyết định có nên ingest chính thức không.

Mục tiêu:
- giúp AN biết tài liệu có đáng học hay không
- tạo bức tranh học nhanh trước khi vào ingest chính thức
- đưa ra khuyến nghị `SKIP | KEEP_SUMMARY | INGEST_OFFICIAL`

Skill này không phải ingest pipeline.
Skill này không tạo Atom.
Skill này không cấp `VERIFIED`.
Skill này không cấp `SYNTHESIZED`.
Skill này không được coi output là tri thức canonical.

Nếu user muốn đưa source vào vault chính thức, handoff sang workflow `ingest-lifecycle`.
Nếu user dùng slash command `/ingest [file]`, không dùng skill này.

## Mô hình đọc 4 tầng

Đây là mô hình đọc và nén ngữ cảnh, không phải workflow riêng.
Nó chỉ hướng dẫn agent đọc đến mức đủ dùng, rồi dừng.

### Tầng 1 — Tín hiệu nhanh

Đọc các tín hiệu rẻ trước:
- tên file
- loại nguồn
- metadata dễ thấy
- mục lục
- heading lớn
- mở bài / kết luận

Mục tiêu: xác định tài liệu đang nói về gì và có đáng đọc tiếp không.

### Tầng 2 — Cấu trúc và luận điểm chính

Đọc các phần đại diện:
- section mở đầu
- section tóm tắt
- các heading quan trọng
- vài đoạn tiêu biểu ở giữa tài liệu

Mục tiêu: dựng được khung tham chiếu, luận điểm chính, và giá trị học tập sơ bộ.

### Tầng 3 — Mở rộng có chọn lọc

Chỉ đọc sâu thêm ở những phần cần để trả lời:
- câu hỏi chính tài liệu đang giải quyết
- đoạn có mật độ ý cao
- phần có số liệu, framework, hoặc định nghĩa quan trọng

Mục tiêu: đủ để đưa ra `learning_status`, `ingest_recommendation`, và `confidence`.

### Tầng 4 — Đọc sâu khi thật sự cần

Chỉ dùng khi ba tầng trên chưa đủ.

Ví dụ:
- tài liệu khó, mơ hồ, hoặc nhiều thuật ngữ
- cần xác định tài liệu có thực sự đáng ingest không
- user yêu cầu phân tích kỹ hơn preview thường

Mục tiêu: hoàn tất preview tốt hơn, không biến preview thành ingest.

## Workflow

### 1. Xác định đúng lane

Dùng skill này khi:
- user mới tải tài liệu về và muốn đọc nhanh
- user chưa biết tài liệu có đáng giữ lâu dài không
- user cần quick summary, keyword, learning questions, khung tham chiếu
- user muốn một learning map trước khi quyết định ingest

Không dùng skill này khi:
- user đã yêu cầu official ingest
- user cần `source_id`, naming lock, source trace, audit stamp
- user muốn tạo `CONCEPT_`, `ENTITY_`, `SOURCE_`, `COMPARE_`, `QUERY_`
- user muốn ghi vào `3-resources/` hoặc `3-resources/wiki/`

### 2. Chọn chế độ output

Mặc định runtime: trả kết quả trong chat, không ghi file.

Preview artifact writing is allowed only when the user request or workflow explicitly asks for a persisted preview artifact.
Trong một implementation goal đã được approve, Codex không hỏi thêm xác nhận giữa chừng cho các thay đổi nằm trong scope.

Hai chế độ hợp lệ:
- `CHAT_ONLY`: tóm tắt và khuyến nghị trong chat
- `WRITE_PREVIEW_ARTIFACT`: tạo preview markdown không-canonical để AN xem lại

### 3. Đọc tối thiểu, không đọc quá tay

Đọc theo nguyên tắc tiết kiệm context:
- ưu tiên metadata, mục lục, section headings, opening/closing sections
- với tài liệu lớn, ưu tiên structure-first thay vì đọc hết ngay
- chỉ đọc thêm khi thông tin hiện có chưa đủ để đưa ra khuyến nghị

Nếu source là web/video/audio:
- ưu tiên local artifact, transcript, hoặc bản lưu đã stage
- nếu chỉ có live source, phải nói rõ rủi ro mutability và auditability

### 4. Trích xuất preview

Trích xuất các trường sau:
- `quick_summary`: 3-8 câu
- `keywords`: 5-15 từ khóa
- `atomic_claims`: 3-10 mệnh đề ngắn
- `main_questions`: 5-10 câu hỏi mà tài liệu trả lời
- `reference_frame`: tài liệu nằm trong khung nào
- `learning_value`: tài liệu giúp học cái gì
- `signals`: lý do nên đọc kỹ hoặc bỏ qua

Nếu cần, có thể thêm:
- `notable_sections`
- `unknowns`
- `followup_questions`

### 5. Đưa ra quyết định intake

Skill phải bắt đầu output bằng `ROUTING_DECISION`, rồi kết thúc bằng output contract sau.

Ví dụ route cho prompt `Tóm tắt PDF này để tôi học nhanh`:

```yaml
ROUTING_DECISION:
  cwd_context: "vault_root | workspace_child"
  selected_workspace: "workspaces/learning | workspaces/source-lab"
  mode: "learning-first | source-preview"
  reason: "[why this route was selected]"
  loaded_overlay: "workspaces/learning/AGENTS.md | workspaces/source-lab/AGENTS.md | NONE"
  action_type: "read-only/chat-only | write-preview-artifact"
  write_artifact: "NO | YES"
  canonical_write: "NO"
  ingest_lifecycle: "NO"
  forbidden_actions_checked:
    - "no 3-resources write"
    - "no Atom generation"
    - "no VERIFIED/SYNTHESIZED"
    - "no ingest-lifecycle"
```

Sau đó mới xuất:

```yaml
SOURCE PREVIEW REPORT:
  artifact_type: "source_document"
  source_input: "[path]"
  learning_status: "PREVIEW_ONLY"
  canonical_status: "NON_CANONICAL"
  source_id: "NONE"
  write_artifact: "NO | YES"
  ingest_recommendation: "SKIP | KEEP_SUMMARY | INGEST_OFFICIAL"
  confidence: "LOW | MEDIUM | HIGH"
  reason:
    - "tại sao đề xuất như vậy"
  next_step:
    - "hành động tiếp theo cho AN"
```

Giải thích ngắn gọn:
- `SKIP`: tài liệu ít giá trị, trùng lặp, hoặc không hợp mục tiêu học
- `KEEP_SUMMARY`: nên giữ lại preview/learning map, nhưng chưa cần ingest
- `INGEST_OFFICIAL`: đủ quan trọng để vào lifecycle chính thức

### 6. Nếu workflow/user text yêu cầu ghi preview artifact

Chỉ áp dụng khi user request hoặc workflow text yêu cầu persisted preview artifact.

Preview artifact phải rõ ràng là không-canonical:
- không đặt trong `3-resources/`
- không đặt trong `3-resources/wiki/`
- không dùng tên dễ nhầm với lifecycle artifact như `SOURCE_*`, `INGEST_*`, `MAP_[ID]`, `NAMING_LOCK_[ID]`
- không đặt cạnh original source nếu original đang nằm dưới `raw_*`

Vị trí ưu tiên:
- `00_Inbox/preview/` cho preview tạm thời trước quyết định ingest
- `1-projects/learning_maps/` cho tài liệu giữ để học

Tên file ưu tiên:
- `PREVIEW_[safe_stem]_YYYYMMDD.md`
- `QUICK_INDEX_[safe_stem]_YYYYMMDD.md`

Không tạo:
- `QUICK_INDEX.md`
- `index.md`
- `PREVIEW_REGISTRY.md`

Nội dung tối thiểu:

```md
# [title]

## Status
- learning_status: PREVIEW_ONLY
- canonical_status: NON_CANONICAL
- source_id: NONE
- ingest_recommendation: SKIP | KEEP_SUMMARY | INGEST_OFFICIAL
- confidence: LOW | MEDIUM | HIGH

## Quick Summary

## Keywords

## Atomic Claims

## Main Questions

## Reference Frame

## Learning Value

## Recommendation Reasoning

## Suggested Next Step
```

### 7. Handoff sang ingest khi cần

Nếu đề xuất là `INGEST_OFFICIAL`, không tự nhảy vào ingest.

Phải nói rõ:
- tài liệu này đang ở lane preview
- nếu AN muốn vào lane canonical thì dùng `ingest-lifecycle`
- official ingest vẫn phải đi qua full chain:
  `prepare-source -> audit-promote-source -> lock-ingest-input -> ingest -> ingest-generate -> ingest-index-log`

## Guardrails

- Không cập nhật `index.md` của workspace chỉ vì đã preview một tài liệu.
- Không cập nhật `3-resources/wiki/index.md`.
- Không tạo hoặc cập nhật skill khác từ output của tài liệu.
- Không ghi vào `3-resources/raw_*`.
- Không ghi vào `3-resources/wiki/*`.
- Không tạo `source_id`.
- Không tạo lifecycle artifact như `SOURCE_PREP_REPORT_*`, `SOURCE_AUDIT_REPORT_*`, `INGEST_INPUT_LOCK_*`.
- Không tạo `MAP_[ID]` hoặc `NAMING_LOCK_[ID]`.
- Không tạo Atom files.
- Không dùng output preview làm bằng chứng để pass ingest gates.
- Không tạo summary cạnh original source nếu source nằm dưới `raw_*`.
- Nếu source đã có lifecycle artifact canonical, không được để preview artifact cạnh tranh vai trò `primary_ingest_file`.
- Nếu naming drift giữa title, raw stem, và lifecycle anchor xuất hiện, phải báo `BLOCKED` thay vì tự đặt lại tên.

## Quick Reference

Dùng skill này cho:
- "Đọc nhanh file này"
- "Tóm tắt để xem có đáng học không"
- "Cho tôi learning map của tài liệu này"
- "Tài liệu này có nên ingest không?"

Không dùng skill này cho:
- "/ingest [file]"
- "tạo atom"
- "promote vào raw_ingest"
- "audit source này"
- "rebuild wiki"

## Common Mistakes

- Biến preview thành mini-ingest.
- Viết preview artifact vào `3-resources/`.
- Tự tạo `source_id` dù user mới yêu cầu tóm tắt nhanh.
- Tạo `summary.md` rồi coi nó là ingest fuel chính thức.
- Tự động cập nhật index, graph, hoặc skill registry dù user chỉ muốn học nhanh.
- Tạo global `QUICK_INDEX.md` khiến nhiều source cạnh tranh một registry.
- Đọc hết tài liệu lớn ngay từ đầu thay vì structure-first.
