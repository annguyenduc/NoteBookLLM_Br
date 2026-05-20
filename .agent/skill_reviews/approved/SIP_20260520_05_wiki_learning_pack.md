# SKILL_IMPROVEMENT_PROPOSAL

```yaml
proposal_id: SIP_20260520_05
skill_id: wiki-learning-pack
current_version: "unversioned / [READ_FROM_SKILL_MD - no version field]"
proposed_version: "0.1.0 (initially versioned)"
source_run_id: manual
trigger: user_correction
severity: medium
approval_required: true
```

## Evidence
- **Báo cáo thực nghiệm vật lý:** Xem bằng chứng đo lường Token và Trigger tại [EVAL_REPORT_20260520.md](file:///d:/NoteBookLLM_Br/.agent/skill_reviews/EVAL_REPORT_20260520.md).
- **File hiện tại:** [wiki-learning-pack/SKILL.md](file:///d:/NoteBookLLM_Br/.agent/skills/wiki-learning-pack/SKILL.md)
- **Bối cảnh:** Frontmatter cũ chỉ gồm `name` và `description`. Hành vi mặc định cũ tạo cảm giác output luôn được ghi đè vào thư mục `3-resources/wiki/learning_packs/` gây rủi ro thay đổi wiki vault âm thầm.

## Problem
- **Rủi ro tự ý tạo artifact:** Agent dễ hiểu lầm rằng nhiệm vụ của skill là luôn tự động ghi tệp tóm tắt lộ trình vào wiki vault mà không hỏi ý kiến người dùng.
- **Thiếu cấu hình an toàn runtime:** Chưa khai báo `default_runtime: chat_only` và `optional_artifact` để phân tách rõ ràng giữa "Đề xuất hiển thị" (chat proposal) và "Ghi file vật lý".

## Proposed Change (diff format)
```diff
---
 name: wiki-learning-pack
 description: Use when the user wants to learn quickly from existing Wiki atoms, create a fast-start learning pack from a topic or source_id, turn indexed atoms into a 60-90 minute self-study path, or build a structured review path before drills or pedagogy. Do NOT use for ingest, atom creation, final synthesis, PDF conversion, slide decks, lesson plans, or vault maintenance.
+triggers:
+  - "wiki-learning-pack"
+  - "học nhanh"
+  - "tự học"
+od:
+  preview:
+    type: markdown
+  capabilities_required:
+    - chat_proposal
+  outputs:
+    optional_artifact: "3-resources/wiki/learning_packs/"
+nbllm:
+  domain: learning
+  default_runtime: chat_only
+  requires_an_go_for_write: true
 ---
```

## Regression Case
- **Regression Case 1 (Chat-Only Proposal - Mặc định):**
  - **Input:** "mình muốn học nhanh các khái niệm cơ bản về lập trình hàm trong 60 phút"
  - **Expected:** Khớp trigger `"học nhanh"`. Agent tiến hành tổng hợp lộ trình tự học và hiển thị trực tiếp nội dung qua cửa sổ chat (chat proposal). Tuyệt đối không ghi hay tạo bất kỳ file nào trong `3-resources/` (read-only và chat-only).
- **Regression Case 2 (Optional Artifact Save with AN Gate):**
  - **Input:** "tạo file learning pack cho OOP và lưu lại vào thư mục learning_packs"
  - **Expected:** Nhận diện yêu cầu ghi file vật lý. Agent dừng lại, xin quyền ghi từ AN. Chỉ khi AN duyệt Approve + GO mới thực hiện tạo và lưu tệp vào `3-resources/wiki/learning_packs/`.

## Risk
- **Low:** Có chốt an toàn `requires_an_go_for_write: true` và định vị rõ `optional_artifact` giúp triệt tiêu hoàn toàn rủi ro ghi file tự động ngoài ý muốn.

## AN Decision
- [x] Approve + GO → agent apply patch theo surgical diff
- [ ] Reject → lý do: ___
- [ ] Defer → review lại sau: ___

## Implementation Note
- Sau khi apply lần đầu, `quick_validate.py` báo top-level keys `triggers`, `od`, `nbllm` không thuộc schema cho phép. Production frontmatter đã được chỉnh tương thích bằng cách đặt toàn bộ extension dưới `metadata:`; nội dung metadata không đổi.
