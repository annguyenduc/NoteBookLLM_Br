/**
 * inspect_dropdown_fields.js
 * Kiểm tra tất cả các FieldDropdown của các block để xem giá trị chính xác là gì.
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

  const dropdowns = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    const targets = [
      'robotics_robot_move',
      'robotics_follow_line_until_cross',
      'robotics_follow_line_by_time'
    ];
    const results = {};
    for (const type of targets) {
      try {
        const b = ws.newBlock(type);
        results[type] = b.inputList.flatMap(i => i.fieldRow)
          .filter(f => f.getOptions)
          .map(f => ({ name: f.name, value: f.getValue(), options: f.getOptions() }));
        b.dispose();
      } catch(e) {
        results[type] = { error: e.message };
      }
    }
    return results;
  });

  console.log('Dropdown Fields Result:', JSON.stringify(dropdowns, null, 2));
  await browser.close();
}

main().catch(console.error);
