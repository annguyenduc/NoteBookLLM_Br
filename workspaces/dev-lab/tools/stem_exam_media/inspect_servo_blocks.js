/**
 * inspect_servo_blocks.js
 * Kiểm tra cấu trúc fields và inputs của các block servo để viết XML chính xác.
 */

const fs = require('fs');
const path = require('path');

const OUT_DIR = path.join(__dirname, 'inspect_out');
fs.mkdirSync(OUT_DIR, { recursive: true });

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

  // Mở mở rộng Rover
  await page.evaluate(() => {
    const ext = Array.from(document.querySelectorAll('a, button, .toolbox-category')).find(el => el.textContent.includes('MỞ RỘNG'));
    if (ext) ext.click();
  });
  await page.waitForTimeout(3000);
  await page.evaluate(() => {
    const rover = Array.from(document.querySelectorAll('.extension-card, .card')).find(el => el.textContent.toLowerCase().includes('rover'));
    if (rover) rover.click();
  });
  await page.waitForTimeout(4000);

  const blockData = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    const targets = [
      'block_move_servo',
      'yolobit_pin_servo_write_angle'
    ];
    const results = {};
    for (const type of targets) {
      try {
        const b = ws.newBlock(type);
        const fields = b.inputList.flatMap(i => i.fieldRow).map(f => ({
          name: f.name,
          value: f.getValue(),
          options: f.getOptions ? f.getOptions() : null
        }));
        const inputs = b.inputList.map(i => ({ name: i.name, type: i.type }));
        results[type] = { fields, inputs };
        b.dispose();
      } catch(e) {
        results[type] = { error: e.message };
      }
    }
    return results;
  });

  console.log('Block Data:', JSON.stringify(blockData, null, 2));
  fs.writeFileSync(path.join(OUT_DIR, 'servo_blocks.json'), JSON.stringify(blockData, null, 2));
  await browser.close();
}

main().catch(console.error);
