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

  console.log('Opening extension library...');
  try {
    await page.click('[class*="extension-button"]', { timeout: 8000 });
    await page.waitForTimeout(2000);
    
    // Extract names of all cards in the extension picker
    // In Scratch-style GUI, cards have class like 'extension-library_library-item-name' or similar.
    // Let's grab all text content inside the library grid.
    const names = await page.evaluate(() => {
      // Find all divs or elements inside the library modal/grid
      // Typically Scratch library items have a grid
      const items = Array.from(document.querySelectorAll('[class*="library-item"]'));
      return items.map(el => {
        const nameEl = el.querySelector('[class*="name"]') || el;
        return nameEl.textContent.trim();
      }).filter(Boolean);
    });

    console.log('Available extensions:', names);
  } catch (e) {
    console.error('Failed to get extensions:', e.message);
    // Take a screenshot to inspect visually
    await page.screenshot({ path: '../debug_ext_library.png' });
    console.log('Screenshot saved to debug_ext_library.png');
  }

  await browser.close();
})();
