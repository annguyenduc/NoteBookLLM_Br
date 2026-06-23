const { chromium } = require('playwright');
const path = require('path');

const mediaDir = path.resolve(__dirname, '..', 'GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media');

const tasks = [
  {
    id: 'cau_02_a',
    extensions: ['Translate', 'Text to Speech'],
    scale: 0.9,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="translate_getTranslate" x="40" y="40"><value name="WORDS"><shadow type="text"><field name="TEXT">hello</field></shadow></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block><block type="text2speech_speakAndWait" x="40" y="140"><value name="WORDS"><shadow type="text"><field name="TEXT">xin chao</field></shadow></value></block></xml>`
  },
  {
    id: 'cau_02_b',
    extensions: ['Translate', 'Face Sensing'],
    scale: 0.9,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="translate_getTranslate" x="40" y="40"><value name="WORDS"><shadow type="text"><field name="TEXT">hello</field></shadow></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block><block type="poseFace_affdexGoToPart" x="40" y="140"><field name="AFFDEX_POINT">11</field></block></xml>`
  },
  {
    id: 'cau_02_c',
    extensions: ['Text to Speech', 'Teachable Machine'],
    scale: 0.9,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="text2speech_speakAndWait" x="40" y="40"><value name="WORDS"><shadow type="text"><field name="TEXT">hello</field></shadow></value></block><block type="teachableMachine_useModelBlock" x="40" y="140"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></xml>`
  },
  {
    id: 'cau_02_d',
    extensions: ['Translate'],
    scale: 0.9,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="broadcast_msg" id="q02d_msg">doc_ket_qua</variable></variables><block type="translate_getTranslate" x="40" y="40"><value name="WORDS"><shadow type="text"><field name="TEXT">hello</field></shadow></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block><block type="event_broadcast" x="40" y="140"><value name="BROADCAST_INPUT"><shadow type="event_broadcast_menu"><field name="BROADCAST_OPTION" id="q02d_msg" variabletype="broadcast_msg">doc_ket_qua</field></shadow></value></block></xml>`
  },
  {
    id: 'cau_07_a',
    extensions: ['Translate'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="translate_getTranslate" x="40" y="40"><value name="WORDS"><shadow type="text"><field name="TEXT">hello</field></shadow></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></xml>`
  },
  {
    id: 'cau_07_b',
    extensions: ['Text to Speech'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="text2speech_speakAndWait" x="40" y="40"><value name="WORDS"><shadow type="text"><field name="TEXT">xin chao</field></shadow></value></block></xml>`
  },
  {
    id: 'cau_07_c',
    extensions: ['Face Sensing'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="poseFace_affdexGoToPart" x="40" y="40"><field name="AFFDEX_POINT">11</field></block></xml>`
  },
  {
    id: 'cau_07_d',
    extensions: ['Teachable Machine'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="teachableMachine_useModelBlock" x="40" y="40"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></xml>`
  },
  {
    id: 'cau_23_a',
    extensions: [],
    scale: 0.95,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="looks_sayforsecs"><value name="MESSAGE"><block type="sensing_answer"></block></value><value name="SECS"><shadow type="math_number"><field name="NUM">2</field></shadow></value></block></next></block></next></block></xml>`
  },
  {
    id: 'cau_23_b',
    extensions: [],
    scale: 0.95,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q23b_var">ngon_ngu</variable><variable type="list" id="q23b_list">lua_chon</variable></variables><block type="data_setvariableto" x="40" y="40"><field name="VARIABLE" id="q23b_var" variabletype="">ngon_ngu</field><value name="VALUE"><shadow type="text"><field name="TEXT">English</field></shadow></value><next><block type="data_addtolist"><field name="LIST" id="q23b_list" variabletype="list">lua_chon</field><value name="ITEM"><block type="data_variable"><field name="VARIABLE" id="q23b_var" variabletype="">ngon_ngu</field></block></value></block></next></block></xml>`
  },
  {
    id: 'cau_23_c',
    extensions: ['Translate', 'Text to Speech'],
    scale: 0.9,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q23c_var">ban_dich</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q23c_var" variabletype="">ban_dich</field><value name="VALUE"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">fr</field></shadow></value></block></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="data_variable"><field name="VARIABLE" id="q23c_var" variabletype="">ban_dich</field></block></value></block></next></block></next></block></next></block></xml>`
  },
  {
    id: 'cau_23_d',
    extensions: ['Face Sensing'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="poseFace_affdexGoToPart" x="40" y="40"><field name="AFFDEX_POINT">11</field></block></xml>`
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
  await injectXml(page, task);
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
  console.log('Batch 3 full review rendered.');
})().catch(err => {
  console.error(err);
  process.exit(1);
});
