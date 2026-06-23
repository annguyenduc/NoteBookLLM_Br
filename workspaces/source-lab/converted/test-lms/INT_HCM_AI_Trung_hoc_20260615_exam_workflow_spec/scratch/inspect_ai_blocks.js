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
      
      // Sử dụng locator chính xác cho card trong modal của Scratch
      const card = page.locator('[class*="library-item_library-item"]').filter({ hasText: name }).first();
      await card.click();
      await page.waitForTimeout(5000); // Đợi model load
      console.log(`Loaded ${name} successfully.`);
    }
  };

  await loadExtension('Teachable Machine');
  await loadExtension('Face Sensing');
  await loadExtension('Body Sensing');

  const info = await page.evaluate(() => {
    const B = window.Blockly;
    if (!B) return { error: 'window.Blockly undefined' };
    
    // Tìm các block types trong Blockly.Blocks nếu có hoặc trong workspace
    // Khoan đã, nếu B.Blocks bị undefined như lúc nãy, ta có thể lấy danh sách block type từ XML hoặc từ workspace?
    // Thử lấy danh sách block type từ Blockly.Blocks nếu nó tồn tại
    // Chờ chút, lúc nãy lỗi: B.Blocks undefined. Nhưng trên thực tế, trong Scratch blocks, 
    // Blockly.Blocks có thể nằm dưới window.Blockly.Blocks? Hãy check xem window.Blockly.Blocks có tồn tại không.
    // Nếu không, ta kiểm tra xem B có các thuộc tính nào khác không.
    return {
      error: null,
      blocklyBlocksExist: typeof window.Blockly.Blocks !== 'undefined',
      blocksKeys: typeof window.Blockly.Blocks !== 'undefined' ? Object.keys(window.Blockly.Blocks).filter(k => 
        k.toLowerCase().includes('teachable') || 
        k.toLowerCase().includes('tm2') || 
        k.toLowerCase().includes('face') || 
        k.toLowerCase().includes('body') || 
        k.toLowerCase().includes('pose')
      ) : []
    };
  });
  
  console.log('AI Block Info:', JSON.stringify(info, null, 2));
  await browser.close();
})();
