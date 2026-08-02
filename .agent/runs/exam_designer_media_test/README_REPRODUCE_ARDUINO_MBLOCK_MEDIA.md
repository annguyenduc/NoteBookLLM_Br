# Reproduce Arduino mBlock Media Preview

Purpose: let a future agent recreate real Arduino Uno block screenshots from mBlock quickly and repeatably, without faking the blocks or guessing opcode structure.

Status: `PREVIEW_ONLY`, `NON_CANONICAL`.

Do not present the output as an official assessment asset until human review approves:
- wording
- answer visibility
- screenshot clarity
- source traceability

## What This Guide Is For

Use this guide when the agent must create a real Arduino block screenshot from:

- Tool: `mBlock IDE`
- URL: `https://ide.mblock.cc/`
- Device: `Arduino Uno`
- Developer source: `Ablock`

This guide is not for:
- synthetic Blockly lookalikes
- AI-generated fake screenshots
- direct exam publishing without review

This file is the canonical operational guide for Arduino screenshot capture in this worktree. Do not maintain a second SOP file with conflicting steps.

## Future Agent Entry Point

Before touching Arduino media generation in this worktree, a future agent should read these files in order:

1. [README.md](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/workspaces/dev-lab/tools/stem_exam_media/README.md>)
2. [README_REPRODUCE_ARDUINO_MBLOCK_MEDIA.md](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/README_REPRODUCE_ARDUINO_MBLOCK_MEDIA.md>)
3. [capture_arduino_uno_xml_playwright.js](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/workspaces/dev-lab/tools/stem_exam_media/capture_arduino_uno_xml_playwright.js>)
4. [arduino_uno_blink_d13_1s.xml](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/workspaces/dev-lab/tools/stem_exam_media/sample_specs/arduino_uno_blink_d13_1s.xml>)

If the goal is only to inspect the already validated preview artifact, open these directly:

- [arduino_uno_blink_d13_1s.png](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/arduino_uno_blink_d13_1s.png>)
- [arduino_uno_blink_d13_1s_manifest.md](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/arduino_uno_blink_d13_1s_manifest.md>)

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

1. Open `https://ide.mblock.cc/` in Playwright Chromium.
2. Wait for the IDE shell to finish loading.
3. Dismiss the optional privacy prompt if it appears.
4. Click `Add` in the device panel.
5. In Device Library, search `Ablock`.
6. Select `Arduino Uno` with `Developers: Ablock`.
7. Click `OK`.
8. Wait for the Arduino Uno categories to appear.
9. Hook the internal Blockly runtime from `window.webpackChunk_mblock_mblock_web`.
10. Clear the main workspace.
11. Inject Blockly XML into the real Arduino Uno workspace.
12. Render the workspace.
13. Crop the screenshot to the rendered block bounds.
14. Save a full-page screenshot for audit/debug.

Do not replace this with:
- screenshots from a different Blockly site
- synthetic image generation
- hand-built diagrams labeled as mBlock output

## Agent Behavior Rules

If a future agent runs this workflow, default behavior should be:

1. inspect the validated sample XML and capture script first
2. select the real `Arduino Uno / Ablock` device through the UI
3. inject XML only after the Arduino toolbox is live
4. save cropped screenshot plus full-page screenshot
5. stop and report preview artifacts
6. require human review before official use

The agent must not:
- capture from a different Arduino extension and label it `Ablock`
- rely on a synthetic renderer while claiming it is real mBlock output
- guess XML names when the live toolbox or block shape can be inspected directly

## Validated Device Selection

The following UI-driven selection was validated in this session:

1. start at `https://ide.mblock.cc/`
2. click visible `Add`
3. search `Ablock`
4. select `Arduino Uno` where the card also shows `Developers: Ablock`
5. click `OK`

After the selection succeeds, the body text should show Arduino-specific categories:

- `Pin`
- `serial port`
- `Data`
- `Sensor`
- `Events`
- `Control`
- `Operators`
- `Variables`
- `My Blocks`

## Validated Script Files

Use these existing files first:

- [capture_arduino_uno_xml_playwright.js](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/workspaces/dev-lab/tools/stem_exam_media/capture_arduino_uno_xml_playwright.js>)

Current validated XML sample:

- [arduino_uno_blink_d13_1s.xml](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/workspaces/dev-lab/tools/stem_exam_media/sample_specs/arduino_uno_blink_d13_1s.xml>)

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
node workspaces\dev-lab\tools\stem_exam_media\capture_arduino_uno_xml_playwright.js `
  --xml workspaces\dev-lab\tools\stem_exam_media\sample_specs\arduino_uno_blink_d13_1s.xml `
  --out .agent\runs\exam_designer_media_test\arduino_uno_blink_d13_1s.png `
  --full .agent\runs\exam_designer_media_test\arduino_uno_blink_d13_1s.full.png
```

