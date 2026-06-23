/**
 * generate_bt3.js
 * Tập lệnh Node.js sử dụng Playwright để tự động nạp XML Bài tập 3 vào MIT Raise Playground,
 * xuất bản file .sb3, lưu file .xml và chụp ảnh .raw.png kết quả.
 * Status: PREVIEW_ONLY
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT_DIR = path.resolve(__dirname, '..');

// Hàm mở thư viện Extension
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
      // Tiếp tục thử selector khác
    }
  }
  
  try {
    await page.mouse.click(30, page.viewportSize().height - 50);
    await page.waitForTimeout(1500);
    return true;
  } catch (e) {
    return false;
  }
}

// Hàm tải một Extension cụ thể
async function loadExtension(page, displayName) {
  console.log(`  Đang tải extension: ${displayName}...`);
  const card = page.locator('div').filter({ hasText: new RegExp(`^${displayName}$`) }).first();
  
  try {
    await card.click({ timeout: 5000 });
    await page.waitForTimeout(2000);
    console.log(`  [OK] Đã click chọn card: ${displayName}`);
    return true;
  } catch (e) {
    console.log(`  [WARN] Không thể click card ${displayName}: ${e.message.substring(0, 100)}`);
    try {
      await page.click(`text="${displayName}"`, { timeout: 3000 });
      await page.waitForTimeout(2000);
      console.log(`  [OK] Click bằng text thành công: ${displayName}`);
      return true;
    } catch (e2) {
      console.log(`  [WARN] Click bằng text cũng thất bại: ${e2.message.substring(0, 80)}`);
      return false;
    }
  }
}

// Hàm tải danh sách các Extension
async function loadExtensions(page, extensionNames) {
  for (const extName of extensionNames) {
    const opened = await openExtensionLibrary(page);
    if (!opened) {
      console.log(`  [WARN] Không thể mở thư viện extension cho: ${extName}`);
      continue;
    }
    
    await page.waitForTimeout(1000);
    const loaded = await loadExtension(page, extName);
    if (!loaded) {
      await page.screenshot({ path: path.join(OUT_DIR, `debug_ext_${extName.replace(/\s+/g, '_')}.png`), fullPage: false });
      console.log(`  [DEBUG] Đã lưu ảnh lỗi tải extension: ${extName}`);
      try {
        await page.click('[class*="back"], button:has-text("Back")', { timeout: 3000 });
        await page.waitForTimeout(1000);
      } catch (e) {}
    }
    await page.waitForTimeout(1500);
  }
}

// Blockly XML cho Bài tập 3 - Trợ lý toán học AI với các biến num1, num2, operation, calcResult và history
const BT3_XML = `<xml xmlns="http://www.w3.org/1999/xhtml">
  <variables>
    <variable type="" id="var_num1">num1</variable>
    <variable type="" id="var_num2">num2</variable>
    <variable type="" id="var_operation">operation</variable>
    <variable type="" id="var_calcResult">calcResult</variable>
    <variable type="" id="var_i">i</variable>
    <variable type="list" id="list_history">history</variable>
  </variables>
  <block type="event_whenflagclicked" id="bt3_start" x="40" y="40">
    <next>
      <block type="data_deletealloflist" id="bt3_clear_history">
        <field name="LIST" id="list_history" variabletype="list">history</field>
        <next>
          <block type="data_setvariableto" id="bt3_init_op">
            <field name="VARIABLE" id="var_operation" variabletype="">operation</field>
            <value name="VALUE"><shadow type="text"><field name="TEXT">-1</field></shadow></value>
            <next>
              <block type="control_repeat_until" id="bt3_loop">
                <value name="CONDITION">
                  <block type="operator_equals" id="bt3_cond_exit">
                    <value name="OPERAND1">
                      <block type="data_variable" id="bt3_v_op">
                        <field name="VARIABLE" id="var_operation" variabletype="">operation</field>
                      </block>
                    </value>
                    <value name="OPERAND2">
                      <shadow type="text"><field name="TEXT">0</field></shadow>
                    </value>
                  </block>
                </value>
                <statement name="SUBSTACK">
                  <block type="sensing_askandwait" id="bt3_ask_op">
                    <value name="QUESTION">
                      <shadow type="text"><field name="TEXT">Chọn phép tính: 1=Cộng, 2=Trừ, 3=Nhân, 4=Chia, 5=Lịch sử, 0=Thoát</field></shadow>
                    </value>
                    <next>
                      <block type="data_setvariableto" id="bt3_set_op">
                        <field name="VARIABLE" id="var_operation" variabletype="">operation</field>
                        <value name="VALUE">
                          <block type="sensing_answer" id="bt3_ans_op"/>
                        </value>
                        <next>
                          <block type="control_if" id="bt3_if_calc">
                            <value name="CONDITION">
                              <block type="operator_and" id="bt3_and_calc">
                                <value name="OPERAND1">
                                  <block type="operator_gt" id="bt3_gt_calc">
                                    <value name="OPERAND1">
                                      <block type="data_variable" id="bt3_v_op_calc1">
                                        <field name="VARIABLE" id="var_operation" variabletype="">operation</field>
                                      </block>
                                    </value>
                                    <value name="OPERAND2">
                                      <shadow type="text"><field name="TEXT">0</field></shadow>
                                    </value>
                                  </block>
                                </value>
                                <value name="OPERAND2">
                                  <block type="operator_lt" id="bt3_lt_calc">
                                    <value name="OPERAND1">
                                      <block type="data_variable" id="bt3_v_op_calc2">
                                        <field name="VARIABLE" id="var_operation" variabletype="">operation</field>
                                      </block>
                                    </value>
                                    <value name="OPERAND2">
                                      <shadow type="text"><field name="TEXT">5</field></shadow>
                                    </value>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <statement name="SUBSTACK">
                              <block type="sensing_askandwait" id="bt3_ask_num1">
                                <value name="QUESTION">
                                  <shadow type="text"><field name="TEXT">Nhập số thứ nhất:</field></shadow>
                                </value>
                                <next>
                                  <block type="data_setvariableto" id="bt3_set_num1">
                                    <field name="VARIABLE" id="var_num1" variabletype="">num1</field>
                                    <value name="VALUE"><block type="sensing_answer" id="bt3_ans_num1"/></value>
                                    <next>
                                      <block type="sensing_askandwait" id="bt3_ask_num2">
                                        <value name="QUESTION">
                                          <shadow type="text"><field name="TEXT">Nhập số thứ hai:</field></shadow>
                                        </value>
                                        <next>
                                          <block type="data_setvariableto" id="bt3_set_num2">
                                            <field name="VARIABLE" id="var_num2" variabletype="">num2</field>
                                            <value name="VALUE"><block type="sensing_answer" id="bt3_ans_num2"/></value>
                                            <next>
                                              <block type="control_if" id="bt3_if_1">
                                                <value name="CONDITION">
                                                  <block type="operator_equals" id="bt3_eq_1">
                                                    <value name="OPERAND1"><block type="data_variable" id="bt3_v_op_1"><field name="VARIABLE" id="var_operation" variabletype="">operation</field></block></value>
                                                    <value name="OPERAND2"><shadow type="text"><field name="TEXT">1</field></shadow></value>
                                                  </block>
                                                </value>
                                                <statement name="SUBSTACK">
                                                  <block type="data_setvariableto" id="bt3_calc_1">
                                                    <field name="VARIABLE" id="var_calcResult" variabletype="">calcResult</field>
                                                    <value name="VALUE">
                                                      <block type="operator_add" id="bt3_add_op">
                                                        <value name="NUM1"><block type="data_variable" id="bt3_num1_1"><field name="VARIABLE" id="var_num1" variabletype="">num1</field></block></value>
                                                        <value name="NUM2"><block type="data_variable" id="bt3_num2_1"><field name="VARIABLE" id="var_num2" variabletype="">num2</field></block></value>
                                                      </block>
                                                    </value>
                                                    <next>
                                                      <block type="data_addtolist" id="bt3_add_list_1">
                                                        <field name="LIST" id="list_history" variabletype="list">history</field>
                                                        <value name="ITEM">
                                                          <block type="operator_join" id="bt3_join_list1_a">
                                                            <value name="STRING1"><block type="data_variable" id="bt3_num1_1_j"><field name="VARIABLE" id="var_num1" variabletype="">num1</field></block></value>
                                                            <value name="STRING2">
                                                              <block type="operator_join" id="bt3_join_list1_b">
                                                                <value name="STRING1"><shadow type="text"><field name="TEXT"> + </field></shadow></value>
                                                                <value name="STRING2">
                                                                  <block type="operator_join" id="bt3_join_list1_c">
                                                                    <value name="STRING1"><block type="data_variable" id="bt3_num2_1_j"><field name="VARIABLE" id="var_num2" variabletype="">num2</field></block></value>
                                                                    <value name="STRING2">
                                                                      <block type="operator_join" id="bt3_join_list1_d">
                                                                        <value name="STRING1"><shadow type="text"><field name="TEXT"> = </field></shadow></value>
                                                                        <value name="STRING2"><block type="data_variable" id="bt3_res_1_j"><field name="VARIABLE" id="var_calcResult" variabletype="">calcResult</field></block></value>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </value>
                                                              </block>
                                                            </value>
                                                          </block>
                                                        </value>
                                                        <next>
                                                          <block type="text2speech_speakAndWait" id="bt3_speak_1">
                                                            <value name="WORDS">
                                                              <block type="operator_join" id="bt3_join_sp1_a">
                                                                <value name="STRING1"><block type="data_variable" id="bt3_num1_1_sp"><field name="VARIABLE" id="var_num1" variabletype="">num1</field></block></value>
                                                                <value name="STRING2">
                                                                  <block type="operator_join" id="bt3_join_sp1_b">
                                                                    <value name="STRING1"><shadow type="text"><field name="TEXT"> cộng </field></shadow></value>
                                                                    <value name="STRING2">
                                                                      <block type="operator_join" id="bt3_join_sp1_c">
                                                                        <value name="STRING1"><block type="data_variable" id="bt3_num2_1_sp"><field name="VARIABLE" id="var_num2" variabletype="">num2</field></block></value>
                                                                        <value name="STRING2">
                                                                          <block type="operator_join" id="bt3_join_sp1_d">
                                                                            <value name="STRING1"><shadow type="text"><field name="TEXT"> bằng </field></shadow></value>
                                                                            <value name="STRING2"><block type="data_variable" id="bt3_res_1_sp"><field name="VARIABLE" id="var_calcResult" variabletype="">calcResult</field></block></value>
                                                                          </block>
                                                                        </value>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </value>
                                                              </block>
                                                            </value>
                                                          </block>
                                                        </next>
                                                      </block>
                                                    </next>
                                                  </block>
                                                </statement>
                                                <next>
                                                  <block type="control_if" id="bt3_if_2">
                                                    <value name="CONDITION">
                                                      <block type="operator_equals" id="bt3_eq_2">
                                                        <value name="OPERAND1"><block type="data_variable" id="bt3_v_op_2"><field name="VARIABLE" id="var_operation" variabletype="">operation</field></block></value>
                                                        <value name="OPERAND2"><shadow type="text"><field name="TEXT">2</field></shadow></value>
                                                      </block>
                                                    </value>
                                                    <statement name="SUBSTACK">
                                                      <block type="data_setvariableto" id="bt3_calc_2">
                                                        <field name="VARIABLE" id="var_calcResult" variabletype="">calcResult</field>
                                                        <value name="VALUE">
                                                          <block type="operator_subtract" id="bt3_sub_op">
                                                            <value name="NUM1"><block type="data_variable" id="bt3_num1_2"><field name="VARIABLE" id="var_num1" variabletype="">num1</field></block></value>
                                                            <value name="NUM2"><block type="data_variable" id="bt3_num2_2"><field name="VARIABLE" id="var_num2" variabletype="">num2</field></block></value>
                                                          </block>
                                                        </value>
                                                        <next>
                                                          <block type="data_addtolist" id="bt3_add_list_2">
                                                            <field name="LIST" id="list_history" variabletype="list">history</field>
                                                            <value name="ITEM">
                                                              <block type="operator_join" id="bt3_join_list2_a">
                                                                <value name="STRING1"><block type="data_variable" id="bt3_num1_2_j"><field name="VARIABLE" id="var_num1" variabletype="">num1</field></block></value>
                                                                <value name="STRING2">
                                                                  <block type="operator_join" id="bt3_join_list2_b">
                                                                    <value name="STRING1"><shadow type="text"><field name="TEXT"> - </field></shadow></value>
                                                                    <value name="STRING2">
                                                                      <block type="operator_join" id="bt3_join_list2_c">
                                                                        <value name="STRING1"><block type="data_variable" id="bt3_num2_2_j"><field name="VARIABLE" id="var_num2" variabletype="">num2</field></block></value>
                                                                        <value name="STRING2">
                                                                          <block type="operator_join" id="bt3_join_list2_d">
                                                                            <value name="STRING1"><shadow type="text"><field name="TEXT"> = </field></shadow></value>
                                                                            <value name="STRING2"><block type="data_variable" id="bt3_res_2_j"><field name="VARIABLE" id="var_calcResult" variabletype="">calcResult</field></block></value>
                                                                          </block>
                                                                        </value>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </value>
                                                              </block>
                                                            </value>
                                                            <next>
                                                              <block type="text2speech_speakAndWait" id="bt3_speak_2">
                                                                <value name="WORDS">
                                                                  <block type="operator_join" id="bt3_join_sp2_a">
                                                                    <value name="STRING1"><block type="data_variable" id="bt3_num1_2_sp"><field name="VARIABLE" id="var_num1" variabletype="">num1</field></block></value>
                                                                    <value name="STRING2">
                                                                      <block type="operator_join" id="bt3_join_sp2_b">
                                                                        <value name="STRING1"><shadow type="text"><field name="TEXT"> trừ </field></shadow></value>
                                                                        <value name="STRING2">
                                                                          <block type="operator_join" id="bt3_join_sp2_c">
                                                                            <value name="STRING1"><block type="data_variable" id="bt3_num2_2_sp"><field name="VARIABLE" id="var_num2" variabletype="">num2</field></block></value>
                                                                            <value name="STRING2">
                                                                              <block type="operator_join" id="bt3_join_sp2_d">
                                                                                <value name="STRING1"><shadow type="text"><field name="TEXT"> bằng </field></shadow></value>
                                                                                <value name="STRING2"><block type="data_variable" id="bt3_res_2_sp"><field name="VARIABLE" id="var_calcResult" variabletype="">calcResult</field></block></value>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </value>
                                                              </block>
                                                            </next>
                                                          </block>
                                                        </next>
                                                      </block>
                                                    </statement>
                                                    <next>
                                                      <block type="control_if" id="bt3_if_3">
                                                        <value name="CONDITION">
                                                          <block type="operator_equals" id="bt3_eq_3">
                                                            <value name="OPERAND1"><block type="data_variable" id="bt3_v_op_3"><field name="VARIABLE" id="var_operation" variabletype="">operation</field></block></value>
                                                            <value name="OPERAND2"><shadow type="text"><field name="TEXT">3</field></shadow></value>
                                                          </block>
                                                        </value>
                                                        <statement name="SUBSTACK">
                                                          <block type="data_setvariableto" id="bt3_calc_3">
                                                            <field name="VARIABLE" id="var_calcResult" variabletype="">calcResult</field>
                                                            <value name="VALUE">
                                                              <block type="operator_multiply" id="bt3_mul_op">
                                                                <value name="NUM1"><block type="data_variable" id="bt3_num1_3"><field name="VARIABLE" id="var_num1" variabletype="">num1</field></block></value>
                                                                <value name="NUM2"><block type="data_variable" id="bt3_num2_3"><field name="VARIABLE" id="var_num2" variabletype="">num2</field></block></value>
                                                              </block>
                                                            </value>
                                                            <next>
                                                              <block type="data_addtolist" id="bt3_add_list_3">
                                                                <field name="LIST" id="list_history" variabletype="list">history</field>
                                                                <value name="ITEM">
                                                                  <block type="operator_join" id="bt3_join_list3_a">
                                                                    <value name="STRING1"><block type="data_variable" id="bt3_num1_3_j"><field name="VARIABLE" id="var_num1" variabletype="">num1</field></block></value>
                                                                    <value name="STRING2">
                                                                      <block type="operator_join" id="bt3_join_list3_b">
                                                                        <value name="STRING1"><shadow type="text"><field name="TEXT"> * </field></shadow></value>
                                                                        <value name="STRING2">
                                                                          <block type="operator_join" id="bt3_join_list3_c">
                                                                            <value name="STRING1"><block type="data_variable" id="bt3_num2_3_j"><field name="VARIABLE" id="var_num2" variabletype="">num2</field></block></value>
                                                                            <value name="STRING2">
                                                                              <block type="operator_join" id="bt3_join_list3_d">
                                                                                <value name="STRING1"><shadow type="text"><field name="TEXT"> = </field></shadow></value>
                                                                                <value name="STRING2"><block type="data_variable" id="bt3_res_3_j"><field name="VARIABLE" id="var_calcResult" variabletype="">calcResult</field></block></value>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </value>
                                                                <next>
                                                                  <block type="text2speech_speakAndWait" id="bt3_speak_3">
                                                                    <value name="WORDS">
                                                                      <block type="operator_join" id="bt3_join_sp3_a">
                                                                        <value name="STRING1"><block type="data_variable" id="bt3_num1_3_sp"><field name="VARIABLE" id="var_num1" variabletype="">num1</field></block></value>
                                                                        <value name="STRING2">
                                                                          <block type="operator_join" id="bt3_join_sp3_b">
                                                                            <value name="STRING1"><shadow type="text"><field name="TEXT"> nhân </field></shadow></value>
                                                                            <value name="STRING2">
                                                                              <block type="operator_join" id="bt3_join_sp3_c">
                                                                                <value name="STRING1"><block type="data_variable" id="bt3_num2_3_sp"><field name="VARIABLE" id="var_num2" variabletype="">num2</field></block></value>
                                                                                <value name="STRING2">
                                                                                  <block type="operator_join" id="bt3_join_sp3_d">
                                                                                    <value name="STRING1"><shadow type="text"><field name="TEXT"> bằng </field></shadow></value>
                                                                                    <value name="STRING2"><block type="data_variable" id="bt3_res_3_sp"><field name="VARIABLE" id="var_calcResult" variabletype="">calcResult</field></block></value>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </next>
                                                              </block>
                                                            </next>
                                                          </block>
                                                        </statement>
                                                        <next>
                                                          <block type="control_if" id="bt3_if_4">
                                                            <value name="CONDITION">
                                                              <block type="operator_equals" id="bt3_eq_4">
                                                                <value name="OPERAND1"><block type="data_variable" id="bt3_v_op_4"><field name="VARIABLE" id="var_operation" variabletype="">operation</field></block></value>
                                                                <value name="OPERAND2"><shadow type="text"><field name="TEXT">4</field></shadow></value>
                                                              </block>
                                                            </value>
                                                            <statement name="SUBSTACK">
                                                              <block type="control_if_else" id="bt3_div_zero_check">
                                                                <value name="CONDITION">
                                                                  <block type="operator_equals" id="bt3_eq_zero">
                                                                    <value name="OPERAND1"><block type="data_variable" id="bt3_num2_zero"><field name="VARIABLE" id="var_num2" variabletype="">num2</field></block></value>
                                                                    <value name="OPERAND2"><shadow type="text"><field name="TEXT">0</field></shadow></value>
                                                                  </block>
                                                                </value>
                                                                <statement name="SUBSTACK">
                                                                  <block type="text2speech_speakAndWait" id="bt3_speak_zero_err">
                                                                    <value name="WORDS"><shadow type="text"><field name="TEXT">Không thể chia cho số 0</field></shadow></value>
                                                                    <next>
                                                                      <block type="data_setvariableto" id="bt3_set_err">
                                                                        <field name="VARIABLE" id="var_calcResult" variabletype="">calcResult</field>
                                                                        <value name="VALUE"><shadow type="text"><field name="TEXT">lỗi</field></shadow></value>
                                                                      </block>
                                                                    </next>
                                                                  </block>
                                                                </statement>
                                                                <statement name="SUBSTACK2">
                                                                  <block type="data_setvariableto" id="bt3_calc_4">
                                                                    <field name="VARIABLE" id="var_calcResult" variabletype="">calcResult</field>
                                                                    <value name="VALUE">
                                                                      <block type="operator_divide" id="bt3_div_op">
                                                                        <value name="NUM1"><block type="data_variable" id="bt3_num1_4"><field name="VARIABLE" id="var_num1" variabletype="">num1</field></block></value>
                                                                        <value name="NUM2"><block type="data_variable" id="bt3_num2_4"><field name="VARIABLE" id="var_num2" variabletype="">num2</field></block></value>
                                                                      </block>
                                                                    </value>
                                                                    <next>
                                                                      <block type="data_addtolist" id="bt3_add_list_4">
                                                                        <field name="LIST" id="list_history" variabletype="list">history</field>
                                                                        <value name="ITEM">
                                                                          <block type="operator_join" id="bt3_join_list4_a">
                                                                            <value name="STRING1"><block type="data_variable" id="bt3_num1_4_j"><field name="VARIABLE" id="var_num1" variabletype="">num1</field></block></value>
                                                                            <value name="STRING2">
                                                                              <block type="operator_join" id="bt3_join_list4_b">
                                                                                <value name="STRING1"><shadow type="text"><field name="TEXT"> / </field></shadow></value>
                                                                                <value name="STRING2">
                                                                                  <block type="operator_join" id="bt3_join_list4_c">
                                                                                    <value name="STRING1"><block type="data_variable" id="bt3_num2_4_j"><field name="VARIABLE" id="var_num2" variabletype="">num2</field></block></value>
                                                                                    <value name="STRING2">
                                                                                      <block type="operator_join" id="bt3_join_list4_d">
                                                                                        <value name="STRING1"><shadow type="text"><field name="TEXT"> = </field></shadow></value>
                                                                                        <value name="STRING2"><block type="data_variable" id="bt3_res_4_j"><field name="VARIABLE" id="var_calcResult" variabletype="">calcResult</field></block></value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                        <next>
                                                                          <block type="text2speech_speakAndWait" id="bt3_speak_4">
                                                                            <value name="WORDS">
                                                                              <block type="operator_join" id="bt3_join_sp4_a">
                                                                                <value name="STRING1"><block type="data_variable" id="bt3_num1_4_sp"><field name="VARIABLE" id="var_num1" variabletype="">num1</field></block></value>
                                                                                <value name="STRING2">
                                                                                  <block type="operator_join" id="bt3_join_sp4_b">
                                                                                    <value name="STRING1"><shadow type="text"><field name="TEXT"> chia </field></shadow></value>
                                                                                    <value name="STRING2">
                                                                                      <block type="operator_join" id="bt3_join_sp4_c">
                                                                                        <value name="STRING1"><block type="data_variable" id="bt3_num2_4_sp"><field name="VARIABLE" id="var_num2" variabletype="">num2</field></block></value>
                                                                                        <value name="STRING2">
                                                                                          <block type="operator_join" id="bt3_join_sp4_d">
                                                                                            <value name="STRING1"><shadow type="text"><field name="TEXT"> bằng </field></shadow></value>
                                                                                            <value name="STRING2"><block type="data_variable" id="bt3_res_4_sp"><field name="VARIABLE" id="var_calcResult" variabletype="">calcResult</field></block></value>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </next>
                                                                      </block>
                                                                    </next>
                                                                  </block>
                                                                </statement>
                                                              </block>
                                                            </statement>
                                                          </block>
                                                        </next>
                                                      </block>
                                                    </next>
                                                  </block>
                                                </next>
                                              </block>
                                              <next>
                                                <block type="control_if" id="bt3_if_limit">
                                                  <value name="CONDITION">
                                                    <block type="operator_gt" id="bt3_gt_limit">
                                                      <value name="OPERAND1">
                                                        <block type="data_lengthoflist" id="bt3_len">
                                                          <field name="LIST" id="list_history" variabletype="list">history</field>
                                                        </block>
                                                      </value>
                                                      <value name="OPERAND2">
                                                        <shadow type="text"><field name="TEXT">3</field></shadow>
                                                      </value>
                                                    </block>
                                                  </value>
                                                  <statement name="SUBSTACK">
                                                    <block type="data_deleteoflist" id="bt3_del_first">
                                                      <field name="LIST" id="list_history" variabletype="list">history</field>
                                                      <value name="INDEX">
                                                        <shadow type="math_integer"><field name="NUM">1</field></shadow>
                                                      </value>
                                                    </block>
                                                  </statement>
                                                </block>
                                              </next>
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
                              <block type="control_if" id="bt3_if_history">
                                <value name="CONDITION">
                                  <block type="operator_equals" id="bt3_eq_history">
                                    <value name="OPERAND1">
                                      <block type="data_variable" id="bt3_v_op_hist">
                                        <field name="VARIABLE" id="var_operation" variabletype="">operation</field>
                                      </block>
                                    </value>
                                    <value name="OPERAND2">
                                      <shadow type="text"><field name="TEXT">5</field></shadow>
                                    </value>
                                  </block>
                                </value>
                                <statement name="SUBSTACK">
                                  <block type="data_setvariableto" id="bt3_set_i">
                                    <field name="VARIABLE" id="var_i" variabletype="">i</field>
                                    <value name="VALUE">
                                      <shadow type="math_number"><field name="NUM">1</field></shadow>
                                    </value>
                                    <next>
                                      <block type="control_repeat" id="bt3_loop_hist">
                                        <value name="TIMES">
                                          <block type="data_lengthoflist" id="bt3_len_hist">
                                            <field name="LIST" id="list_history" variabletype="list">history</field>
                                          </block>
                                        </value>
                                        <statement name="SUBSTACK">
                                          <block type="looks_sayforsecs" id="bt3_say_item">
                                            <value name="MESSAGE">
                                              <block type="data_itemoflist" id="bt3_get_item">
                                                <field name="LIST" id="list_history" variabletype="list">history</field>
                                                <value name="INDEX">
                                                  <block type="data_variable" id="bt3_v_i">
                                                    <field name="VARIABLE" id="var_i" variabletype="">i</field>
                                                  </block>
                                                </value>
                                              </block>
                                            </value>
                                            <value name="SECS">
                                              <shadow type="math_number"><field name="NUM">2</field></shadow>
                                            </value>
                                            <next>
                                              <block type="data_changevariableby" id="bt3_inc_i">
                                                <field name="VARIABLE" id="var_i" variabletype="">i</field>
                                                <value name="VALUE">
                                                  <shadow type="math_number"><field name="NUM">1</field></shadow>
                                                </value>
                                              </block>
                                            </next>
                                          </block>
                                        </statement>
                                      </block>
                                    </next>
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
    </next>
  </block>
</xml>
`;

(async () => {
  console.log('=== KHỞI ĐỘNG PLAYWRIGHT ĐỂ SINH ĐÁP ÁN BÀI TẬP 3 ===');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });

  try {
    console.log('  Đang truy cập MIT Raise Playground...');
    await page.goto('https://playground.raise.mit.edu/create/', {
      waitUntil: 'domcontentloaded',
      timeout: 90000
    });

    console.log('  Chờ môi trường Blockly sẵn sàng...');
    await page.waitForFunction(() => {
      return window.Blockly &&
        typeof window.Blockly.getMainWorkspace === 'function' &&
        window.Blockly.getMainWorkspace();
    }, { timeout: 90000 });

    await page.waitForTimeout(3000);
    
    // Tải Extension Text to Speech
    await loadExtensions(page, ['Text to Speech']);
    await page.waitForTimeout(2000);

    // Nạp XML vào Workspace
    console.log('  Đang nạp Blockly XML cho Bài tập 3...');
    const renderedXml = await page.evaluate((xml) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      const dom = B.Xml.textToDom(xml);
      B.Xml.domToWorkspace(dom, ws);
      ws.render();
      return new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws));
    }, BT3_XML);

    await page.waitForTimeout(3000);

    // Chụp ảnh màn hình khối lệnh
    const pngPath = path.join(OUT_DIR, 'bt3_code.raw.png');
    await page.screenshot({ path: pngPath, fullPage: true });
    console.log(`  [OK] Đã chụp ảnh và lưu tại: ${pngPath}`);

    // Ghi file XML
    const xmlPath = path.join(OUT_DIR, 'bt3_code.xml');
    fs.writeFileSync(xmlPath, renderedXml, 'utf8');
    console.log(`  [OK] Đã ghi file XML tại: ${xmlPath}`);

    // Tải về file dự án .sb3
    console.log('  Xuất tệp dự án .sb3...');
    const fileMenu = page.locator('div').filter({ hasText: /^File$/ }).first();
    await fileMenu.click();
    await page.waitForTimeout(800);

    const saveOption = page.locator('li').filter({ hasText: /Save to your computer/i }).first();
    
    // Đăng ký bộ lắng nghe sự kiện download
    const downloadPromise = page.waitForEvent('download');
    await saveOption.click();
    const download = await downloadPromise;

    const sb3Path = path.join(OUT_DIR, 'bt3_code.sb3');
    await download.saveAs(sb3Path);
    console.log(`  [OK] Đã xuất và lưu file .sb3 tại: ${sb3Path}`);

    console.log('=== [HOÀN THÀNH BÀI TẬP 3 THÀNH CÔNG] ===');
  } catch (err) {
    console.error(`[FAIL] Đã xảy ra lỗi trong quá trình thực thi: ${err.message}`);
    const failPng = path.join(OUT_DIR, 'bt3_fail.png');
    await page.screenshot({ path: failPng, fullPage: false });
    console.log(`  [DEBUG] Đã chụp ảnh lỗi tại: ${failPng}`);
  } finally {
    await browser.close();
  }
})();
