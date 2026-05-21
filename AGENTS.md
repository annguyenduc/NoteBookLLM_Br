# AGENTS.md — NoteBookLLM_Br

> Đọc file này TRƯỚC KHI thực hiện bất kỳ tác vụ nào.
> Mục tiêu hệ thống: Second brain theo mô hình LLM Wiki — ingest tài liệu thô → atomic wiki nodes → synthesis có thể verify nguồn.

---

## Worktree execution boundary

For autonomous or large tasks, agents must follow:

```text
.agent/rules/worktree-agent.md
```

Agents must not modify `main` directly. Any task that edits files must run from a branch named `agent/*` inside `D:\_agent_worktrees\`.

If the current branch is `main`, the agent must stop and report `WRONG_BRANCH_OR_WORKTREE`.

---

## RUNTIME SOURCE OF TRUTH

`AGENTS.md` là runtime source of truth cho agent trong repo này.
Các file khác chỉ là role rule, workflow, skill hoặc reference. Nếu có mâu thuẫn khi chạy thật, ưu tiên theo thứ tự:

1. User instruction trong phiên hiện tại, nếu không vi phạm runtime safety.
2. `AGENTS.md`.
3. `.agent/rules/CORE.md`.
4. `.agent/rules/[agent].md`.
5. Workflow được gọi trực tiếp.
6. Skill instruction.
7. `.agent/docs/GEMINI.md` chỉ là governance reference/archive, không override runtime.

---

## STARTUP PROFILE (Bắt buộc mỗi phiên)

Agent phải chọn đúng profile trước khi đọc context.

### MICRO
Dùng cho local model <= 3B hoặc task rất nhỏ.
Primary target: Llama/Qwen/Gemma/Phi class <= 3B hoặc model có context/reasoning rất hạn chế.
Không tối ưu workflow mặc định quanh 8B; chỉ dùng MICRO cho 8B nếu AN yêu cầu test rõ.

Đọc:
1. `AGENTS.md`
2. `.agent/rules/CORE.md`
3. Current user task
4. File được user chỉ đích danh

Không đọc mặc định: `SOUL.md`, `USER.md`, `WORKSPACE_OVERVIEW.md`, `.agent/docs/GEMINI.md`, unrelated skills, full skill files, multiple wiki skills, non-essential MCP schemas, browser/search/github MCP, subagent-driven-development, writing-plans full workflow, templates dài, log lịch sử.

Hard rules:
- Không write vào `raw_*/` hoặc modify `3-resources/raw_*`.
- Không bulk-edit vault files.
- Chỉ load một task-specific skill summary nếu cần.
- Ưu tiên direct file operations và tránh recursive search nếu không cần.
- Không multi-agent dispatch trừ khi AN yêu cầu.
- Dùng one-step execution với user checkpoints.
- Với read-only audit trong MICRO, giới hạn scope mặc định vào `AGENTS.md`, `.agent/rules/CORE.md`, active role rule, và file user chỉ đích danh; chỉ mở rộng sang root governance/workflow/script files nếu AN yêu cầu hoặc có blocker trực tiếp.
- Chạy `synthesis_guard.py check` trước mọi write vào `synthesis/`.
- Chỉ AN được set `SYNTHESIZED`.
- Dùng `scripts/maintenance/circuit_breaker.py` cho promote operation.
- Sau mỗi 3 turns, tóm tắt working history thành 3 bullets trước khi tiếp tục.
- Trong MICRO mode, không append "Summary of Work" trừ khi AN yêu cầu rõ hoặc đây là assistant turn thứ 3 trong task hiện tại.

Default MCP/tools: `filesystem` only. Bật `sqlite` chỉ khi task cần query/index. Không bật github/browser/search/scrape trừ khi AN yêu cầu rõ.

### NORMAL
Dùng cho cloud model hoặc task vault thông thường.
Đọc:
1. `AGENTS.md`
2. `.agent/rules/CORE.md`
3. `WORKSPACE_OVERVIEW.md`
4. `.agent/rules/[agent].md`

### FULL
Dùng khi task phức tạp, conflict rule, ingest dài, hoặc audit hệ thống.
Đọc:
1. NORMAL profile
2. Relevant `SKILL.md`
3. `.agent/docs/GEMINI.md` chỉ khi cần resolve conflict

### Secret Handling
Không load `.env` mặc định.
Chỉ đọc secret khi script bắt buộc cần và User đã duyệt action có side effect.

### Session End
Sau task có side effect, ghi log vào `3-resources/wiki/logs/log_YYYY_MM_DD.md`.

> **Governance reference/archive**: [[.agent/docs/GEMINI.md]] chỉ dùng để tra cứu lịch sử rule hoặc giải thích khi cần, không override runtime.

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
| **@healer** | `@healer` | Sửa lỗi link, rollback vi phạm | `.agent/rules/healer.md` |

> **Nguyên tắc**: Mỗi agent chỉ đọc rules của mình + CORE.md.
> Khi gặp tình huống phức tạp cần tra cứu lịch sử rule → đọc phần liên quan trong [[.agent/docs/GEMINI.md]], không inject toàn bộ mặc định.

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

> **Lưu ý:** Các hướng dẫn chi tiết về `Skill Self-Improvement Protocol`, `Skill Priority Override`, `Skill-Creator Boundary` và `Skill Overlap Dispatch Boundaries` đã được di chuyển sang [[.agent/docs/GEMINI.md]] để tra cứu.

> **Lưu ý:** Các hướng dẫn về MCP Policy, Ingest Source Policy, Giao thức Vận hành, và Cấu trúc Thư mục đã được chuyển sang [[.agent/docs/GEMINI.md]] để giảm tải Context Window.
