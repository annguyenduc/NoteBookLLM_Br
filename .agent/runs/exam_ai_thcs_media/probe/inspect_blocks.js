const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('Navigating to playground...');
  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'domcontentloaded', timeout: 90000
  });

  await page.waitForFunction(() =>
    window.Blockly &&
    typeof window.Blockly.getMainWorkspace === 'function' &&
    window.Blockly.getMainWorkspace()
  , { timeout: 90000 });

  await page.waitForTimeout(2000);

  // Load Translate & Text to Speech just in case they define their own types
  console.log('Opening extension library to load Translate/TTS...');
  try {
    await page.click('[class*="extension-button"]');
    await page.waitForTimeout(1000);
    await page.click('text="Text to Speech"');
    await page.waitForTimeout(1500);
  } catch (e) {
    console.log('TTS load skip/fail:', e.message);
  }

  const inspection = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    
    function inspectBlock(type, fieldName) {
      try {
        const block = ws.newBlock(type);
        if (!block) return { error: `Block ${type} not found` };
        const field = block.getField(fieldName);
        if (!field) return { error: `Field ${fieldName} not found on ${type}` };
        
        const info = {
          type: type,
          fieldName: fieldName,
          defaultType: field.defaultType_ || null,
          variableTypes: field.variableTypes || null
        };
        block.dispose();
        return info;
      } catch (e) {
        return { type, fieldName, error: e.message };
      }
    }

    return {
      broadcast: inspectBlock('event_whenbroadcastreceived', 'BROADCAST_OPTION'),
      broadcast_send: inspectBlock('event_broadcast', 'BROADCAST_INPUT'),
      list_add: inspectBlock('data_addtolist', 'LIST'),
      var_set: inspectBlock('data_setvariableto', 'VARIABLE')
    };
  });

  console.log('Inspection results:', JSON.stringify(inspection, null, 2));

  await browser.close();
})();
