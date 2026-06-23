const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  await page.goto('https://playground.raise.mit.edu/create/', { waitUntil: 'networkidle', timeout: 90000 });
  await page.waitForSelector('.blocklySvg', { timeout: 30000 });
  await page.waitForTimeout(2000);
  
  // Click File
  console.log('Clicking File Menu...');
  const fileMenuBtn = page.locator('[class*="menu-bar_menu-bar-item"]').filter({ hasText: 'File' }).first();
  await fileMenuBtn.click();
  await page.waitForTimeout(1000);
  
  // Tìm kiếm xem chữ "Save to your computer" ở đâu
  const elementsWithText = await page.evaluate(() => {
    // Duyệt qua tất cả các element chứa text 'Save'
    const els = Array.from(document.querySelectorAll('*')).filter(el => 
      el.textContent && el.textContent.includes('Save to your computer')
    );
    return els.map(el => ({
      tagName: el.tagName,
      className: el.className,
      text: el.innerText ? el.innerText.substring(0, 100) : 'no innerText',
      html: el.outerHTML.substring(0, 300)
    }));
  });
  
  console.log('Elements containing text:', JSON.stringify(elementsWithText, null, 2));
  
  // Thử click thông qua locator text trực tiếp
  console.log('Trying to click Save to your computer via text locator...');
  try {
    const [ download ] = await Promise.all([
      page.waitForEvent('download', { timeout: 10000 }),
      page.locator('text="Save to your computer"').first().click()
    ]);
    const savePath = path.join(__dirname, 'test.sb3');
    await download.saveAs(savePath);
    console.log('SUCCESS! File downloaded to:', savePath);
  } catch (e) {
    console.error('FAILED to download:', e.message);
  }
  
  await browser.close();
})();
