const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const mediaDir = path.resolve(__dirname, '..', 'GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media');

const tasks = [
  {
    id: 'cau_17',
    extensions: ['Face Sensing'],
    scale: 1.25,
    raw: false,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="event_whenflagclicked" id="q17_start" x="40" y="40">
        <next>
          <block type="poseFace_videoToggle" id="q17_video">
            <value name="VIDEO_STATE">
              <shadow type="poseFace_menu_VIDEO_STATE">
                <field name="VIDEO_STATE">on-flipped</field>
              </shadow>
            </value>
            <next>
              <block type="control_forever" id="q17_forever">
                <statement name="SUBSTACK">
                  <block type="control_if" id="q17_if">
                    <value name="CONDITION">
                      <block type="poseFace_affdexIsExpression" id="q17_smile">
                        <value name="EXPRESSION">
                          <shadow type="poseFace_menu_EXPRESSION">
                            <field name="EXPRESSION">smile</field>
                          </shadow>
                        </value>
                      </block>
                    </value>
                    <statement name="SUBSTACK">
                      <block type="looks_sayforsecs" id="q17_say">
                        <value name="MESSAGE">
                          <shadow type="text">
                            <field name="TEXT">Xin chào!</field>
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
                </statement>
              </block>
            </next>
          </block>
        </next>
      </block>
    </xml>`
  },
  {
    id: 'cau_22',
    extensions: ['Face Sensing'],
    scale: 1.15,
    raw: false,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="event_whenflagclicked" id="q22_start" x="40" y="40">
        <next>
          <block type="poseFace_videoToggle" id="q22_video">
            <value name="VIDEO_STATE">
              <shadow type="poseFace_menu_VIDEO_STATE">
                <field name="VIDEO_STATE">on-flipped</field>
              </shadow>
            </value>
            <next>
              <block type="control_forever" id="q22_forever">
                <statement name="SUBSTACK">
                  <block type="control_if_else" id="q22_if">
                    <value name="CONDITION">
                      <block type="poseFace_affdexIsExpression" id="q22_smile">
                        <value name="EXPRESSION">
                          <shadow type="poseFace_menu_EXPRESSION">
                            <field name="EXPRESSION">smile</field>
                          </shadow>
                        </value>
                      </block>
                    </value>
                    <statement name="SUBSTACK">
                      <block type="looks_show" id="q22_show">
                        <next>
                          <block type="poseFace_affdexGoToPart" id="q22_goto">
                            <field name="AFFDEX_POINT">11</field>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <statement name="SUBSTACK2">
                      <block type="looks_hide" id="q22_hide"></block>
                    </statement>
                  </block>
                </statement>
              </block>
            </next>
          </block>
        </next>
      </block>
    </xml>`
  },
  {
    id: 'cau_23_a',
    extensions: ['Face Sensing'],
    scale: 1.12,
    raw: true,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <variables>
        <variable type="" id="q23_var_smile">Số lần cười</variable>
      </variables>
      <block type="event_whenflagclicked" id="q23a_start" x="40" y="40">
        <next>
          <block type="data_setvariableto" id="q23a_init">
            <field name="VARIABLE" id="q23_var_smile">Số lần cười</field>
            <value name="VALUE">
              <shadow type="text"><field name="TEXT">0</field></shadow>
            </value>
            <next>
              <block type="poseFace_videoToggle" id="q23a_video">
                <value name="VIDEO_STATE">
                  <shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow>
                </value>
                <next>
                  <block type="control_forever" id="q23a_forever">
                    <statement name="SUBSTACK">
                      <block type="control_if" id="q23a_if">
                        <value name="CONDITION">
                          <block type="poseFace_affdexIsExpression" id="q23a_smile">
                            <value name="EXPRESSION">
                              <shadow type="poseFace_menu_EXPRESSION"><field name="EXPRESSION">smile</field></shadow>
                            </value>
                          </block>
                        </value>
                        <statement name="SUBSTACK">
                          <block type="data_changevariableby" id="q23a_change">
                            <field name="VARIABLE" id="q23_var_smile">Số lần cười</field>
                            <value name="VALUE">
                              <shadow type="math_number"><field name="NUM">1</field></shadow>
                            </value>
                            <next>
                              <block type="control_wait" id="q23a_wait">
                                <value name="DURATION">
                                  <shadow type="math_positive_number"><field name="NUM">1</field></shadow>
                                </value>
                              </block>
                            </next>
                          </block>
                        </statement>
                      </block>
                    </statement>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </xml>`
  },
  {
    id: 'cau_23_b',
    extensions: ['Face Sensing'],
    scale: 1.02,
    raw: true,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <variables>
        <variable type="" id="q23_var_smile">Số lần cười</variable>
      </variables>
      <block type="event_whenflagclicked" id="q23b_start" x="40" y="40">
        <next>
          <block type="data_setvariableto" id="q23b_init">
            <field name="VARIABLE" id="q23_var_smile">Số lần cười</field>
            <value name="VALUE">
              <shadow type="text"><field name="TEXT">0</field></shadow>
            </value>
            <next>
              <block type="poseFace_videoToggle" id="q23b_video">
                <value name="VIDEO_STATE">
                  <shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow>
                </value>
                <next>
                  <block type="control_forever" id="q23b_forever">
                    <statement name="SUBSTACK">
                      <block type="control_if" id="q23b_if">
                        <value name="CONDITION">
                          <block type="poseFace_affdexIsExpression" id="q23b_smile">
                            <value name="EXPRESSION">
                              <shadow type="poseFace_menu_EXPRESSION"><field name="EXPRESSION">smile</field></shadow>
                            </value>
                          </block>
                        </value>
                        <statement name="SUBSTACK">
                          <block type="data_changevariableby" id="q23b_change">
                            <field name="VARIABLE" id="q23_var_smile">Số lần cười</field>
                            <value name="VALUE">
                              <shadow type="math_number"><field name="NUM">1</field></shadow>
                            </value>
                            <next>
                              <block type="control_wait_until" id="q23b_waituntil">
                                <value name="CONDITION">
                                  <block type="operator_not" id="q23b_not">
                                    <value name="OPERAND">
                                      <block type="poseFace_affdexIsExpression" id="q23b_smile2">
                                        <value name="EXPRESSION">
                                          <shadow type="poseFace_menu_EXPRESSION"><field name="EXPRESSION">smile</field></shadow>
                                        </value>
                                      </block>
                                    </value>
                                  </block>
                                </value>
                              </block>
                            </next>
                          </block>
                        </statement>
                      </block>
                    </statement>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </xml>`
  },
  {
    id: 'cau_24',
    extensions: ['Translate', 'Text to Speech'],
    scale: 0.92,
    raw: false,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <variables>
        <variable type="" id="q24_var_opt">Lựa chọn</variable>
        <variable type="" id="q24_var_orig">Câu gốc</variable>
      </variables>
      <block type="event_whenflagclicked" id="q24_start" x="40" y="40">
        <next>
          <block type="data_setvariableto" id="q24_set_lang">
            <field name="VARIABLE" id="q24_var_opt">Lựa chọn</field>
            <value name="VALUE"><shadow type="text"><field name="TEXT">1</field></shadow></value>
            <next>
              <block type="data_setvariableto" id="q24_set_text">
                <field name="VARIABLE" id="q24_var_orig">Câu gốc</field>
                <value name="VALUE"><shadow type="text"><field name="TEXT">Chào Việt Nam</field></shadow></value>
                <next>
                  <block type="control_if_else" id="q24_if1">
                    <value name="CONDITION">
                      <block type="operator_equals" id="q24_eq1">
                        <value name="OPERAND1"><block type="data_variable" id="q24_var1"><field name="VARIABLE" id="q24_var_opt">Lựa chọn</field></block></value>
                        <value name="OPERAND2"><shadow type="text"><field name="TEXT">1</field></shadow></value>
                      </block>
                    </value>
                    <statement name="SUBSTACK">
                      <block type="control_if_else" id="q24_if_len">
                        <value name="CONDITION">
                          <block type="operator_gt" id="q24_gt">
                            <value name="OPERAND1">
                              <block type="operator_length" id="q24_length">
                                <value name="STRING"><block type="data_variable" id="q24_var_text"><field name="VARIABLE" id="q24_var_orig">Câu gốc</field></block></value>
                              </block>
                            </value>
                            <value name="OPERAND2"><shadow type="math_number"><field name="NUM">10</field></shadow></value>
                          </block>
                        </value>
                        <statement name="SUBSTACK">
                          <block type="looks_sayforsecs" id="q24_toolong">
                            <value name="MESSAGE"><shadow type="text"><field name="TEXT">Too long</field></shadow></value>
                            <value name="SECS"><shadow type="math_number"><field name="NUM">2</field></shadow></value>
                          </block>
                        </statement>
                        <statement name="SUBSTACK2">
                          <block type="text2speech_speakAndWait" id="q24_speak_en">
                            <value name="WORDS">
                              <block type="translate_getTranslate" id="q24_trans_en">
                                <value name="WORDS"><block type="data_variable" id="q24_word_en"><field name="VARIABLE" id="q24_var_orig">Câu gốc</field></block></value>
                                <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                              </block>
                            </value>
                          </block>
                        </statement>
                      </block>
                    </statement>
                    <statement name="SUBSTACK2">
                      <block type="text2speech_speakAndWait" id="q24_speak_fr">
                        <value name="WORDS">
                          <block type="translate_getTranslate" id="q24_trans_fr">
                            <value name="WORDS"><block type="data_variable" id="q24_word_fr"><field name="VARIABLE" id="q24_var_orig">Câu gốc</field></block></value>
                            <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">fr</field></shadow></value>
                          </block>
                        </value>
                      </block>
                    </statement>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </xml>`
  },
  {
    id: 'cau_25',
    extensions: ['Face Sensing'],
    scale: 1.3,
    raw: false,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="event_whenflagclicked" id="q25_start" x="40" y="40">
        <next>
          <block type="poseFace_videoToggle" id="q25_video">
            <value name="VIDEO_STATE">
              <shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow>
            </value>
            <next>
              <block type="control_forever" id="q25_forever">
                <statement name="SUBSTACK">
                  <block type="poseFace_affdexGoToPart" id="q25_goto">
                    <field name="AFFDEX_POINT">11</field>
                    <next>
                      <block type="motion_changeyby" id="q25_changey">
                        <value name="DY"><shadow type="math_number"><field name="NUM">120</field></shadow></value>
                      </block>
                    </next>
                  </block>
                </statement>
              </block>
            </next>
          </block>
        </next>
      </block>
    </xml>`
  },
  {
    id: 'cau_26',
    extensions: ['Face Sensing'],
    scale: 1.45,
    raw: false,
    sourceXmlFile: path.join(mediaDir, 'cau_26.xml')
  },
  {
    id: 'cau_28',
    extensions: ['Face Sensing'],
    scale: 1.08,
    raw: false,
    sourceXmlFile: path.join(mediaDir, 'cau_28.xml')
  },
  {
    id: 'cau_28_block',
    extensions: ['Face Sensing'],
    scale: 2.2,
    raw: false,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="poseFace_affdexIsExpression" id="q28_block" x="40" y="40">
        <value name="EXPRESSION">
          <shadow type="poseFace_menu_EXPRESSION"><field name="EXPRESSION">smile</field></shadow>
        </value>
      </block>
    </xml>`
  }
];

function getXml(task) {
  if (task.sourceXmlFile) {
    return fs.readFileSync(task.sourceXmlFile, 'utf8');
  }
  return task.xml;
}

async function loadExtension(page, loaded, name) {
  if (loaded.has(name)) return;
  await page.evaluate(() => {
    const style = document.getElementById('codex-render-style');
    if (style) style.remove();
  });
  const addExtBtn = page.locator('[class*="gui_extension-button"]').first();
  await addExtBtn.click({ force: true });
  await page.waitForTimeout(1200);
  const card = page.locator('[class*="library-item_library-item"], [class*="library_library-item"]').filter({ hasText: name }).first();
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

async function exportProjectFile(page, task) {
  await page.evaluate(() => {
    const style = document.getElementById('codex-render-style');
    if (style) style.remove();
  });
  await page.waitForTimeout(200);

  const fileMenuBtn = page.locator('[class*="menu-bar_menu-bar-item"]').filter({ hasText: 'File' }).first();
  await fileMenuBtn.click();
  await page.waitForTimeout(500);

  const [download] = await Promise.all([
    page.waitForEvent('download', { timeout: 15000 }),
    page.locator('text="Save to your computer"').first().click()
  ]);

  await download.saveAs(path.join(mediaDir, `${task.id}.sb3`));
  await page.waitForTimeout(300);
}

async function renderTask(page, task) {
  const xml = getXml(task);
  const xmlPath = path.join(mediaDir, `${task.id}.xml`);
  fs.writeFileSync(xmlPath, xml, 'utf8');

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
  }, { xml, scale: task.scale });

  await page.waitForTimeout(900);
  await exportProjectFile(page, task);
  await page.waitForTimeout(400);
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

  const pngPath = path.join(mediaDir, `${task.id}.png`);
  const rawPath = path.join(mediaDir, `${task.id}.raw.png`);
  await page.screenshot({ path: pngPath, clip, omitBackground: true });
  if (task.raw) {
    fs.copyFileSync(pngPath, rawPath);
  }
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
  console.log('All targeted assets rendered.');
})().catch(err => {
  console.error(err);
  process.exit(1);
});
