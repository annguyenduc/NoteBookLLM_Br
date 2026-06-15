# STEM Exam Media Pipeline - Phase 1

Status: `PREVIEW_ONLY`, `NON_CANONICAL`.

This dev-lab tool creates a local playground package for STEM exam media that needs an OhStem-style code-block visual and document export scaffolding. It does not write to `3-resources/`, does not create Atoms, and does not mark anything `VERIFIED` or `SYNTHESIZED`.

## Scope

- Render an OhStem-style SVG preview from a JSON media spec.
- Write an HTML playground page next to the SVG.
- Write a manifest with exam-designer media metadata.
- Write Quarto and Pandoc Markdown export templates that keep media paths local.

The renderer is not a real OhStem App screenshot generator. For official publication, replace preview SVGs with human-reviewed real tool screenshots when required.

For xBot media where visual fidelity matters, use the Playwright capture path against the real OhStem App workspace instead of the local SVG approximation.

See `.agent/runs/exam_designer_media_test/README_REPRODUCE_XBOT_OHSTEM_MEDIA.md` for the validated xBot operational workflow, known failure modes, and the safety-prelude sample.

For Arduino Uno media where block fidelity matters, use the Playwright capture path against the real mBlock IDE with the `Arduino Uno / Developers: Ablock` device, not the local SVG approximation.

See `.agent/runs/exam_designer_media_test/README_REPRODUCE_ARDUINO_MBLOCK_MEDIA.md` for the validated Arduino workflow, runtime hook, sample XML, and crop rules.

Future agents should treat that Arduino guide as the first operational entrypoint for real Arduino Uno / Ablock capture work, then read the linked script and XML sample before making changes.

The robotics palette is pinned to AITT-VN public source values from:

- `https://github.com/AITT-VN/yolouno_extension_robotics/blob/main/definition.js`
- `https://github.com/AITT-VN/yolouno_extension_robotics/blob/main/toolbox.xml`

- `root`: `#717171`
- `robot` / `drivebase`: `#ff4ccd`
- `motor`: `#0090f5`
- `sensor`: `#9b6af6`
- `line`: `#34ccf1`

## Run

From the repository root:

```powershell
python workspaces\dev-lab\tools\stem_exam_media\ohstem_renderer.py `
  --spec workspaces\dev-lab\tools\stem_exam_media\sample_specs\ohstem_line_follower.json `
  --out workspaces\dev-lab\sandbox\stem_exam_media_phase1\playground
```

Expected files:

- `media_ohstem_q01_001.svg`
- `media_ohstem_q01_001.html`
- `media_ohstem_q01_001_manifest.md`
- `exam_export.qmd`
- `exam_export.pandoc.md`

A tracked sample playground is included in `playground/`. The `sandbox/` command above is for disposable reruns.

## Real xBot Capture

The repo now includes a Playwright-based capture script for real xBot Blockly screenshots from `app.ohstem.vn`:

```powershell
$env:PLAYWRIGHT_PKG_DIR = "C:\Users\anngu\AppData\Local\npm-cache\_npx\e41f203b7505f1fb\node_modules\playwright"
node workspaces\dev-lab\tools\stem_exam_media\capture_xbot_xml_playwright.js `
  --xml workspaces\dev-lab\tools\stem_exam_media\sample_specs\xbot_forward_left_1s_2s_speed50.xml `
  --out $env:TEMP\xbot_playwright_capture\xbot_forward_left_1s_2s_speed50.png `
  --full $env:TEMP\xbot_playwright_capture\xbot_forward_left_1s_2s_speed50.full.png
```

Notes:

- `sample_specs/xbot_forward_left_1s_2s_speed50.xml` injects real `xbot_move_move_delay` blocks into the live xBot code page.
- `--out` is the cropped block screenshot.
- `--full` is optional and keeps the full workspace screenshot for audit/debug.
- The `PLAYWRIGHT_PKG_DIR` path is environment-specific; if the local `npx` cache changes, update it to the current cached `playwright` package root.

## Real Arduino Uno Capture

The repo now includes a Playwright-based capture script for real Arduino Uno Blockly screenshots from `ide.mblock.cc` using the `Ablock` extension:

```powershell
$env:PLAYWRIGHT_PKG_DIR = "C:\Users\anngu\AppData\Local\npm-cache\_npx\e41f203b7505f1fb\node_modules\playwright"
node workspaces\dev-lab\tools\stem_exam_media\capture_arduino_uno_xml_playwright.js `
  --xml workspaces\dev-lab\tools\stem_exam_media\sample_specs\arduino_uno_blink_d13_1s.xml `
  --out .agent\runs\exam_designer_media_test\arduino_uno_blink_d13_1s.png `
  --full .agent\runs\exam_designer_media_test\arduino_uno_blink_d13_1s.full.png
```

Notes:

- `sample_specs/arduino_uno_blink_d13_1s.xml` injects a real Arduino Uno blink stack into the live workspace.
- The script selects `Arduino Uno` where the device card shows `Developers: Ablock`.
- The crop bounds are computed only from `svg.blocklySvg g.blocklyDraggable` to avoid including unrelated IDE panels.
- The `PLAYWRIGHT_PKG_DIR` path is environment-specific; if the local `npx` cache changes, update it to the current cached `playwright` package root.

## Export

Use Quarto if available:

```powershell
quarto render exam_export.qmd --to html
quarto render exam_export.qmd --to docx
```

Use Pandoc if available:

```powershell
pandoc exam_export.pandoc.md --resource-path=. --standalone -o exam_export.html
pandoc exam_export.pandoc.md --resource-path=. --standalone -o exam_export.docx
```

This repo also contains a portable Pandoc binary under `scripts/learning/bin/` that can be used manually if system `pandoc` is unavailable.

## Report

See `PHASE1_REPORT.md` for the implementation boundary and verification evidence.

## Review Gate

Before exam use:

- confirm the media directly supports the question or rubric
- confirm the visual does not leak the answer unintentionally
- confirm the manifest is complete
- keep `review_status: "PREVIEW_ONLY"` until AN human review
