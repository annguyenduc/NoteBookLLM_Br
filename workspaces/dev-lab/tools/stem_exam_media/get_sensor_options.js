/**
 * get_sensor_options.js
 * Lấy các tùy chọn thực tế của FieldDropdown 'sensor' trong block 'robotics_line_sensor_read'.
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

  const options = await page.evaluate(() => {
    try {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      const b = ws.newBlock("robotics_line_sensor_read");
      const field = b.getField("sensor");
      const opts = field.getOptions();
      b.dispose();
      return { ok: true, opts };
    } catch(e) {
      return { ok: false, error: e.message };
    }
  });

  console.log('Sensor Options Result:', JSON.stringify(options, null, 2));
  await browser.close();
}

main().catch(console.error);
