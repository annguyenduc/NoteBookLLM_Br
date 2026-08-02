/**
 * get_yolobit_basic_blocks.js
 * Tìm kiếm tất cả các block trong danh sách có chữ "tạm dừng" hoặc thuộc nhóm Cơ bản/BASIC.
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

  const basicBlocks = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    const allTypes = Object.keys(B.Blocks);
    const results = [];
    for (const type of allTypes) {
      if (type.startsWith('yolobit_basic_') || type.includes('delay') || type.includes('sleep') || type.includes('wait')) {
        try {
          const b = ws.newBlock(type);
          const fields = b.inputList.flatMap(i => i.fieldRow).map(f => ({ name: f.name, value: f.getValue() }));
          const label = b.toString ? b.toString() : '';
          results.push({ type, label, fields });
          b.dispose();
        } catch(e) {
          results.push({ type, error: e.message });
        }
      }
    }
    return results;
  });

  console.log('Basic/Delay Blocks:', JSON.stringify(basicBlocks, null, 2));
  await browser.close();
}

main().catch(console.error);
