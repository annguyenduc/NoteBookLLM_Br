# AGENTS.md - NoteBookLLM_Br

> Đọc file này trước khi thực hiện bất kỳ tác vụ nào.
> Mục tiêu tối thượng của vault: giúp AN học nhanh hơn và tra cứu nhanh hơn.

---

## Nguồn Sự Thật Khi Chạy (Runtime Source Of Truth)

`AGENTS.md` là nguồn sự thật khi chạy (runtime source of truth) cho agent trong repo này.
Nếu có mâu thuẫn khi chạy thật, ưu tiên theo thứ tự:

1. Chỉ dẫn của user trong phiên hiện tại, nếu không vi phạm an toàn vận hành (runtime safety).
2. `AGENTS.md`.
3. `.agent/rules/CORE.md`.
4. `.agent/rules/[agent].md`.
5. Workflow được gọi trực tiếp.
6. Skill instruction.
7. `.agent/docs/GEMINI.md` chỉ là tài liệu tham chiếu/lưu trữ (reference/archive), không override runtime.

---

## Mặc Định Học Trước (Learning-First Default)

Mặc định của vault không phải là ingest. Mặc định là học nhanh và tra cứu nhanh:

```text
Capture -> Learn Note -> Promote if valuable
```

Diễn giải:

- Thu nhận (Capture): nhận nguồn hoặc câu hỏi.
- Ghi chú học nhanh (Learn Note): tạo bản đồ học, câu trả lời ngắn, câu hỏi chính.
- Nâng cấp nếu đáng giữ (Promote if valuable): chỉ khi AN muốn đưa vào tri thức chính thức.

### Bước 1: Thu Nhận (Capture)

Nguồn mới, tài liệu dài, web scrape, transcript, hoặc file cần đọc nhanh mặc định đi vào làn xem trước/học nhanh (preview/learning lane).

Vị trí mặc định:

```text
00_Inbox/                  # nguồn mới hoặc staging tạm
workspaces/                # xưởng phụ, non-canonical
1-projects/learning_maps/  # learning note / learning map giữ lại để học
```

### Bước 2: Ghi Chú Học Nhanh (Learn Note)

Agent ưu tiên trả lời trong chat. Chỉ ghi file khi user/workflow cho phép.

Learning note luôn là:

```yaml
learning_status: "PREVIEW_ONLY"
canonical_status: "NON_CANONICAL"
source_id: "NONE"
trust: "UNVERIFIED"
```

Learning note không phải Atom, không phải nhiên liệu ingest (ingest fuel), không phải bằng chứng nguồn (source evidence).

### Bước 3: Nâng Cấp Nếu Đáng Giữ (Promote If Valuable)

Chỉ khi AN muốn đưa tri thức vào vault chính thức mới chuyển sang ingest chính thức (canonical ingest):

```text
ingest-lifecycle
```

Official ingest vẫn phải giữ đủ chuỗi gate:

```text
prepare-source -> audit-promote-source -> lock-ingest-input -> ingest -> ingest-generate -> ingest-index-log
```

Đây là chế độ nâng cao/chính thức (advanced/canonical mode), không phải mặc định cho mọi tài liệu.

---

## Bộ MCP Mặc Định (Default MCP Profile)

Default learning mode:

```text
filesystem
notebooklm-mcp-server
sqlite
tavily
```

Vai trò:

- `filesystem`: đọc/ghi file trong vault khi được phép.
- `notebooklm-mcp-server`: hỏi đáp tài liệu dài, tạo bản đồ học (learning map).
- `sqlite`: tra cứu chỉ mục vault, atom, metadata, quan hệ nguồn.
- `tavily`: tìm kiếm web nhanh khi cần bối cảnh bên ngoài.

Tắt mặc định nếu không cần:

```text
github
browser/scrape nặng
local-ai
multi-agent dispatch
```

Nếu Tavily chưa có trong `codex mcp list`, báo thiếu MCP thay vì giả định đã bật.

---

## Ranh Giới Worktree (Worktree Execution Boundary)

For autonomous or large tasks, agents must follow:

```text
.agent/rules/worktree-agent.md
```

