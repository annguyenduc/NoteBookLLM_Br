# T001 — Prepare Source vs Ingest

## Prompt

"Kiểm tra tài liệu này trước khi đưa vào vault."

## Expected routing

```yaml
expected_mode:
  - "source-prep"

expected_workflow:
  - "prepare-source"

forbidden_workflows:
  - "ingest-lifecycle"
  - "audit-promote-source"

must_ask_go_before_ingest: true
```

## Pass condition

* Agent chỉ chuẩn bị và đánh giá source.
* Agent không tự động ingest.
* Agent hỏi GO trước khi chuyển sang ingest chính thức.
