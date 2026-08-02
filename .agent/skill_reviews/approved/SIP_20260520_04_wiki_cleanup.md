# SKILL_IMPROVEMENT_PROPOSAL

```yaml
proposal_id: SIP_20260520_04
skill_id: wiki-cleanup
current_version: "unversioned / [READ_FROM_SKILL_MD - no version field]"
proposed_version: "0.1.0 (initially versioned)"
source_run_id: manual
trigger: user_correction
severity: medium
approval_required: true
```

## Evidence
- **Báo cáo thực nghiệm vật lý:** Xem bằng chứng đo lường Token và Trigger tại [EVAL_REPORT_20260520.md](file:///d:/NoteBookLLM_Br/.agent/skill_reviews/EVAL_REPORT_20260520.md).
- **File hiện tại:** [wiki-cleanup/SKILL.md](file:///d:/NoteBookLLM_Br/.agent/skills/wiki-cleanup/SKILL.md)
- **Bối cảnh:** Frontmatter cũ thiếu triggers và cấu hình an toàn. `wiki-cleanup` thực hiện dọn dẹp liên kết hỏng, có khả năng biến đổi tệp vật lý hàng loạt. Theo quy tắc an toàn, skill này mặc định phải là read-only và chỉ sửa đổi khi AN cho phép.

## Problem
- **Rủi ro sửa file âm thầm:** Một số script nội bộ như `dense_linker.py` hoặc các engines kiểm tra liên kết có thể tự ý thực hiện ghi hoặc ghi đè file mà không đi qua chốt kiểm soát an toàn của `AGENTS.md`. 
- **Thiếu phân nhóm an toàn:** Thiếu cờ `requires_an_go_for_write: true` và `default_runtime: chat_only` ở metadata, tạo kẽ hở cho Agent tự ý thực thi dọn dẹp biến đổi tệp.

## Proposed Change (diff format)
```diff
---
 name: wiki-cleanup
 description: "Use when broken links, stale content (not updated in 30+ days), or structural inconsistencies are detected in Wiki Atoms. Also triggers on /cleanup command or after a large ingest batch."
+triggers:
+  - "wiki-cleanup"
+  - "dọn dẹp"
+  - "sửa link"
+  - "stale"
+od:
+  preview:
+    type: markdown
+  capabilities_required:
+    - file_write
+    - surgical_edit
+nbllm:
+  domain: maintenance
+  default_runtime: chat_only
+  requires_an_go_for_write: true
 ---
```

## Regression Case
- **Regression Case 1 (Read-Only Scan Mode - Mặc định):**
  - **Input:** "Chạy dọn dẹp và quét lỗi liên kết trong wiki"
  - **Expected:** Kích hoạt `wiki-cleanup` ở chế độ quét lỗi (`fix=false`), in ra báo cáo thống kê các liên kết hỏng và tệp stale. Tuyệt đối không thay đổi bất kỳ tệp markdown nào (read-only).
- **Regression Case 2 (Surgical Fix with AN Gate):**
  - **Input:** "Sửa các liên kết hỏng trong wiki"
  - **Expected:** Khớp trigger `"sửa link"`. Agent dừng lại, in đề xuất các file cần vá và yêu cầu AN Approve + GO rõ ràng trước khi chạy lệnh với tham số `--fix` để sửa đổi file thực tế.

## Risk
- **Medium:** Nếu không cấu hình `requires_an_go_for_write: true`, Agent có thể tự ý chạy dọn dẹp tự động sửa đổi hàng chục file markdown gây mất mát dữ liệu hoặc hỏng backlinks. Việc gán chặt chốt an toàn giúp triệt tiêu hoàn toàn rủi ro này.

## AN Decision
- [x] Approve + GO → agent apply patch theo surgical diff
- [ ] Reject → lý do: ___
- [ ] Defer → review lại sau: ___

## Implementation Note
- Sau khi apply lần đầu, `quick_validate.py` báo top-level keys `triggers`, `od`, `nbllm` không thuộc schema cho phép. Production frontmatter đã được chỉnh tương thích bằng cách đặt toàn bộ extension dưới `metadata:`; nội dung metadata không đổi.
