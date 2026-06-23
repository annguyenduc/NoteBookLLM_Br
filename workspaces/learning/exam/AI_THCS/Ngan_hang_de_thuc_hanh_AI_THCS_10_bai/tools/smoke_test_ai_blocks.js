const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const PACKAGE_DIR = path.resolve(__dirname, '..');
const MEDIA_DIR = path.join(PACKAGE_DIR, 'Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media');

const cases = [
  { id: 1, extensions: ['Text to Speech', 'Translate'] },
  { id: 2, extensions: ['Text to Speech', 'Translate'] },
  { id: 3, extensions: ['Text to Speech'] },
  { id: 4, extensions: ['Text to Speech', 'Translate'] },
  { id: 5, extensions: ['Face Sensing', 'Translate', 'Text to Speech'] },
  { id: 6, extensions: ['Body Sensing', 'Text to Speech'] },
  { id: 7, extensions: ['Text to Speech', 'Translate', 'Face Sensing'] },
  { id: 8, extensions: ['Face Sensing', 'Text to Speech'] },
  { id: 9, extensions: ['Body Sensing', 'Translate', 'Text to Speech'] },
  { id: 10, extensions: ['Teachable Machine', 'Text to Speech', 'Translate'] },
];

async function openExtensionLibrary(page) {
  await page.click('[class*="extension-button"]', { timeout: 12000 });
  await page.waitForTimeout(1200);
}

async function loadExtension(page, name) {
  await openExtensionLibrary(page);
  let card = page.locator('[class*="library-item"]').filter({ hasText: name }).first();
  if (!(await card.count())) card = page.locator(`text="${name}"`).first();
  await card.scrollIntoViewIfNeeded({ timeout: 6000 });
  await card.click({ timeout: 8000, force: true });
  await page.waitForTimeout(2500);
}

async function smoke(browser, item) {
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });
  try {
    await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'domcontentloaded', timeout: 90000 });
    await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace && window.Blockly.getMainWorkspace(), { timeout: 90000 });
    await page.waitForTimeout(2500);
    for (const ext of item.extensions) await loadExtension(page, ext);
    await page.waitForTimeout(4000);
    const xml = fs.readFileSync(path.join(MEDIA_DIR, `bt${item.id}_code.xml`), 'utf8');
    const result = await page.evaluate((xmlText) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const dom = B.Xml.textToDom(xmlText);
      B.Xml.domToWorkspace(dom, ws);
      ws.render();
      const blocks = ws.getAllBlocks(false).map((block) => block.type);
      return {
        top: ws.getTopBlocks().length,
        blocks: blocks.length,
        opcodes: Array.from(new Set(blocks)).sort(),
        xmlLen: new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws)).length,
      };
    }, xml);
    if (result.blocks === 0 || result.top === 0) {
      throw new Error(`XML imported with no runnable blocks: top=${result.top} blocks=${result.blocks}`);
    }
    return { id: item.id, status: 'PASS', ...result };
  } catch (error) {
    return { id: item.id, status: 'FAIL', error: String(error.message || error).slice(0, 500) };
  } finally {
    await page.close();
  }
}

(async () => {
  const browser = await chromium.launch({
    channel: 'msedge',
    headless: true,
    args: ['--use-fake-ui-for-media-stream', '--use-fake-device-for-media-stream'],
  });
  const results = [];
  try {
    for (const item of cases) {
      const result = await smoke(browser, item);
      results.push(result);
      if (result.status === 'PASS') {
        console.log(`BT${result.id}:PASS top=${result.top} blocks=${result.blocks} xmlLen=${result.xmlLen}`);
      } else {
        console.log(`BT${result.id}:FAIL ${result.error}`);
      }
    }
  } finally {
    await browser.close();
  }
  const report = {
    generatedAt: new Date().toISOString(),
    results,
  };
  fs.writeFileSync(path.join(PACKAGE_DIR, 'AI_BLOCKS_SMOKE_REPORT.json'), JSON.stringify(report, null, 2), 'utf8');
  if (results.some((result) => result.status !== 'PASS')) process.exit(1);
})();
