const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT_DIR = path.resolve(__dirname, '..');

async function openExtensionLibrary(page) {
  try {
    await page.click('[class*="extension-button"]', { timeout: 8000 });
    await page.waitForTimeout(2000);
    return true;
  } catch (e) {
    console.log(`  [WARN] Could not open extension library: ${e.message.substring(0, 60)}`);
    return false;
  }
}

async function loadExtension(page, displayName) {
  const opened = await openExtensionLibrary(page);
  if (!opened) return false;
  await page.waitForTimeout(1500); // Wait for cards to fully render
  try {
    const card = page.locator(`text="${displayName}"`).first();
    await card.scrollIntoViewIfNeeded({ timeout: 3000 });
    await card.click({ timeout: 5000 });
    await page.waitForTimeout(3000); // Wait after loading card
    console.log(`  [OK] Extension loaded: ${displayName}`);
    return true;
  } catch (e) {
    console.log(`  [WARN] Extension click failed for: ${displayName}. Trying fallback...`);
    try {
      await page.click(`text="${displayName}"`, { timeout: 3000 });
      await page.waitForTimeout(2000);
      return true;
    } catch (e2) {
      console.log(`  [FAIL] Failed to load extension: ${displayName}`);
      try { await page.locator('text="Back"').first().click({ timeout: 2000 }); await page.waitForTimeout(500); } catch (e3) {}
      return false;
    }
  }
}

async function addSprite(page, searchName, exactName) {
  console.log(`Adding sprite '${exactName}' from library (searching for '${searchName}')...`);
  const addBtn = page.locator('button[aria-label="Choose a Sprite"]').or(page.locator('button[aria-label="Chọn một nhân vật"]')).first();
  await addBtn.click();
  await page.waitForTimeout(2000);
  
  let searchInput = page.locator('input[placeholder="Search"]').or(page.locator('input[placeholder="Tìm kiếm"]')).first();
  await searchInput.fill(searchName);
  await page.waitForTimeout(2000);
  
  const success = await page.evaluate((name) => {
    const cards = document.querySelectorAll('[class*="library-item_library-item"]');
    for (const card of cards) {
      const span = card.querySelector('[class*="library-item-name"]');
      if (span && span.innerText.trim().toLowerCase() === name.toLowerCase()) {
        card.click();
        return true;
      }
    }
    return false;
  }, exactName);

  if (!success) {
    throw new Error(`Sprite '${exactName}' not found in library!`);
  }
  await page.waitForTimeout(3000);
}

async function addBackdrop(page, searchName, exactName) {
  console.log(`Adding backdrop '${exactName}' from library (searching for '${searchName}')...`);
  const addBtn = page.locator('button[aria-label="Choose a Backdrop"]').or(page.locator('button[aria-label="Chọn một phông nền"]')).first();
  await addBtn.click();
  await page.waitForTimeout(2000);
  
  let searchInput = page.locator('input[placeholder="Search"]').or(page.locator('input[placeholder="Tìm kiếm"]')).first();
  await searchInput.fill(searchName);
  await page.waitForTimeout(2000);
  
  const success = await page.evaluate((name) => {
    const cards = document.querySelectorAll('[class*="library-item_library-item"]');
    for (const card of cards) {
      const span = card.querySelector('[class*="library-item-name"]');
      if (span && span.innerText.trim().toLowerCase() === name.toLowerCase()) {
        card.click();
        return true;
      }
    }
    return false;
  }, exactName);

  if (!success) {
    throw new Error(`Backdrop '${exactName}' not found in library!`);
  }
  await page.waitForTimeout(3000);
}

