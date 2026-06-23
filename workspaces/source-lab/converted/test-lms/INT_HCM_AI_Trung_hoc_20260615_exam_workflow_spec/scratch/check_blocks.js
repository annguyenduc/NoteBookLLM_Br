const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForSelector('.blocklySvg', { timeout: 30000 });
  await page.waitForTimeout(2000);
  
  const info = await page.evaluate(() => {
    const B = window.Blockly;
    if (!B) return { error: 'window.Blockly is undefined' };
    return {
      error: null,
      keys: Object.keys(B)
    };
  });
  
  console.log('Blockly keys:', JSON.stringify(info, null, 2));
  await browser.close();
})();
