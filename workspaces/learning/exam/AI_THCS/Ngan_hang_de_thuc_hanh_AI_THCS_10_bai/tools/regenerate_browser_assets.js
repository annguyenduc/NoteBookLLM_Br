const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const PACKAGE_DIR = path.resolve(__dirname, '..');
const MEDIA_DIR = path.join(PACKAGE_DIR, 'Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media');
const SOURCE_DIR = 'D:/NoteBookLLM_Br/.agent/runs/exam_ai_thcs_media/probe';

const BT8_XML = `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_score">score</variable>
    <variable type="" id="var_time">time</variable>
    <variable type="broadcast_msg" id="msg_gameOver">gameOver</variable>
  </variables>

  <block type="event_whenflagclicked" id="bt8_basket_ctrl" x="40" y="40">
    <next>
      <block type="poseFace_videoToggle" id="bt8_cam_on">
        <value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value>
        <next>
          <block type="control_forever" id="bt8_basket_forever">
            <statement name="SUBSTACK">
              <block type="poseFace_affdexGoToPart" id="bt8_face_point">
                <field name="AFFDEX_POINT">0</field>
                <next>
                  <block type="motion_sety" id="bt8_fix_y">
                    <value name="Y"><shadow type="math_number"><field name="NUM">-150</field></shadow></value>
                  </block>
                </next>
              </block>
            </statement>
          </block>
        </next>
      </block>
    </next>
  </block>

  <block type="event_whenflagclicked" id="bt8_ball_start" x="460" y="40">
    <next>
      <block type="data_setvariableto" id="bt8_set_score">
        <field name="VARIABLE" id="var_score" variabletype="">score</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
        <next>
          <block type="motion_gotoxy" id="bt8_init_pos">
            <value name="X"><block type="operator_random" id="bt8_rand1"><value name="FROM"><shadow type="math_number"><field name="NUM">-200</field></shadow></value><value name="TO"><shadow type="math_number"><field name="NUM">200</field></shadow></value></block></value>
            <value name="Y"><shadow type="math_number"><field name="NUM">170</field></shadow></value>
            <next>
              <block type="control_repeat_until" id="bt8_fall_loop">
                <value name="CONDITION"><block type="operator_equals" id="bt8_time_zero"><value name="OPERAND1"><block type="data_variable" id="bt8_time_v"><field name="VARIABLE" id="var_time" variabletype="">time</field></block></value><value name="OPERAND2"><shadow type="math_number"><field name="NUM">0</field></shadow></value></block></value>
                <statement name="SUBSTACK">
                  <block type="motion_changeyby" id="bt8_fall">
                    <value name="DY"><shadow type="math_number"><field name="NUM">-8</field></shadow></value>
                    <next>
                      <block type="control_if" id="bt8_if_catch">
                        <value name="CONDITION"><block type="sensing_touchingobject" id="bt8_touch_ro"><value name="TOUCHINGOBJECTMENU"><shadow type="sensing_touchingobjectmenu"><field name="TOUCHINGOBJECTMENU">Ro</field></shadow></value></block></value>
                        <statement name="SUBSTACK">
                          <block type="data_changevariableby" id="bt8_inc_score">
                            <field name="VARIABLE" id="var_score" variabletype="">score</field>
                            <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                            <next>
                              <block type="text2speech_speakAndWait" id="bt8_tts_catch">
                                <value name="WORDS"><shadow type="text"><field name="TEXT">Bat duoc!</field></shadow></value>
                                <next><block type="motion_gotoxy" id="bt8_reset_ball"><value name="X"><block type="operator_random" id="bt8_rand2"><value name="FROM"><shadow type="math_number"><field name="NUM">-200</field></shadow></value><value name="TO"><shadow type="math_number"><field name="NUM">200</field></shadow></value></block></value><value name="Y"><shadow type="math_number"><field name="NUM">170</field></shadow></value></block></next>
                              </block>
                            </next>
                          </block>
                        </statement>
                        <next>
                          <block type="control_if" id="bt8_if_bottom">
                            <value name="CONDITION"><block type="operator_lt" id="bt8_lt_bottom"><value name="OPERAND1"><block type="motion_yposition" id="bt8_ypos"></block></value><value name="OPERAND2"><shadow type="math_number"><field name="NUM">-170</field></shadow></value></block></value>
                            <statement name="SUBSTACK"><block type="motion_gotoxy" id="bt8_reset_bottom"><value name="X"><block type="operator_random" id="bt8_rand3"><value name="FROM"><shadow type="math_number"><field name="NUM">-200</field></shadow></value><value name="TO"><shadow type="math_number"><field name="NUM">200</field></shadow></value></block></value><value name="Y"><shadow type="math_number"><field name="NUM">170</field></shadow></value></block></statement>
                            <next><block type="control_wait" id="bt8_wait_tick"><value name="DURATION"><shadow type="math_positive_number"><field name="NUM">0.05</field></shadow></value></block></next>
                          </block>
                        </next>
                      </block>
                    </next>
                  </block>
                </statement>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>

  <block type="event_whenflagclicked" id="bt8_timer_start" x="900" y="40">
    <next>
      <block type="data_setvariableto" id="bt8_set_time">
        <field name="VARIABLE" id="var_time" variabletype="">time</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">30</field></shadow></value>
        <next>
          <block type="control_repeat" id="bt8_timer_loop">
            <value name="TIMES"><shadow type="math_number"><field name="NUM">30</field></shadow></value>
            <statement name="SUBSTACK"><block type="control_wait" id="bt8_wait_1s"><value name="DURATION"><shadow type="math_positive_number"><field name="NUM">1</field></shadow></value><next><block type="data_changevariableby" id="bt8_dec_time"><field name="VARIABLE" id="var_time" variabletype="">time</field><value name="VALUE"><shadow type="math_number"><field name="NUM">-1</field></shadow></value></block></next></block></statement>
            <next><block type="event_broadcast" id="bt8_broadcast_gameover"><value name="BROADCAST_INPUT"><shadow type="event_broadcast_menu"><field name="BROADCAST_OPTION" id="msg_gameOver" variabletype="broadcast_msg">gameOver</field></shadow></value></block></next>
          </block>
        </next>
      </block>
    </next>
  </block>

  <block type="event_whenbroadcastreceived" id="bt8_on_gameover" x="900" y="360">
    <field name="BROADCAST_OPTION" id="msg_gameOver" variabletype="broadcast_msg">gameOver</field>
    <next>
      <block type="looks_sayforsecs" id="bt8_say_score">
        <value name="MESSAGE"><block type="operator_join" id="bt8_join1"><value name="STRING1"><shadow type="text"><field name="TEXT">Ban dat </field></shadow></value><value name="STRING2"><block type="operator_join" id="bt8_join2"><value name="STRING1"><block type="data_variable" id="bt8_score_v"><field name="VARIABLE" id="var_score" variabletype="">score</field></block></value><value name="STRING2"><shadow type="text"><field name="TEXT"> diem!</field></shadow></value></block></value></block></value>
        <value name="SECS"><shadow type="math_number"><field name="NUM">3</field></shadow></value>
        <next><block type="text2speech_speakAndWait" id="bt8_tts_score"><value name="WORDS"><block type="operator_join" id="bt8_join3"><value name="STRING1"><shadow type="text"><field name="TEXT">Ban dat </field></shadow></value><value name="STRING2"><block type="operator_join" id="bt8_join4"><value name="STRING1"><block type="data_variable" id="bt8_score_v2"><field name="VARIABLE" id="var_score" variabletype="">score</field></block></value><value name="STRING2"><shadow type="text"><field name="TEXT"> diem!</field></shadow></value></block></value></block></value></block></next>
      </block>
    </next>
  </block>
</xml>`;

