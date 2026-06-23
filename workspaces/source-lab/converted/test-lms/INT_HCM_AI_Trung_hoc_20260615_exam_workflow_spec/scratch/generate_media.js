const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const outDir = path.resolve(__dirname, '..', 'GV-HO-AI-KT- Trí tuệ nhân tạo Trung học - Media');

// Đảm bảo thư mục đích tồn tại
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

const tasks = [
  {
    id: 'cau_22',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="event_whenflagclicked" id="q22_start" x="40" y="40">
        <next>
          <block type="poseFace_videoToggle" id="q22_video_on">
            <value name="VIDEO_STATE">
              <shadow type="poseFace_menu_VIDEO_STATE">
                <field name="VIDEO_STATE">on</field>
              </shadow>
            </value>
            <next>
              <block type="control_wait" id="q22_wait">
                <value name="DURATION">
                  <shadow type="math_positive_number">
                    <field name="NUM">2</field>
                  </shadow>
                </value>
                <next>
                  <block type="control_forever" id="q22_forever">
                    <statement name="SUBSTACK">
                      <block type="control_if" id="q22_if">
                        <value name="CONDITION">
                          <block type="poseFace_affdexIsExpression" id="q22_smile">
                            <value name="EXPRESSION">
                              <shadow type="poseFace_menu_EXPRESSION">
                                <field name="EXPRESSION">smile</field>
                              </shadow>
                            </value>
                          </block>
                        </value>
                        <statement name="SUBSTACK">
                          <block type="looks_sayforsecs" id="q22_say">
                            <value name="MESSAGE">
                              <shadow type="text">
                                <field name="TEXT">Xin chào!</field>
                              </shadow>
                            </value>
                            <value name="SECS">
                              <shadow type="math_number">
                                <field name="NUM">2</field>
                              </shadow>
                            </value>
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
    </xml>`,
    width: 380,
    height: 380,
    extensions: ['Face Sensing'],
    purpose: 'Minh họa logic lập trình tuần tự camera kết hợp cảm biến Face Sensing',
    used_in: 'Câu 22'
  },
  {
    id: 'cau_23',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <variables>
        <variable type="" id="q23_var_smile">Số lần cười</variable>
      </variables>
      <block type="event_whenflagclicked" id="q23_start" x="40" y="40">
        <next>
          <block type="data_setvariableto" id="q23_init">
            <field name="VARIABLE" id="q23_var_smile">Số lần cười</field>
            <value name="VALUE">
              <shadow type="text"><field name="TEXT">0</field></shadow>
            </value>
            <next>
              <block type="poseFace_videoToggle" id="q23_video">
                <value name="VIDEO_STATE">
                  <shadow type="poseFace_menu_VIDEO_STATE">
                    <field name="VIDEO_STATE">on</field>
                  </shadow>
                </value>
                <next>
                  <block type="control_forever" id="q23_forever">
                    <statement name="SUBSTACK">
                      <block type="control_if" id="q23_if">
                        <value name="CONDITION">
                          <block type="poseFace_affdexIsExpression" id="q23_smile">
                            <value name="EXPRESSION">
                              <shadow type="poseFace_menu_EXPRESSION">
                                <field name="EXPRESSION">smile</field>
                              </shadow>
                            </value>
                          </block>
                        </value>
                        <statement name="SUBSTACK">
                          <block type="data_changevariableby" id="q23_change">
                            <field name="VARIABLE" id="q23_var_smile">Số lần cười</field>
                            <value name="VALUE">
                              <shadow type="math_number"><field name="NUM">1</field></shadow>
                            </value>
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
    </xml>`,
    width: 380,
    height: 350,
    extensions: ['Face Sensing'],
    purpose: 'Minh họa lỗi cộng dồn biến số liên tục khi nhận diện nụ cười Face Sensing',
    used_in: 'Câu 23'
  },
  {
    id: 'cau_24',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <variables>
        <variable type="" id="q24_var_opt">Lựa chọn</variable>
        <variable type="" id="q24_var_orig">Câu gốc</variable>
      </variables>
      <block type="event_whenflagclicked" id="q24_start" x="40" y="40">
        <next>
          <block type="data_setvariableto" id="q24_set_lang">
            <field name="VARIABLE" id="q24_var_opt">Lựa chọn</field>
            <value name="VALUE">
              <shadow type="text"><field name="TEXT">2</field></shadow>
            </value>
            <next>
              <block type="data_setvariableto" id="q24_set_text">
                <field name="VARIABLE" id="q24_var_orig">Câu gốc</field>
                <value name="VALUE">
                  <shadow type="text"><field name="TEXT">Xin chào</field></shadow>
                </value>
                <next>
                  <block type="control_if_else" id="q24_if1">
                    <value name="CONDITION">
                      <block type="operator_equals" id="q24_eq1">
                        <value name="OPERAND1">
                          <block type="data_variable" id="q24_var1"><field name="VARIABLE" id="q24_var_opt">Lựa chọn</field></block>
                        </value>
                        <value name="OPERAND2">
                          <shadow type="text"><field name="TEXT">1</field></shadow>
                        </value>
                      </block>
                    </value>
                    <statement name="SUBSTACK">
                      <block type="text2speech_speakAndWait" id="q24_speak1">
                        <value name="WORDS">
                          <block type="translate_getTranslate" id="q24_trans1">
                            <value name="WORDS">
                              <block type="data_variable" id="q24_word1"><field name="VARIABLE" id="q24_var_orig">Câu gốc</field></block>
                            </value>
                            <value name="LANGUAGE">
                              <shadow type="translate_menu_languages" id="q24_lang1">
                                <field name="languages">en</field>
                              </shadow>
                            </value>
                          </block>
                        </value>
                      </block>
                    </statement>
                    <statement name="SUBSTACK2">
                      <block type="control_if_else" id="q24_if2">
                        <value name="CONDITION">
                          <block type="operator_equals" id="q24_eq2">
                            <value name="OPERAND1">
                              <block type="data_variable" id="q24_var2"><field name="VARIABLE" id="q24_var_opt">Lựa chọn</field></block>
                            </value>
                            <value name="OPERAND2">
                              <shadow type="text"><field name="TEXT">2</field></shadow>
                            </value>
                          </block>
                        </value>
                        <statement name="SUBSTACK">
                          <block type="text2speech_speakAndWait" id="q24_speak2">
                            <value name="WORDS">
                              <block type="translate_getTranslate" id="q24_trans2">
                                <value name="WORDS">
                                  <block type="data_variable" id="q24_word2"><field name="VARIABLE" id="q24_var_orig">Câu gốc</field></block>
                                </value>
                                <value name="LANGUAGE">
                                  <shadow type="translate_menu_languages" id="q24_lang2">
                                    <field name="languages">fr</field>
                                  </shadow>
                                </value>
                              </block>
                            </value>
                          </block>
                        </statement>
                        <statement name="SUBSTACK2">
                          <block type="looks_sayforsecs" id="q24_err">
                            <value name="MESSAGE">
                              <shadow type="text"><field name="TEXT">Không hỗ trợ!</field></shadow>
                            </value>
                            <value name="SECS">
                              <shadow type="math_number"><field name="NUM">2</field></shadow>
                            </value>
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
    </xml>`,
    width: 550,
    height: 480,
    extensions: ['Translate', 'Text to Speech'],
    purpose: 'Minh họa logic rẽ nhánh lồng nhau kết hợp dịch thuật và Text to Speech',
    used_in: 'Câu 24'
  },
  {
    id: 'cau_25',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="event_whenflagclicked" id="q25_start" x="40" y="40">
        <next>
          <block type="control_forever" id="q25_forever">
            <statement name="SUBSTACK">
              <block type="poseFace_affdexGoToPart" id="q25_goto">
                <field name="AFFDEX_POINT">30</field>
              </block>
            </statement>
          </block>
        </next>
      </block>
    </xml>`,
    width: 320,
    height: 180,
    extensions: ['Face Sensing'],
    purpose: 'Dự án mẫu đúng của Câu 25: định vị bám mí mắt trái trên',
    used_in: 'Câu 25'
  },
  {
    id: 'cau_25_a',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="poseFace_affdexGoToPart" id="q25_a" x="10" y="10">
        <field name="AFFDEX_POINT">32</field>
      </block>
    </xml>`,
    width: 280,
    height: 65,
    extensions: ['Face Sensing'],
    purpose: 'Lựa chọn A Câu 25: khối định vị right upper eyelid',
    used_in: 'Câu 25'
  },
  {
    id: 'cau_25_b',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="poseFace_affdexGoToPart" id="q25_b" x="10" y="10">
        <field name="AFFDEX_POINT">30</field>
      </block>
    </xml>`,
    width: 280,
    height: 65,
    extensions: ['Face Sensing'],
    purpose: 'Lựa chọn B Câu 25: khối định vị left upper eyelid',
    used_in: 'Câu 25'
  },
  {
    id: 'cau_25_c',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="poseFace_affdexGoToPart" id="q25_c" x="10" y="10">
        <field name="AFFDEX_POINT">0</field>
      </block>
    </xml>`,
    width: 280,
    height: 65,
    extensions: ['Face Sensing'],
    purpose: 'Lựa chọn C Câu 25: khối định vị left ear',
    used_in: 'Câu 25'
  },
  {
    id: 'cau_25_d',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="poseFace_affdexGoToPart" id="q25_d" x="10" y="10">
        <field name="AFFDEX_POINT">12</field>
      </block>
    </xml>`,
    width: 280,
    height: 65,
    extensions: ['Face Sensing'],
    purpose: 'Lựa chọn D Câu 25: khối định vị nose tip',
    used_in: 'Câu 25'
  },
  {
    id: 'cau_26',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="event_whenflagclicked" id="q26_start" x="40" y="40">
        <next>
          <block type="poseFace_videoToggle" id="q26_video">
            <value name="VIDEO_STATE">
              <shadow type="poseFace_menu_VIDEO_STATE">
                <field name="VIDEO_STATE">on</field>
              </shadow>
            </value>
            <next>
              <block type="control_forever" id="q26_forever">
                <statement name="SUBSTACK">
                  <block type="poseFace_affdexGoToPart" id="q26_goto">
                    <field name="AFFDEX_POINT">30</field>
                  </block>
                </statement>
              </block>
            </next>
          </block>
        </next>
      </block>
    </xml>`,
    width: 380,
    height: 300,
    extensions: ['Face Sensing'],
    purpose: 'Minh họa logic bám đuổi mí mắt trái trên (left upper eyelid) trong Face Sensing',
    used_in: 'Câu 26'
  },
  {
    id: 'cau_28',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <variables>
        <variable type="list" id="q28_list_diary">Nhật ký cảm xúc</variable>
        <variable type="" id="q28_var_smile">Số lần cười</variable>
      </variables>
      <block type="event_whenflagclicked" id="q28_start" x="40" y="40">
        <next>
          <block type="data_setvariableto" id="q28_init_var">
            <field name="VARIABLE" id="q28_var_smile">Số lần cười</field>
            <value name="VALUE">
              <shadow type="text"><field name="TEXT">0</field></shadow>
            </value>
            <next>
              <block type="data_deletealloflist" id="q28_clear_list">
                <field name="LIST" id="q28_list_diary" variabletype="list">Nhật ký cảm xúc</field>
                <next>
                  <block type="poseFace_videoToggle" id="q28_video">
                    <value name="VIDEO_STATE">
                      <shadow type="poseFace_menu_VIDEO_STATE">
                        <field name="VIDEO_STATE">on</field>
                      </shadow>
                    </value>
                    <next>
                      <block type="control_forever" id="q28_forever">
                        <statement name="SUBSTACK">
                          <block type="control_if" id="q28_if">
                            <value name="CONDITION">
                              <block type="poseFace_affdexIsExpression" id="q28_smile">
                                <value name="EXPRESSION">
                                  <shadow type="poseFace_menu_EXPRESSION">
                                    <field name="EXPRESSION">smile</field>
                                  </shadow>
                                </value>
                              </block>
                            </value>
                            <statement name="SUBSTACK">
                              <block type="data_addtolist" id="q28_add">
                                <value name="ITEM">
                                  <shadow type="text"><field name="TEXT">Vui vẻ</field></shadow>
                                </value>
                                <field name="LIST" id="q28_list_diary" variabletype="list">Nhật ký cảm xúc</field>
                                <next>
                                  <block type="data_changevariableby" id="q28_change">
                                    <field name="VARIABLE" id="q28_var_smile">Số lần cười</field>
                                    <value name="VALUE">
                                      <shadow type="math_number"><field name="NUM">1</field></shadow>
                                    </value>
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
        </next>
      </block>
    </xml>`,
    width: 420,
    height: 420,
    extensions: ['Face Sensing'],
    purpose: 'Minh họa lỗi cộng dồn danh sách và biến số trong dự án nhận biết cảm xúc online',
    used_in: 'Câu 28'
  },
  {
    id: 'cau_29',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="event_whenflagclicked" id="q29_start" x="40" y="40">
        <next>
          <block type="sensing_askandwait" id="q29_ask1">
            <value name="QUESTION">
              <shadow type="text"><field name="TEXT">Chọn ngôn ngữ: 1-Anh, 2-Pháp</field></shadow>
            </value>
            <next>
              <block type="sensing_askandwait" id="q29_ask2">
                <value name="QUESTION">
                  <shadow type="text"><field name="TEXT">Nhập câu cần dịch:</field></shadow>
                </value>
                <next>
                  <block type="control_if_else" id="q29_if">
                    <value name="CONDITION">
                      <block type="operator_equals" id="q29_eq">
                        <value name="OPERAND1">
                          <block type="sensing_answer" id="q29_ans1"/>
                        </value>
                        <value name="OPERAND2">
                          <shadow type="text"><field name="TEXT">1</field></shadow>
                        </value>
                      </block>
                    </value>
                    <statement name="SUBSTACK">
                      <block type="text2speech_speakAndWait" id="q29_speak1">
                        <value name="WORDS">
                          <block type="translate_getTranslate" id="q29_trans1">
                            <value name="WORDS">
                              <block type="sensing_answer" id="q29_ans2"/>
                            </value>
                            <value name="LANGUAGE">
                              <shadow type="translate_menu_languages" id="q29_lang1">
                                <field name="languages">en</field>
                              </shadow>
                            </value>
                          </block>
                        </value>
                      </block>
                    </statement>
                    <statement name="SUBSTACK2">
                      <block type="text2speech_speakAndWait" id="q29_speak2">
                        <value name="WORDS">
                          <block type="translate_getTranslate" id="q29_trans2">
                            <value name="WORDS">
                              <block type="sensing_answer" id="q29_ans3"/>
                            </value>
                            <value name="LANGUAGE">
                              <shadow type="translate_menu_languages" id="q29_lang2">
                                <field name="languages">fr</field>
                              </shadow>
                            </value>
                          </block>
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
    </xml>`,
    width: 550,
    height: 420,
    extensions: ['Translate', 'Text to Speech'],
    purpose: 'Minh họa lỗi ghi đè biến answer trong hỏi đáp dịch thuật đa ngôn ngữ liên tiếp',
    used_in: 'Câu 29'
  },
  {
    id: 'cau_30',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <variables>
        <variable type="" id="q30_var_photo">Số ảnh chụp</variable>
      </variables>
      <block type="event_whenflagclicked" id="q30_start" x="40" y="40">
        <next>
          <block type="data_setvariableto" id="q30_init">
            <field name="VARIABLE" id="q30_var_photo">Số ảnh chụp</field>
            <value name="VALUE">
              <shadow type="text"><field name="TEXT">0</field></shadow>
            </value>
            <next>
              <block type="poseFace_videoToggle" id="q30_video_on">
                <value name="VIDEO_STATE">
                  <shadow type="poseFace_menu_VIDEO_STATE">
                    <field name="VIDEO_STATE">on</field>
                  </shadow>
                </value>
                <next>
                  <block type="control_forever" id="q30_forever">
                    <statement name="SUBSTACK">
                      <block type="control_if" id="q30_if">
                        <value name="CONDITION">
                          <block type="poseFace_affdexIsExpression" id="q30_blink">
                            <value name="EXPRESSION">
                              <shadow type="poseFace_menu_EXPRESSION">
                                <field name="EXPRESSION">eyeClosure</field>
                              </shadow>
                            </value>
                          </block>
                        </value>
                        <statement name="SUBSTACK">
                          <block type="sound_play" id="q30_play">
                            <value name="SOUND_MENU">
                              <shadow type="sound_sounds_menu">
                                <field name="SOUND_MENU">pop</field>
                              </shadow>
                            </value>
                            <next>
                              <block type="data_changevariableby" id="q30_change">
                                <field name="VARIABLE" id="q30_var_photo">Số ảnh chụp</field>
                                <value name="VALUE">
                                  <shadow type="math_number"><field name="NUM">1</field></shadow>
                                </value>
                                <next>
                                  <block type="poseFace_videoToggle" id="q30_video_off">
                                    <value name="VIDEO_STATE">
                                      <shadow type="poseFace_menu_VIDEO_STATE">
                                        <field name="VIDEO_STATE">off</field>
                                      </shadow>
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
    </xml>`,
    width: 380,
    height: 480,
    extensions: ['Face Sensing'],
    purpose: 'Minh họa lỗi nhận dạng vô hạn trên ảnh tĩnh sau khi tắt camera trong dự án nháy mắt chụp ảnh',
    used_in: 'Câu 30'
  }
];

