const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForSelector('.blocklySvg', { timeout: 30000 });
  await page.waitForTimeout(2000);
  
  const xml = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    ws.clear();
    
    // Tạo một biến list bằng code
    // Trong Scratch blocks: B.Variables.createVariable(ws, id, name, type)
    // Hoặc ws.createVariable(name, type, id)
    const listVar = ws.createVariable('Nhật ký cảm xúc', 'list', 'q28_list_diary');
    
    // Tạo block data_deletealloflist
    const block = ws.newBlock('data_deletealloflist');
    block.initSvg();
    block.render();
    
    // Gán biến list vào field LIST của block
    const field = block.getField('LIST');
    if (field) {
      field.setValue('q28_list_diary');
    }
    
    const dom = B.Xml.workspaceToDom(ws);
    return new XMLSerializer().serializeToString(dom);
  });

  console.log('List Block XML Structure:', xml);
  await browser.close();
})();
