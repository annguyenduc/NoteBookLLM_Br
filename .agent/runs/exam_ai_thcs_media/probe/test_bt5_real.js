const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  console.log('Launching browser in non-headless mode...');
  const browser = await chromium.launch({
    headless: false,
    args: [
      '--use-fake-ui-for-media-stream',
      '--use-fake-device-for-media-stream'
    ]
  });
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

  console.log('Loading playground...');
  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'domcontentloaded', timeout: 90000
  });

  await page.waitForFunction(() =>
    window.Blockly &&
    typeof window.Blockly.getMainWorkspace === 'function' &&
    window.Blockly.getMainWorkspace()
  , { timeout: 90000 });

  await page.waitForTimeout(3000);

  console.log('Loading Face Sensing...');
  await page.click('[class*="extension-button"]');
  await page.waitForTimeout(1000);
  await page.locator('text="Face Sensing"').first().click();
  
  console.log('Waiting 8 seconds for models...');
  await page.waitForTimeout(8000);

  const xml = `<xml xmlns="http://www.w3.org/1999/xhtml">
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
</xml>`;

  console.log('Attempting workspace injection...');
  try {
    await page.evaluate((xmlText) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const dom = B.Xml.textToDom(xmlText);
      B.Xml.domToWorkspace(dom, ws);
      ws.render();
    }, xml);
    console.log('[PASS] Inject succeeded in non-headless mode!');
    await page.screenshot({ path: '../debug_bt5_real.png' });
  } catch (e) {
    console.error('[FAIL] Inject failed:', e.message);
  }

  await browser.close();
})();
