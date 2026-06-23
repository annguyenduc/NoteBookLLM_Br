const { chromium } = require('playwright');
(async () => {
  console.log('Scanning Scratch library sprites...');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  try {
    await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace());
    await page.waitForTimeout(3000);
    
    const addBtn = page.locator('button[aria-label="Choose a Sprite"]').or(page.locator('button[aria-label="Chọn một nhân vật"]')).first();
    await addBtn.click();
    await page.waitForTimeout(4000);
    
    const names = await page.evaluate(() => {
      const items = document.querySelectorAll('[class*="library-item_library-item"]');
      return Array.from(items).map(item => {
        const span = item.querySelector('[class*="library-item-name"]');
        return span ? span.innerText.trim() : '';
      }).filter(n => n !== '');
    });
    
    console.log(`Found ${names.length} sprites.`);
    console.log('Animal sprites or potential characters:');
    const matches = names.filter(name => {
      const n = name.toLowerCase();
      return n.includes('turtle') || n.includes('tortoise') || n.includes('rabbit') || n.includes('hare') || n.includes('snail') || n.includes('frog') || n.includes('hedgehog') || n.includes('dino') || n.includes('crab');
    });
    console.log(matches);
    
    console.log('\nFirst 60 sprites in library:');
    console.log(names.slice(0, 60));
  } catch (err) {
    console.error('Error scanning library:', err.message);
  } finally {
    await browser.close();
  }
})();
