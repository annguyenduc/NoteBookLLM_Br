const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 60000 });
  await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace());
  
  // Load Face Sensing
  console.log("Loading Face Sensing...");
  const addExtBtn = await page.locator('[class*="gui_extension-button"]').first();
  if (await addExtBtn.count() > 0) {
    await addExtBtn.click();
    await page.waitForTimeout(2000);
    const faceSensingCard = page.locator('text="Face Sensing"').first();
    await faceSensingCard.click();
    await page.waitForTimeout(6000);
  }

  const res = await page.evaluate(() => {
    try {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      
      // Tạo thử khối poseFace_affdexExpressionVal
      const block = ws.newBlock('poseFace_affdexExpressionVal');
      if (block) {
        return { success: true, name: block.type };
      }
      return { success: false, error: "Block not found" };
    } catch (err) {
      return { success: false, error: err.message };
    }
  });

  console.log("Result:", res);
  await browser.close();
})();
