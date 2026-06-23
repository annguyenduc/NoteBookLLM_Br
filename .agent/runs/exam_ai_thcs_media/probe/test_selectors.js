const { chromium } = require('playwright');
(async () => {
  console.log('Testing Scratch GUI selectors...');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  try {
    await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace());
    await page.waitForTimeout(3000);
    
    const buttons = await page.evaluate(() => {
      const btnElements = document.querySelectorAll('button, img, div[class*="button"]');
      return Array.from(btnElements).map(el => {
        return {
          tagName: el.tagName,
          className: el.className,
          title: el.getAttribute('title') || '',
          alt: el.getAttribute('alt') || '',
          ariaLabel: el.getAttribute('aria-label') || '',
          text: el.innerText || ''
        };
      });
    });
    
    console.log('Found buttons/elements on page:');
    const stageHeaderButtons = buttons.filter(b => {
      const cls = b.className.toLowerCase();
      const title = b.title.toLowerCase();
      const alt = b.alt.toLowerCase();
      const label = b.ariaLabel.toLowerCase();
      return cls.includes('stage') || title.includes('screen') || alt.includes('screen') || label.includes('screen');
    });
    console.log(stageHeaderButtons);
  } catch (err) {
    console.error('Error:', err.message);
  } finally {
    await browser.close();
  }
})();
