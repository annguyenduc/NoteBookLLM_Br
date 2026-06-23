/**
 * generate_bt9.js
 * Generator for BT9 (AR Jewelry Filter with Body Sensing, Translate, TTS).
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
    await card.scrollIntoViewIfNeeded({ timeout: 8000 });
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
    <variable type="" id="var_idx">costumeIndex</variable>
    <variable type="broadcast_msg" id="msg_doi">changeJewelry</variable>
  </variables>
  <block type="event_whenflagclicked" id="bt9_mu_start" x="40" y="40">
    <next>
      <block type="poseBody_videoToggle" id="bt9_cam_on">
        <value name="VIDEO_STATE">
          <shadow type="poseBody_menu_VIDEO_STATE">
            <field name="VIDEO_STATE">on</field>
          </shadow>
        </value>
        <next>
          <block type="control_forever" id="bt9_mu_forever">
            <statement name="SUBSTACK">
              <block type="poseBody_goToPart" id="bt9_mu_goto">
                <value name="PART">
                  <shadow type="poseBody_menu_PART">
                    <field name="PART">nose</field>
                  </shadow>
                </value>
              </block>
            </statement>
          </block>
        </next>
      </block>
    </next>
  </block>

  <block type="event_whenbroadcastreceived" id="bt9_doi_trang_suc" x="40" y="300">
    <field name="BROADCAST_OPTION" id="msg_doi" variabletype="broadcast_msg">changeJewelry</field>
    <next>
      <block type="looks_switchcostumeto" id="bt9_mu_costume">
        <value name="COSTUME">
          <block type="data_variable" id="bt9_var_costumeIndex">
            <field name="VARIABLE" id="var_idx" variabletype="">costumeIndex</field>
          </block>
        </value>
      </block>
    </next>
  </block>

  <block type="event_whenkeypressed" id="bt9_space" x="520" y="40">
    <field name="KEY_OPTION">space</field>
    <next>
      <block type="data_setvariableto" id="bt9_set_idx">
        <field name="VARIABLE" id="var_idx" variabletype="">costumeIndex</field>
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
                <field name="BROADCAST_OPTION" id="msg_doi" variabletype="broadcast_msg">changeJewelry</field>
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
    await page.screenshot({ path: path.join(OUT_DIR, 'bt9_fail.png'), fullPage: false });
    await browser.close();
    process.exit(1);
  }

  await page.waitForTimeout(3000);

  // Save screenshot
  const pngPath = path.join(OUT_DIR, 'bt9_code.raw.png');
  await page.screenshot({ path: pngPath, fullPage: true });
  console.log(`[OK] Saved screenshot to: ${pngPath}`);

  // Save XML
  const xmlPath = path.join(OUT_DIR, 'bt9_code.xml');
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

    const sb3Path = path.join(OUT_DIR, 'bt9_code.sb3');
    await download.saveAs(sb3Path);
    console.log(`[OK] Saved SB3 to: ${sb3Path}`);
  } catch (sb3Err) {
    console.error('[FAIL] SB3 export failed:', sb3Err.message);
  }

  await browser.close();
  console.log('Generation completed.');
})();
