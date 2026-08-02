/**
 * dump_rover_block_schema.js
 * Dùng Playwright (headless=true) để:
 * 1. Mở Yolobit workspace (tái dùng browser đã có page)
 * 2. Dump JSON schema của các block robotics_*
 *
 * Chạy nhiều lần an toàn (không sửa workspace).
 *
 * Usage:
 *   $env:PLAYWRIGHT_PKG_DIR = "..."
 *   node dump_rover_block_schema.js
 */

const fs   = require('fs');
const path = require('path');

const OUT  = path.join(__dirname, 'rover_schema_out');

async function clickVisible(page, sel) {
  await page.evaluate((s) => {
    const el = Array.from(document.querySelectorAll(s))
      .find(n => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!el) throw new Error('Not found: ' + s);
    el.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
  }, sel);
}

async function main() {
  fs.mkdirSync(OUT, { recursive: true });
  const pkgDir = process.env.PLAYWRIGHT_PKG_DIR;
  if (!pkgDir) throw new Error('PLAYWRIGHT_PKG_DIR required');

  const { chromium } = require(pkgDir);
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  // 1. Navigate
  console.log('[1] home...');
  for (let retry = 0; retry < 3; retry++) {
    try {
      await page.goto('https://app.ohstem.vn', { waitUntil: 'domcontentloaded', timeout: 60000 });
      break;
    } catch (e) {
      console.log(`  retry ${retry+1}/3: ${e.message}`);
      await page.waitForTimeout(3000);
    }
  }
  await page.waitForTimeout(4000);
  await page.screenshot({ path: path.join(OUT, '01_home.png') });

  console.log('[2] yolobit...');
  await clickVisible(page, 'a[href="/devices/yolobit"]');
  await page.waitForTimeout(5000);

  console.log('[3] codes...');
  await clickVisible(page, 'a[href="/codes/yolobit"]');

  console.log('[4] wait blockly...');
  await page.waitForFunction(() =>
    window.Blockly && window.Blockly.getMainWorkspace &&
    window.Blockly.getMainWorkspace(),
  { timeout: 90000 });
  await page.waitForTimeout(10000);

  await page.screenshot({ path: path.join(OUT, '02_workspace.png') });

  // 2. Dump schema của các block robotics_ và block_input_linesensor
  console.log('[5] dump schemas...');
  const schemas = await page.evaluate(() => {
    const B = window.Blockly;
    const targets = [
      'block_input_linesensor_read',
      'robotics_line_sensor_init',
      'robotics_line_sensor_i2c_init',
      'robotics_digital_line_sensor_init',
      'robotics_line_sensor_read',
      'robotics_line_read_all',
      'robotics_follow_line_until_cross',
      'robotics_follow_end_line',
      'robotics_turn_until_line',
      'robotics_follow_line_by_time',
      'robotics_follow_line_until',
    ];
    const result = {};
    for (const type of targets) {
      const def = B.Blocks[type];
      if (!def) { result[type] = null; continue; }
      try {
        // Tạo block tạm để lấy init
        const ws = B.getMainWorkspace();
        const tmp = ws.newBlock(type);
        // Lấy fields
        const fields = [];
        for (const input of (tmp.inputList || [])) {
          for (const field of (input.fieldRow || [])) {
            if (field.name) {
              fields.push({ name: field.name, value: field.getValue ? field.getValue() : null });
            }
          }
        }
        // Lấy inputs
        const inputs = (tmp.inputList || []).map(inp => ({
          name: inp.name,
          type: inp.type,
          fieldNames: (inp.fieldRow || []).map(f => f.name).filter(Boolean),
        }));
        tmp.dispose(false);
        result[type] = { fields, inputs };
      } catch(e) {
        result[type] = { error: e.message };
      }
    }
    return result;
  });

  const schemaPath = path.join(OUT, 'block_schemas.json');
  fs.writeFileSync(schemaPath, JSON.stringify(schemas, null, 2), 'utf8');
  console.log('Schemas:', schemaPath);

  // Print key info
  for (const [type, schema] of Object.entries(schemas)) {
    if (!schema) { console.log(`  ${type}: NOT FOUND`); continue; }
    if (schema.error) { console.log(`  ${type}: ERROR - ${schema.error}`); continue; }
    const fieldNames = schema.fields.map(f => `${f.name}=${JSON.stringify(f.value)}`).join(', ');
    const inputNames = schema.inputs.map(i => i.name).filter(Boolean).join(', ');
    console.log(`  ${type}:\n    fields: [${fieldNames}]\n    inputs: [${inputNames}]`);
  }

  // 3. Dump Python generator info
  console.log('[6] generator info...');
  const genInfo = await page.evaluate(() => {
    const B = window.Blockly;
    const hasPy = !!(B.Python && B.Python.workspaceToCode);
    const hasMpy = !!(B.MicroPython && B.MicroPython.workspaceToCode);
    const genKeys = Object.keys(B.generators || {});
    // Thử lấy generator function của một block
    const sampleGen = B.Python && B.Python['robotics_follow_line_until_cross'];
    return {
      hasPython: hasPy,
      hasMicroPython: hasMpy,
      generatorKeys: genKeys,
      sampleGenExists: !!(sampleGen),
      sampleGenStr: sampleGen ? sampleGen.toString().substring(0, 300) : null,
    };
  });
  fs.writeFileSync(path.join(OUT, 'gen_info.json'), JSON.stringify(genInfo, null, 2));
  console.log('Generator info:', JSON.stringify(genInfo, null, 2));

  // 4. Thử lấy Python code bằng cách inject XML
  console.log('[7] inject test XML...');
  const testXmlSimple = `<xml xmlns="https://developers.google.com/blockly/xml">
  <block type="robotics_follow_line_until_cross" x="40" y="40">
  </block>
</xml>`;

  const pyResult = await page.evaluate((xml) => {
    try {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const parser = new DOMParser();
      const doc = parser.parseFromString(xml, 'text/xml');
      const dom = doc.documentElement;
      B.Xml.domToWorkspace(dom, ws);
      ws.render();

      // Thử tất cả generators
      const gens = { ...B.generators };
      if (B.Python) gens['_Python'] = B.Python;
      if (B.MicroPython) gens['_MicroPython'] = B.MicroPython;

      const results = {};
      for (const [name, gen] of Object.entries(gens)) {
        try {
          if (gen && typeof gen.workspaceToCode === 'function') {
            results[name] = gen.workspaceToCode(ws);
          }
        } catch(e) {
          results[name] = 'ERROR: ' + e.message;
        }
      }
      return results;
    } catch(e) {
      return { FATAL: e.message };
    }
  }, testXmlSimple);

  fs.writeFileSync(path.join(OUT, 'python_test.json'), JSON.stringify(pyResult, null, 2));
  console.log('Python test results:', JSON.stringify(pyResult, null, 2));

  await page.screenshot({ path: path.join(OUT, '03_final.png') });
  await browser.close();
  console.log('\n=== DONE === Output:', OUT);
}

main().catch(e => { console.error(e); process.exit(1); });
