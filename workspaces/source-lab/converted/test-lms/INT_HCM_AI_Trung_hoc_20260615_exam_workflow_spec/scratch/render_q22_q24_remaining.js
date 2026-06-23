const { chromium } = require('playwright');
const path = require('path');

const mediaDir = path.resolve(__dirname, '..', 'GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media');

const tasks = [
  {
    id: 'cau_22_d',
    extensions: ['Teachable Machine', 'Text to Speech'],
    scale: 1.0,
    mode: 'xml',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q22d_var">ban_dich</variable></variables><block type="teachableMachine_useModelBlock" x="40" y="40"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block><block type="teachableMachine_whenModelMatches" x="40" y="170"><field name="CLASS_NAME">Class 1</field><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="data_variable"><field name="VARIABLE" id="q22d_var" variabletype="">ban_dich</field></block></value></block></next></block></xml>`
  },
  {
    id: 'cau_24_a',
    extensions: ['Face Sensing'],
    scale: 1.15,
    mode: 'xml',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="poseFace_affdexGoToPart"><field name="AFFDEX_POINT">11</field></block></statement></block></next></block></next></block></xml>`
  },
  {
    id: 'cau_24_b',
    extensions: [],
    scale: 1.2,
    mode: 'xml',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenkeypressed" x="40" y="40"><field name="KEY_OPTION">space</field><next><block type="looks_nextcostume"></block></next></block></xml>`
  },
  {
    id: 'cau_24_c',
    extensions: [],
    scale: 1.2,
    mode: 'xml',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="motion_gotoxy"><value name="X"><shadow type="math_number"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number"><field name="NUM">120</field></shadow></value></block></next></block></xml>`
  },
  {
    id: 'cau_24_d',
    extensions: ['Face Sensing'],
    scale: 1.15,
    mode: 'xml',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="poseFace_affdexGoToPart"><field name="AFFDEX_POINT">0</field></block></next></block></next></block></xml>`
  }
];

async function restoreUi(page) {
  await page.evaluate(() => {
    const style = document.getElementById('codex-render-style');
    if (style) style.remove();
  });
  await page.waitForTimeout(250);
}

async function loadExtension(page, loaded, name) {
  if (!name || loaded.has(name)) return;
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

async function injectXml(page, task) {
  await page.evaluate(({ xml, scale }) => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    ws.clear();
    const dom = B.Xml.textToDom(xml);
    B.Xml.domToWorkspace(dom, ws);
    ws.setScale(scale);
    ws.scrollX = 0;
    ws.scrollY = 0;
    ws.render();
  }, { xml: task.xml, scale: task.scale });
}

async function renderTask(page, task) {
  if (task.mode === 'xml') {
    await injectXml(page, task);
  } else {
    throw new Error(`Unknown mode: ${task.mode}`);
  }

  await page.waitForTimeout(1000);
  await exportProjectFile(page, path.join(mediaDir, `${task.id}.sb3`));
  await prepareUi(page);
  await page.waitForTimeout(500);

  const clip = await page.evaluate(() => {
    const ws = window.Blockly.getMainWorkspace();
    const blocks = ws.getAllBlocks(false);
    if (!blocks.length) return null;
    let minLeft = Infinity, minTop = Infinity, maxRight = -Infinity, maxBottom = -Infinity;
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

  if (!clip) throw new Error(`No clip rect for ${task.id}`);
  await page.screenshot({ path: path.join(mediaDir, `${task.id}.png`), clip, omitBackground: true });
  console.log(`Rendered ${task.id}`);
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace(), { timeout: 60000 });
  await page.waitForTimeout(4000);
  const loaded = new Set();
  for (const task of tasks) {
    for (const ext of task.extensions) {
      await loadExtension(page, loaded, ext);
    }
    await renderTask(page, task);
  }
  await browser.close();
  console.log('Q22/Q24 remaining files materialized.');
})().catch(err => {
  console.error(err);
  process.exit(1);
});
