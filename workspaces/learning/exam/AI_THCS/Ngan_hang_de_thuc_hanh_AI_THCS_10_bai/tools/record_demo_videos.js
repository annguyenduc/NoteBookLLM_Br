const { chromium } = require('playwright');
const fs = require('fs');
const os = require('os');
const path = require('path');
const { spawnSync } = require('child_process');

const PACKAGE_DIR = path.resolve(__dirname, '..');
const MEDIA_DIR = path.join(PACKAGE_DIR, 'Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media');
const FPS = 4;
const VIDEO_WIDTH = 1280;
const VIDEO_HEIGHT = 720;
const VERIFY_WIDTH = 320;
const VERIFY_HEIGHT = 180;
const VERIFY_MIN_CHANGED_PERCENT = 0.5;

const cases = [
  { id: 1, answers: ['robot', 'robot', 'may tinh', 'computer', 'tri tue', 'intelligence', 'hoc', 'study', 'du lieu', 'data'], waits: [800, 800, 800, 800, 800, 800, 800, 800, 800, 2500] },
  { id: 2, answers: ['1'], keys: [{ key: 'Space', wait: 4500 }, { key: 'Space', wait: 4500 }, { key: 'Space', wait: 6500 }], waits: [2000] },
  { id: 3, answers: ['1', '12', '8', '0'], waits: [800, 800, 800, 2500] },
  { id: 4, answers: ['cong cu dich ngon ngu', 'ai', 'tts', 'scratch', 'camera'], waits: [900, 900, 900, 900, 3500] },
  { id: 6, answers: [], keys: [{ key: 'Space', wait: 4500 }], waits: [6500] },
  { id: 9, answers: [], keys: [{ key: 'Space', wait: 2500 }, { key: 'Space', wait: 2500 }, { key: 'Space', wait: 2500 }], waits: [4500] },
];

