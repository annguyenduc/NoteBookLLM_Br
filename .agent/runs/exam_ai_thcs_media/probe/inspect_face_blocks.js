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

  console.log('Loading Face Sensing and Body Sensing extensions...');
  try {
    // Open library and load Face Sensing
    await page.click('[class*="extension-button"]');
    await page.waitForTimeout(1000);
    await page.locator('text="Face Sensing"').first().click();
    await page.waitForTimeout(4000);

    // Open library and load Body Sensing
    await page.click('[class*="extension-button"]');
    await page.waitForTimeout(1000);
    await page.locator('text="Body Sensing"').first().click();
    await page.waitForTimeout(4000);
  } catch (e) {
    console.log('Extensions load failed:', e.message);
  }

  const structures = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    
    const xmlKeys = Object.keys(B.Xml);
    
    function getBlockXmlText(type) {
      try {
        const block = ws.newBlock(type);
        if (!block) return `Error: Block ${type} not found`;
        
        let dom;
        // Try blockToDom
        if (typeof B.Xml.blockToDom === 'function') {
          dom = B.Xml.blockToDom(block);
        } else if (typeof B.Xml.blockToDomWithXY === 'function') {
          dom = B.Xml.blockToDomWithXY(block);
        } else {
          // Fallback: serialize workspace to dom
          // Temporarily isolate this block in workspace
          ws.clear();
          const block2 = ws.newBlock(type);
          dom = B.Xml.workspaceToDom(ws);
        }
        
        const text = new XMLSerializer().serializeToString(dom);
        return text;
      } catch (e) {
        return `Error on ${type}: ${e.message}`;
      }
    }

    return {
      xmlKeys: xmlKeys,
      face_when: getBlockXmlText('faceDetection_whenFace'),
      face_expression: getBlockXmlText('faceDetection_menu_FACE_EXPRESSION'),
      body_get_x: getBlockXmlText('bodySensing_getBodyPartX'),
      body_part_menu: getBlockXmlText('bodySensing_menu_PART'),
      video_toggle: getBlockXmlText('videoSensing_videoToggle')
    };
  });

  console.log('XML Structures:\n', JSON.stringify(structures, null, 2));

  await browser.close();
})();
