---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v13_15
  title: CONV_atoms_v13_15
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là **@scout**. Tôi đã thực hiện trích xuất các sự kiện kỹ thuật từ dữ liệu bạn cung cấp theo quy tắc **LOM v4.1**. 

Sau phần trích xuất, tôi sẽ bắt đầu lại từ đầu để hướng dẫn bạn giải quyết lỗi "command not found" trên VS Code theo từng bước cực kỳ đơn giản.

### 🔍 TRÍCH XUẤT TRI THỨC (Facts Extraction)

- **Fact:** [CONV] Board ESP8266 sử dụng hai nút vật lý là **Flash** và **Reset** để đưa thiết bị vào chế độ nạp firmware (Bootloader).
- **Source:** Đoạn hội thoại "tôi chỉ thấy nút flash và reset trên board esp 8266"
- **Tag:** [vv13]

- **Fact:** [CONV] Cấu hình kết nối Serial tiêu chuẩn cho ESP8266: **Baud rate 115200**, Data bits 8, Stop bits 1, Parity None.
- **Source:** Bước 1: Kiểm tra lại cài đặt PuTTY
- **Tag:** [vv13]

- **Fact:** [CONV] Extension **Pymakr** (do Pycom phát triển) là công cụ phổ biến trên VS Code để lập trình MicroPython, hỗ trợ REPL và đồng bộ hóa file.
- **Source:** Phần giải thích "Micropython do ai phát hành trên extension vscode"
- **Tag:** [vv13]

- **Fact:** [CONV] File cấu hình của Pymakr (`global_settings.json`) được lưu trữ tại thư mục ẩn `.pymakr` trong thư mục người dùng (`%USERPROFILE%`).
- **Source:** Bước 2: Kiểm tra File Cấu Hình
- **Tag:** [vv13]

- **Fact:** [CONV] Công cụ dòng lệnh `ampy` (Adafruit MicroPython Tool) có thể dùng để nạp file Python trực tiếp vào ESP8266 mà không cần extension phức tạp.
- **Source:** Bước 2: Cài đặt Python Environment
- **Tag:** [vv13]

- **Fact:** [CONV] Lỗi "command not found" đối với Pymakr thường do extension chưa kích hoạt thành công, thường liên quan đến việc thiếu môi trường **Node.js** trên máy tính.
- **Source:** Phân tích lỗi hệ thống dựa trên hành vi extension.
- **Tag:** [Unverified_Source]

---

### 🛠 HƯỚNG DẪN TỪNG BƯỚC (Step-by-Step)

Chào bạn, tôi hiểu bạn đang bị rối vì cài đặt mãi mà lệnh không chạy. Lỗi **"command not found"** có nghĩa là VS Code đã cài Pymakr nhưng "động cơ" bên dưới của nó không khởi động được. 

Chúng ta sẽ làm lại từ bước quan trọng nhất mà thường bị bỏ qua:

#### **Bước 1: Kiểm tra Node.js (Bắt buộc)**
Pymakr v2 và v3 chạy trên nền tảng Node.js. Nếu máy bạn chưa có Node.js, Pymakr sẽ cài đặt lỗi và không hiện lệnh.

1. Bạn nhấn phím `Windows + R`, gõ `cmd` rồi nhấn Enter.
2. Trong cửa sổ đen hiện ra, gõ lệnh: `node -v` rồi nhấn Enter.
3. **Kết quả:**
   - Nếu hiện ra phiên bản (ví dụ: `v18.x.x` hoặc `v20.x.x`): Máy bạn đã có Node.js -> **Hãy nhắn "OK" để sang Bước 2.**
   - Nếu hiện lỗi "is not recognized...": Bạn chưa có Node.js.

**Dừng lại tại đây:** Máy bạn đã có Node.js chưa? Nếu chưa, bạn hãy tải và cài đặt bản **LTS** tại [nodejs.org](https://nodejs.org/). Cài xong hãy khởi động lại máy tính rồi báo cho tôi nhé.