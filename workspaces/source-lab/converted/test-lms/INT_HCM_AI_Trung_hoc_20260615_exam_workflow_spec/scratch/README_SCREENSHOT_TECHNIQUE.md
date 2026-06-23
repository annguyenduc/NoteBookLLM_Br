# Kỹ thuật Chụp Ảnh Khối lệnh Scratch Blockly bằng Playwright (Chuẩn Production)

---

## 1. Tổng quan vấn đề cần giải quyết

Khi chụp màn hình Blockly workspace theo cách thông thường (`page.screenshot()`), ảnh kết quả sẽ bao gồm:

- **Flyout toolbox bên trái**: chiếm khoảng 200–300px không gian ngang
- **Zoom buttons** (góc dưới phải)
- **Background grid pattern** (lưới nền xám)
- **Phần khối lệnh thực tế** chỉ xuất hiện ở vùng bên phải, nhỏ và không rõ nét

**Mục tiêu:**
- Chỉ chụp đúng phần khối lệnh (block stack)
- Không có background, nền trong suốt (transparent PNG)
- Chữ to, rõ ràng — đạt chuẩn xuất bản tài liệu giáo dục

---

## 2. Giải pháp kỹ thuật (6 bước theo thứ tự)

### Bước 1 — Thiết lập Viewport rộng

```javascript
await page.setViewportSize({ width: 1920, height: 1080 });
```

**Lý do:** Flyout toolbox chiếm không gian ngang cố định. Viewport rộng đảm bảo phần block không bị cắt khi tính bounding box.

---

### Bước 2 — Inject XML và đặt zoom scale

```javascript
const ws = window.Blockly.getMainWorkspace();
ws.clear();
const dom = Blockly.Xml.textToDom(xmlStr);
Blockly.Xml.domToWorkspace(dom, ws);

// Zoom cho khối lệnh đơn lẻ (không có context)
ws.setScale(2.2);

// Zoom cho kịch bản ngắn (có hat block + chain)
ws.setScale(1.8);

// Zoom cho kịch bản trung bình
ws.setScale(1.4);

// Zoom bình thường cho kịch bản phức tạp nhiều block
ws.setScale(1.0);
```

Xem hướng dẫn chọn scale tại **Mục 3** bên dưới.

---

### Bước 3 — Ẩn flyout toolbox và làm trong suốt nền

```javascript
// Ẩn toolbox và flyout
document.querySelector('.blocklyToolboxDiv').style.display = 'none';
document.querySelector('.blocklyFlyout').style.display = 'none';

// Ẩn grid background pattern
document.querySelectorAll('.blocklyGridPattern').forEach(el => el.style.display = 'none');

// Làm trong suốt main canvas background
document.querySelectorAll('.blocklyMainBackground').forEach(el => {
  el.style.fill = 'none';
  el.style.fillOpacity = '0';
});

// Làm trong suốt SVG container
document.querySelectorAll('.blocklySvg').forEach(el => {
  el.style.background = 'none';
  el.style.backgroundColor = 'transparent';
});
```

---

### Bước 4 — Scroll workspace về gốc và chờ re-render

```javascript
ws.scrollX = 0;
ws.scrollY = 0;
ws.render();
await page.waitForTimeout(800);
```

**Lý do:** Sau khi ẩn flyout, Blockly có thể re-layout lại nội dung. Scroll về `(0, 0)` đảm bảo block không bị khuất ngoài viewport khi tính bounding box.

---

### Bước 5 — Tính bounding box tổng hợp của TẤT CẢ blocks

```javascript
const allBlocks = ws.getAllBlocks(false);
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

return {
  x: minLeft - 8,  // +8px padding mỗi chiều cho bóng đổ (drop shadow)
  y: minTop - 8,
  width: (maxRight - minLeft) + 16,
  height: (maxBottom - minTop) + 16
};
```

> ⚠️ **LỖI THƯỜNG GẶP — `getSvgRoot()` của hat block:**
>
> ❌ **ĐỪNG dùng:**
> ```javascript
> block.getSvgRoot().getBoundingClientRect()
> // Với ID block đầu tiên (hat block)
> ```
> `getSvgRoot()` của hat block chỉ trả về bounding box của **một ô nhỏ trên cùng**, **KHÔNG bao gồm** toàn bộ chuỗi block bên dưới đã nối vào. Kết quả ảnh bị cắt đứt, chỉ còn phần trên.
>
> ✅ **PHẢI dùng:**
> ```javascript
> ws.getAllBlocks(false)
> // Lấy tất cả blocks và tính union bounding box
> ```

---

### Bước 6 — Chụp screenshot với `omitBackground: true`

```javascript
await page.screenshot({
  path: outPath,
  clip: clipRect,
  omitBackground: true  // <-- BẮT BUỘC để xuất PNG nền trong suốt
});
```

**Lý do:** `omitBackground: true` yêu cầu Playwright không vẽ nền trắng mặc định trước khi chụp, cho phép các pixel trong suốt được giữ nguyên trong file PNG.

---

## 3. Hướng dẫn chọn scale zoom

| Loại kịch bản | Số block ước tính | Scale đề xuất |
|---|---|---|
| Khối lệnh đơn lẻ (không có hat) | 1 block | `2.2` |
| Kịch bản ngắn (hat + 2–3 block) | 3–4 block | `1.8` |
| Kịch bản trung bình | 5–8 block | `1.4` |
| Kịch bản dài, phức tạp | 10+ block | `1.0` |

**Nguyên tắc:** Scale càng cao thì chữ càng to và rõ, nhưng block có thể vượt quá chiều cao 1080px nếu quá nhiều block. Chọn scale để tổng chiều cao block stack **không vượt quá ~900px** (để có thể fit trong viewport).

---

## 4. Tóm tắt quy trình đầy đủ

- **Bước 1:** Set viewport `1920×1080` để tránh block bị cắt
- **Bước 2:** Inject XML vào workspace, chọn scale zoom phù hợp với số lượng block
- **Bước 3:** Ẩn toolbox, flyout, grid, làm trong suốt background SVG
- **Bước 4:** Scroll workspace về `(0, 0)`, gọi `ws.render()`, chờ 800ms re-render
- **Bước 5:** Dùng `ws.getAllBlocks(false)` + union `getBoundingClientRect()` để tính vùng chụp chính xác (tránh lỗi hat block bị cắt)
- **Bước 6:** Chụp với `omitBackground: true` để xuất PNG nền trong suốt

---

## 5. File áp dụng kỹ thuật này

Kỹ thuật này được triển khai trong:

- [`generate_media.js`](./generate_media.js) — Script chính tạo ảnh PNG khối lệnh Scratch cho toàn bộ bài học trong thư mục `scratch/`
