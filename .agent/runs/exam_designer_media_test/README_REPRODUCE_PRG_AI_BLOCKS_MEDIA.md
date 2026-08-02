# Reproduce PRG AI Blocks Media Preview

Purpose: let a future agent, including Gemini or Antigravity, recreate a real screenshot from PRG AI Blocks quickly and repeatably, without rediscovering the workflow.

Status: `PREVIEW_ONLY`, `NON_CANONICAL`.

Do not present the output as an official assessment asset until human review approves:
- wording
- answer visibility
- screenshot clarity
- source traceability

## What This Guide Is For

Use this guide only when the agent must create a real code-sample screenshot from:

- Tool: `PRG AI Blocks`
- URL: `https://playground.raise.mit.edu/create/`

This guide is not for:
- AI-generated fake screenshots
- direct exam publishing without review
- arbitrary Blockly reverse engineering outside the real page

This file is the canonical operational guide for this workflow. Do not maintain a second SOP file with conflicting steps.

## Future Agent Entry Point

Before touching PRG AI Blocks media generation in this worktree, a future agent should read these files in order:

1. [README.md](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/workspaces/dev-lab/tools/stem_exam_media/README.md>)
2. [README_REPRODUCE_PRG_AI_BLOCKS_MEDIA.md](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/README_REPRODUCE_PRG_AI_BLOCKS_MEDIA.md>)
3. [prg_ai_blocks_sample.xml](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/prg_ai_blocks_sample.xml>)
4. [prg_ai_blocks_sample_manifest.md](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/prg_ai_blocks_sample_manifest.md>)

If the goal is only to inspect the already validated preview artifact, open these directly:

- [prg_ai_blocks_sample.png](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/prg_ai_blocks_sample.png>)
- [prg_ai_blocks_sample.xml](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/prg_ai_blocks_sample.xml>)
- [prg_ai_blocks_sample_manifest.md](</D:/_agent_worktrees/20260612_stem_exam_media_phase1/.agent/runs/exam_designer_media_test/prg_ai_blocks_sample_manifest.md>)

## Required Output

A successful run must produce all 3 files:

1. `prg_ai_blocks_sample.png`
2. `prg_ai_blocks_sample.xml`
3. `prg_ai_blocks_sample_manifest.md`

If any of the 3 files is missing, the run is not complete.

## Canonical Reproduction Method

Use this exact method:

1. Open the real PRG AI Blocks page in Playwright Chromium.
2. Wait for the Blockly workspace to exist on the page.
3. Clear the main workspace.
4. Inject Blockly XML into `window.Blockly.getMainWorkspace()`.
5. Render the workspace.
6. Save the rendered workspace XML to disk.
7. Capture a screenshot from the real page.
8. Write a manifest for the asset.

Do not replace this with:
- synthetic image generation
- hand-drawn diagrams
- screenshots from a different Blockly site

## Agent Behavior Rules

If Gemini, Antigravity, or another agent runs this workflow, the default behavior must be:

1. design a short assessment-oriented code sample
2. write Blockly XML for that sample
3. open the real PRG AI Blocks page
4. try direct XML injection first
5. save raw screenshot, XML, and manifest
6. stop and report preview artifacts
7. require human review before official use

The agent must not improvise a different site, a synthetic screenshot, or an exam-ready final asset.

## Recommended Folder Layout

Run from a disposable probe folder, but write the final artifacts into a stable run folder.

Example:

```text
.agent/runs/<run_id>/
  probe/
    create_sample_xml.js
    package.json
    node_modules/
  prg_ai_blocks_sample.png
  prg_ai_blocks_sample.xml
  prg_ai_blocks_sample_manifest.md
```

Keep:
- `.png`
- `.xml`
- manifest

Delete after the run if no longer needed:
- `probe/node_modules`
- temporary scripts
- extra debug screenshots

## Environment Setup

Run in PowerShell.

```powershell
npx.cmd playwright --version
npx.cmd playwright install chromium
npm init -y
npm install playwright@1.60.0 --no-save
```

Notes:
- Use `npx.cmd`, not `npx`, because PowerShell execution policy may block `npx.ps1`.
- If Playwright cannot find Chromium, rerun `npx.cmd playwright install chromium`.
- If `require('playwright')` fails, run the script from the same directory where `npm install playwright@1.60.0 --no-save` was executed.

## Hard Rules For The Script

To avoid common agent mistakes:

1. Save the script file as UTF-8 if it contains Vietnamese.
2. Prefer ASCII-only sample text in the script if encoding is uncertain.
3. Do not assume `window.Blockly` exists immediately after page load.
4. Wait until both of these are true before injecting XML:
   - `window.Blockly` exists
   - `window.Blockly.getMainWorkspace()` returns a workspace
5. Always call:
   - `ws.clear()`
   - `Blockly.Xml.domToWorkspace(...)`
   - `ws.render()`
6. Save the XML actually rendered by the page, not just the source string you intended to load.

## Conditional Fallback: Load Extension Only If Needed

Do not assume AI extensions must always be loaded by clicking through the UI.

Required behavior:

1. Try direct XML injection first.
2. If the required block types are missing or do not render correctly, only then:
   - click `Add Extension`
   - load the required extension
   - retry XML injection

Examples of fallback-loaded extensions:
- `Teachable Machine`
- `Face Sensing`
- `Body Sensing`

Rule:
- `inject directly first`
- `load extension only if opcode or block type is missing`

## Minimal Reproduction Script

Save this as `create_sample_xml.js` in the probe directory.

This version is intentionally ASCII-safe so future agents do not get mojibake from bad file encoding.

