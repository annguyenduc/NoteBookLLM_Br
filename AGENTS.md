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
00_Inbox/sources-pending/  # Nơi chứa các nguồn thô chờ học/ingest cách ly
workspaces/                # xưởng phụ, non-canonical
1-projects/learning_maps/  # learning note / learning map giữ lại để học
```

- **Quy tắc Định danh (source_id Lock)**: Bắt kể ở luồng Learn hay Ingest, mọi tài liệu thô được nạp bắt buộc phải có `source_id`. 
- Agent phải tra cứu `D:\NoteBookLLM_Br\1-projects\sources\source_registry.md` trước tiên. Nếu chưa có, AI tự động sinh `source_id` theo quy tắc `[LOẠI]_[VIẾT_TẮT]` và đăng ký vào bảng trước khi tiến hành bước tiếp theo. Không dùng giá trị "NONE" cho source_id.

### Bước 2: Ghi Chú Học Nhanh (Learn Note)

Agent ưu tiên trả lời trong chat. Chỉ ghi file khi user/workflow cho phép.

Learning note luôn là:

```yaml
learning_status: "PREVIEW_ONLY"
canonical_status: "NON_CANONICAL"
source_id: "REQUIRED" # Bắt buộc ghi nhận source_id đã đăng ký trong source_registry.md
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

Default workspace profile: `micro`

```text
filesystem
```

Vai trò:

- `filesystem`: đọc/ghi file trong vault khi được phép.

Các MCP khác (sqlite, notebooklm, tavily, local-ai, wiki-ops, github, v.v.) bị tắt mặc định ở mức chạy nền và chuyển sang chế độ script theo yêu cầu (On-Demand One-Shot Script) để tiết kiệm tài nguyên RAM.

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

Root vault route task bằng registry chung:

```text
.agent/config/workspace-routing.yaml
```

Registry này là nơi duy nhất sở hữu danh sách workspace, intent, default workflow, và forbidden-by-default. Workflow/skill không được tự hard-code toàn bộ workspace list; chúng chỉ consume và echo `ROUTING_DECISION`.

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
  selected_workspace: "[registry.routes.*.workspace | NONE]"
  mode: "[registry route default_mode]"
  reason: "[vì sao chọn route này]"
  loaded_overlay: "[registry route overlay | NONE]"
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

Nếu route là preview tài liệu dài cần OCR/convert/NotebookLM recon, registry hiện chọn `workspaces/source-lab`.
Nếu chỉ học nhanh, tóm tắt, tạo câu hỏi hoặc flashcard, registry hiện ưu tiên `workspaces/learning`.
Khi thêm workspace mới, cập nhật `.agent/config/workspace-routing.yaml` và workspace overlay, không sửa từng skill/workflow nếu contract không đổi.

---

## Startup Profiles

### STARTUP MINIMAL

Always read:
- `AGENTS.md`
- `.agent/rules/CORE.md`
- `.agent/rules/[active_agent].md`

Do not bulk-load root markdown files.
Root `.md` files are references, not default context.
Load the smallest file or section that answers the current routing question.

### ROOT REFERENCE LOAD POLICY

Default:
- Do not read `WORKSPACE_OVERVIEW.md`, `USER.md`, `SOUL.md`, `GEMINI.md`, `EXAMPLES.md`, or `SKILLS_INDEX.md` during normal startup.

Load conditions:
- Path / folder / ingest / architecture / pipeline question -> `WORKSPACE_OVERVIEW.md`
- User preference / learning / pedagogy question -> `USER.md`
- Governance philosophy / human gate / system identity -> `SOUL.md`
- Rule conflict / hard stop / constitutional lookup -> `GEMINI.md`
- Atom format / naming / markdown convention / examples -> `EXAMPLES.md`
- Skill routing / skill discovery / skill inventory -> `SKILLS_INDEX.md`

If a task needs only one section, read only that section.

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
| `@exam-designer` | `@exam-designer` | ra đề thi, quiz, đáp án, rubric từ kiến thức có sẵn | `.agent/rules/exam-designer.md` |
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
