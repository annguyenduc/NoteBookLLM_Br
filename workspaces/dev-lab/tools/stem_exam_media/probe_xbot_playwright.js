const fs = require('fs');
const path = require('path');

async function main() {
  const pkgDir = process.env.PLAYWRIGHT_PKG_DIR;
  if (!pkgDir) {
    throw new Error('PLAYWRIGHT_PKG_DIR is required');
  }

  const { chromium } = require(pkgDir);
  const outDir = path.resolve(process.env.TEMP || '.', 'xbot_playwright_probe');
  fs.mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1100 } });

  await page.goto('https://app.ohstem.vn', {
    waitUntil: 'domcontentloaded',
    timeout: 60000,
  });
  await page.waitForTimeout(3000);
  await page.evaluate(() => {
    const candidates = Array.from(document.querySelectorAll('a[href="/devices/xbot"]'));
    const visible = candidates.find((node) => {
      const rect = node.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0;
    });
    const target = visible || candidates[0];
    if (!target) {
      throw new Error('xBot link not found');
    }
    target.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
  });
  await page.waitForTimeout(10000);
  await page.evaluate(() => {
    const candidates = Array.from(document.querySelectorAll('a[href="/codes/xbot"]'));
    const visible = candidates.find((node) => {
      const rect = node.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0;
    });
    const target = visible || candidates[0];
    if (!target) {
      throw new Error('xBot code tile not found');
    }
    target.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
  });
  await page.waitForTimeout(12000);

  const state = await page.evaluate(() => {
    const blockly = window.Blockly || null;
    const workspace = blockly && typeof blockly.getMainWorkspace === 'function'
      ? blockly.getMainWorkspace()
      : null;

    let blockTypes = [];
    let toolboxText = '';
    let toolboxType = null;

    if (workspace && workspace.options && workspace.options.languageTree) {
      const tree = workspace.options.languageTree;
      toolboxType = Object.prototype.toString.call(tree);

      if (tree && typeof tree.querySelectorAll === 'function') {
        toolboxText = tree.outerHTML || '';
        blockTypes = Array.from(tree.querySelectorAll('block'))
          .map((node) => node.getAttribute('type'))
          .filter(Boolean);
      } else {
        try {
          toolboxText = JSON.stringify(tree).slice(0, 20000);
        } catch (error) {
          toolboxText = String(tree);
        }
      }
    }

    return {
      href: location.href,
      title: document.title,
      hasBlockly: Boolean(blockly),
      hasWorkspace: Boolean(workspace),
      toolboxType,
      blockTypeCount: blockTypes.length,
      firstBlockTypes: blockTypes.slice(0, 200),
      toolboxSnippet: toolboxText.slice(0, 20000),
    };
  });

  fs.writeFileSync(
    path.join(outDir, 'xbot_probe_state.json'),
    JSON.stringify(state, null, 2),
    'utf8'
  );

  await page.screenshot({
    path: path.join(outDir, 'xbot_workspace.png'),
    fullPage: true,
  });

  await browser.close();
  console.log(JSON.stringify({
    outDir,
    href: state.href,
    title: state.title,
    hasBlockly: state.hasBlockly,
    hasWorkspace: state.hasWorkspace,
    blockTypeCount: state.blockTypeCount,
    firstBlockTypes: state.firstBlockTypes.slice(0, 20),
  }, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
