/**
 * generate_bt6.js
 * Generator for BT6 (Gymnastics AI with Body Sensing, Variables count and isCounted, and Text to Speech).
 * Status: ACTIVE
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
    <variable type="" id="var_count">count</variable>
    <variable type="" id="var_isCounted">isCounted</variable>
  </variables>
  
  <block type="event_whenflagclicked" id="bt6_start" x="40" y="40">
    <next>
      <block type="data_setvariableto" id="bt6_set_count">
        <field name="VARIABLE" id="var_count" variabletype="">count</field>
        <value name="VALUE">
          <shadow type="math_number"><field name="NUM">0</field></shadow>
        </value>
        <next>
          <block type="data_setvariableto" id="bt6_set_isCounted">
            <field name="VARIABLE" id="var_isCounted" variabletype="">isCounted</field>
            <value name="VALUE">
              <shadow type="math_number"><field name="NUM">0</field></shadow>
            </value>
            <next>
              <block type="poseBody_videoToggle" id="bt6_cam_on">
                <value name="VIDEO_STATE">
                  <shadow type="poseBody_menu_VIDEO_STATE">
                    <field name="VIDEO_STATE">on</field>
                  </shadow>
                </value>
                <next>
                  <block type="looks_switchcostumeto" id="bt6_costume_tap">
                    <value name="COSTUME">
                      <shadow type="looks_costume"><field name="COSTUME">dang tap</field></shadow>
                    </value>
                    <next>
                      <block type="control_forever" id="bt6_forever">
                        <statement name="SUBSTACK">
                          <block type="poseBody_goToPart" id="bt6_goto_wrist">
                            <value name="PART">
                              <shadow type="poseBody_menu_PART">
                                <field name="PART">leftWrist</field>
                              </shadow>
                            </value>
                            <next>
                              <block type="control_if" id="bt6_if_raise">
                                <value name="CONDITION">
                                  <block type="operator_and" id="bt6_and_cond_raise">
                                    <value name="OPERAND1">
                                      <block type="operator_lt" id="bt6_lt_y">
                                        <value name="OPERAND1">
                                          <block type="motion_yposition" id="bt6_y_pos"></block>
                                        </value>
                                        <value name="OPERAND2">
                                          <shadow type="math_number"><field name="NUM">100</field></shadow>
                                        </value>
                                      </block>
                                    </value>
                                    <value name="OPERAND2">
                                      <block type="operator_equals" id="bt6_eq_isCounted_0">
                                        <value name="OPERAND1">
                                          <block type="data_variable" id="bt6_var_isCounted_v1">
                                            <field name="VARIABLE" id="var_isCounted" variabletype="">isCounted</field>
                                          </block>
                                        </value>
                                        <value name="OPERAND2">
                                          <shadow type="math_number"><field name="NUM">0</field></shadow>
                                        </value>
                                      </block>
                                    </value>
                                  </block>
                                </value>
                                <statement name="SUBSTACK">
                                  <block type="data_changevariableby" id="bt6_inc_count">
                                    <field name="VARIABLE" id="var_count" variabletype="">count</field>
                                    <value name="VALUE">
                                      <shadow type="math_number"><field name="NUM">1</field></shadow>
                                    </value>
                                    <next>
                                      <block type="data_setvariableto" id="bt6_set_isCounted_1">
                                        <field name="VARIABLE" id="var_isCounted" variabletype="">isCounted</field>
                                        <value name="VALUE">
                                          <shadow type="math_number"><field name="NUM">1</field></shadow>
                                        </value>
                                        <next>
                                          <block type="text2speech_speakAndWait" id="bt6_tts_count">
                                            <value name="WORDS">
                                              <block type="data_variable" id="bt6_var_count_v1">
                                                <field name="VARIABLE" id="var_count" variabletype="">count</field>
                                              </block>
                                            </value>
                                          </block>
                                        </next>
                                      </block>
                                    </next>
                                  </block>
                                </statement>
                                <next>
                                  <block type="control_if" id="bt6_if_lower">
                                    <value name="CONDITION">
                                      <block type="operator_and" id="bt6_and_cond_lower">
                                        <value name="OPERAND1">
                                          <block type="operator_gt" id="bt6_gt_y">
                                            <value name="OPERAND1">
                                              <block type="motion_yposition" id="bt6_y_pos2"></block>
                                            </value>
                                            <value name="OPERAND2">
                                              <shadow type="math_number"><field name="NUM">150</field></shadow>
                                            </value>
                                          </block>
                                        </value>
                                        <value name="OPERAND2">
                                          <block type="operator_equals" id="bt6_eq_isCounted_1">
                                            <value name="OPERAND1">
                                              <block type="data_variable" id="bt6_var_isCounted_v2">
                                                <field name="VARIABLE" id="var_isCounted" variabletype="">isCounted</field>
                                              </block>
                                            </value>
                                            <value name="OPERAND2">
                                              <shadow type="math_number"><field name="NUM">1</field></shadow>
                                            </value>
                                          </block>
                                        </value>
                                      </block>
                                    </value>
                                    <statement name="SUBSTACK">
                                      <block type="data_setvariableto" id="bt6_set_isCounted_0">
                                        <field name="VARIABLE" id="var_isCounted" variabletype="">isCounted</field>
                                        <value name="VALUE">
                                          <shadow type="math_number"><field name="NUM">0</field></shadow>
                                        </value>
                                      </block>
                                    </statement>
                                    <next>
                                      <block type="control_if" id="bt6_if_win">
                                        <value name="CONDITION">
                                          <block type="operator_equals" id="bt6_eq_count_10">
                                            <value name="OPERAND1">
                                              <block type="data_variable" id="bt6_var_count_v2">
                                                <field name="VARIABLE" id="var_count" variabletype="">count</field>
                                              </block>
                                            </value>
                                            <value name="OPERAND2">
                                              <shadow type="math_number"><field name="NUM">10</field></shadow>
                                            </value>
                                          </block>
                                        </value>
                                        <statement name="SUBSTACK">
                                          <block type="looks_switchcostumeto" id="bt6_costume_win">
                                            <value name="COSTUME">
                                              <shadow type="looks_costume"><field name="COSTUME">chuc mung</field></shadow>
                                            </value>
                                            <next>
                                              <block type="text2speech_speakAndWait" id="bt6_tts_win">
                                                <value name="WORDS">
                                                  <shadow type="text"><field name="TEXT">Chúc mừng bạn đã hoàn thành bài tập!</field></shadow>
                                                </value>
                                                <next>
                                                  <block type="looks_sayforsecs" id="bt6_say_win">
                                                    <value name="MESSAGE">
                                                      <shadow type="text"><field name="TEXT">Chúc mừng bạn đã hoàn thành!</field></shadow>
                                                    </value>
                                                    <value name="SECS">
                                                      <shadow type="math_number"><field name="NUM">2</field></shadow>
                                                    </value>
                                                    <next>
                                                      <block type="control_stop" id="bt6_stop">
                                                        <field name="STOP_OPTION">all</field>
                                                      </block>
                                                    </next>
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
      <block type="data_setvariableto" id="bt6_reset_count">
        <field name="VARIABLE" id="var_count" variabletype="">count</field>
        <value name="VALUE">
          <shadow type="math_number"><field name="NUM">0</field></shadow>
        </value>
        <next>
          <block type="data_setvariableto" id="bt6_reset_isCounted">
            <field name="VARIABLE" id="var_isCounted" variabletype="">isCounted</field>
            <value name="VALUE">
              <shadow type="math_number"><field name="NUM">0</field></shadow>
            </value>
            <next>
              <block type="looks_switchcostumeto" id="bt6_reset_costume">
                <value name="COSTUME">
                  <shadow type="looks_costume"><field name="COSTUME">dang tap</field></shadow>
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
  await loadExtension(page, 'Body Sensing');
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
    await page.screenshot({ path: path.join(OUT_DIR, 'bt6_fail.png'), fullPage: false });
    await browser.close();
    process.exit(1);
  }

  await page.waitForTimeout(3000);

  // Save screenshot
  const pngPath = path.join(OUT_DIR, 'bt6_code.raw.png');
  await page.screenshot({ path: pngPath, fullPage: true });
  console.log(`[OK] Saved screenshot to: ${pngPath}`);

  // Save XML
  const xmlPath = path.join(OUT_DIR, 'bt6_code.xml');
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

    const sb3Path = path.join(OUT_DIR, 'bt6_code.sb3');
    await download.saveAs(sb3Path);
    console.log(`[OK] Saved SB3 to: ${sb3Path}`);
  } catch (sb3Err) {
    console.error('[FAIL] SB3 export failed:', sb3Err.message);
  }

  await browser.close();
  console.log('Generation completed.');
})();
