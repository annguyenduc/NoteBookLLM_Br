# REPORT - Phase B Package-Native Ingest

Status: `IMPLEMENTED_WITH_LOCAL_FAILURES`

## Scope Completed

- additive package-aware promote routing in `scripts/maintenance/promote.py`
- additive `ingest.py --package` in `.agent/skills/wiki-ingest/scripts/ingest.py`
- backward compatibility preserved for file-oriented promote and file-oriented ingest

## Routing Contract Implemented

Package routing activates only for explicit staged package paths:

```text
00_Inbox/Staging_Raw_Ingest/<source_id>/...
```

Mappings:
- `manifest.md` or `RAW_*_MANIFEST.md` -> `3-resources/raw_ingest/<source_id>/manifest.md`
- `outline.md` -> `3-resources/raw_ingest/<source_id>/outline.md`
- `chunks/RAW_*.md` -> `3-resources/raw_ingest/<source_id>/chunks/<filename>.md`

Legacy file-oriented staging remains unchanged:

```text
00_Inbox/Staging_Raw_Ingest/RAW_*.md -> 3-resources/raw_ingest/<filename>.md
```

## Ingest Package Mode Implemented

New interface:

```text
python .agent/skills/wiki-ingest/scripts/ingest.py --package "<package_dir>"
```

Behavior:
- validates package directory
- requires `manifest.md`
- requires `chunks/` with `RAW_*.md`
- requires chunk audit blocks
- reuses existing ingest path by ingesting the manifest as the package control artifact

## Test Results

| Test | Result | Notes |
|---|---|---|
| `py_compile` for `promote.py` and `ingest.py` | PASS | no syntax errors |
| old file-oriented promote dry-run | PASS | still routes to `3-resources/raw_ingest/<filename>.md` |
| package chunk promote dry-run | PASS | routes to `3-resources/raw_ingest/arch_thinking_in_systems/chunks/<filename>.md` |
| old file-oriented ingest | PASS | staged file ingested successfully |
| `ingest.py --package <valid_package>` | PASS | manifest and chunk resolved, package ingest completed |
| `ingest.py --package <invalid_package>` | PASS | failed cleanly: missing `chunks/` |
| package manifest promote dry-run | FAIL | blocked by legacy manifest audit stamp missing `verify_scope` |

## Local Failures

- `00_Inbox/Staging_Raw_Ingest/arch_thinking_in_systems/manifest.md`
  - package promote dry-run is blocked because the legacy manifest audit stamp lacks `verify_scope`
  - this is an audit-compatibility issue in the staged test artifact, not an additive routing bug

## Compatibility Assessment

- file-oriented promote preserved: `YES`
- file-oriented ingest preserved: `YES`
- origin gate preserved: `YES`
- audit gate preserved: `YES`
- strict/personal policy preserved: `YES`
- bulk migration required: `NO`

## Recommendation

Next step:
- decide whether package manifest promotion should require a refreshed manifest audit contract
- or whether manifest files should be regenerated/audited in a package-specific way before package-level promote