## Validated Arduino Uno Opcodes

The following block types were validated against the real Arduino Uno / Ablock toolbox:

- `arduino_uno.arduino_when_board_launch`
- `arduino_uno.setDigital`
- `arduino_uno.getDigital`
- `arduino_uno.getAnalog`
- `arduino_uno.setPwm`
- `arduino_uno.setTone`
- `arduino_uno.setServo`
- `control_wait`
- `control_forever`

## Validated Sample Exercise

The first validated sample in this session reproduces the simple LED blink pattern from the Arduino training material:

1. `when Arduino Uno starts up`
2. `forever`
3. `set digital pin 13 output as high`
4. `wait 1 seconds`
5. `set digital pin 13 output as low`
6. `wait 1 seconds`

This is a good baseline because:
- it uses only validated core Arduino Uno blocks
- it matches the training content in `INT_HCM_Arduino`
- it is visually compact enough for exam media

## XML Rules

Use real Arduino Uno XML, not guessed pseudo-XML.

Validated details:

- `arduino_uno.arduino_when_board_launch` is the required startup hat block
- `arduino_uno.setDigital` uses:
  - value input `PORT`
  - field `LEVEL`
- `control_wait` uses value input `DURATION`
- the toolbox default for `PORT` is a `math_number` shadow

Validated example fragments:

```xml
<block type="arduino_uno.setDigital">
  <value name="PORT">
    <shadow type="math_number">
      <field name="NUM">13</field>
    </shadow>
  </value>
  <field name="LEVEL">1</field>
</block>
```

```xml
<block type="control_wait">
  <value name="DURATION">
    <shadow type="math_number">
      <field name="NUM">1</field>
    </shadow>
  </value>
</block>
```

## Runtime Rules

Important:

- `window.Blockly` was not exposed directly on `ide.mblock.cc` in this session
- the validated path is to hook the webpack runtime from `window.webpackChunk_mblock_mblock_web`
- then scan modules for a Blockly export whose workspace toolbox contains `category[id="arduino_uno.CATEGORY_PIN"]`

Do not assume the public global API matches OhStem or Scratch-hosted Blockly pages.

## Screenshot Rules

For the cropped screenshot:

- inject XML first
- render the workspace
- find rendered blocks via `svg.blocklySvg g.blocklyDraggable`
- compute the union of visible block bounding boxes
- crop with a small margin

Also save:

- a full-page screenshot for audit/debug

Do not overwrite the full screenshot with the cropped screenshot.

## Known Failure Modes

### 1. Device Library search fills the wrong input

Symptom:
- search text lands in another text box and the device list does not filter

Response:
- target `input[placeholder="Search"]` inside the modal
- confirm the filtered list shows `Arduino Uno` and `Developers: Ablock`

### 2. The wrong device is selected

Symptom:
- toolbox still shows `CyberPi` or another device after clicking `OK`

Response:
- select the device card by both texts:
  - `Arduino Uno`
  - `Developers: Ablock`

### 3. `window.Blockly` is undefined

Symptom:
- direct global Blockly access fails on mBlock

Response:
- hook `window.webpackChunk_mblock_mblock_web`
- scan runtime modules for the internal Blockly export

### 4. Screenshot includes left-side IDE UI instead of only the blocks

Symptom:
- crop bounds include sprites, device panel, or other non-block UI

Response:
- compute bounds only from `svg.blocklySvg g.blocklyDraggable`
- do not use a broader page-wide draggable selector

### 5. `require('playwright')` fails

Symptom:
- Node cannot resolve Playwright from the repo root

Response:
- set `PLAYWRIGHT_PKG_DIR`
- require Playwright from that explicit package root

## Pass / Fail Criteria

Pass:

- real `ide.mblock.cc` page was opened
- real `Arduino Uno / Ablock` device was selected
- Arduino toolbox categories were visible
- XML was injected into the real workspace
- cropped screenshot visibly shows the intended Arduino stack
- full screenshot exists

Fail:

- screenshot is from a different Arduino tool
- screenshot is synthetic while claiming to be real mBlock output
- source XML is missing
- wrong device extension was used

## Current Validated Result

This session validated the baseline blink sample:

- [cropped capture](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/arduino_uno_blink_d13_1s.png>)
- [full capture](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/arduino_uno_blink_d13_1s.full.png>)
- [source xml](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/arduino_uno_blink_d13_1s.xml>)
- [manifest](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/arduino_uno_blink_d13_1s_manifest.md>)

These are preview artifacts, not canonical assets.
