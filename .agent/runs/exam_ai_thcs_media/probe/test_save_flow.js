const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const admZip = require('adm-zip'); // We can check if adm-zip is available or write a quick zip checker

const OUT_DIR = path.resolve(__dirname, '..');

(async () => {
  console.log('=== Testing Save to your computer Flow ===');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'domcontentloaded', timeout: 90000
  });

  await page.waitForFunction(() =>
    window.Blockly &&
    typeof window.Blockly.getMainWorkspace === 'function' &&
    window.Blockly.getMainWorkspace()
  , { timeout: 90000 });

  await page.waitForTimeout(3000);

  // Load Text to Speech extension
  console.log('Loading Text to Speech...');
  try {
    await page.click('[class*="extension-button"]', { timeout: 5000 });
    await page.waitForTimeout(2000);
    const card = page.locator('text="Text to Speech"').first();
    await card.click({ timeout: 5000 });
    await page.waitForTimeout(3000);
    console.log('Extension loaded.');
  } catch (e) {
    console.log('Failed to load extension:', e.message);
  }

  // Inject a simple XML
  console.log('Injecting XML...');
  const xml = `<xml xmlns="http://www.w3.org/1999/xhtml">
    <block type="event_whenflagclicked" id="test_start" x="40" y="40">
      <next>
        <block type="text2speech_speakAndWait" id="test_speak">
          <value name="WORDS"><shadow type="text"><field name="TEXT">Hello world</field></shadow></value>
        </block>
      </next>
    </block>
  </xml>`;

  await page.evaluate((xmlText) => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    ws.clear();
    const dom = B.Xml.textToDom(xmlText);
    B.Xml.domToWorkspace(dom, ws);
    ws.render();
  }, xml);

  await page.waitForTimeout(2000);

  // Take screenshot for debug
  await page.screenshot({ path: path.join(__dirname, 'debug_before_save.png') });

  // Click File menu
  console.log('Clicking File...');
  const fileMenu = page.locator('div').filter({ hasText: /^File$/ }).first();
  await fileMenu.click();
  await page.waitForTimeout(1000);

  // Click Save to your computer and wait for download
  console.log('Clicking Save to your computer...');
  const saveOption = page.locator('li').filter({ hasText: /Save to your computer/i }).first();
  
  // Set up download listener
  const downloadPromise = page.waitForEvent('download');
  await saveOption.click();
  const download = await downloadPromise;

  const downloadPath = path.join(__dirname, 'test.sb3');
  await download.saveAs(downloadPath);
  console.log('Download completed:', downloadPath);

  // Inspect the sb3 file using adm-zip to see if project.json contains blocks
  try {
    const zip = new admZip(downloadPath);
    const zipEntries = zip.getEntries();
    console.log('Zip contents:', zipEntries.map(e => e.entryName));
    const projectJsonEntry = zip.getEntry('project.json');
    if (projectJsonEntry) {
      const projectJsonText = projectJsonEntry.getData().toString('utf8');
      const project = JSON.parse(projectJsonText);
      
      // Let's count targets and blocks
      console.log('Number of targets:', project.targets.length);
      for (const target of project.targets) {
        console.log(`Target: ${target.name}, Blocks count: ${Object.keys(target.blocks || {}).length}`);
      }
    }
  } catch (err) {
    console.error('Failed to read sb3 zip:', err.message);
  }

  await browser.close();
})();
