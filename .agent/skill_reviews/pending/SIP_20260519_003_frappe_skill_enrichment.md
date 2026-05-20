# SIP_20260519_003_frappe_skill_enrichment.md

## Metadata
```yaml
sip_id: SIP_20260519_003
skill_id: frappe_skill_enrichment_bundle
skill_paths:
  - D:/anngu/.codex/skills/cm-frappe-agent/SKILL.md
  - D:/anngu/.codex/skills/cm-frappe-agent/skills/bench-commands/SKILL.md
  - D:/anngu/.codex/skills/cm-frappe-agent/skills/client-scripts/SKILL.md
  - D:/anngu/.codex/skills/cm-frappe-agent/skills/doctype-patterns/SKILL.md
  - D:/anngu/.codex/skills/cm-frappe-agent/skills/frappe-api/SKILL.md
  - D:/anngu/.codex/skills/cm-frappe-agent/skills/remote-operations/SKILL.md
  - D:/anngu/.codex/skills/cm-frappe-agent/skills/server-scripts/SKILL.md
  - D:/anngu/.codex/skills/cm-frappe-agent/skills/web-forms/SKILL.md
trigger: missing_step
created: 2026-05-19
status: PENDING
author: "@pm"
phase: Phase 3A
approval_required: true
production_edit_performed: false
```

## Scope Lock

Phase 3A chỉ tạo proposal/SIP. Không sửa production `SKILL.md`, không đổi `description`, không archive, không xoá, không move.

Đề xuất này chỉ mô tả cách enrich 8 Frappe `SKILL.md` bằng nội dung body gọn, có pointer tới legacy references. Nếu AN approve + GO ở phase sau, phần thực thi phải là surgical patch riêng và vẫn giữ nguyên frontmatter `description`.

## Evidence

User đã yêu cầu: "AN GO - Phase 3A Frappe skill remediation proposal: đọc Frappe legacy bodies, tạo proposal/SIP cho cách enrich 8 Frappe SKILL.md; không sửa production SKILL.md, không đổi description, không archive, không xoá, không move."

Đã đọc 8 production skill bodies:

- `cm-frappe-agent/SKILL.md`
- `bench-commands/SKILL.md`
- `client-scripts/SKILL.md`
- `doctype-patterns/SKILL.md`
- `frappe-api/SKILL.md`
- `remote-operations/SKILL.md`
- `server-scripts/SKILL.md`
- `web-forms/SKILL.md`

Quan sát từ production bodies:

- Cả 8 file hiện dùng cùng wrapper generic: `Goal`, `Instructions`, `Examples`, `Constraints`, `Legacy Notes`, `Quality Gate`, `Example Triggers`.
- Cả 8 file chỉ trỏ legacy bằng một dòng: `Original pre-migration body is preserved in references/legacy_body.vi.md`.
- Cả 8 file có `Example Triggers` giống nhau: `"Plan this task before implementation."`, `"Route this request to the right skills."`, `"Audit the skill and report risks."`
- Các body production không expose domain-specific operating rules ngay trong body, nên agent phải tự đoán khi nào đọc legacy reference.

Đã đọc legacy body headings và kích thước:

| Skill | Legacy lines | Nội dung legacy đáng giữ |
|---|---:|---|
| `cm-frappe-agent` | 36 | 7-layer architecture, lifecycle agents/tools, red flags |
| `bench-commands` | 627 | site/app/dev/build/migrate/cache/console/backup commands |
| `client-scripts` | 648 | form events, field manipulation, queries, buttons, child table, dialogs, API calls |
| `doctype-patterns` | 583 | DocType JSON, fields, naming, controller hooks, permissions, data integrity |
| `frappe-api` | 747 | document ops, database API, whitelisted API, utilities, notifications, background jobs |
| `remote-operations` | 19 | key references, red flags, example triggers |
| `server-scripts` | 615 | controller, whitelisted APIs, DB operations, jobs, hooks, notifications |
| `web-forms` | 18 | key references, red flags, example triggers |

Domain-critical evidence:

- Parent legacy defines 7-layer rule: controller thin, engines pure Python, API boundary via `@frappe.whitelist`, tasks/setup/tests/client JS separated.
- `doctype-patterns` legacy includes a hard safety rule: never use non-ASCII/accented characters in DocType names or fieldnames; use English canonical names and localization labels instead.
- `remote-operations` and `web-forms` have thin legacy bodies, so enrichment should point to existing resources (`resources/rest-api-patterns.md`, `resources/web-form-patterns.md`) instead of inventing unsupported detail.

