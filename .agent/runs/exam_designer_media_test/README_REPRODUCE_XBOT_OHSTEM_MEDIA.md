# Reproduce xBot OhStem Media Preview

Purpose: let a future agent recreate real xBot block screenshots from OhStem App quickly and repeatably, without falling back to approximate SVG rendering when visual fidelity matters.

Status: `PREVIEW_ONLY`, `NON_CANONICAL`.

Do not present the output as an official assessment asset until human review approves:
- wording
- answer visibility
- screenshot clarity
- source traceability

## What This Guide Is For

Use this guide when the agent must create a real xBot code-block screenshot from:

- Tool: `OhStem App`
- Base URL: `https://app.ohstem.vn`
- Device: `xBot`
- Coding page target: `#!/codes/xbot`

This guide is not for:
- synthetic SVG approximations when fidelity is required
- AI-generated fake screenshots
- direct exam publishing without review

This file is the canonical operational guide for xBot screenshot capture in this worktree. Do not maintain a second SOP file with conflicting steps.

## Future Agent Entry Point

Before touching xBot media generation in this worktree, a future agent should read these files in order:

1. [README.md](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/workspaces/dev-lab/tools/stem_exam_media/README.md>)
2. [README_REPRODUCE_XBOT_OHSTEM_MEDIA.md](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/README_REPRODUCE_XBOT_OHSTEM_MEDIA.md>)
3. [capture_xbot_xml_playwright.js](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/workspaces/dev-lab/tools/stem_exam_media/capture_xbot_xml_playwright.js>)
4. [xbot_forward_left_1s_2s_speed50.xml](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/workspaces/dev-lab/tools/stem_exam_media/sample_specs/xbot_forward_left_1s_2s_speed50.xml>)

If the goal is only to inspect the already validated xBot preview artifact, open these directly:

- [cropped capture](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/xbot_forward_left_1s_2s_speed50_safe.png>)
- [full capture](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/xbot_forward_left_1s_2s_speed50_safe.full.png>)
- [source xml](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/xbot_forward_left_1s_2s_speed50_safe.xml>)
- [manifest](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/xbot_forward_left_1s_2s_speed50_safe_manifest.md>)

## Required Output

A successful run should produce at least these 3 artifacts:

1. cropped screenshot `.png`
2. injected Blockly XML `.xml`
3. full workspace screenshot `.full.png` for audit/debug

Optional but recommended:

4. manifest or run note

If the cropped screenshot or source XML is missing, the run is not complete.

## Canonical Reproduction Method

Use this exact flow:

1. Open `https://app.ohstem.vn` in Playwright Chromium.
2. Wait for the home page to stabilize.
3. Enter xBot from the visible home-page device link.
4. Enter the coding page from the visible xBot coding link.
5. Wait until both are true:
   - `window.Blockly` exists
   - `window.Blockly.getMainWorkspace()` returns a workspace
6. Clear the workspace.
7. Inject Blockly XML into the real xBot workspace.
8. Render the workspace.
9. Crop the screenshot to the rendered block bounds.
10. Save a full-page screenshot for audit/debug.

Do not replace this with:
- direct SVG mimicry when the user asked for sample fidelity
- screenshots from another Blockly site
- hand-built diagrams labeled as OhStem output

## Agent Behavior Rules

If a future agent runs this workflow, default behavior should be:

1. prefer Playwright capture over local SVG if the user cares about matching the sample
2. inspect existing validated XML or script first
3. navigate through the OhStem home page, not direct `/devices/xbot` loader route
4. inject XML only after the workspace exists
5. save cropped screenshot plus full-page screenshot
6. stop and report preview artifacts
7. require human review before official use

The agent must not:
- invent a different Blockly site
- label synthetic output as OhStem screenshot
- skip the safety prelude if the user explicitly asked to include it

## Validated Navigation

The following UI-driven navigation was validated in this session:

1. start at `https://app.ohstem.vn`
2. click visible link `a[href="/devices/xbot"]`
3. wait for xBot home
4. click visible link `a[href="/codes/xbot"]`
5. wait for Blockly workspace

Important:

- Direct navigation to `https://app.ohstem.vn/devices/xbot` can stall on a loader screen.
- Prefer the validated home-page bootstrap flow above.
- The app is SPA-style and hash routing matters. Let the page bootstrap itself before injection.

## Validated Script Files

Use these existing files first:

- [capture_xbot_xml_playwright.js](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/workspaces/dev-lab/tools/stem_exam_media/capture_xbot_xml_playwright.js>)
- [probe_xbot_playwright.js](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/workspaces/dev-lab/tools/stem_exam_media/probe_xbot_playwright.js>)

Current validated XML sample:

- [xbot_forward_left_1s_2s_speed50.xml](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/workspaces/dev-lab/tools/stem_exam_media/sample_specs/xbot_forward_left_1s_2s_speed50.xml>)

## Environment Setup

Run in PowerShell.

