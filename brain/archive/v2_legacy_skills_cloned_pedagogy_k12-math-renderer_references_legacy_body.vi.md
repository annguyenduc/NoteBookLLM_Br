# ➗ Math Renderer (LITE)

> **Goal:** Hiển thị công thức Toán học (LaTeX) dưới dạng trực quan, chuyên nghiệp như sách giáo khoa thông qua MathJax.

## 🚀 Execution Workflow
1. **Extract:** Lấy nội dung Markdown chứa LaTeX.
2. **Save:** Lưu vào `docs/exports/math_preview.md`.
3. **Transform:** Chạy lệnh:
   `python scripts/transformer.py docs/exports/math_preview.md --html`
4. **Deliver:** Gửi link file `.html` kết quả cho người dùng.

## 🎨 Quality Standards
- **Engine:** MathJax (Phải được nhúng trong HTML).
- **Styling:** Sử dụng `style.css` của bộ Kit (Premium Look).
- **Readability:** Công thức không bị vỡ hoặc mất ký hiệu trên trình duyệt.

## 🚨 Quality Gate (Red Flags)
- ❌ Thiếu dấu `$` hoặc `$$` bao quanh công thức LaTeX.
- ❌ File HTML không tải được thư viện MathJax (Lỗi mạng hoặc script).
- ❌ Encoding file không phải UTF-8 dẫn đến lỗi ký tự đặc biệt.

## 💡 Example Triggers
- "Render latex cho đoạn phân tích trên."
- "Xem math preview cho bài học này."
- "Hiện công thức này ra bản đẹp để tôi đọc."
