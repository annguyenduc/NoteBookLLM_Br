# 🛡️ Antigravity Core Principles (Vault Rules)

> **Goal**: Đảm bảo và duy trì tính toàn vẹn của tri thức trong Vault Obsidian `NoteBookLLM_Br`.

## 1. Nguyên tắc Đặt tên (Naming)
- Sử dụng tiếng Việt (UTF-8) hoặc Tiếng Anh (không dấu) tùy ngữ cảnh.
- Tránh dùng khoảng trắng; dùng `_` hoặc CamelCase nếu cần.
- Luôn có prefix số cho các Folder quan trọng (vùng truy cập nhanh).

## 2. Cấu trúc Ghi chú (Metadata)
- Mọi ghi chú mới PHẢI có Frontmatter (YAML) được tạo từ `templates/Note_Template.md`.
- PHẢI có ít nhất một tag `#status` (draft, review, persistent).
- PHẢI gán tag `@agent_id` của Agent tham gia biên soạn.

## 3. Quản lý Liên kết (Linking)
- Ưu tiên sử dụng `[[Wikilinks]]` thay vì link tuyệt đối để tăng tính di động cho Vault.
- Khi nhắc đến một Agent, hãy dùng tag `@` (ví dụ: `@pm`, `@engineer`).

## 4. Bảo mật & An toàn (Safety)
- Tuyệt đối không xóa dữ liệu thô trong `3-resources/raw/` cho đến khi đã được @qa xác nhận đã "Hóa thân" (Distilled) thành công sang `3-resources/distilled/`.
- Mọi thay đổi lớn về cấu trúc Vault phải được `@pm` phê duyệt.

---
**Phê duyệt bởi**: Antigravity PM | **Version**: 1.1.0

## 5. Tính Chính xác & Nguồn Tri thức (Integrity) [NEW]
- **Nguyên tắc "LMS-Only"**: Tri thức trong hệ quản trị LMS CHỈ được lấy từ các tệp nguồn `LMS_Tests`.
- **Cấm Hallucination**: Tuyệt đối không bổ sung kiến thức phổ thông, thực tế bên ngoài hoặc phương pháp sư phạm tự suy luận vào hệ tri thức chuyên sâu nếu đề thi không nhắc tới.
- **Trích dẫn Nguồn**: Mọi thông tin kỹ thuật, thông số phần cứng khi tổng hợp phải có mã đề trích dẫn đi kèm (ví dụ: `[Nguồn: AI_01]`).

