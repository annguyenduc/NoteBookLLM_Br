# SKILL_IMPROVEMENT_PROPOSAL

```yaml
proposal_id: SIP_20260520_002
skill_id: prompt-master
current_version: 1.7.0
proposed_version: 1.7.1
source_run_id: manual
trigger: missing_step
severity: medium
approval_required: true
```

## Evidence

- User asked whether `.agent/skills/prompt-master/SKILL.md` needs improvement to fit `D:\NoteBookLLM_Br`.
- Read-only audit found the skill already has a `NoteBookLLM_Br Core Agents Routing` section, but the workspace overlay is incomplete.
- Current Antigravity guidance says to anchor prompts with `user_global`, `AGENTS.md`, and `GEMINI.md`. In this workspace, `AGENTS.md` is the runtime source of truth; `GEMINI.md` is only governance reference/archive and must not override runtime.
- Current skill mentions approval generally, but does not encode the workspace action safety classes: `Read-only`, `File artifact write`, `State-changing`, and `Governance-changing`.
- Current skill does not encode official ingest vs preview lane boundaries: `/ingest [file]` must enter `ingest-lifecycle`; `knowledge-intake` remains routing/preview; NotebookLM is `UNVERIFIED` reconnaissance only.
- Current skill does not include vault path topology for prompt generation: source-scoped control artifacts under `1-projects/sources/[source_id]/`, simple staging under `00_Inbox/sources/[source_id]/`, complex runs under `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/`, and flattened raw storage under `3-resources/raw_*`.
- Current skill does not encode the workspace SIP boundary for skill-improvement prompts.

## Unknowns

- No eval run has been executed yet for prompt quality before/after this SIP.
- This SIP proposes a surgical overlay update only; it does not attempt to refresh all external tool guidance such as model version details.
- Exact final wording should be reviewed by AN before patching production `SKILL.md`.

## Problem

`prompt-master` is optimized for general prompt engineering, but for `D:\NoteBookLLM_Br` it can still generate prompts that accidentally weaken local governance:

- treating `GEMINI.md` as active runtime context instead of reference/archive
- asking agents to perform write or state-changing work without explicit AN approval gates
- mixing preview, NotebookLM reconnaissance, and official ingest lanes
- omitting path topology that prevents flat artifact sprawl
- producing skill-edit prompts that skip SIP review and patch production skills directly

The issue is not the general prompting framework. The missing piece is a compact `NoteBookLLM_Br Workspace Overlay` that every Codex/Antigravity/agentic prompt uses when the target task touches this vault.

## Proposed Change (diff format)

