# Tool Routing Reference

Read **only the section matching your target tool**. Do not load this entire file if you only need one section.

---

## LLM / Chat AI

### Claude (claude.ai, Claude API, Claude 4.x)
- Be explicit and specific — Claude 4.x follows instructions literally. Opus 4.7 especially: it does exactly what you say, nothing more. Missing context = narrow literal output, not a smart guess.
- XML tags help for complex multi-section prompts: `<context>`, `<task>`, `<constraints>`, `<output_format>`
- Claude Opus 4.x over-engineers by default — add "Only make changes directly requested. Do not add features or refactor beyond what was asked."
- Provide context and reasoning WHY, not just WHAT — Claude generalizes better from explanations
- Always specify output format and length explicitly
- For complex or multi-step tasks on Opus 4.7: front-load everything in one turn — intent, constraints, acceptance criteria, relevant files. Every extra back-and-forth turn adds reasoning overhead and token cost.
- Do NOT add "think step by step" or fixed thinking budget instructions — Opus 4.7 uses adaptive thinking and calibrates depth automatically. To influence depth: "Think carefully before responding" (more) or "Prioritize responding quickly" (less).
- Use Template M for agentic or multi-step tasks on Opus 4.7.

---

### ChatGPT / GPT-5.x / OpenAI GPT models
- Start with the smallest prompt that achieves the goal — add structure only when needed
- Be explicit about the output contract: what format, what length, what "done" looks like
- State tool-use expectations explicitly if the model has access to tools
- Use compact structured outputs — GPT-5.x handles dense instruction well
- Constrain verbosity when needed: "Respond in under 150 words. No preamble. No caveats."
- GPT-5.x is strong at long-context synthesis and tone adherence — leverage these

---

### o3 / o4-mini / OpenAI reasoning models
- SHORT clean instructions ONLY — these models reason across thousands of internal tokens
- NEVER add CoT, "think step by step", or reasoning scaffolding — it actively degrades output
- Prefer zero-shot first — add few-shot only if strictly needed and tightly aligned
- State what you want and what done looks like. Nothing more.
- Keep system prompts under 200 words — longer prompts hurt performance on reasoning models

---

### Gemini 2.x / Gemini 3 Pro
- Strong at long-context and multimodal — leverage its large context window for document-heavy prompts
- Prone to hallucinated citations — always add "Cite only sources you are certain of. If uncertain, say [uncertain]."
- Can drift from strict output formats — use explicit format locks with a labelled example
- For grounded tasks add "Base your response only on the provided context. Do not extrapolate."

---

### Qwen 2.5 (instruct variants)
- Excellent instruction following, JSON output, structured data — leverage these strengths
- Provide a clear system prompt defining the role — Qwen2.5 responds well to role context
- Works well with explicit output format specs including JSON schemas
- Shorter focused prompts outperform long complex ones — scope tightly

---

### Qwen3 (thinking mode)
- Two modes: thinking mode (/think or enable_thinking=True) and non-thinking mode
- Thinking mode: treat exactly like o3 — short clean instructions, no CoT, no scaffolding
- Non-thinking mode: treat like Qwen2.5 instruct — full structure, explicit format, role assignment

---

### Ollama (local model deployment)
- ALWAYS ask which model is running before writing — Llama3, Mistral, Qwen2.5, CodeLlama all behave differently
- System prompt is the most impactful lever — include it in the output so user can set it in their Modelfile
- Shorter simpler prompts outperform complex ones — local models lose coherence with deep nesting
- Temperature 0.1 for coding/deterministic tasks, 0.7-0.8 for creative tasks
- For coding: CodeLlama or Qwen2.5-Coder, not general Llama

---

### Llama / Mistral / open-weight LLMs
- Shorter prompts work better — these models lose coherence with deeply nested instructions
- Simple flat structure — avoid heavy nesting or multi-level hierarchies
- Be more explicit than you would with Claude or GPT — instruction following is weaker
- Always include a role in the system prompt

---

### DeepSeek-R1
- Reasoning-native like o3 — do NOT add CoT instructions
- Short clean instructions only — state the goal and desired output format
- Outputs reasoning in `<think>` tags by default — add "Output only the final answer, no reasoning." if needed

---

### MiniMax (M2.7 / M2.5)
- OpenAI-compatible API — prompts that work with GPT models transfer directly
- Strong at instruction following, structured output, and long-context synthesis — 1M context window on M2.7
- M2.5-highspeed has a 204K context window and is optimized for speed — use for latency-sensitive tasks
- Temperature must be between 0 and 1 (inclusive) — prompts that set temperature above 1 will fail
- May output reasoning in `<think>` tags — add "Output only the final answer, no reasoning tags." if the user does not want visible thinking
- Good at code generation, JSON output, and multi-step analysis — leverage these strengths
- Responds well to explicit role assignment and structured prompts with clear output format specifications
- For function calling: supports OpenAI-style tool definitions — include tool schemas directly

