---
description: Workflow định tuyến nguồn vào theo mô hình 2 entry lanes, 1 canonical core; không phải ingest engine
---

# Workflow: knowledge-intake

> Runtime note 2026-05-21: vault default đã chuyển sang `learning-first`.
> Dùng `.agent/workflows/learning-first.md` cho học nhanh/tra cứu nhanh.
> Dùng workflow này khi cần phân luồng rõ giữa preview và official ingest.

`knowledge-intake` là workflow routing nhẹ cho lớp tiếp nhận nguồn.

Mục tiêu là tách rõ:
- Preview lane: đọc nhanh, học nhanh, đánh giá có đáng ingest không.
- Official ingest lane: handoff sang canonical core `ingest-lifecycle`.
- NotebookLM recon layer: trinh sát nhanh, không-canonical, chỉ để giảm mù trước preview hoặc ingest planning.

Workflow này không thay thế `ingest-lifecycle` và không được tự tạo tri thức canonical.
Workflow này cũng không thay thế `NotebookLM query`; nó là lớp chuẩn hóa sau recon, không phải lớp trả lời nhanh.

---

## 1. Objective

Triển khai mô hình:

```text
2 entry lanes, 1 canonical core
```

Canonical core vẫn là:

```text
prepare-source
-> audit-promote-source
-> lock-ingest-input
-> ingest
-> ingest-generate
-> ingest-index-log
```

---

## 2. Entry Lanes

### Recon Layer: NotebookLM Query

Đây không phải entry lane độc lập.
Đây là lớp phụ trợ có thể chạy trước Lane A hoặc trước khi quyết định handoff sang Lane B.

Mục tiêu:
- hỏi nhanh nguồn đã có trong NotebookLM
- lấy ý chính, đoạn quan trọng, candidate concepts, candidate entities
- tìm câu hỏi còn mơ hồ, contradiction, gap

Status:

```yaml
recon_status: "UNVERIFIED"
canonical_status: "NON_CANONICAL_ANALYSIS"
```

Hard rule:
- output của NotebookLM không phải `source_evidence_file`
- output của NotebookLM không phải `primary_ingest_file`
- output của NotebookLM không được dùng để tạo Atom trực tiếp
- mọi claim đi tiếp phải được đối chiếu lại qua `knowledge-intake` hoặc canonical source
- output từ NotebookLM được coi là `query notes` only; claim nào không có source location phải hạ xuống `LOW` confidence và không được đi vào Atom candidate handoff nếu chưa verify với `primary_ingest_file`

### Lane A: Preview

Dùng cho natural-language request như:
- đọc nhanh file này
- file này có đáng ingest không
- tạo learning map
- preview nguồn này
- xem file/workflow/code này nói gì

Flow:

```text
knowledge-intake
-> artifact-specific preview mode
-> CHAT_ONLY by default during runtime
-> optional preview artifact if workflow/user text explicitly requests write
```

Preview output luôn là:

```yaml
learning_status: "PREVIEW_ONLY"
canonical_status: "NON_CANONICAL"
source_id: "NONE"
```

### Lane B: Official Ingest

Slash command:

```text
/ingest [file]
```

phải bypass `knowledge-intake` và đi thẳng vào `ingest-lifecycle`.

Natural-language official ingest request như:
- ingest file này end-to-end
- đưa file này vào vault chính thức
- ingest chính thức file này

thì `knowledge-intake` chỉ route và handoff ngay sang `ingest-lifecycle`.

Không tạo preview artifact trong route này.

Recommended sequence when NotebookLM is available:

```text
NotebookLM query
-> knowledge-intake
-> preview analysis in chat
-> handoff to ingest-lifecycle if official ingest is truly needed
```

---

## 3. Input Contract

```yaml
KNOWLEDGE INTAKE REQUEST:
  source_input: "[path | URL | uploaded file | existing workspace file]"
  user_intent: "PREVIEW | OFFICIAL_INGEST | AUTO_ROUTE"
  artifact_type: "source_document | code | workflow_or_rule | report_or_log | wiki_atom | visual_asset | unknown"
  complexity_hint: "LOW | MEDIUM | HIGH | UNKNOWN"
```

---

## 4. Routing Contract

```yaml
KNOWLEDGE INTAKE ROUTING:
  slash_command_ingest: "BYPASS_TO_INGEST_LIFECYCLE"
  natural_language_preview: "PREVIEW_MODE"
  natural_language_official_ingest: "HANDOFF_TO_INGEST_LIFECYCLE"
  default_preview_mode: "CHAT_ONLY"
  preview_write_policy: "ONLY_WHEN_REQUESTED_BY_WORKFLOW_OR_USER_TEXT"
  mid_task_confirmation_required: "NO"
```

