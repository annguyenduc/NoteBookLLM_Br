# SPEC — Run Package Ingest Runtime

Source context: `NoteBookLLM_Br` ingest pipeline  
Scope owner: `@pm`  
Status: `DRAFT`  
Phase target: `Phase A only`

## 1. Problem Statement

Current ingest runtime is too dependent on the interactive IDE session.

Observed issues:
- large PDF ingest keeps too much workflow state inside agent context
- `Converted_Sources` chunks exist, but there is no durable run-level workspace for resume
- long ingest runs do not have a canonical `state + manifest + outline + report` package
- `raw_ingest` is being forced to carry responsibility that belongs to pre-promote orchestration

This creates 3 recurring risks:
- runtime interruption loses operational context
- chunk-level processing can drift away from whole-document context
- Antigravity is implicitly acting as workflow executor instead of review/control surface

## 2. Objective

Introduce a deterministic, filesystem-backed run package between:

`00_Inbox/Converted_Sources/`  
and  
`3-resources/raw_ingest/`

This run package must:
- persist ingest runtime state outside the IDE session
- support resume for long PDF runs
- preserve whole-source context before atomization
- keep Antigravity as command/review surface, not execution memory

## 3. Non-Goals

Phase A does not:
- replace Docling with Ollama
- refactor `ingest.py` to package-native atomization
- change Human Gate or synthesis governance
- move final canonical storage away from `raw_ingest` or `wiki`
- introduce multi-worker ingest on Nitro 5

## 4. Target Architecture

### 4.1 Runtime Split

Antigravity:
- launch command
- inspect reports
- review diffs
- approve next step

Python runner:
- execute state machine
- update `state.json`
- write logs and reports
- resume from last durable stage

Converters:
- `pymupdf` fast path
- `docling` structured path
- OCR path when required

LLM:
- optional downstream language inference only
- not workflow memory
- not workflow coordinator

### 4.2 New Intermediate Layer

```text
runs/
└── ingest_[SOURCE_ID]_[DATE]/
    ├── state.json
    ├── manifest.md
    ├── outline.md
    ├── rolling_summary.md
    ├── chunks/
    ├── reports/
    ├── logs/
    └── failed_queue/
```

Meaning:
- `Converted_Sources` = technical converter output
- `runs/ingest_*` = resumable orchestration workspace
- `raw_ingest` = audited ingest fuel
- `wiki` = atomized knowledge

## 5. Phase A Contract

Phase A introduces run packaging without breaking current file-oriented downstream ingest.

### 5.1 Required Outputs

Each ingest run must produce:
- `state.json`
- `manifest.md`
- `outline.md`
- `reports/summary.md`
- `logs/run.log`

Optional:
- `rolling_summary.md`
- `failed_queue/`

### 5.2 Required CLI Surface

New runner contract:

```text
python scripts/ingest/ingest_runner.py \
  --source "<path>" \
  --chunk-size <n> \
  --mode dry-run|review|apply \
  --resume <run_path> \
  --max-workers 1 \
  --ocr off|auto|force
```

Default Nitro 5 policy:
- `chunk-size = 10..15`
- `max-workers = 1`
- `ocr = off` unless needed

## 6. State Model

`state.json` minimum schema:

```json
{
  "source_id": "book_x",
  "source_file": "00_Inbox/book.pdf",
  "run_dir": "runs/ingest_book_x_2026-05-16",
  "stage": "INIT",
  "mode": "review",
  "engine": "docling",
  "chunk_size": 10,
  "ocr": "off",
  "completed_batches": [],
  "failed_batches": [],
  "completed_chunks": [],
  "failed_chunks": [],
  "last_error": null
}
```

Rules:
- every stage transition must update `state.json`
- resume must read `state.json`, not rely on IDE memory
- failed stages must record `last_error`

## 7. Stage Model

Phase A runner state machine:

```text
INIT
-> CONVERT
-> BUILD_MANIFEST
-> BUILD_OUTLINE
-> PACKAGE_REPORT
-> READY_FOR_AUDIT
```

Phase A stops at `READY_FOR_AUDIT`.

Rationale:
- keeps scope small
- preserves compatibility with current downstream audit/promote flow
- avoids premature refactor of `ingest.py`

## 8. Converter Routing Policy

Routing policy must exist even if implementation is minimal in Phase A.

### 8.1 Modes

`fast`
- intended for text-native PDF
- preferred engine: `pymupdf` / `pymupdf4llm`

`structured`
- intended for layout-heavy PDF
- preferred engine: `docling`
- OCR off by default

`ocr`
- intended for scanned PDF
- preferred engine: Docling OCR or separate OCR engine

### 8.2 Policy Rule

Default:
- text-native PDF -> `fast`
- layout/table-heavy PDF -> `structured`
- scan/photo PDF -> `ocr`

Phase A may keep the implementation behind one runner while still recording chosen mode in `state.json` and `manifest.md`.

## 9. Manifest Contract

`manifest.md` is the whole-source control artifact.

Minimum contents:
- source id
- source file
- total pages if known
- conversion engine
- chunk size
- chunk inventory
- status per chunk

Purpose:
- move whole-document context out of prompt memory
- provide stable reference for later audit and atomization

## 10. Outline Contract

`outline.md` is the structure recovery artifact.

Minimum contents:
- front matter range
- chapter or section ranges
- chunk-to-page mapping
- heading extraction summary

Purpose:
- prevent chunk processing from losing whole-document structure
- provide document map before atomization

## 11. Governance Constraints

Phase A must preserve current repo doctrine:
- no direct writes to `3-resources/raw_*` outside official gates
- use `circuit_breaker.py` for promote
- do not atomize directly from transient `Converted_Sources` chunks
- deterministic scripts before LLM judgment
- long PDF runs must support resume

## 12. Acceptance Criteria

Phase A is acceptable only if:
- a PDF can produce a durable run directory under `runs/`
- killing the IDE session does not destroy ingest state
- rerun with `--resume` can continue from saved stage
- `manifest.md` and `outline.md` are generated deterministically
- no write to `raw_ingest` happens before audit/promote gate
- current downstream pipeline remains compatible

## 13. Risks

- run package may duplicate data already present in `Converted_Sources`
- package structure can drift if not normalized early
- partial implementation may tempt users to treat `runs/` as verified knowledge

## 14. Mitigations

- `runs/README.md` must explicitly mark `runs/` as transient workspace
- keep Phase A output minimal and deterministic
- delay package-native atomization to Phase B
- preserve current audit/promote boundary unchanged for now

## 15. Phase B Preview

Not in current implementation scope, but expected later:
- `raw_ingest/[source_id]/` source package
- folder-level promote contract
- `ingest.py --package`
- rolling summary and semantic chunk orchestration