---

## Agentic Code AI

### Claude Code
- Agentic — runs tools, edits files, executes commands autonomously
- Starting state + target state + allowed actions + forbidden actions + stop conditions + checkpoints
- Stop conditions are MANDATORY — runaway loops are the biggest credit killer
- Opus 4.7 default in Claude Code is xhigh effort — do NOT specify effort level in prompts, it's already set
- Opus 4.7 is more literal than 4.6 — vague first turns produce narrower results. Front-load everything: intent, file scope, constraints, acceptance criteria, session strategy.
- Opus 4.7 uses fewer tool calls by default and reasons more between calls — explicitly instruct tool use when needed: "Read all files in /src/auth/ before starting"
- Opus 4.7 spawns fewer subagents by default — explicitly request when needed: "Use a subagent to investigate X so it stays out of main context"
- Claude Opus 4.x over-engineers — add "Only make changes directly requested. Do not add extra files, abstractions, or features."
- Always scope to specific files and directories — never give a global instruction without a path anchor
- Human review triggers required: "Stop and ask before deleting any file, adding any dependency, or affecting the database schema"
- Session hygiene matters: new task = new session. Use /rewind instead of correcting mid-conversation. /compact at ~50% context, not 90%.
- For complex tasks: use Template M. It handles scope, criteria, stop conditions, and session strategy in one structured block.

---

### Antigravity (Google's agent-first IDE, powered by Gemini 2.0 / 3 Pro)
- Outcome-driven artifacts: Always request structured deliverables as Artifacts (e.g., `implementation_plan.md`, `task.md`, `walkthrough.md`) before any execution begins.
- Strict multi-step orchestration: Specify exactly the sequential steps with clear checkpoint gates ("Done when: ...").
- Browser validation: Leverage built-in browser automation for pixel-perfect layout checks at multiple resolutions (e.g. 375px, 1440px).
- Autonomy constraints: Always declare the authorization level. Explicitly instruct the agent to pause and ask for confirmation before executing any state-changing command or file modification.
- Single-task scoping: Scope every prompt to a single, isolated feature or component to prevent context swelling and attention drift.
- User rule grounding for `D:\NoteBookLLM_Br`: anchor prompts to `AGENTS.md` as runtime source of truth and `.agent/rules/CORE.md` as the mandatory kernel. Treat `GEMINI.md` as governance reference/archive only; do not inject it by default and never let it override runtime instructions.

---

### NoteBookLLM_Br Workspace Overlay
Apply this overlay whenever the generated prompt targets Codex, Antigravity, Claude Code, Cline, Cursor, or any agent working inside `D:\NoteBookLLM_Br`.

Runtime precedence:
- Current user instruction in the session
- `AGENTS.md`
- `.agent/rules/CORE.md`
- active agent rule or directly invoked workflow
- task-specific skill
- `GEMINI.md` only as reference/archive when explicitly needed

Action safety:
- Read-only inspection, dry-run, and chat reports may proceed without AN GO.
- File artifact writes, production skill edits, promote operations, raw/wiki writes, metadata updates, MCP switching, git commit/push, and synthesis writes require explicit AN approval.
- Any prompt that asks for write-capable work must state the approved scope, forbidden paths, and stop conditions.
- Never write directly into `3-resources/raw_sources/`, `3-resources/raw_ingest/`, or `3-resources/raw_assets/`; use the approved promote flow.
- Never ask an agent to set `SYNTHESIZED`; only AN may do that.

Ingest and preview routing:
- `/ingest [file]` and official ingest requests must enter `.agent/workflows/ingest-lifecycle.md`.
- `knowledge-intake` is a routing/preview layer, not the ingest engine.
- `process-raw-resource` is preview-only and non-canonical unless AN explicitly requests an artifact.
- NotebookLM output is `UNVERIFIED` reconnaissance only; it cannot be `source_evidence_file`, `primary_ingest_file`, or direct Atom fuel.

Path topology:
- Simple source staging: `00_Inbox/sources/[source_id]/`
- Complex, AI-first, rerun, or resumable work: `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/`
- Source-scoped analysis/control artifacts: `1-projects/sources/[source_id]/`
- Raw storage under `3-resources/raw_*` remains flattened; do not create source subfolders there.