## Problem

The migration preserved legacy content but made the production bodies too generic. This creates three practical gaps:

1. Trigger/body mismatch: frontmatter says the skill is Frappe-specific, but body examples are generic planning/routing/audit phrases.
2. Missing progressive disclosure: large legacy files exist, but the body does not say which reference section to load for a task.
3. Lost quality gates: important Frappe guardrails exist in legacy references, but are not visible enough at activation time.

This is not a request to restore the old large bodies verbatim. Copying 600-700 lines back into `SKILL.md` would hurt context hygiene. The correct remediation is a compact body that routes to the right legacy/reference material only when needed.

## Proposed Change

### Bundle Rule

For all 8 `SKILL.md` files:

- Keep `name`, `description`, and existing version unless AN explicitly chooses a version bump.
- Keep `references/legacy_body.vi.md`; do not move or archive it.
- Replace generic example triggers with domain-specific trigger examples.
- Add a `When to load references` section that tells the agent when to open `references/legacy_body.vi.md` and when to use parent `resources/`.
- Add a compact `Quality Gates` section extracted from observed legacy content.
- Keep each body line count `<= 120` after patch. This is now a hard regression criterion for Phase 3B, not just a rough target.

### Phase 3B Implementation Guardrails

Before patch:

- Create a byte-for-byte backup of all 8 production `SKILL.md` files.
- Record pre-patch SHA-256 for each full file.
- Record pre-patch SHA-256 for each frontmatter block, where frontmatter is the byte range from file start through the second `---` delimiter.
- Generate a before/after diff summary after patch.

After patch:

- Verify every referenced relative path in the 8 bodies exists from the corresponding `SKILL.md` folder.
- Verify body line count `<= 120` for each `SKILL.md`.
- Verify frontmatter byte-for-byte preserved for all 8 files.
- Verify only body content changed.
- Verify no `references/legacy_body.vi.md` file changed.

Rollback note:

- If any regression check fails, restore the 8 production `SKILL.md` files from the pre-patch backup and report the failed check. Do not attempt partial repair over a failed regression state.

### 1. `cm-frappe-agent/SKILL.md`

Proposed body enrichment:

```diff
+ ## Operating Model
+ Use this parent skill to route full-lifecycle Frappe/ERPNext work.
+ Keep the 7-layer boundary visible:
+ - L1 DocType controller: validation and lifecycle hooks only.
+ - L2 engines: pure Python business logic, unit-testable, no DB calls.
+ - L3 API: `@frappe.whitelist` boundary.
+ - L4 tasks: scheduled/background wrappers around engines.
+ - L5 setup: install/migrate hooks.
+ - L6 tests: isolated tests for L2 logic and integration gates.
+ - L7 client JS: form/list/web UI behavior.
+
+ ## Dispatch
+ - Bench/site/app operations -> `skills/bench-commands`
+ - DocType schema/modeling -> `skills/doctype-patterns`
+ - Controller/server-side Python -> `skills/server-scripts`
+ - General Frappe API references -> `skills/frappe-api`
+ - Form/client JS -> `skills/client-scripts`
+ - Guest-facing Web Forms -> `skills/web-forms`
+ - Remote REST/API operations -> `skills/remote-operations`
+
+ ## When To Load References
+ Load `references/legacy_body.vi.md` when choosing architecture, boundaries, lifecycle ownership, or red-flag checks.
+ Load `resources/code-patterns-guide.md` for implementation patterns and `resources/7-layer-architecture.md` for deeper architecture decisions.
```

Regression case:

- Input: "Thiết kế app Frappe cho quản lý ticket, có workflow, API và báo cáo."
- Expected: parent skill routes architecture first, separates DocType/controller/engine/API/client responsibilities, then points to child skills.

### 2. `bench-commands/SKILL.md`

Proposed body enrichment:

