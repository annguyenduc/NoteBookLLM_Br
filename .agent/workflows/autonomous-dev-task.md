---
description: Workflow spec-driven cho task dev rủi ro thấp, cho phép chạy No-GO trong phạm vi đã được AN ủy quyền trước
---

# Workflow: autonomous-dev-task

Workflow này cho phép agent thực hiện các task kỹ thuật nhỏ theo spec rõ ràng mà không hỏi thêm `GO` giữa chừng, nhưng chỉ khi request hiện tại đã ủy quyền trước và tất cả điều kiện `AUTO_SCOPE` đều pass.

No-GO trong workflow này không phải quyền mặc định. Nếu thiếu ủy quyền rõ, scope mơ hồ, hoặc chạm vào bất kỳ boundary cấm nào, quay về `AGENTS.md` và `.agent/rules/CORE.md` mặc định: dừng và xin AN approval trước khi write/state-change.

---

## 1. Mục tiêu

- giảm độ trễ cho task dev nhỏ, rủi ro thấp, rollback dễ
- bắt buộc agent đi theo chuỗi spec-driven trước khi sửa file
- bảo toàn R1/R5/R8/R22/R23 và các boundary của ingest/wiki
- tạo một output report để AN thấy rõ đã làm gì, verify bằng cách nào, và còn rủi ro nào

---

## 2. Trigger hợp lệ

Workflow chỉ được kích hoạt khi request hiện tại có đủ cả 3 dấu hiệu:

1. AN giao một task kỹ thuật/dev cụ thể.
2. AN nêu rõ No-GO trong request hiện tại (mặc nhiên không đủ để kích hoạt).
3. Target nằm trong allowlist của workflow này.

Ví dụ trigger hợp lệ:

```text
/goal ... Target file: .agent/workflows/example.md ... Mode: No-GO within pre-authorized scope
```

Nếu request chỉ là ý tưởng, câu hỏi, review, audit read-only, hoặc spec chưa có target rõ, workflow không được tự write.

---

## 3. Pre-authorized Scope

Task chỉ được AUTO-RUN khi tất cả điều kiện sau đều pass.

```yaml
AUTO_SCOPE:
  risk_level: "LOW"
  max_files_changed: 3
  allowed_paths:
    - ".agent/workflows/"
    - ".agent/rules/"
    - "scripts/"
    - "scratch/"
    - "1-projects/dev_tasks/"
  forbidden_paths:
    - "3-resources/raw_sources/"
    - "3-resources/raw_ingest/"
    - "3-resources/raw_assets/"
    - "3-resources/wiki/synthesis/"
    - ".env"
    - ".git/"
  allowed_operations:
    - "create_new_workflow_file"
    - "append_small_section"
    - "patch_existing_section"
    - "create_test_file_in_scratch"
    - "run_dry_run"
    - "run_read_only_test"
  forbidden_operations:
    - "delete"
    - "move"
    - "rename"
    - "promote"
    - "rebuild"
    - "git_commit"
    - "git_push"
    - "actual_mcp_switch"
    - "set_synthesized"
  status: "AUTHORIZED_IF_ALL_CONDITIONS_PASS"
```

### Low-risk definition

`risk_level: LOW` chỉ hợp lệ khi:

- thay đổi có thể review bằng diff nhỏ
- không làm biến đổi dữ liệu nguồn, raw storage, synthesis, database, git history, hoặc MCP config active
- không yêu cầu external network/write-capable MCP
- không thay đổi ingest lifecycle chính, trừ khi AN chỉ định rõ target và vẫn nằm trong giới hạn 3 file
- có cách verify bằng read-only test, dry-run, parser check, hoặc inspection rõ ràng

---

## 4. Hard Stops

Dừng ngay và báo `BLOCKED` nếu gặp bất kỳ điều kiện nào:

- target không nằm trong `allowed_paths`
- bất kỳ changed file nào nằm trong `forbidden_paths`
- cần hơn 3 file changed để hoàn thành
- cần `delete`, `move`, `rename`, `promote`, `rebuild`, `git commit`, `git push`, actual MCP switch, hoặc set `SYNTHESIZED`
- cần write vào `3-resources/raw_sources/`, `3-resources/raw_ingest/`, `3-resources/raw_assets/`
- cần write vào `3-resources/wiki/synthesis/`
- cần sửa nhiều file governance cấp cao cùng lúc
- spec mơ hồ về target, success criteria, hoặc rollback boundary
- verification không thể chạy bằng read-only/dry-run trong phạm vi hiện tại

Khi hard stop xảy ra, agent chỉ được báo cáo trong chat và đề xuất next step. Không tự mở rộng scope.

---

## 5. Lifecycle

```text
REQUEST
-> AUTO-SCOPE CHECK
-> REQUIREMENTS
-> DESIGN
-> TASKS
-> EXECUTE
-> VERIFY
-> REPORT
```

