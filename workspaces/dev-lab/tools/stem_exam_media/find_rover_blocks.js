/**
 * find_rover_blocks.js
 * Tìm kiếm các block trong category ROVER để xem:
 * - Khối nào dùng để đọc cảm biến line (mắt 1, 2, 3, 4)
 * - Khối nào dùng để di chuyển motor (tốc độ bánh trái/phải)
 * và dump ra code Python mẫu của chúng.
 */

const fs = require('fs');
const path = require('path');

const OUT_DIR = path.join(__dirname, 'blocks_probe_out');
fs.mkdirSync(OUT_DIR, { recursive: true });

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
  if (!pkgDir) throw new Error('PLAYWRIGHT_PKG_DIR required');

  const { chromium } = require(pkgDir);
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  console.log('[1] Loading app...');
  for (let r = 0; r < 5; r++) {
    try {
      await page.goto('https://app.ohstem.vn', { waitUntil: 'domcontentloaded', timeout: 60000 });
      break;
    } catch(e) {
      console.log(`  retry ${r+1}/5: ${e.message}`);
      await page.waitForTimeout(4000);
    }
  }
  await page.waitForTimeout(5000);

  console.log('[2] Selecting Yolobit...');
  await clickVisible(page, 'a[href="/devices/yolobit"]');
  await page.waitForTimeout(5000);

  console.log('[3] Opening coding...');
  await clickVisible(page, 'a[href="/codes/yolobit"]');

  console.log('[4] Wait Blockly...');
  await page.waitForFunction(() =>
    window.Blockly && window.Blockly.getMainWorkspace && window.Blockly.getMainWorkspace(),
    { timeout: 90000 }
  );
  await page.waitForTimeout(10000);

  console.log('[5] Load Rover Extension...');
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
  await page.waitForTimeout(4000);

  await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button'));
    const skip = btns.find(b => b.textContent && (b.textContent.includes('Bỏ qua') || b.textContent.includes('Skip') || b.textContent.includes('OK')));
    if (skip) skip.click();
  });
  await page.waitForTimeout(3000);

  // 6. Quét qua toàn bộ khối trong toolbox và tìm các khối chứa từ khóa "tốc độ", "động cơ", "di chuyển", "cảm biến", "mắt", "line"
  console.log('[6] Scanning toolbox blocks...');
  const blockInfos = await page.evaluate(() => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    
    // Hàm lấy Python code của 1 block
    function getBlockPython(type) {
      try {
        ws.clear();
        const b = ws.newBlock(type);
        b.initSvg();
        b.render();
        let code = '';
        if (B.Python && typeof B.Python.workspaceToCode === 'function') {
          code = B.Python.workspaceToCode(ws);
        }
        b.dispose();
        return code;
      } catch(e) {
        return 'ERROR: ' + e.message;
      }
    }

    const allTypes = Object.keys(B.Blocks);
    const results = [];

    for (const type of allTypes) {
      // Chỉ lấy các block thuộc về thiết bị (có tên bắt đầu bằng robotics_, block_move_, block_input_ hoặc xbot_ hoặc rover_)
      if (type.startsWith('robotics_') || type.startsWith('block_') || type.startsWith('yolobit_')) {
        try {
          ws.clear();
          const b = ws.newBlock(type);
          
          // Lấy nhãn hiển thị của block bằng cách ghép các text trong fieldRow
          const labels = [];
          for (const input of b.inputList) {
            for (const field of input.fieldRow) {
              if (field.getText) {
                labels.push(field.getText());
              } else if (field.value_) {
                labels.push(field.value_);
              }
            }
          }
          
          const labelText = labels.join(' ').trim();
          b.dispose();

          // Lọc các block liên quan đến motor, di chuyển hoặc cảm biến line
          const lowText = labelText.toLowerCase();
          const matches = 
            lowText.includes('động cơ') || 
            lowText.includes('tốc độ') || 
            lowText.includes('di chuyển') || 
            lowText.includes('cảm biến') || 
            lowText.includes('mắt') || 
            lowText.includes('line') ||
            lowText.includes('quay') ||
            type.includes('motor') ||
            type.includes('sensor') ||
            type.includes('linesensor') ||
            type.includes('move');

          if (matches) {
            const py = getBlockPython(type);
            results.push({
              type,
              labelText,
              python: py
            });
          }
        } catch(e) {
          // Bỏ qua lỗi khởi tạo block
        }
      }
    }
    return results;
  });

  console.log('[7] Found blocks count:', blockInfos.length);
  fs.writeFileSync(path.join(OUT_DIR, 'found_blocks.json'), JSON.stringify(blockInfos, null, 2), 'utf8');

  // Liệt kê ra console các block quan trọng nhất
  blockInfos.forEach(info => {
    console.log(`- Type: ${info.type}`);
    console.log(`  Label: ${info.labelText}`);
    console.log(`  Python: ${info.python.trim()}`);
  });

  await page.screenshot({ path: path.join(OUT_DIR, 'blocks_scanned.png') });
  await browser.close();
}

main().catch(e => {
  console.error(e);
  process.exit(1);
});
