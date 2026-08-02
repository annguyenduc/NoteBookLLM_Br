/**
 * test_move_10s.js
 * Kiểm thử nạp XML "Di chuyển tới trong 10s rồi dừng lại"
 * lên OhStem App xem có sinh mã Python chính xác không.
 */

const fs = require('path');
const fsExtra = require('fs');

const xmlText = `<xml xmlns="https://developers.google.com/blockly/xml">
  <block type="yolobit_input_on_button_pressed" x="40" y="40">
    <field name="button">a</field>
    <statement name="NAME">
      <block type="robotics_robot_move">
        <field name="direction">forward</field>
        <next>
          <block type="yolobit_basic_delay">
            <value name="time">
              <shadow type="math_number">
                <field name="NUM">10000</field>
              </shadow>
            </value>
            <next>
              <block type="robotics_robot_stop"></block>
            </next>
          </block>
        </next>
      </block>
    </statement>
  </block>
</xml>`;

async function clickVisible(page, selector) {
  await page.evaluate((sel) => {
    const el = Array.from(document.querySelectorAll(sel)).find((node) => {
      const rect = node.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0;
    });
    if (!el) throw new Error(`Không tìm thấy: ${sel}`);
    el.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
  }, selector);
}

async function main() {
  const pkgDir = process.env.PLAYWRIGHT_PKG_DIR;
  const { chromium } = require(pkgDir);
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  console.log('[1] Loading home...');
  await page.goto('https://app.ohstem.vn', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(5000);

  console.log('[2] Click device Yolobit...');
  await clickVisible(page, 'a[href="/devices/yolobit"]');
  await page.waitForTimeout(5000);

  console.log('[3] Click coding...');
  await clickVisible(page, 'a[href="/codes/yolobit"]');

  console.log('[4] Wait Blockly...');
  await page.waitForFunction(() =>
    window.Blockly && window.Blockly.getMainWorkspace && window.Blockly.getMainWorkspace(),
    { timeout: 90000 }
  );
  await page.waitForTimeout(10000);

  console.log('[5] Mở rộng Rover...');
  try {
    await clickVisible(page, 'a[href="/extensions/yolobit"]');
    await page.waitForTimeout(2000);
  } catch {
    await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button, .toolbox-category'));
      const extBtn = btns.find(b => b.textContent && b.textContent.includes('MỞ RỘNG'));
      if (extBtn) extBtn.click();
    });
    await page.waitForTimeout(2000);
  }

  await page.evaluate(() => {
    const cards = Array.from(document.querySelectorAll('.extension-card, .card, [class*="extension"]'));
    const rover = cards.find(c => c.textContent && c.textContent.toLowerCase().includes('rover'));
    if (rover) rover.click();
  });
  await page.waitForTimeout(3000);

  await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button'));
    const skip = btns.find(b => b.textContent && (b.textContent.includes('Bỏ qua') || b.textContent.includes('Skip') || b.textContent.includes('OK')));
    if (skip) skip.click();
  });
  await page.waitForTimeout(4000);

  console.log('[5.5] Đợi tất cả các block được định nghĩa đầy đủ...');
  await page.waitForFunction(() =>
    window.Blockly &&
    window.Blockly.Blocks &&
    window.Blockly.Blocks['yolobit_basic_delay'] &&
    window.Blockly.Blocks['robotics_robot_move'] &&
    window.Blockly.getMainWorkspace(),
    { timeout: 30000 }
  );
  await page.waitForTimeout(3000);

  console.log('[6] Injecting Move 10s XML...');
  const result = await page.evaluate((xmlStr) => {
    try {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      
      let dom;
      if (B.utils && B.utils.xml && typeof B.utils.xml.textToDom === 'function') {
        dom = B.utils.xml.textToDom(xmlStr);
      } else {
        dom = B.Xml.textToDom(xmlStr);
      }

      B.Xml.domToWorkspace(dom, ws);
      ws.render();
      ws.cleanUp();
      return { ok: true, error: null };
    } catch(e) {
      return { ok: false, error: e.stack || e.message };
    }
  }, xmlText);

  console.log('[7] XML status:', JSON.stringify(result));

  console.log('[8] Switching to Python tab...');
  await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button, .tab, [role="tab"]'));
    const pyTab = btns.find(b => b.textContent && b.textContent.trim() === 'Python');
    if (pyTab) pyTab.click();
  });
  await page.waitForTimeout(3000);

  const pyCode = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    if (B.Python && typeof B.Python.workspaceToCode === 'function') {
      return B.Python.workspaceToCode(ws);
    }
    return 'Generator failed';
  });

  console.log('[9] Generated Python:\n', pyCode);
  
  const OUT_DIR = fs.join(__dirname, 'inspect_out');
  fsExtra.writeFileSync(fs.join(OUT_DIR, 'generated_python_move_10s.py'), pyCode, 'utf8');
  await page.screenshot({ path: fs.join(OUT_DIR, 'move_10s_rendered.png') });
  await browser.close();

  if (!result.ok) {
    console.error('XML Injection FAILED!');
    process.exit(1);
  } else {
    console.log('XML Injection PASSED!');
  }
}

main().catch(e => {
  console.error(e);
  process.exit(1);
});
