const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 800 });
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForSelector('.blocklySvg', { timeout: 30000 });
  await page.waitForTimeout(2000);
  
  const extBtn = await page.$('[class^="gui_extension-button"]');
  if (extBtn) {
    console.log('Clicking Extension Button...');
    await extBtn.click();
    await page.waitForTimeout(3000);
    
    // Chụp ảnh màn hình modal extension
    await page.screenshot({ path: 'extension_modal.png' });
    console.log('Saved extension_modal.png');
    
    // In ra danh sách tất cả các div có class chứa "library" hoặc "card"
    const classes = await page.evaluate(() => {
      const allDivs = Array.from(document.querySelectorAll('div'));
      return allDivs
        .map(d => d.className)
        .filter(c => typeof c === 'string' && (c.includes('library') || c.includes('card') || c.includes('extension')))
        .slice(0, 30);
    });
    console.log('Found classes:', classes);
  } else {
    console.log('Extension Button not found.');
  }
  await browser.close();
})();
