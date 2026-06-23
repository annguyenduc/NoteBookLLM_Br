const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 60000 });
  await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace());
  
  // Load Face Sensing
  console.log("Loading Face Sensing...");
  const addExtBtn = await page.locator('[class*="gui_extension-button"]').first();
  if (await addExtBtn.count() > 0) {
    await addExtBtn.click();
    await page.waitForTimeout(2000);
    const faceSensingCard = page.locator('text="Face Sensing"').first();
    await faceSensingCard.click();
    await page.waitForTimeout(6000);
  }

  const xmlStr = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    const callbacks = ws.toolboxCategoryCallbacks_;
    
    // Tìm key category (không phân biệt chữ hoa chữ thường)
    let key = Object.keys(callbacks).find(k => k.toLowerCase() === 'face' || k.toLowerCase().includes('sensing'));
    if (!key) {
      // Thử tìm trong các category khác
      key = Object.keys(callbacks).find(k => callbacks[k]);
    }
    
    if (key && typeof callbacks[key] === 'function') {
      const xmlList = callbacks[key](ws);
      const parent = document.createElement('xml');
      xmlList.forEach(el => parent.appendChild(el.cloneNode(true)));
      return new XMLSerializer().serializeToString(parent);
    }
    
    return "Category callback not found. Keys: " + Object.keys(callbacks).join(', ');
  });
  
  console.log("Face sensing category XML:", xmlStr);
  fs.writeFileSync('face_sensing_toolbox.xml', xmlStr, 'utf8');

  await browser.close();
})();