const BT9_XML = `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_idx">costumeIndex</variable>
    <variable type="broadcast_msg" id="msg_change">changeJewelry</variable>
  </variables>

  <block type="event_whenflagclicked" id="bt9_hat_start" x="40" y="40">
    <next>
      <block type="poseBody_videoToggle" id="bt9_hat_video">
        <value name="VIDEO_STATE"><shadow type="poseBody_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value>
        <next>
          <block type="control_forever" id="bt9_hat_loop">
            <statement name="SUBSTACK">
              <block type="poseBody_goToPart" id="bt9_hat_goto">
                <value name="PART"><shadow type="poseBody_menu_PART"><field name="PART">nose</field></shadow></value>
                <next><block type="motion_changeyby" id="bt9_hat_offset"><value name="DY"><shadow type="math_number"><field name="NUM">55</field></shadow></value></block></next>
              </block>
            </statement>
          </block>
        </next>
      </block>
    </next>
  </block>

  <block type="event_whenflagclicked" id="bt9_left_ear_start" x="420" y="40">
    <next>
      <block type="control_forever" id="bt9_left_ear_loop">
        <statement name="SUBSTACK">
          <block type="poseBody_goToPart" id="bt9_left_ear_goto">
            <value name="PART"><shadow type="poseBody_menu_PART"><field name="PART">leftEar</field></shadow></value>
          </block>
        </statement>
      </block>
    </next>
  </block>

  <block type="event_whenflagclicked" id="bt9_right_ear_start" x="760" y="40">
    <next>
      <block type="control_forever" id="bt9_right_ear_loop">
        <statement name="SUBSTACK">
          <block type="poseBody_goToPart" id="bt9_right_ear_goto">
            <value name="PART"><shadow type="poseBody_menu_PART"><field name="PART">rightEar</field></shadow></value>
          </block>
        </statement>
      </block>
    </next>
  </block>

  <block type="event_whenflagclicked" id="bt9_glasses_start" x="1100" y="40">
    <next>
      <block type="control_forever" id="bt9_glasses_loop">
        <statement name="SUBSTACK">
          <block type="poseBody_goToPart" id="bt9_glasses_goto">
            <value name="PART"><shadow type="poseBody_menu_PART"><field name="PART">nose</field></shadow></value>
          </block>
        </statement>
      </block>
    </next>
  </block>

  <block type="event_whenbroadcastreceived" id="bt9_hat_change" x="40" y="300">
    <field name="BROADCAST_OPTION" id="msg_change" variabletype="broadcast_msg">changeJewelry</field>
    <next><block type="looks_switchcostumeto" id="bt9_hat_costume"><value name="COSTUME"><block type="data_variable" id="bt9_hat_idx"><field name="VARIABLE" id="var_idx" variabletype="">costumeIndex</field></block></value></block></next>
  </block>

  <block type="event_whenbroadcastreceived" id="bt9_left_ear_change" x="420" y="300">
    <field name="BROADCAST_OPTION" id="msg_change" variabletype="broadcast_msg">changeJewelry</field>
    <next><block type="looks_switchcostumeto" id="bt9_left_ear_costume"><value name="COSTUME"><block type="data_variable" id="bt9_left_idx"><field name="VARIABLE" id="var_idx" variabletype="">costumeIndex</field></block></value></block></next>
  </block>

  <block type="event_whenbroadcastreceived" id="bt9_right_ear_change" x="760" y="300">
    <field name="BROADCAST_OPTION" id="msg_change" variabletype="broadcast_msg">changeJewelry</field>
    <next><block type="looks_switchcostumeto" id="bt9_right_ear_costume"><value name="COSTUME"><block type="data_variable" id="bt9_right_idx"><field name="VARIABLE" id="var_idx" variabletype="">costumeIndex</field></block></value></block></next>
  </block>

  <block type="event_whenbroadcastreceived" id="bt9_glasses_change" x="1100" y="300">
    <field name="BROADCAST_OPTION" id="msg_change" variabletype="broadcast_msg">changeJewelry</field>
    <next><block type="looks_switchcostumeto" id="bt9_glasses_costume"><value name="COSTUME"><block type="data_variable" id="bt9_glasses_idx"><field name="VARIABLE" id="var_idx" variabletype="">costumeIndex</field></block></value></block></next>
  </block>

  <block type="event_whenkeypressed" id="bt9_space" x="40" y="520">
    <field name="KEY_OPTION">space</field>
    <next>
      <block type="data_setvariableto" id="bt9_set_idx">
        <field name="VARIABLE" id="var_idx" variabletype="">costumeIndex</field>
        <value name="VALUE"><block type="operator_random" id="bt9_rand"><value name="FROM"><shadow type="math_number"><field name="NUM">1</field></shadow></value><value name="TO"><shadow type="math_number"><field name="NUM">3</field></shadow></value></block></value>
        <next>
          <block type="event_broadcast" id="bt9_bc_change">
            <value name="BROADCAST_INPUT"><shadow type="event_broadcast_menu"><field name="BROADCAST_OPTION" id="msg_change" variabletype="broadcast_msg">changeJewelry</field></shadow></value>
            <next>
              <block type="control_wait" id="bt9_wait">
                <value name="DURATION"><shadow type="math_positive_number"><field name="NUM">0.5</field></shadow></value>
                <next>
                  <block type="looks_sayforsecs" id="bt9_say">
                    <value name="MESSAGE"><shadow type="text"><field name="TEXT">Bo trang suc moi that long lay!</field></shadow></value>
                    <value name="SECS"><shadow type="math_number"><field name="NUM">2</field></shadow></value>
                    <next>
                      <block type="text2speech_speakAndWait" id="bt9_tts">
                        <value name="WORDS"><block type="translate_getTranslate" id="bt9_translate"><value name="WORDS"><shadow type="text"><field name="TEXT">Bo trang suc moi that long lay!</field></shadow></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value></block></value>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>`;

