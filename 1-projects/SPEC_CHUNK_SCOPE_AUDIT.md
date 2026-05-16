# SPEC - Chunk Scope Audit

Source context: `NoteBookLLM_Br` ingest pipeline  
Scope owner: `@pm`  
Status: `DRAFT`  
Phase target: `Post-Phase A blocker remediation`  

## 1. Problem Statement

`md_auditor.py` currently applies full-PDF verification semantics to any Markdown file that declares a `Source PDF`.

Observed blocker:
- a run-package chunk such as `RAW_..._P028-028.md` is audited as if it should represent the whole source PDF
- `verify_convert` compares chunk text, pages, and images against the full source PDF
- chunk-level audit therefore fails correctly, even when the chunk itself is structurally valid

This blocks downstream file-oriented audit/promote for Phase A run packages.

## 2. Objective

Extend `md_auditor.py` audit semantics so that verification scope is explicit.

The tool must support:
- full-source audit
- chunk-scope audit
- package-scope audit interface

The immediate goal is only to unblock correct audit behavior for a single chunk Markdown file.

## 3. Scope

This spec covers:
- `md_auditor.py` CLI audit semantics
- scope-aware verification behavior
- manifest-assisted chunk verification contract
- acceptance criteria for chunk verification

## 4. Non-Goals

This spec does not:
- change `promote.py` folder semantics
- refactor `ingest.py` to `--package`
- introduce `raw_ingest/[source_id]/` package storage
- change atomization flow
- start Phase B package-native ingest
- require immediate implementation of package-level promote

## 5. Current Behavior

Current `md_auditor.py` behavior is valid only for:
- one Markdown file representing one whole source

Current failure mode for chunks:
- the auditor sees `Source PDF: ARCH_Thinking_in_Systems.pdf`
- it calls `verify_convert.py` with the full PDF and the single chunk file
- verification reports critical page loss, text loss, and image loss
- audit is marked `FAILED`

This is an audit semantics mismatch, not a Phase A design failure.

## 6. Target Audit Modes

### 6.1 Full-Source Audit

Use when:
- one Markdown file represents one whole PDF or equivalent source

Behavior:
- lint Markdown
- detect ligature/noise issues
- verify links/assets
- compare Markdown against the full source PDF
- generate normal audit stamp

### 6.2 Chunk-Scope Audit

Use when:
- one Markdown file represents only a page range or structured chunk of a source PDF

Behavior:
- lint Markdown
- detect ligature/noise issues
- verify links/assets
- determine expected scope from chunk metadata and/or manifest
- compare only the expected page range or chunk unit, not the entire PDF
- generate normal audit stamp using chunk-scope verification result

### 6.3 Package-Scope Audit

Use when:
- a run package or manifest should be verified as one complete converted package

Behavior target:
- verify all chunks together against the source PDF
- validate manifest inventory completeness
- compare total page coverage, text coverage, and asset inventory at package level

Important:
- package-scope is interface-only in this spec
- implementation may be deferred if needed to keep the change small

## 7. CLI Contract

Minimum CLI extension:

```text
python scripts/maintenance/md_auditor.py \
  "<markdown-file>" \
  --fix \
  --verify-scope chunk \
  --manifest "<run-dir>/manifest.md"
```

Required values for `--verify-scope`:
- `full-source`
- `chunk`
- `package`

Default behavior:
- if `--verify-scope` is omitted, keep current `full-source` semantics for backward compatibility

Manifest requirement:
- `--manifest` is required for `chunk` mode when chunk metadata alone is insufficient
- `--manifest` may be optional for `full-source`
- `--manifest` is expected for `package`

## 8. Chunk-Scope Verification Contract

For chunk mode, `md_auditor.py` must determine expected verification boundaries from one or more of:
- filename page range, such as `_P028-028.md`
- in-file metadata, such as:
  - `Chunk Unit ID`
  - `Chunk Range: Pages 28 to 28`
  - `Manifest File`
- manifest inventory entry matching the chunk filename

Chunk-mode verification must:
- confirm the chunk maps to the expected page range
- compare only that expected page range or chunk slice
- evaluate text and asset presence only within that scope
- avoid treating missing content outside the chunk scope as failure

Chunk-mode verification must not:
- compare chunk content against all 235 pages of the source PDF
- fail only because the chunk is smaller than the full source

## 9. Package-Scope Interface Contract

Package-scope should be designed so later work can accept:
- a manifest path
- a run directory
- or a canonical package control file

However, this spec does not require implementation now.

Allowed output for this spec:
- define CLI/interface expectations only

## 10. Backward Compatibility

Existing full-source audits must continue to work unchanged for:
- single-file converted sources
- manifest-style files already explicitly excluded from full-text parity in prior governance

Chunk-scope support must be additive.

## 11. Acceptance Criteria

This spec is satisfied only if future implementation can demonstrate:
- `RAW_..._P028-028.md` is not compared against the whole 235-page PDF
- chunk verification uses `P028-028` or the matching manifest entry as expected scope
- a chunk can pass audit without representing the full source
- full-source audit continues to behave as before for existing single-file flows
- no change is required to `promote.py` folder semantics
- no change is required to `ingest.py --package`

## 12. Risks

- scope detection may be ambiguous when chunk filenames or headers drift
- chunk-only verification could become too weak if page-range extraction is unreliable
- package-scope design could leak into Phase B if not boundary-checked

## 13. Mitigations

- prefer explicit `--verify-scope` over inference
- prefer manifest-backed chunk lookup when available
- keep package-scope implementation deferred until chunk mode is stable
- preserve current full-source default to avoid breaking old flows

## 14. Required Handoff

After spec approval:
- handoff to `@engineer` for implementation planning and code changes in `md_auditor.py`

## 15. Definition of Done

This spec is done when:
- the audit semantics mismatch is documented clearly
- the three audit modes are defined
- the CLI contract is explicit
- boundaries against Phase B and package-native ingest remain intact
