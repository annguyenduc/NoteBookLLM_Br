const fs = require('fs');
const path = require('path');

function parseArgs(argv) {
  const args = {};
  for (let i = 2; i < argv.length; i += 1) {
    const token = argv[i];
    if (token === '--xml') {
      args.xml = argv[++i];
    } else if (token === '--out') {
      args.out = argv[++i];
    } else if (token === '--full') {
      args.full = argv[++i];
    }
  }
  if (!args.xml || !args.out) {
    throw new Error('Usage: node capture_xbot_xml_playwright.js --xml <file.xml> --out <file.png> [--full <file.png>]');
  }
  return args;
}

async function main() {
  const args = parseArgs(process.argv);
  const pkgDir = process.env.PLAYWRIGHT_PKG_DIR;
  if (!pkgDir) {
    throw new Error('PLAYWRIGHT_PKG_DIR is required');
  }

  const xmlPath = path.resolve(args.xml);
  const outPath = path.resolve(args.out);
  const fullPath = args.full ? path.resolve(args.full) : null;
  const xmlText = fs.readFileSync(xmlPath, 'utf8');
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  if (fullPath) {
    fs.mkdirSync(path.dirname(fullPath), { recursive: true });
  }

  const { chromium } = require(pkgDir);
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1100 }, deviceScaleFactor: 2 });

  await page.goto('https://app.ohstem.vn', {
    waitUntil: 'domcontentloaded',
    timeout: 60000,
  });
  await page.waitForTimeout(3000);

  await page.evaluate(() => {
    const xbot = Array.from(document.querySelectorAll('a[href="/devices/xbot"]')).find((node) => {
      const rect = node.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0;
    });
    if (!xbot) {
      throw new Error('xBot device link not found');
    }
    xbot.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
  });
  await page.waitForTimeout(8000);

  await page.evaluate(() => {
    const code = Array.from(document.querySelectorAll('a[href="/codes/xbot"]')).find((node) => {
      const rect = node.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0;
    });
    if (!code) {
      throw new Error('xBot code link not found');
    }
    code.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
  });

  await page.waitForFunction(() => {
    return (
      window.Blockly &&
      typeof window.Blockly.getMainWorkspace === 'function' &&
      window.Blockly.getMainWorkspace()
    );
  }, { timeout: 60000 });
  await page.waitForTimeout(12000);

  const clip = await page.evaluate((injectedXml) => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    ws.clear();

    const xmlDom = (B.utils && B.utils.xml && typeof B.utils.xml.textToDom === 'function')
      ? B.utils.xml.textToDom(injectedXml)
      : B.Xml.textToDom(injectedXml);

    B.Xml.domToWorkspace(xmlDom, ws);
    ws.render();
    if (typeof ws.cleanUp === 'function') {
      ws.cleanUp();
    }
    if (typeof ws.scrollCenter === 'function') {
      ws.scrollCenter();
    }

    const blocks = Array.from(document.querySelectorAll('g.blocklyDraggable'));
    const rects = blocks
      .map((node) => node.getBoundingClientRect())
      .filter((rect) => rect.width > 0 && rect.height > 0);

    if (!rects.length) {
      throw new Error('No rendered blocks found after XML injection');
    }

    const margin = 16;
    const left = Math.max(0, Math.min(...rects.map((rect) => rect.left)) - margin);
    const top = Math.max(0, Math.min(...rects.map((rect) => rect.top)) - margin);
    const right = Math.max(...rects.map((rect) => rect.right)) + margin;
    const bottom = Math.max(...rects.map((rect) => rect.bottom)) + margin;

    return {
      x: left,
      y: top,
      width: right - left,
      height: bottom - top,
      blockCount: rects.length,
    };
  }, xmlText);

  if (fullPath) {
    await page.screenshot({ path: fullPath, fullPage: true });
  }
  await page.screenshot({
    path: outPath,
    clip,
  });

  await browser.close();
  console.log(JSON.stringify({
    xml: xmlPath,
    out: outPath,
    full: fullPath,
    clip,
  }, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
