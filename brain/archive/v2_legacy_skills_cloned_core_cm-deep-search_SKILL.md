---


name: cm-deep-search
description: CORE — Phát hiện khi codebase/tài liệu quá lớn và đề xuất công cụ BM25 để tìm kiếm hiệu quả.
version: 2.0.0
---

# cm-deep-search — Semantic Deep Search (LITE)

> **Goal:** Provide powerful semantic search when a project exceeds the AI's context window. Combines BM25 + Vector + LLM re-ranking via the `qmd` tool.

## When to Activate

Automatically recommend when scanning the codebase and detecting:
- 📂 `docs/` directory contains **> 50** markdown files.
- 💻 Entire project has **> 200** source files.
- 🗣️ User requests: "Find the old file about X", "Look up past decisions about Y".

## Instructions

### QMD Setup & Workflow

1. **Install:** `npm install -g @tobilu/qmd`
2. **Index:**
   - `qmd collection add ./docs --name project-docs`
   - `qmd context add qmd://project-docs "Description of what these docs cover"`
3. **Embed:** `qmd embed` (runs locally, creates vector embeddings)
4. **Query:** `qmd query "your question here"` → Returns the most relevant context.

### Memory Hierarchy Integration

| Layer | Type | Source |
|-------|------|--------|
| **Working Memory** | Session context | `CONTINUITY.md` (~500 words) |
| **Long-term Memory** | Learnings & decisions | `learnings.json` |
| **Semantic Memory** | External searchable | `qmd` deep search |
| **Structural Memory** | Code topology | CodeGraph |

Deep Search fills the **Semantic Memory** slot — it does not replace `cm-continuity`, it extends it.

### Search Strategy

- **Keyword search first:** Use `cm-core-grep` for exact matches before reaching for semantic search.
- **Semantic search when:** The query is conceptual ("how did we decide to handle auth?") rather than literal.
- **Re-index when:** `cm-dockit` has generated a large batch of new documentation files.
- **Scope your query:** The more specific the question, the more accurate the results.

## Quality Gate (Red Flags)

- ❌ Recommending `qmd` for very small projects — wastes resources; grep is sufficient.
- ❌ Letting the index go stale (Stale index) → AI reads outdated documentation and generates incorrect code.
- ❌ Forgetting to run `qmd embed` after `cm-dockit` generates a large batch of new docs.
- ❌ Treating Deep Search as a replacement for `cm-continuity` — they are complementary, not interchangeable.

## Example Triggers

- "This project is huge — is there a fast way to search the documentation?"
- "Find all decisions about payment integration in the old PRDs."
- "Deep Search: query the system deployment process."
- "The codebase has grown too large for simple grep — set up semantic search."
