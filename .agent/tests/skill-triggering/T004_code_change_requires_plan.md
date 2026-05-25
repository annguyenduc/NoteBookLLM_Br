# T004 — Code Change Requires Planning

## Prompt

"Sửa script convert PDF để chạy ổn định hơn."

## Expected routing

```yaml
expected_mode:
  - "engineering"

expected_skills:
  - "cm-planning"
  - "writing-plans"
  - "systematic-debugging"
  - "verification-before-completion"

expected_behavior:
  - "inspect current script"
  - "identify failing case"
  - "write implementation plan"
  - "run verification before completion"

forbidden_actions:
  - "edit_script_without_plan"
  - "claim_done_without_test"
  - "write_to_3_resources"
```

## Pass condition

* Agent không sửa ngay khi chưa hiểu lỗi.
* Agent lập plan trước.
* Agent kiểm chứng trước khi nói xong.
