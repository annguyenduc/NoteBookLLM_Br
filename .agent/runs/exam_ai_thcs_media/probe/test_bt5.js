const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const browser = await chromium.launch({
    headless: true,
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

  console.log('Loading Face Sensing extension...');
  // Open extension library
  await page.click('[class*="extension-button"]');
  await page.waitForTimeout(1000);
  await page.locator('text="Face Sensing"').first().click();
  
  console.log('Waiting 5 seconds for extension to initialize...');
  await page.waitForTimeout(5000);

  // Take a screenshot to see if it crashed or loaded
  await page.screenshot({ path: '../debug_bt5_loaded.png' });
  console.log('Screenshot saved as debug_bt5_loaded.png');

  console.log('Attempting workspace injection...');
  const xml = `<xml xmlns="http://www.w3.org/1999/xhtml">
    <variables></variables>
    <block type="event_whenflagclicked" id="bt5_start" x="40" y="40">
      <next>
        <block type="looks_say" id="bt5_say_wait">
          <value name="MESSAGE"><shadow type="text"><field name="TEXT">Nhin vao camera nao!</field></shadow></value>
        </block>
      </next>
    </block>
  </xml>`;

  try {
    await page.evaluate((xmlText) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      console.log('Clearing workspace...');
      ws.clear();
      console.log('Parsing XML...');
      const dom = B.Xml.textToDom(xmlText);
      console.log('Loading XML to workspace...');
      B.Xml.domToWorkspace(dom, ws);
      console.log('Rendering workspace...');
      ws.render();
    }, xml);
    console.log('[PASS] Inject succeeded!');
  } catch (e) {
    console.error('[FAIL] Inject failed:', e.message);
    console.error('Stack:', e.stack);
  }

  await browser.close();
})();
