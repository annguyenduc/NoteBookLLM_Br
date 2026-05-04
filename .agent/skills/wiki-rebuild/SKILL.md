---
name: wiki-rebuild
description: "Đồng bộ hóa hạ tầng tri thức, cập nhật file chỉ mục (Index) và hệ thống liên kết ngược (Backlinks)."
---

Synchronize knowledge infrastructure, update indices, and manage backlink injection.

## Context
As the volume of atoms grows, manual index maintenance becomes impossible. `wiki-rebuild` maintains a live knowledge map and enables deep traceability via backlinks.

## Workflow

### Step 1: Structural Sync
Synchronize the state between the filesystem and the database.
```bash
python .agent/skills/wiki-rebuild/scripts/rebuild.py
```
This should be run **nightly** for maintenance.

### Step 2: Index Generation
Update the central `index.md` at `3-resources/wiki/index.md`. Categories include Concepts, Entities, Sources, and Synthesis.

### Step 3: Backlinks Injection
Inject a list of files linking to the current Atom into the `_backlinks` section at the end of each Markdown file.

## Constraints
- Do not alter the core content of an Atom when injecting backlinks.
- Always verify Database integrity before performing a sync.
