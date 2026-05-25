# T001 — PDF Summary Should Use Learning Pack

## Prompt

"Tóm tắt PDF này để tôi học nhanh."

## Expected routing

```yaml
expected_mode:
  - "learning-first"
  - "chat-only unless user asks for artifact"

expected_skill:
  - "wiki-learning-pack"

allowed_supporting_skills:
  - "process-raw-resource"

forbidden_skills:
  - "wiki-ingest"
  - "wiki-rebuild"
  - "wiki-promote"

must_not_write:
  - "3-resources/"
  - "3-resources/raw_sources/"
  - "3-resources/wiki/"

must_ask_go: false
```

## Pass condition

* Agent tạo bản tóm tắt học nhanh.
* Agent không ingest nguồn vào canonical vault.
* Agent không tạo atom chính thức.
* Agent không rebuild index.
