const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForSelector('.blocklySvg', { timeout: 30000 });
  await page.waitForTimeout(2000);
  
  // Nạp Face Sensing
  const extBtn = await page.$('[class^="gui_extension-button"]');
  if (extBtn) {
    await extBtn.click();
    await page.waitForTimeout(2000);
    await page.click('div[class*="library-item_library-item"]:has-text("Face Sensing")');
    await page.waitForTimeout(5000);
  }
  
  // Lấy các options của trường AFFDEX_POINT
  const options = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    ws.clear();
    
    // Inject thử một block mặc định để lấy field
    const xmlText = `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="poseFace_affdexGoToPart" id="test_block" x="40" y="40">
        <field name="AFFDEX_POINT">0</field>
      </block>
    </xml>`;
    
    const dom = B.Xml.textToDom(xmlText);
    B.Xml.domToWorkspace(dom, ws);
    ws.render();
    
    const block = ws.getTopBlocks()[0];
    if (!block) return 'No block found';
    const field = block.getField('AFFDEX_POINT');
    if (!field) return 'No field found';
    
    // Lấy các options
    return field.getOptions ? field.getOptions() : 'getFieldOptions not a function';
  });
  
  console.log('Dropdown Options for AFFDEX_POINT:', JSON.stringify(options, null, 2));
  await browser.close();
})();
