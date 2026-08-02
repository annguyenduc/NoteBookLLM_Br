/**
 * get_rover_python_playwright.js
 * Inject các block dò line của Robotics extension vào Yolobit workspace
 * và xuất Python code thực tế (headless).
 *
 * Usage:
 *   $env:PLAYWRIGHT_PKG_DIR = "C:\Users\anngu\AppData\Local\npm-cache\_npx\e41f203b7505f1fb\node_modules\playwright"
 *   node workspaces\dev-lab\tools\stem_exam_media\get_rover_python_playwright.js
 */

const fs   = require('fs');
const path = require('path');

const OUT_DIR = path.join(__dirname, 'rover_python_out');

async function waitBlockly(page, timeout = 90000) {
  await page.waitForFunction(() =>
    window.Blockly &&
    typeof window.Blockly.getMainWorkspace === 'function' &&
    window.Blockly.getMainWorkspace(),
  { timeout });
  await page.waitForTimeout(10000);
}

async function clickVisible(page, selector) {
  await page.evaluate((sel) => {
    const el = Array.from(document.querySelectorAll(sel))
      .find(n => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!el) throw new Error('Not found: ' + sel);
    el.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
  }, selector);
}

// ── Lấy Python code từ workspace hiện tại ──────────────────
async function getPythonCode(page) {
  return page.evaluate(() => {
    const B = window.Blockly;
    const ws = B && B.getMainWorkspace && B.getMainWorkspace();
    if (!ws) return 'NO_WORKSPACE';

    // Thử Python generator
    if (B.Python && typeof B.Python.workspaceToCode === 'function') {
      return B.Python.workspaceToCode(ws);
    }
    // Thử MicroPython generator
    if (B.MicroPython && typeof B.MicroPython.workspaceToCode === 'function') {
      return B.MicroPython.workspaceToCode(ws);
    }
    // Thử generator chung
    const gen = B.generators && (B.generators['Python'] || B.generators['MicroPython']);
    if (gen && typeof gen.workspaceToCode === 'function') {
      return gen.workspaceToCode(ws);
    }
    // Liệt kê generators
    return 'Available generators: ' + JSON.stringify(Object.keys(B.generators || {}));
  });
}

// ── Inject XML và lấy Python ────────────────────────────────
async function testBlock(page, blockType, extraFields = '') {
  const xml = `<xml xmlns="https://developers.google.com/blockly/xml">
  <block type="${blockType}" x="40" y="40">${extraFields}</block>
</xml>`;

  const result = await page.evaluate((xmlStr) => {
    try {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      // Thử nhiều cách parse XML
      let dom;
      if (B.utils && B.utils.xml && typeof B.utils.xml.textToDom === 'function') {
        dom = B.utils.xml.textToDom(xmlStr);
      } else if (B.Xml && typeof B.Xml.textToDom === 'function') {
        dom = B.Xml.textToDom(xmlStr);
      } else {
        const parser = new DOMParser();
        dom = parser.parseFromString(xmlStr, 'text/xml').documentElement;
      }
      B.Xml.domToWorkspace(dom, ws);

      // Lấy Python
      if (B.Python && typeof B.Python.workspaceToCode === 'function') {
        return { ok: true, code: B.Python.workspaceToCode(ws) };
      }
      if (B.MicroPython && typeof B.MicroPython.workspaceToCode === 'function') {
        return { ok: true, code: B.MicroPython.workspaceToCode(ws) };
      }
      const gen = B.generators && (B.generators['Python'] || B.generators['MicroPython']);
      if (gen) return { ok: true, code: gen.workspaceToCode(ws) };
      return { ok: false, code: 'No Python generator. Gens: ' + JSON.stringify(Object.keys(B.generators || {})) };
    } catch (e) {
      return { ok: false, code: 'ERROR: ' + e.message };
    }
  }, xml);
  return result;
}

async function main() {
  fs.mkdirSync(OUT_DIR, { recursive: true });

  const pkgDir = process.env.PLAYWRIGHT_PKG_DIR;
  if (!pkgDir) throw new Error('PLAYWRIGHT_PKG_DIR required');

  const { chromium } = require(pkgDir);
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  // ── Navigate ──────────────────────────────────────────────
  console.log('[1] Home...');
  await page.goto('https://app.ohstem.vn', { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(4000);

  console.log('[2] Yolo:Bit device...');
  await clickVisible(page, 'a[href="/devices/yolobit"]');
  await page.waitForTimeout(5000);

  console.log('[3] Codes/yolobit...');
  await clickVisible(page, 'a[href="/codes/yolobit"]');

  console.log('[4] Wait Blockly...');
  await waitBlockly(page);
  await page.screenshot({ path: path.join(OUT_DIR, '01_workspace.png') });

  // ── Kiểm tra generators ───────────────────────────────────
  const genInfo = await page.evaluate(() => {
    const B = window.Blockly;
    return {
      hasPython: !!(B.Python),
      hasMicroPython: !!(B.MicroPython),
      generatorKeys: Object.keys(B.generators || {}),
      xmlUtils: !!(B.utils && B.utils.xml),
      xmlParse: !!(B.Xml),
    };
  });
  console.log('[i] Generator info:', JSON.stringify(genInfo));
  fs.writeFileSync(path.join(OUT_DIR, 'generator_info.json'), JSON.stringify(genInfo, null, 2));

  // ── Thử các block dò line quan trọng ─────────────────────
  const blocksToTest = [
    // Block đọc cảm biến line thô
    { type: 'block_input_linesensor_read', note: 'Đọc cảm biến line (kênh 1-4)' },
    { type: 'robotics_line_sensor_read',   note: 'Đọc line sensor array' },
    { type: 'robotics_line_read_all',      note: 'Đọc tất cả kênh line' },
    // Block dò line tự động
    { type: 'robotics_follow_line_until_cross', note: 'Dò line đến ngã tư' },
    { type: 'robotics_follow_end_line',         note: 'Dò line đến cuối' },
    { type: 'robotics_turn_until_line',         note: 'Quay đến khi gặp line' },
    { type: 'robotics_follow_line_by_time',     note: 'Dò line theo thời gian' },
    { type: 'robotics_follow_line_until',       note: 'Dò line theo điều kiện' },
    // Khởi tạo
    { type: 'robotics_line_sensor_init',        note: 'Khởi tạo line sensor' },
  ];

  const results = {};
  for (const { type, note } of blocksToTest) {
    console.log(`[test] ${type}...`);
    const r = await testBlock(page, type);
    results[type] = { note, ok: r.ok, code: r.code };
    console.log(`  → ${r.ok ? 'OK' : 'FAIL'}: ${r.code.substring(0, 120)}`);
  }

  fs.writeFileSync(
    path.join(OUT_DIR, 'block_python_results.json'),
    JSON.stringify(results, null, 2), 'utf8'
  );

  // ── Screenshot cuối ───────────────────────────────────────
  await page.screenshot({ path: path.join(OUT_DIR, '02_final.png') });

  console.log('\n=== DONE ===');
  console.log('Output:', OUT_DIR);
  await browser.close();
}

main().catch(e => { console.error(e); process.exit(1); });
