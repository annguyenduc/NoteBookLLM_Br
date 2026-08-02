/**
 * get_delay_input.js
 * Tìm tên input của block yolobit_basic_delay.
 */

const fs = require('fs');

async function main() {
  const pkgDir = process.env.PLAYWRIGHT_PKG_DIR;
  const { chromium } = require(pkgDir);
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  await page.goto('https://app.ohstem.vn', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(5000);
  await page.click('a[href="/devices/yolobit"]');
  await page.waitForTimeout(5000);
  await page.click('a[href="/codes/yolobit"]');
  
  await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace());
  await page.waitForTimeout(10000);

  const inputName = await page.evaluate(() => {
    try {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      const b = ws.newBlock("yolobit_basic_delay");
      const inputs = b.inputList.map(i => ({ name: i.name, type: i.type }));
      b.dispose();
      return { ok: true, inputs };
    } catch(e) {
      return { ok: false, error: e.message };
    }
  });

  console.log('Delay Input Result:', JSON.stringify(inputName, null, 2));
  await browser.close();
}

main().catch(console.error);
