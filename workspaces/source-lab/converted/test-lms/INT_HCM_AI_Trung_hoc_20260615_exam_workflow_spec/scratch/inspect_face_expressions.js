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

  const expressions = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    
    // Tìm cấu trúc khối poseFace_affdexIsExpression
    const block = ws.newBlock('poseFace_affdexIsExpression');
    if (!block) return 'Block not found';
    
    const input = block.getInput('EXPRESSION');
    if (!input) return 'Input EXPRESSION not found';
    
    // Nếu block có field dropdown trực tiếp
    const field = block.getField('EXPRESSION');
    if (field && typeof field.getOptions === 'function') {
      return field.getOptions();
    }
    
    // Nếu nó dùng shadow block menu
    // Hãy tìm block type poseFace_menu_EXPRESSION
    const menuBlock = ws.newBlock('poseFace_menu_EXPRESSION');
    if (menuBlock) {
      const menuField = menuBlock.getField('EXPRESSION');
      if (menuField && typeof menuField.getOptions === 'function') {
        return menuField.getOptions();
      }
    }
    
    return {
      blockFields: block.inputList.map(i => ({
        name: i.name,
        fields: i.fieldRow.map(f => ({ name: f.name, text: f.text_ }))
      }))
    };
  });

  console.log('Face Sensing Expressions:', JSON.stringify(expressions, null, 2));
  await browser.close();
})();