```javascript
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const outDir = path.resolve('..');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });

  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'domcontentloaded',
    timeout: 60000
  });

  await page.waitForFunction(() => {
    return (
      window.Blockly &&
      typeof window.Blockly.getMainWorkspace === 'function' &&
      window.Blockly.getMainWorkspace()
    );
  }, { timeout: 60000 });

  await page.waitForTimeout(2000);

  const renderedXml = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    ws.clear();

    const xmlText = `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="event_whenflagclicked" id="exam_start" x="40" y="40">
        <next>
          <block type="sensing_askandwait" id="ask_ai">
            <value name="QUESTION">
              <shadow type="text">
                <field name="TEXT">What helps a computer learn patterns from data?</field>
              </shadow>
            </value>
            <next>
              <block type="control_if" id="if_answer_ai">
                <value name="CONDITION">
                  <block type="operator_equals" id="check_answer_ai">
                    <value name="OPERAND1">
                      <block type="sensing_answer" id="answer_value"></block>
                    </value>
                    <value name="OPERAND2">
                      <shadow type="text">
                        <field name="TEXT">AI</field>
                      </shadow>
                    </value>
                  </block>
                </value>
                <statement name="SUBSTACK">
                  <block type="looks_sayforsecs" id="say_correct">
                    <value name="MESSAGE">
                      <shadow type="text">
                        <field name="TEXT">Correct. AI can learn patterns from data.</field>
                      </shadow>
                    </value>
                    <value name="SECS">
                      <shadow type="math_number">
                        <field name="NUM">2</field>
                      </shadow>
                    </value>
                  </block>
                </statement>
              </block>
            </next>
          </block>
        </next>
      </block>
    </xml>`;

    const dom = B.Xml.textToDom(xmlText);
    B.Xml.domToWorkspace(dom, ws);
    ws.render();

    return new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws));
  });

  fs.writeFileSync(
    path.join(outDir, 'prg_ai_blocks_sample.xml'),
    renderedXml,
    'utf8'
  );

  await page.screenshot({
    path: path.join(outDir, 'prg_ai_blocks_sample.png'),
    fullPage: true
  });

  await browser.close();
})();
```

Run:

```powershell
node .\create_sample_xml.js
```

## Raw Screenshot vs Annotated Screenshot

Keep these separate:

- `raw screenshot`: direct screenshot from the real PRG AI Blocks page
- `annotated screenshot`: optional derivative with highlight boxes or callouts

Rules:
- never overwrite the raw screenshot
- never present the annotated screenshot as the source artifact
- if highlighting is needed, save a second file such as `.annotated.png`

## Pass / Fail Criteria

Pass only if all conditions below are true:

- the page opened at `/create/`
- `window.Blockly` was found
- the workspace was cleared before injection
- XML was rendered into the real page workspace
- `prg_ai_blocks_sample.xml` was written
- `prg_ai_blocks_sample.png` was written
- the screenshot visibly shows the injected block stack

Fail the run if any of these happen:

- screenshot is blank
- screenshot shows the wrong page
- XML file is missing
- text is unreadable
- blocks are disconnected unexpectedly
- the screenshot is from a synthetic or mocked source

## Forbidden Shortcuts

Do not:

- generate a fake screenshot with image AI
- use a different Blockly site and label it PRG AI Blocks
- skip saving XML
- skip manifest creation
- overwrite the raw screenshot with an annotated version
- embed the full manifest into the exam file

## Manifest Requirements

Every generated media asset from a real tool must have a manifest with at least:

```yaml
asset_id: "MEDIA_PRG_AI_BLOCKS_Q01_001"
file_name: "prg_ai_blocks_sample.png"
type: "image"
source_tool: "PRG AI Blocks"
source_url: "https://playground.raise.mit.edu/create/"
generation_method: "real_tool_blockly_xml_injection"
source_file: "prg_ai_blocks_sample.xml"
reproduction_guide: "README_REPRODUCE_PRG_AI_BLOCKS_MEDIA.md"
used_in: "Sample question: observe block code and predict behavior"
purpose: "Preview generated code-sample media for @exam-designer rule validation"
answer_leak_check: "NEEDS_REVIEW"
review_status: "PREVIEW_ONLY"
canonical_status: "NON_CANONICAL"
```

## Quality Checklist Before Exam Use

Before using a screenshot in an assessment:

- The screenshot came from the real tool.
- The XML file used for generation is saved.
- The manifest exists and is complete.
- The screenshot is readable at target document size.
- The question tells the learner exactly what to inspect.
- The screenshot does not accidentally reveal the answer unless that is intentional.
- A human has reviewed the asset before release.

## Known Failure Modes

- `npx` fails due to execution policy:
  - use `npx.cmd`

- Chromium is missing:
  - run `npx.cmd playwright install chromium`

- `require('playwright')` fails:
  - run `npm install playwright@1.60.0 --no-save` in the probe directory
  - run the script from that same directory

- `window.Blockly` is undefined:
  - confirm the page is `https://playground.raise.mit.edu/create/`
  - wait for the workspace with `page.waitForFunction(...)`

- Vietnamese text appears garbled:
  - save the script as UTF-8
  - or use ASCII-only sample text in the automation script

- Blocks are present but disconnected:
  - use properly nested XML with `<next>`, `<value>`, and `<statement>`
  - do not assemble blocks one by one unless necessary

- Screenshot is technically valid but not usable in an exam:
  - keep it as preview only
  - request human review

## Minimal Delivery Contract

The agent should report:

- output folder
- files created
- whether direct injection worked
- whether extension-loading fallback was required
- whether the asset set is raw only or raw + annotated
- whether human review is still required
