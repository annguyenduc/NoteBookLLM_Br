const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  console.log('Launching browser...');
  const browser = await chromium.launch({
    headless: true,
    args: [
      '--use-fake-ui-for-media-stream',
      '--use-fake-device-for-media-stream'
    ]
  });
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

  console.log('Navigating to playground...');
  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'domcontentloaded', timeout: 90000
  });

  await page.waitForFunction(() =>
    window.Blockly &&
    typeof window.Blockly.getMainWorkspace === 'function' &&
    window.Blockly.getMainWorkspace()
  , { timeout: 90000 });

  await page.waitForTimeout(3000);

  console.log('Opening extension library...');
  try {
    await page.click('[class*="extension-button"]');
    await page.waitForTimeout(2000);
    
    console.log('Clicking Teachable Machine...');
    const card = page.locator('[class*="library-item"]').filter({ hasText: 'Teachable Machine' }).first();
    await card.scrollIntoViewIfNeeded({ timeout: 3000 });
    await card.click({ timeout: 5000 });
    
    console.log('Waiting for Teachable Machine model loading (7 seconds)...');
    await page.waitForTimeout(7000);
  } catch (e) {
    console.error('Error loading extension:', e.message);
  }

  // Dump categories
  const categoriesData = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    if (!ws.options || !ws.options.languageTree) {
      return { error: 'languageTree not found' };
    }
    
    const serializer = new XMLSerializer();
    const xmlDom = ws.options.languageTree;
    const categories = Array.from(xmlDom.querySelectorAll('category'));
    const result = [];
    
    categories.forEach(cat => {
      const name = cat.getAttribute('name');
      const id = cat.getAttribute('id');
      const xml = serializer.serializeToString(cat);
      result.push({ name, id, xml });
    });
    
    return result;
  });

  if (categoriesData.error) {
    console.error(categoriesData.error);
  } else {
    console.log('\n--- Registered Categories ---');
    categoriesData.forEach(c => {
      console.log(`Name: ${c.name}, ID: ${c.id}`);
      if (c.name.toLowerCase().includes('teachable') || c.id.toLowerCase().includes('teachable') || c.id.toLowerCase().includes('tm')) {
        console.log('XML Content:\n', c.xml);
      }
    });
    
    // Save all to a JSON file for detailed review if needed
    fs.writeFileSync(path.join(__dirname, 'tm_categories.json'), JSON.stringify(categoriesData, null, 2), 'utf8');
    console.log('Saved categories to tm_categories.json');
  }

  await browser.close();
})();
