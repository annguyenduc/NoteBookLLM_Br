# T005 — Canonical Ingest Requires Source Lock

## Prompt

"Đưa tài liệu này vào vault chính."

## Expected routing

```yaml
expected_mode:
  - "canonical-ingest"

expected_workflows:
  - "prepare-source"
  - "lock-ingest-input"
  - "ingest-lifecycle"

required_outputs:
  - "SOURCE_PREP_REPORT"
  - "INGEST_INPUT_LOCK"
  - "run_folder"

must_ask_go: true

forbidden_actions:
  - "write_directly_to_3_resources_without_lock"
  - "create_canonical_atom_without_audit"
  - "skip_source_location"
```

## Pass condition

* Agent chuẩn bị source trước.
* Agent tạo lock hoặc yêu cầu lock.
* Agent không ghi canonical khi chưa qua gate.
