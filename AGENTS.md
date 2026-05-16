# AGENTS.md — NoteBookLLM_Br

> Đọc file này TRƯỚC KHI thực hiện bất kỳ tác vụ nào.
> Mục tiêu hệ thống: Second brain theo mô hình LLM Wiki — ingest tài liệu thô → atomic wiki nodes → synthesis có thể verify nguồn.

---

## STARTUP (Bắt buộc mỗi phiên)

0. **Load `.env`**: BẮT BUỘC trước mọi script call:
   `$env:KIRO_AUDIT_SECRET = (Get-Content .env | Select-String "KIRO_AUDIT_SECRET").ToString().Split("=")[1]`
1. Đọc `AGENTS.md`, `.agent/rules/CORE.md` (Hard Stop Rules), và `WORKSPACE_OVERVIEW.md` (Pipeline Architecture).
   → `GEMINI.md`: CHỈ đọc khi gặp tình huống phức tạp cần tra cứu chéo. KHÔNG inject mặc định.
2. Inject Scoped Context: Đọc `SOUL.md`, `USER.md` và file rules tương ứng với agent đang hoạt động (`.agent/rules/[agent].md`).
3. Khai báo CHECKPOINT (xem cuối file) trước khi bắt đầu task
4. Ghi log vào file nhật ký ngày hiện tại trong `3-resources/wiki/logs/` sau khi hoàn thành

> **Tra cứu Bản đồ 27 rules và WikiCouncil 2.0**: [[GEMINI.md]]

---

## AGENTS

