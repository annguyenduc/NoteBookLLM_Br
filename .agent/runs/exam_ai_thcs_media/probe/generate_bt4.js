/**
 * generate_bt4.js
 * Tập lệnh tự động nạp XML Bài tập 4 lên MIT Raise Playground,
 * xuất tệp .sb3, .xml và chụp ảnh khối lệnh .raw.png.
 * 
 * Các biến yêu cầu:
 * - score, round
 * - danh sách questions, answers
 * - broadcast showResult
 * 
 * Ngôn ngữ phản hồi và chú thích: Tiếng Việt.
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT_DIR = path.resolve(__dirname, '..');

async function openExtensionLibrary(page) {
  const selectors = [
    '[class*="addExtension"]',
    '[class*="extension-button"]', 
    '[class*="extensionButton"]',
    'button[class*="add"]',
    '.scratch-gui_extension-button__',
    '[title*="extension"]',
    '[title*="Extension"]',
    '[class*="toolbox"] button:last-child',
    '[class*="blocklyToolbox"] + * button',
  ];
  
  for (const sel of selectors) {
    try {
      const el = page.locator(sel).first();
      if (await el.isVisible({ timeout: 2000 })) {
        await el.click();
        await page.waitForTimeout(1500);
        console.log(`  [OK] Đã mở thư viện extension bằng selector: ${sel}`);
        return true;
      }
    } catch (e) {
      // Bỏ qua và thử selector tiếp theo
    }
  }
  
  // Phương án cuối cùng: Click vào góc dưới bên trái của Blockly toolbox
  try {
    await page.mouse.click(30, page.viewportSize().height - 50);
    await page.waitForTimeout(1500);
    console.log('  [OK] Đã click giả lập vùng nút Extension');
    return true;
  } catch (e) {
    return false;
  }
}

async function loadExtension(page, displayName) {
  console.log(`  Đang tìm và nạp extension: ${displayName}...`);
  const card = page.locator('div').filter({ hasText: new RegExp(`^${displayName}$`) }).first();
  
  try {
    await card.click({ timeout: 5000 });
    await page.waitForTimeout(2000);
    console.log(`  [OK] Đã nạp extension card: ${displayName}`);
    return true;
  } catch (e) {
    console.log(`  [WARN] Không thể click card ${displayName}: ${e.message.substring(0, 100)}`);
    
    try {
      await page.click(`text="${displayName}"`, { timeout: 3000 });
      await page.waitForTimeout(2000);
      console.log(`  [OK] Đã click text của extension: ${displayName}`);
      return true;
    } catch (e2) {
      console.log(`  [FAIL] Không thể nạp extension bằng text-click: ${e2.message.substring(0, 80)}`);
      return false;
    }
  }
}

async function loadExtensions(page, extensionNames) {
  for (const extName of extensionNames) {
    const opened = await openExtensionLibrary(page);
    if (!opened) {
      console.log(`  [WARN] Không mở được thư viện extension để nạp: ${extName}`);
      continue;
    }
    
    await page.waitForTimeout(1000);
    const loaded = await loadExtension(page, extName);
    if (!loaded) {
      await page.screenshot({ path: path.join(OUT_DIR, `debug_ext_fail_${extName.replace(/\s+/g, '_')}.png`), fullPage: false });
      console.log(`  [DEBUG] Đã lưu ảnh lỗi nạp extension: ${extName}`);
      
      // Nhấn Back để quay lại trang chính
      try {
        await page.click('[class*="back"], button:has-text("Back")', { timeout: 3000 });
        await page.waitForTimeout(1000);
      } catch (e) {}
    }
    await page.waitForTimeout(1500);
  }
}

// Blockly XML cho Bài tập 4 theo đúng đặc tả yêu cầu của USER
const BT4_XML = `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_score">score</variable>
    <variable type="" id="var_round">round</variable>
    <variable type="list" id="list_questions">questions</variable>
    <variable type="list" id="list_answers">answers</variable>
    <variable type="broadcast_msg" id="msg_showResult">showResult</variable>
  </variables>
  <block type="event_whenflagclicked" id="bt4_start" x="40" y="40">
    <next>
      <block type="data_setvariableto" id="bt4_set_score">
        <field name="VARIABLE" id="var_score" variabletype="">score</field>
        <value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value>
        <next>
          <block type="data_setvariableto" id="bt4_set_round">
            <field name="VARIABLE" id="var_round" variabletype="">round</field>
            <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
            <next>
              <block type="data_deletealloflist" id="bt4_del_q">
                <field name="LIST" id="list_questions" variabletype="list">questions</field>
                <next>
                  <block type="data_deletealloflist" id="bt4_del_a">
                    <field name="LIST" id="list_answers" variabletype="list">answers</field>
                    <next>
                      <!-- Thêm câu hỏi và đáp án 1 -->
                      <block type="data_addtolist" id="bt4_add_q1">
                        <field name="LIST" id="list_questions" variabletype="list">questions</field>
                        <value name="ITEM"><shadow type="text"><field name="TEXT">Tri tue nhan tao viet tat la gi?</field></shadow></value>
                        <next>
                          <block type="data_addtolist" id="bt4_add_a1">
                            <field name="LIST" id="list_answers" variabletype="list">answers</field>
                            <value name="ITEM"><shadow type="text"><field name="TEXT">AI</field></shadow></value>
                            <next>
                              <!-- Thêm câu hỏi và đáp án 2 -->
                              <block type="data_addtolist" id="bt4_add_q2">
                                <field name="LIST" id="list_questions" variabletype="list">questions</field>
                                <value name="ITEM"><shadow type="text"><field name="TEXT">Google dich ten tieng Anh la gi?</field></shadow></value>
                                <next>
                                  <block type="data_addtolist" id="bt4_add_a2">
                                    <field name="LIST" id="list_answers" variabletype="list">answers</field>
                                    <value name="ITEM"><shadow type="text"><field name="TEXT">Translate</field></shadow></value>
                                    <next>
                                      <!-- Thêm câu hỏi và đáp án 3 -->
                                      <block type="data_addtolist" id="bt4_add_q3">
                                        <field name="LIST" id="list_questions" variabletype="list">questions</field>
                                        <value name="ITEM"><shadow type="text"><field name="TEXT">Doc chu thanh giong noi la gi?</field></shadow></value>
                                        <next>
                                          <block type="data_addtolist" id="bt4_add_a3">
                                            <field name="LIST" id="list_answers" variabletype="list">answers</field>
                                            <value name="ITEM"><shadow type="text"><field name="TEXT">Text to Speech</field></shadow></value>
                                            <next>
                                              <!-- Thêm câu hỏi và đáp án 4 -->
                                              <block type="data_addtolist" id="bt4_add_q4">
                                                <field name="LIST" id="list_questions" variabletype="list">questions</field>
                                                <value name="ITEM"><shadow type="text"><field name="TEXT">Cam xuc smile la vui hay buon?</field></shadow></value>
                                                <next>
                                                  <block type="data_addtolist" id="bt4_add_a4">
                                                    <field name="LIST" id="list_answers" variabletype="list">answers</field>
                                                    <value name="ITEM"><shadow type="text"><field name="TEXT">vui</field></shadow></value>
                                                    <next>
                                                      <!-- Thêm câu hỏi và đáp án 5 -->
                                                      <block type="data_addtolist" id="bt4_add_q5">
                                                        <field name="LIST" id="list_questions" variabletype="list">questions</field>
                                                        <value name="ITEM"><shadow type="text"><field name="TEXT">Day may hoc tren web ten la gi?</field></shadow></value>
                                                        <next>
                                                          <block type="data_addtolist" id="bt4_add_a5">
                                                            <field name="LIST" id="list_answers" variabletype="list">answers</field>
                                                            <value name="ITEM"><shadow type="text"><field name="TEXT">Teachable Machine</field></shadow></value>
                                                            <next>
                                                              <!-- Bắt đầu vòng lặp hỏi đáp -->
                                                              <block type="control_repeat_until" id="bt4_loop">
                                                                <value name="CONDITION">
                                                                  <block type="operator_gt" id="bt4_check_vong">
                                                                    <value name="OPERAND1">
                                                                      <block type="data_variable" id="bt4_round_v"><field name="VARIABLE" id="var_round" variabletype="">round</field></block>
                                                                    </value>
                                                                    <value name="OPERAND2">
                                                                      <shadow type="math_number"><field name="NUM">5</field></shadow>
                                                                    </value>
                                                                  </block>
                                                                </value>
                                                                <statement name="SUBSTACK">
                                                                  <block type="text2speech_speakAndWait" id="bt4_speak_q">
                                                                    <value name="WORDS">
                                                                      <block type="data_itemoflist" id="bt4_get_q_tts">
                                                                        <field name="LIST" id="list_questions" variabletype="list">questions</field>
                                                                        <value name="INDEX">
                                                                          <block type="data_variable" id="bt4_round_i1"><field name="VARIABLE" id="var_round" variabletype="">round</field></block>
                                                                        </value>
                                                                      </block>
                                                                    </value>
                                                                    <next>
                                                                      <block type="sensing_askandwait" id="bt4_ask">
                                                                        <value name="QUESTION">
                                                                          <block type="data_itemoflist" id="bt4_get_q_ask">
                                                                            <field name="LIST" id="list_questions" variabletype="list">questions</field>
                                                                            <value name="INDEX">
                                                                              <block type="data_variable" id="bt4_round_i2"><field name="VARIABLE" id="var_round" variabletype="">round</field></block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                        <next>
                                                                          <block type="control_if_else" id="bt4_check_ans">
                                                                            <value name="CONDITION">
                                                                              <block type="operator_equals" id="bt4_check_eq">
                                                                                <value name="OPERAND1">
                                                                                  <block type="sensing_answer" id="bt4_ans"></block>
                                                                                </value>
                                                                                <value name="OPERAND2">
                                                                                  <block type="data_itemoflist" id="bt4_get_a_val">
                                                                                    <field name="LIST" id="list_answers" variabletype="list">answers</field>
                                                                                    <value name="INDEX">
                                                                                      <block type="data_variable" id="bt4_round_i3"><field name="VARIABLE" id="var_round" variabletype="">round</field></block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="SUBSTACK">
                                                                              <block type="text2speech_speakAndWait" id="bt4_say_correct">
                                                                                <value name="WORDS"><shadow type="text"><field name="TEXT">Chinh xac</field></shadow></value>
                                                                                <next>
                                                                                  <block type="data_changevariableby" id="bt4_add_score">
                                                                                    <field name="VARIABLE" id="var_score" variabletype="">score</field>
                                                                                    <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                                                                                  </block>
                                                                                </next>
                                                                              </block>
                                                                            </statement>
                                                                            <statement name="SUBSTACK2">
                                                                              <block type="text2speech_speakAndWait" id="bt4_say_wrong">
                                                                                <value name="WORDS"><shadow type="text"><field name="TEXT">Sai roi</field></shadow></value>
                                                                              </block>
                                                                            </statement>
                                                                            <next>
                                                                              <block type="data_changevariableby" id="bt4_inc_round">
                                                                                <field name="VARIABLE" id="var_round" variabletype="">round</field>
                                                                                <value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value>
                                                                              </block>
                                                                            </next>
                                                                          </block>
                                                                        </next>
                                                                      </block>
                                                                    </next>
                                                                  </block>
                                                                </statement>
                                                                <next>
                                                                  <!-- Broadcast thông báo kết quả sau khi kết thúc 5 câu -->
                                                                  <block type="event_broadcast" id="bt4_broadcast_res">
                                                                    <value name="BROADCAST_INPUT">
                                                                      <shadow type="event_broadcast_menu">
                                                                        <field name="BROADCAST_OPTION" id="msg_showResult" variabletype="broadcast_msg">showResult</field>
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
    </next>
  </block>

  <!-- Sprite 2 nhận thông báo tổng kết điểm số -->
  <block type="event_whenbroadcastreceived" id="bt4_res_received" x="550" y="40">
    <field name="BROADCAST_OPTION" id="msg_showResult" variabletype="broadcast_msg">showResult</field>
    <next>
      <!-- Hiển thị Say kết quả bằng tiếng Việt -->
      <block type="looks_sayforsecs" id="bt4_say_res">
        <value name="MESSAGE">
          <block type="operator_join" id="bt4_join_vi1">
            <value name="STRING1"><shadow type="text"><field name="TEXT">Bạn đạt </field></shadow></value>
            <value name="STRING2">
              <block type="operator_join" id="bt4_join_vi2">
                <value name="STRING1"><block type="data_variable" id="bt4_score_v1"><field name="VARIABLE" id="var_score" variabletype="">score</field></block></value>
                <value name="STRING2"><shadow type="text"><field name="TEXT"> trên 5 điểm!</field></shadow></value>
              </block>
            </value>
          </block>
        </value>
        <value name="SECS"><shadow type="math_number"><field name="NUM">3</field></shadow></value>
        <next>
          <!-- Phát âm thanh TTS tiếng Việt -->
          <block type="text2speech_speakAndWait" id="bt4_tts_vi">
            <value name="WORDS">
              <block type="operator_join" id="bt4_join_vi3">
                <value name="STRING1"><shadow type="text"><field name="TEXT">Bạn đạt </field></shadow></value>
                <value name="STRING2">
                  <block type="operator_join" id="bt4_join_vi4">
                    <value name="STRING1"><block type="data_variable" id="bt4_score_v2"><field name="VARIABLE" id="var_score" variabletype="">score</field></block></value>
                    <value name="STRING2"><shadow type="text"><field name="TEXT"> trên 5 điểm</field></shadow></value>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <!-- Dùng Translate dịch kết quả sang tiếng Anh và TTS đọc to -->
              <block type="text2speech_speakAndWait" id="bt4_tts_en">
                <value name="WORDS">
                  <block type="translate_getTranslate" id="bt4_trans_en">
                    <value name="WORDS">
                      <block type="operator_join" id="bt4_join_en1">
                        <value name="STRING1"><shadow type="text"><field name="TEXT">Bạn đạt </field></shadow></value>
                        <value name="STRING2">
                          <block type="operator_join" id="bt4_join_en2">
                            <value name="STRING1"><block type="data_variable" id="bt4_score_v3"><field name="VARIABLE" id="var_score" variabletype="">score</field></block></value>
                            <value name="STRING2"><shadow type="text"><field name="TEXT"> trên 5 điểm</field></shadow></value>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">en</field></shadow></value>
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
  console.log('=== KHỞI ĐỘNG PLAYWRIGHT ĐỂ SINH ĐÁP ÁN BÀI TẬP 4 ===');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

  try {
    console.log('  Đang tải trang MIT Raise Playground...');
    await page.goto('https://playground.raise.mit.edu/create/', {
      waitUntil: 'domcontentloaded',
      timeout: 90000
    });

    // Chờ Blockly khởi tạo thành công
    await page.waitForFunction(() => {
      return window.Blockly &&
        typeof window.Blockly.getMainWorkspace === 'function' &&
        window.Blockly.getMainWorkspace();
    }, { timeout: 90000 });

    console.log('  [OK] Đã khởi tạo Blockly. Chờ 3 giây ổn định giao diện...');
    await page.waitForTimeout(3000);

    // Chụp ảnh màn hình ban đầu để debug nếu cần
    await page.screenshot({ path: path.join(OUT_DIR, 'debug_initial.png'), fullPage: false });

    // Nạp các extension bắt buộc: Text to Speech, Translate
    console.log('  Đang nạp các extension...');
    await loadExtensions(page, ['Text to Speech', 'Translate']);

    await page.waitForTimeout(2000);
    await page.screenshot({ path: path.join(OUT_DIR, 'debug_after_ext.png'), fullPage: false });

    // Nạp khối lệnh XML
    console.log('  Đang nạp cấu trúc XML khối lệnh Bài tập 4...');
    const renderedXml = await page.evaluate((xml) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const dom = B.Xml.textToDom(xml);
      B.Xml.domToWorkspace(dom, ws);
      ws.render();
      return new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws));
    }, BT4_XML);

    await page.waitForTimeout(2000);

    // Lưu ảnh chụp khối lệnh raw
    const pngPath = path.join(OUT_DIR, 'bt4_code.raw.png');
    await page.screenshot({ path: pngPath, fullPage: true });
    console.log(`  [OK] Đã lưu hình ảnh: bt4_code.raw.png`);

    // Lưu tệp XML
    const xmlPath = path.join(OUT_DIR, 'bt4_code.xml');
    fs.writeFileSync(xmlPath, renderedXml, 'utf8');
    console.log(`  [OK] Đã lưu mã nguồn: bt4_code.xml`);

    // Xuất dự án ra tệp .sb3
    console.log('  Đang xuất dự án thành tệp .sb3...');
    try {
      const fileMenu = page.locator('div').filter({ hasText: /^File$/ }).first();
      await fileMenu.click();
      await page.waitForTimeout(800);

      const saveOption = page.locator('li').filter({ hasText: /Save to your computer/i }).first();
      
      // Thiết lập listener để đón tệp tải xuống
      const downloadPromise = page.waitForEvent('download');
      await saveOption.click();
      const download = await downloadPromise;

      const sb3Path = path.join(OUT_DIR, 'bt4_code.sb3');
      await download.saveAs(sb3Path);
      console.log(`  [OK] Đã lưu tệp Scratch: bt4_code.sb3`);
    } catch (sb3Err) {
      console.error(`  [FAIL] Không thể xuất tệp .sb3: ${sb3Err.message}`);
    }

  } catch (err) {
    const failPng = path.join(OUT_DIR, 'bt4_fail.png');
    await page.screenshot({ path: failPng, fullPage: false });
    console.error(`  [ERROR] Lỗi thực thi Playwright: ${err.message}`);
  } finally {
    await browser.close();
    console.log('=== KẾT THÚC THỰC THI BÀI TẬP 4 ===');
  }
})();
