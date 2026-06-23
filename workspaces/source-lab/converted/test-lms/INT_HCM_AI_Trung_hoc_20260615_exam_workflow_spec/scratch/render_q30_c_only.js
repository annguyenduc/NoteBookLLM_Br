const { chromium } = require('playwright');
const path = require('path');

const mediaDir = path.resolve(__dirname, '..', 'GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media');

const xml = `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q30c_text">ban_dich</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="teachableMachine_videoToggle"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value><next><block type="teachableMachine_useModelBlock"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q30c_text" variabletype="">ban_dich</field><value name="VALUE"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="data_variable"><field name="VARIABLE" id="q30c_text" variabletype="">ban_dich</field></block></value></block></next></block></next></block></next></block></next></block></next></block></xml>`;

async function restoreUi(page) {
  await page.evaluate(() => {
    const style = document.getElementById('codex-render-style');
    if (style) style.remove();
  });
  await page.waitForTimeout(250);
}

async function loadExtension(page, loaded, name) {
  if (loaded.has(name)) return;
  await restoreUi(page);
  const extBtn = page.locator('[class^="gui_extension-button"]').first();
  await extBtn.click({ force: true });
  await page.waitForTimeout(1200);
  const card = page
    .locator('[class*="library-item_library-item"], [class*="library_library-item"]')
    .filter({ hasText: name })
    .first();
  await card.click({ force: true });
  await page.waitForTimeout(4500);
  loaded.add(name);
}

async function prepareUi(page) {
  await page.evaluate(() => {
    const style = document.createElement('style');
    style.id = 'codex-render-style';
    style.innerHTML = `
      [class*="gui_menu-bar"],
      [class*="gui_stage-and-target-wrapper"],
      [class*="gui_sidebar"] { display: none !important; }
      .blocklyToolboxDiv, .blocklyFlyout, .blocklyScrollbarBackground, .blocklyScrollbarHandle, .blocklyZoom { display: none !important; }
      .blocklyGridPattern { display: none !important; }
      .blocklyMainBackground { fill: none !important; fill-opacity: 0 !important; }
      .blocklySvg { background: transparent !important; background-color: transparent !important; }
      [class*="gui_blocks-wrapper"] {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: 9999 !important;
      }
      body { background: transparent !important; }
    `;
    const old = document.getElementById('codex-render-style');
    if (old) old.remove();
    document.head.appendChild(style);
  });
}

async function setWorkspaceXml(page) {
  await page.evaluate(({ xml }) => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    ws.clear();
    const dom = B.Xml.textToDom(xml);
    B.Xml.domToWorkspace(dom, ws);
    ws.setScale(0.72);
    ws.scrollX = 0;
    ws.scrollY = 0;
    ws.render();
  }, { xml });
}

async function exportProjectFile(page, outPath) {
  await restoreUi(page);
  const fileMenuBtn = page.locator('[class*="menu-bar_menu-bar-item"]').filter({ hasText: 'File' }).first();
  await fileMenuBtn.click();
  await page.waitForTimeout(500);
  const [download] = await Promise.all([
    page.waitForEvent('download', { timeout: 15000 }),
    page.locator('text="Save to your computer"').first().click()
  ]);
  await download.saveAs(outPath);
  await page.waitForTimeout(300);
}

async function captureBlocks(page, outPath) {
  const clip = await page.evaluate(() => {
    const ws = window.Blockly.getMainWorkspace();
    const blocks = ws.getAllBlocks(false);
    if (!blocks.length) return null;
    let minLeft = Infinity;
    let minTop = Infinity;
    let maxRight = -Infinity;
    let maxBottom = -Infinity;
    for (const block of blocks) {
      const root = block.getSvgRoot();
      if (!root) continue;
      const rect = root.getBoundingClientRect();
      if (!rect.width || !rect.height) continue;
      minLeft = Math.min(minLeft, rect.left);
      minTop = Math.min(minTop, rect.top);
      maxRight = Math.max(maxRight, rect.right);
      maxBottom = Math.max(maxBottom, rect.bottom);
    }
    if (minLeft === Infinity) return null;
    const pad = 4;
    return {
      x: Math.max(0, minLeft - pad),
      y: Math.max(0, minTop - pad),
      width: Math.max(1, (maxRight - minLeft) + pad * 2),
      height: Math.max(1, (maxBottom - minTop) + pad * 2)
    };
  });

  if (!clip) throw new Error('No clip for q30_c');
  await page.screenshot({ path: outPath, clip, omitBackground: true });
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace(), { timeout: 60000 });
  await page.waitForTimeout(4000);

  const loaded = new Set();
  for (const ext of ['Translate', 'Text to Speech', 'Teachable Machine']) {
    await loadExtension(page, loaded, ext);
  }

  await setWorkspaceXml(page);
  await page.waitForTimeout(900);
  await exportProjectFile(page, path.join(mediaDir, 'cau_30_c.sb3'));
  await prepareUi(page);
  await page.waitForTimeout(300);
  await captureBlocks(page, path.join(mediaDir, 'cau_30_c.png'));
  await browser.close();
  console.log('Rendered q30_c only.');
})().catch(err => {
  console.error(err);
  process.exit(1);
});