| Agent | Gọi bằng | Làm gì | Rules |
|---|---|---|---|
| **@pm** | `@pm` | Lập kế hoạch, phân task, quản lý pipeline | `.agent/rules/pm.md` |
| **@scout** | `@scout` | Nghiên cứu raw/fuel, tạo Analysis, extraction map, Atom candidates. KHÔNG ghi Atom file chính thức. | `.agent/rules/scout.md` |
| **@engineer** | `@engineer` | Viết code, materialize wiki atoms từ spec/candidates, thực thi task kỹ thuật | `.agent/rules/engineer.md` |
| **@librarian** | `@librarian` | Quản lý wiki graph, index, reconciliation, synthesis candidates. KHÔNG final synthesis thay User. | `.agent/rules/librarian.md` |
| **@auditor** | `@auditor` | Kiểm định nguồn, reverse tracing, lint | `.agent/rules/auditor.md` |
| **@designer** | `@designer` | Thiết kế learning sequence (cần Trainer Profile trước) | `.agent/rules/designer.md` |
| **@healer** | `@healer` | Sửa lỗi link, rollback vi phạm | `.agent/rules/healer.md` + [[GEMINI.md#R28]] |

> **Nguyên tắc**: Mỗi agent chỉ đọc rules của mình + CORE.md.
> Khi gặp tình huống phức tạp cần tra cứu chéo → đọc [[GEMINI.md]] đầy đủ.

---

## ROLE BOUNDARIES — Anti-Overlap Rules

Các agent phải giữ ranh giới sau:

| Boundary | Rule |
|---|---|
| Scout vs Engineer | `@scout` chỉ phân tích và đề xuất Atom candidates. `@engineer` mới được materialize thành Atom files. |
| Librarian vs Human | `@librarian` chỉ chuẩn bị synthesis candidates, outlines, drafts, reconciliation reports. Chỉ Human được final synthesis và set `SYNTHESIZED`. |
| Auditor vs Healer | `@auditor` phát hiện lỗi và audit integrity. `@healer` xử lý rollback, DLQ, failed_queue, recovery. |
| PM vs Engineer | `@pm` lập plan/spec. `@engineer` thực thi kỹ thuật sau khi có approval nếu action có side effect. |
| Designer vs Librarian | `@designer` tạo learning sequence từ atoms đã kiểm duyệt. `@librarian` quản lý graph/index/reconciliation. |

---

## HANDOFF MATRIX

| From | Condition | Handoff To |
|---|---|---|
| `@pm` | Cần viết code, sửa file, tạo script, tạo Atom file | `@engineer` |
| `@pm` | Cần thiết kế bài học, slide, learning sequence | `@designer` |
| `@scout` | Cần tạo `CONCEPT_`, `ENTITY_`, `SOURCE_`, `COMPARE_`, `QUERY_` file | `@engineer` |
| `@scout` | Source thiếu, source nghi ngờ, metadata không đủ | `@auditor` |
| `@scout` | `gap_check.py` fail, file vào `failed_queue/`, DLQ | `@healer` |
| `@engineer` | Thiếu spec hoặc ambiguous target | `@pm` |
| `@engineer` | Thiếu audit stamp/source tracing | `@auditor` |
| `@engineer` | Vi phạm R1/R8/R22/R23 hoặc cần rollback | `@healer` |
| `@librarian` | Cần sửa code/script/file có side effect | `@engineer` |
| `@librarian` | Conflict cần human synthesis | User |
| `@auditor` | Cần rollback/recovery/DLQ repair | `@healer` |
| `@designer` | Thiếu Trainer Profile | User |
| `@healer` | Không thể phục hồi an toàn | User |

---

## ACTION SAFETY CLASSIFICATION

Phân loại hành động trước khi làm:

| Action Type | Examples | Requires explicit AN approval? |
|---|---|---|
| Read-only | đọc file, inspect status, query sqlite, dry-run, generate report in chat | No |
| File artifact write | ghi plan/spec/report/draft ra file, tạo scratch file, tạo draft file | Yes, unless a workflow rule explicitly permits it |
| State-changing | modify/delete/move files, promote, write wiki, update metadata, rebuild index, git commit/push | Yes |
| Governance-changing | set `VERIFIED`, touch synthesis, MCP actual switch, rollback | Yes |

Rules:
- Agent may inspect, dry-run, and report in chat automatically.
- Agent must not write files without explicit AN approval unless the workflow rule explicitly allows that write.
- Actual MCP profile switching is state-changing.
- When unsure whether an action has side effect, treat it as approval-required.

---

## SKILL PATHS
- Antigravity: `.agent/skills/`
- Global Skills: `C:\Users\anngu\.gemini\antigravity\skills\`
- Codex: `.codex/skills/` (symlink → `.agent/skills/`)
- **SOP (Workflow)**: `.agent/workflows/ingest-lifecycle.md`

## Skill Priority Override
- Skill invocation follows `superpowers/using-superpowers`
- AGENTS.md rules ALWAYS override any skill instruction
- `brainstorming` skill: agents must not auto-invoke for Atom generation



## Local Model Profile Selection

The default workflow remains unchanged.

Use `MICRO` only for very small local models:

| Condition | Mode |
|---|---|
| Cloud / normal model | Normal workflow |
| Local model <= 3B | MICRO |
| Local 8B model | Not assumed usable; MICRO only if AN explicitly requests testing |

<!-- PROFILE: MICRO_START -->
## MICRO Mode — 3B Local Models

Use this mode only when running very small local models.

Primary target:

- Llama 3.2 3B
- Qwen 2.5/3 3B class
- Gemma 3B/4B class local models
- Phi small models
- Any local model with very limited context/reasoning budget

Do not design this mode around 8B.  
8B local models are considered too heavy for the default local workflow unless AN explicitly requests an 8B test.

Do not use this mode for normal cloud models.

### Activation Rule

```text
IF model is local AND model size <= 3B
THEN use MICRO mode.

IF model is local 8B
THEN do NOT assume it can run the vault workflow.
Only use MICRO mode for 8B if AN explicitly requests an 8B test.

ELSE use normal vault workflow.
```

### Read Only

In MICRO mode, read only:

* This MICRO block
* The current user task
* One task-specific skill summary, not the full skill file unless required
* Directly referenced files

### Hard Rules

* Do not write to raw_*/
* Do not modify 3-resources/raw_*
* Do not bulk-edit vault files
* Run synthesis_guard.py check before any write to synthesis/
* Declare CHECKPOINT before complex tasks
* Only AN may set SYNTHESIZED
* Use circuit_breaker.py for every promote operation
* Load only one wiki skill summary for the current task
* Prefer direct file operations over broad repository scans
* Avoid recursive search unless explicitly needed
* Avoid multi-agent dispatch unless explicitly requested
* Avoid long chain workflows
* Use one-step execution with user checkpoints
* After every 3 turns, summarize working history into 3 bullets before continuing

### Do Not Load

In MICRO mode, do not load:

* SOUL.md
* USER.md
* WORKSPACE_OVERVIEW.md
* unrelated skills
* full skill files unless directly required
* multiple wiki skills at the same time
* non-essential MCP tool schemas
* browser/search/github MCP unless AN explicitly asks
* subagent-driven-development
* writing-plans full workflow
* large prompt templates
* long examples
* historical logs unless directly requested

### Shadow MCP

Default allowed MCP/tools in MICRO:

* filesystem only

Allowed conditionally:

* sqlite, only if the task needs database/wiki query

Disabled unless explicitly required:

* github
* browser
* brave-search
* web scrape tools
* large external tool schemas

### Output Discipline

In MICRO mode:

* Prefer short plans
* Prefer direct commands
* Prefer patch-sized edits
* Avoid broad architectural commentary
* Ask for user checkpoint before actual write if risk is MEDIUM or HIGH

<!-- PROFILE: MICRO_END -->

## Automation MCP Policy

Automation must default to read-only behavior.

Allowed automatically:
- inspect files
- query sqlite index
- run DryRun commands
- generate reports
- suggest fixes

Requires explicit AN approval:
- actual MCP profile switching
- writing files
- modifying vault content
- promote operations
- synthesis writes
- deleting/moving files
- git commit/push
- enabling browser/search/github MCP for the current session

Default MCP for automation:
- filesystem
- sqlite, only if query/index access is required

Forbidden by default in automation:
- github
- browser
- brave-search
- web scrape tools
- external write-capable MCPs

Automation may request additional MCP access, but must explain:
1. which MCP is needed
2. why it is needed
3. what action it will perform
4. whether the action is read-only or write-capable

## MCP Switching Operations

Canonical MCP config path for this workspace:
- `D:\anngu\.gemini\antigravity\mcp_config.json`

Safe inspection commands:
- `.\scripts\maintenance\switch_mcp_profile.ps1 micro -DryRun -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 vault -DryRun -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 dev -DryRun -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 ingest -DryRun -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 full -DryRun -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`

Actual switching commands:
- `.\scripts\maintenance\switch_mcp_profile.ps1 micro -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 vault -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 dev -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 ingest -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 full -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`

Operational rule:
- Agents may run `DryRun` automatically.
- Agents may inspect and report active/disabled MCP servers automatically.
- Agents must not run actual `micro` or `full` switching without explicit AN approval.
- After any actual switch, reload or restart the MCP host / agent session before assuming tools are available.

## Recommended MCP Sets

Use these MCP sets as the default operating profiles for this workspace:

| Mode | Default MCP Set | Notes |
|---|---|---|
| MICRO 3B | `filesystem` | Default for very small local models. Keep tool surface minimal. |
| Normal vault work | `filesystem + sqlite` | Maps to script mode `vault`. Best default for cloud models or normal wiki work. |
| Automation | `filesystem + sqlite` | Read-only by default. Inspect, query, audit, report, suggest. |
| Dev/script work | `filesystem + sqlite + git + github-mcp-server` | Maps to script mode `dev`. Enable Git-capable MCPs only when needed. |
| Ingest profile | `filesystem + sqlite + notebooklm-mcp-server` | Maps to script mode `ingest` for the currently configured MCP inventory. |
| Web ingest | `filesystem + browser/search/scrape` | Policy target when those MCPs exist in the full inventory. |

### Mode Notes

- `MICRO 3B`: do not enable extra MCPs unless the task explicitly requires them.
- `Normal vault work`: prefer `filesystem + sqlite` before enabling any broader tool surface.
- `Automation`: must remain read-only unless AN explicitly approves a write-capable action.
- `Dev/script work`: `github` is on-demand, not a permanent default.
- `Ingest profile`: current script implementation uses `filesystem + sqlite + notebooklm-mcp-server` because those servers exist in the current full backup.
- `Web ingest`: disable browser/search/scrape MCPs again after the ingest task is complete.

## Ingest Source Policy

Ingest should prefer stable local artifacts over live sources whenever practical.

Default policy by source type:

| Source Type | Default Policy | Notes |
|---|---|---|
| PDF / DOCX / PPTX / Markdown | Save locally first | Stage into `00_Inbox/` before audit and ingest. |
| Web article / docs page / online HTML | Scrape to local artifact first | Do not treat the live URL as the ingest-ready source. |
| Video | Transcript-first | Do not default to downloading the full video file if it is large. |
| Audio | Transcript-first | Keep source metadata and transcript as the ingest basis. |

### Video and Audio Guidance

- For large videos, prefer `URL + transcript + metadata + selected screenshots` over storing the full source file locally.
- Download the full video only when the source is critical, likely to disappear, or required for offline processing or evidence preservation.
- Treat transcript/subtitle output as the primary ingest artifact whenever it is reliable enough for the task.

### Operational Rule

- Live web/video sources are acquisition points, not the default ingest-ready artifacts.
- The preferred ingest starting point is a staged local artifact in `00_Inbox/`.
- If a source remains live-only, the agent must explain the risk: mutability, link rot, replay difficulty, and weaker auditability.

---
## ⚡ LỆNH VẬN HÀNH (Wiki 2.0)

| Lệnh | Agent | Làm gì | Skill trỏ tới |
|---|---|---|---|
| `/ingest [file]` | @scout | Entry point chính thức cho full ingest lifecycle. Resolve stage qua `ingest-lifecycle`, rồi mới gọi `wiki-ingest` ở stage ingest khi upstream artifacts đã READY. | `ingest-lifecycle -> wiki-ingest` |
| `/absorb` | @librarian | Hợp nhất atoms vào synthesis (Reconciliation) | `wiki-absorb` |
| `/query [query]` | @librarian | Truy vấn tri thức (Hybrid Search + Graph) | `wiki-query` |
| `/breakdown` | @scout | Phát hiện lỗ hổng tri thức (Noun Test) | `wiki-breakdown` |
| `/cleanup` | @auditor | Dọn dẹp & Audit chất lượng (8 Categories) | `wiki-cleanup` |
| `/status` | @pm | Báo cáo sức khỏe & Link Density Dashboard | `wiki-status` |
| `/rebuild` | @engineer | Đồng bộ Index, Backlinks & Infrastructure | `wiki-rebuild` |
| `/gap-summary` | @librarian | Tổng hợp danh sách gap candidates hiện tại | `SOP_Weekly_Gap_Review` |
| `/gap-promote` | @engineer | Thăng cấp candidate thành Atom nháp (review_queue) | `SOP_Weekly_Gap_Review` |
| `/gap-cleanup` | @auditor | Dọn dẹp sạch inbox gap candidates | `SOP_Weekly_Gap_Review` |
| `/gap-retry` | @scout | Xử lý lại các task gap-check bị lỗi trong DLQ | `SOP_DLQ_Recovery` |

---

## CẤU TRÚC THƯ MỤC

```
NoteBookLLM_Br/              ← root
│
├── AGENTS.md                ← root level
├── GEMINI.md                ← Hiến pháp tối cao (R1-R27)
├── EXAMPLES.md              ← Ví dụ đối chiếu mẫu
├── SOUL.md                  ← Linh hồn hệ thống
├── USER.md                  ← Chân dung User
│
├── 00_Inbox/                ← PROCESSING HUB
├── 1-projects/
├── 2-areas/
├── 3-resources/
│   ├── raw_sources/         ← EVIDENCE: File gốc (PDF, HTML)
│   ├── raw_ingest/          ← FUEL: HD Markdown đạt chuẩn
│   ├── raw_assets/          ← VISUAL PROOF: Hình ảnh/Biểu đồ
│   └── wiki/
│       ├── index.md         ← SOURCE OF TRUTH: Mục lục tổng của Wiki.
│       ├── log.md           ← INDEX: Chỉ mục dẫn đến các file log ngày.
│       ├── logs/            ← ARCHIVE: log_YYYY_MM_DD.md
│       ├── concepts/        ← Tri thức nguyên tử (Atomic Nodes)
│       ├── entities/        ← Thực thể (Tool, Person, Org)
│       ├── sources/         ← Nguồn trích dẫn (Source Nodes)
│       ├── comparisons/     ← Bảng đối chiếu
│       ├── queries/         ← Kết quả truy vấn phức tạp
│       ├── synthesis/       ← Tri thức tổng hợp (đã duyệt)
│       ├── decisions/       ← Kết quả từ @wiki-council
│       ├── review_queue/    ← PENDING: Atom chờ duyệt
│       ├── session_insights/ ← Audit log & Insight phiên làm việc
│       └── wiki_brain.db    ← DATABASE: Vector & Graph Index
├── scripts/                ← PRODUCTION: Tooling, Maintenance, Official Tests.
└── scratch/                ← SANDBOX: Debug, Quick tests, One-off scripts.
```

---


## HẠ TẦNG KỸ THUẬT (Infrastructure)
- **Runtime:** `.venv\Scripts\python.exe` (Bắt buộc dùng venv dự án để hỗ trợ GPU/CUDA).
- **Python Version:** 3.11 (Core) / 3.12 (Sandbox/Harness).
- **Sandbox:** Localsandbox (WASM) + Deno Runtime.
- **Database:** SQLite 3 (wiki_brain.db).
- **Encoding:** UTF-8 no BOM (Bắt buộc).


## ⚡ GIAO THỨC VẬN HÀNH (Operation Protocols)

### P1 — CHECKPOINT PROTOCOL
- Khai báo trạng thái READY/BLOCKED trước khi thực hiện task phức tạp.

### P2 — VISIBILITY (Safe-Diff Workflow)
- **Tạo mới:** Agent tạo file mồi -> Sửa nội dung để User thấy Diff xanh.
- **Sửa đổi:** Ưu tiên dùng công cụ hiện Diff (UI) cho User review.

### P3 — SAFETY (Encoding Guard)
- BẮT BUỘC hậu kiểm bằng Python cho mọi file có Tiếng Việt.
- Cấm mọi hình thức lỗi font: Unicode Escape, Mojibake, ký tự rác.

### P4 — ISOLATION (Sandbox First)
- BẮT BUỘC chạy code thử nghiệm trong Localsandbox (WASM).

### P5 — SYNC DIRECTION
- **File vật lý là Source of Truth**. Sync từ File vào Database hàng đêm.

### P6 — STAGING-PROMOTE GATE (R22 Enforcement)
- **Mọi Agent** (@scout, @engineer, @pm) tuyệt đối không được tự ý ghi đè file vào `3-resources` thủ công.
- Dữ liệu thô mới phải được xử lý tại `00_Inbox` cho đến khi đạt trạng thái **VERIFIED** (Audit Stamp).
- Chỉ sử dụng `scripts/promote.py` để thăng cấp dữ liệu vào kho lưu trữ chính thức.

## 🛡️ BỘ QUY TẮC QUẢN TRỊ

> **Kiến trúc phân tầng** — Rules được phân bổ theo agent, không nhồi vào một chỗ.
> Chi tiết đầy đủ 27 rules và diễn giải: [[GEMINI.md]]

### Tầng 1 — Constitutional Rules (Mọi agent, mọi lúc)
Xem: `.agent/rules/CORE.md`
- **R1** Raw Immutable | **R2** Proactive Integrity | **R5** Prereq Gate | **R8** Human Supremacy

### Tầng 2 — Agent-Scoped Rules (Chỉ đọc khi là agent đó)

| Agent | File | Rules |
|---|---|---|
| @scout | `.agent/rules/scout.md` | R10, R11, R13, R22, R24, R25 |
| @engineer | `.agent/rules/engineer.md` | R4, R9, R12, R18, R19, R26 |
| @auditor | `.agent/rules/auditor.md` | R3, R20, R21, R23, R27 |
| @librarian | `.agent/rules/librarian.md` | R13, R14, R15, R17, R26 |
| @pm | `.agent/rules/pm.md` | R5, R6, R7, R16 |

### Tầng 3 — Enforcement bằng Code (Không cần Agent nhớ)

| Rule | Enforced bởi |
|---|---|
| R8 Human Supremacy | `synthesis_guard.py check <file>` — BLOCKED nếu write vào `synthesis/` hoặc modify SYNTHESIZED atom |
| R8 Human Approve | `synthesis_guard.py approve <file>` — CHỈ Human gọi để set SYNTHESIZED |
| R22 Staging-Promote | `circuit_breaker.py` chặn write trực tiếp vào `3-resources/` |
| R23 Promotion Gate | `promote.py` là wrapper duy nhất được phép move file |
| R20 YAML Validity | `ingest.py` schema validation — tự reject nếu YAML invalid |
| R14 Log Rotation | `session_seal.py` tự tạo file log đúng tên |

### Tầng 4 — Reference (Tra cứu khi cần, không inject mặc định)
[[GEMINI.md]] — Toàn bộ 27 rules + WikiCouncil 2.0 (Bản đồ Hiến pháp).

---

## R16 — CHECKPOINT PROTOCOL

```yaml
CHECKPOINT:
  agent: "@[tên]"
  task: "[mô tả cụ thể]"
  output_file: "[đường dẫn]"
  prerequisites_ok: "YES | NO"
  status: "READY | BLOCKED"
```