async function waitForInput(page, timeout = 6000) {
  const deadline = Date.now() + timeout;
  while (Date.now() < deadline) {
    const inputIndex = await page.evaluate(() => {
      const inputs = Array.from(document.querySelectorAll('input'));
      const visible = inputs
        .map((input, index) => ({ input, index, rect: input.getBoundingClientRect() }))
        .filter(({ input, rect }) => {
          const style = window.getComputedStyle(input);
          return rect.width > 100 && rect.height > 15 && style.visibility !== 'hidden' && style.display !== 'none';
        });

      const active = visible.find(({ input, rect }) => input === document.activeElement && rect.top > window.innerHeight * 0.55);
      if (active) return active.index;

      const stageQuestion = visible
        .filter(({ rect }) => rect.top > window.innerHeight * 0.55)
        .sort((a, b) => (b.rect.width * b.rect.height) - (a.rect.width * a.rect.height))[0];
      return stageQuestion ? stageQuestion.index : -1;
    }
    );

    if (inputIndex >= 0) {
      const input = page.locator('input').nth(inputIndex);
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

function resolveFfmpeg() {
  if (process.env.FFMPEG_PATH && fs.existsSync(process.env.FFMPEG_PATH)) return process.env.FFMPEG_PATH;
  try {
    const ffmpegStatic = require('ffmpeg-static');
    if (ffmpegStatic && fs.existsSync(ffmpegStatic)) return ffmpegStatic;
  } catch (_) {}

  const localFallback = path.join('C:', 'tmp', 'ai_thcs_smoke', 'node_modules', 'ffmpeg-static', 'ffmpeg.exe');
  if (fs.existsSync(localFallback)) return localFallback;

  throw new Error('ffmpeg not found. Set FFMPEG_PATH or install ffmpeg-static in the runtime used to run this script.');
}

function runFfmpeg(args, label, options = {}) {
  const result = spawnSync(resolveFfmpeg(), args, {
    encoding: options.binaryStdout ? null : 'utf8',
    maxBuffer: 128 * 1024 * 1024,
  });
  if (result.status !== 0) {
    const stderr = Buffer.isBuffer(result.stderr) ? result.stderr.toString('utf8') : result.stderr;
    const stdout = Buffer.isBuffer(result.stdout) ? result.stdout.toString('utf8') : result.stdout;
    throw new Error(`${label} failed\n${stderr || stdout}`);
  }
  return result;
}

async function loadProject(page, sb3Path) {
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace && window.Blockly.getMainWorkspace(), { timeout: 90000 });
  await page.waitForTimeout(2500);

  await page.getByText('File', { exact: true }).click();
  const chooserPromise = page.waitForEvent('filechooser');
  await page.getByText('Load from your computer', { exact: true }).click();
  const chooser = await chooserPromise;
  await chooser.setFiles(sb3Path);

  const expectedTitle = path.basename(sb3Path, '.sb3');
  await page.waitForFunction(
    (title) => document.querySelector('input[class*="project-title"]')?.value === title,
    expectedTitle,
    { timeout: 30000 }
  );
  await page.waitForTimeout(2500);
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

async function captureLoop(page, frameDir, stopSignal) {
  let index = 0;
  let lastError = null;
  while (!stopSignal.stop) {
    const framePath = path.join(frameDir, `frame_${String(index).padStart(4, '0')}.png`);
    try {
      await page.screenshot({ path: framePath });
      index += 1;
    } catch (error) {
      lastError = error;
      break;
    }
    await page.waitForTimeout(Math.round(1000 / FPS));
  }
  if (lastError) throw lastError;
  return index;
}

function encodeFrames(frameDir, outputPath) {
  runFfmpeg([
    '-y',
    '-framerate', String(FPS),
    '-i', path.join(frameDir, 'frame_%04d.png'),
    '-c:v', 'libvpx',
    '-pix_fmt', 'yuv420p',
    '-b:v', '1600k',
    outputPath,
  ], `encoding ${outputPath}`);
}

function verifyVideoMotion(videoPath) {
  const frameBytes = VERIFY_WIDTH * VERIFY_HEIGHT * 3;
  const result = runFfmpeg([
    '-i', videoPath,
    '-vf', `fps=1,scale=${VERIFY_WIDTH}:${VERIFY_HEIGHT}`,
    '-f', 'rawvideo',
    '-pix_fmt', 'rgb24',
    '-',
  ], `verifying ${videoPath}`, { binaryStdout: true });

  const raw = result.stdout;
  const frameCount = Math.floor(raw.length / frameBytes);
  if (frameCount < 2) {
    throw new Error(`Motion verification failed for ${videoPath}: only ${frameCount} frame(s) decoded`);
  }

  let maxChangedPercent = 0;
  for (let frame = 1; frame < frameCount; frame += 1) {
    let changed = 0;
    const offset = frame * frameBytes;
    for (let pixel = 0; pixel < frameBytes; pixel += 3) {
      const delta =
        Math.abs(raw[offset + pixel] - raw[pixel]) +
        Math.abs(raw[offset + pixel + 1] - raw[pixel + 1]) +
        Math.abs(raw[offset + pixel + 2] - raw[pixel + 2]);
      if (delta > 30) changed += 1;
    }
    const changedPercent = (changed / (VERIFY_WIDTH * VERIFY_HEIGHT)) * 100;
    maxChangedPercent = Math.max(maxChangedPercent, changedPercent);
  }

  if (maxChangedPercent < VERIFY_MIN_CHANGED_PERCENT) {
    throw new Error(`Motion verification failed for ${videoPath}: max changed pixels ${maxChangedPercent.toFixed(3)}%`);
  }

  return { frameCount, maxChangedPercent: Number(maxChangedPercent.toFixed(3)) };
}

async function recordOne(browser, item) {
  const sb3Path = path.join(MEDIA_DIR, `bt${item.id}_code.sb3`);
  if (!fs.existsSync(sb3Path)) throw new Error(`Missing SB3 for BT${item.id}: ${sb3Path}`);

  const context = await browser.newContext({
    viewport: { width: VIDEO_WIDTH, height: VIDEO_HEIGHT },
    permissions: ['camera', 'microphone'],
  });
  const page = await context.newPage();
  const frameDir = fs.mkdtempSync(path.join(os.tmpdir(), `ai-thcs-bt${item.id}-frames-`));
  const finalPath = path.join(MEDIA_DIR, `bt${item.id}_demo.webm`);
  const stopSignal = { stop: false };
  let capturePromise = null;
  try {
    await loadProject(page, sb3Path);
    await enterFullScreen(page);
    capturePromise = captureLoop(page, frameDir, stopSignal);
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
  } finally {
    stopSignal.stop = true;
    if (capturePromise) await capturePromise;
    await context.close();
  }

  if (fs.existsSync(finalPath)) fs.unlinkSync(finalPath);
  const frames = fs.readdirSync(frameDir).filter((file) => file.endsWith('.png')).length;
  if (frames < 2) throw new Error(`BT${item.id}: only ${frames} screenshot frame(s) captured`);
  encodeFrames(frameDir, finalPath);
  const verification = verifyVideoMotion(finalPath);
  fs.rmSync(frameDir, { recursive: true, force: true });
  console.log(`BT${item.id}: video saved ${finalPath}; frames=${frames}; motion=${verification.maxChangedPercent}%`);
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
