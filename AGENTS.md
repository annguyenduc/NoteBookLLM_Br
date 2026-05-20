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
7. `GEMINI.md` chỉ là governance reference/archive, không override runtime.

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

Không đọc mặc định: `SOUL.md`, `USER.md`, `WORKSPACE_OVERVIEW.md`, `GEMINI.md`, unrelated skills, full skill files, multiple wiki skills, non-essential MCP schemas, browser/search/github MCP, subagent-driven-development, writing-plans full workflow, templates dài, log lịch sử.

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
3. `GEMINI.md` chỉ khi cần resolve conflict

### Secret Handling
Không load `.env` mặc định.
Chỉ đọc secret khi script bắt buộc cần và User đã duyệt action có side effect.

### Session End
Sau task có side effect, ghi log vào `3-resources/wiki/logs/log_YYYY_MM_DD.md`.

> **Governance reference/archive**: [[GEMINI.md]] chỉ dùng để tra cứu lịch sử rule hoặc giải thích khi cần, không override runtime.

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
> Khi gặp tình huống phức tạp cần tra cứu lịch sử rule → đọc phần liên quan trong [[GEMINI.md]], không inject toàn bộ mặc định.

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

## SKILL SELF-IMPROVEMENT PROTOCOL

Agent KHÔNG được tự sửa production SKILL.md dưới bất kỳ hình thức nào
trừ khi AN đã approve SIP và nói GO rõ ràng.

### Khi nào tạo SIP
Tạo file SIP tại `.agent/skill_reviews/pending/SIP_[YYYYMMDD]_[seq]_[skill_id].md`
khi có ít nhất 1 trigger rõ:
- user_correction
- missing_step
- repeated_failure (≥2 lần trong 7 ngày)
- output_drift
- test_gap

Không tạo SIP cho PASS run bình thường.
Không tạo SIP cho lỗi cá biệt do source file.

### Sau khi tạo SIP
Agent báo AN trong phiên hiện tại: "Đã tạo SIP tại [path]. Cần AN review."
Agent không làm gì thêm cho đến khi AN nói GO.

### SIP Content Discipline
SIP phải phân biệt rõ:
- Evidence: chỉ ghi điều đã thấy từ user, run log, hoặc file đã đọc.
- Unknowns: ghi rõ các điểm chưa xác minh, ví dụ `current_version: [READ_FROM_SKILL_MD]` nếu agent chưa đọc SKILL.md.
- Proposed Change: chỉ là đề xuất dạng diff; không được bịa current behavior hoặc khẳng định nguyên nhân kỹ thuật nếu chưa xác minh.

### Promotion Rule
AN approve + nói GO rõ ràng → agent apply patch theo surgical diff → move SIP sang `approved/`
AN reject → agent move SIP sang `rejected/` với lý do
AN defer → giữ SIP trong `pending/`, không sửa production skill

## Skill Priority Override
- Skill invocation follows `superpowers/using-superpowers`
- AGENTS.md rules ALWAYS override any skill instruction
- `brainstorming` skill: agents must not auto-invoke for Atom generation

## Skill-Creator Boundary

Use workspace `skill-creator` for vault-specific skill design, improvement, trigger tuning, regression testing, and policy alignment:

- `D:\NoteBookLLM_Br\.agent\skills\skill-creator`

Use Codex `.system/skill-creator` only for Codex-compatible packaging and scaffolding work, including `agents/openai.yaml`, `init_skill.py`, `quick_validate.py`, generated OpenAI metadata, or `.system` skill structure:

- `D:\anngu\.codex\skills\.system\skill-creator`

Rules:
- `.system/skill-creator` must never override vault-specific policy.
- workspace `skill-creator` must not modify Codex system scaffolding unless AN explicitly requests and approves that scope.

## Skill Overlap Dispatch Boundaries

These boundaries resolve known overlap between active skills without editing production `SKILL.md` descriptions.

### Web Capture
- Use `wiki-web-scrape` for static/public web pages where the needed output is text/Markdown staged to `00_Inbox/`.
- Use `wiki-crawl-4ai` for dynamic pages, visual proof, bot-bypass, screenshot evidence, or any R10 visual validation requirement.
- Neither skill may write directly to `3-resources/raw_*`; official ingest resumes through `ingest-lifecycle`.

### Preview vs Official Ingest
- Use `process-raw-resource` for source preview, triage, learning map, quick summary, or "should I ingest this?" requests. Output is non-canonical unless a workflow/user explicitly approves a preview artifact.
- Use `knowledge-intake` as the preview/official-ingest router when the request is ambiguous or spans preview lanes.
- `/ingest [file]` and official ingest requests bypass preview and must enter through `.agent/workflows/ingest-lifecycle.md`.
- `wiki-ingest` is a deterministic stage only; it is not the top-level `/ingest` entrypoint.

### Query Dispatch
- Use `wiki-query` for exact keywords, known entities/concepts, source tracing, graph traversal, and provenance questions.
- Use `wiki-semantic-search` when keyword search is empty/weak, the user asks conceptually, or the intent is abstract rather than exact-match.

