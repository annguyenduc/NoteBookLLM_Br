---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v13_15
  title: atoms_v13_15
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Tôi sẽ giúp bạn chưng cất lại quy trình và giải quyết lỗi "command not found" một cách hệ thống nhất.

Lỗi "command not found" thường do extension Pymakr không thể khởi chạy vì thiếu môi trường thực thi (Node.js) hoặc bị lỗi tiến trình ngầm. Chúng ta sẽ bắt đầu lại từ đầu.

### **Bước 1: Gỡ bỏ bản cài đặt lỗi và dọn dẹp**

1.  Vào mục **Extensions** (`Ctrl+Shift+X`).
2.  Tìm **Pymakr**, nhấn **Uninstall**.
3.  **Quan trọng:** Đóng hoàn toàn VS Code.
4.  Mở thư mục `%USERPROFILE%\.vscode\extensions` (như bạn đã làm lúc trước) và xóa tất cả các thư mục có tên `pycom.pymakr-x.x.x` nếu chúng còn sót lại.

**Xác nhận:** Bạn đã gỡ cài đặt và xóa thư mục cũ chưa? Nếu rồi, hãy phản hồi "Oki" để sang bước cài đặt môi trường bắt buộc.

--------------------------------------------------
**TRÍCH XUẤT TRI THỨC (LOM v4.1):**

- **Fact:** Pymakr là extension trên VS Code hỗ trợ nạp firmware và code cho ESP8266/ESP32 qua giao diện REPL.
- **Source:** [vv13 - Assistant's previous response].
- **Tag:** [vv13]

- **Fact:** Extension Pymakr (đặc biệt là phiên bản 2.x trở lên) yêu cầu **Node.js** được cài đặt trên hệ điều hành để chạy các tiến trình xử lý Serial.
- **Source:** Kiến thức kỹ thuật về kiến trúc extension Pymakr.
- **Tag:** [Unverified_Source]

- **Fact:** Cấu hình kết nối ESP8266 thông dụng gồm cổng COM (ví dụ: COM32) và Baud rate 115200.
- **Source:** [vv13 - User/Assistant interaction].
- **Tag:** [vv13]