```diff
--- a/.agent/skills/prompt-master/SKILL.md
+++ b/.agent/skills/prompt-master/SKILL.md
@@
 **Antigravity (Google's agent-first IDE, powered by Gemini 2.0 / 3 Pro)**
 ...
-- User rule grounding: Anchor prompts with direct references to local governance files (`user_global`, `AGENTS.md`, `GEMINI.md`).
+- User rule grounding for `D:\NoteBookLLM_Br`: anchor prompts to `AGENTS.md` as runtime source of truth and `.agent/rules/CORE.md` as the mandatory kernel. Treat `GEMINI.md` as governance reference/archive only; do not inject it by default and never let it override runtime instructions.
+
+---
+
+**NoteBookLLM_Br Workspace Overlay**
+Apply this overlay whenever the generated prompt targets Codex, Antigravity, Claude Code, Cline, Cursor, or any agent working inside `D:\NoteBookLLM_Br`.
+
+Runtime precedence:
+- Current user instruction in the session
+- `AGENTS.md`
+- `.agent/rules/CORE.md`
+- active agent rule or directly invoked workflow
+- task-specific skill
+- `GEMINI.md` only as reference/archive when explicitly needed
+
+Action safety:
+- Read-only inspection, dry-run, and chat reports may proceed without AN GO.
+- File artifact writes, production skill edits, promote operations, raw/wiki writes, metadata updates, MCP switching, git commit/push, and synthesis writes require explicit AN approval.
+- Any prompt that asks for write-capable work must state the approved scope, forbidden paths, and stop conditions.
+- Never write directly into `3-resources/raw_sources/`, `3-resources/raw_ingest/`, or `3-resources/raw_assets/`; use the approved promote flow.
+- Never ask an agent to set `SYNTHESIZED`; only AN may do that.
+
+Ingest and preview routing:
+- `/ingest [file]` and official ingest requests must enter `.agent/workflows/ingest-lifecycle.md`.
+- `knowledge-intake` is a routing/preview layer, not the ingest engine.
+- `process-raw-resource` is preview-only and non-canonical unless AN explicitly requests an artifact.
+- NotebookLM output is `UNVERIFIED` reconnaissance only; it cannot be `source_evidence_file`, `primary_ingest_file`, or direct Atom fuel.
+
+Path topology:
+- Simple source staging: `00_Inbox/sources/[source_id]/`
+- Complex, AI-first, rerun, or resumable work: `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/`
+- Source-scoped analysis/control artifacts: `1-projects/sources/[source_id]/`
+- Raw storage under `3-resources/raw_*` remains flattened; do not create source subfolders there.
+
+Language and encoding:
+- For operator-facing or wiki-facing artifacts in this vault, write Vietnamese body text with diacritics by default.
+- Keep metadata keys, enum values, filenames, `source_id`, and exact titles canonical.
+- Require UTF-8 validation when writing Vietnamese files.
+
+Skill-improvement prompts:
+- Do not patch production `SKILL.md` directly unless AN has approved a SIP and said GO for that SIP.
+- If a skill gap is found, create a SIP under `.agent/skill_reviews/pending/` with evidence, unknowns, proposed diff, regression case, and risk.
+- After creating SIP, stop and ask AN to review.
@@
 **NoteBookLLM_Br Core Agents Routing**
 If the target tool or persona is a specialized agent in the NoteBookLLM_Br workspace, apply these strict routing directives to align with role boundaries:
@@
-- `@scout`: Request raw knowledge extraction and candidates mapping in `00_Inbox/`. Add constraint: "Do not promote to raw_*/ or touch core resources. Run gap_check.py manually."
+- `@scout`: Request source preview, raw knowledge extraction, analysis maps, and Atom candidates only. Add constraint: "Do not materialize official Atom files, promote to raw_*/, or treat NotebookLM output as canonical source evidence."
@@
-- `@engineer`: Request minimal, high-efficiency code implementations (Surgical Changes, Karpathy style). Add constraint: "Write minimum code, no over-engineering. Done when localsandbox WASM tests pass."
+- `@engineer`: Request minimal, high-efficiency code implementations or approved Atom materialization from a clear spec. Add constraint: "Write minimum code, no over-engineering. Respect approved scope, raw storage boundaries, and verification gates."
```

## Regression Case

- Input: "Viết prompt cho Antigravity để sửa workflow ingest trong `D:\NoteBookLLM_Br`."
- Expected: Generated prompt names `AGENTS.md` as runtime source of truth, includes action safety classes, requires AN GO for writes, forbids direct raw writes, and routes official ingest through `ingest-lifecycle`.

- Input: "Viết prompt cho Codex nâng cấp skill `wiki-learning-pack`."
- Expected: Generated prompt tells the agent to audit first, create a SIP in `.agent/skill_reviews/pending/` if a gap is found, and not patch production `SKILL.md` until AN approves the SIP and says GO.

- Input: "Viết prompt để dùng NotebookLM tạo atoms từ tài liệu."
- Expected: Generated prompt refuses direct Atom creation from NotebookLM output, labels NotebookLM as `UNVERIFIED` reconnaissance, and routes follow-up through `knowledge-intake` or official ingest gates.

## Risk

medium - The patch changes default prompt behavior for this workspace. Risk is controlled by keeping the change as a small overlay rather than rewriting the whole skill.

## Validation Plan

- Re-read `SKILL.md` after patch to confirm no duplicated frontmatter or broken section order.
- Run structural validator if available.
- Run UTF-8 readback check because the file contains Vietnamese.
- Manually test at least the three regression inputs above in chat or eval form.

## AN Decision

- [x] Approve + GO -> agent apply patch theo surgical diff
- [ ] Reject -> lý do: ___
- [ ] Defer -> review lại sau: ___
