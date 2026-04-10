# Skill System Standardization v5.0.0

## Phase 1 - Stabilize (No breaking path changes for consumers)
- Repair broken local references (`file:///...`) to repo-local relative links.
- Introduce alias map (`skill-alias-map.v5.json`) to preserve compatibility.
- Run structural validator and link checker.
- Freeze additions until validation passes.

## Phase 2 - Refactor Taxonomy (Controlled breaking change)
- Rename legacy `tot-*` folders to canonical names.
- Update frontmatter `name` fields to canonical IDs.
- Update skill index/routing tables and migration notes.
- Keep alias fallback for at least one release cycle.

## Success Metrics
- Mojibake markers in skill files: 0 critical files after remediation batch.
- Broken local links: 0.
- Taxonomy collisions after rename: 0.
- Validator pass rate: 100%.
