const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const PACKAGE_DIR = path.resolve(__dirname, '..');
const MEDIA_DIR = path.join(PACKAGE_DIR, 'Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media');

const cases = [
  { id: 1, answers: ['robot', 'robot', 'may tinh', 'computer', 'tri tue', 'intelligence', 'hoc', 'study', 'du lieu', 'data'], waits: [800, 800, 800, 800, 800, 800, 800, 800, 800, 2500] },
  { id: 2, answers: ['1'], keys: [{ key: 'Space', wait: 4500 }, { key: 'Space', wait: 4500 }, { key: 'Space', wait: 6500 }], waits: [2000] },
  { id: 3, answers: ['1', '12', '8', '0'], waits: [800, 800, 800, 2500] },
  { id: 4, answers: ['cong cu dich ngon ngu', 'ai', 'tts', 'scratch', 'camera'], waits: [900, 900, 900, 900, 3500] },
  { id: 6, answers: [], keys: [{ key: 'Space', wait: 4500 }], waits: [6500] },
  { id: 9, answers: [], keys: [{ key: 'Space', wait: 2500 }, { key: 'Space', wait: 2500 }, { key: 'Space', wait: 2500 }], waits: [4500] },
];

async function waitForInput(page, timeout = 6000) {
  const candidates = [
    'input[class*="stage-question_question-input"]',
    'input[placeholder]',
    'input',
  ];
  const deadline = Date.now() + timeout;
  while (Date.now() < deadline) {
    for (const selector of candidates) {
      const input = page.locator(selector).first();
      try {
        if (await input.isVisible({ timeout: 300 })) return input;
      } catch (_) {}
    }
    await page.waitForTimeout(250);
  }
  return null;
}

async function answerIfAsked(page, value) {
  const input = await waitForInput(page);
  if (!input) return false;
  await input.fill(value);
  await page.keyboard.press('Enter');
  await page.waitForTimeout(400);
  return true;
}

async function loadProject(page, sb3Path) {
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace && window.Blockly.getMainWorkspace(), { timeout: 90000 });
  await page.waitForTimeout(2500);
  await page.locator('input[type="file"]').first().setInputFiles(sb3Path);
  await page.waitForTimeout(5000);
}

async function enterFullScreen(page) {
  const selectors = [
    'img[alt="Enter full screen mode"]',
    'button[aria-label*="full screen" i]',
    '[class*="stage-header_stage-size-row"] img',
  ];
  for (const selector of selectors) {
    try {
      const target = page.locator(selector).first();
      if (await target.isVisible({ timeout: 1000 })) {
        await target.click({ timeout: 3000 });
        await page.waitForTimeout(1500);
        return;
      }
    } catch (_) {}
  }
}

async function clickGreenFlag(page) {
  const selectors = [
    '[class*="green-flag_green-flag"]',
    'img[alt="Green flag"]',
    'img[title="Go"]',
  ];
  for (const selector of selectors) {
    try {
      await page.locator(selector).first().click({ timeout: 3000 });
      await page.waitForTimeout(1200);
      return;
    } catch (_) {}
  }
  throw new Error('Green flag button not found');
}

async function recordOne(browser, item) {
  const sb3Path = path.join(MEDIA_DIR, `bt${item.id}_code.sb3`);
  if (!fs.existsSync(sb3Path)) throw new Error(`Missing SB3 for BT${item.id}: ${sb3Path}`);

  const context = await browser.newContext({
    recordVideo: { dir: MEDIA_DIR, size: { width: 1280, height: 720 } },
    viewport: { width: 1280, height: 720 },
    permissions: ['camera', 'microphone'],
  });
  const page = await context.newPage();
  let tempVideo = null;
  try {
    await loadProject(page, sb3Path);
    await enterFullScreen(page);
    await clickGreenFlag(page);
    for (let i = 0; i < item.answers.length; i += 1) {
      await answerIfAsked(page, item.answers[i]);
      await page.waitForTimeout(item.waits[i] || 800);
    }
    for (const action of item.keys || []) {
      await page.keyboard.press(action.key);
      await page.waitForTimeout(action.wait || 1000);
    }
    await page.waitForTimeout((item.waits || []).at(-1) || 3000);
    tempVideo = await page.video().path();
  } finally {
    await context.close();
  }

  const finalPath = path.join(MEDIA_DIR, `bt${item.id}_demo.webm`);
  if (fs.existsSync(finalPath)) fs.unlinkSync(finalPath);
  fs.renameSync(tempVideo, finalPath);
  console.log(`BT${item.id}: video saved ${finalPath}`);
}

(async () => {
  const browser = await chromium.launch({
    channel: 'msedge',
    headless: true,
    args: ['--use-fake-ui-for-media-stream', '--use-fake-device-for-media-stream'],
  });
  try {
    for (const item of cases) await recordOne(browser, item);
  } finally {
    await browser.close();
  }
})();