### Learning UX Dispatch

- User wants to learn quickly from existing atoms -> `wiki-learning-pack`.
- User wants recall/transfer questions after studying -> `wiki-review-drill` if available; otherwise `wiki-learning-pack` may include basic Review Questions only.
- User asks which learned atoms are still unpracticed -> `wiki-learning-audit`.
- `wiki-learning-pack` must not run `wiki-learning-audit`; it may only recommend it as `Next Action`.
- `wiki-learning-audit` requires separate AN GO and must start with dry-run.
- User wants slides, lesson plans, rubrics, or activity sheets -> `@designer` / `pedagogy`.

### Frappe / ERPNext Skill Boundary

Frappe skills are inactive for the current vault unless the user explicitly requests Frappe, ERPNext, Bench, DocType, Server Script, Client Script, Web Form, or Frappe REST/API work.

Do not use Frappe skills for LLM Wiki ingest, K12 lesson/video generation, general skill governance, PDF conversion, or vault maintenance tasks.

### Planning And Execution
- Use `brainstorming` before creative feature/component/behavior design, except where AGENTS.md explicitly disables it such as Atom generation.
- Use `writing-plans` when a multi-step implementation already has a spec or concrete requirement.
- Use `executing-plans` when there is an approved written plan to execute.
- Use `subagent-driven-development` only when AN explicitly requests or approves multi-agent/subagent execution.

### Debug, Test, Review, Verification
- Use `systematic-debugging` when there is a bug, failed test, unexplained behavior, or root-cause question.
- Use `cm-tdd` when the task should be driven by tests or a red/green repair loop.
- Use `verification-before-completion` before claiming a fix/workflow is complete or passing.
- Use `cm-code-review` only for explicit review requests or when responding to review feedback.



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

### Tavily Cost-Control & Search Policy

Để kiểm soát chi phí API credits của Tavily (Basic Search = 1 credit, Advanced Search = 2 credits, Basic Extract = 1 credit / 5 URL, Advanced Extract = 2 credits / 5 URL), Agent PHẢI tuân thủ các quy tắc sau:

1. **Ưu tiên Tìm kiếm Nội bộ:** Chỉ sử dụng Tavily MCP khi tìm kiếm cục bộ (`wiki-query` hoặc `wiki-semantic-search`) không mang lại kết quả hoặc thông tin yêu cầu cần cập nhật thực tế từ Internet.
2. **Cấu hình Mặc định (Basic Mode):** Khi gọi `tavily-search`, BẮT BUỘC đặt mặc định `search_depth: "basic"`. Chỉ chuyển sang `advanced` khi có chỉ định rõ ràng của AN.
3. **Giới hạn Trích xuất (Extract Limitation):** Không tự ý chạy `tavily-extract` trên nhiều URL mà không có sự đồng ý của AN. Chỉ trích xuất từ các nguồn chất lượng cao, có độ tin cậy được xác định trước, và luôn giải thích lý do/chi phí dự kiến cho AN trước khi gọi.
4. **Tránh Gọi Lặp:** Tận dụng tối đa kết quả tìm kiếm đã có trong phiên làm việc hiện tại, tránh gọi lại các câu truy vấn tương tự hoặc chồng chéo.

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
| Dev/script work | `filesystem + sqlite + Git CLI (Direct)` | Maps to script mode `dev`. Sử dụng lệnh Git CLI trực tiếp thay cho github-mcp-server để tiết kiệm 12.5K tokens. |
| Ingest profile | `filesystem + sqlite + notebooklm-mcp-server` | Maps to script mode `ingest` for the currently configured MCP inventory. |
| Web ingest | `filesystem + browser/search/scrape` | Policy target when those MCPs exist in the full inventory. |

### Mode Notes

- `MICRO 3B`: do not enable extra MCPs unless the task explicitly requires them.
- `Normal vault work`: prefer `filesystem + sqlite` before enabling any broader tool surface.
- `Automation`: must remain read-only unless AN explicitly approves a write-capable action.
- `Dev/script work`: Ưu tiên sử dụng lệnh Git CLI trực tiếp qua run_command, loại bỏ hoàn toàn github-mcp-server để tối ưu hóa context.
- `Ingest profile`: current script implementation uses `filesystem + sqlite + notebooklm-mcp-server` because those servers exist in the current full backup.
- `Ingest profile`: dùng `notebooklm-mcp-server` trước hết như lớp reconnaissance nhanh cho source dài hoặc source đã có trong NotebookLM; không coi output MCP là canonical ingest artifact.
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

### Source-Scoped Staging and Run Packages

