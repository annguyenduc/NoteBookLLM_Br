/**
 * generate_bt10.js
 * Node.js script to generate answer files for Exercise 10 (BT10).
 * Loaded extensions: Teachable Machine, Text to Speech, Translate
 * English variables/lists: time, presentCount, list: presentList, broadcast: timeUp
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
    // Find card inside the extension modal by class and title
    const card = page.locator('[class*="library-item"]').filter({ hasText: displayName }).first();
    await card.scrollIntoViewIfNeeded({ timeout: 3000 });
    await card.click({ timeout: 5000 });
    await page.waitForTimeout(3000); // Wait after loading card
    console.log(`  [OK] Extension loaded: ${displayName}`);
    return true;
  } catch (e) {
    console.log(`  [WARN] Extension click failed for: ${displayName}. Trying fallback...`);
    try {
      await page.click(`text="${displayName}"`, { timeout: 3000 });
      await page.waitForTimeout(2000);
      return true;
    } catch (e2) {
      console.log(`  [FAIL] Failed to load extension: ${displayName}`);
      try { await page.locator('text="Back"').first().click({ timeout: 2000 }); await page.waitForTimeout(500); } catch (e3) {}
      return false;
    }
  }
}

// Blockly XML for Exercise 10
const BT10_XML = `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_time">time</variable>
    <variable type="" id="var_presentCount">presentCount</variable>
    <variable type="list" id="list_presentList">presentList</variable>
    <variable type="broadcast_msg" id="msg_timeUp">timeUp</variable>
  </variables>

  <!-- Green Flag clicked block -->
  <block type="event_whenflagclicked" id="bt10_start" x="40" y="40">
    <next>
      <block type="teachableMachine_videoToggle" id="bt10_video_on">
        <value name="VIDEO_STATE">
          <shadow type="teachableMachine_menu_VIDEO_STATE">
            <field name="VIDEO_STATE">on</field>
          </shadow>
        </value>
        <next>
          <block type="teachableMachine_useModelBlock" id="bt10_load_model">
            <value name="MODEL_URL">
              <shadow type="text">
                <field name="TEXT">https://teachablemachine.withgoogle.com/models/placeholder/</field>
              </shadow>
            </value>
            <next>
              <block type="data_deletealloflist" id="bt10_clear">
                <field name="LIST" id="list_presentList" variabletype="list">presentList</field>
                <next>
                  <block type="data_setvariableto" id="bt10_set_time">
                    <field name="VARIABLE" id="var_time" variabletype="">time</field>
                    <value name="VALUE">
                      <shadow type="math_number">
                        <field name="NUM">30</field>
                      </shadow>
                    </value>
                    <next>
                      <block type="data_setvariableto" id="bt10_set_count">
                        <field name="VARIABLE" id="var_presentCount" variabletype="">presentCount</field>
                        <value name="VALUE">
                          <shadow type="math_number">
                            <field name="NUM">0</field>
                          </shadow>
                        </value>
                        <next>
                          <block type="control_repeat_until" id="bt10_loop">
                            <value name="CONDITION">
                              <block type="operator_equals" id="bt10_tg_check">
                                <value name="OPERAND1">
                                  <block type="data_variable" id="bt10_tg_v">
                                    <field name="VARIABLE" id="var_time" variabletype="">time</field>
                                  </block>
                                </value>
                                <value name="OPERAND2">
                                  <shadow type="math_number">
                                    <field name="NUM">0</field>
                                  </shadow>
                                </value>
                              </block>
                            </value>
                            <statement name="SUBSTACK">
                              <!-- Detection block: check if not in list to avoid duplicate counting, and not Background -->
                              <block type="control_if" id="bt10_if_detect">
                                <value name="CONDITION">
                                  <block type="operator_and" id="bt10_and">
                                    <value name="OPERAND1">
                                      <block type="operator_not" id="bt10_not_contains">
                                        <value name="OPERAND">
                                          <block type="data_listcontainsitem" id="bt10_list_check">
                                            <field name="LIST" id="list_presentList" variabletype="list">presentList</field>
                                            <value name="ITEM">
                                              <block type="teachableMachine_modelPrediction" id="bt10_pred1"/>
                                            </value>
                                          </block>
                                        </value>
                                      </block>
                                    </value>
                                    <value name="OPERAND2">
                                      <block type="operator_not" id="bt10_not_bg">
                                        <value name="OPERAND">
                                          <block type="operator_equals" id="bt10_eq_bg">
                                            <value name="OPERAND1">
                                              <block type="teachableMachine_modelPrediction" id="bt10_pred2"/>
                                            </value>
                                            <value name="OPERAND2">
                                              <shadow type="text">
                                                <field name="TEXT">Background</field>
                                              </shadow>
                                            </value>
                                          </block>
                                        </value>
                                      </block>
                                    </value>
                                  </block>
                                </value>
                                <statement name="SUBSTACK">
                                  <!-- Add to check-in list -->
                                  <block type="data_addtolist" id="bt10_add_list">
                                    <field name="LIST" id="list_presentList" variabletype="list">presentList</field>
                                    <value name="ITEM">
                                      <block type="teachableMachine_modelPrediction" id="bt10_pred3"/>
                                    </value>
                                    <next>
                                      <!-- Speak confirmation -->
                                      <block type="text2speech_speakAndWait" id="bt10_tts_checkin">
                                        <value name="WORDS">
                                          <block type="operator_join" id="bt10_join_checkin">
                                            <value name="STRING1">
                                              <block type="teachableMachine_modelPrediction" id="bt10_pred4"/>
                                            </value>
                                            <value name="STRING2">
                                              <shadow type="text">
                                                <field name="TEXT"> da diem danh!</field>
                                              </shadow>
                                            </value>
                                          </block>
                                        </value>
                                      </block>
                                    </next>
                                  </block>
                                </statement>
                                <next>
                                  <!-- Wait 1 second and decrement time -->
                                  <block type="control_wait" id="bt10_wait_1s">
                                    <value name="DURATION">
                                      <shadow type="math_positive_number">
                                        <field name="NUM">1</field>
                                      </shadow>
                                    </value>
                                    <next>
                                      <block type="data_changevariableby" id="bt10_dec_time">
                                        <field name="VARIABLE" id="var_time" variabletype="">time</field>
                                        <value name="VALUE">
                                          <shadow type="math_number">
                                            <field name="NUM">-1</field>
                                          </shadow>
                                        </value>
                                      </block>
                                    </next>
                                  </block>
                                </next>
                              </block>
                            </statement>
                            <next>
                              <!-- Timeout: broadcast timeUp -->
                              <block type="event_broadcast" id="bt10_bc_timeup">
                                <value name="BROADCAST_INPUT">
                                  <shadow type="event_broadcast_menu">
                                    <field name="BROADCAST_OPTION" id="msg_timeUp" variabletype="broadcast_msg">timeUp</field>
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
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>

  <!-- Broadcast receiver block (When receive timeUp) -->
  <block type="event_whenbroadcastreceived" id="bt10_when_timeup" x="520" y="40">
    <field name="BROADCAST_OPTION" id="msg_timeUp" variabletype="broadcast_msg">timeUp</field>
    <next>
      <!-- Set presentCount to length of presentList -->
      <block type="data_setvariableto" id="bt10_set_count_end">
        <field name="VARIABLE" id="var_presentCount" variabletype="">presentCount</field>
        <value name="VALUE">
          <block type="data_lengthoflist" id="bt10_len">
            <field name="LIST" id="list_presentList" variabletype="list">presentList</field>
          </block>
        </value>
        <next>
          <!-- Speak Vietnamese result -->
          <block type="text2speech_speakAndWait" id="bt10_speak_vi">
            <value name="WORDS">
              <block type="operator_join" id="bt10_join_vi1">
                <value name="STRING1">
                  <shadow type="text">
                    <field name="TEXT">Co </field>
                  </shadow>
                </value>
                <value name="STRING2">
                  <block type="operator_join" id="bt10_join_vi2">
                    <value name="STRING1">
                      <block type="data_variable" id="bt10_v_count">
                        <field name="VARIABLE" id="var_presentCount" variabletype="">presentCount</field>
                      </block>
                    </value>
                    <value name="STRING2">
                      <shadow type="text">
                        <field name="TEXT"> thanh vien da diem danh.</field>
                      </shadow>
                    </value>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <!-- Speak English result (translated) -->
              <block type="text2speech_speakAndWait" id="bt10_speak_en">
                <value name="WORDS">
                  <block type="translate_getTranslate" id="bt10_trans">
                    <value name="WORDS">
                      <block type="operator_join" id="bt10_join_en1">
                        <value name="STRING1">
                          <shadow type="text">
                            <field name="TEXT">Co </field>
                          </shadow>
                        </value>
                        <value name="STRING2">
                          <block type="operator_join" id="bt10_join_en2">
                            <value name="STRING1">
                              <block type="data_variable" id="bt10_v_count2">
                                <field name="VARIABLE" id="var_presentCount" variabletype="">presentCount</field>
                              </block>
                            </value>
                            <value name="STRING2">
                              <shadow type="text">
                                <field name="TEXT"> thanh vien da diem danh.</field>
                              </shadow>
                            </value>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="LANGUAGE">
                      <shadow type="translate_menu_languages">
                        <field name="languages">en</field>
                      </shadow>
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
</xml>`;

(async () => {
  console.log('=== PRG AI Blocks — Generate BT10 (Teachable Machine + TTS + Translate) ===');
  console.log(`Output directory: ${OUT_DIR}`);

  const browser = await chromium.launch({
    headless: true,
    args: [
      '--use-fake-ui-for-media-stream',
      '--use-fake-device-for-media-stream'
    ]
  });
  
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

  try {
    console.log('Navigating to playground...');
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
    const requiredExtensions = ['Teachable Machine', 'Text to Speech', 'Translate'];
    for (const ext of requiredExtensions) {
      await loadExtension(page, ext);
    }

    console.log('Extensions loaded. Waiting 7 seconds for virtual camera and model setup...');
    await page.waitForTimeout(7000);

    // Inject XML into workspace
    console.log('Injecting Blockly XML...');
    const renderedXml = await page.evaluate((xml) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const dom = B.Xml.textToDom(xml);
      B.Xml.domToWorkspace(dom, ws);
      ws.render();
      return new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws));
    }, BT10_XML);

    await page.waitForTimeout(2000);

    // Take screenshot
    const pngPath = path.join(OUT_DIR, 'bt10_code.raw.png');
    await page.screenshot({ path: pngPath, fullPage: true });
    console.log(`  [OK] bt10_code.raw.png saved to ${pngPath}`);

    // Save XML file
    const xmlPath = path.join(OUT_DIR, 'bt10_code.xml');
    fs.writeFileSync(xmlPath, renderedXml, 'utf8');
    console.log(`  [OK] bt10_code.xml saved to ${xmlPath}`);

    // Download SB3 file
    console.log('Exporting SB3...');
    const fileMenu = page.locator('div').filter({ hasText: /^File$/ }).first();
    await fileMenu.click();
    await page.waitForTimeout(1000);

    const saveOption = page.locator('li').filter({ hasText: /Save to your computer/i }).first();
    
    // Set up download promise listener
    const downloadPromise = page.waitForEvent('download');
    await saveOption.click();
    const download = await downloadPromise;

    const sb3Path = path.join(OUT_DIR, 'bt10_code.sb3');
    await download.saveAs(sb3Path);
    console.log(`  [OK] bt10_code.sb3 saved to ${sb3Path}`);

    console.log('[PASS] Exercise 10 artifacts generated successfully.');
  } catch (err) {
    console.error(`[FAIL] Error occurred during BT10 generation: ${err.message}`);
    // Take fail screenshot for debugging
    try {
      await page.screenshot({ path: path.join(OUT_DIR, 'bt10_fail.png'), fullPage: false });
      console.log('  [DEBUG] Saved error screenshot to bt10_fail.png');
    } catch (ssErr) {}
  } finally {
    await browser.close();
  }
})();
