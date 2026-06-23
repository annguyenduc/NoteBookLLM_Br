const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const outDir = path.resolve(__dirname, '..', 'GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media');

const tasks = [
  {
    id: 'cau_11_move',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="motion_movesteps" id="q11_move" x="40" y="40">
        <value name="STEPS">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
      </block>
    </xml>`,
    zoom: 2.2,
    purpose: 'Khối lệnh move 10 steps đơn lẻ cho câu 11'
  },
  {
    id: 'cau_11_turn',
    xml: `<xml xmlns="http://www.w3.org/1999/xhtml">
      <block type="motion_turnright" id="q11_turn" x="40" y="40">
        <value name="DEGREES">
          <shadow type="math_number">
            <field name="NUM">15</field>
          </shadow>
        </value>
      </block>
    </xml>`,
    zoom: 2.2,
    purpose: 'Khối lệnh turn right 15 degrees đơn lẻ cho câu 11'
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
  
  await page.waitForTimeout(6000);

  for (const task of tasks) {
    console.log(`========================================`);
    console.log(`Đang thực hiện task: ${task.id}...`);
    
    await page.setViewportSize({ width: 1920, height: 1080 });
    
    console.log(`Injecting XML...`);
    await page.evaluate(({ xmlStr, zoom }) => {
      const B = window.Blockly;
      const ws = B.getMainWorkspace();
      ws.clear();
      
      const dom = B.Xml.textToDom(xmlStr);
      B.Xml.domToWorkspace(dom, ws);
      
      ws.setScale(zoom);
      ws.render();
      
      ws.scrollX = 20;
      ws.scrollY = 20;
      ws.render();
    }, { xmlStr: task.xml, zoom: task.zoom });

    console.log(`Chụp ảnh khối lệnh...`);
    await page.evaluate(() => {
      const elToolbox = document.querySelector('.blocklyToolboxDiv');
      if (elToolbox) elToolbox.style.display = 'none';
      const elHeader = document.querySelector('[class^="stage-header_stage-header"]');
      if (elHeader) elHeader.style.display = 'none';
      const elGuiStage = document.querySelector('[class^="gui_stage-and-target-wrapper"]');
      if (elGuiStage) elGuiStage.style.display = 'none';
      const elGuiMenu = document.querySelector('[class^="menu-bar_menu-bar"]');
      if (elGuiMenu) elGuiMenu.style.display = 'none';
      
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

    await page.waitForTimeout(1000);
    
    const outPath = path.join(outDir, `${task.id}.png`);
    
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
      
      const ws = window.Blockly.getMainWorkspace();
      ws.scrollX = 0;
      ws.scrollY = 0;
      ws.render();
    });
    
    await page.waitForTimeout(800);
    
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
      console.log(`=> Đã lưu ảnh sạch: ${task.id}.png`);
    } else {
      console.error(`=> LỖI: Không lấy được clip rect cho ${task.id}`);
    }
    
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

  await browser.close();
  console.log('Hoàn thành sinh hình ảnh cau_11 thành công!');
})();
