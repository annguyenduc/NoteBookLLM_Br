/**
 * generate_bt7.js
 * Generator for BT7 (Multilingual Virtual Classroom with Face Sensing, Translate, TTS).
 * Target variable name: currentLesson
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT_DIR = path.resolve(__dirname, '..');

async function openExtensionLibrary(page) {
  try {
    await page.click('[class*="extension-button"]', { timeout: 10000 });
    await page.waitForTimeout(2500);
    return true;
  } catch (e) {
    console.log(`  [WARN] Could not open extension library: ${e.message.substring(0, 60)}`);
    return false;
  }
}

async function loadExtension(page, displayName) {
  console.log(`  Loading extension: ${displayName}...`);
  const opened = await openExtensionLibrary(page);
  if (!opened) return false;
  await page.waitForTimeout(2000); // Wait for cards to fully render
  try {
    const card = page.locator(`text="${displayName}"`).first();
    await card.scrollIntoViewIfNeeded({ timeout: 5000 });
    await card.click({ timeout: 8000 });
    await page.waitForTimeout(4000); // Wait after loading card
    console.log(`  [OK] Extension loaded: ${displayName}`);
    return true;
  } catch (e) {
    console.log(`  [WARN] Extension click failed for: ${displayName}. Trying fallback...`);
    try {
      await page.click(`text="${displayName}"`, { timeout: 5000 });
      await page.waitForTimeout(3000);
      return true;
    } catch (e2) {
      console.log(`  [FAIL] Failed to load extension: ${displayName}`);
      try {
        await page.locator('text="Back"').first().click({ timeout: 3000 });
        await page.waitForTimeout(1000);
      } catch (e3) {}
      return false;
    }
  }
}

(async () => {
  const xmlContent = `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_currentLesson">currentLesson</variable>
    <variable type="broadcast_msg" id="msg_day_hoc">dạy bài học</variable>
    <variable type="broadcast_msg" id="msg_hoc_lai">học lại</variable>
    <variable type="broadcast_msg" id="msg_ket_thuc">kết thúc</variable>
  </variables>

  <!-- Script 1: Event Flag Clicked -->
  <block type="event_whenflagclicked" id="bt7_start" x="40" y="40">
    <next>
      <block type="poseFace_videoToggle" id="bt7_cam_on">
        <value name="VIDEO_STATE">
          <shadow type="poseFace_menu_VIDEO_STATE">
            <field name="VIDEO_STATE">on</field>
          </shadow>
        </value>
        <next>
          <block type="sensing_askandwait" id="bt7_ask">
            <value name="QUESTION">
              <shadow type="text"><field name="TEXT">Chọn bài học (1=AI là gì / 2=Translate / 3=Teachable Machine):</field></shadow>
            </value>
            <next>
              <block type="data_setvariableto" id="bt7_set_lesson">
                <field name="VARIABLE" id="var_currentLesson" variabletype="">currentLesson</field>
                <value name="VALUE">
                  <block type="sensing_answer" id="bt7_ans1"></block>
                </value>
                <next>
                  <block type="event_broadcast" id="bt7_bc_start">
                    <value name="BROADCAST_INPUT">
                      <shadow type="event_broadcast_menu">
                        <field name="BROADCAST_OPTION" id="msg_day_hoc" variabletype="broadcast_msg">dạy bài học</field>
                      </shadow>
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

  <!-- Script 2: When Broadcast Received "dạy bài học" -->
  <block type="event_whenbroadcastreceived" id="bt7_recv_teach" x="40" y="320">
    <field name="BROADCAST_OPTION" id="msg_day_hoc" variabletype="broadcast_msg">dạy bài học</field>
    <next>
      <block type="control_if_else" id="bt7_check_1">
        <value name="CONDITION">
          <block type="operator_equals" id="bt7_eq_1">
            <value name="OPERAND1">
              <block type="data_variable" id="bt7_v_l1"><field name="VARIABLE" id="var_currentLesson" variabletype="">currentLesson</field></block>
            </value>
            <value name="OPERAND2">
              <shadow type="text"><field name="TEXT">1</field></shadow>
            </value>
          </block>
        </value>
        <statement name="SUBSTACK">
          <block type="looks_switchbackdropto" id="bt7_bg1">
            <value name="BACKDROP"><shadow type="looks_backdrop"><field name="BACKDROP">AI</field></shadow></value>
            <next>
              <block type="looks_sayforsecs" id="bt7_say_v1">
                <value name="MESSAGE"><shadow type="text"><field name="TEXT">Bài 1: AI là Trí tuệ Nhân tạo, giúp máy học và quyết định.</field></shadow></value>
                <value name="SECS"><shadow type="math_number"><field name="NUM">3</field></shadow></value>
                <next>
                  <block type="text2speech_speakAndWait" id="bt7_speak_v1">
                    <value name="WORDS"><shadow type="text"><field name="TEXT">Bài 1: AI là Trí tuệ Nhân tạo, giúp máy học và quyết định.</field></shadow></value>
                    <next>
                      <block type="looks_sayforsecs" id="bt7_say_e1">
                        <value name="MESSAGE">
                          <block type="translate_getTranslate" id="bt7_tr_e1">
                            <value name="WORDS"><shadow type="text"><field name="TEXT">Bài 1: AI là Trí tuệ Nhân tạo, giúp máy học và quyết định.</field></shadow></value>
                            <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                          </block>
                        </value>
                        <value name="SECS"><shadow type="math_number"><field name="NUM">3</field></shadow></value>
                        <next>
                          <block type="text2speech_speakAndWait" id="bt7_speak_e1">
                            <value name="WORDS">
                              <block type="translate_getTranslate" id="bt7_tr_e1_tts">
                                <value name="WORDS"><shadow type="text"><field name="TEXT">Bài 1: AI là Trí tuệ Nhân tạo, giúp máy học và quyết định.</field></shadow></value>
                                <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                              </block>
                            </value>
                            <next>
                              <block type="looks_say" id="bt7_prompt_smile1">
                                <value name="MESSAGE"><shadow type="text"><field name="TEXT">Hãy cười lên để sang bài tiếp theo nhé!</field></shadow></value>
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
        </statement>
        <statement name="SUBSTACK2">
          <block type="control_if_else" id="bt7_check_2">
            <value name="CONDITION">
              <block type="operator_equals" id="bt7_eq_2">
                <value name="OPERAND1">
                  <block type="data_variable" id="bt7_v_l2"><field name="VARIABLE" id="var_currentLesson" variabletype="">currentLesson</field></block>
                </value>
                <value name="OPERAND2">
                  <shadow type="text"><field name="TEXT">2</field></shadow>
                </value>
              </block>
            </value>
            <statement name="SUBSTACK">
              <block type="looks_switchbackdropto" id="bt7_bg2">
                <value name="BACKDROP"><shadow type="looks_backdrop"><field name="BACKDROP">Translate</field></shadow></value>
                <next>
                  <block type="looks_sayforsecs" id="bt7_say_v2">
                    <value name="MESSAGE"><shadow type="text"><field name="TEXT">Bài 2: Translate giúp chúng ta tự tin giao tiếp đa ngôn ngữ.</field></shadow></value>
                    <value name="SECS"><shadow type="math_number"><field name="NUM">3</field></shadow></value>
                    <next>
                      <block type="text2speech_speakAndWait" id="bt7_speak_v2">
                        <value name="WORDS"><shadow type="text"><field name="TEXT">Bài 2: Translate giúp chúng ta tự tin giao tiếp đa ngôn ngữ.</field></shadow></value>
                        <next>
                          <block type="looks_sayforsecs" id="bt7_say_e2">
                            <value name="MESSAGE">
                              <block type="translate_getTranslate" id="bt7_tr_e2">
                                <value name="WORDS"><shadow type="text"><field name="TEXT">Bài 2: Translate giúp chúng ta tự tin giao tiếp đa ngôn ngữ.</field></shadow></value>
                                <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                              </block>
                            </value>
                            <value name="SECS"><shadow type="math_number"><field name="NUM">3</field></shadow></value>
                            <next>
                              <block type="text2speech_speakAndWait" id="bt7_speak_e2">
                                <value name="WORDS">
                                  <block type="translate_getTranslate" id="bt7_tr_e2_tts">
                                    <value name="WORDS"><shadow type="text"><field name="TEXT">Bài 2: Translate giúp chúng ta tự tin giao tiếp đa ngôn ngữ.</field></shadow></value>
                                    <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                                  </block>
                                </value>
                                <next>
                                  <block type="looks_say" id="bt7_prompt_smile2">
                                    <value name="MESSAGE"><shadow type="text"><field name="TEXT">Hãy cười lên để sang bài tiếp theo nhé!</field></shadow></value>
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
            </statement>
            <statement name="SUBSTACK2">
              <block type="control_if_else" id="bt7_check_3">
                <value name="CONDITION">
                  <block type="operator_equals" id="bt7_eq_3">
                    <value name="OPERAND1">
                      <block type="data_variable" id="bt7_v_l3"><field name="VARIABLE" id="var_currentLesson" variabletype="">currentLesson</field></block>
                    </value>
                    <value name="OPERAND2">
                      <shadow type="text"><field name="TEXT">3</field></shadow>
                    </value>
                  </block>
                </value>
                <statement name="SUBSTACK">
                  <block type="looks_switchbackdropto" id="bt7_bg3">
                    <value name="BACKDROP"><shadow type="looks_backdrop"><field name="BACKDROP">TeachableMachine</field></shadow></value>
                    <next>
                      <block type="looks_sayforsecs" id="bt7_say_v3">
                        <value name="MESSAGE"><shadow type="text"><field name="TEXT">Bài 3: Teachable Machine giúp huấn luyện máy nhận diện hình ảnh.</field></shadow></value>
                        <value name="SECS"><shadow type="math_number"><field name="NUM">3</field></shadow></value>
                        <next>
                          <block type="text2speech_speakAndWait" id="bt7_speak_v3">
                            <value name="WORDS"><shadow type="text"><field name="TEXT">Bài 3: Teachable Machine giúp huấn luyện máy nhận diện hình ảnh.</field></shadow></value>
                            <next>
                              <block type="looks_sayforsecs" id="bt7_say_e3">
                                <value name="MESSAGE">
                                  <block type="translate_getTranslate" id="bt7_tr_e3">
                                    <value name="WORDS"><shadow type="text"><field name="TEXT">Bài 3: Teachable Machine giúp huấn luyện máy nhận diện hình ảnh.</field></shadow></value>
                                    <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                                  </block>
                                </value>
                                <value name="SECS"><shadow type="math_number"><field name="NUM">3</field></shadow></value>
                                <next>
                                  <block type="text2speech_speakAndWait" id="bt7_speak_e3">
                                    <value name="WORDS">
                                      <block type="translate_getTranslate" id="bt7_tr_e3_tts">
                                        <value name="WORDS"><shadow type="text"><field name="TEXT">Bài 3: Teachable Machine giúp huấn luyện máy nhận diện hình ảnh.</field></shadow></value>
                                        <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                                      </block>
                                    </value>
                                    <next>
                                      <block type="looks_say" id="bt7_prompt_smile3">
                                        <value name="MESSAGE"><shadow type="text"><field name="TEXT">Hãy cười lên để hoàn thành phòng học nhé!</field></shadow></value>
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
                </statement>
                <statement name="SUBSTACK2">
                  <block type="event_broadcast" id="bt7_bc_end">
                    <value name="BROADCAST_INPUT">
                      <shadow type="event_broadcast_menu">
                        <field name="BROADCAST_OPTION" id="msg_day_hoc" variabletype="broadcast_msg">dạy bài học</field>
                      </shadow>
                    </value>
                  </block>
                </statement>
              </block>
            </statement>
          </block>
        </statement>
      </block>
    </next>
  </block>

  <!-- Script 3: Event Face Sensing Smiling -->
  <block type="poseFace_affdexWhenExpression" id="bt7_face_smile" x="650" y="40">
    <value name="EXPRESSION">
      <shadow type="poseFace_menu_EXPRESSION">
        <field name="EXPRESSION">smile</field>
      </shadow>
    </value>
    <next>
      <block type="control_if_else" id="bt7_if_valid">
        <value name="CONDITION">
          <block type="operator_lt" id="bt7_less_than">
            <value name="OPERAND1">
              <block type="data_variable" id="bt7_v_l_smile"><field name="VARIABLE" id="var_currentLesson" variabletype="">currentLesson</field></block>
            </value>
            <value name="OPERAND2">
              <shadow type="text"><field name="TEXT">3</field></shadow>
            </value>
          </block>
        </value>
        <statement name="SUBSTACK">
          <block type="data_changevariableby" id="bt7_inc_lesson">
            <field name="VARIABLE" id="var_currentLesson" variabletype="">currentLesson</field>
            <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
            <next>
              <block type="event_broadcast" id="bt7_bc_next_lesson">
                <value name="BROADCAST_INPUT">
                  <shadow type="event_broadcast_menu">
                    <field name="BROADCAST_OPTION" id="msg_day_hoc" variabletype="broadcast_msg">dạy bài học</field>
                  </shadow>
                </value>
              </block>
            </next>
          </block>
        </statement>
        <statement name="SUBSTACK2">
          <block type="control_if" id="bt7_if_is_3">
            <value name="CONDITION">
              <block type="operator_equals" id="bt7_eq_is_3">
                <value name="OPERAND1">
                  <block type="data_variable" id="bt7_v_l_smile_3"><field name="VARIABLE" id="var_currentLesson" variabletype="">currentLesson</field></block>
                </value>
                <value name="OPERAND2">
                  <shadow type="text"><field name="TEXT">3</field></shadow>
                </value>
              </block>
            </value>
            <statement name="SUBSTACK">
              <block type="data_changevariableby" id="bt7_inc_lesson_end">
                <field name="VARIABLE" id="var_currentLesson" variabletype="">currentLesson</field>
                <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                <next>
                  <block type="event_broadcast" id="bt7_bc_to_end">
                    <value name="BROADCAST_INPUT">
                      <shadow type="event_broadcast_menu">
                        <field name="BROADCAST_OPTION" id="msg_ket_thuc" variabletype="broadcast_msg">kết thúc</field>
                      </shadow>
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

  <!-- Script 4: When Broadcast Received "kết thúc" -->
  <block type="event_whenbroadcastreceived" id="bt7_recv_end" x="650" y="320">
    <field name="BROADCAST_OPTION" id="msg_ket_thuc" variabletype="broadcast_msg">kết thúc</field>
    <next>
      <block type="looks_switchbackdropto" id="bt7_bg_end">
        <value name="BACKDROP"><shadow type="looks_backdrop"><field name="BACKDROP">KetThuc</field></shadow></value>
        <next>
          <block type="looks_sayforsecs" id="bt7_say_end_v">
            <value name="MESSAGE"><shadow type="text"><field name="TEXT">Chúc mừng bạn đã hoàn thành 3 bài học của phòng học ảo đa ngôn ngữ!</field></shadow></value>
            <value name="SECS"><shadow type="math_number"><field name="NUM">4</field></shadow></value>
            <next>
              <block type="text2speech_speakAndWait" id="bt7_speak_end_v">
                <value name="WORDS"><shadow type="text"><field name="TEXT">Chúc mừng bạn đã hoàn thành 3 bài học của phòng học ảo đa ngôn ngữ!</field></shadow></value>
                <next>
                  <block type="looks_sayforsecs" id="bt7_say_end_e">
                    <value name="MESSAGE">
                      <block type="translate_getTranslate" id="bt7_tr_end_e">
                        <value name="WORDS"><shadow type="text"><field name="TEXT">Chúc mừng bạn đã hoàn thành 3 bài học của phòng học ảo đa ngôn ngữ!</field></shadow></value>
                        <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                      </block>
                    </value>
                    <value name="SECS"><shadow type="math_number"><field name="NUM">4</field></shadow></value>
                    <next>
                      <block type="text2speech_speakAndWait" id="bt7_speak_end_e">
                        <value name="WORDS">
                          <block type="translate_getTranslate" id="bt7_tr_end_e_tts">
                            <value name="WORDS"><shadow type="text"><field name="TEXT">Chúc mừng bạn đã hoàn thành 3 bài học của phòng học ảo đa ngôn ngữ!</field></shadow></value>
                            <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                          </block>
                        </value>
                        <next>
                          <block type="looks_say" id="bt7_say_reset_prompt">
                            <value name="MESSAGE"><shadow type="text"><field name="TEXT">Phòng học kết thúc. Nhấn R để reset học lại nhé!</field></shadow></value>
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
    </next>
  </block>

  <!-- Script 5: When "r" Key Pressed (Reset) -->
  <block type="event_whenkeypressed" id="bt7_key_r" x="1200" y="40">
    <field name="KEY_OPTION">r</field>
    <next>
      <block type="data_setvariableto" id="bt7_reset_val">
        <field name="VARIABLE" id="var_currentLesson" variabletype="">currentLesson</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
        <next>
          <block type="event_broadcast" id="bt7_bc_reset">
            <value name="BROADCAST_INPUT">
              <shadow type="event_broadcast_menu">
                <field name="BROADCAST_OPTION" id="msg_day_hoc" variabletype="broadcast_msg">dạy bài học</field>
              </shadow>
            </value>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>`;

  console.log('Launching browser in headless mode...');
  const browser = await chromium.launch({
    headless: true,
    args: [
      '--use-fake-ui-for-media-stream',
      '--use-fake-device-for-media-stream'
    ]
  });
  
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

  console.log('Navigating to raise playground...');
  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'domcontentloaded', timeout: 90000
  });

  await page.waitForFunction(() =>
    window.Blockly &&
    typeof window.Blockly.getMainWorkspace === 'function' &&
    window.Blockly.getMainWorkspace()
  , { timeout: 90000 });

  await page.waitForTimeout(4000);

  // Load Extensions
  await loadExtension(page, 'Face Sensing');
  await loadExtension(page, 'Translate');
  await loadExtension(page, 'Text to Speech');

  console.log('Waiting 10 seconds for ML models & virtual webcam...');
  await page.waitForTimeout(10000);

  // Inject XML code
  let renderedXml;
  console.log('Injecting XML blocks...');
  try {
    renderedXml = await page.evaluate((xmlText) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const dom = B.Xml.textToDom(xmlText);
      B.Xml.domToWorkspace(dom, ws);
      ws.render();
      return new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws));
    }, xmlContent);
    console.log('[PASS] XML injected successfully.');
  } catch (err) {
    console.error('[FAIL] XML injection failed:', err.message);
    await page.screenshot({ path: path.join(OUT_DIR, 'bt7_fail.png'), fullPage: false });
    await browser.close();
    process.exit(1);
  }

  await page.waitForTimeout(3000);

  // Save screenshot
  const pngPath = path.join(OUT_DIR, 'bt7_code.raw.png');
  await page.screenshot({ path: pngPath, fullPage: true });
  console.log(`[OK] Saved screenshot to: ${pngPath}`);

  // Save XML
  const xmlPath = path.join(OUT_DIR, 'bt7_code.xml');
  fs.writeFileSync(xmlPath, renderedXml, 'utf8');
  console.log(`[OK] Saved XML to: ${xmlPath}`);

  // Download SB3
  try {
    console.log('Exporting project to SB3...');
    const fileMenu = page.locator('div').filter({ hasText: /^File$/ }).first();
    await fileMenu.click();
    await page.waitForTimeout(1000);

    const saveOption = page.locator('li').filter({ hasText: /Save to your computer/i }).first();
    
    // Set up download listener
    const downloadPromise = page.waitForEvent('download');
    await saveOption.click();
    const download = await downloadPromise;

    const sb3Path = path.join(OUT_DIR, 'bt7_code.sb3');
    await download.saveAs(sb3Path);
    console.log(`[OK] Saved SB3 to: ${sb3Path}`);
  } catch (sb3Err) {
    console.error('[FAIL] SB3 export failed:', sb3Err.message);
  }

  await browser.close();
  console.log('Generation completed.');
})();
