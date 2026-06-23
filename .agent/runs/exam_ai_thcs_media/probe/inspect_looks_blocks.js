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

  console.log('Loading extensions...');
  try {
    await page.click('[class*="extension-button"]');
    await page.waitForTimeout(1000);
    await page.locator('text="Face Sensing"').first().click();
    await page.waitForTimeout(3000);
  } catch (e) {
    console.log('Face Sensing load skip/fail:', e.message);
  }

  const structures = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    
    function inspectBlockStructure(type) {
      try {
        // We clear workspace, create the block natively using Scratch-blocks,
        // which automatically Populates default shadow blocks on creation,
        // then we export the workspace to XML.
        ws.clear();
        const block = ws.newBlock(type);
        if (!block) return `Error: Block ${type} not found`;
        
        // Render workspace so shadow blocks are fully generated
        ws.render();
        
        const dom = B.Xml.workspaceToDom(ws);
        const text = new XMLSerializer().serializeToString(dom);
        return text;
      } catch (e) {
        return `Error on ${type}: ${e.message}`;
      }
    }

    return {
      switch_costume: inspectBlockStructure('looks_switchcostumeto'),
      switch_backdrop: inspectBlockStructure('looks_switchbackdropto'),
      face_when: inspectBlockStructure('faceDetection_whenFace')
    };
  });

  console.log('Inspection results:\n', JSON.stringify(structures, null, 2));

  await browser.close();
})();
