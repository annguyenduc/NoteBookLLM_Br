const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT_DIR = path.resolve(__dirname, '..');

// Khối XML được mô tả ở Task 1 của implementation_plan.md
const BT1_XML = `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_score">score</variable>
    <variable type="" id="var_round">round</variable>
    <variable type="" id="var_vietWord">vietWord</variable>
  </variables>
  <block type="event_whenflagclicked" id="bt1_start" x="40" y="40">
    <next>
      <block type="data_setvariableto" id="bt1_set_score">
        <field name="VARIABLE" id="var_score" variabletype="">score</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
        <next>
          <block type="data_setvariableto" id="bt1_set_round">
            <field name="VARIABLE" id="var_round" variabletype="">round</field>
            <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
            <next>
              <block type="control_repeat_until" id="bt1_loop">
                <value name="CONDITION">
                  <block type="operator_gt" id="bt1_cond">
                    <value name="OPERAND1"><block type="data_variable" id="bt1_v1"><field name="VARIABLE" id="var_round" variabletype="">round</field></block></value>
                    <value name="OPERAND2"><shadow type="text"><field name="TEXT">5</field></shadow></value>
                  </block>
                </value>
                <statement name="SUBSTACK">
                  <block type="looks_switchcostumeto" id="bt1_cost_cho">
                    <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">cho</field></shadow></value>
                    <next>
                      <block type="sensing_askandwait" id="bt1_ask_vi">
                        <value name="QUESTION"><shadow type="text"><field name="TEXT">Nhập một từ tiếng Việt bạn muốn học:</field></shadow></value>
                        <next>
                          <block type="data_setvariableto" id="bt1_set_vi">
                            <field name="VARIABLE" id="var_vietWord" variabletype="">vietWord</field>
                            <value name="VALUE"><block type="sensing_answer" id="bt1_ans1"></block></value>
                            <next>
                              <block type="looks_sayforsecs" id="bt1_say_en">
                                <value name="MESSAGE">
                                  <block type="operator_join" id="bt1_j1">
                                    <value name="STRING1"><shadow type="text"><field name="TEXT">Tiếng Anh là: </field></shadow></value>
                                    <value name="STRING2">
                                      <block type="translate_getTranslate" id="bt1_tr1">
                                        <value name="WORDS"><block type="data_variable" id="bt1_v_vi"><field name="VARIABLE" id="var_vietWord" variabletype="">vietWord</field></block></value>
                                        <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                                      </block>
                                    </value>
                                  </block>
                                </value>
                                <value name="SECS"><shadow type="math_number"><field name="NUM">2</field></shadow></value>
                                <next>
                                  <block type="text2speech_speakAndWait" id="bt1_tts_en">
                                    <value name="WORDS">
                                      <block type="translate_getTranslate" id="bt1_tr2">
                                        <value name="WORDS"><block type="data_variable" id="bt1_v_vi2"><field name="VARIABLE" id="var_vietWord" variabletype="">vietWord</field></block></value>
                                        <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                                      </block>
                                    </value>
                                    <next>
                                      <block type="sensing_askandwait" id="bt1_ask_en2">
                                        <value name="QUESTION"><shadow type="text"><field name="TEXT">Gõ lại từ tiếng Anh vừa nghe:</field></shadow></value>
                                        <next>
                                          <block type="control_if_else" id="bt1_check">
                                            <value name="CONDITION">
                                              <block type="operator_equals" id="bt1_eq">
                                                <value name="OPERAND1"><block type="sensing_answer" id="bt1_ans2"></block></value>
                                                <value name="OPERAND2">
                                                  <block type="translate_getTranslate" id="bt1_tr3">
                                                    <value name="WORDS"><block type="data_variable" id="bt1_v_vi3"><field name="VARIABLE" id="var_vietWord" variabletype="">vietWord</field></block></value>
                                                    <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                                                  </block>
                                                </value>
                                              </block>
                                            </value>
                                            <statement name="SUBSTACK">
                                              <block type="looks_switchcostumeto" id="bt1_cost_dung">
                                                <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">dung</field></shadow></value>
                                                <next>
                                                  <block type="text2speech_speakAndWait" id="bt1_tts_ok">
                                                    <value name="WORDS"><shadow type="text"><field name="TEXT">Correct!</field></shadow></value>
                                                    <next>
                                                      <block type="data_changevariableby" id="bt1_add_pt">
                                                        <field name="VARIABLE" id="var_score" variabletype="">score</field>
                                                        <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                                                      </block>
                                                    </next>
                                                  </block>
                                                </next>
                                              </block>
                                            </statement>
                                            <statement name="SUBSTACK2">
                                              <block type="looks_switchcostumeto" id="bt1_cost_sai">
                                                <value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">sai</field></shadow></value>
                                                <next>
                                                  <block type="text2speech_speakAndWait" id="bt1_tts_err">
                                                    <value name="WORDS">
                                                      <block type="operator_join" id="bt1_j2">
                                                        <value name="STRING1"><shadow type="text"><field name="TEXT">Sai rồi! Từ đúng là </field></shadow></value>
                                                        <value name="STRING2">
                                                          <block type="translate_getTranslate" id="bt1_tr4">
                                                            <value name="WORDS"><block type="data_variable" id="bt1_v_vi4"><field name="VARIABLE" id="var_vietWord" variabletype="">vietWord</field></block></value>
                                                            <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
                                                          </block>
                                                        </value>
                                                      </block>
                                                    </value>
                                                  </block>
                                                </next>
                                              </block>
                                            </statement>
                                            <next>
                                              <block type="data_changevariableby" id="bt1_inc_vong">
                                                <field name="VARIABLE" id="var_round" variabletype="">round</field>
                                                <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                                                <next>
                                                  <block type="control_wait" id="bt1_wait">
                                                    <value name="DURATION"><shadow type="math_positive_number"><field name="NUM">1</field></shadow></value>
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
                    </next>
                  </block>
                </statement>
                <next>
                  <block type="looks_sayforsecs" id="bt1_end_say">
                    <value name="MESSAGE">
                      <block type="operator_join" id="bt1_j3">
                        <value name="STRING1"><shadow type="text"><field name="TEXT">Bạn đạt </field></shadow></value>
                        <value name="STRING2">
                          <block type="operator_join" id="bt1_j4">
                            <value name="STRING1"><block type="data_variable" id="bt1_v_diem"><field name="VARIABLE" id="var_score" variabletype="">score</field></block></value>
                            <value name="STRING2"><shadow type="text"><field name="TEXT">/5 điểm!</field></shadow></value>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="SECS"><shadow type="math_number"><field name="NUM">3</field></shadow></value>
                    <next>
                      <block type="text2speech_speakAndWait" id="bt1_end_tts">
                        <value name="WORDS">
                          <block type="operator_join" id="bt1_j5">
                            <value name="STRING1"><shadow type="text"><field name="TEXT">Bạn đạt </field></shadow></value>
                            <value name="STRING2">
                              <block type="operator_join" id="bt1_j6">
                                <value name="STRING1"><block type="data_variable" id="bt1_v_diem2"><field name="VARIABLE" id="var_score" variabletype="">score</field></block></value>
                                <value name="STRING2"><shadow type="text"><field name="TEXT"> trên 5 điểm</field></shadow></value>
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
        </next>
      </block>
    </next>
  </block>
</xml>`;

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
  await page.waitForTimeout(1500); // Đợi thẻ thư viện render đầy đủ
  try {
    const card = page.locator(`text="${displayName}"`).first();
    await card.scrollIntoViewIfNeeded({ timeout: 3000 });
    await card.click({ timeout: 5000 });
    await page.waitForTimeout(3000); // Đợi extension tải xong
    console.log(`  [OK] Đã tải extension: ${displayName}`);
    return true;
  } catch (e) {
    console.log(`  [WARN] Click thẻ extension thất bại với: ${displayName}. Đang thử fallback...`);
    try {
      await page.click(`text="${displayName}"`, { timeout: 3000 });
      await page.waitForTimeout(2000);
      return true;
    } catch (e2) {
      console.log(`  [FAIL] Không thể tải extension: ${displayName}`);
      try { await page.locator('text="Back"').first().click({ timeout: 2000 }); await page.waitForTimeout(500); } catch (e3) {}
      return false;
    }
  }
}

