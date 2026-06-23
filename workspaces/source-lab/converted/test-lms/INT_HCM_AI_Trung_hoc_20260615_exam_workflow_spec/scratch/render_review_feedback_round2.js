const { chromium } = require('playwright');
const path = require('path');

const mediaDir = path.resolve(__dirname, '..', 'GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media');

const tasks = [
  {
    imageName: 'cau_14_1.png',
    sourceName: 'cau_14_source_pack.sb3',
    extensions: ['Face Sensing'],
    scale: 0.92,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="motion_changeyby"><value name="DY"><shadow type="math_number"><field name="NUM">5</field></shadow></value></block></statement></block></next></block></next></block></xml>`,
    packXml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="motion_changeyby"><value name="DY"><shadow type="math_number"><field name="NUM">5</field></shadow></value></block></statement></block></next></block></next></block><block type="event_whenflagclicked" x="420" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="poseFace_affdexGoToPart"><field name="AFFDEX_POINT">11</field></block></statement></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_14_2.png',
    sourceName: 'cau_14_source_pack.sb3',
    extensions: ['Face Sensing'],
    scale: 0.92,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="poseFace_affdexGoToPart"><field name="AFFDEX_POINT">11</field></block></statement></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_23_a.png',
    sourceName: 'cau_23_a.sb3',
    extensions: [],
    scale: 0.88,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">Target language?</field></shadow></value></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_23_b.png',
    sourceName: 'cau_23_b.sb3',
    extensions: [],
    scale: 0.88,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q23_lang">ngon_ngu_dich</variable><variable type="list" id="q23_choices">lua_chon</variable></variables><block type="data_setvariableto" x="40" y="40"><field name="VARIABLE" id="q23_lang" variabletype="">ngon_ngu_dich</field><value name="VALUE"><shadow type="text"><field name="TEXT">French</field></shadow></value><next><block type="data_addtolist"><field name="LIST" id="q23_choices" variabletype="list">lua_chon</field><value name="ITEM"><block type="data_variable"><field name="VARIABLE" id="q23_lang" variabletype="">ngon_ngu_dich</field></block></value></block></next></block></xml>`
  },
  {
    imageName: 'cau_23_c.png',
    sourceName: 'cau_23_c.sb3',
    extensions: ['Translate', 'Text to Speech'],
    scale: 0.82,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q23_text">ban_dich</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q23_text" variabletype="">ban_dich</field><value name="VALUE"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">fr</field></shadow></value></block></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="data_variable"><field name="VARIABLE" id="q23_text" variabletype="">ban_dich</field></block></value></block></next></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_23_d.png',
    sourceName: 'cau_23_d.sb3',
    extensions: ['Face Sensing'],
    scale: 0.95,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="poseFace_affdexGoToPart"><field name="AFFDEX_POINT">11</field></block></statement></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_24_a.png',
    sourceName: 'cau_24_a.sb3',
    extensions: ['Face Sensing'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="control_forever" x="40" y="40"><statement name="SUBSTACK"><block type="poseFace_affdexGoToPart"><field name="AFFDEX_POINT">11</field></block></statement></block></xml>`
  },
  {
    imageName: 'cau_24_b.png',
    sourceName: 'cau_24_b.sb3',
    extensions: [],
    scale: 1.1,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenkeypressed" x="40" y="40"><field name="KEY_OPTION">space</field><next><block type="looks_nextcostume"></block></next></block></xml>`
  },
  {
    imageName: 'cau_24_c.png',
    sourceName: 'cau_24_c.sb3',
    extensions: [],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="motion_gotoxy" x="40" y="40"><value name="X"><shadow type="math_number"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number"><field name="NUM">120</field></shadow></value></block></xml>`
  },
  {
    imageName: 'cau_24_d.png',
    sourceName: 'cau_24_d.sb3',
    extensions: ['Face Sensing'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="poseFace_affdexGoToPart" x="40" y="40"><field name="AFFDEX_POINT">0</field></block></xml>`
  },
  {
    imageName: 'cau_25_a.png',
    sourceName: 'cau_25_a.sb3',
    extensions: ['Teachable Machine'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="teachableMachine_videoToggle" x="40" y="40"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value></block></xml>`
  },
  {
    imageName: 'cau_25_b.png',
    sourceName: 'cau_25_b.sb3',
    extensions: ['Teachable Machine'],
    scale: 1.0,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="teachableMachine_useModelBlock" x="40" y="40"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></xml>`
  },
  {
    imageName: 'cau_25_c.png',
    sourceName: 'cau_25_c.sb3',
    extensions: ['Teachable Machine'],
    scale: 0.82,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="list" id="q25_list">co_mat</variable></variables><block type="teachableMachine_whenModelMatches" x="40" y="40"><field name="CLASS_NAME">Class 1</field><next><block type="control_if"><value name="CONDITION"><block type="operator_not"><value name="OPERAND"><block type="data_listcontainsitem"><field name="LIST" id="q25_list" variabletype="list">co_mat</field><value name="ITEM"><shadow type="text"><field name="TEXT">An</field></shadow></value></block></value></block></value><statement name="SUBSTACK"><block type="data_addtolist"><field name="LIST" id="q25_list" variabletype="list">co_mat</field><value name="ITEM"><shadow type="text"><field name="TEXT">An</field></shadow></value><next><block type="looks_say"><value name="MESSAGE"><shadow type="text"><field name="TEXT">Da diem danh</field></shadow></value></block></next></block></statement></block></next></block></xml>`
  },
  {
    imageName: 'cau_25_d.png',
    sourceName: 'cau_25_d.sb3',
    extensions: ['Face Sensing'],
    scale: 0.84,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="list" id="q25d_list">co_mat</variable></variables><block type="control_if" x="40" y="40"><value name="CONDITION"><block type="poseFace_affdexIsTopEmotion"><value name="EMOTION"><shadow type="poseFace_menu_EMOTION"><field name="EMOTION">joy</field></shadow></value></block></value><statement name="SUBSTACK"><block type="data_addtolist"><field name="LIST" id="q25d_list" variabletype="list">co_mat</field><value name="ITEM"><shadow type="text"><field name="TEXT">An</field></shadow></value></block></statement></block></xml>`
  },
  {
    imageName: 'cau_26_1.png',
    sourceName: 'cau_26_source.sb3',
    extensions: ['Face Sensing'],
    scale: 0.92,
    maskBlockId: 'q26_blank',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="poseFace_affdexGoToPart" id="q26_blank"><field name="AFFDEX_POINT">11</field></block></statement></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_26_a.png',
    sourceName: 'cau_26_a.sb3',
    extensions: ['Face Sensing'],
    scale: 1.04,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="poseFace_affdexGoToPart" x="40" y="40"><field name="AFFDEX_POINT">11</field></block></xml>`
  },
  {
    imageName: 'cau_26_b.png',
    sourceName: 'cau_26_b.sb3',
    extensions: ['Face Sensing'],
    scale: 1.04,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="poseFace_affdexGoToPart" x="40" y="40"><field name="AFFDEX_POINT">12</field></block></xml>`
  },
  {
    imageName: 'cau_26_c.png',
    sourceName: 'cau_26_c.sb3',
    extensions: ['Face Sensing'],
    scale: 1.04,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="poseFace_affdexGoToPart" x="40" y="40"><field name="AFFDEX_POINT">30</field></block></xml>`
  },
  {
    imageName: 'cau_26_d.png',
    sourceName: 'cau_26_d.sb3',
    extensions: ['Face Sensing'],
    scale: 1.04,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="poseFace_affdexGoToPart" x="40" y="40"><field name="AFFDEX_POINT">32</field></block></xml>`
  },
  {
    imageName: 'cau_27_a.png',
    sourceName: 'cau_27_a.sb3',
    extensions: ['Face Sensing'],
    scale: 0.9,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="control_if"><value name="CONDITION"><block type="poseFace_affdexIsTopEmotion"><value name="EMOTION"><shadow type="poseFace_menu_EMOTION"><field name="EMOTION">joy</field></shadow></value></block></value><statement name="SUBSTACK"><block type="looks_say"><value name="MESSAGE"><shadow type="text"><field name="TEXT">vui</field></shadow></value><next><block type="looks_switchcostumeto"><value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">hoa</field></shadow></value></block></next></block></statement></block></statement></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_27_b.png',
    sourceName: 'cau_27_b.sb3',
    extensions: ['Face Sensing'],
    scale: 0.94,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="control_if"><value name="CONDITION"><block type="poseFace_affdexIsTopEmotion"><value name="EMOTION"><shadow type="poseFace_menu_EMOTION"><field name="EMOTION">joy</field></shadow></value></block></value><statement name="SUBSTACK"><block type="looks_say"><value name="MESSAGE"><shadow type="text"><field name="TEXT">vui</field></shadow></value></block></statement></block></statement></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_27_c.png',
    sourceName: 'cau_27_c.sb3',
    extensions: ['Face Sensing'],
    scale: 0.9,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="control_if"><value name="CONDITION"><block type="poseFace_affdexIsTopEmotion"><value name="EMOTION"><shadow type="poseFace_menu_EMOTION"><field name="EMOTION">joy</field></shadow></value></block></value><statement name="SUBSTACK"><block type="looks_switchcostumeto"><value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">hoa</field></shadow></value><next><block type="looks_say"><value name="MESSAGE"><shadow type="text"><field name="TEXT">vui</field></shadow></value></block></next></block></statement></block></statement></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_27_d.png',
    sourceName: 'cau_27_d.sb3',
    extensions: ['Face Sensing'],
    scale: 0.94,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on-flipped</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="control_if"><value name="CONDITION"><block type="poseFace_affdexIsTopEmotion"><value name="EMOTION"><shadow type="poseFace_menu_EMOTION"><field name="EMOTION">joy</field></shadow></value></block></value><statement name="SUBSTACK"><block type="looks_switchcostumeto"><value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">hoa</field></shadow></value></block></statement></block></statement></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_28_a.png',
    sourceName: 'cau_28_a.sb3',
    extensions: [],
    scale: 0.76,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q28a_hat">mu_on</variable><variable type="" id="q28a_glass">kinh_on</variable></variables><block type="event_whenkeypressed" x="40" y="40"><field name="KEY_OPTION">1</field><next><block type="control_if_else"><value name="CONDITION"><block type="operator_equals"><value name="OPERAND1"><block type="data_variable"><field name="VARIABLE" id="q28a_hat" variabletype="">mu_on</field></block></value><value name="OPERAND2"><shadow type="math_number"><field name="NUM">0</field></shadow></value></block></value><statement name="SUBSTACK"><block type="data_setvariableto"><field name="VARIABLE" id="q28a_hat" variabletype="">mu_on</field><value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value><next><block type="looks_nextcostume"></block></next></block></statement><statement name="SUBSTACK2"><block type="data_setvariableto"><field name="VARIABLE" id="q28a_hat" variabletype="">mu_on</field><value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value><next><block type="looks_switchcostumeto"><value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">costume1</field></shadow></value></block></next></block></statement></block></next></block><block type="event_whenkeypressed" x="430" y="40"><field name="KEY_OPTION">2</field><next><block type="control_if_else"><value name="CONDITION"><block type="operator_equals"><value name="OPERAND1"><block type="data_variable"><field name="VARIABLE" id="q28a_glass" variabletype="">kinh_on</field></block></value><value name="OPERAND2"><shadow type="math_number"><field name="NUM">0</field></shadow></value></block></value><statement name="SUBSTACK"><block type="data_setvariableto"><field name="VARIABLE" id="q28a_glass" variabletype="">kinh_on</field><value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value><next><block type="looks_nextcostume"></block></next></block></statement><statement name="SUBSTACK2"><block type="data_setvariableto"><field name="VARIABLE" id="q28a_glass" variabletype="">kinh_on</field><value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value><next><block type="looks_switchcostumeto"><value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">costume1</field></shadow></value></block></next></block></statement></block></next></block><block type="event_whenkeypressed" x="820" y="40"><field name="KEY_OPTION">r</field><next><block type="data_setvariableto"><field name="VARIABLE" id="q28a_hat" variabletype="">mu_on</field><value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q28a_glass" variabletype="">kinh_on</field><value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value><next><block type="looks_switchcostumeto"><value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">costume1</field></shadow></value></block></next></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_28_b.png',
    sourceName: 'cau_28_b.sb3',
    extensions: [],
    scale: 0.76,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q28b_hat">mu_on</variable><variable type="" id="q28b_glass">kinh_on</variable></variables><block type="event_whenkeypressed" x="40" y="40"><field name="KEY_OPTION">1</field><next><block type="data_setvariableto"><field name="VARIABLE" id="q28b_hat" variabletype="">mu_on</field><value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value><next><block type="looks_nextcostume"></block></next></block></next></block><block type="event_whenkeypressed" x="350" y="40"><field name="KEY_OPTION">2</field><next><block type="data_setvariableto"><field name="VARIABLE" id="q28b_glass" variabletype="">kinh_on</field><value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value><next><block type="looks_nextcostume"></block></next></block></next></block><block type="event_whenkeypressed" x="670" y="40"><field name="KEY_OPTION">r</field><next><block type="data_setvariableto"><field name="VARIABLE" id="q28b_hat" variabletype="">mu_on</field><value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value><next><block type="looks_switchcostumeto"><value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">costume1</field></shadow></value></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_28_c.png',
    sourceName: 'cau_28_c.sb3',
    extensions: [],
    scale: 0.82,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q28c_all">phu_kien_on</variable></variables><block type="event_whenkeypressed" x="40" y="40"><field name="KEY_OPTION">1</field><next><block type="data_setvariableto"><field name="VARIABLE" id="q28c_all" variabletype="">phu_kien_on</field><value name="VALUE"><shadow type="text"><field name="TEXT">mu</field></shadow></value><next><block type="looks_nextcostume"></block></next></block></next></block><block type="event_whenkeypressed" x="330" y="40"><field name="KEY_OPTION">2</field><next><block type="data_setvariableto"><field name="VARIABLE" id="q28c_all" variabletype="">phu_kien_on</field><value name="VALUE"><shadow type="text"><field name="TEXT">kinh</field></shadow></value><next><block type="looks_nextcostume"></block></next></block></next></block><block type="event_whenkeypressed" x="620" y="40"><field name="KEY_OPTION">r</field><next><block type="data_setvariableto"><field name="VARIABLE" id="q28c_all" variabletype="">phu_kien_on</field><value name="VALUE"><shadow type="text"><field name="TEXT">none</field></shadow></value><next><block type="looks_switchcostumeto"><value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">costume1</field></shadow></value></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_28_d.png',
    sourceName: 'cau_28_d.sb3',
    extensions: [],
    scale: 0.76,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q28d_hat">mu_on</variable><variable type="" id="q28d_glass">kinh_on</variable></variables><block type="event_whenkeypressed" x="40" y="40"><field name="KEY_OPTION">1</field><next><block type="data_setvariableto"><field name="VARIABLE" id="q28d_hat" variabletype="">mu_on</field><value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value><next><block type="looks_nextcostume"></block></next></block></next></block><block type="event_whenkeypressed" x="340" y="40"><field name="KEY_OPTION">2</field><next><block type="data_setvariableto"><field name="VARIABLE" id="q28d_glass" variabletype="">kinh_on</field><value name="VALUE"><shadow type="math_number"><field name="NUM">1</field></shadow></value><next><block type="looks_nextcostume"></block></next></block></next></block><block type="event_whenkeypressed" x="650" y="40"><field name="KEY_OPTION">r</field><next><block type="looks_switchcostumeto"><value name="COSTUME"><shadow type="looks_costume"><field name="COSTUME">costume1</field></shadow></value></block></next></block></xml>`
  },
  {
    imageName: 'cau_29_a.png',
    sourceName: 'cau_29_a.sb3',
    extensions: ['Teachable Machine'],
    scale: 0.68,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="list" id="q29a_list">co_mat</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_resettimer"><next><block type="teachableMachine_videoToggle"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value><next><block type="teachableMachine_useModelBlock"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></next></block></next></block></next></block><block type="teachableMachine_whenModelMatches" x="40" y="300"><field name="CLASS_NAME">Class 1</field><next><block type="control_if"><value name="CONDITION"><block type="operator_not"><value name="OPERAND"><block type="data_listcontainsitem"><field name="LIST" id="q29a_list" variabletype="list">co_mat</field><value name="ITEM"><shadow type="text"><field name="TEXT">An</field></shadow></value></block></value></block></value><statement name="SUBSTACK"><block type="data_addtolist"><field name="LIST" id="q29a_list" variabletype="list">co_mat</field><value name="ITEM"><shadow type="text"><field name="TEXT">An</field></shadow></value></block></statement><next><block type="sensing_resettimer"></block></next></block></next></block><block type="event_whenflagclicked" x="560" y="40"><next><block type="control_forever"><statement name="SUBSTACK"><block type="control_if"><value name="CONDITION"><block type="operator_gt"><value name="OPERAND1"><block type="sensing_timer"></block></value><value name="OPERAND2"><shadow type="math_number"><field name="NUM">10</field></shadow></value></block></value><statement name="SUBSTACK"><block type="teachableMachine_videoToggle"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">off</field></shadow></value></block></statement></block></statement></block></next></block></xml>`
  },
  {
    imageName: 'cau_29_b.png',
    sourceName: 'cau_29_b.sb3',
    extensions: ['Teachable Machine'],
    scale: 0.7,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="list" id="q29b_list">co_mat</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_resettimer"><next><block type="teachableMachine_videoToggle"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value><next><block type="teachableMachine_useModelBlock"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></next></block></next></block></next></block><block type="teachableMachine_whenModelMatches" x="40" y="290"><field name="CLASS_NAME">Class 1</field><next><block type="data_addtolist"><field name="LIST" id="q29b_list" variabletype="list">co_mat</field><value name="ITEM"><shadow type="text"><field name="TEXT">An</field></shadow></value><next><block type="sensing_resettimer"></block></next></block></next></block><block type="event_whenflagclicked" x="540" y="40"><next><block type="control_forever"><statement name="SUBSTACK"><block type="control_if"><value name="CONDITION"><block type="operator_gt"><value name="OPERAND1"><block type="sensing_timer"></block></value><value name="OPERAND2"><shadow type="math_number"><field name="NUM">10</field></shadow></value></block></value><statement name="SUBSTACK"><block type="teachableMachine_videoToggle"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">off</field></shadow></value></block></statement></block></statement></block></next></block></xml>`
  },
  {
    imageName: 'cau_29_c.png',
    sourceName: 'cau_29_c.sb3',
    extensions: ['Teachable Machine'],
    scale: 0.72,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="list" id="q29c_list">co_mat</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_resettimer"><next><block type="teachableMachine_videoToggle"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value><next><block type="teachableMachine_useModelBlock"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></next></block></next></block></next></block><block type="teachableMachine_whenModelMatches" x="40" y="300"><field name="CLASS_NAME">Class 1</field><next><block type="control_if"><value name="CONDITION"><block type="operator_not"><value name="OPERAND"><block type="data_listcontainsitem"><field name="LIST" id="q29c_list" variabletype="list">co_mat</field><value name="ITEM"><shadow type="text"><field name="TEXT">An</field></shadow></value></block></value></block></value><statement name="SUBSTACK"><block type="data_addtolist"><field name="LIST" id="q29c_list" variabletype="list">co_mat</field><value name="ITEM"><shadow type="text"><field name="TEXT">An</field></shadow></value></block></statement><next><block type="sensing_resettimer"></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_29_d.png',
    sourceName: 'cau_29_d.sb3',
    extensions: ['Teachable Machine'],
    scale: 0.7,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="list" id="q29d_list">co_mat</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_resettimer"><next><block type="teachableMachine_videoToggle"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value><next><block type="teachableMachine_useModelBlock"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></next></block></next></block></next></block><block type="teachableMachine_whenModelMatches" x="40" y="290"><field name="CLASS_NAME">Class 1</field><next><block type="control_if"><value name="CONDITION"><block type="operator_not"><value name="OPERAND"><block type="data_listcontainsitem"><field name="LIST" id="q29d_list" variabletype="list">co_mat</field><value name="ITEM"><shadow type="text"><field name="TEXT">An</field></shadow></value></block></value></block></value><statement name="SUBSTACK"><block type="data_addtolist"><field name="LIST" id="q29d_list" variabletype="list">co_mat</field><value name="ITEM"><shadow type="text"><field name="TEXT">An</field></shadow></value></block></statement></block></next></block><block type="event_whenflagclicked" x="560" y="40"><next><block type="control_forever"><statement name="SUBSTACK"><block type="control_if"><value name="CONDITION"><block type="operator_gt"><value name="OPERAND1"><block type="sensing_timer"></block></value><value name="OPERAND2"><shadow type="math_number"><field name="NUM">10</field></shadow></value></block></value><statement name="SUBSTACK"><block type="teachableMachine_videoToggle"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">off</field></shadow></value></block></statement></block></statement></block></next></block></xml>`
  },
  {
    imageName: 'cau_30_a.png',
    sourceName: 'cau_30_a.sb3',
    extensions: ['Translate', 'Text to Speech', 'Face Sensing'],
    scale: 0.74,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q30a_var">ban_dich</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q30a_var" variabletype="">ban_dich</field><value name="VALUE"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="data_variable"><field name="VARIABLE" id="q30a_var" variabletype="">ban_dich</field></block></value><next><block type="event_broadcast"><value name="BROADCAST_INPUT"><shadow type="event_broadcast_menu"><field name="BROADCAST_OPTION" id="q30_msg">start_ai</field></shadow></value></block></next></block></next></block></next></block></next></block><block type="event_whenbroadcastreceived" x="760" y="30"><field name="BROADCAST_OPTION" id="q30_msg">start_ai</field><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value></block></next></block></xml>`
  },
  {
    imageName: 'cau_30_b.png',
    sourceName: 'cau_30_b.sb3',
    extensions: ['Face Sensing'],
    scale: 0.95,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="sensing_resettimer"><next><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value><next><block type="control_forever"><statement name="SUBSTACK"><block type="control_if"><value name="CONDITION"><block type="operator_gt"><value name="OPERAND1"><block type="sensing_timer"></block></value><value name="OPERAND2"><shadow type="math_number"><field name="NUM">10</field></shadow></value></block></value><statement name="SUBSTACK"><block type="poseFace_videoToggle"><value name="VIDEO_STATE"><shadow type="poseFace_menu_VIDEO_STATE"><field name="VIDEO_STATE">off</field></shadow></value></block></statement></block></statement></block></next></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_30_c.png',
    sourceName: 'cau_30_c.sb3',
    extensions: ['Translate', 'Text to Speech', 'Teachable Machine'],
    scale: 0.72,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><variables><variable type="" id="q30c_text">ban_dich</variable></variables><block type="event_whenflagclicked" x="40" y="40"><next><block type="teachableMachine_videoToggle"><value name="VIDEO_STATE"><shadow type="teachableMachine_menu_VIDEO_STATE"><field name="VIDEO_STATE">on</field></shadow></value><next><block type="teachableMachine_useModelBlock"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value><next><block type="sensing_askandwait"><value name="QUESTION"><shadow type="text"><field name="TEXT">English word?</field></shadow></value><next><block type="data_setvariableto"><field name="VARIABLE" id="q30c_text" variabletype="">ban_dich</field><value name="VALUE"><block type="translate_getTranslate"><value name="WORDS"><block type="sensing_answer"></block></value><value name="LANGUAGE"><shadow type="translate_menu_languages"><field name="languages">vi</field></shadow></value></block></value><next><block type="text2speech_speakAndWait"><value name="WORDS"><block type="data_variable"><field name="VARIABLE" id="q30c_text" variabletype="">ban_dich</field></block></value></block></next></block></next></block></next></block></next></block></next></block></xml>`
  },
  {
    imageName: 'cau_30_d.png',
    sourceName: 'cau_30_d.sb3',
    extensions: ['Translate', 'Text to Speech', 'Teachable Machine'],
    scale: 0.9,
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="event_whenflagclicked" x="40" y="40"><next><block type="event_broadcast"><value name="BROADCAST_INPUT"><shadow type="event_broadcast_menu"><field name="BROADCAST_OPTION" id="q30d_msg">start_ai</field></shadow></value></block></next></block><block type="event_whenbroadcastreceived" x="320" y="40"><field name="BROADCAST_OPTION" id="q30d_msg">start_ai</field><next><block type="teachableMachine_useModelBlock"><value name="MODEL_URL"><shadow type="text"><field name="TEXT">Paste URL Here!</field></shadow></value></block></next></block></xml>`
  }
];

async function restoreUi(page) {
  await page.evaluate(() => {
    const style = document.getElementById('codex-render-style');
    if (style) style.remove();
    const mask = document.getElementById('codex-mask');
    if (mask) mask.remove();
  });
  await page.waitForTimeout(250);
}

async function loadExtension(page, loaded, name) {
  if (!name || loaded.has(name)) return;
  await restoreUi(page);
  const extBtn = page.locator('[class^="gui_extension-button"]').first();
  await extBtn.click({ force: true });
  await page.waitForTimeout(1200);
  const card = page
    .locator('[class*="library-item_library-item"], [class*="library_library-item"]')
    .filter({ hasText: name })
    .first();
  await card.click({ force: true });
  await page.waitForTimeout(4500);
  loaded.add(name);
}

async function prepareUi(page) {
  await page.evaluate(() => {
    const style = document.createElement('style');
    style.id = 'codex-render-style';
    style.innerHTML = `
      [class*="gui_menu-bar"],
      [class*="gui_stage-and-target-wrapper"],
      [class*="gui_sidebar"] { display: none !important; }
      .blocklyToolboxDiv, .blocklyFlyout, .blocklyScrollbarBackground, .blocklyScrollbarHandle, .blocklyZoom { display: none !important; }
      .blocklyGridPattern { display: none !important; }
      .blocklyMainBackground { fill: none !important; fill-opacity: 0 !important; }
      .blocklySvg { background: transparent !important; background-color: transparent !important; }
      [class*="gui_blocks-wrapper"] {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: 9999 !important;
      }
      body { background: transparent !important; }
    `;
    const old = document.getElementById('codex-render-style');
    if (old) old.remove();
    document.head.appendChild(style);
  });
}

async function setWorkspaceXml(page, xml, scale) {
  await page.evaluate(({ xml, scale }) => {
    const B = window.Blockly;
    const ws = B.getMainWorkspace();
    ws.clear();
    const dom = B.Xml.textToDom(xml);
    B.Xml.domToWorkspace(dom, ws);
    ws.setScale(scale);
    ws.scrollX = 0;
    ws.scrollY = 0;
    ws.render();
  }, { xml, scale });
}

async function exportProjectFile(page, outPath) {
  await restoreUi(page);
  const fileMenuBtn = page.locator('[class*="menu-bar_menu-bar-item"]').filter({ hasText: 'File' }).first();
  await fileMenuBtn.click();
  await page.waitForTimeout(500);
  const [download] = await Promise.all([
    page.waitForEvent('download', { timeout: 15000 }),
    page.locator('text="Save to your computer"').first().click()
  ]);
  await download.saveAs(outPath);
  await page.waitForTimeout(300);
}

async function maskBlock(page, blockId) {
  if (!blockId) return;
  await page.evaluate(({ blockId }) => {
    const old = document.getElementById('codex-mask');
    if (old) old.remove();
    const ws = window.Blockly.getMainWorkspace();
    const block = ws.getBlockById(blockId);
    if (!block) return;
    const rect = block.getSvgRoot().getBoundingClientRect();
    const mask = document.createElement('div');
    mask.id = 'codex-mask';
    mask.textContent = '?';
    mask.style.cssText = [
      'position:fixed',
      `left:${Math.max(0, rect.left - 2)}px`,
      `top:${Math.max(0, rect.top - 2)}px`,
      `width:${rect.width + 4}px`,
      `height:${rect.height + 4}px`,
      'background:#ffffff',
      'border:3px dashed #d64545',
      'border-radius:8px',
      'display:flex',
      'align-items:center',
      'justify-content:center',
      'font:700 28px Arial',
      'color:#d64545',
      'z-index:20000'
    ].join(';');
    document.body.appendChild(mask);
  }, { blockId });
}

async function captureBlocks(page, outPath) {
  const clip = await page.evaluate(() => {
    const ws = window.Blockly.getMainWorkspace();
    const blocks = ws.getAllBlocks(false);
    if (!blocks.length) return null;
    let minLeft = Infinity;
    let minTop = Infinity;
    let maxRight = -Infinity;
    let maxBottom = -Infinity;
    for (const block of blocks) {
      const root = block.getSvgRoot();
      if (!root) continue;
      const rect = root.getBoundingClientRect();
      if (!rect.width || !rect.height) continue;
      minLeft = Math.min(minLeft, rect.left);
      minTop = Math.min(minTop, rect.top);
      maxRight = Math.max(maxRight, rect.right);
      maxBottom = Math.max(maxBottom, rect.bottom);
    }
    if (minLeft === Infinity) return null;
    const pad = 4;
    return {
      x: Math.max(0, minLeft - pad),
      y: Math.max(0, minTop - pad),
      width: Math.max(1, (maxRight - minLeft) + pad * 2),
      height: Math.max(1, (maxBottom - minTop) + pad * 2)
    };
  });

  if (!clip) throw new Error(`No block clip for ${outPath}`);
  await page.screenshot({ path: outPath, clip, omitBackground: true });
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace(), { timeout: 60000 });
  await page.waitForTimeout(4000);

  const loaded = new Set();
  const exported = new Set();

  for (const task of tasks) {
    for (const ext of task.extensions) {
      await loadExtension(page, loaded, ext);
    }

    if (!exported.has(task.sourceName)) {
      await setWorkspaceXml(page, task.packXml || task.xml, task.scale);
      await page.waitForTimeout(900);
      await exportProjectFile(page, path.join(mediaDir, task.sourceName));
      exported.add(task.sourceName);
    }

    await setWorkspaceXml(page, task.xml, task.scale);
    await page.waitForTimeout(900);
    await prepareUi(page);
    await page.waitForTimeout(300);
    await maskBlock(page, task.maskBlockId);
    await page.waitForTimeout(200);
    await captureBlocks(page, path.join(mediaDir, task.imageName));
    console.log(`Rendered ${task.imageName}`);
  }

  await browser.close();
  console.log('Round 2 review feedback media rendered.');
})().catch(err => {
  console.error(err);
  process.exit(1);
});
