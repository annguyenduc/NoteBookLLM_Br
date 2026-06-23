const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const WORKSPACE_DIR = path.resolve(__dirname, '..', '..', '..', '..', 'workspaces', 'source-lab', 'converted');
const SB3_PATH = path.join(WORKSPACE_DIR, 'bt2_code.sb3');

if (!fs.existsSync(SB3_PATH)) {
  console.error(`Error: SB3 file not found at ${SB3_PATH}`);
  process.exit(1);
}

(async () => {
  console.log('=== Ghi hình video demo Bài tập 2 (Thỏ và Nhím) ===');
  
  const browser = await chromium.launch({
    headless: true,
    args: [
      '--use-fake-ui-for-media-stream',
      '--use-fake-device-for-media-stream'
    ]
  });

  // Tạo context với tính năng quay video (ghi hình Stage)
  const context = await browser.newContext({
    recordVideo: {
      dir: WORKSPACE_DIR,
      size: { width: 1280, height: 720 }
    },
    viewport: { width: 1280, height: 720 }
  });

  const page = await context.newPage();
  
  try {
    console.log('Truy cập trang playground...');
    await page.goto('https://playground.raise.mit.edu/create/', { timeout: 60000 });
    
    console.log('Đợi workspace sẵn sàng...');
    await page.waitForFunction(() => window.Blockly && window.Blockly.getMainWorkspace(), { timeout: 30000 });
    await page.waitForTimeout(2000);

    console.log(`Nạp tệp dự án SB3 mẫu từ ${SB3_PATH}...`);
    const fileInput = page.locator('input[type="file"]').first();
    await fileInput.setInputFiles(SB3_PATH);
    await page.waitForTimeout(5000); // Chờ 5 giây để dự án nạp hoàn toàn

    console.log('Chuyển sang chế độ Full Screen Stage...');
    await page.click('img[alt="Enter full screen mode"]');
    await page.waitForTimeout(2000); // Chờ 2 giây để giao diện Full Screen hiển thị ổn định

    console.log('Bắt đầu chạy dự án (Click Green Flag)...');
    const greenFlagSelector = '[class*="green-flag_green-flag"], img[alt="Green flag"], img[title="Go"]';
    await page.click(greenFlagSelector, { timeout: 5000 });
    await page.waitForTimeout(3000); // Chờ hiển thị hộp thoại hỏi ngôn ngữ

    console.log('Chọn ngôn ngữ: Tiếng Việt (Nhập 1)...');
    // Định vị ô nhập câu trả lời của Scratch stage
    const askInput = page.locator('input[class*="stage-question_question-input"]').first();
    if (await askInput.isVisible()) {
      await askInput.fill('1');
      await page.waitForTimeout(500);
      await page.keyboard.press('Enter');
      console.log('  [OK] Đã chọn Tiếng Việt.');
    } else {
      // Fallback: Tìm thẻ input duy nhất trên trang
      try {
        await page.fill('input', '1');
        await page.keyboard.press('Enter');
        console.log('  [OK] Đã chọn Tiếng Việt (fallback input).');
      } catch (err) {
        console.log('  [WARN] Không thấy ô nhập câu hỏi, thử click cờ xanh lại...');
        await page.click(greenFlagSelector);
        await page.waitForTimeout(2000);
        await page.fill('input', '1');
        await page.keyboard.press('Enter');
      }
    }

    // Thời gian của mỗi cảnh: Đợi thoại chạy xong rồi nhấn Space để chuyển
    console.log('--- Đang kể Cảnh 1 ---');
    await page.waitForTimeout(8000); // Chờ thoại 8s
    
    console.log('Chuyển sang Cảnh 2 (Nhấn Space)...');
    await page.keyboard.press('Space');
    
    console.log('--- Đang kể Cảnh 2 ---');
    await page.waitForTimeout(8000); // Chờ thoại 8s
    
    console.log('Chuyển sang Cảnh 3 (Nhấn Space)...');
    await page.keyboard.press('Space');
    
    console.log('--- Đang kể Cảnh 3 ---');
    await page.waitForTimeout(8000); // Chờ thoại 8s
    
    console.log('Chuyển sang Cảnh 4 (Nhấn Space)...');
    await page.keyboard.press('Space');
    
    console.log('--- Đang kể Cảnh 4 (Kết thúc song ngữ) ---');
    await page.waitForTimeout(16000); // Chờ thoại kết thúc 16s

    console.log('Kết thúc câu chuyện. Đóng trình duyệt...');
  } catch (err) {
    console.error('Lỗi trong quá trình ghi hình:', err.message);
  }

  // Lấy đường dẫn file video ngẫu nhiên để đổi tên
  const video = page.video();
  let videoPath = "";
  if (video) {
    videoPath = await video.path();
    console.log(`Video tạm thời lưu tại: ${videoPath}`);
  }

  await context.close();
  await browser.close();

  // Đổi tên file video thành bt2_demo.webm
  if (videoPath && fs.existsSync(videoPath)) {
    const finalVideoPath = path.join(WORKSPACE_DIR, 'bt2_demo.webm');
    if (fs.existsSync(finalVideoPath)) {
      fs.unlinkSync(finalVideoPath); // Xóa video cũ nếu có
    }
    fs.renameSync(videoPath, finalVideoPath);
    console.log(`[PASS] Video demo đã được lưu thành công tại: ${finalVideoPath}`);
  } else {
    console.log('[FAIL] Không thể lưu file video demo.');
  }
})();
