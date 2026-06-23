/**
 * generate_bt1_v2.js
 * Fix: Load extensions via UI click BEFORE XML injection
 * Per README rule: "load extension only if opcode or block type is missing"
 * 
 * This script handles BT1 first as a probe.
 * Extensions needed: translate, text2speech
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT_DIR = path.resolve(__dirname, '..');

// Extension display names as shown in PRG AI Blocks UI
const EXTENSION_MAP = {
  translate: 'Translate',
  text2speech: 'Text to Speech',
  faceSensing: 'Face Sensing',
  bodySensing: 'Body Sensing',
  teachableMachine: 'Teachable Machine'
};

async function loadExtensions(page, extensionNames) {
  for (const extName of extensionNames) {
    console.log(`  Loading extension: ${extName}...`);
    try {
      // Click "Add Extension" button
      await page.click('[class*="addButton"], [title*="Add Extension"], button:has-text("Add Extension")', { timeout: 10000 });
      await page.waitForTimeout(1000);

      // Find and click the extension card
      const displayName = EXTENSION_MAP[extName] || extName;
      const card = page.locator(`[class*="extensionCard"]:has-text("${displayName}"), .card:has-text("${displayName}")`).first();
      
      if (await card.isVisible({ timeout: 5000 })) {
        await card.click();
        await page.waitForTimeout(2000);
        console.log(`  [OK] Extension loaded: ${displayName}`);
      } else {
        console.log(`  [WARN] Extension card not found: ${displayName}`);
      }
    } catch (err) {
      console.log(`  [WARN] Failed to load extension ${extName}: ${err.message.substring(0, 80)}`);
    }
  }
}

async function generateExercise(browser, exerciseId, xmlContent, description, extensions) {
  console.log(`\n[BT${exerciseId}] ${description}`);

  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'domcontentloaded',
    timeout: 90000
  });

  await page.waitForFunction(() => {
    return (
      window.Blockly &&
      typeof window.Blockly.getMainWorkspace === 'function' &&
      window.Blockly.getMainWorkspace()
    );
  }, { timeout: 90000 });

  await page.waitForTimeout(3000);
  console.log('  [OK] Blockly workspace ready');

  // Load required extensions first
  if (extensions && extensions.length > 0) {
    await loadExtensions(page, extensions);
    await page.waitForTimeout(2000);
  }

  // Inject XML
  console.log('  Injecting XML...');
  let renderedXml;
  try {
    renderedXml = await page.evaluate((xml) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const dom = B.Xml.textToDom(xml);
      B.Xml.domToWorkspace(dom, ws);
      ws.render();
      return new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws));
    }, xmlContent);
    console.log('  [OK] XML injected');
  } catch (err) {
    // Take screenshot of failure for debugging
    const failPath = path.join(OUT_DIR, `bt${exerciseId}_fail.png`);
    await page.screenshot({ path: failPath, fullPage: false });
    console.log(`  [FAIL] XML injection error. Debug screenshot: ${path.basename(failPath)}`);
    await page.close();
    throw err;
  }

  await page.waitForTimeout(2000);

  // Save PNG
  const pngPath = path.join(OUT_DIR, `bt${exerciseId}_code.raw.png`);
  await page.screenshot({ path: pngPath, fullPage: true });
  console.log(`  [OK] PNG saved: ${path.basename(pngPath)}`);

  // Save XML
  const xmlPath = path.join(OUT_DIR, `bt${exerciseId}_code.xml`);
  fs.writeFileSync(xmlPath, renderedXml, 'utf8');
  console.log(`  [OK] XML saved: ${path.basename(xmlPath)}`);

  await page.close();
  return { pngPath, xmlPath };
}

// BT1 XML — simplified to avoid deep nesting issues
// Focus: event_whenflagclicked + data_setvariableto + control_repeat + sensing_askandwait + translate + text2speech + control_if_else
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
                <value name="QUESTION"><shadow type="text"><field name="TEXT">Nhap tu tieng Viet:</field></shadow></value>
                <next>
                  <block type="text2speech_speakAndWait" id="bt1_tts_translate">
                    <value name="WORDS">
                      <block type="translate_getTranslate" id="bt1_trans">
                        <value name="WORDS"><block type="sensing_answer" id="bt1_ans_src"></block></value>
                        <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                      </block>
                    </value>
                    <next>
                      <block type="sensing_askandwait" id="bt1_ask_eng">
                        <value name="QUESTION"><shadow type="text"><field name="TEXT">Go lai tieng Anh vua nghe:</field></shadow></value>
                        <next>
                          <block type="control_if_else" id="bt1_if_check">
                            <value name="CONDITION">
                              <block type="operator_equals" id="bt1_eq">
                                <value name="OPERAND1"><block type="sensing_answer" id="bt1_ans_check"></block></value>
                                <value name="OPERAND2">
                                  <block type="translate_getTranslate" id="bt1_trans2">
                                    <value name="WORDS"><block type="sensing_answer" id="bt1_ans_src2"></block></value>
                                    <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <statement name="SUBSTACK">
                              <block type="text2speech_speakAndWait" id="bt1_tts_correct">
                                <value name="WORDS"><shadow type="text"><field name="TEXT">Correct! +1</field></shadow></value>
                                <next>
                                  <block type="data_changevariableby" id="bt1_inc_score">
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
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>`;

(async () => {
  console.log('=== PRG AI Blocks v2 — BT1 Probe (with extension loading) ===');
  const browser = await chromium.launch({ headless: true });

  try {
    await generateExercise(
      browser,
      1,
      BT1_XML,
      'BT1 - Chatbot hoc tu vung (Translate + TTS + Loop 5 + If)',
      ['translate', 'text2speech']
    );
    console.log('\n[PASS] BT1 completed successfully.');
  } catch (err) {
    console.error(`\n[FAIL] BT1 error: ${err.message.substring(0, 200)}`);
  }

  await browser.close();
  console.log('Status: PREVIEW_ONLY — Human review required.');
})();
