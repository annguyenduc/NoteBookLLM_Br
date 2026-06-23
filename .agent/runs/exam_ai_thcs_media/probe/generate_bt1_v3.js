/**
 * generate_bt1_v3.js
 * Fix v3: Correct selectors from real debug screenshot
 * The extension library IS opening (screenshot shows it)
 * Issue: card click selector wrong. Use text-based locator.
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT_DIR = path.resolve(__dirname, '..');

async function loadExtension(page, displayName) {
  console.log(`  Loading extension: ${displayName}...`);
  
  // The extension library is already open OR we need to click Add Extension
  // Find the extension card by its text title (h2/h3/div with the name)
  // From the debug screenshot, cards show title text directly
  
  // Try to click card - the card contains the extension name in a text element
  // Playwright: find element that contains text, is clickable, looks like a card
  const card = page.locator('div').filter({ hasText: new RegExp(`^${displayName}$`) }).first();
  
  try {
    await card.click({ timeout: 5000 });
    await page.waitForTimeout(2000);
    console.log(`  [OK] Clicked card: ${displayName}`);
    return true;
  } catch (e) {
    console.log(`  [WARN] Card click failed for ${displayName}: ${e.message.substring(0, 100)}`);
    
    // Try alternative: find by role=button or any clickable containing the text
    try {
      await page.click(`text="${displayName}"`, { timeout: 3000 });
      await page.waitForTimeout(2000);
      console.log(`  [OK] Text-click worked for: ${displayName}`);
      return true;
    } catch (e2) {
      console.log(`  [WARN] Text-click also failed: ${e2.message.substring(0, 80)}`);
      return false;
    }
  }
}

async function openExtensionLibrary(page) {
  // The Add Extension button in Scratch-style UI
  // From screenshot: the library opened, so this worked. But our selector was broad.
  // Try multiple known selectors:
  const selectors = [
    '[class*="addExtension"]',
    '[class*="extension-button"]', 
    '[class*="extensionButton"]',
    'button[class*="add"]',
    // Scratch GUI specific
    '.scratch-gui_extension-button__',
    // Generic - any button with title
    '[title*="extension"]',
    '[title*="Extension"]',
    // Icon button at bottom of toolbox
    '[class*="toolbox"] button:last-child',
    '[class*="blocklyToolbox"] + * button',
  ];
  
  for (const sel of selectors) {
    try {
      const el = page.locator(sel).first();
      if (await el.isVisible({ timeout: 2000 })) {
        await el.click();
        await page.waitForTimeout(1500);
        console.log(`  [OK] Opened extension library with selector: ${sel}`);
        return true;
      }
    } catch (e) {
      // continue
    }
  }
  
  // Last resort: try clicking bottom-left area of the Blockly toolbox
  try {
    await page.mouse.click(30, page.viewportSize().height - 50);
    await page.waitForTimeout(1500);
    return true;
  } catch (e) {
    return false;
  }
}

async function loadExtensions(page, extensionNames) {
  for (const extName of extensionNames) {
    // Open extension library for each extension
    const opened = await openExtensionLibrary(page);
    if (!opened) {
      console.log(`  [WARN] Could not open extension library for: ${extName}`);
      continue;
    }
    
    await page.waitForTimeout(1000);
    const loaded = await loadExtension(page, extName);
    if (!loaded) {
      // Take debug screenshot
      await page.screenshot({ path: path.join(OUT_DIR, `debug_ext_${extName}.png`), fullPage: false });
      console.log(`  [DEBUG] Saved extension picker screenshot for: ${extName}`);
      
      // Try Back button and continue
      try {
        await page.click('[class*="back"], button:has-text("Back")', { timeout: 3000 });
        await page.waitForTimeout(1000);
      } catch (e) {}
    }
    
    await page.waitForTimeout(1500);
  }
}

// BT1 XML - simple version with extensions
// Using known-good block types for standard Scratch + translate + text2speech
const BT1_XML = `<xml xmlns="http://www.w3.org/1999/xhtml">
  <block type="event_whenflagclicked" id="bt1_start" x="40" y="40">
    <next>
      <block type="data_setvariableto" id="bt1_set_diem">
        <field name="VARIABLE">Diem</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
        <next>
          <block type="control_repeat" id="bt1_loop5">
            <value name="TIMES"><shadow type="math_number"><field name="NUM">5</field></shadow></value>
            <statement name="SUBSTACK">
              <block type="sensing_askandwait" id="bt1_ask_viet">
                <value name="QUESTION"><shadow type="text"><field name="TEXT">Nhap tu tieng Viet muon hoc:</field></shadow></value>
                <next>
                  <block type="text2speech_speakAndWait" id="bt1_tts_say">
                    <value name="WORDS">
                      <block type="translate_getTranslate" id="bt1_trans">
                        <value name="WORDS"><block type="sensing_answer" id="bt1_ans_s"></block></value>
                        <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                      </block>
                    </value>
                    <next>
                      <block type="sensing_askandwait" id="bt1_ask_eng">
                        <value name="QUESTION"><shadow type="text"><field name="TEXT">Go lai tu tieng Anh vua nghe:</field></shadow></value>
                        <next>
                          <block type="control_if_else" id="bt1_if_check">
                            <value name="CONDITION">
                              <block type="operator_equals" id="bt1_eq">
                                <value name="OPERAND1"><block type="sensing_answer" id="bt1_ans_c"></block></value>
                                <value name="OPERAND2">
                                  <block type="translate_getTranslate" id="bt1_trans2">
                                    <value name="WORDS"><block type="sensing_answer" id="bt1_ans_s2"></block></value>
                                    <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <statement name="SUBSTACK">
                              <block type="text2speech_speakAndWait" id="bt1_tts_correct">
                                <value name="WORDS"><shadow type="text"><field name="TEXT">Correct! +1 diem!</field></shadow></value>
                                <next>
                                  <block type="data_changevariableby" id="bt1_inc">
                                    <field name="VARIABLE">Diem</field>
                                    <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                                  </block>
                                </next>
                              </block>
                            </statement>
                            <statement name="SUBSTACK2">
                              <block type="text2speech_speakAndWait" id="bt1_tts_wrong">
                                <value name="WORDS"><shadow type="text"><field name="TEXT">Sai roi! Thu lai nhe.</field></shadow></value>
                              </block>
                            </statement>
                          </block>
                        </next>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </statement>
            <next>
              <block type="text2speech_speakAndWait" id="bt1_tts_total">
                <value name="WORDS">
                  <block type="operator_join" id="bt1_join">
                    <value name="STRING1"><shadow type="text"><field name="TEXT">Ban dat </field></shadow></value>
                    <value name="STRING2">
                      <block type="operator_join" id="bt1_join2">
                        <value name="STRING1"><block type="data_variable" id="bt1_score"><field name="VARIABLE">Diem</field></block></value>
                        <value name="STRING2"><shadow type="text"><field name="TEXT"> tren 5 diem!</field></shadow></value>
                      </block>
                    </value>
                  </block>
                </value>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>`;

(async () => {
  console.log('=== PRG AI Blocks v3 — BT1 Probe (fixed selectors) ===');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'domcontentloaded',
    timeout: 90000
  });

  await page.waitForFunction(() => {
    return window.Blockly &&
      typeof window.Blockly.getMainWorkspace === 'function' &&
      window.Blockly.getMainWorkspace();
  }, { timeout: 90000 });

  await page.waitForTimeout(3000);
  
  // Take initial screenshot to see UI state
  await page.screenshot({ path: path.join(OUT_DIR, 'debug_initial.png'), fullPage: false });
  console.log('  [DEBUG] Saved initial page screenshot');

  // Print all buttons on page for debugging
  const buttons = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('button, [role="button"]'))
      .map(el => ({
        tag: el.tagName,
        class: el.className.substring(0, 80),
        text: el.textContent.trim().substring(0, 40),
        title: el.title || '',
        visible: el.offsetParent !== null
      }))
      .filter(el => el.visible);
  });
  console.log('  [DEBUG] Visible buttons:');
  buttons.slice(0, 20).forEach(b => console.log(`    - [${b.tag}] class="${b.class}" text="${b.text}" title="${b.title}"`) );

  await loadExtensions(page, ['Text to Speech', 'Translate']);
  
  // Take screenshot after extension loading
  await page.screenshot({ path: path.join(OUT_DIR, 'debug_after_ext.png'), fullPage: false });
  console.log('  [DEBUG] Saved post-extension screenshot');

  // Try XML injection
  console.log('  Injecting XML...');
  try {
    const renderedXml = await page.evaluate((xml) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const dom = B.Xml.textToDom(xml);
      B.Xml.domToWorkspace(dom, ws);
      ws.render();
      return new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws));
    }, BT1_XML);

    await page.waitForTimeout(2000);
    const pngPath = path.join(OUT_DIR, 'bt1_code.raw.png');
    await page.screenshot({ path: pngPath, fullPage: true });
    fs.writeFileSync(path.join(OUT_DIR, 'bt1_code.xml'), renderedXml, 'utf8');
    console.log('[PASS] BT1 completed: bt1_code.raw.png + bt1_code.xml saved.');
  } catch (err) {
    await page.screenshot({ path: path.join(OUT_DIR, 'bt1_fail_v3.png'), fullPage: false });
    console.error(`[FAIL] XML injection error: ${err.message.substring(0, 300)}`);
  }

  await browser.close();
})();
