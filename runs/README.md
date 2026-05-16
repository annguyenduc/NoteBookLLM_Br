# runs/ - Transient Ingest Runtime Workspace

Purpose:
- hold resumable ingest runtime state outside the IDE session
- package pre-audit context such as `state.json`, `manifest.md`, `outline.md`, reports, and logs
- support interruption and resume for large PDF ingest runs

Rules:
- `runs/` is transient workspace, not canonical knowledge storage
- files under `runs/` are not verified knowledge by default
- `runs/` may copy or reference converter chunks from `00_Inbox/Converted_Sources/`
- only outputs that later pass audit and promote may become `raw_ingest` or `wiki` content

Phase A boundary:
- runner stops at `READY_FOR_AUDIT`
- no direct write to `3-resources/raw_ingest`
- no atomization refactor
