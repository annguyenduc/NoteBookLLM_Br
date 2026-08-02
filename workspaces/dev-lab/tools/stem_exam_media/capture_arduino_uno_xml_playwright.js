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
    throw new Error(
      'Usage: node capture_arduino_uno_xml_playwright.js --xml <file.xml> --out <file.png> [--full <file.png>]'
    );
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
  const page = await browser.newPage({
    viewport: { width: 1440, height: 1100 },
    deviceScaleFactor: 2,
  });

  await page.goto('https://ide.mblock.cc/', {
    waitUntil: 'domcontentloaded',
    timeout: 120000,
  });
  await page.waitForTimeout(15000);

  const agree = page.getByText('Agree', { exact: true });
  if (await agree.count()) {
    try {
      await agree.click({ timeout: 3000 });
    } catch {
      // Cookie/privacy prompt is optional for reruns.
    }
  }

  await page.getByText('Add', { exact: true }).click({ timeout: 30000 });
  await page.waitForTimeout(3000);
  await page.locator('input[placeholder="Search"]').last().fill('Ablock');
  await page.waitForTimeout(3000);

  const deviceCard = page
    .locator('.ant-list-item.device-item', { hasText: 'Arduino Uno' })
    .filter({ hasText: 'Developers: Ablock' })
    .first();
  await deviceCard.click({ timeout: 30000 });
  await page.waitForTimeout(1000);
  await page.getByText('OK', { exact: true }).click({ timeout: 30000 });
  await page.waitForTimeout(12000);

  const clip = await page.evaluate((injectedXml) => {
    const chunk = window.webpackChunk_mblock_mblock_web;
    if (!chunk || !Array.isArray(chunk)) {
      throw new Error('mBlock webpack runtime not found');
    }

    let req = null;
    chunk.push([[Symbol('probe')], {}, (runtimeRequire) => {
      req = runtimeRequire;
    }]);
    if (!req) {
      throw new Error('mBlock webpack require hook failed');
    }

    let BlocklyApi = null;
    for (const id of Object.keys(req.m || {})) {
      try {
        const mod = req(id);
        const directWorkspace =
          mod &&
          typeof mod.getMainWorkspace === 'function' &&
          mod.getMainWorkspace();
        const nestedWorkspace =
          mod &&
          mod.Blockly &&
          typeof mod.Blockly.getMainWorkspace === 'function' &&
          mod.Blockly.getMainWorkspace();

        if (
          directWorkspace &&
          directWorkspace.options &&
          directWorkspace.options.languageTree &&
          directWorkspace.options.languageTree.querySelector &&
          directWorkspace.options.languageTree.querySelector(
            'category[id="arduino_uno.CATEGORY_PIN"]'
          )
        ) {
          BlocklyApi = mod;
          break;
        }

        if (
          nestedWorkspace &&
          nestedWorkspace.options &&
          nestedWorkspace.options.languageTree &&
          nestedWorkspace.options.languageTree.querySelector &&
          nestedWorkspace.options.languageTree.querySelector(
            'category[id="arduino_uno.CATEGORY_PIN"]'
          )
        ) {
          BlocklyApi = mod.Blockly;
          break;
        }
      } catch {
        // Skip modules that are not the Blockly runtime.
      }
    }

    if (!BlocklyApi) {
      throw new Error('Arduino Uno Blockly runtime not found');
    }

    const ws = BlocklyApi.getMainWorkspace();
    if (!ws) {
      throw new Error('Arduino Uno workspace is not ready');
    }

    ws.clear();
    const xmlDom = BlocklyApi.Xml.textToDom(injectedXml);
    BlocklyApi.Xml.domToWorkspace(xmlDom, ws);
    ws.render();
    if (typeof ws.cleanUp === 'function') {
      ws.cleanUp();
    }

    const rects = Array.from(
      document.querySelectorAll('svg.blocklySvg g.blocklyDraggable')
    )
      .map((node) => node.getBoundingClientRect())
      .filter((rect) => rect.width > 0 && rect.height > 0);

    if (!rects.length) {
      throw new Error('No rendered Arduino Uno blocks found after XML injection');
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
  console.log(
    JSON.stringify(
      {
        xml: xmlPath,
        out: outPath,
        full: fullPath,
        clip,
      },
      null,
      2
    )
  );
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
