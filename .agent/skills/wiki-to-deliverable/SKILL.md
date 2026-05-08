---
name: wiki-to-deliverable
description: Use when synthesizing multiple Knowledge Atoms from the vault into a structured Markdown summary or Obsidian note. Triggers on 'tổng hợp từ vault', 'compile atoms', 'make summary from wiki', 'draft from vault', or when a topic requires pulling connected Atoms into a single readable output. Do NOT use for single-Atom lookup (use wiki-query instead) or for generating curriculum deliverables for external audiences (KDI scope excluded).
---

# Wiki to Deliverable

## Overview
Pull connected Atoms from the vault and compile them into a structured Markdown document. The output is for personal learning synthesis — a readable summary that links back to source Atoms via wikilinks, not a polished external deliverable.

Primary use case: "I've been ingesting on topic X for weeks. Give me a summary I can actually read and think with."

## Guardrails
- Never invent connections between Atoms that don't exist in the DB graph.
- Always include `[[wikilink]]` references to source Atoms — do not produce orphan summaries.
- Do not set any Atom's status to `SYNTHESIZED`; the output document is a new note, not a promotion.
- Keep output within the vault's PARA structure: new notes go to `1-projects/` or `3-resources/` depending on scope.
- Mark the output note with `generated_by: wiki-to-deliverable` in frontmatter so it's distinguishable from human-written notes.
- **Template**: Bản tổng hợp phải tuân thủ cấu trúc tại `.agent/skills/references/SYNTHESIS_TEMPLATE.md`.

- If fewer than 3 Atoms are found for the topic, warn the user and suggest running wiki-query or wiki-semantic-search first to locate more material.

## Workflow
1. **Clarify topic scope.**
   Ask (or infer from context): what topic, what angle, what depth?
   Example: "agent workflows" → narrow to Atoms tagged `multi-agent` and `antigravity`.

2. **Query the vault for relevant Atoms.**
   `python .agent/skills/wiki-query/scripts/wiki_query_helper.py --query "<topic>" --limit 10`
   If results are weak: escalate to `wiki-semantic-search`.

3. **Inspect graph edges** for connections between returned Atoms.
   Look for `SUPPORTS`, `EXTENDS`, `CONTRADICTS` edges — these become the structure of the summary.

4. **Draft the Markdown summary.**
   Structure:
   ```
   ---
   title: <Topic> — Synthesis
   created: <date>
   generated_by: wiki-to-deliverable
   source_atoms: [atom_id_1, atom_id_2, ...]
   status: DRAFT
   ---

   ## Core Idea
   <1–2 sentence synthesis of the central concept>

   ## Key Points
   <Drawn from SUPPORTS/EXTENDS edges — each point links to its source Atom>

   ## Open Questions / Tensions
   <Drawn from CONTRADICTS edges or low-confidence Atoms>

   ## Next Actions
   <What to read, practice, or verify to upgrade this from DRAFT to SYNTHESIZED>
   ```

5. **Save to vault.**
   - Topic is active project: save to `1-projects/<topic>/`
   - Topic is reference material: save to `3-resources/wiki/synthesis/`

6. **Report** file path and Atom count used.

## Quick Reference
- Query starting point:
  `python .agent/skills/wiki-query/scripts/wiki_query_helper.py --query "<topic>" --limit 10`
- Semantic fallback:
  use `wiki-semantic-search` skill
- Output location default:
  `3-resources/wiki/synthesis/<topic>-synthesis-<YYYYMMDD>.md`

## Common Mistakes
- Writing a summary from memory instead of from actual Atom content — every claim must trace to a queried Atom.
- Producing output without wikilinks — an orphan summary adds no value to the graph.
- Skipping the "Open Questions" section — this is where learning actually happens.
- Saving to the wrong PARA bucket (e.g., putting reference synthesis in `1-projects/`).
- Treating the output as publishable — it's a personal thinking tool, not a finished document.

## Technical Keywords (Audit)
- **SUPPORTS / EXTENDS / CONTRADICTS**: Edge types that drive summary structure.
- **wikilink**: `[[Atom Title]]` format required in all output.
- **PARA**: Projects / Areas / Resources / Archive — vault folder structure.
- **generated_by**: frontmatter tag to distinguish AI-compiled notes from human notes.
- **status: DRAFT**: all output from this skill starts as DRAFT.

## Technical Reference
- Edge types: SUPPORTS (reinforcing), EXTENDS (building on), CONTRADICTS (tension/conflict).
- PARA structure: 1-projects/ (active), 2-areas/ (ongoing), 3-resources/ (reference), 4-archive/.
- synthesis/ subfolder: tập trung các bản tổng hợp multi-Atom để dễ review.
- generated_by field: phân biệt note do agent tạo vs. human viết khi audit vault.
