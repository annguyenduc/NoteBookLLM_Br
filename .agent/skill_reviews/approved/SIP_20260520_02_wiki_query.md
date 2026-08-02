# SKILL_IMPROVEMENT_PROPOSAL

```yaml
proposal_id: SIP_20260520_02
skill_id: wiki-query
current_version: "unversioned / [READ_FROM_SKILL_MD - no version field]"
proposed_version: "0.1.0 (initially versioned)"
source_run_id: manual
trigger: user_correction
severity: low
approval_required: true
```

## Evidence
- **Báo cáo thực nghiệm vật lý:** Xem bằng chứng đo lường Token và Trigger tại [EVAL_REPORT_20260520.md](file:///d:/NoteBookLLM_Br/.agent/skill_reviews/EVAL_REPORT_20260520.md).
- **File hiện tại:** [wiki-query/SKILL.md](file:///d:/NoteBookLLM_Br/.agent/skills/wiki-query/SKILL.md)
- **Bối cảnh:** Frontmatter cũ cực kỳ đơn giản chỉ gồm `name` và `description` tiếng Anh, thiếu triggers đa ngôn ngữ. Khi người dùng truy vấn định nghĩa khái niệm hoặc nguồn gốc tài liệu bằng Tiếng Việt, Agent mất thời gian fuzzy match thay vì định tuyến trực tiếp.

## Problem
- **Độ nhạy định tuyến Tiếng Việt kém:** Thiếu các triggers tường minh như `wiki-query`, `định nghĩa`, `truy vấn nguồn` khiến Agent khó nhận diện tức thì các lệnh tìm kiếm chính xác.
- **Rủi ro trùng lặp với Chat Thường:** Nếu trigger từ khóa quá rộng như "định nghĩa", có nguy cơ Agent kích hoạt nhầm skill khi người dùng hỏi các câu hỏi mang tính triết học hoặc giao tiếp thông thường chứ không có ý định lục lọi Wiki Vault.

## Proposed Change (diff format)
```diff
---
 name: wiki-query
 description: "Use when retrieving concept definitions, tracing source provenance, or discovering connections between Knowledge Atoms via keyword or graph traversal. Use wiki-semantic-search instead when keyword search returns poor results."
+triggers:
+  - "wiki-query"
+  - "định nghĩa"
+  - "truy vấn nguồn"
+od:
+  preview:
+    type: markdown
+  capabilities_required:
+    - read_file
+nbllm:
+  domain: query
+  default_runtime: chat_only
+  requires_an_go_for_write: false
 ---
```

## Regression Case
- **Regression Case 1 (Exact Wiki Query Trigger):**
  - **Input:** "tìm định nghĩa của khái niệm monad trong wiki" hoặc "truy vấn nguồn gốc của Concept_FunctionalProgramming.md"
  - **Expected:** Khớp chính xác với trigger `"định nghĩa"` hoặc `"truy vấn nguồn"` trong ngữ cảnh Wiki Vault, tự động kích hoạt `wiki-query` để tra cứu trực tiếp trong SQLite index.
- **Regression Case 2 (Fuzzy Normal Chat Filter - Độc lập):**
  - **Input:** "định nghĩa giùm mình cuộc sống là gì dưới góc nhìn triết học"
  - **Expected:** Phân biệt rõ ràng đây là yêu cầu suy ngẫm/giao tiếp thông thường (chat thường), không kích hoạt `wiki-query` để tra cứu cơ sở dữ liệu vật lý (tránh gây lãng phí tài nguyên và sai lệch ngữ cảnh).

## Risk
- **Low:** Skill này là tác vụ chỉ đọc (read-only query) nên hoàn toàn an toàn, không có rủi ro thay đổi dữ liệu hệ thống.

## AN Decision
- [x] Approve + GO → agent apply patch theo surgical diff
- [ ] Reject → lý do: ___
- [ ] Defer → review lại sau: ___

## Implementation Note
- Sau khi apply lần đầu, `quick_validate.py` báo top-level keys `triggers`, `od`, `nbllm` không thuộc schema cho phép. Production frontmatter đã được chỉnh tương thích bằng cách đặt toàn bộ extension dưới `metadata:`; nội dung metadata không đổi.
