/**
 * generate_bt5.js
 * Generator for BT5 (Character Face Expression Reaction with Face Sensing, Translate, TTS).
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
  </variables>
  <block type="event_whenflagclicked" id="bt5_start" x="40" y="40">
    <next>
      <block type="poseFace_videoToggle" id="bt5_cam_on">
        <value name="VIDEO_STATE">
          <shadow type="poseFace_menu_VIDEO_STATE">
            <field name="VIDEO_STATE">on</field>
          </shadow>
        </value>
        <next>
          <block type="looks_switchcostumeto" id="bt5_costume_wait">
            <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">cho</field></shadow></value>
            <next>
              <block type="looks_switchbackdropto" id="bt5_backdrop_wait">
                <value name="BACKDROP"><shadow type="looks_backdrop"><field name="BACKDROP">binh thuong</field></shadow></value>
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
    </next>
  </block>

  <block type="poseFace_affdexWhenExpression" id="bt5_face_vui" x="40" y="250">
    <value name="EXPRESSION">
      <shadow type="poseFace_menu_EXPRESSION">
        <field name="EXPRESSION">smile</field>
      </shadow>
    </value>
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
                    <next>
                      <block type="text2speech_speakAndWait" id="bt5_speak_vui">
                        <value name="WORDS">
                          <block type="translate_getTranslate" id="bt5_trans_vui_tts">
                            <value name="WORDS"><shadow type="text"><field name="TEXT">Ban dang rat vui ve!</field></shadow></value>
                            <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                          </block>
                        </value>
                        <next>
                          <block type="looks_switchcostumeto" id="bt5_costume_wait_after_vui">
                            <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">cho</field></shadow></value>
                            <next>
                              <block type="looks_say" id="bt5_say_wait_after_vui">
                                <value name="MESSAGE"><shadow type="text"><field name="TEXT">Dang cho cam xuc...</field></shadow></value>
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

  <block type="poseFace_affdexWhenExpression" id="bt5_face_sad" x="520" y="250">
    <value name="EXPRESSION">
      <shadow type="poseFace_menu_EXPRESSION">
        <field name="EXPRESSION">sad</field>
      </shadow>
    </value>
    <next>
      <block type="looks_switchcostumeto" id="bt5_costume_sad">
        <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">buon</field></shadow></value>
        <next>
          <block type="looks_switchbackdropto" id="bt5_backdrop_sad">
            <value name="BACKDROP"><shadow type="looks_backdrop"><field name="BACKDROP">buon</field></shadow></value>
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
                    <next>
                      <block type="text2speech_speakAndWait" id="bt5_speak_sad">
                        <value name="WORDS">
                          <block type="translate_getTranslate" id="bt5_trans_sad_tts">
                            <value name="WORDS"><shadow type="text"><field name="TEXT">Co chuyen gi buon vay?</field></shadow></value>
                            <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                          </block>
                        </value>
                        <next>
                          <block type="looks_switchcostumeto" id="bt5_costume_wait_after_sad">
                            <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">cho</field></shadow></value>
                            <next>
                              <block type="looks_say" id="bt5_say_wait_after_sad">
                                <value name="MESSAGE"><shadow type="text"><field name="TEXT">Dang cho cam xuc...</field></shadow></value>
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

  <block type="poseFace_affdexWhenExpression" id="bt5_face_surprise" x="980" y="250">
    <value name="EXPRESSION">
      <shadow type="poseFace_menu_EXPRESSION">
        <field name="EXPRESSION">surprise</field>
      </shadow>
    </value>
    <next>
      <block type="looks_switchcostumeto" id="bt5_costume_surprise">
        <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">ngac nhien</field></shadow></value>
        <next>
          <block type="looks_switchbackdropto" id="bt5_backdrop_surprise">
            <value name="BACKDROP"><shadow type="looks_backdrop"><field name="BACKDROP">ngac nhien</field></shadow></value>
            <next>
              <block type="looks_sayforsecs" id="bt5_say_surprise">
                <value name="MESSAGE"><shadow type="text"><field name="TEXT">Ban ngac nhien qua!</field></shadow></value>
                <value name="SECS"><shadow type="math_number"><field name="NUM">2</field></shadow></value>
                <next>
                  <block type="looks_sayforsecs" id="bt5_say_surprise_eng">
                    <value name="MESSAGE">
                      <block type="translate_getTranslate" id="bt5_trans_surprise">
                        <value name="WORDS"><shadow type="text"><field name="TEXT">Ban ngac nhien qua!</field></shadow></value>
                        <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                      </block>
                    </value>
                    <value name="SECS"><shadow type="math_number"><field name="NUM">2</field></shadow></value>
                    <next>
                      <block type="text2speech_speakAndWait" id="bt5_speak_surprise">
                        <value name="WORDS">
                          <block type="translate_getTranslate" id="bt5_trans_surprise_tts">
                            <value name="WORDS"><shadow type="text"><field name="TEXT">Ban ngac nhien qua!</field></shadow></value>
                            <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                          </block>
                        </value>
                        <next>
                          <block type="looks_switchcostumeto" id="bt5_costume_wait_after_surprise">
                            <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">cho</field></shadow></value>
                            <next>
                              <block type="looks_say" id="bt5_say_wait_after_surprise">
                                <value name="MESSAGE"><shadow type="text"><field name="TEXT">Dang cho cam xuc...</field></shadow></value>
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
    await page.screenshot({ path: path.join(OUT_DIR, 'bt5_fail.png'), fullPage: false });
    await browser.close();
    process.exit(1);
  }

  await page.waitForTimeout(3000);

  // Save screenshot
  const pngPath = path.join(OUT_DIR, 'bt5_code.raw.png');
  await page.screenshot({ path: pngPath, fullPage: true });
  console.log(`[OK] Saved screenshot to: ${pngPath}`);

  // Save XML
  const xmlPath = path.join(OUT_DIR, 'bt5_code.xml');
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

    const sb3Path = path.join(OUT_DIR, 'bt5_code.sb3');
    await download.saveAs(sb3Path);
    console.log(`[OK] Saved SB3 to: ${sb3Path}`);
  } catch (sb3Err) {
    console.error('[FAIL] SB3 export failed:', sb3Err.message);
  }

  await browser.close();
  console.log('Generation completed.');
})();
