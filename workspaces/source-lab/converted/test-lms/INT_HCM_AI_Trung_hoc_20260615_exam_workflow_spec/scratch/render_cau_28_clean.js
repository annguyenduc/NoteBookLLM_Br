const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const outDir = path.resolve('..', 'GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media');
  const xmlPath = path.join(outDir, 'cau_28.xml');
  
  if (!fs.existsSync(xmlPath)) {
    console.error("XML file not found: " + xmlPath);
    process.exit(1);
  }
  
  const xmlContent = fs.readFileSync(xmlPath, 'utf8');
  console.log("Read XML from " + xmlPath);

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1000, height: 1000 } });
  
  console.log("Navigating to playground...");
  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'networkidle',
    timeout: 60000
  });

  await page.waitForFunction(() => {
    return (
      window.Blockly &&
      typeof window.Blockly.getMainWorkspace === 'function' &&
      window.Blockly.getMainWorkspace()
    );
  }, { timeout: 60000 });

  console.log("Loading Face Sensing extension...");
  const addExtBtn = await page.locator('[class*="gui_extension-button"]').first();
  if (await addExtBtn.count() > 0) {
    await addExtBtn.click();
  } else {
    await page.mouse.click(20, 970);
  }

  await page.waitForTimeout(2000);

  const faceSensingCard = page.locator('text="Face Sensing"').first();
  if (await faceSensingCard.count() > 0) {
    await faceSensingCard.click();
  } else {
    const cards = page.locator('[class*="library_library-item"]');
    const texts = await cards.allTextContents();
    const idx = texts.findIndex(t => t.includes("Face Sensing"));
    if (idx !== -1) {
      await cards.nth(idx).click();
    }
  }

  console.log("Waiting for extension to load...");
  await page.waitForTimeout(10000);

  // Apply CSS to hide UI components
  console.log("Applying styles to hide UI...");
  await page.evaluate(() => {
    const style = document.createElement('style');
    style.innerHTML = `
      [class*="gui_menu-bar"] { display: none !important; }
      [class*="gui_stage-and-target-wrapper"] { display: none !important; }
      [class*="gui_sidebar"] { display: none !important; }
      .blocklyToolboxDiv { display: none !important; }
      .blocklyFlyout { display: none !important; }
      body { background-color: #e0f2fe !important; }
      [class*="gui_blocks-wrapper"] {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: 9999 !important;
      }
      .blocklyScrollbarBackground { display: none !important; }
      .blocklyScrollbarHandle { display: none !important; }
      .blocklyZoom { display: none !important; }
    `;
    document.head.appendChild(style);
  });

  console.log("Rendering Q28 block...");
  await page.evaluate((xml) => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    ws.clear();
    const dom = B.Xml.textToDom(xml);
    B.Xml.domToWorkspace(dom, ws);
    ws.render();
    ws.scrollX = 0;
    ws.scrollY = 0;
    if (ws.zoomToFit) ws.zoomToFit();
  }, xmlContent);

  await page.waitForTimeout(2000);
  const blockCanvas = page.locator('.blocklyBlockCanvas').first();
  const boundingBox = await blockCanvas.boundingBox();
  const padding = 40;
  if (boundingBox) {
    await page.screenshot({
      path: path.join(outDir, 'cau_28.png'),
      clip: {
        x: Math.max(0, boundingBox.x - padding),
        y: Math.max(0, boundingBox.y - padding),
        width: boundingBox.width + (padding * 2),
        height: boundingBox.height + (padding * 2)
      }
    });
    // Save raw screenshot
    await page.screenshot({
      path: path.join(outDir, 'cau_28.raw.png'),
      clip: {
        x: Math.max(0, boundingBox.x - padding),
        y: Math.max(0, boundingBox.y - padding),
        width: boundingBox.width + (padding * 2),
        height: boundingBox.height + (padding * 2)
      }
    });
    console.log("Chụp thành công cau_28.png sạch không có viền đỏ.");
  } else {
    await page.screenshot({ path: path.join(outDir, 'cau_28.png') });
    await page.screenshot({ path: path.join(outDir, 'cau_28.raw.png') });
  }

  await browser.close();
  console.log("Done rendering Q28 clean!");
})();
