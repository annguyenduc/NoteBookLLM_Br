/**
 * test_and_dump_python.js
 * Mở Yolobit workspace, thêm extension Rover, nạp XML,
 * và click tab Python để xem đoạn code Python sinh ra từ blocks.
 *
 * Usage:
 *   $env:PLAYWRIGHT_PKG_DIR = "C:\Users\anngu\AppData\Local\npm-cache\_npx\e41f203b7505f1fb\node_modules\playwright"
 *   node workspaces\dev-lab\tools\stem_exam_media\test_and_dump_python.js
 */

const fs = require('fs');
const path = require('path');

const OUT_DIR = path.join(__dirname, 'python_test_out');
fs.mkdirSync(OUT_DIR, { recursive: true });

const xmlText = `<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="ngaTu_var">ngaTu</variable>
  </variables>
  <block type="yolobit_input_on_button_pressed" x="40" y="40">
    <field name="button">a</field>
    <statement name="NAME">
      <block type="yolobit_basic_scroll_text">
        <value name="message">
          <shadow type="text">
            <field name="TEXT">GO</field>
          </shadow>
        </value>
        <next>
          <block type="variables_set">
            <field name="VAR" id="ngaTu_var">ngaTu</field>
            <value name="VALUE">
              <shadow type="math_number">
                <field name="NUM">0</field>
              </shadow>
            </value>
            <next>
              <block type="block_control_forever">
                <statement name="FOREVER">
                  <block type="robotics_follow_line_until_cross">
                    <field name="then">STOP</field>
                    <next>
                      <block type="variables_set">
                        <field name="VAR" id="ngaTu_var">ngaTu</field>
                        <value name="VALUE">
                          <block type="math_arithmetic">
                            <field name="OP">ADD</field>
                            <value name="A">
                              <block type="variables_get">
                                <field name="VAR" id="ngaTu_var">ngaTu</field>
                              </block>
                            </value>
                            <value name="B">
                              <shadow type="math_number">
                                <field name="NUM">1</field>
                              </shadow>
                            </value>
                          </block>
                        </value>
                        <next>
                          <block type="yolobit_basic_scroll_number">
                            <value name="message">
                              <block type="variables_get">
                                <field name="VAR" id="ngaTu_var">ngaTu</field>
                              </block>
                            </value>
                            <next>
                              <block type="robotics_follow_line_by_time">
                                <field name="then">STOP</field>
                                <value name="time">
                                  <shadow type="math_number">
                                    <field name="NUM">0.4</field>
                                  </shadow>
                                </value>
                              </block>
                            </next>
                          </block>
                        </next>
                      </block>
                    </next>
                  </block>
                </statement>
              </block>
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
    if (!el) throw new Error(`Không tìm thấy element: ${sel}`);
    el.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
  }, selector);
}

async function main() {
  const pkgDir = process.env.PLAYWRIGHT_PKG_DIR;
  if (!pkgDir) throw new Error('PLAYWRIGHT_PKG_DIR required');

  const { chromium } = require(pkgDir);
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  // 1. Home
  console.log('[1] Loading home...');
  for (let r = 0; r < 3; r++) {
    try {
      await page.goto('https://app.ohstem.vn', { waitUntil: 'domcontentloaded', timeout: 60000 });
      break;
    } catch(e) {
      console.log(`  retry ${r+1}: ${e.message}`);
      await page.waitForTimeout(3000);
    }
  }
  await page.waitForTimeout(4000);

  // 2. Yolobit
  console.log('[2] Click device Yolobit...');
  await clickVisible(page, 'a[href="/devices/yolobit"]');
  await page.waitForTimeout(5000);

  // 3. Coding
  console.log('[3] Click coding...');
  await clickVisible(page, 'a[href="/codes/yolobit"]');

  // 4. Wait
  console.log('[4] Wait Blockly...');
  await page.waitForFunction(() =>
    window.Blockly && window.Blockly.getMainWorkspace && window.Blockly.getMainWorkspace(),
    { timeout: 90000 }
  );
  await page.waitForTimeout(10000);

  // 5. Thêm extension Rover
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

  // Click Rover Card
  await page.evaluate(() => {
    const cards = Array.from(document.querySelectorAll('.extension-card, .card, [class*="extension"]'));
    const rover = cards.find(c => c.textContent && c.textContent.toLowerCase().includes('rover'));
    if (rover) rover.click();
  });
  await page.waitForTimeout(3000);

  // Skip popup
  await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button'));
    const skip = btns.find(b => b.textContent && (b.textContent.includes('Bỏ qua') || b.textContent.includes('Skip') || b.textContent.includes('OK')));
    if (skip) skip.click();
  });
  await page.waitForTimeout(2000);

  // 6. Inject XML
  console.log('[6] Injecting XML...');
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

  // 7. Click Python tab to see generated Python code
  console.log('[8] Switching to Python tab...');
  await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button, .tab, [role="tab"]'));
    // Tìm tab có text "Python"
    const pyTab = btns.find(b => b.textContent && b.textContent.trim() === 'Python');
    if (pyTab) {
      pyTab.click();
      return true;
    }
    return false;
  });
  await page.waitForTimeout(3000);

  // Đọc nội dung mã Python sinh ra
  const pyCode = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    // Thử lấy trực tiếp từ generator
    if (B.Python && typeof B.Python.workspaceToCode === 'function') {
      return B.Python.workspaceToCode(ws);
    }
    // Hoặc thử lấy từ editor DOM
    const editor = document.querySelector('.ace_content, .cm-content, textarea');
    if (editor) return editor.textContent || editor.value;
    return 'Không tìm thấy trình biên dịch hoặc editor';
  });

  console.log('[9] Generated Python:\n', pyCode);
  fs.writeFileSync(path.join(OUT_DIR, 'generated_python.py'), pyCode, 'utf8');

  await page.screenshot({ path: path.join(OUT_DIR, 'python_tab_active.png') });
  await browser.close();
}

main().catch(e => {
  console.error(e);
  process.exit(1);
});