```diff
+ ## Scope
+ Use for Bench CLI tasks: site create/drop/use, backup/restore, app install/uninstall/update, build, migrate, cache, console, scheduler, and production operations.
+
+ ## Command Safety
+ - Treat `drop-site`, force uninstall, reset, restore, and production update as destructive or state-changing.
+ - Ask for explicit approval before commands that delete data, alter a production site, or overwrite site state.
+ - Prefer dry-run/inspection commands first when diagnosing.
+
+ ## When To Load References
+ Load `references/legacy_body.vi.md` before giving exact `bench` commands or sequences.
+ Load parent `resources/bench_commands.md` for concise command catalog.
+ Load parent `resources/installation-guide.md` for install/setup tasks.
```

Regression case:

- Input: "Bench site bị lỗi migrate, cần xem lệnh nào chạy tiếp."
- Expected: inspect/migrate/cache/build sequence, warning before state-changing repair, reference load before exact commands.

### 3. `client-scripts/SKILL.md`

Proposed body enrichment:

```diff
+ ## Scope
+ Use for Frappe Desk client-side JavaScript: form events, field display/required/read-only behavior, link queries, custom buttons, child tables, dialogs, `frappe.call`, messages, and utilities.
+
+ ## Quality Gates
+ - Do not put server-side permission logic only in client scripts.
+ - Keep fieldnames canonical and stable; display labels can be localized.
+ - For child tables, handle row events and refresh behavior explicitly.
+ - For API calls, specify method path, args, callback/error handling, and permission assumptions.
+
+ ## When To Load References
+ Load `references/legacy_body.vi.md` before writing form scripts, child-table code, dialog code, or `frappe.call` snippets.
+ Load parent `resources/code-patterns-guide.md` if the request spans client and server code.
```

Regression case:

- Input: "Thêm nút custom trên Sales Invoice gọi API tính điểm khách hàng."
- Expected: client script uses custom button + `frappe.call`, hands server method design to server/API skill, does not hide permission logic client-side.

### 4. `doctype-patterns/SKILL.md`

Proposed body enrichment:

```diff
+ ## Scope
+ Use for DocType design: JSON structure, field types, field options, naming, autoname, child tables, Single/Virtual DocTypes, permissions, and controller hook placement.
+
+ ## Hard Gate
+ Never use Vietnamese/accented/non-ASCII characters in DocType names or `fieldname`.
+ Use English canonical names for DocTypes and `snake_case` fieldnames.
+ Put Vietnamese or other localized display text in `label`, not in identifiers.
+
+ ## When To Load References
+ Load `references/legacy_body.vi.md` before designing or editing DocTypes.
+ Load parent `resources/doctype-registry.md` if the task needs existing DocType catalog alignment.
+ Load parent `resources/scaffold_checklist.md` before proposing generated files.
```

Regression case:

- Input: "Tạo DocType Hóa đơn đào tạo với field tên học viên."
- Expected: propose `Training Invoice`, `student_name`, Vietnamese labels only; block accented identifiers.

### 5. `frappe-api/SKILL.md`

Proposed body enrichment:

```diff
+ ## Scope
+ Use for Frappe Python/JS APIs: document operations, `frappe.db`, raw SQL, whitelisted methods, utilities, messaging, emails, notifications, background jobs, and REST patterns.
+
+ ## API Safety
+ - Prefer document APIs when controller hooks and permissions must run.
+ - Flag `ignore_permissions`, `ignore_mandatory`, raw SQL, manual commit/rollback, and guest whitelisted methods as high-risk choices.
+ - For public APIs, state auth, allowed methods, input validation, and permission checks.
+
+ ## When To Load References
+ Load `references/legacy_body.vi.md` before giving API snippets.
+ Load parent `resources/rest-api-patterns.md` for REST/remote API behavior.
+ Load parent `resources/common_pitfalls.md` when debugging unexpected Frappe API behavior.
```

Regression case:

- Input: "Viết endpoint cho mobile app tạo Lead."
- Expected: whitelisted API design with method restrictions, validation, permission/auth assumption, no casual guest access.

### 6. `remote-operations/SKILL.md`

Proposed body enrichment:

```diff
+ ## Scope
+ Use for remote Frappe/ERPNext operations over REST/API: remote site management, integration calls, API tokens, backups/checks over a network boundary, and production-safe operation plans.
+
+ ## Remote Safety
+ - Classify every remote action as read-only, write-capable, destructive, or credential-sensitive.
+ - Do not request or expose secrets in chat.
+ - Prefer read-only health checks before write-capable operations.
+ - For production remote actions, require explicit approval and rollback notes.
+
+ ## When To Load References
+ Load `references/legacy_body.vi.md` for existing key references and red flags.
+ Load parent `resources/rest-api-patterns.md` for REST operation patterns.
+ Load parent `resources/common_pitfalls.md` for operational failure diagnosis.
```

