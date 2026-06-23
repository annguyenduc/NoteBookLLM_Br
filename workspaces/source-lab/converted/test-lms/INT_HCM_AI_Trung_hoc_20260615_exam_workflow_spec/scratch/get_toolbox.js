const { chromium } = require('playwright');
const fs = require('fs');

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

  const toolboxXml = await page.evaluate(() => {
    const ws = window.Blockly.getMainWorkspace();
    if (!ws || !ws.toolbox_) return 'No workspace or toolbox';
    const xmlNode = ws.toolbox_.toolboxXml_;
    return xmlNode ? new XMLSerializer().serializeToString(xmlNode) : 'No XML node';
  });
  
  fs.writeFileSync('toolbox.xml', toolboxXml, 'utf8');
  console.log('Saved toolbox.xml successfully!');
  await browser.close();
})();
