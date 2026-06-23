const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const outDir = path.resolve('..', 'GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 800, height: 600 } });
  
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
    await page.mouse.click(20, 570);
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
  await page.waitForTimeout(8000);

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

  // Nạp khối lệnh go to [nose bridge] (ID 11) cho Câu 17
  const xmlContent = `<xml xmlns="http://www.w3.org/1999/xhtml">
    <block type="poseFace_affdexGoToPart" id="q17_goto" x="50" y="50">
      <field name="AFFDEX_POINT">11</field>
    </block>
  </xml>`;

  console.log("Rendering Q17 block (nose bridge)...");
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
  const padding = 8;
  if (boundingBox) {
    console.log(`Bounding Box found: `, boundingBox);
    await page.screenshot({
      path: path.join(outDir, 'cau_17_a.png'),
      clip: {
        x: Math.max(0, boundingBox.x - padding),
        y: Math.max(0, boundingBox.y - padding),
        width: boundingBox.width + (padding * 2),
        height: boundingBox.height + (padding * 2)
      }
    });
  } else {
    console.log("No bounding box, taking full screen screenshot");
    await page.screenshot({ path: path.join(outDir, 'cau_17_a.png') });
  }

  await browser.close();
  console.log("Done rendering Q17 crop!");
})();
