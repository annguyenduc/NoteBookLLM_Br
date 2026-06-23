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
      await page.click(`div[class*="library-item_library-item"]:has-text("${name}")`);
      await page.waitForTimeout(5000);
    }
  };

  await loadExtension('Teachable Machine');
  await loadExtension('Face Sensing');

  const vmInfo = await page.evaluate(() => {
    const vm = window.vm;
    if (!vm) return { error: 'window.vm is undefined', windowKeys: Object.keys(window) };
    
    const blockIds = vm.runtime ? Object.keys(vm.runtime._blockInfo || {}) : [];
    
    return {
      error: null,
      vmExists: true,
      blockIds: blockIds.filter(k => 
        k.toLowerCase().includes('tm') || 
        k.toLowerCase().includes('teachable') || 
        k.toLowerCase().includes('face') || 
        k.toLowerCase().includes('body')
      )
    };
  });
  
  console.log('VM Info:', JSON.stringify(vmInfo, null, 2));
  await browser.close();
})();
