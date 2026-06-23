const { chromium } = require('playwright');
const fs = require('fs');

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

  console.log('Loading Face Sensing and Body Sensing extensions...');
  try {
    // Open library and load Face Sensing
    await page.click('[class*="extension-button"]');
    await page.waitForTimeout(1000);
    await page.locator('text="Face Sensing"').first().click();
    await page.waitForTimeout(4000);

    // Open library and load Body Sensing
    await page.click('[class*="extension-button"]');
    await page.waitForTimeout(1000);
    await page.locator('text="Body Sensing"').first().click();
    await page.waitForTimeout(4000);
  } catch (e) {
    console.log('Extensions load failed:', e.message);
  }

  const toolboxXmls = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    
    // In Scratch-blocks, the toolbox XML is typically stored in B.Variables or ws.getToolbox() or ws.options.languageTree
    // Let's inspect ws.options.languageTree which holds the full toolbox DOM tree.
    if (ws.options && ws.options.languageTree) {
      const serializer = new XMLSerializer();
      
      // Let's find categories in the languageTree
      const xmlDom = ws.options.languageTree;
      const categories = Array.from(xmlDom.querySelectorAll('category'));
      const catXmls = {};
      
      categories.forEach(cat => {
        const id = cat.getAttribute('id') || cat.getAttribute('name');
        catXmls[id] = serializer.serializeToString(cat);
      });
      
      return catXmls;
    }
    return { error: 'options.languageTree not found' };
  });

  let output = '';
  for (const catId in toolboxXmls) {
    if (catId === 'poseFace' || catId === 'poseBody') {
      output += `\n=== Category: ${catId} ===\n${toolboxXmls[catId]}\n`;
    }
  }
  fs.writeFileSync('D:\\_agent_worktrees\\20260619_exam_ai_thcs_media\\.agent\\runs\\exam_ai_thcs_media\\probe\\toolbox_details.xml', output, 'utf8');
  console.log('Saved to toolbox_details.xml');
  await browser.close();
})();
