# SKILL_IMPROVEMENT_PROPOSAL

```yaml
proposal_id: SIP_20260520_03
skill_id: wiki-semantic-search
current_version: "unversioned / [READ_FROM_SKILL_MD - no version field]"
proposed_version: "0.1.0 (initially versioned)"
source_run_id: manual
trigger: user_correction
severity: low
approval_required: true
```

## Evidence
- **Báo cáo thực nghiệm vật lý:** Xem bằng chứng đo lường Token và Trigger tại [EVAL_REPORT_20260520.md](file:///d:/NoteBookLLM_Br/.agent/skill_reviews/EVAL_REPORT_20260520.md).
- **File hiện tại:** [wiki-semantic-search/SKILL.md](file:///d:/NoteBookLLM_Br/.agent/skills/wiki-semantic-search/SKILL.md)
- **Bối cảnh:** Frontmatter cũ thiếu triggers đa ngôn ngữ. Khi keyword search thất bại hoặc người dùng hỏi các câu hỏi trừu tượng mang tính ý nghĩa ("các khái niệm liên quan", "tương đương ngữ nghĩa"), Agent dễ tiếp tục chạy `wiki-query` lặp đi lặp lại thay vì chuyển hướng sang vector search.

## Problem
- **Thiếu ranh giới kích hoạt rõ ràng:** Không phân biệt rõ ràng khi nào dùng exact keyword search (`wiki-query`) và khi nào dùng vector search (`wiki-semantic-search`).
- **Trigger mơ hồ:** Từ khóa `"tương đương"` nếu không đặt trong ngữ cảnh cụ thể rất dễ bị hiểu lầm là các lệnh so sánh file hoặc chuyển đổi định dạng.

## Proposed Change (diff format)
```diff
---
 name: wiki-semantic-search
 description: "Use when wiki-query (keyword search) returns no results or irrelevant results, when the search intent is conceptual or abstract rather than exact-match, or when the user asks questions using meaning rather than specific terms."
+triggers:
+  - "wiki-semantic-search"
+  - "ngữ nghĩa"
+  - "tương đương"
+od:
+  preview:
+    type: markdown
+  capabilities_required:
+    - read_file
nbllm:
+  domain: query
+  default_runtime: chat_only
+  requires_an_go_for_write: false
 ---
```

## Regression Case
- **Regression Case 1 (Semantic Search Trigger - Khớp Đúng):**
  - **Input:** "tìm các khái niệm có ý nghĩa tương đương hoặc liên quan tới bất biến trạng thái" hoặc "tìm kiếm ngữ nghĩa bài viết nói về xử lý song song"
  - **Expected:** Phát hiện từ khóa `"tương đương"` hoặc `"ngữ nghĩa"` đi kèm ngữ cảnh tìm kiếm khái niệm. Hệ thống bỏ qua keyword search chính xác của `wiki-query` và kích hoạt `wiki-semantic-search` để quét vector index (QMD).
- **Regression Case 2 (Fuzzy Maintenance Filter - Tránh Nhầm Lẫn):**
  - **Input:** "chuyển đổi tương đương 2 file markdown cũ sang format mới"
  - **Expected:** Nhận thức rõ ràng đây là tác vụ bảo trì/định dạng tệp, không kích hoạt `wiki-semantic-search` tra cứu ngữ nghĩa.

## Risk
- **Low:** Skill này là tác vụ chỉ đọc (read-only vector query) nên không có khả năng gây hư hại hoặc biến đổi dữ liệu vault.

## AN Decision
- [x] Approve + GO → agent apply patch theo surgical diff
- [ ] Reject → lý do: ___
- [ ] Defer → review lại sau: ___

## Implementation Note
- Sau khi apply lần đầu, `quick_validate.py` báo top-level keys `triggers`, `od`, `nbllm` không thuộc schema cho phép. Production frontmatter đã được chỉnh tương thích bằng cách đặt toàn bộ extension dưới `metadata:`; nội dung metadata không đổi.
