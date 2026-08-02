/**
 * test_manual_logic.js
 * Kiểm thử XML chứa logic dò line thủ công (so sánh S1-S4 và điều khiển speed ratio + move)
 * đảm bảo nạp thành công 100% không lỗi trên OhStem.
 */

const fs = require('path');
const fsExtra = require('fs');

const xmlText = `<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="ngaTu_var">ngaTu</variable>
  </variables>
  <block type="yolobit_input_on_button_pressed" x="40" y="40">
    <field name="button">a</field>
    <statement name="NAME">
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
              <block type="controls_if">
                <mutation elseif="4" else="1"></mutation>
                
                <!-- TRƯỜNG HỢP 1: NGÃ TƯ (Cả S1 và S4 cùng chạm vạch đen) -->
                <value name="IF0">
                  <block type="logic_operation">
                    <field name="OP">AND</field>
                    <value name="A">
                      <block type="robotics_line_sensor_read">
                        <field name="sensor">0</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="robotics_line_sensor_read">
                        <field name="sensor">3</field>
                      </block>
                    </value>
                  </block>
                </value>
                <statement name="DO0">
                  <!-- Đếm ngã tư -->
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
                          <!-- Đi thẳng qua ngã tư trong 0.4s -->
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
                </statement>

                <!-- TRƯỜNG HỢP 2: LỆCH TRÁI NHẸ (Mắt S2 đè vạch đen) -->
                <value name="IF1">
                  <block type="robotics_line_sensor_read">
                    <field name="sensor">1</field>
                  </block>
                </value>
                <statement name="DO1">
                  <!-- Rẽ trái nhẹ: left speed = 35, right speed = 60 -->
                  <block type="robotics_robot_set_speed_ratio">
                    <value name="left">
                      <shadow type="math_number">
                        <field name="NUM">35</field>
                      </shadow>
                    </value>
                    <value name="right">
                      <shadow type="math_number">
                        <field name="NUM">60</field>
                      </shadow>
                    </value>
                    <next>
                      <block type="robotics_robot_move">
                        <field name="direction">forward</field>
                      </block>
                    </next>
                  </block>
                </statement>

                <!-- TRƯỜNG HỢP 3: LỆCH PHẢI NHẸ (Mắt S3 đè vạch đen) -->
                <value name="IF2">
                  <block type="robotics_line_sensor_read">
                    <field name="sensor">2</field>
                  </block>
                </value>
                <statement name="DO2">
                  <!-- Rẽ phải nhẹ: left speed = 60, right speed = 35 -->
                  <block type="robotics_robot_set_speed_ratio">
                    <value name="left">
                      <shadow type="math_number">
                        <field name="NUM">60</field>
                      </shadow>
                    </value>
                    <value name="right">
                      <shadow type="math_number">
                        <field name="NUM">35</field>
                      </shadow>
                    </value>
                    <next>
                      <block type="robotics_robot_move">
                        <field name="direction">forward</field>
                      </block>
                    </next>
                  </block>
                </statement>

                <!-- TRƯỜNG HỢP 4: LỆCH TRÁI NHIỀU (Mắt S1 ngoài cùng đè vạch đen) -->
                <value name="IF3">
                  <block type="robotics_line_sensor_read">
                    <field name="sensor">0</field>
                  </block>
                </value>
                <statement name="DO3">
                  <!-- Rẽ trái gấp: left speed = -20, right speed = 60 -->
                  <block type="robotics_robot_set_speed_ratio">
                    <value name="left">
                      <shadow type="math_number">
                        <field name="NUM">-20</field>
                      </shadow>
                    </value>
                    <value name="right">
                      <shadow type="math_number">
                        <field name="NUM">60</field>
                      </shadow>
                    </value>
                    <next>
                      <block type="robotics_robot_move">
                        <field name="direction">forward</field>
                      </block>
                    </next>
                  </block>
                </statement>

                <!-- TRƯỜNG HỢP 5: LỆCH PHẢI NHIỀU (Mắt S4 ngoài cùng đè vạch đen) -->
                <value name="IF4">
                  <block type="robotics_line_sensor_read">
                    <field name="sensor">3</field>
                  </block>
                </value>
                <statement name="DO4">
                  <!-- Rẽ phải gấp: left speed = 60, right speed = -20 -->
                  <block type="robotics_robot_set_speed_ratio">
                    <value name="left">
                      <shadow type="math_number">
                        <field name="NUM">60</field>
                      </shadow>
                    </value>
                    <value name="right">
                      <shadow type="math_number">
                        <field name="NUM">-20</field>
                      </shadow>
                    </value>
                    <next>
                      <block type="robotics_robot_move">
                        <field name="direction">forward</field>
                      </block>
                    </next>
                  </block>
                </statement>

                <!-- MẶC ĐỊNH: ĐI THẲNG -->
                <statement name="ELSE">
                  <block type="robotics_robot_set_speed_ratio">
                    <value name="left">
                      <shadow type="math_number">
                        <field name="NUM">60</field>
                      </shadow>
                    </value>
                    <value name="right">
                      <shadow type="math_number">
                        <field name="NUM">60</field>
                      </shadow>
                    </value>
                    <next>
                      <block type="robotics_robot_move">
                        <field name="direction">forward</field>
                      </block>
                    </next>
                  </block>
                </statement>

              </block>
            </statement>
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
  await page.waitForTimeout(2000);

  console.log('[6] Injecting Manual Logic XML...');
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
  
  const OUT_DIR = fs.join(__dirname, 'manual_xml_out');
  fsExtra.writeFileSync(fs.join(OUT_DIR, 'generated_python.py'), pyCode, 'utf8');
  await page.screenshot({ path: fs.join(OUT_DIR, 'manual_logic_rendered.png') });
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
