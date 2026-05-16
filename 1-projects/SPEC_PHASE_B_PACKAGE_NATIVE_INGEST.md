# SPEC - Phase B Package-Native Ingest

Source context: `NoteBookLLM_Br` ingest pipeline
Scope owner: `@pm`
Status: `DRAFT`
Phase target: `Minimal Phase B`

## 1. Objective

Introduce minimal package-native ingest support without breaking the existing file-oriented flow.

Phase B must:
- preserve current file ingest behavior
- add package-aware storage under `raw_ingest/[source_id]/`
- let `ingest.py` accept a package path
- treat a package manifest as the canonical ingest control artifact

## 2. Problem Statement

Phase A proves that:
- run packages work
- chunk-scope audit works
- personal audit policy works
- staged chunk promotion works

But the downstream model is still file-native:
- promoted chunks land as loose files in `3-resources/raw_ingest/`
- `ingest.py` accepts a single file path only
- whole-source context remains split across many chunk files

This is operationally workable, but it is not yet package-native ingest.

## 3. Scope

This spec covers:
- `raw_ingest/[source_id]/` package layout
- package manifest as canonical source control artifact
- package-aware promote semantics
- `ingest.py --package`
- package-aware source tracing
- backward compatibility with current file ingest
- migration path from loose chunk files to package source

## 4. Non-Goals

This spec does not cover:
- atom schema redesign
- synthesis flow changes
- bulk vault migration
- Ollama/model strategy
- removal of file-oriented ingest
- bypass of audit or origin gates
- direct writes into `3-resources/raw_ingest`

## 5. Package Layout

Canonical package target:

```text
3-resources/raw_ingest/[source_id]/
```

Minimum contents:

```text
3-resources/raw_ingest/[source_id]/
├── manifest.md
├── outline.md
└── chunks/
    ├── RAW_...md
    ├── RAW_...md
    └── ...
```

Optional later additions:
- `reports/`
- `images/`
- `assets/`

## 6. Canonical Artifact

Within a package, the canonical ingest control artifact is:

```text
manifest.md
```

Rules:
- `manifest.md` is the package entrypoint for `ingest.py --package`
- chunk files remain evidence-bearing ingest fuel, not the top-level control artifact
- `outline.md` is supporting structure context, not the canonical control file

## 7. Promote Semantics

Phase B needs package-aware promote behavior.

Minimum required behavior:
- staged package content must still originate under `00_Inbox`
- promote must still enforce audit gate
- promote must still enforce origin gate
- package promotion must preserve the package directory boundary under `raw_ingest/[source_id]/`

Required semantic change:
- RAW chunk destination must be able to resolve to:

```text
3-resources/raw_ingest/[source_id]/chunks/<filename>.md
```

instead of only:

```text
3-resources/raw_ingest/<filename>.md
```

This is an additive routing change, not a governance change.

## 8. Ingest Interface

Current interface:

```text
python .../ingest.py "<file_path>"
```

Phase B additive interface:

```text
python .../ingest.py --package "3-resources/raw_ingest/[source_id]"
```

Expected behavior:
- resolve `manifest.md` inside the package
- use package metadata as ingest control context
- preserve existing file ingest path unchanged

Backward compatibility:
- file-path ingest remains valid
- package ingest is additive

## 9. Source Tracing

Package-native ingest must preserve traceability:
- package manifest must point back to source PDF
- chunk files must remain traceable to page range and manifest entry
- package ingest must not sever traceability just because the ingest target is now a directory

## 10. Migration Strategy

Migration must be additive and local:
- do not bulk rewrite existing `raw_ingest` immediately
- allow existing loose-file ingest to coexist during transition
- use package-native ingest first on newly promoted sources or controlled test sources

## 11. Implementation Boundary

Minimal implementation would likely require:
- additive promote routing for package destinations
- additive `ingest.py --package`
- package manifest resolution
- compatibility checks for both file and package paths

It must not require:
- replacing the current file ingest path
- package-wide rewrite of old sources
- direct filesystem bypass around `promote.py`

## 12. Risks

Primary risks:
- package routing ambiguity in `promote.py`
- broad refactor pressure inside `ingest.py`
- collision between loose-file and package-native storage
- package promotion becoming folder-level orchestration rather than bounded additive routing

## 13. Key Constraint

This Phase B is only acceptable if package-native ingest remains:
- additive
- bounded
- backward compatible

If implementation requires broad promote routing redesign or large ingest refactor, it exceeds the allowed minimal scope.

## 14. Gate Assessment

This spec remains minimal at the architecture level.

However, implementation is not yet automatically safe under the current execution gate because the spec implies:
- promote routing changes
- new destination semantics under `raw_ingest/[source_id]/`
- additive but real `ingest.py` interface expansion

Therefore:
- `Stage 2` may complete with this spec
- `Stage 3` requires explicit manual approval under the current goal gate

## 15. Definition of Done

This spec is complete when:
- package layout is defined
- canonical manifest role is defined
- package-aware promote semantics are defined
- `ingest.py --package` is defined
- backward compatibility is explicit
- the implementation risk boundary is explicit
