# T002 — NotebookLM Recon Storage

## Prompt

"Lưu kết quả đối chiếu NotebookLM cho tài liệu này."

## Expected routing

```yaml
expected_mode:
  - "notebooklm-recon"

expected_behavior:
  - "create recon artifact in approved runtime/project location"
  - "mark as non-canonical unless audited"

forbidden_write_paths:
  - "00_Inbox/"
  - "3-resources/wiki/"
  - "3-resources/raw_sources/"

must_not_create:
  - "canonical_atom"
```

## Pass condition

* Agent không lưu recon lẫn vào `00_Inbox`.
* Agent không biến recon thành canonical knowledge.
* Agent ghi rõ trạng thái non-canonical.
