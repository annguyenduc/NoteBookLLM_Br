/**
 * inspect_robot_movement_blocks.js
 * Kiểm tra cấu trúc inputs/fields của block robotics_robot_set_speed_ratio và robotics_robot_move
 * để biết cách viết XML chính xác không dùng biến motor.
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

  // Mở rộng Rover
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
      'robotics_robot_set_speed_ratio',
      'robotics_robot_move',
      'robotics_robot_stop'
    ];
    const results = {};
    for (const type of targets) {
      try {
        const b = ws.newBlock(type);
        const fields = b.inputList.flatMap(i => i.fieldRow).map(f => ({ name: f.name, value: f.getValue() }));
        const inputs = b.inputList.map(i => ({ name: i.name, type: i.type }));
        let python = '';
        if (B.Python) python = B.Python.workspaceToCode(ws);
        results[type] = { fields, inputs, python };
        b.dispose();
      } catch(e) {
        results[type] = { error: e.message };
      }
    }
    return results;
  });

  console.log('Block Data:', JSON.stringify(blockData, null, 2));
  fs.writeFileSync(path.join(OUT_DIR, 'movement_blocks.json'), JSON.stringify(blockData, null, 2));
  await browser.close();
}

main().catch(console.error);
