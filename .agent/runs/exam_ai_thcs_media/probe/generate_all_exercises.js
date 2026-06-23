/**
 * generate_all_exercises.js
 * Playwright script to generate PNG screenshots + XML for AI THCS exercises
 * Method: Real PRG AI Blocks page (https://playground.raise.mit.edu/create/) + Blockly XML injection
 * Status: PREVIEW_ONLY
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT_DIR = path.resolve(__dirname, '..');

async function generateExercise(page, exerciseId, xmlContent, description) {
  console.log(`\n[BT${exerciseId}] Generating: ${description}`);

  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'domcontentloaded',
    timeout: 90000
  });

  await page.waitForFunction(() => {
    return (
      window.Blockly &&
      typeof window.Blockly.getMainWorkspace === 'function' &&
      window.Blockly.getMainWorkspace()
    );
  }, { timeout: 90000 });

  await page.waitForTimeout(3000);

  const renderedXml = await page.evaluate((xml) => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    ws.clear();
    const dom = B.Xml.textToDom(xml);
    B.Xml.domToWorkspace(dom, ws);
    ws.render();
    return new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws));
  }, xmlContent);

  await page.waitForTimeout(1500);

  const pngPath = path.join(OUT_DIR, `bt${exerciseId}_code.raw.png`);
  await page.screenshot({ path: pngPath, fullPage: true });

  const xmlPath = path.join(OUT_DIR, `bt${exerciseId}_code.xml`);
  fs.writeFileSync(xmlPath, renderedXml, 'utf8');

  console.log(`  [OK] PNG: ${path.basename(pngPath)}`);
  console.log(`  [OK] XML: ${path.basename(xmlPath)}`);

  return { pngPath, xmlPath };
}

const exercises = [
  {
    id: 1,
    description: 'BT1 - Chatbot hoc tu vung (Translate + TTS + Loop + If)',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
  <block type="event_whenflagclicked" id="bt1_start" x="40" y="40">
    <next>
      <block type="data_setvariableto" id="bt1_set_score">
        <field name="VARIABLE">Diem</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
        <next>
          <block type="data_setvariableto" id="bt1_set_round">
            <field name="VARIABLE">Vong</field>
            <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
            <next>
              <block type="control_repeat" id="bt1_loop">
                <value name="TIMES"><shadow type="math_number"><field name="NUM">5</field></shadow></value>
                <statement name="SUBSTACK">
                  <block type="sensing_askandwait" id="bt1_ask_viet">
                    <value name="QUESTION"><shadow type="text"><field name="TEXT">Nhap mot tu tieng Viet ban muon hoc:</field></shadow></value>
                    <next>
                      <block type="translate_getTranslate" id="bt1_show_translate">
                        <value name="WORDS"><block type="sensing_answer" id="bt1_ans0"></block></value>
                        <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                        <next>
                          <block type="text2speech_speakAndWait" id="bt1_tts_speak">
                            <value name="WORDS">
                              <block type="translate_getTranslate" id="bt1_translate2">
                                <value name="WORDS"><block type="sensing_answer" id="bt1_ans1"></block></value>
                                <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                              </block>
                            </value>
                            <next>
                              <block type="sensing_askandwait" id="bt1_ask_eng">
                                <value name="QUESTION"><shadow type="text"><field name="TEXT">Go lai tu tieng Anh vua nghe:</field></shadow></value>
                                <next>
                                  <block type="control_if_else" id="bt1_check">
                                    <value name="CONDITION">
                                      <block type="operator_equals" id="bt1_compare">
                                        <value name="OPERAND1"><block type="sensing_answer" id="bt1_ans2"></block></value>
                                        <value name="OPERAND2"><block type="translate_getTranslate" id="bt1_translate3"><value name="WORDS"><block type="sensing_answer" id="bt1_ans3"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value></block></value>
                                      </block>
                                    </value>
                                    <statement name="SUBSTACK">
                                      <block type="text2speech_speakAndWait" id="bt1_tts_correct">
                                        <value name="WORDS"><shadow type="text"><field name="TEXT">Correct! +1 diem</field></shadow></value>
                                        <next>
                                          <block type="data_changevariableby" id="bt1_add_score">
                                            <field name="VARIABLE">Diem</field>
                                            <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                                          </block>
                                        </next>
                                      </block>
                                    </statement>
                                    <statement name="SUBSTACK2">
                                      <block type="text2speech_speakAndWait" id="bt1_tts_wrong">
                                        <value name="WORDS"><shadow type="text"><field name="TEXT">Sai roi! Hay thu lai.</field></shadow></value>
                                      </block>
                                    </statement>
                                  </block>
                                </next>
                              </block>
                            </next>
                          </block>
                        </next>
                      </block>
                    </next>
                  </block>
                </statement>
                <next>
                  <block type="text2speech_speakAndWait" id="bt1_tts_total">
                    <value name="WORDS">
                      <block type="operator_join" id="bt1_join">
                        <value name="STRING1"><shadow type="text"><field name="TEXT">Ban dat </field></shadow></value>
                        <value name="STRING2">
                          <block type="operator_join" id="bt1_join2">
                            <value name="STRING1"><block type="data_variable" id="bt1_score_var"><field name="VARIABLE">Diem</field></block></value>
                            <value name="STRING2"><shadow type="text"><field name="TEXT"> tren 5 diem!</field></shadow></value>
                          </block>
                        </value>
                      </block>
                    </value>
                  </block>
                </next>
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
    id: 8,
    description: 'BT8 - Tro choi bat bong Face Sensing + TTS + Countdown',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
  <block type="event_whenflagclicked" id="bt8_start_ball" x="40" y="40">
    <next>
      <block type="data_setvariableto" id="bt8_set_score">
        <field name="VARIABLE">Diem</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
        <next>
          <block type="data_setvariableto" id="bt8_set_time">
            <field name="VARIABLE">ThoiGian</field>
            <value name="VALUE"><shadow type="math_number"><field name="NUM">30</field></shadow></value>
            <next>
              <block type="motion_gotoxy" id="bt8_ball_init">
                <value name="X"><block type="operator_random" id="bt8_rand_x"><value name="FROM"><shadow type="math_number"><field name="NUM">-200</field></shadow></value><value name="TO"><shadow type="math_number"><field name="NUM">200</field></shadow></value></block></value>
                <value name="Y"><shadow type="math_number"><field name="NUM">170</field></shadow></value>
                <next>
                  <block type="control_repeat_until" id="bt8_loop">
                    <value name="CONDITION">
                      <block type="operator_equals" id="bt8_check_time">
                        <value name="OPERAND1"><block type="data_variable" id="bt8_time_var"><field name="VARIABLE">ThoiGian</field></block></value>
                        <value name="OPERAND2"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
                      </block>
                    </value>
                    <statement name="SUBSTACK">
                      <block type="motion_changeyby" id="bt8_ball_fall">
                        <value name="DY"><shadow type="math_number"><field name="NUM">-10</field></shadow></value>
                        <next>
                          <block type="control_if" id="bt8_if_touching">
                            <value name="CONDITION">
                              <block type="sensing_touchingobject" id="bt8_touch">
                                <value name="TOUCHINGOBJECTMENU"><shadow type="sensing_touchingobjectmenu"><field name="TOUCHINGOBJECTMENU">Ro</field></shadow></value>
                              </block>
                            </value>
                            <statement name="SUBSTACK">
                              <block type="data_changevariableby" id="bt8_add_score">
                                <field name="VARIABLE">Diem</field>
                                <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                                <next>
                                  <block type="text2speech_speakAndWait" id="bt8_tts_catch">
                                    <value name="WORDS"><shadow type="text"><field name="TEXT">Bat duoc!</field></shadow></value>
                                    <next>
                                      <block type="motion_gotoxy" id="bt8_ball_reset">
                                        <value name="X"><block type="operator_random" id="bt8_rand_x2"><value name="FROM"><shadow type="math_number"><field name="NUM">-200</field></shadow></value><value name="TO"><shadow type="math_number"><field name="NUM">200</field></shadow></value></block></value>
                                        <value name="Y"><shadow type="math_number"><field name="NUM">170</field></shadow></value>
                                      </block>
                                    </next>
                                  </block>
                                </next>
                              </block>
                            </statement>
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
    </next>
  </block>

  <block type="event_whenflagclicked" id="bt8_basket" x="520" y="40">
    <next>
      <block type="control_forever" id="bt8_basket_forever">
        <statement name="SUBSTACK">
          <block type="motion_setx" id="bt8_basket_x">
            <value name="X">
              <block type="faceDetection_faceX" id="bt8_face_x">
                <value name="FACE"><shadow type="faceDetection_menu_FACE"><field name="FACE">1</field></shadow></value>
              </block>
            </value>
          </block>
        </statement>
      </block>
    </next>
  </block>

  <block type="event_whenbroadcastreceived" id="bt8_result" x="40" y="500">
    <field name="BROADCAST_OPTION">KetThuc</field>
    <next>
      <block type="text2speech_speakAndWait" id="bt8_tts_result">
        <value name="WORDS">
          <block type="operator_join" id="bt8_join">
            <value name="STRING1"><shadow type="text"><field name="TEXT">Ban dat </field></shadow></value>
            <value name="STRING2">
              <block type="operator_join" id="bt8_join2">
                <value name="STRING1"><block type="data_variable" id="bt8_score_var"><field name="VARIABLE">Diem</field></block></value>
                <value name="STRING2"><shadow type="text"><field name="TEXT"> diem!</field></shadow></value>
              </block>
            </value>
          </block>
        </value>
      </block>
    </next>
  </block>
</xml>`
  }
];

(async () => {
  console.log('=== PRG AI Blocks Media Generator — AI THCS Exercises ===');
  console.log(`Output directory: ${OUT_DIR}`);

  const browser = await chromium.launch({ headless: true });
  const results = [];

  for (const ex of exercises) {
    try {
      const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });
      const res = await generateExercise(page, ex.id, ex.xml, ex.description);
      await page.close();
      results.push({ id: ex.id, status: 'OK', ...res });
    } catch (err) {
      console.error(`  [FAIL] BT${ex.id}: ${err.message}`);
      results.push({ id: ex.id, status: 'FAIL', error: err.message });
    }
  }

  await browser.close();

  console.log('\n=== SUMMARY ===');
  for (const r of results) {
    if (r.status === 'OK') {
      console.log(`  BT${r.id}: OK — ${path.basename(r.pngPath)}`);
    } else {
      console.log(`  BT${r.id}: FAIL — ${r.error}`);
    }
  }
  console.log('\nStatus: PREVIEW_ONLY — Human review required before official use.');
})();
