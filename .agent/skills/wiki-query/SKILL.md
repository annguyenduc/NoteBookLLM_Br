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