(async () => {
  console.log('=== Bắt đầu sinh các tệp đáp án cho Bài tập 1 ===');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

  try {
    console.log('Truy cập trang MIT Raise Playground...');
    await page.goto('https://playground.raise.mit.edu/create/', {
      waitUntil: 'domcontentloaded',
      timeout: 90000
    });

    console.log('Đang chờ workspace của Blockly sẵn sàng...');
    await page.waitForFunction(() => {
      return window.Blockly &&
        typeof window.Blockly.getMainWorkspace === 'function' &&
        window.Blockly.getMainWorkspace();
    }, { timeout: 90000 });

    await page.waitForTimeout(3000);

    // Tải các extension cần thiết
    console.log('Đang tải các extension...');
    await loadExtension(page, 'Text to Speech');
    await loadExtension(page, 'Translate');
    await page.waitForTimeout(2000);

    // Inject XML
    console.log('Đang nạp mã Blockly XML...');
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

    // Lưu ảnh screenshot
    const pngPath = path.join(OUT_DIR, 'bt1_code.raw.png');
    await page.screenshot({ path: pngPath, fullPage: true });
    console.log(`[OK] Đã lưu ảnh chụp khối lệnh tại: ${pngPath}`);

    // Lưu tệp XML
    const xmlPath = path.join(OUT_DIR, 'bt1_code.xml');
    fs.writeFileSync(xmlPath, renderedXml, 'utf8');
    console.log(`[OK] Đã lưu tệp XML tại: ${xmlPath}`);

    // Tải về dự án SB3
    console.log('Đang xuất tệp dự án SB3...');
    const fileMenu = page.locator('div').filter({ hasText: /^File$/ }).first();
    await fileMenu.click();
    await page.waitForTimeout(800);

    const saveOption = page.locator('li').filter({ hasText: /Save to your computer/i }).first();
    
    const downloadPromise = page.waitForEvent('download');
    await saveOption.click();
    const download = await downloadPromise;

    const sb3Path = path.join(OUT_DIR, 'bt1_code.sb3');
    await download.saveAs(sb3Path);
    console.log(`[OK] Đã lưu tệp SB3 tại: ${sb3Path}`);

    console.log('=== [PASS] Hoàn thành sinh đáp án Bài tập 1 thành công! ===');
  } catch (err) {
    const failPath = path.join(OUT_DIR, 'bt1_fail.png');
    await page.screenshot({ path: failPath, fullPage: false });
    console.error(`[FAIL] Có lỗi xảy ra trong quá trình sinh file: ${err.stack}`);
  } finally {
    await browser.close();
  }
})();
