/**
 * generate_bt8.js
 * Generator for BT8 (Face-controlled game with Face Sensing, TTS).
 * Status: PREVIEW_ONLY
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
    <variable type="" id="var_score">score</variable>
    <variable type="" id="var_time">time</variable>
    <variable type="broadcast_msg" id="msg_gameOver">gameOver</variable>
  </variables>

  <!-- 1. Script cho Bóng (Ball falling, catching, resetting) -->
  <block type="event_whenflagclicked" id="bt8_ball_start" x="40" y="40">
    <next>
      <block type="data_setvariableto" id="bt8_set_score">
        <field name="VARIABLE" id="var_score" variabletype="">score</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
        <next>
          <block type="motion_gotoxy" id="bt8_init_pos">
            <value name="X">
              <block type="operator_random" id="bt8_rand1">
                <value name="FROM"><shadow type="math_number"><field name="NUM">-200</field></shadow></value>
                <value name="TO"><shadow type="math_number"><field name="NUM">200</field></shadow></value>
              </block>
            </value>
            <value name="Y"><shadow type="math_number"><field name="NUM">170</field></shadow></value>
            <next>
              <block type="control_forever" id="bt8_fall_loop">
                <statement name="SUBSTACK">
                  <block type="motion_changeyby" id="bt8_fall">
                    <value name="DY"><shadow type="math_number"><field name="NUM">-8</field></shadow></value>
                    <next>
                      <block type="control_if" id="bt8_if_catch">
                        <value name="CONDITION">
                          <block type="sensing_touchingobject" id="bt8_touch_ro">
                            <value name="TOUCHINGOBJECTMENU">
                              <shadow type="sensing_touchingobjectmenu">
                                <field name="TOUCHINGOBJECTMENU">Ro</field>
                              </shadow>
                            </value>
                          </block>
                        </value>
                        <statement name="SUBSTACK">
                          <block type="data_changevariableby" id="bt8_inc_score">
                            <field name="VARIABLE" id="var_score" variabletype="">score</field>
                            <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                            <next>
                              <block type="text2speech_speakAndWait" id="bt8_tts_catch">
                                <value name="WORDS"><shadow type="text"><field name="TEXT">Bat duoc!</field></shadow></value>
                                <next>
                                  <block type="motion_gotoxy" id="bt8_reset_ball">
                                    <value name="X">
                                      <block type="operator_random" id="bt8_rand2">
                                        <value name="FROM"><shadow type="math_number"><field name="NUM">-200</field></shadow></value>
                                        <value name="TO"><shadow type="math_number"><field name="NUM">200</field></shadow></value>
                                      </block>
                                    </value>
                                    <value name="Y"><shadow type="math_number"><field name="NUM">170</field></shadow></value>
                                  </block>
                                </next>
                              </block>
                            </next>
                          </block>
                        </statement>
                        <next>
                          <block type="control_if" id="bt8_if_bottom">
                            <value name="CONDITION">
                              <block type="operator_lt" id="bt8_lt_bottom">
                                <value name="OPERAND1"><block type="motion_yposition" id="bt8_ypos"></block></value>
                                <value name="OPERAND2"><shadow type="math_number"><field name="NUM">-170</field></shadow></value>
                              </block>
                            </value>
                            <statement name="SUBSTACK">
                              <block type="motion_gotoxy" id="bt8_reset_ball_bottom">
                                <value name="X">
                                  <block type="operator_random" id="bt8_rand3">
                                    <value name="FROM"><shadow type="math_number"><field name="NUM">-200</field></shadow></value>
                                    <value name="TO"><shadow type="math_number"><field name="NUM">200</field></shadow></value>
                                  </block>
                                </value>
                                <value name="Y"><shadow type="math_number"><field name="NUM">170</field></shadow></value>
                              </block>
                            </statement>
                            <next>
                              <block type="control_wait" id="bt8_wait_tick">
                                <value name="DURATION"><shadow type="math_positive_number"><field name="NUM">0.05</field></shadow></value>
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

  <!-- 2. Script cho Rổ hứng (Basket bám theo tọa độ X khuôn mặt) -->
  <block type="event_whenflagclicked" id="bt8_basket_ctrl" x="540" y="40">
    <next>
      <block type="poseFace_videoToggle" id="bt8_cam_on">
        <value name="VIDEO_STATE">
          <shadow type="poseFace_menu_VIDEO_STATE">
            <field name="VIDEO_STATE">on</field>
          </shadow>
        </value>
        <next>
          <block type="control_forever" id="bt8_basket_forever">
            <statement name="SUBSTACK">
              <block type="motion_setx" id="bt8_setx_face">
                <value name="X">
                  <block type="faceDetection_faceX" id="bt8_face_x">
                    <value name="FACE">
                      <shadow type="faceDetection_menu_FACE">
                        <field name="FACE">1</field>
                      </shadow>
                    </value>
                  </block>
                </value>
              </block>
            </statement>
          </block>
        </next>
      </block>
    </next>
  </block>

  <!-- 3. Script cho Đồng hồ đếm ngược 30 giây độc lập -->
  <block type="event_whenflagclicked" id="bt8_timer_start" x="900" y="40">
    <next>
      <block type="data_setvariableto" id="bt8_set_time">
        <field name="VARIABLE" id="var_time" variabletype="">time</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">30</field></shadow></value>
        <next>
          <block type="control_repeat" id="bt8_timer_loop">
            <value name="TIMES"><shadow type="math_number"><field name="NUM">30</field></shadow></value>
            <statement name="SUBSTACK">
              <block type="control_wait" id="bt8_wait_1s">
                <value name="DURATION"><shadow type="math_positive_number"><field name="NUM">1</field></shadow></value>
                <next>
                  <block type="data_changevariableby" id="bt8_dec_time">
                    <field name="VARIABLE" id="var_time" variabletype="">time</field>
                    <value name="VALUE"><shadow type="math_number"><field name="NUM">-1</field></shadow></value>
                  </block>
                </next>
              </block>
            </statement>
            <next>
              <block type="event_broadcast" id="bt8_broadcast_gameover">
                <value name="BROADCAST_INPUT">
                  <shadow type="event_broadcast_menu">
                    <field name="BROADCAST_OPTION" id="msg_gameOver" variabletype="broadcast_msg">gameOver</field>
                  </shadow>
                </value>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>

  <!-- 4. Script khi nhận gameOver thì thông báo điểm -->
  <block type="event_whenbroadcastreceived" id="bt8_on_gameover" x="540" y="320">
    <field name="BROADCAST_OPTION" id="msg_gameOver" variabletype="broadcast_msg">gameOver</field>
    <next>
      <block type="control_stop" id="bt8_stop_all_scripts">
        <field name="STOP_OPTION">other scripts in sprite</field>
        <next>
          <block type="looks_sayforsecs" id="bt8_say_score">
            <value name="MESSAGE">
              <block type="operator_join" id="bt8_join_msg1">
                <value name="STRING1"><shadow type="text"><field name="TEXT">Ban dat </field></shadow></value>
                <value name="STRING2">
                  <block type="operator_join" id="bt8_join_msg2">
                    <value name="STRING1">
                      <block type="data_variable" id="bt8_v_score">
                        <field name="VARIABLE" id="var_score" variabletype="">score</field>
                      </block>
                    </value>
                    <value name="STRING2"><shadow type="text"><field name="TEXT"> diem!</field></shadow></value>
                  </block>
                </value>
              </block>
            </value>
            <value name="SECS"><shadow type="math_number"><field name="NUM">3</field></shadow></value>
            <next>
              <block type="text2speech_speakAndWait" id="bt8_tts_score">
                <value name="WORDS">
                  <block type="operator_join" id="bt8_join_msg3">
                    <value name="STRING1"><shadow type="text"><field name="TEXT">Ban dat </field></shadow></value>
                    <value name="STRING2">
                      <block type="operator_join" id="bt8_join_msg4">
                        <value name="STRING1">
                          <block type="data_variable" id="bt8_v_score2">
                            <field name="VARIABLE" id="var_score" variabletype="">score</field>
                          </block>
                        </value>
                        <value name="STRING2"><shadow type="text"><field name="TEXT"> diem!</field></shadow></value>
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
    await page.screenshot({ path: path.join(OUT_DIR, 'bt8_fail.png'), fullPage: false });
    await browser.close();
    process.exit(1);
  }

  await page.waitForTimeout(3000);

  // Save screenshot
  const pngPath = path.join(OUT_DIR, 'bt8_code.raw.png');
  await page.screenshot({ path: pngPath, fullPage: true });
  console.log(`[OK] Saved screenshot to: ${pngPath}`);

  // Save XML
  const xmlPath = path.join(OUT_DIR, 'bt8_code.xml');
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

    const sb3Path = path.join(OUT_DIR, 'bt8_code.sb3');
    await download.saveAs(sb3Path);
    console.log(`[OK] Saved SB3 to: ${sb3Path}`);
  } catch (sb3Err) {
    console.error('[FAIL] SB3 export failed:', sb3Err.message);
  }

  await browser.close();
  console.log('Generation completed.');
})();
