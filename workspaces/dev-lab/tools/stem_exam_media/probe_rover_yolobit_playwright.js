/**
 * probe_rover_yolobit_playwright.js
 * Mở Yolobit workspace, bật extension Robot Rover,
 * rồi dump tất cả opcode của Rover (đặc biệt IR sensor)
 * và xuất Python code mẫu.
 *
 * Usage:
 *   $env:PLAYWRIGHT_PKG_DIR = "C:\Users\anngu\AppData\Local\npm-cache\_npx\e41f203b7505f1fb\node_modules\playwright"
 *   node probe_rover_yolobit_playwright.js --out <output_dir>
 */

const fs = require('fs');
const path = require('path');

function parseArgs(argv) {
  const args = { out: path.join(__dirname, 'rover_probe_out') };
  for (let i = 2; i < argv.length; i++) {
    if (argv[i] === '--out') args.out = argv[++i];
  }
  return args;
}

async function waitForBlockly(page, timeout = 60000) {
  await page.waitForFunction(() => {
    return (
      window.Blockly &&
      typeof window.Blockly.getMainWorkspace === 'function' &&
      window.Blockly.getMainWorkspace()
    );
  }, { timeout });
  // Chờ thêm để workspace ổn định
  await page.waitForTimeout(8000);
}

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
  const args = parseArgs(process.argv);
  const pkgDir = process.env.PLAYWRIGHT_PKG_DIR;
  if (!pkgDir) throw new Error('PLAYWRIGHT_PKG_DIR is required');

  fs.mkdirSync(args.out, { recursive: true });

  const { chromium } = require(pkgDir);
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  // ── Bước 1: Mở trang chủ OhStem ──
  console.log('[1] Mở app.ohstem.vn...');
  await page.goto('https://app.ohstem.vn', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForTimeout(4000);
  await page.screenshot({ path: path.join(args.out, '01_home.png') });

  // ── Bước 2: Click vào Yolo:Bit ──
  console.log('[2] Click Yolo:Bit...');
  await clickVisible(page, 'a[href="/devices/yolobit"]');
  await page.waitForTimeout(5000);
  await page.screenshot({ path: path.join(args.out, '02_yolobit_device.png') });

  // ── Bước 3: Click vào Lập trình (codes/yolobit) ──
  console.log('[3] Click Lập trình (codes/yolobit)...');
  await clickVisible(page, 'a[href="/codes/yolobit"]');

  // ── Bước 4: Chờ Blockly workspace load ──
  console.log('[4] Chờ Blockly workspace...');
  await waitForBlockly(page);
  await page.screenshot({ path: path.join(args.out, '03_blockly_ready.png') });

  // ── Bước 5: Bật extension Robot Rover ──
  console.log('[5] Mở Extensions và bật Rover...');
  // Click nút "MỞ RỘNG" hoặc biểu tượng extensions
  try {
    await clickVisible(page, 'a[href="/extensions/yolobit"]');
    await page.waitForTimeout(2000);
  } catch {
    // Thử tìm nút extensions trong toolbar
    await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button, .toolbox-category'));
      const extBtn = btns.find(b => b.textContent && b.textContent.includes('MỞ RỘNG'));
      if (extBtn) extBtn.click();
    });
    await page.waitForTimeout(2000);
  }
  await page.screenshot({ path: path.join(args.out, '04_extensions_panel.png') });

  // Tìm và click card Robot Rover
  const roverFound = await page.evaluate(() => {
    const cards = Array.from(document.querySelectorAll('.extension-card, .card, [class*="extension"]'));
    const rover = cards.find(c => c.textContent && c.textContent.toLowerCase().includes('rover'));
    if (rover) {
      rover.click();
      return true;
    }
    // Thử tìm theo text
    const allElems = Array.from(document.querySelectorAll('*'));
    const roverElem = allElems.find(el =>
      el.children.length === 0 &&
      el.textContent.trim().toLowerCase() === 'robot rover'
    );
    if (roverElem) {
      roverElem.closest('[class*="card"], [class*="item"], div').click();
      return true;
    }
    return false;
  });
  console.log(`  Rover card found & clicked: ${roverFound}`);
  await page.waitForTimeout(3000);
  await page.screenshot({ path: path.join(args.out, '05_after_rover_enable.png') });

  // Đóng popup nếu có (bỏ qua download)
  await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button'));
    const skip = btns.find(b => b.textContent && (
      b.textContent.includes('Bỏ qua') || b.textContent.includes('Skip') || b.textContent.includes('OK')
    ));
    if (skip) skip.click();
  });
  await page.waitForTimeout(2000);

  // ── Bước 6: Dump tất cả Blockly block types có rover/IR ──
  console.log('[6] Dump block opcodes...');
  const blockData = await page.evaluate(() => {
    const allTypes = Object.keys(window.Blockly && window.Blockly.Blocks || {});
    const roverBlocks = allTypes.filter(t =>
      t.includes('rover') || t.includes('ir') || t.includes('line') ||
      t.includes('IR') || t.includes('Line')
    );
    return {
      total: allTypes.length,
      roverBlocks,
      allTypes: allTypes.sort(),
    };
  });

  fs.writeFileSync(
    path.join(args.out, 'block_opcodes.json'),
    JSON.stringify(blockData, null, 2),
    'utf8'
  );
  console.log(`  Tổng blocks: ${blockData.total}`);
  console.log(`  Rover/IR blocks (${blockData.roverBlocks.length}):`);
  blockData.roverBlocks.forEach(t => console.log(`    - ${t}`));

  // ── Bước 7: Chụp toolbox category ROVER ──
  console.log('[7] Mở category Rover trong toolbox...');
  await page.evaluate(() => {
    // Tìm category có tên "ROVER" hoặc "Rover"
    const cats = Array.from(document.querySelectorAll('.blocklyTreeLabel, .toolbox-category-label, [class*="toolbox"]'));
    const roverCat = cats.find(c => c.textContent && c.textContent.toUpperCase().includes('ROVER'));
    if (roverCat) roverCat.click();
  });
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(args.out, '06_rover_category.png') });

  // ── Bước 8: Thêm một block IR vào workspace để lấy Python code ──
  console.log('[8] Thử inject XML test dò line...');
  const testXml = `<xml xmlns="https://developers.google.com/blockly/xml">
  <block type="rover_run_with_speed" x="40" y="40">
  </block>
</xml>`;

  // Thử inject và xem Python code
  const pythonCode = await page.evaluate(async (xml) => {
    try {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const dom = (B.utils && B.utils.xml)
        ? B.utils.xml.textToDom(xml)
        : B.Xml.textToDom(xml);
      B.Xml.domToWorkspace(dom, ws);
      ws.render();

      // Lấy Python code nếu có generator
      if (B.Python && typeof B.Python.workspaceToCode === 'function') {
        return B.Python.workspaceToCode(ws);
      }
      if (B.Generator && B.Generator.NAME_) {
        return 'Generator available: ' + B.Generator.NAME_;
      }
      return 'No Python generator found';
    } catch (e) {
      return 'ERROR: ' + e.message;
    }
  }, testXml);
  console.log('  Python code preview:', pythonCode);

  // ── Bước 9: Dump Python code từ các block phổ biến ──
  console.log('[9] Thử xuất Python từ workspace button...');
  // Click Python tab nếu có
  await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button, .tab, [role="tab"]'));
    const pyBtn = btns.find(b => b.textContent && b.textContent.toLowerCase().includes('python'));
    if (pyBtn) pyBtn.click();
  });
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(args.out, '07_python_view.png') });

  // Đọc Python code từ textarea/editor
  const pyText = await page.evaluate(() => {
    const ta = document.querySelector('textarea.blocklyComputedStyle, .python-editor textarea, .ace_content, .cm-content');
    if (ta) return ta.textContent || ta.value;
    const pre = document.querySelector('pre');
    if (pre) return pre.textContent;
    return 'Not found';
  });
  console.log('  Python text:', pyText.substring(0, 500));
  fs.writeFileSync(path.join(args.out, 'python_code_sample.py'), pyText, 'utf8');

  await page.screenshot({ path: path.join(args.out, '08_final.png') });

  // Kết quả
  const report = {
    timestamp: new Date().toISOString(),
    roverBlockCount: blockData.roverBlocks.length,
    roverBlocks: blockData.roverBlocks,
    pythonCode: pyText,
  };
  fs.writeFileSync(path.join(args.out, 'report.json'), JSON.stringify(report, null, 2), 'utf8');
  console.log('\n=== XONG ===');
  console.log('Output dir:', args.out);

  await browser.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
