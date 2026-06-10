# Reproduce PRG AI Blocks Media Preview

Purpose: let a future agent recreate code-sample screenshots from PRG AI Blocks without rediscovering the workflow.

Status: `PREVIEW_ONLY`, `NON_CANONICAL`. Do not use these artifacts as official assessment assets until human review approves wording, answer visibility, and visual clarity.

## Source Tool

- Tool: PRG AI Blocks
- URL: https://playground.raise.mit.edu/create/
- Page title observed: `PRG AI Blocks`
- Browser automation used: Playwright Chromium
- Workspace API used: `window.Blockly.getMainWorkspace()` + `Blockly.Xml.domToWorkspace(...)`

## Generated Preview Artifacts

- `prg_ai_blocks_home.png`: baseline screenshot after opening the playground.
- `prg_ai_blocks_opcode_test.png`: probe screenshot proving common Scratch/Blockly opcodes can be instantiated.
- `prg_ai_blocks_sample.png`: final sample screenshot for review.
- `prg_ai_blocks_sample.xml`: XML source loaded into Blockly workspace.
- `prg_ai_blocks_sample_manifest.md`: metadata and review state for the final sample.

## Environment Setup

Run from any writable scratch/probe directory, preferably under `.agent/runs/<run_id>/`:

```powershell
npx.cmd playwright --version
npx.cmd playwright install chromium
npm init -y
npm install playwright@1.60.0 --no-save
```

Notes:
- Use `npx.cmd`, not `npx`, because PowerShell may block `npx.ps1` by execution policy.
- If Playwright says the browser executable is missing, run `npx.cmd playwright install chromium`.
- Delete temporary `node_modules`/probe folders after the run. Keep only screenshots, XML/source, and manifest if they are useful evidence.

## Minimal Reproduction Script

Save as `create_sample_xml.js` inside the probe directory and run `node create_sample_xml.js`.

```javascript
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const outDir = path.resolve('..');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'networkidle',
    timeout: 60000
  });
  await page.waitForTimeout(4000);

  const result = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    ws.clear();

    const xmlText = `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="event_whenflagclicked" id="exam_start" x="40" y="40">
        <next>
          <block type="sensing_askandwait" id="ask_ai">
            <value name="QUESTION">
              <shadow type="text"><field name="TEXT">Công nghệ nào giúp máy tính nhận biết mẫu từ dữ liệu?</field></shadow>
            </value>
            <next>
              <block type="control_if" id="if_answer_ai">
                <value name="CONDITION">
                  <block type="operator_equals" id="check_answer_ai">
                    <value name="OPERAND1"><block type="sensing_answer" id="answer_value"></block></value>
                    <value name="OPERAND2"><shadow type="text"><field name="TEXT">AI</field></shadow></value>
                  </block>
                </value>
                <statement name="SUBSTACK">
                  <block type="looks_sayforsecs" id="say_correct">
                    <value name="MESSAGE"><shadow type="text"><field name="TEXT">Đúng! AI có thể học mẫu từ dữ liệu.</field></shadow></value>
                    <value name="SECS"><shadow type="math_number"><field name="NUM">2</field></shadow></value>
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

  fs.writeFileSync(path.join(outDir, 'prg_ai_blocks_sample.xml'), result, 'utf8');
  await page.screenshot({
    path: path.join(outDir, 'prg_ai_blocks_sample.png'),
    fullPage: true
  });
  await browser.close();
})();
```

## Manifest Requirements

Every generated media asset from a real tool must have a manifest with at least:

```yaml
asset_id: "MEDIA_PRG_AI_BLOCKS_Q01_001"
file_name: "prg_ai_blocks_sample.png"
type: "image"
source_tool: "PRG AI Blocks"
source_url: "https://playground.raise.mit.edu/create/"
generation_method: "tool_api_generated"
source_file: "prg_ai_blocks_sample.xml"
used_in: "Sample question: observe block code and predict behavior"
purpose: "Preview generated code-sample media for @exam-designer rule validation"
answer_leak_check: "NEEDS_REVIEW"
review_status: "PREVIEW_ONLY"
canonical_status: "NON_CANONICAL"
```

## Quality Checklist

Before using a screenshot in an exam:

- The screenshot is from the real tool or clearly labeled `SYNTHETIC_MEDIA`.
- The XML/source file or reproduction steps are saved.
- The screenshot does not leak an answer unless the task is to identify/debug that answer.
- The text is readable at target document size.
- The question states exactly what students should observe.
- The manifest has `answer_leak_check` and `review_status`.
- Human review happens before any official release.

## Known Failure Modes

- `npx` fails with execution policy: use `npx.cmd`.
- Playwright package exists but browser missing: run `npx.cmd playwright install chromium`.
- `require('playwright')` fails from temp scripts: create a probe directory and run `npm install playwright@1.60.0 --no-save` there.
- `window.Blockly` missing: wait longer after page load or verify the page URL is `/create/`.
- Blocks render but are disconnected: use Blockly XML with `<next>`, `<value>`, and `<statement>` nesting instead of creating blocks one by one.
- Generated media is only preview evidence unless a human reviews and approves it.
