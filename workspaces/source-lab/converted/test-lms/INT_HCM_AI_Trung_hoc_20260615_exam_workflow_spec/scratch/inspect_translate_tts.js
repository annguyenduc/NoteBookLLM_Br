const { chromium } = require('playwright');

(async () => {
  console.log('Khởi chạy Chromium...');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForSelector('.blocklySvg', { timeout: 30000 });
  await page.waitForTimeout(2000);
  
  const loadExtension = async (name) => {
    console.log(`Đang nạp extension: ${name}...`);
    const extBtn = await page.$('[class^="gui_extension-button"]');
    if (extBtn) {
      await extBtn.click();
      await page.waitForTimeout(2000);
      const card = page.locator('[class*="library-item_library-item"]').filter({ hasText: name }).first();
      await card.click();
      await page.waitForTimeout(4000);
      console.log(`Nạp xong ${name}`);
    }
  };

  await loadExtension('Translate');
  await loadExtension('Text to Speech');

  const toolboxXml = await page.evaluate(() => {
    // Lấy toolbox XML
    const ws = window.Blockly.getMainWorkspace();
    const toolbox = ws.toolbox_;
    if (!toolbox) return 'No toolbox';
    
    // Tìm các block trong toolbox
    const categories = Array.from(document.querySelectorAll('.blocklyToolboxDiv .blocklyTreeRow'));
    const info = categories.map(cat => cat.textContent.trim());
    
    // Trích xuất languageTree của workspace
    const languageTree = ws.options && ws.options.languageTree ? ws.options.languageTree : null;
    if (!languageTree) return 'No language tree';
    
    // Tìm các block của Translate và Text to Speech trong languageTree
    const serializer = new XMLSerializer();
    const xmlStr = serializer.serializeToString(languageTree);
    return xmlStr;
  });

  // Tìm các block chứa translate hoặc speech
  const fs = require('fs');
  const path = require('path');
  const outPath = path.join(__dirname, 'toolbox_tree.xml');
  fs.writeFileSync(outPath, toolboxXml, 'utf8');
  console.log('Đã lưu language tree của toolbox vào: toolbox_tree.xml');

  // Lọc lấy các khối của translate và text2speech để hiển thị
  const lines = toolboxXml.split('\n');
  const matched = [];
  let recording = false;
  let blockCount = 0;
  
  const blocks = [];
  const parser = new (require('xmldom').DOMParser)();
  const doc = parser.parseFromString(toolboxXml, 'text/xml');
  const categoryNodes = doc.getElementsByTagName('category');
  
  for (let i = 0; i < categoryNodes.length; i++) {
    const cat = categoryNodes[i];
    const name = cat.getAttribute('name');
    const id = cat.getAttribute('id');
    if (name === 'Translate' || name === 'Text to Speech' || id === 'translate' || id === 'text2speech') {
      console.log(`\n--- Category: ${name || id} ---`);
      const blockElements = cat.getElementsByTagName('block');
      for (let j = 0; j < blockElements.length; j++) {
        console.log(serializer.serializeToString(blockElements[j]));
      }
    }
  }

  await browser.close();
})();