Language and encoding:
- For operator-facing or wiki-facing artifacts in this vault, write Vietnamese body text with diacritics by default.
- Keep metadata keys, enum values, filenames, `source_id`, and exact titles canonical.
- Require UTF-8 validation when writing Vietnamese files.

Skill-improvement prompts:
- Do not patch production `SKILL.md` directly unless AN has approved a SIP and said GO for that SIP.
- If a skill gap is found, create a SIP under `.agent/skill_reviews/pending/` with evidence, unknowns, proposed diff, regression case, and risk.
- After creating SIP, stop and ask AN to review.

**NoteBookLLM_Br Core Agents Routing**
If the target tool or persona is a specialized agent in the NoteBookLLM_Br workspace, apply these strict routing directives to align with role boundaries:
- `@pm`: Request blueprints, specifications, and roadmap planning. Add constraint: "Strictly read-only; no code modifications or file changes. Must seek User approval (R5)."
- `@scout`: Request source preview, raw knowledge extraction, analysis maps, and Atom candidates only. Add constraint: "Do not materialize official Atom files, promote to raw_*/, or treat NotebookLM output as canonical source evidence."
- `@engineer`: Request minimal, high-efficiency code implementations or approved Atom materialization from a clear spec. Add constraint: "Write minimum code, no over-engineering. Respect approved scope, raw storage boundaries, and verification gates."
- `@librarian`: Request index generation, backlinks management, and reconciliation drafts. Add constraint: "Must never set status to SYNTHESIZED (R8 - Human Supremacy)."
- `@auditor`: Request source tracing, metadata validation, and quality auditing. Add constraint: "Fail-hard on any invalid metadata (R20, R21)."
- `@designer`: Request pedagogy sequencing, slide decks, and lesson plans. Add constraint: "Verify Trainer Profile is active before generation."
- `@healer`: Request system rollback, DLQ recovery, and fixing broken links. Add constraint: "Restrict actions to 00_Inbox/, failed_queue/, and wiki/ links only."

---

### Cursor / Windsurf
- File path + function name + current behavior + desired change + do-not-touch list + language and version
- Never give a global instruction without a file anchor
- "Done when:" is required — defines when the agent stops editing
- For complex tasks: split into sequential prompts rather than one large prompt

---

### Cline (formerly Claude Dev)
- Agentic VS Code extension — autonomously edits files, runs terminal commands, uses browser tools
- Powered by Claude, GPT, or other LLMs — prompting style should match the underlying model
- Starting state + target state + file scope + stop conditions + approval gates
- Always specify which files to edit and which to leave untouched
- Add "Ask before running terminal commands" or "Ask before installing dependencies" to prevent unwanted actions
- Can read file contents, search codebases, and use browser automation — leverage these for context gathering
- For multi-step tasks: break into sequential prompts with clear checkpoints
- Cline shows a task list before executing — review it and adjust scope if needed

---

### GitHub Copilot
- Write the exact function signature, docstring, or comment immediately before invoking
- Describe input types, return type, edge cases, and what the function must NOT do
- Copilot completes what it predicts, not what you intend — leave no ambiguity in the comment

---

### Bolt / v0 / Lovable / Figma Make / Google Stitch
- Full-stack generators default to bloated boilerplate — scope it down explicitly
- Always specify: stack, version, what NOT to scaffold, clear component boundaries
- Lovable responds well to design-forward descriptions — include visual/UX intent
- v0 is Vercel-native — specify if you need non-Next.js output
- Bolt handles full-stack — be explicit about which parts are frontend vs backend vs database
- Figma Make is design-to-code native — reference your Figma component names directly
- Google Stitch is prompt-to-UI focused — describe the interface goal not the implementation. Add "match Material Design 3 guidelines" for Google-native styling
- Add "Do not add authentication, dark mode, or features not explicitly listed" to prevent feature bloat

---

### Devin / SWE-agent
- Fully autonomous — can browse web, run terminal, write and test code
- Very explicit starting state + target state required
- Forbidden actions list is critical — Devin will make decisions you did not intend without explicit constraints
- Scope the filesystem: "Only work within /src. Do not touch infrastructure, config, or CI files."

---

## Research / Orchestration AI

### Research / Orchestration AI (Perplexity, Manus AI)
- Perplexity search mode: specify search vs analyze vs compare. Add citation requirements. Reframe hallucination-prone questions as grounded queries.
- Manus and Perplexity Computer are multi-agent orchestrators — describe the end deliverable, not the steps. They decompose internally.
- For Perplexity Computer: specify the output artifact type (report / spreadsheet / code / summary). Add "Flag any data point you are not confident about."
- For long multi-step tasks: add verification checkpoints since each chained step compounds hallucination risk

---

