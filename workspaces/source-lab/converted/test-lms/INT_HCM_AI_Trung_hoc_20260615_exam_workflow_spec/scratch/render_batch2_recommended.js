const { chromium } = require('playwright');
const path = require('path');

const mediaDir = path.resolve(__dirname, '..', 'GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media');

const tasks = [
  {
    question: '06',
    imageName: 'cau_06_1.png',
    sourceName: 'cau_06_source.sb3',
    extensions: [],
    scale: 0.95,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">What's your name?</field></shadow></value><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">How old are you?</field></shadow></value></block></next></block></next></block></xml>`
  },
  {
    question: '08',
    imageName: 'cau_08_1.png',
    sourceName: 'cau_08_source.sb3',
    extensions: ['Face Sensing'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="poseFace_affdexGoToPart"><field name="AFFDEX_POINT">11</field></block></statement></block></next></block></next></block></xml>`
  },
  {
    question: '09',
    imageName: 'cau_09_1.png',
    sourceName: 'cau_09_source.sb3',
    extensions: ['Teachable Machine'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="teachableMachine_useModelBlock" x="40" y="40"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></xml>`
  },
  {
    question: '10',
    imageName: 'cau_10_1.png',
    sourceName: 'cau_10_source.sb3',
    extensions: ['Teachable Machine'],
    scale: 0.95,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="teachableMachine_videoToggle"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value><next><block type="teachableMachine_useModelBlock"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></next></block></next></block></xml>`
  },
  {
    question: '11',
    imageName: 'cau_11_1.png',
    sourceName: 'cau_11_source_pack.sb3',
    extensions: ['Translate', 'Text to Speech'],
    scale: 0.9,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q11_var">ban_dich</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q11_var" variabletype="">ban_dich</field><value name="VALUE"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="data_variable"><field name="VARIABLE" id="q11_var" variabletype="">ban_dich</field></block></value></block></next></block></next></block></next></block></xml>`,
    packXml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q11_var">ban_dich</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q11_var" variabletype="">ban_dich</field><value name="VALUE"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="data_variable"><field name="VARIABLE" id="q11_var" variabletype="">ban_dich</field></block></value></block></next></block></next></block></next></block><block type="event_whenflagclicked" x="420" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="sensing_answer"></block></value><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">Next word?</field></shadow></value></block></next></block></next></block></next></block></xml>`
  },
  {
    question: '11',
    imageName: 'cau_11_2.png',
    sourceName: 'cau_11_source_pack.sb3',
    extensions: ['Translate', 'Text to Speech'],
    scale: 0.9,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="sensing_answer"></block></value><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">Next word?</field></shadow></value></block></next></block></next></block></next></block></xml>`
  },
  {
    question: '12',
    imageName: 'cau_12_1.png',
    sourceName: 'cau_12_source_pack.sb3',
    extensions: ['Translate', 'Text to Speech'],
    scale: 0.88,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q12_var">ban_dich</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q12_var" variabletype="">ban_dich</field><value name="VALUE"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="data_variable"><field name="VARIABLE" id="q12_var" variabletype="">ban_dich</field></block></value></block></next></block></next></block></next></block></xml>`,
    packXml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q12_var">ban_dich</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q12_var" variabletype="">ban_dich</field><value name="VALUE"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="data_variable"><field name="VARIABLE" id="q12_var" variabletype="">ban_dich</field></block></value></block></next></block></next></block></next></block><block type="event_whenflagclicked" x="520" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q12_var" variabletype="">ban_dich</field><value name="VALUE"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="sensing_answer"></block></value></block></next></block></next></block></next></block><block type="event_whenflagclicked" x="1000" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></value></block></next></block></next></block><block type="event_whenflagclicked" x="1480" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="sensing_answer"></block></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q12_var" variabletype="">ban_dich</field><value name="VALUE"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></value></block></next></block></next></block></next></block></xml>`
  },
  {
    question: '12',
    imageName: 'cau_12_2.png',
    sourceName: 'cau_12_source_pack.sb3',
    extensions: ['Translate', 'Text to Speech'],
    scale: 0.88,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q12_var">ban_dich</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q12_var" variabletype="">ban_dich</field><value name="VALUE"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="sensing_answer"></block></value></block></next></block></next></block></next></block></xml>`
  },
  {
    question: '12',
    imageName: 'cau_12_3.png',
    sourceName: 'cau_12_source_pack.sb3',
    extensions: ['Translate', 'Text to Speech'],
    scale: 0.88,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></value></block></next></block></next></block></xml>`
  },
  {
    question: '12',
    imageName: 'cau_12_4.png',
    sourceName: 'cau_12_source_pack.sb3',
    extensions: ['Translate', 'Text to Speech'],
    scale: 0.88,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q12_var">ban_dich</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="sensing_answer"></block></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q12_var" variabletype="">ban_dich</field><value name="VALUE"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></value></block></next></block></next></block></next></block></xml>`
  },
  {
    question: '13',
    imageName: 'cau_13_1.png',
    sourceName: 'cau_13_source_pack.sb3',
    extensions: ['Translate', 'Text to Speech', 'Face Sensing', 'Teachable Machine'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="translate_getTranslate" x="40" y="40"><value name="WORDS"><shadow type="text"><field name="TEXT">hello</field></shadow></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></xml>`,
    packXml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="translate_getTranslate" x="40" y="40"><value name="WORDS"><shadow type="text"><field name="TEXT">hello</field></shadow></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block><block type="text2speech_speakAndWait" x="320" y="40"><value name="WORDS"><shadow type="text"><field name="TEXT">xin chao</field></shadow></value></block><block type="poseFace_affdexGoToPart" x="560" y="40"><field name="AFFDEX_POINT">11</field></block><block type="teachableMachine_useModelBlock" x="780" y="40"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></xml>`
  },
  {
    question: '13',
    imageName: 'cau_13_2.png',
    sourceName: 'cau_13_source_pack.sb3',
    extensions: ['Translate', 'Text to Speech', 'Face Sensing', 'Teachable Machine'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="text2speech_speakAndWait" x="40" y="40"><value name="WORDS"><shadow type="text"><field name="TEXT">xin chao</field></shadow></value></block></xml>`
  },
  {
    question: '13',
    imageName: 'cau_13_3.png',
    sourceName: 'cau_13_source_pack.sb3',
    extensions: ['Translate', 'Text to Speech', 'Face Sensing', 'Teachable Machine'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="poseFace_affdexGoToPart" x="40" y="40"><field name="AFFDEX_POINT">11</field></block></xml>`
  },
  {
    question: '13',
    imageName: 'cau_13_4.png',
    sourceName: 'cau_13_source_pack.sb3',
    extensions: ['Translate', 'Text to Speech', 'Face Sensing', 'Teachable Machine'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="teachableMachine_useModelBlock" x="40" y="40"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></xml>`
  },
  {
    question: '19',
    imageName: 'cau_19_1.png',
    sourceName: 'cau_19_source.sb3',
    extensions: ['Face Sensing'],
    scale: 0.95,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="poseFace_setVideoTransparency"><value name="TRANSPARENCY"><shadow type="math_number"><field name="NUM">50</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="poseFace_affdexGoToPart"><field name="AFFDEX_POINT">11</field></block></statement></block></next></block></next></block></next></block></xml>`
  },
  {
    question: '21',
    imageName: 'cau_21_1.png',
    sourceName: 'cau_21_source_pack.sb3',
    extensions: ['Teachable Machine'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="teachableMachine_videoToggle" x="40" y="40"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value></block></xml>`,
    packXml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="broadcast_msg" id="q21_msg">mo_camera</variable></variables><block type="event_whenkeypressed" x="40" y="40"><field name="KEY_OPTION">b</field><next><block type="teachableMachine_videoToggle"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value></block></next></block><block type="teachableMachine_useModelBlock" x="320" y="40"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></xml>`
  },
  {
    question: '21',
    imageName: 'cau_21_2.png',
    sourceName: 'cau_21_source_pack.sb3',
    extensions: ['Teachable Machine'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="teachableMachine_useModelBlock" x="40" y="40"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></xml>`
  },
  {
    question: '21',
    imageName: 'cau_21_3.png',
    sourceName: 'cau_21_source_pack.sb3',
    extensions: ['Teachable Machine'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="teachableMachine_videoToggle"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value></block></next></block></xml>`,
    captureMode: 'stage'
  },
  {
    question: '26',
    imageName: 'cau_26_1.png',
    sourceName: 'cau_26_source.sb3',
    extensions: [],
    scale: 0.95,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="list" id="q26_list">co_mat</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="data_deletealloflist"><field name="LIST" id="q26_list" variabletype="list">co_mat</field><next><block type="data_addtolist"><field name="LIST" id="q26_list" variabletype="list">co_mat</field><value name="ITEM"><shadow type="text"><field name="TEXT">An</field></shadow></value></block></next></block></next></block></xml>`
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

async function prepareBlocksUi(page) {
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

async function setWorkspaceXml(page, xml, scale) {
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
  }, { xml, scale });
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
  await prepareBlocksUi(page);
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
  if (!clip) throw new Error(`No block clip for ${outPath}`);
  await page.screenshot({ path: outPath, clip, omitBackground: true });
}

async function captureStage(page, outPath) {
  await restoreUi(page);
  const greenFlag = page.locator('[class*="green-flag_green-flag"], [class*="green-flag"]').first();
  if (await greenFlag.count()) {
    await greenFlag.click({ force: true });
    await page.waitForTimeout(1200);
  }
  const stage = page.locator('[class*="stage-wrapper"], [class*="stage_stage-wrapper"], [class*="stage_stage"]').first();
  if (await stage.count()) {
    const box = await stage.boundingBox();
    if (box) {
      await page.screenshot({
        path: outPath,
        clip: {
          x: Math.max(0, box.x),
          y: Math.max(0, box.y),
          width: Math.max(1, box.width),
          height: Math.max(1, box.height)
        }
      });
      return;
    }
  }
  await page.screenshot({ path: outPath });
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace(), { timeout: 60000 });
  await page.waitForTimeout(4000);

  const loaded = new Set();
  const exportedQuestions = new Set();

  for (const task of tasks) {
    for (const ext of task.extensions) {
      await loadExtension(page, loaded, ext);
    }

    if (!exportedQuestions.has(task.question)) {
      await setWorkspaceXml(page, task.packXml || task.xml, task.scale);
      await page.waitForTimeout(800);
      await exportProjectFile(page, path.join(mediaDir, task.sourceName));
      exportedQuestions.add(task.question);
    }

    await setWorkspaceXml(page, task.xml, task.scale);
    await page.waitForTimeout(800);

    const outPath = path.join(mediaDir, task.imageName);
    if (task.captureMode === 'stage') {
      await captureStage(page, outPath);
    } else {
      await captureBlocks(page, outPath);
    }
    console.log(`Rendered ${task.imageName}`);
  }

  await browser.close();
  console.log('Batch 2 recommended rendered.');
})().catch(err => {
  console.error(err);
  process.exit(1);
});