- Không để phẳng `SOURCE_PREP_REPORT_*`, `SOURCE_AUDIT_REPORT_*`, `INGEST_INPUT_LOCK_*` trực tiếp trong `00_Inbox/` khi source có scope rõ ràng.
- Với `fresh/simple source`, ưu tiên dùng `00_Inbox/sources/[source_id]/` cho source staging và lifecycle control artifacts.
- Với `complex/AI-first/rerun/resumable source`, ưu tiên dùng `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/` làm run package.
- Không tạo folder con theo source bên trong `3-resources/raw_sources/`, `3-resources/raw_ingest/`, hoặc `3-resources/raw_assets/`; các vùng raw giữ `flattened storage`.
- `1-projects/sources/[source_id]/` là default cho source-scoped control/analysis artifacts như `SOURCE_PREP_REPORT_*`, `SOURCE_AUDIT_REPORT_*`, `INGEST_INPUT_LOCK_*`, `STRUCTURE_[ID]`, `FIGURES_[ID]`, `NAMING_LOCK_[ID]`, `MAP_[ID]`, `Analysis_*`, và `INGEST_ORCHESTRATION_REPORT_*`.
- Không để phẳng các artifact trên trực tiếp trong `1-projects/` khi source có scope rõ ràng.
- `1-projects/` root chỉ giữ project-level notes hoặc lightweight recon artifacts khi workflow đã chốt path root.

### Video and Audio Guidance

- For large videos, prefer `URL + transcript + metadata + selected screenshots` over storing the full source file locally.
- Download the full video only when the source is critical, likely to disappear, or required for offline processing or evidence preservation.
- Treat transcript/subtitle output as the primary ingest artifact whenever it is reliable enough for the task.

### Operational Rule

- Live web/video sources are acquisition points, not the default ingest-ready artifacts.
- The preferred ingest starting point is a staged local artifact in `00_Inbox/sources/[source_id]/` for simple runs, or a run package under `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/` for complex runs.
- If a source remains live-only, the agent must explain the risk: mutability, link rot, replay difficulty, and weaker auditability.

## Knowledge Intake Policy

There are two entry lanes:
- Preview lane: `knowledge-intake` routes natural-language preview requests to preview modes. `NON_CANONICAL`.
- Official ingest lane: `/ingest` and official ingest requests go to `ingest-lifecycle`. `CANONICAL`.

NotebookLM query là lớp reconnaissance phụ trợ, không phải entry lane thứ ba.
Nó chỉ dùng để trinh sát nhanh trước `knowledge-intake` hoặc trước khi đọc sâu source dài.

Rules:
- `/ingest [file]` bypasses `knowledge-intake`.
- Preview runtime defaults to `CHAT_ONLY`.
- Preview artifact writes are allowed only when requested by workflow/user text.
- During an approved implementation goal, Codex must not stop for additional GO confirmations inside the declared scope.
- Preview artifacts cannot satisfy official ingest gates.
- Official ingest must ignore `00_Inbox/preview/`.
- Lifecycle control artifacts may live in `00_Inbox/sources/[source_id]/` or `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/`.
- Lifecycle control artifacts do not satisfy official gates by location alone; the current lifecycle/run must explicitly resolve them as the active artifacts for that source/run.

### NotebookLM Recon Policy

Use `notebooklm-mcp-server` as a reconnaissance layer when helpful:
- tìm nhanh ý chính
- tìm chương/đoạn đáng chú ý
- tìm atom candidates sơ bộ
- tìm câu hỏi còn mơ hồ, contradiction, gap

Hard boundaries:
- output từ NotebookLM là `UNVERIFIED`
- không dùng output NotebookLM làm `source_evidence_file`
- không dùng output NotebookLM làm `primary_ingest_file`
- không dùng output NotebookLM để tạo Atom trực tiếp
- không coi NotebookLM answer là source of truth

Required follow-up:
- NotebookLM recon phải đi qua `knowledge-intake` ở mode `CHAT_ONLY` hoặc preview mode phù hợp để lọc nhiễu, chuẩn hóa claim, và loại bỏ ý không trace được về nguồn
- chỉ sau đó mới được handoff sang canonical core nếu source và gates đã rõ

Recommended sequence:

```text
NotebookLM query
-> knowledge-intake (chat_only)
-> prepare-source
-> audit-promote-source
-> lock-ingest-input
-> ingest
```

Optional analysis artifact:
- `NOTEBOOKLM_RECON_[SOURCE_ID].md`
- default path:
  - `1-projects/NOTEBOOKLM_RECON_[SOURCE_ID].md`
- `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/NOTEBOOKLM_RECON_[SOURCE_ID].md` chỉ dùng như ngoại lệ debug/runtime khi được yêu cầu rõ
- artifact này là analysis phụ trợ, không phải canonical ingest fuel

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
├── GEMINI.md                ← Governance reference/archive, không phải runtime source of truth
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
> Diễn giải lịch sử 27 rules: [[GEMINI.md]] — reference/archive, không override runtime.

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
| R22 Staging-Promote | `scripts/maintenance/circuit_breaker.py` chặn write trực tiếp vào `3-resources/` |
| R23 Promotion Gate | `promote.py` là wrapper duy nhất được phép move file |
| R20 YAML Validity | `ingest.py` schema validation — tự reject nếu YAML invalid |
| R14 Log Rotation | `session_seal.py` tự tạo file log đúng tên |

### Tầng 4 — Reference (Tra cứu khi cần, không inject mặc định)
[[GEMINI.md]] — Governance reference/archive cho 27 rules và WikiCouncil 2.0; không phải startup bắt buộc.

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