### Computer-Use / Browser Agents (Perplexity Comet/Computer, OpenAI Atlas, Claude in Chrome, OpenClaw Agents)
- These agents control a real browser — they click, scroll, fill forms, and complete transactions autonomously
- Describe the outcome, not the navigation steps: "Find the cheapest flight from X to Y on Emirates or KLM, no Boeing 737 Max, one stop maximum"
- Specify constraints explicitly — the agent will make its own decisions without them
- Add permission boundaries: "Do not make any purchase. Research only."
- Add a stop condition for irreversible actions: "Ask me before submitting any form, completing any transaction, or sending any message"
- Comet works best with web research, comparison, and data extraction tasks
- Atlas is stronger for multi-step commerce and account management tasks

---

## Creative / Visual AI

### Image AI — Generation (Midjourney, DALL-E 3, Stable Diffusion, SeeDream)
First detect: generation from scratch or editing an existing image?

- **Midjourney**: Comma-separated descriptors, not prose. Subject first, then style, mood, lighting, composition. Parameters at end: `--ar 16:9 --v 6 --style raw`. Negative prompts via `--no [unwanted elements]`
- **DALL-E 3**: Prose description works. Add "do not include text in the image unless specified." Describe foreground, midground, background separately for complex compositions.
- **Stable Diffusion**: `(word:weight)` syntax. CFG 7-12. Negative prompt is MANDATORY. Steps 20-30 for drafts, 40-50 for finals.
- **SeeDream**: Strong at artistic and stylized generation. Specify art style explicitly (anime, cinematic, painterly) before scene content. Mood and atmosphere descriptors work well. Negative prompt recommended.

---

### Image AI — Reference Editing (when user has an existing image to modify)
Detect when: user mentions "change", "edit", "modify", "adjust" anything in an existing image, or uploads a reference.
Always instruct the user to attach the reference image to the tool first. Build the prompt around the delta ONLY — what changes, what stays the same.
Read references/templates.md Template J for the full reference editing template.

---

### ComfyUI
Node-based workflow — not a single prompt box. Ask which checkpoint model is loaded before writing.
Always output two separate blocks: Positive Prompt and Negative Prompt. Never merge them.
Read references/templates.md Template K for the full ComfyUI template.

---

### 3D AI — Text to 3D/Game Systems (Meshy, Tripo, Rodin)
- Describe: style keyword (low-poly / realistic / stylized cartoon) + subject + key features + primary material + texture detail + technical spec
- Negative prompt supported — use it: "no background, no base, no floating parts"
- Meshy: best for game assets and teams. Game asset prompts work best here.
- Tripo: fastest for clean topology. Rapid prototyping and concept assets.
- Rodin: highest quality for photorealistic prompts. Slower and more expensive.
- Specify intended export use: game engine (GLB/FBX), 3D printing (STL), web (GLB)
- For characters: specify A-pose or T-pose if the model will be rigged

---

### 3D AI — In-Engine AI (Unity AI, Blender AI tools)
- Unity AI (Unity 6.2+, replaces retired Muse): use /ask for documentation and project queries, /run for automating repetitive Editor tasks, /code for generating or reviewing C# code. Be precise — state exactly what needs to happen in the Editor.
- Unity AI Generators: text-to-sprite, text-to-texture, text-to-animation. Describe the asset type, art style, and technical constraints (resolution, color palette, animation loop or one-shot).
- BlenderGPT / Blender AI add-ons: these generate Python scripts that execute in Blender. Be specific about geometry, material names, and scene context. Include "apply to selected object" or "apply to entire scene" to avoid ambiguity.

---

### Video AI (Sora, Runway, Kling, LTX Video, Dream Machine)
- Sora: describe as if directing a film shot. Camera movement is critical — static vs dolly vs crane changes output dramatically.
- Runway Gen-3: responds to cinematic language — reference film styles for consistent aesthetic.
- Kling: strong at realistic human motion — describe body movement explicitly, specify camera angle and shot type.
- LTX Video: fast generation, prompt-sensitive — keep descriptions concise and visual. Specify resolution and motion intensity explicitly.
- Dream Machine (Luma): cinematic quality — reference lighting setups, lens types, and color grading styles.

---

### Voice AI (ElevenLabs)
- Specify emotion, pacing, emphasis markers, and speech rate directly
- Use SSML-like markers for emphasis: indicate which words to stress, where to pause
- Prose descriptions do not translate — specify parameters directly

---

## Workflow / Automation AI

### Workflow AI (Zapier, Make, n8n)
- Trigger app + trigger event → action app + action + field mapping. Step by step.
- Auth requirements noted explicitly — "assumes [app] is already connected"
- For multi-step workflows: number each step and specify what data passes between steps
