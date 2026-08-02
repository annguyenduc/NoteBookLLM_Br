# On-Demand Script Policy

This rule implements `SPEC_ON_DEMAND_SCRIPT_POLICY`.

Goal: keep heavy tools at zero idle RAM. Prefer one-shot scripts for heavy
capabilities, and keep persistent MCP background servers minimal.

Config source:

```text
.agent/config/on-demand-scripts.yaml
```

## Default

Agents may run allowlisted read-only, dry-run, query, report, or inspect scripts
without AN GO if the script exits after completion and does not modify state.

Agents must ask AN GO before any script or command with side effects.

## Required Routing Block

Before running any script, classify it in chat or terminal notes:

```yaml
SCRIPT_ROUTING_DECISION:
  script: "[script name]"
  mode: "safe_auto | needs_GO | blocked"
  reason: "[why]"
  writes_files: "YES | NO"
  touches_3_resources: "YES | NO"
  external_service: "YES | NO"
  persistent_process: "YES | NO"
  requires_AN_GO: "YES | NO"
```

If `requires_AN_GO: "NO"`, the agent may run it.

If `requires_AN_GO: "YES"`, stop and ask AN.

If `mode: "blocked"`, do not run it.

## Safe Auto

Safe auto scripts are one-shot scripts that only inspect, query, dry-run, or
report. They must exit after completion and print a clear summary.

Examples:

```powershell
python scripts/tasks/query_wiki.py "feedback loop"
python scripts/tasks/check_ram_processes.py
python scripts/tasks/inspect_mcp_config.py
python scripts/tasks/sqlite_query_once.py "select count(*) from atoms"
```

Allowed without GO only when all are true:

- read-only or dry-run
- no file writes or vault state changes
- no MCP profile changes
- no persistent server, daemon, watcher, or background process
- no git commit, push, merge, move, delete, promote, or rebuild
- no external file upload
- exits after completion

One-shot external queries are allowed without GO only when the current user task
explicitly needs the external service. The result must be displayed only unless
AN separately approves saving it.

## Requires AN GO

Ask AN GO before running:

- any script with `--apply`
- any script that writes, modifies, deletes, or moves files
- any script that touches `3-resources/`
- any script that promotes raw/wiki artifacts
- any index rebuild
- any actual MCP profile switch
- any NotebookLM ingest or export
- any persistent daemon or background server
- any external upload
- `git commit`, `git push`, or `git merge`

Known examples:

```text
switch_mcp_profile.ps1
promote.py
circuit_breaker.py promote
rebuild.py
wiki_ops.py --write
gap_promote.py
promote_atom.py
write_to_wiki.py
notebooklm_ingest.py
notebooklm_export.py
```

## Hard Stops

Stop immediately if a script:

- starts a background server unexpectedly
- writes while declared read-only
- touches `3-resources/raw_*`
- tries to promote an artifact
- modifies MCP config unexpectedly
- sends file or vault content externally without explicit task need
- hangs instead of exiting
- reports an undeclared side effect

Report the blocker and do not retry through a different tool.

## Output Contract

After every script run, report:

```yaml
SCRIPT_RUN_REPORT:
  script: "[script]"
  command: "[command]"
  mode: "safe_auto | needs_GO"
  result: "PASS | FAIL | PARTIAL"
  files_written: []
  files_modified: []
  external_service_called: "NONE | [service]"
  stayed_resident: "NO"
  summary: "[short result]"
```

## RAM Policy

Default workspace MCP stays light:

```text
filesystem only
```

Heavy tools should run as on-demand one-shot scripts:

- sqlite query once
- Tavily search once
- NotebookLM query once
- local-ai audit once
- wiki-ops inspect once

These are forbidden as default background MCP servers:

- notebooklm-mcp-server
- tavily Python wrapper
- local-ai MCP
- wiki-ops MCP
- github wrapper
