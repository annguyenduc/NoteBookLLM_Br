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
      console.log(`Loaded ${name}`);
    }
  };

  await loadExtension('Teachable Machine');
  await loadExtension('Face Sensing');
  await loadExtension('Body Sensing');

  const info = await page.evaluate(() => {
    const ws = window.Blockly.getMainWorkspace();
    if (!ws) return { error: 'No workspace' };
    
    // Tìm các thuộc tính của ws
    const wsKeys = Object.keys(ws);
    
    // Kiểm tra toolbox
    const toolboxInfo = ws.toolbox_ ? {
      keys: Object.keys(ws.toolbox_),
      // Thử tìm các thuộc tính chứa XML hoặc string
      xmlString: ws.toolbox_.toolboxXml_ ? ws.toolbox_.toolboxXml_.outerHTML : null,
      languageTree: ws.options && ws.options.languageTree ? ws.options.languageTree.outerHTML : null
    } : 'No ws.toolbox_';

    // Kiểm tra flyout (nếu Scratch dùng flyout trực tiếp thay vì toolbox dạng cột)
    const flyoutInfo = ws.flyout_ ? {
      keys: Object.keys(ws.flyout_)
    } : 'No ws.flyout_';

    // Tìm kiếm các block được đăng ký trong hệ thống thông qua Blockly
    // Mặc dù window.Blockly.Blocks không tồn tại trực tiếp, hãy thử tìm xem Blockly.Blocks có nằm ở chỗ khác không
    // Ví dụ: trong window.Blockly.getMainWorkspace().getFlyout().getWorkspace().getTopBlocks()
    return {
      wsKeys,
      toolboxInfo,
      flyoutInfo,
      optionsKeys: ws.options ? Object.keys(ws.options) : []
    };
  });

  console.log('Workspace Info:', JSON.stringify(info, null, 2));
  await browser.close();
})();
