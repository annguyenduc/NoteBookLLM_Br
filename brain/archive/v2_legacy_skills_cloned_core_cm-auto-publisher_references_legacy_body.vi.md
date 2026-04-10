# 🚀 Auto-Publisher (LITE)

> **Goal:** Tự động hóa quy trình xuất bản bài viết (Markdown + Media) lên hệ thống website Astro thông qua Router API, đảm bảo tính nhất quán của Git history và xử lý ảnh thông minh.

## 📦 API Payload Structure
| Field | Type | Description |
|---|---|---|
| `site_id` | String | ID của trang web đích (Ví dụ: `cody-master`). |
| `title` | String | Tiêu đề hấp dẫn (SEO-friendly). |
| `description`| String | Meta description (1-2 câu). |
| `content` | String | Nội dung Markdown thô. |
| `media` | Array | Mảng `[{url: "...", filename: cm-auto-publisher

## 🚀 5-Phase Workflow
1. **Analyze:** Trích xuất nội dung từ URL/Video/Raw text.
2. **Media Prep:** Xây dựng mảng `media` với tên file kebab-case.
3. **Payload:** Khởi tạo JSON payload hoàn chỉnh.
4. **Push:** Gửi POST request tới Router API (Cloudflare Workers) kèm API Key.
5. **Verify:** Xác nhận response `{"success": true}` và thông báo commit SHA.

## 📐 Execution Rule
- **Router API:** `https://content-factory-router.<ACCOUNT>.workers.dev/publish`
- **Method:** POST với `Authorization: Bearer <API_KEY>`.
- **Media:** Không tải ảnh về máy. Router API sẽ tự động xử lý từ URL gốc.

## 🚨 Quality Gate (Red Flags)
- ❌ Tự ý tạo file `.mdx` và `git push` thủ công (Gây xung đột dữ liệu).
- ❌ Dùng `echo` hoặc `cat` để dựng JSON phức tạp (Bắt buộc viết ra file `.json`).
- ❌ Tên file media không đạt chuẩn SEO (Bắt buộc dùng kebab-case).
- ❌ Thiếu API Key hoặc sai `site_id`.

## 💡 Example Triggers
- "Xuất bản bài viết này lên blog CodyMaster."
- "Lấy tin từ link [URL] và đẩy lên trang tin tức tự động."
- "Publish draft bài học Robotics lên hệ thống."