// BT2 XML: interactive story with 4 scenes, using language variable and scene2/scene3/scene4 broadcasts.
const BT2_XML = `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_lang" islocal="false" iscloud="false">language</variable>
    <variable type="broadcast_msg" id="msg_scene2" islocal="false" iscloud="false">scene2</variable>
    <variable type="broadcast_msg" id="msg_scene3" islocal="false" iscloud="false">scene3</variable>
    <variable type="broadcast_msg" id="msg_scene4" islocal="false" iscloud="false">scene4</variable>
  </variables>

  <!-- CANH 1 -->
  <block type="event_whenflagclicked" id="bt2_start" x="40" y="40">
    <next>
      <block type="sensing_askandwait" id="bt2_ask_lang">
        <value name="QUESTION">
          <shadow type="text">
            <field name="TEXT">Chọn ngôn ngữ (1: Tiếng Việt, 2: Tiếng Anh):</field>
          </shadow>
        </value>
        <next>
          <block type="data_setvariableto" id="bt2_set_lang">
            <field name="VARIABLE" id="var_lang" variabletype="">language</field>
            <value name="VALUE">
              <block type="sensing_answer" id="bt2_ans_lang"></block>
            </value>
            <next>
              <block type="looks_switchbackdropto" id="bt2_backdrop1">
                <value name="BACKDROP">
                  <shadow type="looks_backdrop">
                    <field name="BACKDROP">Forest</field>
                  </shadow>
                </value>
                <next>
                  <block type="looks_switchcostumeto" id="bt2_costume1">
                    <value name="COSTUME">
                      <shadow type="looks_costume">
                        <field name="COSTUME">rabbit-a</field>
                      </shadow>
                    </value>
                    <next>
                      <block type="control_if_else" id="bt2_if_lang1">
                        <value name="CONDITION">
                          <block type="operator_equals" id="bt2_eq1">
                            <value name="OPERAND1">
                              <block type="data_variable" id="bt2_lang_var">
                                <field name="VARIABLE" id="var_lang" variabletype="">language</field>
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
                                    <field name="TEXT">Ngày xửa ngày xưa, một chú thỏ kiêu ngạo luôn tự hào mình chạy nhanh nhất khu rừng và thường chế giễu nhím chậm chạp.</field>
                                  </shadow>
                                </value>
                                <value name="LANGUAGE">
                                  <shadow type="translate_menu_languages">
                                    <field name="languages">en</field>
                                  </shadow>
                                </value>
                              </block>
                            </value>
                            <next>
                              <block type="looks_sayforsecs" id="bt2_say_eng1">
                                <value name="MESSAGE">
                                  <block type="translate_getTranslate" id="bt2_trans1_say">
                                    <value name="WORDS">
                                      <shadow type="text">
                                        <field name="TEXT">Ngày xửa ngày xưa, một chú thỏ kiêu ngạo luôn tự hào mình chạy nhanh nhất khu rừng và thường chế giễu nhím chậm chạp.</field>
                                      </shadow>
                                    </value>
                                    <value name="LANGUAGE">
                                      <shadow type="translate_menu_languages">
                                        <field name="languages">en</field>
                                      </shadow>
                                    </value>
                                  </block>
                                </value>
                                <value name="SECS">
                                  <shadow type="math_number">
                                    <field name="NUM">4</field>
                                  </shadow>
                                </value>
                              </block>
                            </next>
                          </block>
                        </statement>
                        <statement name="SUBSTACK2">
                          <block type="text2speech_speakAndWait" id="bt2_tts_viet1">
                            <value name="WORDS">
                              <shadow type="text">
                                <field name="TEXT">Ngày xửa ngày xưa, một chú thỏ kiêu ngạo luôn tự hào mình chạy nhanh nhất khu rừng và thường chế giễu nhím chậm chạp.</field>
                              </shadow>
                            </value>
                            <next>
                              <block type="looks_sayforsecs" id="bt2_say_viet1">
                                <value name="MESSAGE">
                                  <shadow type="text">
                                    <field name="TEXT">Ngày xửa ngày xưa, một chú thỏ kiêu ngạo luôn tự hào mình chạy nhanh nhất khu rừng và thường chế giễu nhím chậm chạp.</field>
                                  </shadow>
                                </value>
                                <value name="SECS">
                                  <shadow type="math_number">
                                    <field name="NUM">4</field>
                                  </shadow>
                                </value>
                              </block>
                            </next>
                          </block>
                        </statement>
                        <next>
                          <block type="control_wait_until" id="bt2_wait_space1">
                            <value name="CONDITION">
                              <block type="sensing_keypressed" id="bt2_key_space1">
                                <field name="KEY_OPTION">space</field>
                              </block>
                            </value>
                            <next>
                              <block type="event_broadcast" id="bt2_bcast_scene2">
                                <value name="BROADCAST_INPUT">
                                  <shadow type="event_broadcast_menu">
                                    <field name="BROADCAST_OPTION" id="msg_scene2" variabletype="broadcast_msg">scene2</field>
                                  </shadow>
                                </value>
                              </block>
                            </next>
                          </block>
                        </next>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>

  <!-- CANH 2 -->
  <block type="event_whenbroadcastreceived" id="bt2_canh2" x="520" y="40">
    <field name="BROADCAST_OPTION" id="msg_scene2" variabletype="broadcast_msg">scene2</field>
    <next>
      <block type="looks_switchbackdropto" id="bt2_backdrop2">
        <value name="BACKDROP">
          <shadow type="looks_backdrop">
            <field name="BACKDROP">Woods</field>
          </shadow>
        </value>
        <next>
          <block type="looks_switchcostumeto" id="bt2_costume2">
            <value name="COSTUME">
              <shadow type="looks_costume">
                <field name="COSTUME">rabbit-b</field>
              </shadow>
            </value>
            <next>
              <block type="control_if_else" id="bt2_if_lang2">
                <value name="CONDITION">
                  <block type="operator_equals" id="bt2_eq2">
                    <value name="OPERAND1">
                      <block type="data_variable" id="bt2_lang_var2">
                        <field name="VARIABLE" id="var_lang" variabletype="">language</field>
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
                            <field name="TEXT">Tức giận vì bị chê bai, nhím đã thách thức thỏ chạy thi. Thỏ kiêu ngạo đồng ý ngay lập tức vì nghĩ mình sẽ thắng dễ dàng.</field>
                          </shadow>
                        </value>
                        <value name="LANGUAGE">
                          <shadow type="translate_menu_languages">
                            <field name="languages">en</field>
                          </shadow>
                        </value>
                      </block>
                    </value>
                    <next>
                      <block type="looks_sayforsecs" id="bt2_say_eng2">
                        <value name="MESSAGE">
                          <block type="translate_getTranslate" id="bt2_trans2_say">
                            <value name="WORDS">
                              <shadow type="text">
                                <field name="TEXT">Tức giận vì bị chê bai, nhím đã thách thức thỏ chạy thi. Thỏ kiêu ngạo đồng ý ngay lập tức vì nghĩ mình sẽ thắng dễ dàng.</field>
                              </shadow>
                            </value>
                            <value name="LANGUAGE">
                              <shadow type="translate_menu_languages">
                                <field name="languages">en</field>
                              </shadow>
                            </value>
                          </block>
                        </value>
                        <value name="SECS">
                          <shadow type="math_number">
                            <field name="NUM">4</field>
                          </shadow>
                        </value>
                      </block>
                    </next>
                  </block>
                </statement>
                <statement name="SUBSTACK2">
                  <block type="text2speech_speakAndWait" id="bt2_tts_viet2">
                    <value name="WORDS">
                      <shadow type="text">
                        <field name="TEXT">Tức giận vì bị chê bai, nhím đã thách thức thỏ chạy thi. Thỏ kiêu ngạo đồng ý ngay lập tức vì nghĩ mình sẽ thắng dễ dàng.</field>
                      </shadow>
                    </value>
                    <next>
                      <block type="looks_sayforsecs" id="bt2_say_viet2">
                        <value name="MESSAGE">
                          <shadow type="text">
                            <field name="TEXT">Tức giận vì bị chê bai, nhím đã thách thức thỏ chạy thi. Thỏ kiêu ngạo đồng ý ngay lập tức vì nghĩ mình sẽ thắng dễ dàng.</field>
                          </shadow>
                        </value>
                        <value name="SECS">
                          <shadow type="math_number">
                            <field name="NUM">4</field>
                          </shadow>
                        </value>
                      </block>
                    </next>
                  </block>
                </statement>
                <next>
                  <block type="control_wait_until" id="bt2_wait_space2">
                    <value name="CONDITION">
                      <block type="sensing_keypressed" id="bt2_key_space2">
                        <field name="KEY_OPTION">space</field>
                      </block>
                    </value>
                    <next>
                      <block type="event_broadcast" id="bt2_bcast_scene3">
                        <value name="BROADCAST_INPUT">
                          <shadow type="event_broadcast_menu">
                            <field name="BROADCAST_OPTION" id="msg_scene3" variabletype="broadcast_msg">scene3</field>
                          </shadow>
                        </value>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>

  <!-- CANH 3 -->
  <block type="event_whenbroadcastreceived" id="bt2_canh3" x="520" y="480">
    <field name="BROADCAST_OPTION" id="msg_scene3" variabletype="broadcast_msg">scene3</field>
    <next>
      <block type="looks_switchbackdropto" id="bt2_backdrop3">
        <value name="BACKDROP">
          <shadow type="looks_backdrop">
            <field name="BACKDROP">Blue Sky</field>
          </shadow>
        </value>
        <next>
          <block type="looks_switchcostumeto" id="bt2_costume3">
            <value name="COSTUME">
              <shadow type="looks_costume">
                <field name="COSTUME">rabbit-c</field>
              </shadow>
            </value>
            <next>
              <block type="control_if_else" id="bt2_if_lang3">
                <value name="CONDITION">
                  <block type="operator_equals" id="bt2_eq3">
                    <value name="OPERAND1">
                      <block type="data_variable" id="bt2_lang_var3">
                        <field name="VARIABLE" id="var_lang" variabletype="">language</field>
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
                  <block type="text2speech_speakAndWait" id="bt2_tts_eng3">
                    <value name="WORDS">
                      <block type="translate_getTranslate" id="bt2_trans3">
                        <value name="WORDS">
                          <shadow type="text">
                            <field name="TEXT">Cuộc đua bắt đầu. Thỏ chạy nhanh bỏ xa nhím rồi chủ quan nằm ngủ dưới gốc cây. Nhím vẫn kiên trì, không ngừng chạy từng bước.</field>
                          </shadow>
                        </value>
                        <value name="LANGUAGE">
                          <shadow type="translate_menu_languages">
                            <field name="languages">en</field>
                          </shadow>
                        </value>
                      </block>
                    </value>
                    <next>
                      <block type="looks_sayforsecs" id="bt2_say_eng3">
                        <value name="MESSAGE">
                          <block type="translate_getTranslate" id="bt2_trans3_say">
                            <value name="WORDS">
                              <shadow type="text">
                                <field name="TEXT">Cuộc đua bắt đầu. Thỏ chạy nhanh bỏ xa nhím rồi chủ quan nằm ngủ dưới gốc cây. Nhím vẫn kiên trì, không ngừng chạy từng bước.</field>
                              </shadow>
                            </value>
                            <value name="LANGUAGE">
                              <shadow type="translate_menu_languages">
                                <field name="languages">en</field>
                              </shadow>
                            </value>
                          </block>
                        </value>
                        <value name="SECS">
                          <shadow type="math_number">
                            <field name="NUM">4</field>
                          </shadow>
                        </value>
                      </block>
                    </next>
                  </block>
                </statement>
                <statement name="SUBSTACK2">
                  <block type="text2speech_speakAndWait" id="bt2_tts_viet3">
                    <value name="WORDS">
                      <shadow type="text">
                        <field name="TEXT">Cuộc đua bắt đầu. Thỏ chạy nhanh bỏ xa nhím rồi chủ quan nằm ngủ dưới gốc cây. Nhím vẫn kiên trì, không ngừng chạy từng bước.</field>
                      </shadow>
                    </value>
                    <next>
                      <block type="looks_sayforsecs" id="bt2_say_viet3">
                        <value name="MESSAGE">
                          <shadow type="text">
                            <field name="TEXT">Cuộc đua bắt đầu. Thỏ chạy nhanh bỏ xa nhím rồi chủ quan nằm ngủ dưới gốc cây. Nhím vẫn kiên trì, không ngừng chạy từng bước.</field>
                          </shadow>
                        </value>
                        <value name="SECS">
                          <shadow type="math_number">
                            <field name="NUM">4</field>
                          </shadow>
                        </value>
                      </block>
                    </next>
                  </block>
                </statement>
                <next>
                  <block type="control_wait_until" id="bt2_wait_space3">
                    <value name="CONDITION">
                      <block type="sensing_keypressed" id="bt2_key_space3">
                        <field name="KEY_OPTION">space</field>
                      </block>
                    </value>
                    <next>
                      <block type="event_broadcast" id="bt2_bcast_scene4">
                        <value name="BROADCAST_INPUT">
                          <shadow type="event_broadcast_menu">
                            <field name="BROADCAST_OPTION" id="msg_scene4" variabletype="broadcast_msg">scene4</field>
                          </shadow>
                        </value>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>

  <!-- CANH 4 -->
  <block type="event_whenbroadcastreceived" id="bt2_canh4" x="980" y="40">
    <field name="BROADCAST_OPTION" id="msg_scene4" variabletype="broadcast_msg">scene4</field>
    <next>
      <block type="looks_switchbackdropto" id="bt2_backdrop4">
        <value name="BACKDROP">
          <shadow type="looks_backdrop">
            <field name="BACKDROP">Farm</field>
          </shadow>
        </value>
        <next>
          <block type="looks_switchcostumeto" id="bt2_costume4">
            <value name="COSTUME">
              <shadow type="looks_costume">
                <field name="COSTUME">rabbit-a</field>
              </shadow>
            </value>
            <next>
              <!-- Tieng Viet truoc -->
              <block type="text2speech_speakAndWait" id="bt2_tts_viet4">
                <value name="WORDS">
                  <shadow type="text">
                    <field name="TEXT">Nhím vượt qua thỏ đang ngủ và về đích trước để giành chiến thắng. Câu chuyện khuyên ta: kiên trì và chăm chỉ sẽ chiến thắng sự kiêu ngạo.</field>
                  </shadow>
                </value>
                <next>
                  <block type="looks_sayforsecs" id="bt2_say_viet4">
                    <value name="MESSAGE">
                      <shadow type="text">
                        <field name="TEXT">Nhím vượt qua thỏ đang ngủ và về đích trước để giành chiến thắng. Câu chuyện khuyên ta: kiên trì và chăm chỉ sẽ chiến thắng sự kiêu ngạo.</field>
                      </shadow>
                    </value>
                    <value name="SECS">
                      <shadow type="math_number">
                        <field name="NUM">5</field>
                      </shadow>
                    </value>
                    <next>
                      <!-- Tieng Anh sau (dich song ngu) -->
                      <block type="text2speech_speakAndWait" id="bt2_tts_eng4">
                        <value name="WORDS">
                          <block type="translate_getTranslate" id="bt2_trans4">
                            <value name="WORDS">
                              <shadow type="text">
                                <field name="TEXT">Nhím vượt qua thỏ đang ngủ và về đích trước để giành chiến thắng. Câu chuyện khuyên ta: kiên trì và chăm chỉ sẽ chiến thắng sự kiêu ngạo.</field>
                              </shadow>
                            </value>
                            <value name="LANGUAGE">
                              <shadow type="translate_menu_languages">
                                <field name="languages">en</field>
                              </shadow>
                            </value>
                          </block>
                        </value>
                        <next>
                          <block type="looks_sayforsecs" id="bt2_say_eng4">
                            <value name="MESSAGE">
                              <block type="translate_getTranslate" id="bt2_trans4_say">
                                <value name="WORDS">
                                  <shadow type="text">
                                    <field name="TEXT">Nhím vượt qua thỏ đang ngủ và về đích trước để giành chiến thắng. Câu chuyện khuyên ta: kiên trì và chăm chỉ sẽ chiến thắng sự kiêu ngạo.</field>
                                  </shadow>
                                </value>
                                <value name="LANGUAGE">
                                  <shadow type="translate_menu_languages">
                                    <field name="languages">en</field>
                                  </shadow>
                                </value>
                              </block>
                            </value>
                            <value name="SECS">
                              <shadow type="math_number">
                                <field name="NUM">5</field>
                              </shadow>
                            </value>
                          </block>
                        </next>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>`;

