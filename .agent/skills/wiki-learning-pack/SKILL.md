---
name: wiki-learning-pack
description: Use when the user wants to learn quickly from existing Wiki atoms, create a fast-start learning pack from a topic or source_id, turn indexed atoms into a 60-90 minute self-study path, or build a structured review path before drills or pedagogy. Do NOT use for ingest, atom creation, final synthesis, PDF conversion, slide decks, lesson plans, or vault maintenance.
---

# wiki-learning-pack

## Purpose

Create a Learning Pack from existing indexed Wiki atoms so the user can learn a topic in 60-90 minutes without rereading the full source.

This skill is a Learning UX layer over existing atoms. It is read-heavy and write-light: read enough atom/source context to organize learning, then produce one chat proposal by default or one Learning Pack artifact only after explicit AN GO.

## When to use

Use this skill when the user asks to:

- Learn a topic quickly from the vault.
- Create a Fast Start, learning path, study pack, or Learning Pack.
- Turn a `source_id` such as `ARCH_TIS` into a structured self-study artifact.
- Organize existing atoms into concept order, practice tasks, review questions, and source trace.
- Prepare a learning outline before `wiki-review-drill`, `pedagogy`, or `wiki-to-deliverable`.

Primary owner: `@librarian`.

## When not to use

Do not use this skill for:

- Ingesting sources, converting PDFs, scraping web pages, or rebuilding the index.
- Creating, modifying, promoting, or deleting atoms.
- Patching `concepts/`, `entities/`, `sources/`, `comparisons/`, `queries/`, or `synthesis/`.
- Setting `SYNTHESIZED` or presenting the Learning Pack as final synthesis.
- Creating giáo án, slide decks, activity sheets, or rubrics. Handoff to `@designer` / `pedagogy` for that.
- Broad vault maintenance or skill governance work.

## Inputs

Accept one of:

- `source_id`, for example `ARCH_TIS`.
- Topic name, for example `Thinking in Systems`.
- A set of atom filenames or atom IDs.
- A user goal, for example "học nhanh trong 90 phút" or "ôn để áp dụng vào thiết kế vault".

Before writing any file, confirm the target output path and get explicit AN GO for that Learning Pack artifact.

## Output contract

Use this exact structure for the Learning Pack:

```md
# Big Picture
# Key Concepts
# Concept Map
# Must-Know Atoms
# Comparison Table
# Failure Modes
# Practice Task
# Review Questions
# Related Projects
# Source Trace
# Missing Context
# Next Action
```

Keep the pack practical: it should tell the user what to learn first, what to compare, what mistakes to avoid, and how to apply the topic.

## Status policy

- Prefer `VERIFIED` / `SYNTHESIZED` atoms.
- Use `DRAFT` atoms only if the output is labeled `EXPLORATORY`.
- Do not use atoms that lack source trace.
- If atom status is mixed or source trace is incomplete, state that in `Missing Context`.
- Do not present DRAFT, untraced, NotebookLM recon, or preview-only material as confirmed knowledge.

If metadata is included in a Learning Pack artifact, use `status: "DRAFT"` or `status: "LEARNING_DRAFT"`.

## Workflow

1. Identify the topic, `source_id`, or atom set.
2. Check wiki status or index context to confirm the topic already has atoms.
3. Use `wiki-query` for exact keywords, known atoms, source tracing, and graph traversal.
4. Use `wiki-semantic-search` only when keyword search is weak or the user does not remember the exact term.
5. Select a small must-know set before expanding related atoms.
6. Build a 60-90 minute learning path: big picture, key concepts, comparisons, failure modes, practice, review.
7. Add `Source Trace` to atom/source references; do not cite NotebookLM recon as source of truth.
8. Put unresolved gaps in `Missing Context`; route gap discovery to `wiki-breakdown` if needed.
9. Return a chat-only proposal unless AN explicitly approved writing the Learning Pack file.

## Write boundary

Default behavior is chat-only.

With explicit AN GO for a Learning Pack file, write only under:

```text
3-resources/wiki/learning_packs/
```

Do not:

- Patch concepts/entities/sources or any atom folder.
- Run ingest, promote, rebuild, scrape, or PDF conversion.
- Create more than one Learning Pack artifact for one request unless AN explicitly asks.
- Write to `synthesis/` or set `SYNTHESIZED`.

## Handoff rules

- Handoff to `wiki-query` for exact retrieval and source trace.
- Handoff to `wiki-semantic-search` when the user describes the idea but lacks exact keywords.
- Handoff to `wiki-breakdown` when missing concepts block fast learning.
- Handoff to `wiki-learning-audit` when the user wants to mark learned-but-unpracticed knowledge.
- Handoff to `@designer` / `pedagogy` only after the user wants lesson plans, slides, rubrics, or activity sheets.
- Handoff to `wiki-review-drill` if/when that skill exists and the user wants recall/transfer practice after a Learning Pack.

## Learning audit boundary

Do not run `wiki-learning-audit` automatically from this skill.

Only recommend `wiki-learning-audit` as a next step when the Learning Pack identifies unpracticed, weak, or practice-unverified concepts.

Because `wiki-learning-audit` can update frontmatter and review queue entries, it requires a separate AN GO and must start with dry-run.

## Regression cases

### Case 1: ARCH_TIS Fast Start

Input:

```text
Tạo Learning Pack Fast Start cho ARCH_TIS
```

Expected:

- Gather relevant indexed atoms by `source_id/topic`.
- Produce the Output Contract.
- If file writing is approved, write only `3-resources/wiki/learning_packs/LEARNING_PACK_ARCH_TIS_Fast_Start.md`.
- Do not create atoms, run ingest, or rebuild.

### Case 2: Mixed status atoms

Input:

```text
Tạo Learning Pack cho một topic có cả VERIFIED và DRAFT atoms
```

Expected:

- Prefer VERIFIED/SYNTHESIZED atoms.
- Label DRAFT-based sections as `EXPLORATORY`.
- Put missing trace/status concerns in `Missing Context`.

### Case 3: User asks for slides

Input:

```text
Biến ARCH_TIS thành slide dạy học
```

Expected:

- Do not create slides inside this skill.
- Prepare or reference a Learning Pack/outline first, then handoff to `@designer` / `pedagogy`.

## Validation checklist

Before claiming a Learning Pack is ready:

- [ ] Output follows the exact Output Contract.
- [ ] Important claims trace to atom/source references.
- [ ] Status policy is respected.
- [ ] `DRAFT` material, if used, is labeled `EXPLORATORY`.
- [ ] `Missing Context` lists gaps instead of hiding them.
- [ ] No atom, ingest, rebuild, promote, or synthesis action was performed.
- [ ] File write, if any, is a single artifact under `3-resources/wiki/learning_packs/` and had explicit AN GO.
