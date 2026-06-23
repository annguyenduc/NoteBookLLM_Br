const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForSelector('.blocklySvg', { timeout: 30000 });
  await page.waitForTimeout(2000);
  
  const loadExtension = async (name) => {
    const extBtn = await page.$('[class^="gui_extension-button"]');
    if (extBtn) {
      await extBtn.click();
      await page.waitForTimeout(2000);
      const card = page.locator('[class*="library-item_library-item"]').filter({ hasText: name }).first();
      await card.click();
      await page.waitForTimeout(4000);
    }
  };

  await loadExtension('Face Sensing');

  const options = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    
    // Tìm cấu trúc khối poseFace_affdexGoToPart
    const block = ws.newBlock('poseFace_affdexGoToPart');
    if (!block) return 'Block not found';
    
    const field = block.getField('AFFDEX_POINT');
    if (field && typeof field.getOptions === 'function') {
      return field.getOptions();
    }
    
    return 'Field AFFDEX_POINT not found';
  });

  console.log('Face Sensing Parts Options:', JSON.stringify(options, null, 2));
  await browser.close();
})();