function extractXmlFromSource(fileName, constName) {
  const source = fs.readFileSync(path.join(SOURCE_DIR, fileName), 'utf8');
  const marker = constName ? `const ${constName} = \`` : 'const xmlContent = `';
  const start = source.indexOf(marker);
  if (start < 0) throw new Error(`Cannot find ${marker} in ${fileName}`);
  const bodyStart = start + marker.length;
  const end = source.indexOf('`;', bodyStart);
  if (end < 0) throw new Error(`Cannot find XML end in ${fileName}`);
  return source.slice(bodyStart, end);
}

async function openExtensionLibrary(page) {
  await page.click('[class*="extension-button"]', { timeout: 12000 });
  await page.waitForTimeout(1200);
}

async function loadExtension(page, name) {
  await openExtensionLibrary(page);
  let card = page.locator('[class*="library-item"]').filter({ hasText: name }).first();
  if (!(await card.count())) {
    card = page.locator(`text="${name}"`).first();
  }
  await card.scrollIntoViewIfNeeded({ timeout: 6000 });
  await card.click({ timeout: 8000, force: true });
  await page.waitForTimeout(3000);
}

async function generate(browser, item) {
  const page = await browser.newPage({ viewport: { width: 1500, height: 950 }, acceptDownloads: true });
  try {
    await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'domcontentloaded', timeout: 90000 });
    await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace && window.Blockly.getMainWorkspace(), { timeout: 90000 });
    await page.waitForTimeout(2500);
    for (const ext of item.extensions) await loadExtension(page, ext);
    await page.waitForTimeout(item.modelWaitMs || 2500);

    const renderedXml = await page.evaluate((xmlText) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const dom = B.Xml.textToDom(xmlText);
      B.Xml.domToWorkspace(dom, ws);
      ws.render();
      return new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws));
    }, item.xml);

    fs.writeFileSync(path.join(MEDIA_DIR, `bt${item.id}_code.xml`), renderedXml, 'utf8');
    await page.screenshot({ path: path.join(MEDIA_DIR, `bt${item.id}_code.raw.png`), fullPage: true });

    const downloadPromise = page.waitForEvent('download', { timeout: 30000 });
    await page.locator('div').filter({ hasText: /^File$/ }).first().click({ timeout: 10000 });
    await page.waitForTimeout(500);
    await page.locator('li').filter({ hasText: /Save to your computer/i }).first().click({ timeout: 10000 });
    const download = await downloadPromise;
    await download.saveAs(path.join(MEDIA_DIR, `bt${item.id}_code.sb3`));
    console.log(`BT${item.id}: regenerated`);
  } finally {
    await page.close();
  }
}

