# SKILL_IMPROVEMENT_PROPOSAL

```yaml
proposal_id: SIP_20260520_01
skill_id: wiki-web-scrape
current_version: "unversioned / [READ_FROM_SKILL_MD - no version field]"
proposed_version: "0.1.0 (initially versioned)"
source_run_id: manual
trigger: user_correction
severity: medium
approval_required: true
```

## Evidence
- **Báo cáo thực nghiệm vật lý:** Xem bằng chứng đo lường Token và Trigger tại [EVAL_REPORT_20260520.md](file:///d:/NoteBookLLM_Br/.agent/skill_reviews/EVAL_REPORT_20260520.md).
- **File hiện tại:** [wiki-web-scrape/SKILL.md](file:///d:/NoteBookLLM_Br/.agent/skills/wiki-web-scrape/SKILL.md)
- **Bối cảnh:** Frontmatter hiện tại chỉ có `name` và `description` tiếng Anh, thiếu trường `triggers`, `od` và `nbllm` namespace. Khi thực tế chạy bằng Tiếng Việt, Agent khó định tuyến chính xác nếu chỉ fuzzy match description tiếng Anh, hoặc dễ tự ý chạy cào web ghi đè vào hệ thống mà không có sự kiểm soát của AN.

## Problem
- **Thiếu định tuyến đa ngôn ngữ:** Thiếu các từ khóa kích hoạt rõ ràng bằng tiếng Việt khiến Agent không tự tin kích hoạt skill này khi người dùng yêu cầu cào/quét URL.
- **Rủi ro kiểm soát an toàn:** Skill này thực hiện tải dữ liệu từ URL ngoài và ghi file vào vùng đệm `00_Inbox/`. Cấu trúc metadata cũ chưa khai báo rõ ràng các thuộc tính an toàn runtime khiến Agent dễ ngộ nhận quyền ghi tự do.

## Proposed Change (diff format)
```diff
---
 name: wiki-web-scrape
 description: Use when the user provides a URL (like Wikipedia, articles, web pages) to read, analyze, or create atoms. SUPERSEDES sub_browser. This tool safely extracts Markdown via Lightpanda and stages it to 00_Inbox/. Prohibited for direct writing to 3-resources/raw_*/.
+triggers:
+  - "wiki-web-scrape"
+  - "cào"
+  - "scrape"
+od:
+  preview:
+    type: markdown
+  capabilities_required:
+    - file_write
+  outputs:
+    primary: "00_Inbox/"
+nbllm:
+  domain: ingest
+  default_runtime: chat_only
+  requires_an_go_for_write: true
 ---
```

## Regression Case
- **Regression Case 1 (Static URL Ingest):**
  - **Input:** "Cào trang Wikipedia về Functional Programming và lưu lại."
  - **Expected:** Kích hoạt `wiki-web-scrape` để tải trang qua Lightpanda, lưu bản thô đạt chuẩn vào `00_Inbox/sources/` để chờ duyệt. Tuyệt đối không ghi trực tiếp vào `3-resources/raw_sources/` (bảo toàn luật R1 và R22).
- **Regression Case 2 (Dynamic URL Boundary):**
  - **Input:** "Capture URL này có nhiều hiệu ứng hoạt họa JavaScript: https://example.com/dynamic"
  - **Expected:** Nhận diện trang động có rủi ro hiển thị kém trên Lightpanda, định tuyến sử dụng `wiki-crawl-4ai` (có hỗ trợ screenshot/visual proof) thay vì chạy `wiki-web-scrape` hoặc sub_browser tự do.

## Risk
- **Low:** Đề xuất chỉ chuẩn hóa metadata frontmatter và đặt cờ an toàn `requires_an_go_for_write: true`. Mọi hoạt động ghi tệp đều được kiểm soát bởi AN trước khi thực thi.

## AN Decision
- [x] Approve + GO → agent apply patch theo surgical diff
- [ ] Reject → lý do: ___
- [ ] Defer → review lại sau: ___

## Implementation Note
- Sau khi apply lần đầu, `quick_validate.py` báo top-level keys `triggers`, `od`, `nbllm` không thuộc schema cho phép. Production frontmatter đã được chỉnh tương thích bằng cách đặt toàn bộ extension dưới `metadata:`; nội dung metadata không đổi.