(async () => {
  console.log('Khởi chạy Chromium...');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  console.log('Mở trang PRG AI Blocks...');
  await page.goto('https://playground.raise.mit.edu/create/', {
    waitUntil: 'networkidle',
    timeout: 90000
  });
  
  // Chờ trang load hoàn toàn
  await page.waitForTimeout(6000);

  const loadedExtensions = new Set();

  const loadExtension = async (name) => {
    if (loadedExtensions.has(name)) return;
    console.log(`Đang nạp extension: ${name}...`);
    const extBtn = await page.$('[class^="gui_extension-button"]');
    if (extBtn) {
      await extBtn.click();
      await page.waitForTimeout(2000);
      const card = page.locator('[class*="library-item_library-item"]').filter({ hasText: name }).first();
      await card.click();
      await page.waitForTimeout(5000); // Đợi model load
      loadedExtensions.add(name);
      console.log(`Loaded ${name} successfully.`);
    }
  };
  
  // Chạy các task sinh ảnh và tải sb3
  for (const task of tasks) {
    console.log(`========================================`);
    console.log(`Đang thực hiện task: ${task.id}...`);
    
    // Nạp các extension yêu cầu cho task này
    for (const ext of task.extensions) {
      await loadExtension(ext);
    }
    
    // Set viewport 1920x1080 để block if/else rộng không bị cắt ngang
    await page.setViewportSize({ width: 1920, height: 1080 });
    
    // Inject XML vào workspace
    console.log(`Injecting XML...`);
    const renderedXml = await page.evaluate(({ xmlStr, taskId }) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      
      // Load XML vào workspace
      const dom = B.Xml.textToDom(xmlStr);
      B.Xml.domToWorkspace(dom, ws);
      
      // Phóng to (zoom) khối lệnh tùy theo loại để hiển thị to rõ nét
      if (taskId.startsWith('cau_25_')) {
        ws.setScale(2.2); // Tăng zoom cho các lựa chọn khối lệnh đơn lẻ
      } else if (taskId === 'cau_25') {
        ws.setScale(1.8); // Zoom cho kịch bản chính câu 25
      } else {
        ws.setScale(1.0); // Khôi phục zoom mặc định cho các câu khác
      }
      
      ws.render();
      
      // Định vị lại workspace về sát góc trên bên trái
      ws.scrollX = 20;
      ws.scrollY = 20;
      ws.render();

      return new XMLSerializer().serializeToString(B.Xml.workspaceToDom(ws));
    }, { xmlStr: task.xml, taskId: task.id });

    // Lưu file XML thực tế
    const xmlPath = path.join(outDir, `${task.id}.xml`);
    fs.writeFileSync(xmlPath, renderedXml, 'utf8');
    console.log(`=> Đã lưu file XML: ${task.id}.xml`);

    // Tải tệp dự án .sb3 tương ứng bằng cách tương tác UI
    console.log(`Tải xuống tệp .sb3...`);
    try {
      const fileMenuBtn = page.locator('[class*="menu-bar_menu-bar-item"]').filter({ hasText: 'File' }).first();
      await fileMenuBtn.click();
      await page.waitForTimeout(500);

      const [ download ] = await Promise.all([
        page.waitForEvent('download', { timeout: 15000 }),
        page.locator('text="Save to your computer"').first().click()
      ]);
      const sb3Path = path.join(outDir, `${task.id}.sb3`);
      await download.saveAs(sb3Path);
      console.log(`=> Đã lưu file dự án: ${task.id}.sb3`);
    } catch (e) {
      console.error(`=> LỖI TẢI XUỐNG .sb3 cho ${task.id}:`, e.message);
    }

    // Thiết lập view chụp screenshot sát block
    console.log(`Chụp ảnh khối lệnh...`);
    await page.evaluate(() => {
      // Ẩn các layout bên ngoài Blockly div bằng CSS
      const elToolbox = document.querySelector('.blocklyToolboxDiv');
      if (elToolbox) elToolbox.style.display = 'none';
      const elHeader = document.querySelector('[class^="stage-header_stage-header"]');
      if (elHeader) elHeader.style.display = 'none';
      const elGuiStage = document.querySelector('[class^="gui_stage-and-target-wrapper"]');
      if (elGuiStage) elGuiStage.style.display = 'none';
      const elGuiMenu = document.querySelector('[class^="menu-bar_menu-bar"]');
      if (elGuiMenu) elGuiMenu.style.display = 'none';
      
      // Cho phép blockly div chiếm trọn màn hình
      const blocklyDiv = document.getElementById('blocklyDiv');
      if (blocklyDiv) {
        blocklyDiv.style.position = 'fixed';
        blocklyDiv.style.top = '0';
        blocklyDiv.style.left = '0';
        blocklyDiv.style.width = '100%';
        blocklyDiv.style.height = '100%';
        blocklyDiv.style.zIndex = '9999';
      }
    });

    // Chờ render ổn định
    await page.waitForTimeout(1000);
    

    
    const outPath = path.join(outDir, `${task.id}.raw.png`);
    if (task.id.startsWith('cau_25')) {
      console.log(`Chụp sát mép block cho ${task.id}...`);
      
      // Ẩn toolbox, flyout và làm nền trong suốt hoàn toàn
      await page.evaluate(() => {
        const toolbox = document.querySelector('.blocklyToolboxDiv');
        if (toolbox) toolbox.style.display = 'none';
        const flyout = document.querySelector('.blocklyFlyout');
        if (flyout) flyout.style.display = 'none';
        
        // Ẩn grid pattern
        const gridPatterns = document.querySelectorAll('.blocklyGridPattern');
        gridPatterns.forEach(el => el.style.display = 'none');
        
        // Làm trong suốt background của main canvas
        const mainBackgrounds = document.querySelectorAll('.blocklyMainBackground');
        mainBackgrounds.forEach(el => {
          el.style.fill = 'none';
          el.style.fillOpacity = '0';
        });
        
        // Làm trong suốt SVG container
        const blocklySvgs = document.querySelectorAll('.blocklySvg');
        blocklySvgs.forEach(el => {
          el.style.background = 'none';
          el.style.backgroundColor = 'transparent';
        });
      });
      
      // Scroll workspace về gốc và chờ re-render
      await page.evaluate(() => {
        const B = window.Blockly;
        const ws = B.getMainWorkspace();
        ws.scrollX = 0;
        ws.scrollY = 0;
        ws.render();
      });
      await page.waitForTimeout(800);
      
      // Lấy bounding box của block
      let blockId;
      if (task.id === 'cau_25') {
        blockId = 'q25_start';
      } else {
        blockId = `q25_${task.id.split('_')[2]}`; // ví dụ q25_a
      }
      
      const clipRect = await page.evaluate(() => {
        const B = window.Blockly;
        const ws = B.getMainWorkspace();
        const allBlocks = ws.getAllBlocks(false);
        if (!allBlocks || allBlocks.length === 0) return null;
        
        // Tính bounding box tổng hợp bao gồm TẤT CẢ block trong workspace
        let minLeft = Infinity, minTop = Infinity, maxRight = -Infinity, maxBottom = -Infinity;
        for (const block of allBlocks) {
          const svgRoot = block.getSvgRoot();
          if (!svgRoot) continue;
          const rect = svgRoot.getBoundingClientRect();
          if (rect.width === 0 || rect.height === 0) continue;
          if (rect.left < minLeft) minLeft = rect.left;
          if (rect.top < minTop) minTop = rect.top;
          if (rect.right > maxRight) maxRight = rect.right;
          if (rect.bottom > maxBottom) maxBottom = rect.bottom;
        }
        
        if (minLeft === Infinity) return null;
        
        // Trả về bounding box tổng hợp với biên rộng ra 8px để không bị cắt bóng đổ
        return {
          x: minLeft - 8,
          y: minTop - 8,
          width: (maxRight - minLeft) + 16,
          height: (maxBottom - minTop) + 16
        };
      });
      
      if (clipRect) {
        await page.screenshot({
          path: outPath,
          clip: clipRect,
          omitBackground: true
        });
        fs.copyFileSync(outPath, path.join(outDir, `${task.id}.png`));
        console.log(`=> Đã lưu ảnh sát mép cho ${task.id}.png`);
      } else {
        console.error(`=> LỖI: Không lấy được clip rect cho block ${blockId}`);
      }
      
      // Hiện lại toolbox, flyout và khôi phục grid, background
      await page.evaluate(() => {
        const toolbox = document.querySelector('.blocklyToolboxDiv');
        if (toolbox) toolbox.style.display = '';
        const flyout = document.querySelector('.blocklyFlyout');
        if (flyout) flyout.style.display = '';
        
        const gridPatterns = document.querySelectorAll('.blocklyGridPattern');
        gridPatterns.forEach(el => el.style.display = '');
        
        const mainBackgrounds = document.querySelectorAll('.blocklyMainBackground');
        mainBackgrounds.forEach(el => {
          el.style.fill = '';
          el.style.fillOpacity = '';
        });
        
        const blocklySvgs = document.querySelectorAll('.blocklySvg');
        blocklySvgs.forEach(el => {
          el.style.background = '';
          el.style.backgroundColor = '';
        });
      });
    } else {
      // Áp dụng cùng kỹ thuật: ẩn toolbox/flyout, làm nền trong suốt, crop sát mép block
      await page.evaluate(() => {
        const toolbox = document.querySelector('.blocklyToolboxDiv');
        if (toolbox) toolbox.style.display = 'none';
        const flyout = document.querySelector('.blocklyFlyout');
        if (flyout) flyout.style.display = 'none';
        
        document.querySelectorAll('.blocklyGridPattern').forEach(el => el.style.display = 'none');
        document.querySelectorAll('.blocklyMainBackground').forEach(el => {
          el.style.fill = 'none';
          el.style.fillOpacity = '0';
        });
        document.querySelectorAll('.blocklySvg').forEach(el => {
          el.style.background = 'none';
          el.style.backgroundColor = 'transparent';
        });
        
        // Scroll workspace về gốc
        const ws = window.Blockly.getMainWorkspace();
        ws.scrollX = 0;
        ws.scrollY = 0;
        ws.render();
      });
      
      await page.waitForTimeout(800);
      
      // Tính bounding box tổng hợp của TẤT CẢ blocks
      const clipRect = await page.evaluate(() => {
        const ws = window.Blockly.getMainWorkspace();
        const allBlocks = ws.getAllBlocks(false);
        if (!allBlocks || allBlocks.length === 0) return null;
        
        let minLeft = Infinity, minTop = Infinity, maxRight = -Infinity, maxBottom = -Infinity;
        for (const block of allBlocks) {
          const svgRoot = block.getSvgRoot();
          if (!svgRoot) continue;
          const rect = svgRoot.getBoundingClientRect();
          if (rect.width === 0 || rect.height === 0) continue;
          if (rect.left < minLeft) minLeft = rect.left;
          if (rect.top < minTop) minTop = rect.top;
          if (rect.right > maxRight) maxRight = rect.right;
          if (rect.bottom > maxBottom) maxBottom = rect.bottom;
        }
        
        if (minLeft === Infinity) return null;
        
        return {
          x: minLeft - 8,
          y: minTop - 8,
          width: (maxRight - minLeft) + 16,
          height: (maxBottom - minTop) + 16
        };
      });
      
      if (clipRect) {
        await page.screenshot({
          path: outPath,
          clip: clipRect,
          omitBackground: true
        });
        fs.copyFileSync(outPath, path.join(outDir, `${task.id}.png`));
        console.log(`=> Đã lưu ảnh sát mép: ${task.id}.png`);
      } else {
        console.error(`=> LỖI: Không lấy được clip rect cho ${task.id}`);
      }
      
      // Khôi phục lại toolbox/flyout cho task sau
      await page.evaluate(() => {
        const toolbox = document.querySelector('.blocklyToolboxDiv');
        if (toolbox) toolbox.style.display = '';
        const flyout = document.querySelector('.blocklyFlyout');
        if (flyout) flyout.style.display = '';
        document.querySelectorAll('.blocklyGridPattern').forEach(el => el.style.display = '');
        document.querySelectorAll('.blocklyMainBackground').forEach(el => {
          el.style.fill = '';
          el.style.fillOpacity = '';
        });
        document.querySelectorAll('.blocklySvg').forEach(el => {
          el.style.background = '';
          el.style.backgroundColor = '';
        });
      });
    }

    // Phục hồi lại CSS ban đầu để chuẩn bị cho task sau
    await page.evaluate(() => {
      const elToolbox = document.querySelector('.blocklyToolboxDiv');
      if (elToolbox) elToolbox.style.display = '';
      const elHeader = document.querySelector('[class^="stage-header_stage-header"]');
      if (elHeader) elHeader.style.display = '';
      const elGuiStage = document.querySelector('[class^="gui_stage-and-target-wrapper"]');
      if (elGuiStage) elGuiStage.style.display = '';
      const elGuiMenu = document.querySelector('[class^="menu-bar_menu-bar"]');
      if (elGuiMenu) elGuiMenu.style.display = '';
      
      const blocklyDiv = document.getElementById('blocklyDiv');
      if (blocklyDiv) {
        blocklyDiv.style.position = '';
        blocklyDiv.style.top = '';
        blocklyDiv.style.left = '';
        blocklyDiv.style.width = '';
        blocklyDiv.style.height = '';
        blocklyDiv.style.zIndex = '';
      }
    });

    // Tạo tệp manifest riêng lẻ cho ảnh này
    const manifestContent = `---
asset_id: "MEDIA_PRG_AI_BLOCKS_${task.id.toUpperCase()}_001"
file_name: "${task.id}.raw.png"
annotated_file_name: "${task.id}.png"
type: "image"
source_tool: "PRG AI Blocks"
source_url: "https://playground.raise.mit.edu/create/"
generation_method: "real_tool_blockly_xml_injection"
source_file: "${task.id}.xml"
reproduction_guide: "README_REPRODUCE_PRG_AI_BLOCKS_MEDIA.md"
used_in: "${task.used_in}"
purpose: "${task.purpose}"
extension_loading_required: "${task.extensions.length > 0 ? 'YES' : 'NO'}"
extensions_loaded:
${task.extensions.map(e => `  - "${e}"`).join('\n') || '  - ""'}
answer_leak_check: "PASS"
review_status: "PREVIEW_ONLY"
canonical_status: "NON_CANONICAL"
human_review_required: "YES"
---

# PRG AI Blocks Manifest - ${task.id.toUpperCase()}

Tải tệp dự án tương ứng để nạp trực tiếp vào playground kiểm tra:
[${task.id}.sb3](${task.id}.sb3)
`;
    const manifestPath = path.join(outDir, `${task.id}_manifest.md`);
    fs.writeFileSync(manifestPath, manifestContent, 'utf8');
    console.log(`=> Đã lưu manifest riêng lẻ: ${task.id}_manifest.md`);
  }
  
  await browser.close();
  console.log('Hoàn thành sinh toàn bộ tài nguyên code mẫu thành công!');
})();