Agents must not modify `main` directly. Any task that edits files must run from a branch named `agent/*` inside `D:\_agent_worktrees\`.

If the current branch is `main`, `master`, or the current working directory is `D:\NoteBookLLM_Br`, the agent must stop and report:

```text
WRONG_BRANCH_OR_WORKTREE
```

---

## Đóng Băng Đường Dẫn Cốt Lõi (Core Path Freeze)

Để tái cấu trúc không làm vỡ scripts vận hành, các path sau được đóng băng trong phase hiện tại:

```text
00_Inbox/
1-projects/
2-areas/
3-resources/
4-archive/
.agent/
scripts/
```

Không di chuyển, đổi tên, hoặc đổi nghĩa các path trên nếu chưa có lớp tương thích (compatibility layer) và kiểm tra hồi quy (regression check).

`3-resources/` vẫn là nguồn sự thật chính thức (canonical source of truth):

```text
3-resources/raw_sources/
3-resources/raw_ingest/
3-resources/raw_assets/
3-resources/wiki/
```

---

## Ranh Giới Workspaces

`workspaces/` là vùng làm việc phụ nằm trong vault nhưng không chính thức (non-canonical).

Root vault có thể đọc `workspaces/*/AGENTS.md` để chọn đúng overlay, nhưng không tự động load toàn bộ workspace con.

Nếu current working directory nằm trong `workspaces/[name]/`, agent phải dùng thứ tự runtime:

1. root `AGENTS.md`
2. `workspaces/[name]/AGENTS.md`
3. `.agent/rules/CORE.md`
4. workflow/skill được overlay đó cho phép

Shared agent library luôn nằm ở:

```text
.agent/
```

Workspace con chỉ khai báo overlay: workflow nào active, skill nào allowed, workflow nào forbidden hoặc escalation-only.

Allowed:

- đọc/ghi trong workspace phụ được giao.
- tạo preview, notes, experiments, reports non-canonical.
- tạo candidate package để AN quyết định có promote/ingest không.

Forbidden:

- ghi trực tiếp vào `3-resources/`.
- ghi trực tiếp vào `3-resources/raw_sources/`, `raw_ingest/`, `raw_assets/`, hoặc `wiki/`.
- tạo Atom canonical.
- set `VERIFIED`.
- set `SYNTHESIZED`.
- coi NotebookLM/Tavily output là source of truth.

---

## Workspace Dispatch

Root vault dùng bảng này để route task sang workspace overlay phù hợp:

| Workspace | Khi dùng | Default workflow | Forbidden by default |
|---|---|---|---|
| `workspaces/learning/` | học nhanh, learning map, ghi chú học, ôn tập | `.agent/workflows/learning-first.md` | official ingest, Atom generation, writes to `3-resources/` |
| `workspaces/source-lab/` | preview tài liệu dài, OCR/convert thử, NotebookLM recon | `.agent/skills/process-raw-resource/SKILL.md` | canonical writes, lifecycle artifacts unless AN starts ingest |
| `workspaces/research-lab/` | tìm bối cảnh web, so sánh nguồn, Tavily recon | `.agent/workflows/learning-first.md` | treating web result as source truth |
| `workspaces/dev-lab/` | thử nghiệm script, benchmark, patch kỹ thuật | `.agent/workflows/autonomous-dev-task.md` | touching raw/wiki/synthesis without exact GO |

Escalation rule:

- Nếu workspace con kết luận `PROMOTE`, chỉ báo cáo handoff.
- Chỉ khi AN GO official ingest mới dùng `.agent/workflows/ingest-lifecycle.md`.
- Workspace con không cần đọc chi tiết ingest lifecycle khi chỉ đang học nhanh/preview.

---

## Routing Trace

Mọi request đi qua root dispatch hoặc workspace overlay phải mở đầu output bằng block ngắn:

```yaml
ROUTING_DECISION:
  cwd_context: "vault_root | workspace_child"
  selected_workspace: "workspaces/learning | workspaces/source-lab | workspaces/research-lab | workspaces/dev-lab | NONE"
  mode: "learning-first | source-preview | research-preview | dev-task | official-ingest"
  reason: "[vì sao chọn route này]"
  loaded_overlay: "[path | NONE]"
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

Ví dụ với prompt `Tóm tắt PDF này để tôi học nhanh` từ root:

```yaml
ROUTING_DECISION:
  cwd_context: "vault_root"
  selected_workspace: "workspaces/learning"
  mode: "learning-first"
  reason: "User intent is fast learning summary, not official ingest"
  loaded_overlay: "workspaces/learning/AGENTS.md"
  action_type: "read-only/chat-only"
  write_artifact: "NO"
  canonical_write: "NO"
  ingest_lifecycle: "NO"
  forbidden_actions_checked:
    - "no 3-resources write"
    - "no Atom generation"
    - "no VERIFIED/SYNTHESIZED"
    - "no ingest-lifecycle"
```

Nếu route là preview tài liệu dài cần OCR/convert/NotebookLM recon, chọn `workspaces/source-lab`.
Nếu chỉ học nhanh, tóm tắt, tạo câu hỏi hoặc flashcard, ưu tiên `workspaces/learning`.

---

## Startup Profiles

### MICRO

Dùng cho task nhỏ, local model <= 3B, hoặc khi cần giảm context tối đa.

Đọc:

1. `AGENTS.md`
2. `.agent/rules/CORE.md`
3. Current user task
4. File được user chỉ định

Không đọc mặc định:

```text
SOUL.md
USER.md
WORKSPACE_OVERVIEW.md
.agent/docs/GEMINI.md
unrelated skills
full skill files
non-essential MCP schemas
browser/search/github MCP
log lịch sử
```

Hard rules:

- Không write vào `raw_*/` hoặc modify `3-resources/raw_*`.
- Không bulk-edit vault files.
- Chỉ load một task-specific skill summary nếu cần.
- Ưu tiên direct file operations và tránh recursive search nếu không cần.
- Không multi-agent dispatch trừ khi AN yêu cầu.
- Chạy `synthesis_guard.py check` trước mọi write vào `3-resources/wiki/synthesis/`.
- Chỉ AN được set `SYNTHESIZED`.

### NORMAL

Dùng cho cloud model hoặc task vault thông thường.

Đọc:

1. `AGENTS.md`
2. `.agent/rules/CORE.md`
3. `WORKSPACE_OVERVIEW.md`
4. `.agent/rules/[agent].md` nếu có role rõ

### FULL

Dùng khi task phức tạp, conflict rule, official ingest dài, hoặc audit hệ thống.

Đọc:

1. NORMAL profile
2. Relevant `SKILL.md`
3. `.agent/docs/GEMINI.md` chỉ khi cần resolve conflict

---

## An Toàn Hành Động (Action Safety)

Read-only actions không cần GO:

- đọc file liên quan
- inspect status
- dry-run
- query sqlite/index read-only
- tạo plan/spec/report trong chat

Cần AN GO:

- tạo/sửa/xóa/di chuyển file
- promote operation
- synthesis write
- actual MCP profile switching
- rebuild index
- git commit/push
- script có side effect

Nếu không chắc action có side effect không, coi như cần GO.

---

## Agent Roles

Agent role chỉ load khi task gọi role đó hoặc cần boundary rõ:

| Agent | Call | Purpose | Rules |
|---|---|---|---|
| `@pm` | `@pm` | lập plan, phân task, quản lý pipeline | `.agent/rules/pm.md` |
| `@scout` | `@scout` | preview/source analysis, Atom candidates, không ghi Atom chính thức | `.agent/rules/scout.md` |
| `@engineer` | `@engineer` | code, scripts, materialize theo spec được duyệt | `.agent/rules/engineer.md` |
| `@librarian` | `@librarian` | wiki graph, index, reconciliation, synthesis candidates | `.agent/rules/librarian.md` |
| `@auditor` | `@auditor` | source tracing, audit, lint | `.agent/rules/auditor.md` |
| `@designer` | `@designer` | learning sequence khi có Trainer Profile | `.agent/rules/designer.md` |
| `@healer` | `@healer` | rollback, DLQ, recovery | `.agent/rules/healer.md` |

Ma trận bàn giao chi tiết (handoff matrix) và lịch sử governance nằm trong `.agent/docs/GEMINI.md` khi cần tra cứu, không load mặc định.

---

## Định Tuyến Workflow (Workflow Routing)

Default:

```text
learning-first -> process-raw-resource -> learning note / chat answer
```

Use `knowledge-intake` khi cần route giữa preview và official ingest.

Use `ingest-lifecycle` chỉ khi AN muốn official ingest vào canonical vault.

Slash command:

```text
/ingest [file]
```

phải bypass preview và đi thẳng vào `ingest-lifecycle`.

---

## Secret Handling

Không load `.env` mặc định.
Chỉ đọc secret khi script bắt buộc cần và User đã duyệt action có side effect.

---

## Session End

Sau task có side effect trong vault chính, ghi log vào:

```text
3-resources/wiki/logs/log_YYYY_MM_DD.md
```

Nếu đang trong worktree refactor governance, báo cáo `TASK_REPORT` trước khi merge.

Mỗi phiên có thay đổi trạng thái hoặc tạo future dependency phải cập nhật:

```text
CONTINUITY.md
```

Nội dung bắt buộc:

```yaml
current_state: "[đang ở đâu]"
next_step_for_AN: "[bước tiếp theo để AN check]"
blockers:
  - "[nếu có]"
```

Không để `CONTINUITY.md` dài quá mức; nếu vượt khoảng 500 từ, rút gọn còn trạng thái hiện tại, quyết định đã chốt, blocker, và bước tiếp theo.

---

## Skill Paths

- Antigravity: `.agent/skills/`
- Global Skills: `C:\Users\anngu\.gemini\antigravity\skills\`
- Codex: `.codex/skills/` symlink to `.agent/skills/`
- Official ingest workflow: `.agent/workflows/ingest-lifecycle.md`
- Learning-first workflow: `.agent/workflows/learning-first.md`
