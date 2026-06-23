const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  console.log('=== Testing SB3 Export ===');
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

  // Check what global variables are available
  const globals = await page.evaluate(() => {
    const keys = Object.keys(window);
    const result = {};
    for (const key of keys) {
      if (key.toLowerCase().includes('vm') || key.toLowerCase().includes('scratch') || key.toLowerCase().includes('gui')) {
        result[key] = typeof window[key];
      }
    }
    // Also check common scratch-gui paths
    if (window.vm) {
      result['vm_methods'] = Object.getOwnPropertyNames(Object.getPrototypeOf(window.vm)).filter(m => typeof window.vm[m] === 'function');
    }
    return result;
  });
  console.log('Global variables related to VM/Scratch:', JSON.stringify(globals, null, 2));

  // Try to find the File menu and click it
  console.log('Looking for File menu...');
  const menuItems = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('*'))
      .filter(el => el.textContent && el.textContent.trim() === 'File')
      .map(el => ({
        tag: el.tagName,
        className: el.className,
        parent: el.parentElement ? el.parentElement.className : ''
      }));
  });
  console.log('File menu candidates:', JSON.stringify(menuItems, null, 2));

  await browser.close();
})();
