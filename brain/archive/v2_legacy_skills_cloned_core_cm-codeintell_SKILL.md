---



name: cm-codeintell
description: "CORE — Project Topology & Intelligence. Tạo Skeleton Index, AST knowledge graph và sơ đồ kiến trúc đa ngôn ngữ."
version: 3.0.0
---

# cm-codeintell — Code Intelligence (PRO)

> **Goal:** Transform manual code reading into structural querying. Use Skeleton Index (< 4s) + AST graph + Mermaid diagrams to deeply understand any codebase — small or massive.

## When to Activate

- Starting work on an unfamiliar codebase
- Planning a refactor that spans multiple modules
- Debugging a complex chain of callers/callees
- Needing an architectural overview before making decisions

## Instructions

### The 5-Layer Intelligence Model

| Layer | Name | Tech | Output / Benefit |
|-------|------|------|-----------------|
| **L0** | **Topology** | Analysis | Recognize module boundaries & main data flows. |
| **L1** | **Skeleton** | Grep/POSIX | `.cm/skeleton.md` (Instant function signatures). |
| **L2** | **Graph** | Tree-sitter AST | SQLite DB (Callers/Callees/Impact). |
| **L3** | **Diagram** | Mermaid.js | `.cm/architecture.mmd` (Big picture view). |
| **L4** | **Context** | Synthesis | Focused context packet for the LLM. |

### Phase 0: Topology & Permission Gate

Before any query, the agent must:
1. **Permission Gate (`cm-identity-guard`):**
   - Authenticate if topology scan crosses sensitive directories (`.ssh`, `vault/`, `secrets/`).
2. **Identify Entry Points:** Find main launch files (main, index, app).
3. **Map Dependencies:** Read `package.json`, `requirements.txt` or equivalent.

### Advanced Intelligence Tools

- `codegraph_search(symbol)` — Find a symbol by name or meaning.
- `codegraph_callers(func)` — Trace who calls this function.
- `codegraph_impact(symbol)` — Predict what breaks if this symbol changes.
- **Recursive Indexing:** Automatically re-run indexing when the directory structure changes by > 10%.

### Integration with Other Skills

1. **`cm-start`:** Auto-detect project scale and set up the appropriate layer.
2. **`cm-planning`:** Use `impact_analysis` to flag high-risk areas in the plan.
3. **`cm-debugging`:** Trace root causes through call chains (Callers/Callees).

## Quality Gate (Red Flags)

- ❌ Maintaining a stale index → Creates an illusion about the current code structure.
- ❌ Scanning a large codebase (> 200 files) with `list_dir` without a Skeleton index.
- ❌ Missing "silent dependencies" (implicit dependencies via strings or config chains).

## Example Triggers

- "Explain the structure of this project (Topology)."
- "Run Impact Analysis for refactoring the login function."
- "Update the Skeleton Index for this project."
- "Show me who calls `processPayment()` and what it depends on."
