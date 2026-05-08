---
name: wiki-query
description: "Use when retrieving concept definitions, tracing source provenance, or discovering connections between Knowledge Atoms via keyword or graph traversal. Use wiki-semantic-search instead when keyword search returns poor results."
---

# Wiki Query

## Overview
Use this skill for direct, read-only lookup of indexed wiki knowledge. Start with exact terms, titles, or short phrases, then validate promising hits in the underlying markdown files.

## Guardrails
- Keep the workflow read-only.
- Prefer `SYNTHESIZED` and `VERIFIED` material over `DRAFT`.
- If the query is conceptual or fuzzy, switch to `wiki-semantic-search` instead of forcing keyword search.
- The helper script uses the legacy `nodes_fts` index; confirm real files before relying on snippets.
- When saving persistent research results to a file, use the template at `.agent/skills/references/QUERY_TEMPLATE.md`.


## Workflow
1. Start with a narrow keyword query.
2. Run:
   `python .agent/skills/wiki-query/scripts/wiki_query_helper.py --query "<terms>" --limit 5`
3. Open the returned file paths or IDs and verify the relevant passages in markdown.
4. If results are weak or irrelevant, escalate to `wiki-semantic-search`.

## Quick Reference
- Keyword helper:
  `python .agent/skills/wiki-query/scripts/wiki_query_helper.py --query "agent workflow" --limit 5`
- Supporting data sources:
  indexed DB tables, wiki markdown files, and graph edges for manual follow-up

## Common Mistakes
- Treating a snippet as final evidence without reading the source file.
- Using keyword search for abstract "what feels related?" questions.
- Writing SQL updates while in a query-only task.

## Technical Keywords (Audit)
- **FTS5**: SQLite Full-Text Search engine.
- **confidence**: Score used to rank query results.
- **USER.md**: Persona-based query tailoring.
- **R3**: Always validate source metadata.

## Technical Reference
- FTS5: SQLite Full-Text Search engine (BM25 ranking)
- confidence: score threshold cho reranking kết quả
- USER.md: đọc trước mọi LLM call để giới hạn output
- R3: mọi output phải có trích dẫn nguồn tuyệt đối
