---
name: wiki-query
description: "Use when retrieving concept definitions, tracing source provenance, or discovering connections between Knowledge Atoms via keyword or graph traversal. Use wiki-semantic-search instead when keyword search returns poor results."
---

Retrieve knowledge from the Wiki using Hybrid Search (Full-Text Search + Graph Traversal).

## Context
When answering questions or mapping connections between atoms, `wiki-query` provides patterns to extract precise information from `wiki_brain.db`.

## Workflow

### Step 1: Keyword Search (FTS5)
Use full-text search to find atoms containing keywords in titles or metadata.
```sql
SELECT file_id, title, status, confidence 
FROM atom_search 
WHERE atom_search MATCH 'keyword' 
ORDER BY rank;
```

### Step 2: Graph Discovery (Link Tracing)
Expand search to related atoms.
```sql
-- Find related concepts
SELECT target_id, edge_type 
FROM edges 
WHERE source_id = 'atom_id';
```

### Step 3: Content Retrieval
Read the raw Markdown content using the `file_id` to synthesize the final answer.

## Constraints
- **Read-only**: Never execute `UPDATE/DELETE/INSERT` in this skill.
- **Status Priority**: Prioritize `SYNTHESIZED` or `VERIFIED` atoms. Warn if using `DRAFT`.
description: Use when the user needs keyword-based lookup, source tracing, or quick navigation across indexed wiki notes, and semantic search is unnecessary or has not been tried yet.
---

# Wiki Query

## Overview
Use this skill for direct, read-only lookup of indexed wiki knowledge. Start with exact terms, titles, or short phrases, then validate promising hits in the underlying markdown files.

## Guardrails
- Keep the workflow read-only.
- Prefer `SYNTHESIZED` and `VERIFIED` material over `DRAFT`.
- If the query is conceptual or fuzzy, switch to `wiki-semantic-search` instead of forcing keyword search.
- The helper script uses the legacy `nodes_fts` index; confirm real files before relying on snippets.

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
