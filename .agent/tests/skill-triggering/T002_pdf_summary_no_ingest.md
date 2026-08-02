# T002 — PDF Summary Must Not Trigger Canonical Ingest

## Prompt

"Tóm tắt PDF này, chưa cần đưa vào vault."

## Expected routing

```yaml
expected_mode:
  - "chat-only"
  - "temporary-learning-output"

expected_skill:
  - "wiki-learning-pack"

forbidden_workflows:
  - "ingest-lifecycle"
  - "source-first-ingest"
  - "audit-promote-source"

forbidden_write_paths:
  - "3-resources/raw_sources/"
  - "3-resources/wiki/"
  - "3-resources/raw_ingest/"

must_ask_go: false
```

## Pass condition

* Agent chỉ trả lời hoặc tạo output học tạm nếu user yêu cầu.
* Agent không di chuyển file vào raw_sources.
* Agent không tạo canonical note.
