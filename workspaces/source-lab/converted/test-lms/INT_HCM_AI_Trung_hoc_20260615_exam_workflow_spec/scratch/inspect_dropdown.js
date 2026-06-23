const { chromium } = require('playwright');

(async () => {
  console.log('Khởi chạy Chromium...');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  console.log('Mở trang PRG AI Blocks...');
  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'networkidle',
    timeout: 90000
  });
  
  await page.waitForTimeout(6000);

  // Nạp Face Sensing
  console.log('Nạp extension Face Sensing...');
  const extBtn = await page.$('[class^="gui_extension-button"]');
  if (extBtn) {
    await extBtn.click();
    await page.waitForTimeout(2000);
    const card = page.locator('[class*="library-item_library-item"]').filter({ hasText: 'Face Sensing' }).first();
    await card.click();
    await page.waitForTimeout(6000);
  }

  // Inject một kịch bản XML đơn giản có khối go to face part
  console.log('Injecting XML test...');
  await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    ws.clear();
    const xmlStr = `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="poseFace_affdexGoToPart" id="test_goto" x="40" y="40">
        <field name="AFFDEX_POINT">0</field>
      </block>
    </xml>`;
    const dom = B.Xml.textToDom(xmlStr);
    B.Xml.domToWorkspace(dom, ws);
    ws.render();
  });

  // Click chuột phải vào workspace (vùng trống, ví dụ tại tọa độ x=300, y=300)
  console.log('Click chuột phải vào workspace...');
  const workspaceEl = await page.$('.blocklySvg');
  if (workspaceEl) {
    // Click chuột phải tại vị trí x=300, y=300 trên SVG canvas để tránh click trúng block ở x=40, y=40
    await workspaceEl.click({ button: 'right', position: { x: 300, y: 300 }, force: true });
    await page.waitForTimeout(1000);
    
    // Đọc các tùy chọn trong context menu
    const menuText = await page.evaluate(() => {
      const menu = document.querySelector('.blocklyContextMenu');
      if (!menu) return 'Không tìm thấy .blocklyContextMenu';
      
      const items = menu.querySelectorAll('.goog-menuitem');
      const results = [];
      items.forEach(item => {
        results.push(item.textContent ? item.textContent.trim() : '');
      });
      return results;
    });
    
    console.log('CÁC TÙY CHỌN TRONG CONTEXT MENU CỦA WORKSPACE:');
    console.log(menuText);
  } else {
    console.log('Không tìm thấy element .blocklySvg');
  }

  await browser.close();
})();