The validated flow in this worktree reused a cached `playwright` package from the local `npx` cache.

Example:

```powershell
$env:PLAYWRIGHT_PKG_DIR = "C:\Users\anngu\AppData\Local\npm-cache\_npx\e41f203b7505f1fb\node_modules\playwright"
```

Notes:

- This path is environment-specific.
- If the local `npx` cache changes, locate the new cached `playwright` package root first.
- Do not assume `require('playwright')` works from the repo root without this env var.

## Capture Command

Use the existing script:

```powershell
$env:PLAYWRIGHT_PKG_DIR = "C:\Users\anngu\AppData\Local\npm-cache\_npx\e41f203b7505f1fb\node_modules\playwright"
node workspaces\dev-lab\tools\stem_exam_media\capture_xbot_xml_playwright.js `
  --xml workspaces\dev-lab\tools\stem_exam_media\sample_specs\xbot_forward_left_1s_2s_speed50.xml `
  --out $env:TEMP\xbot_playwright_capture\xbot_forward_left_1s_2s_speed50_safe.png `
  --full $env:TEMP\xbot_playwright_capture\xbot_forward_left_1s_2s_speed50_safe.full.png
```

## Validated xBot Opcodes

The following block types were validated against the real xBot page:

- `xbot_led_onboard_clear`
- `xbot_move_stop`
- `block_wait_until`
- `xbot_button_onboard_read_digital`
- `block_control_sleep`
- `xbot_move_move_delay`
- `xbot_move_move`
- `xbot_move_turn_angle`

## Validated Safety Prelude

For xBot exam media, the following safety prelude was validated and should be preferred unless the user explicitly wants a shorter stack:

1. `tắt đèn led trên board`
2. `dừng di chuyển`
3. `chờ cho đến khi [nút trên board được nhấn]`
4. `chờ 1 giây`

Then append the exercise-specific movement blocks.

For the validated sample in this session, the movement task is:

5. `di chuyển [forward] với tốc độ 50 trong 1 giây`
6. `di chuyển [turn_left] với tốc độ 50 trong 2 giây`

## XML Rules

Use real xBot XML, not guessed pseudo-XML.

Validated details:

- `xbot_move_move_delay` uses:
  - field `direction`
  - value input `speed`
  - value input `time`
- `block_wait_until` uses value input `condition`
- `block_control_sleep` uses value input `duration`
- `xbot_button_onboard_read_digital` works as the reporter block inside `condition`

Example pattern:

```xml
<block type="block_wait_until">
  <value name="condition">
    <block type="xbot_button_onboard_read_digital"></block>
  </value>
</block>
```

## Inspection Rules

When inspecting the xBot toolbox or block definitions:

- do not assume `workspace.options.languageTree` is an XML DOM node
- on xBot it was validated as an object tree, not a DOM tree
- do not call `querySelectorAll(...)` on it blindly
- inspect it as JSON-like data first

## Screenshot Rules

For the cropped screenshot:

- inject XML first
- render the workspace
- find rendered blocks via `g.blocklyDraggable`
- compute the union of visible block bounding boxes
- crop with a small margin

Also save:

- a full-page screenshot for audit/debug

Do not overwrite the full screenshot with the cropped screenshot.

## Known Failure Modes

### 1. Loader screen never resolves

Symptom:
- page stays on blue loading screen after direct device URL

Response:
- restart from home page
- click visible `a[href="/devices/xbot"]`
- then click visible `a[href="/codes/xbot"]`

### 2. `window.Blockly` exists but workspace is null

Symptom:
- app shell loaded but code page not ready

Response:
- wait longer
- re-check `window.Blockly.getMainWorkspace()`

### 3. Toolbox inspection throws `querySelectorAll is not a function`

Symptom:
- xBot `languageTree` is not an XML DOM

Response:
- inspect `workspace.options.languageTree` as object data
- avoid DOM-only methods unless the type supports them

### 4. `require('playwright')` fails

Symptom:
- Node cannot resolve Playwright package from repo root

Response:
- set `PLAYWRIGHT_PKG_DIR`
- require Playwright from that explicit package root

## Pass / Fail Criteria

Pass:

- real xBot code page was opened
- Blockly workspace existed
- XML was injected into the real workspace
- cropped screenshot visibly shows the intended block stack
- full screenshot exists

Fail:

- screenshot is from synthetic renderer while claiming to be real capture
- screenshot is blank
- screenshot is from a different tool
- source XML is missing

## Current Validated Result

This session validated the combined safety + movement stack screenshot:

- [cropped capture](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/xbot_forward_left_1s_2s_speed50_safe.png>)
- [full capture](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/xbot_forward_left_1s_2s_speed50_safe.full.png>)
- [source xml](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/xbot_forward_left_1s_2s_speed50_safe.xml>)
- [manifest](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/xbot_forward_left_1s_2s_speed50_safe_manifest.md>)

These are preview artifacts, not canonical assets.