(async () => {
  let items = [
    { id: 1, extensions: ['Text to Speech', 'Translate'], xml: extractXmlFromSource('generate_bt1.js', 'BT1_XML'), modelWaitMs: 2500 },
    { id: 5, extensions: ['Face Sensing', 'Translate', 'Text to Speech'], xml: extractXmlFromSource('generate_bt5.js'), modelWaitMs: 8000 },
    { id: 7, extensions: ['Text to Speech', 'Translate', 'Face Sensing'], xml: extractXmlFromSource('generate_bt7.js'), modelWaitMs: 8000 },
    { id: 8, extensions: ['Face Sensing', 'Text to Speech'], xml: BT8_XML, modelWaitMs: 8000 },
    { id: 9, extensions: ['Body Sensing', 'Translate', 'Text to Speech'], xml: BT9_XML, modelWaitMs: 8000 },
    { id: 10, extensions: ['Teachable Machine', 'Text to Speech', 'Translate'], xml: extractXmlFromSource('generate_bt10.js', 'BT10_XML'), modelWaitMs: 8000 }
  ];
  const requested = new Set(process.argv.slice(2).map((value) => Number(value)).filter(Boolean));
  if (requested.size) {
    items = items.filter((item) => requested.has(item.id));
  }
  fs.mkdirSync(MEDIA_DIR, { recursive: true });
  const browser = await chromium.launch({
    channel: 'msedge',
    headless: true,
    args: ['--use-fake-ui-for-media-stream', '--use-fake-device-for-media-stream']
  });
  try {
    for (const item of items) await generate(browser, item);
  } finally {
    await browser.close();
  }
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
