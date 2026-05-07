---
name: wiki-semantic-search
description: "Use when wiki-query (keyword search) returns no results or irrelevant results, when the search intent is conceptual or abstract rather than exact-match, or when the user asks questions using meaning rather than specific terms."
---

# Wiki Semantic Search

## Overview
Use the local QMD search stack for meaning-based retrieval when exact terms are unknown or too brittle. Semantic retrieval is a search aid, not a substitute for source validation.

## Guardrails
- Use this after `wiki-query` fails or when the request is clearly conceptual.
- Validate any strong answer against the returned wiki file and, when needed, the raw source.
- Refresh embeddings after major ingest or rebuild work if the index is stale.
- Do not use semantic search for simple filename lookup or directory browsing.

## Workflow
1. Check index health:
   `qmd status`
2. Choose the search mode:
   `qmd vsearch "<concept question>"` for broader semantic retrieval.
   `qmd query "<complex question>"` for hybrid ranked retrieval.
3. Open the returned file with:
   `qmd get "<wiki/path.md>" --full`
4. Verify the answer against the file contents before citing it.
5. If new knowledge has not been embedded yet, run:
   `qmd embed`

## Quick Reference
- Semantic search:
  `qmd vsearch "agent memory versus knowledge graph"`
- Hybrid query:
  `qmd query "How does the vault separate verified from synthesized knowledge?"`
- Full retrieval:
  `qmd get "wiki/concepts/FILE.md" --full`

## Common Mistakes
- Forgetting to re-embed after large content changes.
- Taking a high-ranking result as proof without opening the source file.
- Using semantic search where a direct keyword query would be faster and clearer.
