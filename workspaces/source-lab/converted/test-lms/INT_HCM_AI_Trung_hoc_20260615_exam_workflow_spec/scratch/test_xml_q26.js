const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 60000 });
  await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace());
  
  // Load Face Sensing
  console.log("Loading Face Sensing...");
  const addExtBtn = await page.locator('[class*="gui_extension-button"]').first();
  if (await addExtBtn.count() > 0) {
    await addExtBtn.click();
    await page.waitForTimeout(2000);
    const faceSensingCard = page.locator('text="Face Sensing"').first();
    await faceSensingCard.click();
    await page.waitForTimeout(6000);
  }

  // Test XML rendering
  const testXml = async (xmlStr, label) => {
    const res = await page.evaluate((xml) => {
      try {
        const B = window.Blockly;
        const ws = B.getMainWorkspace();
        ws.clear();
        const dom = B.Xml.textToDom(xml);
        B.Xml.domToWorkspace(dom, ws);
        return { success: true };
      } catch (err) {
        return { success: false, error: err.message };
      }
    }, xmlStr);
    console.log(`Test ${label}:`, res);
  };

  // xmlD4: Nối sound_play với change variable
  const xmlD4 = `<xml xmlns="http://www.w3.org/1999/xhtml">
    <variables>
      <variable type="" id="q26_var_score">Điểm</variable>
    </variables>
    <block type="sound_play" id="q26_sound" x="150" y="150">
      <value name="SOUND_MENU">
        <shadow type="sound_sounds_menu" id="sound_val_26">
          <field name="SOUND_MENU">pop</field>
        </shadow>
      </value>
      <next>
        <block type="data_changevariableby" id="q26_change">
          <field name="VARIABLE" id="q26_var_score">Điểm</field>
          <value name="VALUE">
            <shadow type="math_number" id="num_val_26">
              <field name="NUM">1</field>
            </shadow>
          </value>
        </block>
      </next>
    </block>
  </xml>`;

  await testXml(xmlD4, "xmlD4 (sound_play + change var)");

  await browser.close();
})();
