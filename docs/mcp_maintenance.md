# 📘 HƯỚNG DẪN VẬN HÀNH & BẢO TRÌ HỆ THỐNG MCP (SOP)

> **Thông tin Dự án**: NoteBookLLM_Br | **Tiêu chuẩn**: B2B Premium | **Ngày**: 08/04/2026

---

## 1. 🏗️ CẤU TRÚC HỆ THỐNG MCP
Hệ thống hiện tại của anh bao gồm các "Cổng tri thức" (Servers) được quản lý qua tệp cấu hình trung tâm:
- **NotebookLM MCP**: Kết nối Google NotebookLM.
- **Gemini Sync**: Đồng bộ và chưng cất dữ liệu.
- **Filesystem MCP**: Thao tác tệp tin trực tiếp trên ổ đĩa.

**Vị trí tệp cấu hình**: `C:\Users\anngu\.gemini\antigravity\mcp_config.json`

---

## 2. 🛠️ QUY TRÌNH XỬ LÝ LỖI (DEBUGGING)

### 🔴 Lỗi 1: Xung đột thư viện (TypeError, Pydantic)
- **Biểu hiện**: Server không khởi động được, thông báo lỗi liên quan đến `Field`, `default` hoặc `Pydantic`.
- **Cách khắc phục**: Ép server chạy bằng môi trường ảo (.venv) thay vì Python hệ thống.
- **Cấu hình chuẩn**:
  ```json
  "command": "d:\\NoteBookLLM_Br\\.venv\\Scripts\\python.exe",
  ```

### 🟡 Lỗi 2: Authentication Expired
- **Biểu hiện**: Agent báo lỗi `RPC Error 16` khi dùng NotebookLM.
- **Cách khắc phục**: Mở Terminal và chạy lệnh:
  ```powershell
  notebooklm-mcp-auth
  ```
  Sau đó đăng nhập Google trong trình duyệt Chrome vừa hiện ra.

---

## 3. ➕ CÁCH CÀI ĐẶT SERVER MỚI (VÍ DỤ: FILESYSTEM)
Để thêm một MCP server mới, anh chỉ cần thêm một thẻ (entry) vào `mcpServers` trong `mcp_config.json`.

**Mẫu cho Filesystem (Node.js)**:
```json
"filesystem": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "D:\\NoteBookLLM_Br",
    "D:\\"
  ]
}
```

---

## 📅 QUY TẮC VÀNG (GOLDEN RULES)

1.  **Luôn dùng Đường dẫn Tuyệt đối**: Trong file JSON, dùng `\\` (double backslash) để Windows không bị lỗi.
2.  **Môi trường ưu tiên**: Luôn ưu tiên dùng `.venv` để cài các gói MCP mới bằng lệnh `pip install`.
3.  **Hành động sau khi sửa**: Sau khi sửa `mcp_config.json`, hãy **Reload/Restart MCP Servers** để thay đổi có hiệu lực.

---
*Người soạn: @pm (Antigravity Swarm)*