Any preview output must include this trace before summary/report content:

```yaml
ROUTING_DECISION:
  cwd_context: "vault_root | workspace_child"
  selected_workspace: "workspaces/learning | workspaces/source-lab | workspaces/research-lab | NONE"
  mode: "learning-first | source-preview | research-preview | official-ingest"
  reason: "[why this route was selected]"
  loaded_overlay: "[workspace AGENTS.md path | NONE]"
  action_type: "read-only/chat-only | write-preview-artifact | state-changing"
  write_artifact: "NO | YES"
  canonical_write: "NO | YES"
  ingest_lifecycle: "NO | YES"
  forbidden_actions_checked:
    - "no 3-resources write"
    - "no Atom generation"
    - "no VERIFIED/SYNTHESIZED"
    - "no ingest-lifecycle"
```

Allowed:
- classify user intent
- detect artifact type
- accept NotebookLM recon notes as non-canonical input
- select preview mode
- produce preview report
- handoff official ingest requests to `ingest-lifecycle`

Forbidden:
- must not intercept `/ingest`
- must not create `source_id`
- must not create `SOURCE_PREP_REPORT`
- must not create `SOURCE_AUDIT_REPORT`
- must not create `INGEST_INPUT_LOCK`
- must not create `MAP_[ID]`
- must not create `NAMING_LOCK_[ID]`
- must not create Atom files
- must not write to `3-resources/`
- must not satisfy official ingest gates
- must not treat NotebookLM answer text as source of truth

---

## 5. Preview Write Policy

Preview runtime default is `CHAT_ONLY`.

Preview artifact writing is allowed only when the user request or workflow explicitly asks for a persisted preview artifact.

During an approved implementation goal, Codex must not ask for additional confirmation inside the declared scope.

```yaml
PREVIEW EXECUTION MODE:
  mode: "CHAT_ONLY | WRITE_PREVIEW_ARTIFACT"
  write_allowed: "YES if requested by current workflow/user text"
  mid_task_confirmation_required: "NO"
```

Preview artifact location:

```text
00_Inbox/preview/
```

Do not use global names:
- `QUICK_INDEX.md`
- `index.md`
- `SOURCE_*`
- `MAP_[ID]`
- `NAMING_LOCK_[ID]`
- `INGEST_*`

Use source-scoped names:
- `PREVIEW_[safe_stem]_YYYYMMDD.md`
- `QUICK_INDEX_[safe_stem]_YYYYMMDD.md`

Do not implement `PREVIEW_REGISTRY.md` in this phase.

Optional recon artifact:
- `NOTEBOOKLM_RECON_[SOURCE_ID].md`
- default location:
  - `1-projects/NOTEBOOKLM_RECON_[SOURCE_ID].md`
- `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/NOTEBOOKLM_RECON_[SOURCE_ID].md` is debug/runtime-only and should not be used unless explicitly requested
- this artifact is auxiliary analysis, not canonical ingest fuel

---

## 6. Preview Modes

All preview modes are read/analyze/recommend by default.

### source-preview

For:
- PDF, DOCX, PPTX, Markdown, web scrape, transcript, source document

Optional non-canonical inputs:
- NotebookLM query notes
- manually pasted reconnaissance notes

```yaml
ROUTING_DECISION:
  cwd_context: "vault_root | workspace_child"
  selected_workspace: "workspaces/learning | workspaces/source-lab | workspaces/research-lab | NONE"
  mode: "learning-first | source-preview | research-preview"
  action_type: "read-only/chat-only | write-preview-artifact"
  write_artifact: "NO | YES"
  canonical_write: "NO"
  ingest_lifecycle: "NO"
SOURCE PREVIEW REPORT:
  artifact_type: "source_document"
  source_input: "[path]"
  recon_input: "NONE | NOTEBOOKLM_QUERY_NOTES | MANUAL_RECON_NOTES"
  learning_status: "PREVIEW_ONLY"
  canonical_status: "NON_CANONICAL"
  source_id: "NONE"
  write_artifact: "NO | YES"
  ingest_recommendation: "SKIP | KEEP_SUMMARY | INGEST_OFFICIAL"
  confidence: "LOW | MEDIUM | HIGH"
```

### code-preview

For:
- `scripts/*.py`
- `.agent/skills/*/scripts/*.py`
- `.kiro/*.py`
- `tests/*.py`

```yaml
CODE PREVIEW REPORT:
  artifact_type: "code"
  canonical_status: "NON_CANONICAL_ANALYSIS"
  side_effect_risk: "NONE | LOW | MEDIUM | HIGH"
  owner_agent: "@engineer | @auditor | @healer | @pm"
  recommended_next_action: "READ_ONLY | WRITE_SPEC | TEST | PATCH | ESCALATE"
```

