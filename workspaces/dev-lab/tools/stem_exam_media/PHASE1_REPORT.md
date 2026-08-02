# STEM Exam Media Pipeline Phase 1 Report

Status: `PREVIEW_ONLY`, `NON_CANONICAL`.

## Routing

- Workspace: `workspaces/dev-lab`
- Branch/worktree: `agent/20260612-stem-exam-media-phase1`
- Canonical writes: no
- `3-resources/` writes: no
- Ingest lifecycle: no

## Delivered

- OhStem-style renderer: `ohstem_renderer.py`
- Sample spec: `sample_specs/ohstem_line_follower.json`
- Export templates: `templates/quarto_exam_export.qmd`, `templates/pandoc_exam_export.md`
- Tracked playground package: `playground/`
- Tests: `../../tests/stem_exam_media/test_ohstem_renderer.py`
- Review feedback fix: OhStem/Yolo robotics colors now use AITT-VN public source values from `definition.js` and `toolbox.xml`:
  - `root #717171`
  - `robot/drivebase #ff4ccd`
  - `motor #0090f5`
  - `sensor #9b6af6`
  - `line #34ccf1`

## Phase 1 Boundary

The renderer creates local preview media. It does not claim to be a real OhStem App screenshot. Official exam release should use a human-reviewed real tool screenshot if the assessment requires source-tool evidence.

## Validation Evidence

- Unit test passed: `Ran 3 tests ... OK`.
- AST syntax check passed: `AST_OK 2`.
- Portable Pandoc wrote `playground/exam_export.html` with exit code 0.
- Pandoc emitted Vietnamese translation warnings; the HTML export still completed.
- `git status --short | Select-String 3-resources` returned no matches.