Regression case:

- Input: "Gọi API từ xa để update Customer trên site ERPNext production."
- Expected: classify as write-capable production remote operation, require approval before execution, outline auth/rollback/verification.

### 7. `server-scripts/SKILL.md`

Proposed body enrichment:

```diff
+ ## Scope
+ Use for server-side Frappe Python: DocType controllers, document events, whitelisted APIs, database reads/writes, background jobs, scheduled jobs, hooks, error handling, email, and realtime notifications.
+
+ ## Server-Side Gates
+ - Keep business logic in service/engine functions where possible; keep controllers thin.
+ - Avoid bypassing controller/permission behavior unless the reason is explicit.
+ - Treat raw SQL, commits, rollbacks, deletes, and `ignore_permissions` as high-risk.
+ - Pair server changes with tests or a concrete manual verification path.
+
+ ## When To Load References
+ Load `references/legacy_body.vi.md` before writing controller, hook, API, DB, or job code.
+ Load parent `resources/code-patterns-guide.md` for implementation patterns.
+ Load parent `resources/upgrade_patterns.md` for migration/upgrade-sensitive changes.
```

Regression case:

- Input: "Thêm hook khi submit Payment Entry để tạo bản ghi phụ."
- Expected: controller/hook boundary, service function extraction if logic grows, permission and transaction considerations.

### 8. `web-forms/SKILL.md`

Proposed body enrichment:

```diff
+ ## Scope
+ Use for Frappe Web Forms: public/guest form behavior, client script, CSS, field visibility, validation split between client and server, permissions, submission handling, and common Web Form pitfalls.
+
+ ## Web Form Gates
+ - Treat guest access as security-sensitive.
+ - Do not rely on client-side validation alone.
+ - State where server-side validation/permissions live.
+ - Keep user-facing labels localized while identifiers remain canonical.
+
+ ## When To Load References
+ Load `references/legacy_body.vi.md` for existing key references and red flags.
+ Load parent `resources/web-form-patterns.md` for actual Web Form implementation patterns.
+ Load `skills/client-scripts/references/legacy_body.vi.md` only when the task needs Desk-style JS patterns that also apply to Web Forms.
```

Regression case:

- Input: "Làm Web Form đăng ký học viên cho khách không login."
- Expected: guest access classified as sensitive, server validation and permission path stated, labels separated from canonical fieldnames.

## Regression Set For Phase 3B

If AN approves implementation, run these lightweight checks after patch:

1. YAML/frontmatter parse passes for all 8 files.
2. No `description:` line changed in any of the 8 files.
3. No production `references/legacy_body.vi.md` file modified.
4. Each body contains `When To Load References`.
5. `doctype-patterns/SKILL.md` contains the non-ASCII identifier hard gate.
6. `remote-operations/SKILL.md` classifies remote actions by safety level.
7. `web-forms/SKILL.md` flags guest access and client-only validation risk.
8. Each `SKILL.md` remains concise and references only existing relative paths.
9. Each `SKILL.md` body line count is `<= 120`.
10. Frontmatter for each `SKILL.md` is byte-for-byte identical to the pre-patch backup.
11. A backup and diff summary exist before reporting completion.

## Risk

Risk: medium.

Reason: touching 8 skill bodies can improve triggering quality but may create drift if the body promises references or behavior that do not exist. The proposal avoids that by referencing only observed files and preserving legacy bodies as source material.

Main implementation risk for Phase 3B: accidental frontmatter description change or over-expansion of `SKILL.md` bodies. Mitigation: patch only body sections, then diff-check `description:` lines and legacy references.

## Required Approval Point

AN review required before any production edit.

If approved, next phase should be:

```text
AN GO - Phase 3B apply SIP_20260519_003 only; enrich 8 Frappe SKILL.md bodies; preserve descriptions; do not modify legacy references; run regression checks.
```

## AN Decision

- [ ] Approve + GO -> agent applies surgical body-only patches in Phase 3B.
- [ ] Reject -> reason: ___
- [ ] Defer -> review again after: ___