No patching from preview mode.

### workflow-preview

For:
- `AGENTS.md`
- `WORKSPACE_OVERVIEW.md`
- `.agent/workflows/*.md`
- `.agent/skills/*/SKILL.md`
- `.agent/rules/*.md`

```yaml
WORKFLOW PREVIEW REPORT:
  artifact_type: "workflow_or_rule"
  canonical_status: "NON_CANONICAL_ANALYSIS"
  affected_boundaries:
    - "entrypoint"
    - "artifact contract"
    - "agent authority"
    - "approval gate"
  risk_level: "LOW | MEDIUM | HIGH"
  recommended_owner: "@pm | @auditor | @engineer"
  recommended_next_action: "KEEP | PATCH_SPEC | PATCH_RULE | ESCALATE"
```

### report-preview

For:
- `logs/log_YYYY_MM_DD.md`
- `Analysis_*.md`
- `*_REPORT.md`
- `error_log.md`

```yaml
REPORT PREVIEW:
  artifact_type: "report_or_log"
  current_state: "DONE | BLOCKED | WAITING_FOR_REVIEW | UNKNOWN"
  next_action: "NONE | RESUME | AUDIT | HEAL | ASK_USER"
  related_artifacts:
    - "[path]"
  recommended_owner: "@pm | @healer | @auditor | @engineer"
```

### notebooklm-recon-preview

For:
- NotebookLM query output
- NotebookLM answer notes attached in chat

```yaml
NOTEBOOKLM RECON REPORT:
  artifact_type: "source_document_recon"
  recon_status: "UNVERIFIED"
  canonical_status: "NON_CANONICAL_ANALYSIS"
  source_trace_status: "PARTIAL | UNKNOWN"
  recommended_next_action: "RUN_SOURCE_PREVIEW | ASK_FOR_SOURCE | HANDOFF_OFFICIAL_INGEST | STOP"
```

NotebookLM recon preview chỉ có quyền:
- gom câu trả lời nhanh thành hypothesis
- đánh dấu claim cần kiểm chứng
- đề xuất chỗ nào nên đọc kỹ hơn trong source chính

### atom-preview

For:
- `3-resources/wiki/concepts/*.md`
- `3-resources/wiki/entities/*.md`
- `3-resources/wiki/sources/*.md`
- `3-resources/wiki/synthesis/*.md`

```yaml
ATOM PREVIEW REPORT:
  artifact_type: "wiki_atom"
  current_status: "DRAFT | VERIFIED | SYNTHESIZED | STALE | UNKNOWN"
  source_trace_status: "OK | WEAK | MISSING"
  link_status: "OK | BROKEN | UNKNOWN"
  recommended_next_action: "NONE | AUDIT | LINT | REVIEW | ESCALATE"
```

Hard rule: agent must not set `SYNTHESIZED`.

### asset-preview

For:
- images
- figures
- tables
- screenshots
- raw_assets
- diagram exports

```yaml
ASSET PREVIEW REPORT:
  artifact_type: "visual_asset"
  canonical_status: "NON_CANONICAL_UNLESS_REGISTERED"
  likely_source: "[path | UNKNOWN]"
  visual_type: "diagram | chart | table | screenshot | unknown"
  recommended_next_action: "REGISTER_IN_FIGURES | IGNORE | ASK_USER | INGEST_OFFICIAL"
```

---

## 7. Output Contract

```yaml
KNOWLEDGE INTAKE REPORT:
  routing_decision: "PRESENT | MISSING"
  source_input: "[path]"
  artifact_type: "[detected type]"
  selected_lane: "PREVIEW | OFFICIAL_INGEST | BLOCKED"
  selected_preview_mode: "source-preview | code-preview | workflow-preview | report-preview | atom-preview | asset-preview | NONE"
  preview_artifact: "[path | NONE]"
  official_ingest_entrypoint: ".agent/workflows/ingest-lifecycle.md | NONE"
  canonical_core_touched: "YES | NO"
  status: "DONE | HANDOFF | BLOCKED"
  gate_reasons:
    - "[reason]"
```

---

## 8. Guardrails

- `/ingest [file]` bypasses `knowledge-intake`.
- Preview artifacts are `NON_CANONICAL`.
- Preview artifacts cannot satisfy official ingest gates.
- Preview artifacts must not contain a real `source_id`; use `source_id: "NONE"`.
- `knowledge-intake` must not run promote, rebuild, actual ingest, or atom generation.
- `knowledge-intake` must not write to `3-resources/`.
- Official ingest remains owned by `ingest-lifecycle`.
