const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  
  console.log("Navigating to playground...");
  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'networkidle',
    timeout: 60000
  });

  await page.waitForFunction(() => {
    return (
      window.Blockly &&
      typeof window.Blockly.getMainWorkspace === 'function' &&
      window.Blockly.getMainWorkspace()
    );
  }, { timeout: 60000 });

  console.log("Loading Face Sensing extension...");
  const addExtBtn = await page.locator('[class*="gui_extension-button"]').first();
  if (await addExtBtn.count() > 0) {
    await addExtBtn.click();
  } else {
    await page.mouse.click(20, 690);
  }

  await page.waitForTimeout(2000);

  const faceSensingCard = page.locator('text="Face Sensing"').first();
  if (await faceSensingCard.count() > 0) {
    await faceSensingCard.click();
  } else {
    const cards = page.locator('[class*="library_library-item"]');
    const texts = await cards.allTextContents();
    const idx = texts.findIndex(t => t.includes("Face Sensing"));
    if (idx !== -1) {
      await cards.nth(idx).click();
    }
  }

  console.log("Waiting for extension to load...");
  await page.waitForTimeout(8000);

  // List all registered Blockly blocks starting with poseFace_
  const blocksList = await page.evaluate(() => {
    const B = window.Blockly;
    const B_Blocks = B.Blocks || {};
    const keys = Object.keys(B_Blocks);
    const poseFaceBlocks = keys.filter(k => k.toLowerCase().includes('face'));
    
    // Check if we can get toolbox XML or categories
    const ws = B.getMainWorkspace();
    const callbacks = ws.toolboxCategoryCallbacks_;
    let xmlStr = "";
    if (callbacks && callbacks.get('FACE')) {
      const xmlList = callbacks.get('FACE')(ws);
      const parent = document.createElement('xml');
      xmlList.forEach(el => parent.appendChild(el.cloneNode(true)));
      xmlStr = new XMLSerializer().serializeToString(parent);
    } else if (callbacks && callbacks.get('face')) {
      const xmlList = callbacks.get('face')(ws);
      const parent = document.createElement('xml');
      xmlList.forEach(el => parent.appendChild(el.cloneNode(true)));
      xmlStr = new XMLSerializer().serializeToString(parent);
    }
    
    return {
      poseFaceBlocks: poseFaceBlocks,
      toolboxXml: xmlStr
    };
  });
  
  console.log("Registered Face Blocks:", blocksList.poseFaceBlocks);
  console.log("Face sensing category XML:", blocksList.toolboxXml);

  await browser.close();
})();
