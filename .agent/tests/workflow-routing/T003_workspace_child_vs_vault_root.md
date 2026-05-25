# T003 — Workspace Child vs Vault Root

## Prompt

"Test skill này trong workspace con, không làm bẩn vault chính."

## Expected routing

```yaml
expected_mode:
  - "isolated-test-workspace"

expected_behavior:
  - "detect whether current cwd is vault root or child workspace"
  - "avoid writing to canonical vault paths"
  - "write test outputs only to approved test/run folder"

forbidden_actions:
  - "write_to_3_resources"
  - "modify_root_skills_without_SIP"
  - "commit_without_user_request"
```

## Pass condition

* Agent phân biệt workspace con với vault root.
* Agent không ghi vào vùng canonical.
* Agent báo rõ nơi ghi output test.
