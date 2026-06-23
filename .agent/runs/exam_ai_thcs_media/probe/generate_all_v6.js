/**
 * generate_all_v6.js
 * Batch generator with robust initialization waits for camera extensions.
 * Status: PREVIEW_ONLY
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT_DIR = path.resolve(__dirname, '..');

async function openExtensionLibrary(page) {
  try {
    await page.click('[class*="extension-button"]', { timeout: 8000 });
    await page.waitForTimeout(2000);
    return true;
  } catch (e) {
    console.log(`  [WARN] Could not open extension library: ${e.message.substring(0, 60)}`);
    return false;
  }
}

async function loadExtension(page, displayName) {
  const opened = await openExtensionLibrary(page);
  if (!opened) return false;
  await page.waitForTimeout(1500); // Wait for cards to fully render
  try {
    const card = page.locator(`text="${displayName}"`).first();
    await card.scrollIntoViewIfNeeded({ timeout: 3000 });
    await card.click({ timeout: 5000 });
    await page.waitForTimeout(3000); // Wait after loading card
    console.log(`  [OK] Extension loaded: ${displayName}`);
    return true;
  } catch (e) {
    console.log(`  [WARN] Extension click failed for: ${displayName}. Trying fallback...`);
    // Try click raw text
    try {
      await page.click(`text="${displayName}"`, { timeout: 3000 });
      await page.waitForTimeout(2000);
      return true;
    } catch (e2) {
      console.log(`  [FAIL] Failed to load extension: ${displayName}`);
      // Try back button to close modal
      try { await page.locator('text="Back"').first().click({ timeout: 2000 }); await page.waitForTimeout(500); } catch (e3) {}
      return false;
    }
  }
}

async function generateExercise(browser, ex) {
  console.log(`\n[BT${ex.id}] ${ex.description}`);
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'domcontentloaded', timeout: 90000
  });

  await page.waitForFunction(() =>
    window.Blockly &&
    typeof window.Blockly.getMainWorkspace === 'function' &&
    window.Blockly.getMainWorkspace()
  , { timeout: 90000 });

  await page.waitForTimeout(3000);

  // Load required extensions
  for (const extName of (ex.extensions || [])) {
    await loadExtension(page, extName);
  }

  // Camera check
  const hasCameraExt = (ex.extensions || []).some(ext =>
    ext.includes('Sensing') || ext.includes('Machine')
  );

  if (hasCameraExt) {
    console.log('  [INFO] Camera/ML extension detected. Waiting 7 seconds for model & virtual webcam setup...');
    await page.waitForTimeout(7000);
  } else {
    await page.waitForTimeout(2000);
  }

  // Inject XML
  let renderedXml;
  try {
    renderedXml = await page.evaluate((xml) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const dom = B.Xml.textToDom(xml);
      B.Xml.domToWorkspace(dom, ws);
      ws.render();
      return new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws));
    }, ex.xml);
  } catch (err) {
    await page.screenshot({ path: path.join(OUT_DIR, `bt${ex.id}_fail.png`), fullPage: false });
    await page.close();
    throw new Error(`XML injection failed: ${err.message.substring(0, 200)}`);
  }

  await page.waitForTimeout(2000);

  const pngPath = path.join(OUT_DIR, `bt${ex.id}_code.raw.png`);
  await page.screenshot({ path: pngPath, fullPage: true });

  const xmlPath = path.join(OUT_DIR, `bt${ex.id}_code.xml`);
  fs.writeFileSync(xmlPath, renderedXml, 'utf8');

  console.log(`  [OK] bt${ex.id}_code.raw.png + bt${ex.id}_code.xml saved`);
  await page.close();
  return { pngPath, xmlPath };
}

// ============================================================
// EXERCISES 2-10 DEFINITIONS (WITH EXPLICIT VARIABLES)
// ============================================================

const exercises = [
  // BT2: Truyen tuong tac da ngon ngu - Translate + TTS + Backdrop + Broadcast
  {
    id: 2,
    description: 'BT2 - Truyen tuong tac da ngon ngu (Translate + TTS + Backdrop + Broadcast)',
    extensions: ['Text to Speech', 'Translate'],
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_lang" islocal="false" iscloud="false">NgonNgu</variable>
    <variable type="broadcast_msg" id="msg_canh2" islocal="false" iscloud="false">Canh 2</variable>
  </variables>
  <block type="event_whenflagclicked" id="bt2_start" x="40" y="40">
    <next>
      <block type="sensing_askandwait" id="bt2_ask_lang">
        <value name="QUESTION"><shadow type="text"><field name="TEXT">Chon ngon ngu: 1-Tieng Viet / 2-Tieng Anh</field></shadow></value>
        <next>
          <block type="data_setvariableto" id="bt2_set_lang">
            <field name="VARIABLE" id="var_lang" variabletype="">NgonNgu</field>
            <value name="VALUE"><block type="sensing_answer" id="bt2_ans_lang"></block></value>
            <next>
              <block type="looks_switchbackdropto" id="bt2_backdrop1">
                <value name="BACKDROP"><shadow type="looks_backdrop"><field name="BACKDROP">Canh 1</field></shadow></value>
                <next>
                  <block type="control_if_else" id="bt2_if_lang1">
                    <value name="CONDITION">
                      <block type="operator_equals" id="bt2_eq1">
                        <value name="OPERAND1"><block type="data_variable" id="bt2_lang_var"><field name="VARIABLE" id="var_lang" variabletype="">NgonNgu</field></block></value>
                        <value name="OPERAND2"><shadow type="text"><field name="TEXT">2</field></shadow></value>
                      </block>
                    </value>
                    <statement name="SUBSTACK">
                      <block type="text2speech_speakAndWait" id="bt2_tts_eng1">
                        <value name="WORDS">
                          <block type="translate_getTranslate" id="bt2_trans1">
                            <value name="WORDS"><shadow type="text"><field name="TEXT">Ngay xua ngay xua, co mot chu meo nho...</field></shadow></value>
                            <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                          </block>
                        </value>
                      </block>
                    </statement>
                    <statement name="SUBSTACK2">
                      <block type="text2speech_speakAndWait" id="bt2_tts_viet1">
                        <value name="WORDS"><shadow type="text"><field name="TEXT">Ngay xua ngay xua, co mot chu meo nho...</field></shadow></value>
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

  <block type="event_whenbroadcastreceived" id="bt2_canh2" x="520" y="40">
    <field name="BROADCAST_OPTION" id="msg_canh2" variabletype="broadcast_msg">Canh 2</field>
    <next>
      <block type="looks_switchbackdropto" id="bt2_backdrop2">
        <value name="BACKDROP"><shadow type="looks_backdrop"><field name="BACKDROP">Canh 2</field></shadow></value>
        <next>
          <block type="control_if_else" id="bt2_if_lang2">
            <value name="CONDITION">
              <block type="operator_equals" id="bt2_eq2">
                <value name="OPERAND1"><block type="data_variable" id="bt2_lang_var2"><field name="VARIABLE" id="var_lang" variabletype="">NgonNgu</field></block></value>
                <value name="OPERAND2"><shadow type="text"><field name="TEXT">2</field></shadow></value>
              </block>
            </value>
            <statement name="SUBSTACK">
              <block type="text2speech_speakAndWait" id="bt2_tts_eng2">
                <value name="WORDS">
                  <block type="translate_getTranslate" id="bt2_trans2">
                    <value name="WORDS"><shadow type="text"><field name="TEXT">Chu meo gap mot ban moi la chu cho...</field></shadow></value>
                    <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                  </block>
                </value>
              </block>
            </statement>
            <statement name="SUBSTACK2">
              <block type="text2speech_speakAndWait" id="bt2_tts_viet2">
                <value name="WORDS"><shadow type="text"><field name="TEXT">Chu meo gap mot ban moi la chu cho...</field></shadow></value>
              </block>
            </statement>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>`
  },

  // BT3: Tro ly toan hoc - TTS + 4 phep tinh + If + List
  {
    id: 3,
    description: 'BT3 - Tro ly toan hoc AI (TTS + 4 phep tinh + If + chia 0 + List)',
    extensions: ['Text to Speech'],
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_so1">So1</variable>
    <variable type="" id="var_so2">So2</variable>
    <variable type="" id="var_ketqua">KetQua</variable>
    <variable type="list" id="list_lichsu">LichSu</variable>
  </variables>
  <block type="event_whenflagclicked" id="bt3_start" x="40" y="40">
    <next>
      <block type="data_deletealloflist" id="bt3_clear">
        <field name="LIST" id="list_lichsu" variabletype="list">LichSu</field>
        <next>
          <block type="sensing_askandwait" id="bt3_ask_s1">
            <value name="QUESTION"><shadow type="text"><field name="TEXT">Nhap so thu nhat:</field></shadow></value>
            <next>
              <block type="data_setvariableto" id="bt3_set_s1">
                <field name="VARIABLE" id="var_so1" variabletype="">So1</field>
                <value name="VALUE"><block type="sensing_answer" id="bt3_ans1"></block></value>
                <next>
                  <block type="sensing_askandwait" id="bt3_ask_s2">
                    <value name="QUESTION"><shadow type="text"><field name="TEXT">Nhap so thu hai:</field></shadow></value>
                    <next>
                      <block type="data_setvariableto" id="bt3_set_s2">
                        <field name="VARIABLE" id="var_so2" variabletype="">So2</field>
                        <value name="VALUE"><block type="sensing_answer" id="bt3_ans2"></block></value>
                        <next>
                          <block type="sensing_askandwait" id="bt3_ask_op">
                            <value name="QUESTION"><shadow type="text"><field name="TEXT">Phep tinh (1=Cong 2=Tru 3=Nhan 4=Chia):</field></shadow></value>
                            <next>
                              <block type="control_if" id="bt3_if_cong">
                                <value name="CONDITION">
                                  <block type="operator_equals" id="bt3_eq_cong">
                                    <value name="OPERAND1"><block type="sensing_answer" id="bt3_op_ans"></block></value>
                                    <value name="OPERAND2"><shadow type="text"><field name="TEXT">1</field></shadow></value>
                                  </block>
                                </value>
                                <statement name="SUBSTACK">
                                  <block type="data_setvariableto" id="bt3_calc_cong">
                                    <field name="VARIABLE" id="var_ketqua" variabletype="">KetQua</field>
                                    <value name="VALUE">
                                      <block type="operator_add" id="bt3_add">
                                        <value name="NUM1"><block type="data_variable" id="bt3_s1a"><field name="VARIABLE" id="var_so1" variabletype="">So1</field></block></value>
                                        <value name="NUM2"><block type="data_variable" id="bt3_s2a"><field name="VARIABLE" id="var_so2" variabletype="">So2</field></block></value>
                                      </block>
                                    </value>
                                    <next>
                                      <block type="text2speech_speakAndWait" id="bt3_tts_cong">
                                        <value name="WORDS">
                                          <block type="operator_join" id="bt3_j1">
                                            <value name="STRING1"><block type="data_variable" id="bt3_s1j"><field name="VARIABLE" id="var_so1" variabletype="">So1</field></block></value>
                                            <value name="STRING2">
                                              <block type="operator_join" id="bt3_j2">
                                                <value name="STRING1"><shadow type="text"><field name="TEXT"> cong </field></shadow></value>
                                                <value name="STRING2">
                                                  <block type="operator_join" id="bt3_j3">
                                                    <value name="STRING1"><block type="data_variable" id="bt3_s2j"><field name="VARIABLE" id="var_so2" variabletype="">So2</field></block></value>
                                                    <value name="STRING2">
                                                      <block type="operator_join" id="bt3_j4">
                                                        <value name="STRING1"><shadow type="text"><field name="TEXT"> bang </field></shadow></value>
                                                        <value name="STRING2"><block type="data_variable" id="bt3_kq_j"><field name="VARIABLE" id="var_ketqua" variabletype="">KetQua</field></block></value>
                                                      </block>
                                                    </value>
                                                  </block>
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
    </next>
  </block>
</xml>`
  },

  // BT4: He thong hoi dap - TTS + Translate + 2 List + Broadcast
  {
    id: 4,
    description: 'BT4 - He thong quiz 5 cau (TTS + Translate + 2 List + Broadcast)',
    extensions: ['Text to Speech', 'Translate'],
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_diem">Diem</variable>
    <variable type="" id="var_vong">Vong</variable>
    <variable type="list" id="list_cauhoi">CauHoi</variable>
    <variable type="list" id="list_dapandung">DapAnDung</variable>
    <variable type="broadcast_msg" id="msg_ketqua">KetQua</variable>
  </variables>
  <block type="event_whenflagclicked" id="bt4_start" x="40" y="40">
    <next>
      <block type="data_setvariableto" id="bt4_set_diem">
        <field name="VARIABLE" id="var_diem" variabletype="">Diem</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
        <next>
          <block type="data_setvariableto" id="bt4_set_vong">
            <field name="VARIABLE" id="var_vong" variabletype="">Vong</field>
            <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
            <next>
              <block type="data_addtolist" id="bt4_add_q1">
                <field name="LIST" id="list_cauhoi" variabletype="list">CauHoi</field>
                <value name="ITEM"><shadow type="text"><field name="TEXT">Translate la gi?</field></shadow></value>
                <next>
                  <block type="data_addtolist" id="bt4_add_a1">
                    <field name="LIST" id="list_dapandung" variabletype="list">DapAnDung</field>
                    <value name="ITEM"><shadow type="text"><field name="TEXT">Cong cu dich ngon ngu</field></shadow></value>
                    <next>
                      <block type="control_repeat_until" id="bt4_loop">
                        <value name="CONDITION">
                          <block type="operator_gt" id="bt4_check_vong">
                            <value name="OPERAND1"><block type="data_variable" id="bt4_vong_var"><field name="VARIABLE" id="var_vong" variabletype="">Vong</field></block></value>
                            <value name="OPERAND2"><shadow type="math_number"><field name="NUM">5</field></shadow></value>
                          </block>
                        </value>
                        <statement name="SUBSTACK">
                          <block type="text2speech_speakAndWait" id="bt4_tts_q">
                            <value name="WORDS">
                              <block type="data_itemoflist" id="bt4_get_q">
                                <value name="INDEX"><block type="data_variable" id="bt4_vong_idx"><field name="VARIABLE" id="var_vong" variabletype="">Vong</field></block></value>
                                <field name="LIST" id="list_cauhoi" variabletype="list">CauHoi</field>
                              </block>
                            </value>
                            <next>
                              <block type="sensing_askandwait" id="bt4_ask">
                                <value name="QUESTION">
                                  <block type="data_itemoflist" id="bt4_get_q2">
                                    <value name="INDEX"><block type="data_variable" id="bt4_vong_idx2"><field name="VARIABLE" id="var_vong" variabletype="">Vong</field></block></value>
                                    <field name="LIST" id="list_cauhoi" variabletype="list">CauHoi</field>
                                  </block>
                                </value>
                                <next>
                                  <block type="control_if_else" id="bt4_check">
                                    <value name="CONDITION">
                                      <block type="operator_equals" id="bt4_eq">
                                        <value name="OPERAND1"><block type="sensing_answer" id="bt4_ans"></block></value>
                                        <value name="OPERAND2">
                                          <block type="data_itemoflist" id="bt4_get_a">
                                            <value name="INDEX"><block type="data_variable" id="bt4_vong_idx3"><field name="VARIABLE" id="var_vong" variabletype="">Vong</field></block></value>
                                            <field name="LIST" id="list_dapandung" variabletype="list">DapAnDung</field>
                                          </block>
                                        </value>
                                      </block>
                                    </value>
                                    <statement name="SUBSTACK">
                                      <block type="text2speech_speakAndWait" id="bt4_tts_correct">
                                        <value name="WORDS"><shadow type="text"><field name="TEXT">Chinh xac! +1 diem</field></shadow></value>
                                        <next>
                                          <block type="data_changevariableby" id="bt4_inc_diem">
                                            <field name="VARIABLE" id="var_diem" variabletype="">Diem</field>
                                            <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                                          </block>
                                        </next>
                                      </block>
                                    </statement>
                                    <statement name="SUBSTACK2">
                                      <block type="text2speech_speakAndWait" id="bt4_tts_wrong">
                                        <value name="WORDS"><shadow type="text"><field name="TEXT">Sai! Dap an dung la...</field></shadow></value>
                                      </block>
                                    </statement>
                                  </block>
                                </next>
                              </block>
                            </next>
                          </block>
                        </statement>
                        <next>
                          <block type="data_changevariableby" id="bt4_inc_vong">
                            <field name="VARIABLE" id="var_vong" variabletype="">Vong</field>
                            <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
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

  <block type="event_whenbroadcastreceived" id="bt4_kq_sprite" x="520" y="40">
    <field name="BROADCAST_OPTION" id="msg_ketqua" variabletype="broadcast_msg">KetQua</field>
    <next>
      <block type="text2speech_speakAndWait" id="bt4_tts_kq">
        <value name="WORDS">
          <block type="operator_join" id="bt4_join_kq">
            <value name="STRING1"><shadow type="text"><field name="TEXT">Ban dat </field></shadow></value>
            <value name="STRING2">
              <block type="operator_join" id="bt4_join_kq2">
                <value name="STRING1"><block type="data_variable" id="bt4_diem_j"><field name="VARIABLE" id="var_diem" variabletype="">Diem</field></block></value>
                <value name="STRING2"><shadow type="text"><field name="TEXT"> tren 5 diem!</field></shadow></value>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="text2speech_speakAndWait" id="bt4_tts_eng">
            <value name="WORDS">
              <block type="translate_getTranslate" id="bt4_trans_kq">
                <value name="WORDS">
                  <block type="operator_join" id="bt4_join_eng">
                    <value name="STRING1"><shadow type="text"><field name="TEXT">Ban dat </field></shadow></value>
                    <value name="STRING2">
                      <block type="operator_join" id="bt4_join_eng2">
                        <value name="STRING1"><block type="data_variable" id="bt4_diem_e"><field name="VARIABLE" id="var_diem" variabletype="">Diem</field></block></value>
                        <value name="STRING2"><shadow type="text"><field name="TEXT"> tren 5 diem!</field></shadow></value>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
              </block>
            </value>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>`
  },

  // BT5: Nhan vat phan ung cam xuc - Face Sensing + Translate
  {
    id: 5,
    description: 'BT5 - Nhan vat cam xuc (Face Sensing + Translate + Costume/Backdrop)',
    extensions: ['Face Sensing', 'Translate'],
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
  </variables>
  <block type="event_whenflagclicked" id="bt5_start" x="40" y="40">
    <next>
      <block type="videoSensing_videoToggle" id="bt5_cam_on">
        <value name="VIDEO_STATE"><shadow type="videoSensing_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value>
        <next>
          <block type="looks_switchcostumeto" id="bt5_costume_wait">
            <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">cho</field></shadow></value>
            <next>
              <block type="looks_say" id="bt5_say_wait">
                <value name="MESSAGE"><shadow type="text"><field name="TEXT">Nhin vao camera nao!</field></shadow></value>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>

  <block type="faceDetection_whenFace" id="bt5_face_vui" x="40" y="250">
    <value name="FACE_EXPRESSION"><shadow type="faceDetection_menu_FACE_EXPRESSION"><field name="FACE_EXPRESSION">smiling</field></shadow></value>
    <next>
      <block type="looks_switchcostumeto" id="bt5_costume_vui">
        <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">vui</field></shadow></value>
        <next>
          <block type="looks_switchbackdropto" id="bt5_backdrop_vui">
            <value name="BACKDROP"><shadow type="looks_backdrop"><field name="BACKDROP">vui</field></shadow></value>
            <next>
              <block type="looks_sayforsecs" id="bt5_say_vui">
                <value name="MESSAGE"><shadow type="text"><field name="TEXT">Ban dang rat vui ve!</field></shadow></value>
                <value name="SECS"><shadow type="math_number"><field name="NUM">2</field></shadow></value>
                <next>
                  <block type="looks_sayforsecs" id="bt5_say_vui_eng">
                    <value name="MESSAGE">
                      <block type="translate_getTranslate" id="bt5_trans_vui">
                        <value name="WORDS"><shadow type="text"><field name="TEXT">Ban dang rat vui ve!</field></shadow></value>
                        <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                      </block>
                    </value>
                    <value name="SECS"><shadow type="math_number"><field name="NUM">2</field></shadow></value>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>

  <block type="faceDetection_whenFace" id="bt5_face_sad" x="520" y="250">
    <value name="FACE_EXPRESSION"><shadow type="faceDetection_menu_FACE_EXPRESSION"><field name="FACE_EXPRESSION">sad</field></shadow></value>
    <next>
      <block type="looks_switchcostumeto" id="bt5_costume_sad">
        <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">buon</field></shadow></value>
        <next>
          <block type="looks_sayforsecs" id="bt5_say_sad">
            <value name="MESSAGE"><shadow type="text"><field name="TEXT">Co chuyen gi buon vay?</field></shadow></value>
            <value name="SECS"><shadow type="math_number"><field name="NUM">2</field></shadow></value>
            <next>
              <block type="looks_sayforsecs" id="bt5_say_sad_eng">
                <value name="MESSAGE">
                  <block type="translate_getTranslate" id="bt5_trans_sad">
                    <value name="WORDS"><shadow type="text"><field name="TEXT">Co chuyen gi buon vay?</field></shadow></value>
                    <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                  </block>
                </value>
                <value name="SECS"><shadow type="math_number"><field name="NUM">2</field></shadow></value>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>`
  },

  // BT6: The duc AI - Body Sensing + TTS
  {
    id: 6,
    description: 'BT6 - The duc AI Body Sensing (Body Sensing + TTS + dem dong tac)',
    extensions: ['Body Sensing', 'Text to Speech'],
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_solan">SoLan</variable>
    <variable type="" id="var_dadem">DaDem</variable>
  </variables>
  <block type="event_whenflagclicked" id="bt6_start" x="40" y="40">
    <next>
      <block type="data_setvariableto" id="bt6_set_soLan">
        <field name="VARIABLE" id="var_solan" variabletype="">SoLan</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
        <next>
          <block type="data_setvariableto" id="bt6_set_daDem">
            <field name="VARIABLE" id="var_dadem" variabletype="">DaDem</field>
            <value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
            <next>
              <block type="videoSensing_videoToggle" id="bt6_cam_on">
                <value name="VIDEO_STATE"><shadow type="videoSensing_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value>
                <next>
                  <block type="looks_switchcostumeto" id="bt6_costume_tap">
                    <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">dang tap</field></shadow></value>
                    <next>
                      <block type="control_forever" id="bt6_forever">
                        <statement name="SUBSTACK">
                          <block type="motion_goto" id="bt6_goto_wrist">
                            <value name="TO">
                              <shadow type="motion_menu_goto_menu"><field name="TO">_mouse_</field></shadow>
                            </value>
                            <next>
                              <block type="control_if" id="bt6_if_raise">
                                <value name="CONDITION">
                                  <block type="operator_and" id="bt6_and_cond">
                                    <value name="OPERAND1">
                                      <block type="operator_lt" id="bt6_lt_y">
                                        <value name="OPERAND1"><block type="motion_yposition" id="bt6_y_pos"></block></value>
                                        <value name="OPERAND2"><shadow type="math_number"><field name="NUM">100</field></shadow></value>
                                      </block>
                                    </value>
                                    <value name="OPERAND2">
                                      <block type="operator_equals" id="bt6_eq_dem">
                                        <value name="OPERAND1"><block type="data_variable" id="bt6_daDem_v"><field name="VARIABLE" id="var_dadem" variabletype="">DaDem</field></block></value>
                                        <value name="OPERAND2"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
                                      </block>
                                    </value>
                                  </block>
                                </value>
                                <statement name="SUBSTACK">
                                  <block type="data_changevariableby" id="bt6_inc_soLan">
                                    <field name="VARIABLE" id="var_solan" variabletype="">SoLan</field>
                                    <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                                    <next>
                                      <block type="data_setvariableto" id="bt6_set_dem1">
                                        <field name="VARIABLE" id="var_dadem" variabletype="">DaDem</field>
                                        <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                                        <next>
                                          <block type="text2speech_speakAndWait" id="bt6_tts_count">
                                            <value name="WORDS"><block type="data_variable" id="bt6_soLan_v"><field name="VARIABLE" id="var_solan" variabletype="">SoLan</field></block></value>
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
    </next>
  </block>

  <block type="event_whenkeypressed" id="bt6_reset" x="520" y="40">
    <field name="KEY_OPTION">space</field>
    <next>
      <block type="data_setvariableto" id="bt6_reset_soLan">
        <field name="VARIABLE" id="var_solan" variabletype="">SoLan</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
        <next>
          <block type="data_setvariableto" id="bt6_reset_daDem">
            <field name="VARIABLE" id="var_dadem" variabletype="">DaDem</field>
            <value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
            <next>
              <block type="looks_switchcostumeto" id="bt6_reset_costume">
                <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">dang tap</field></shadow></value>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>`
  },

  // BT7: Phong hoc ao - Translate + TTS + Face Sensing
  {
    id: 7,
    description: 'BT7 - Phong hoc ao da ngon ngu (Translate + TTS + Face Sensing chuyen bai)',
    extensions: ['Text to Speech', 'Translate', 'Face Sensing'],
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="broadcast_msg" id="msg_bai1">Bai 1</variable>
    <variable type="broadcast_msg" id="msg_bai2">Bai 2</variable>
  </variables>
  <block type="event_whenflagclicked" id="bt7_start" x="40" y="40">
    <next>
      <block type="sensing_askandwait" id="bt7_ask">
        <value name="QUESTION"><shadow type="text"><field name="TEXT">Chon chu de (1=AI la gi / 2=Translate / 3=Teachable Machine):</field></shadow></value>
        <next>
          <block type="control_if" id="bt7_if_b1">
            <value name="CONDITION">
              <block type="operator_equals" id="bt7_eq1">
                <value name="OPERAND1"><block type="sensing_answer" id="bt7_ans1"></block></value>
                <value name="OPERAND2"><shadow type="text"><field name="TEXT">1</field></shadow></value>
              </block>
            </value>
            <statement name="SUBSTACK">
              <block type="event_broadcast" id="bt7_bc1">
                <value name="BROADCAST_INPUT">
                  <shadow type="event_broadcast_menu">
                    <field name="BROADCAST_OPTION" id="msg_bai1" variabletype="broadcast_msg">Bai 1</field>
                  </shadow>
                </value>
              </block>
            </statement>
          </block>
        </next>
      </block>
    </next>
  </block>

  <block type="event_whenbroadcastreceived" id="bt7_bai1" x="40" y="350">
    <field name="BROADCAST_OPTION" id="msg_bai1" variabletype="broadcast_msg">Bai 1</field>
    <next>
      <block type="looks_switchbackdropto" id="bt7_bd1">
        <value name="BACKDROP"><shadow type="looks_backdrop"><field name="BACKDROP">AI</field></shadow></value>
        <next>
          <block type="text2speech_speakAndWait" id="bt7_tts_b1">
            <value name="WORDS"><shadow type="text"><field name="TEXT">AI la Tri tue Nhan tao, giup may tinh hoc va quyet dinh.</field></shadow></value>
            <next>
              <block type="looks_sayforsecs" id="bt7_say_b1_eng">
                <value name="MESSAGE">
                  <block type="translate_getTranslate" id="bt7_trans1">
                    <value name="WORDS"><shadow type="text"><field name="TEXT">AI la Tri tue Nhan tao, giup may tinh hoc va quyet dinh.</field></shadow></value>
                    <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                  </block>
                </value>
                <value name="SECS"><shadow type="math_number"><field name="NUM">4</field></shadow></value>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>

  <block type="faceDetection_whenFace" id="bt7_face_smile" x="520" y="350">
    <value name="FACE_EXPRESSION"><shadow type="faceDetection_menu_FACE_EXPRESSION"><field name="FACE_EXPRESSION">smiling</field></shadow></value>
    <next>
      <block type="event_broadcast" id="bt7_bc_next">
        <value name="BROADCAST_INPUT">
          <shadow type="event_broadcast_menu">
            <field name="BROADCAST_OPTION" id="msg_bai2" variabletype="broadcast_msg">Bai 2</field>
          </shadow>
        </value>
      </block>
    </next>
  </block>
</xml>`
  },

  // BT8: Tro choi bat bong - Face Sensing + TTS
  {
    id: 8,
    description: 'BT8 - Tro choi bat bong Face Sensing + TTS + Countdown 30s',
    extensions: ['Face Sensing', 'Text to Speech'],
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_diem">Diem</variable>
    <variable type="" id="var_tg">ThoiGian</variable>
    <variable type="broadcast_msg" id="msg_ketthuc">KetThuc</variable>
  </variables>
  <block type="event_whenflagclicked" id="bt8_ball_start" x="40" y="40">
    <next>
      <block type="data_setvariableto" id="bt8_set_diem">
        <field name="VARIABLE" id="var_diem" variabletype="">Diem</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
        <next>
          <block type="data_setvariableto" id="bt8_set_tg">
            <field name="VARIABLE" id="var_tg" variabletype="">ThoiGian</field>
            <value name="VALUE"><shadow type="math_number"><field name="NUM">30</field></shadow></value>
            <next>
              <block type="motion_gotoxy" id="bt8_init_pos">
                <value name="X"><block type="operator_random" id="bt8_rand1"><value name="FROM"><shadow type="math_number"><field name="NUM">-200</field></shadow></value><value name="TO"><shadow type="math_number"><field name="NUM">200</field></shadow></value></block></value>
                <value name="Y"><shadow type="math_number"><field name="NUM">170</field></shadow></value>
                <next>
                  <block type="control_repeat_until" id="bt8_fall_loop">
                    <value name="CONDITION">
                      <block type="operator_equals" id="bt8_tg_check">
                        <value name="OPERAND1"><block type="data_variable" id="bt8_tg_v"><field name="VARIABLE" id="var_tg" variabletype="">ThoiGian</field></block></value>
                        <value name="OPERAND2"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
                      </block>
                    </value>
                    <statement name="SUBSTACK">
                      <block type="motion_changeyby" id="bt8_fall">
                        <value name="DY"><shadow type="math_number"><field name="NUM">-10</field></shadow></value>
                        <next>
                          <block type="control_if" id="bt8_if_catch">
                            <value name="CONDITION">
                              <block type="sensing_touchingobject" id="bt8_touch_ro">
                                <value name="TOUCHINGOBJECTMENU"><shadow type="sensing_touchingobjectmenu"><field name="TOUCHINGOBJECTMENU">Ro</field></shadow></value>
                              </block>
                            </value>
                            <statement name="SUBSTACK">
                              <block type="data_changevariableby" id="bt8_inc_diem">
                                <field name="VARIABLE" id="var_diem" variabletype="">Diem</field>
                                <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                                <next>
                                  <block type="text2speech_speakAndWait" id="bt8_tts_catch">
                                    <value name="WORDS"><shadow type="text"><field name="TEXT">Bat duoc!</field></shadow></value>
                                    <next>
                                      <block type="motion_gotoxy" id="bt8_reset_ball">
                                        <value name="X"><block type="operator_random" id="bt8_rand2"><value name="FROM"><shadow type="math_number"><field name="NUM">-200</field></shadow></value><value name="TO"><shadow type="math_number"><field name="NUM">200</field></shadow></value></block></value>
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

  <block type="event_whenflagclicked" id="bt8_basket_ctrl" x="520" y="40">
    <next>
      <block type="control_forever" id="bt8_basket_forever">
        <statement name="SUBSTACK">
          <block type="motion_setx" id="bt8_setx_face">
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

  <block type="event_whenbroadcastreceived" id="bt8_result_show" x="40" y="480">
    <field name="BROADCAST_OPTION" id="msg_ketthuc" variabletype="broadcast_msg">KetThuc</field>
    <next>
      <block type="text2speech_speakAndWait" id="bt8_tts_result">
        <value name="WORDS">
          <block type="operator_join" id="bt8_join_result">
            <value name="STRING1"><shadow type="text"><field name="TEXT">Ban dat </field></shadow></value>
            <value name="STRING2">
              <block type="operator_join" id="bt8_join_result2">
                <value name="STRING1"><block type="data_variable" id="bt8_diem_j"><field name="VARIABLE" id="var_diem" variabletype="">Diem</field></block></value>
                <value name="STRING2"><shadow type="text"><field name="TEXT"> diem xuat sac!</field></shadow></value>
              </block>
            </value>
          </block>
        </value>
      </block>
    </next>
  </block>
</xml>`
  },

  // BT9: Bo loc AR - Body Sensing + Translate + TTS
  {
    id: 9,
    description: 'BT9 - Bo loc trang suc AR (Body Sensing + Translate + TTS + Broadcast costume)',
    extensions: ['Body Sensing', 'Translate', 'Text to Speech'],
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_idx">ChiSoCostume</variable>
    <variable type="broadcast_msg" id="msg_doi">DoiTrangSuc</variable>
  </variables>
  <block type="event_whenflagclicked" id="bt9_mu_start" x="40" y="40">
    <next>
      <block type="videoSensing_videoToggle" id="bt9_cam_on">
        <value name="VIDEO_STATE"><shadow type="videoSensing_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value>
        <next>
          <block type="control_forever" id="bt9_mu_forever">
            <statement name="SUBSTACK">
              <block type="motion_gotoxy" id="bt9_mu_goto">
                <value name="X">
                  <block type="bodySensing_getBodyPartX" id="bt9_mu_x">
                    <value name="PART"><shadow type="bodySensing_menu_PART"><field name="PART">nose</field></shadow></value>
                  </block>
                </value>
                <value name="Y">
                  <block type="bodySensing_getBodyPartY" id="bt9_mu_y">
                    <value name="PART"><shadow type="bodySensing_menu_PART"><field name="PART">nose</field></shadow></value>
                  </block>
                </value>
              </block>
            </statement>
          </block>
        </next>
      </block>
    </next>
  </block>

  <block type="event_whenbroadcastreceived" id="bt9_doi_trang_suc" x="40" y="300">
    <field name="BROADCAST_OPTION" id="msg_doi" variabletype="broadcast_msg">DoiTrangSuc</field>
    <next>
      <block type="looks_switchcostumeto" id="bt9_mu_costume">
        <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">mu1</field></shadow></value>
      </block>
    </next>
  </block>

  <block type="event_whenkeypressed" id="bt9_space" x="520" y="40">
    <field name="KEY_OPTION">space</field>
    <next>
      <block type="data_setvariableto" id="bt9_set_idx">
        <field name="VARIABLE" id="var_idx" variabletype="">ChiSoCostume</field>
        <value name="VALUE">
          <block type="operator_random" id="bt9_rand">
            <value name="FROM"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
            <value name="TO"><shadow type="math_number"><field name="NUM">3</field></shadow></value>
          </block>
        </value>
        <next>
          <block type="event_broadcast" id="bt9_bc_doi">
            <value name="BROADCAST_INPUT">
              <shadow type="event_broadcast_menu">
                <field name="BROADCAST_OPTION" id="msg_doi" variabletype="broadcast_msg">DoiTrangSuc</field>
              </shadow>
            </value>
            <next>
              <block type="control_wait" id="bt9_wait">
                <value name="DURATION"><shadow type="math_positive_number"><field name="NUM">0.5</field></shadow></value>
                <next>
                  <block type="looks_sayforsecs" id="bt9_say_mota">
                    <value name="MESSAGE"><shadow type="text"><field name="TEXT">Bo trang suc moi that long lay!</field></shadow></value>
                    <value name="SECS"><shadow type="math_number"><field name="NUM">2</field></shadow></value>
                    <next>
                      <block type="text2speech_speakAndWait" id="bt9_tts_eng">
                        <value name="WORDS">
                          <block type="translate_getTranslate" id="bt9_trans">
                            <value name="WORDS"><shadow type="text"><field name="TEXT">Bo trang suc moi that long lay!</field></shadow></value>
                            <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
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
    </next>
  </block>
</xml>`
  },

  // BT10: Diem danh AI - Teachable Machine + TTS + Translate + List
  {
    id: 10,
    description: 'BT10 - Diem danh AI toan dien (Teachable Machine + TTS + Translate + List)',
    extensions: ['Teachable Machine', 'Text to Speech', 'Translate'],
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_tg">ThoiGian</variable>
    <variable type="" id="var_soco">SoCo</variable>
    <variable type="list" id="list_danhsach">DaDiemDanh</variable>
    <variable type="broadcast_msg" id="msg_hetgio">HetGio</variable>
  </variables>
  <block type="event_whenflagclicked" id="bt10_start" x="40" y="40">
    <next>
      <block type="data_deletealloflist" id="bt10_clear">
        <field name="LIST" id="list_danhsach" variabletype="list">DaDiemDanh</field>
        <next>
          <block type="data_setvariableto" id="bt10_set_tg">
            <field name="VARIABLE" id="var_tg" variabletype="">ThoiGian</field>
            <value name="VALUE"><shadow type="math_number"><field name="NUM">30</field></shadow></value>
            <next>
              <block type="control_repeat_until" id="bt10_loop">
                <value name="CONDITION">
                  <block type="operator_equals" id="bt10_tg_check">
                    <value name="OPERAND1"><block type="data_variable" id="bt10_tg_v"><field name="VARIABLE" id="var_tg" variabletype="">ThoiGian</field></block></value>
                    <value name="OPERAND2"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
                  </block>
                </value>
                <statement name="SUBSTACK">
                  <block type="control_if" id="bt10_if_tv1">
                    <value name="CONDITION">
                      <block type="operator_not" id="bt10_not_tv1">
                        <value name="OPERAND">
                          <block type="data_listcontainsitem" id="bt10_list_check">
                            <field name="LIST" id="list_danhsach" variabletype="list">DaDiemDanh</field>
                            <value name="ITEM"><shadow type="text"><field name="TEXT">Thanh vien 1</field></shadow></value>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="SUBSTACK">
                      <block type="data_addtolist" id="bt10_add_tv1">
                        <field name="LIST" id="list_danhsach" variabletype="list">DaDiemDanh</field>
                        <value name="ITEM"><shadow type="text"><field name="TEXT">Thanh vien 1</field></shadow></value>
                        <next>
                          <block type="text2speech_speakAndWait" id="bt10_tts_tv1">
                            <value name="WORDS"><shadow type="text"><field name="TEXT">Thanh vien 1 da diem danh!</field></shadow></value>
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

  <block type="event_whenbroadcastreceived" id="bt10_tong_ket" x="520" y="40">
    <field name="BROADCAST_OPTION" id="msg_hetgio" variabletype="broadcast_msg">HetGio</field>
    <next>
      <block type="data_setvariableto" id="bt10_count">
        <field name="VARIABLE" id="var_soco" variabletype="">SoCo</field>
        <value name="VALUE">
          <block type="data_lengthoflist" id="bt10_len">
            <field name="LIST" id="list_danhsach" variabletype="list">DaDiemDanh</field>
          </block>
        </value>
        <next>
          <block type="text2speech_speakAndWait" id="bt10_tts_vi">
            <value name="WORDS">
              <block type="operator_join" id="bt10_join1">
                <value name="STRING1"><shadow type="text"><field name="TEXT">Co </field></shadow></value>
                <value name="STRING2">
                  <block type="operator_join" id="bt10_join2">
                    <value name="STRING1"><block type="data_variable" id="bt10_soco_v"><field name="VARIABLE" id="var_soco" variabletype="">SoCo</field></block></value>
                    <value name="STRING2"><shadow type="text"><field name="TEXT"> tren 3 thanh vien diem danh.</field></shadow></value>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="text2speech_speakAndWait" id="bt10_tts_en">
                <value name="WORDS">
                  <block type="translate_getTranslate" id="bt10_trans">
                    <value name="WORDS">
                      <block type="operator_join" id="bt10_join3">
                        <value name="STRING1"><shadow type="text"><field name="TEXT">Co </field></shadow></value>
                        <value name="STRING2">
                          <block type="operator_join" id="bt10_join4">
                            <value name="STRING1"><block type="data_variable" id="bt10_soco_v2"><field name="VARIABLE" id="var_soco" variabletype="">SoCo</field></block></value>
                            <value name="STRING2"><shadow type="text"><field name="TEXT"> tren 3 thanh vien diem danh.</field></shadow></value>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                  </block>
                </value>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>`
  }
];

(async () => {
  console.log('=== PRG AI Blocks v6 — Generate BT2 to BT10 (camera delay fix) ===');
  console.log(`Output: ${OUT_DIR}`);

  const browser = await chromium.launch({
    headless: true,
    args: [
      '--use-fake-ui-for-media-stream',
      '--use-fake-device-for-media-stream'
    ]
  });
  
  const results = [];

  for (const ex of exercises) {
    try {
      const res = await generateExercise(browser, ex);
      results.push({ id: ex.id, status: 'OK', ...res });
    } catch (err) {
      console.error(`  [FAIL] BT${ex.id}: ${err.message.substring(0, 150)}`);
      results.push({ id: ex.id, status: 'FAIL', error: err.message });
    }
  }

  await browser.close();

  console.log('\n=== SUMMARY ===');
  let passed = 0, failed = 0;
  for (const r of results) {
    if (r.status === 'OK') {
      console.log(`  BT${r.id}: [OK] bt${r.id}_code.raw.png`);
      passed++;
    } else {
      console.log(`  BT${r.id}: [FAIL] ${r.error.substring(0, 100)}`);
      failed++;
    }
  }
  console.log(`\nTotal: ${passed} passed, ${failed} failed`);
  console.log('Status: PREVIEW_ONLY — Human review required before official use.');
})();
