const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

  console.log('Loading page...');
  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'domcontentloaded', timeout: 90000
  });

  await page.waitForFunction(() =>
    window.Blockly &&
    typeof window.Blockly.getMainWorkspace === 'function' &&
    window.Blockly.getMainWorkspace()
  , { timeout: 90000 });

  await page.waitForTimeout(3000);

  // Load extensions
  console.log('Loading extensions...');
  // Click Add Extension button
  await page.click('[class*="extension-button"]');
  await page.waitForTimeout(1000);
  await page.click('text="Text to Speech"');
  await page.waitForTimeout(2000);

  await page.click('[class*="extension-button"]');
  await page.waitForTimeout(1000);
  await page.click('text="Translate"');
  await page.waitForTimeout(2000);

  // XML with explicit variables
  const xml = `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_lang" islocal="false" iscloud="false">NgonNgu</variable>
    <variable type="broadcast_msg" id="msg_canh2" islocal="false" iscloud="false">Canh 2</variable>
  </variables>
  
  <block type="event_whenflagclicked" id="bt2_start" x="40" y="40">
    <next>
      <block type="sensing_askandwait" id="bt2_ask_lang">
        <value name="QUESTION">
          <shadow type="text">
            <field name="TEXT">Chon ngon ngu: 1-Tieng Viet / 2-Tieng Anh</field>
          </shadow>
        </value>
        <next>
          <block type="data_setvariableto" id="bt2_set_lang">
            <field name="VARIABLE" id="var_lang" variabletype="">NgonNgu</field>
            <value name="VALUE">
              <block type="sensing_answer" id="bt2_ans_lang"></block>
            </value>
            <next>
              <block type="looks_switchbackdropto" id="bt2_backdrop1">
                <value name="BACKDROP">
                  <shadow type="looks_backdrop">
                    <field name="BACKDROP">Canh 1</field>
                  </shadow>
                </value>
                <next>
                  <block type="control_if_else" id="bt2_if_lang1">
                    <value name="CONDITION">
                      <block type="operator_equals" id="bt2_eq1">
                        <value name="OPERAND1">
                          <block type="data_variable" id="bt2_lang_var">
                            <field name="VARIABLE" id="var_lang" variabletype="">NgonNgu</field>
                          </block>
                        </value>
                        <value name="OPERAND2">
                          <shadow type="text">
                            <field name="TEXT">2</field>
                          </shadow>
                        </value>
                      </block>
                    </value>
                    <statement name="SUBSTACK">
                      <block type="text2speech_speakAndWait" id="bt2_tts_eng1">
                        <value name="WORDS">
                          <block type="translate_getTranslate" id="bt2_trans1">
                            <value name="WORDS">
                              <shadow type="text">
                                <field name="TEXT">Ngay xua ngay xua, co mot chu meo nho...</field>
                              </shadow>
                            </value>
                            <value name="LANGUAGE">
                              <shadow type="translate_menu_languages">
                                <field name="languages">en</field>
                              </shadow>
                            </value>
                          </block>
                        </value>
                      </block>
                    </statement>
                    <statement name="SUBSTACK2">
                      <block type="text2speech_speakAndWait" id="bt2_tts_viet1">
                        <value name="WORDS">
                          <shadow type="text">
                            <field name="TEXT">Ngay xua ngay xua, co mot chu meo nho...</field>
                          </shadow>
                        </value>
                      </block>
                    </statement>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>

  <block type="event_whenbroadcastreceived" id="bt2_canh2" x="520" y="40">
    <field name="BROADCAST_OPTION" id="msg_canh2" variabletype="broadcast_msg">Canh 2</field>
    <next>
      <block type="looks_switchbackdropto" id="bt2_backdrop2">
        <value name="BACKDROP">
          <shadow type="looks_backdrop">
            <field name="BACKDROP">Canh 2</field>
          </shadow>
        </value>
        <next>
          <block type="control_if_else" id="bt2_if_lang2">
            <value name="CONDITION">
              <block type="operator_equals" id="bt2_eq2">
                <value name="OPERAND1">
                  <block type="data_variable" id="bt2_lang_var2">
                    <field name="VARIABLE" id="var_lang" variabletype="">NgonNgu</field>
                  </block>
                </value>
                <value name="OPERAND2">
                  <shadow type="text">
                    <field name="TEXT">2</field>
                  </shadow>
                </value>
              </block>
            </value>
            <statement name="SUBSTACK">
              <block type="text2speech_speakAndWait" id="bt2_tts_eng2">
                <value name="WORDS">
                  <block type="translate_getTranslate" id="bt2_trans2">
                    <value name="WORDS">
                      <shadow type="text">
                        <field name="TEXT">Chu meo gap mot ban moi la chu cho...</field>
                      </shadow>
                    </value>
                    <value name="LANGUAGE">
                      <shadow type="translate_menu_languages">
                        <field name="languages">en</field>
                      </shadow>
                    </value>
                  </block>
                </value>
              </block>
            </statement>
            <statement name="SUBSTACK2">
              <block type="text2speech_speakAndWait" id="bt2_tts_viet2">
                <value name="WORDS">
                  <shadow type="text">
                    <field name="TEXT">Chu meo gap mot ban moi la chu cho...</field>
                  </shadow>
                </value>
              </block>
            </statement>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>`;

  console.log('Injecting XML...');
  try {
    const renderedXml = await page.evaluate((xmlText) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const dom = B.Xml.textToDom(xmlText);
      B.Xml.domToWorkspace(dom, ws);
      ws.render();
      return new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws));
    }, xml);

    console.log('[PASS] XML injection succeeded!');
    await page.screenshot({ path: path.join(__dirname, '..', 'bt2_test.png'), fullPage: true });
    console.log('Screenshot saved as bt2_test.png');
  } catch (err) {
    console.error('[FAIL] XML injection failed:', err.message);
  }

  await browser.close();
})();
