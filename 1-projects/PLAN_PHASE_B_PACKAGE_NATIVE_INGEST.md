# PLAN - Phase B Package-Native Ingest

Related goal: `Implement Approved Phase B Package-Native Ingest`
Related spec: `1-projects/SPEC_PHASE_B_PACKAGE_NATIVE_INGEST.md`
Owner: `@engineer`
Status: `DRAFT`

## 1. Bounded Scope Assessment

This implementation remains bounded and additive if package routing is activated only by explicit staging layout:

```text
00_Inbox/Staging_Raw_Ingest/<source_id>/...
```

This avoids changing the meaning of existing file-oriented promotes such as:

```text
00_Inbox/Staging_Raw_Ingest/RAW_....md
```

No broad refactor is required if we:
- keep old file routing unchanged
- add package routing only for explicit staged package paths
- add `ingest.py --package` as an additive interface

## 2. Files To Modify

- `scripts/maintenance/promote.py`
- `.agent/skills/wiki-ingest/scripts/ingest.py`

No change required unless proven necessary:
- `.kiro/circuit_breaker.py`

## 3. Exact Promote Routing Change

### 3.1 Activation Signal

Enable package-aware routing only when the staged file lives under:

```text
00_Inbox/Staging_Raw_Ingest/<source_id>/
```

Examples:

```text
00_Inbox/Staging_Raw_Ingest/arch_thinking_in_systems/manifest.md
00_Inbox/Staging_Raw_Ingest/arch_thinking_in_systems/outline.md
00_Inbox/Staging_Raw_Ingest/arch_thinking_in_systems/chunks/RAW_....md
```

### 3.2 Destination Mapping

- `manifest.md` or `RAW_*_MANIFEST.md`
  -> `3-resources/raw_ingest/<source_id>/manifest.md`
- `outline.md`
  -> `3-resources/raw_ingest/<source_id>/outline.md`
- `chunks/RAW_*.md`
  -> `3-resources/raw_ingest/<source_id>/chunks/<filename>.md`

If the staged path is not package-shaped:
- preserve current file-oriented routing unchanged

## 4. Exact `ingest.py --package` Interface

Add:

```text
python .agent/skills/wiki-ingest/scripts/ingest.py --package "<package_dir>"
```

Expected behavior:
- validate package directory exists
- resolve `manifest.md`
- validate `chunks/` exists and contains `RAW_*.md`
- confirm chunk files carry audit blocks
- reuse existing file-ingest path by ingesting the package manifest as the canonical control artifact

Backward compatibility:
- existing positional file path still works unchanged

## 5. Compatibility Tests

Required checks:
- old file-oriented promote dry-run still routes to `3-resources/raw_ingest/<filename>.md`
- package manifest dry-run routes to `3-resources/raw_ingest/<source_id>/manifest.md`
- package chunk dry-run routes to `3-resources/raw_ingest/<source_id>/chunks/<filename>.md`
- old file-oriented ingest still works
- `ingest.py --package <valid_package>` resolves manifest and chunks
- invalid package path fails cleanly

## 6. Rollback Risks

Primary risks:
- package routing accidentally capturing legacy file-oriented staging paths
- manifest promotion failing because staged package files are not audited
- `ingest.py --package` becoming a broad rewrite instead of a validation wrapper around existing file ingest

Mitigations:
- package mode activates only from explicit staging folder layout
- keep `ingest_file()` as the core file-ingest path
- fail fast when package manifest or chunks are missing/invalid

## 7. Decision

Proceed with implementation.

Reason:
- routing change can stay additive
- `ingest.py --package` can remain a thin wrapper
- current goal explicitly approves the required promote routing and package layout changes