(async () => {
  console.log('=== BT2 Generator: Multi-language Interactive Story ===');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

  page.on('console', msg => {
    console.log(`[BROWSER] ${msg.text()}`);
  });

  try {
    console.log('Navigating to MIT Raise Playground...');
    await page.goto('https://playground.raise.mit.edu/create/', {
      waitUntil: 'domcontentloaded',
      timeout: 90000
    });

    console.log('Waiting for Blockly workspace...');
    await page.waitForFunction(() => {
      return window.Blockly &&
        typeof window.Blockly.getMainWorkspace === 'function' &&
        window.Blockly.getMainWorkspace();
    }, { timeout: 90000 });

    await page.waitForTimeout(3000);

    // Load necessary extensions
    console.log('Loading extensions...');
    await loadExtension(page, 'Text to Speech');
    await loadExtension(page, 'Translate');

    // Add Sprites and Backdrops
    console.log('Adding sprites from library...');
    await addSprite(page, 'rabbit', 'Rabbit');
    await addSprite(page, 'hedgehog', 'Hedgehog');

    console.log('Adding backdrops from library...');
    await addBackdrop(page, 'forest', 'Forest');
    await addBackdrop(page, 'woods', 'Woods');
    await addBackdrop(page, 'blue sky', 'Blue Sky');
    await addBackdrop(page, 'farm', 'Farm');

    console.log('Injecting XML blocks and cleaning default sprite...');
    const renderedXml = await page.evaluate(async (xml) => {
      // Find VM
      const allElements = document.querySelectorAll('*');
      let vm = null;
      for (const el of allElements) {
        const reactKeys = Object.keys(el).filter(k => k.startsWith('__reactInternalInstance$') || k.startsWith('__reactFiber$'));
        for (const key of reactKeys) {
          let fiber = el[key];
          let current = fiber;
          while (current) {
            if (current.memoizedProps && current.memoizedProps.vm) {
              vm = current.memoizedProps.vm;
              break;
            }
            current = current.return; 
          }
          if (vm) break;
        }
        if (vm) break;
      }
      if (!vm) throw new Error("Scratch VM not found!");
      window.vm = vm;

      // Delete default Sprite1 (Cat)
      const catTarget = vm.runtime.targets.find(t => t.getName() === 'Sprite1');
      if (catTarget) {
        vm.deleteSprite(catTarget.id);
      }

      // Find Rabbit target and inject XML
      const rabbitTarget = vm.runtime.targets.find(t => t.getName() === 'Rabbit');
      if (!rabbitTarget) throw new Error("Rabbit sprite not found!");
      console.log('Chuyển editing target sang Rabbit...');
      await vm.setEditingTarget(rabbitTarget.id);
      // Chờ 3.5 giây để GUI cập nhật workspace listener
      await new Promise(resolve => setTimeout(resolve, 3500));

      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const dom = B.Xml.textToDom(xml);
      B.Xml.domToWorkspace(dom, ws);
      ws.render();
      console.log('Đã nạp XML vào workspace.');

      // Chờ 3 giây để Blockly events đồng bộ sang VM target
      await new Promise(resolve => setTimeout(resolve, 3000));
      console.log(`Số lượng blocks trong target Rabbit sau đồng bộ: ${Object.keys(rabbitTarget.blocks._blocks).length}`);
      
      return new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws));
    }, BT2_XML);

    await page.waitForTimeout(2000);

    // Save XML file
    const xmlPath = path.join(OUT_DIR, 'bt2_code.xml');
    fs.writeFileSync(xmlPath, renderedXml, 'utf8');
    console.log(`[OK] Saved XML to ${xmlPath}`);

    // Take screenshot
    const pngPath = path.join(OUT_DIR, 'bt2_code.raw.png');
    await page.screenshot({ path: pngPath, fullPage: true });
    console.log(`[OK] Saved screenshot to ${pngPath}`);

    // Download SB3 file
    console.log('Exporting project to SB3...');
    const fileMenu = page.locator('div').filter({ hasText: /^File$/ }).first();
    await fileMenu.click();
    await page.waitForTimeout(1000);

    const saveOption = page.locator('li').filter({ hasText: /Save to your computer/i }).first();
    
    // Set up download listener
    const downloadPromise = page.waitForEvent('download');
    await saveOption.click();
    const download = await downloadPromise;

    const sb3Path = path.join(OUT_DIR, 'bt2_code.sb3');
    await download.saveAs(sb3Path);
    console.log(`[OK] Saved SB3 to ${sb3Path}`);

    console.log('=== BT2 GENERATION COMPLETE ===');
  } catch (err) {
    console.error(`[ERROR] Task failed: ${err.message}`);
    // Save debug screenshot if failed
    try {
      await page.screenshot({ path: path.join(OUT_DIR, 'bt2_error_debug.png'), fullPage: false });
      console.log('[DEBUG] Saved error debug screenshot');
    } catch (e) {}
  } finally {
    await browser.close();
  }
})();