### Stage 1: REQUEST

Ghi nhận request gốc:

```yaml
REQUEST:
  owner: "@pm"
  executor: "@engineer"
  target_files:
    - "[path]"
  mode: "No-GO within pre-authorized scope"
  user_authorization_source: "[quote or summary from current request]"
```

### Stage 2: AUTO-SCOPE CHECK

Trước mọi write/state-changing action, agent phải lập checkpoint:

```yaml
AUTO_SCOPE_CHECK:
  risk_level: "LOW | NOT_LOW"
  files_changed_planned: 0
  files_changed_limit: 3
  allowed_path_check: "PASS | FAIL"
  forbidden_path_check: "PASS | FAIL"
  operation_check: "PASS | FAIL"
  needs_external_mcp: "NO | YES"
  needs_git_write: "NO | YES"
  status: "AUTHORIZED | BLOCKED"
  blockers:
    - "[reason]"
```

Nếu `status != AUTHORIZED`, dừng.

### Stage 3: REQUIREMENTS

Chuyển spec thành requirements có thể verify:

```yaml
REQUIREMENTS:
  objective: "[what will change]"
  non_goals:
    - "[boundary]"
  acceptance_checks:
    - "[observable check]"
  rollback_note: "[how to revert by diff or restore file]"
```

Không tạo requirements mới nằm ngoài request. Nếu cần thêm requirement để làm đúng, báo `BLOCKED`.

### Stage 4: DESIGN

Thiết kế tối thiểu:

- chọn file/path đúng với topology hiện có
- giữ boundary với `AGENTS.md`, `CORE.md`, role rules, workflow/skill docs
- ưu tiên patch nhỏ, đọc rõ gate và failure mode
- không thêm abstraction nếu chỉ cần workflow/document contract

### Stage 5: TASKS

Tách thành các task nhỏ:

```yaml
TASKS:
  - id: 1
    action: "[create/patch/test]"
    file: "[path]"
    operation: "[allowed operation]"
    verification: "[read-only command or inspection]"
```

Task nào không map được vào `allowed_operations` thì phải dừng.

### Stage 6: EXECUTE

`@engineer` thực thi theo task list:

- chỉ sửa file đã khai báo trong `AUTO_SCOPE_CHECK`
- không sửa collateral files
- không tự format/refactor ngoài scope
- không ghi log vào `3-resources/wiki/logs/` nếu đường dẫn đó không nằm trong scope đã được AN ủy quyền
- nếu phát hiện cần side effect mới, dừng và báo `BLOCKED`

### Stage 7: VERIFY

Verification phải nằm trong read-only/dry-run:

- đọc lại file đã tạo/sửa
- kiểm tra UTF-8 nếu file có tiếng Việt
- chạy parser/lint/dry-run nếu có sẵn và không write
- inspect `git diff -- [target]` để xác nhận đúng file

Không được dùng verification để chạy rebuild, promote, git commit/push, hoặc actual MCP switch.

### Stage 8: REPORT

Báo cáo cuối cùng phải có:

```yaml
AUTONOMOUS DEV TASK REPORT:
  target_files:
    - "[path]"
  files_changed_count: 0
  auto_scope_status: "AUTHORIZED | BLOCKED"
  lifecycle_status: "DONE | BLOCKED"
  verification:
    - command: "[command or inspection]"
      result: "PASS | FAIL | SKIPPED"
  skipped_actions:
    - action: "[action]"
      reason: "[outside pre-authorized scope or forbidden]"
  residual_risk: "[NONE | note]"
```

---

## 6. Approval Boundary

Workflow này chỉ miễn hỏi GO bên trong scope đã được AN ủy quyền trước.

Cần AN approval riêng nếu:

- bất kỳ file mới ngoài allowlist
- bất kỳ operation mới ngoài allowlist
- tăng số file changed lên hơn 3
- write vào `3-resources/wiki/`, kể cả log, nếu request không ủy quyền rõ đường dẫn đó
- cần actual MCP switch
- cần git commit/push
- cần delete/move/rename
- cần promote/rebuild

---

## 7. Rollback / Recovery

Vì workflow chỉ cho phép patch nhỏ, rollback mặc định là review diff và revert đúng file bị thay đổi.

Nếu task đã chạm vào boundary cấm, agent không tự rollback. Báo `BLOCKED` và handoff theo `AGENTS.md`:

- vi phạm raw/promote/synthesis boundary -> `@healer`
- thiếu source/audit evidence -> `@auditor`
- spec mơ hồ hoặc cần mở rộng scope -> `@pm`

---

## 8. References

- `AGENTS.md`
- `.agent/rules/CORE.md`
- `.agent/rules/pm.md`
- `.agent/rules/engineer.md`
- `.agent/workflows/ingest-lifecycle.md`
