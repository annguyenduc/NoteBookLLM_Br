---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v12_1
  title: CONV_atoms_v12_1
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v12) theo quy tắc LOM v4.1:

**1. Lĩnh vực: AI (ChatGPT Application)**
- **Fact:** [CONV] Ứng dụng ChatGPT trên máy tính có chế độ "Companion Mode" (Cửa sổ đồng hành), thường được kích hoạt mặc định bằng tổ hợp phím **Alt + Space**, khiến ứng dụng không mở ở chế độ toàn màn hình (maximize) mà hiện dưới dạng cửa sổ nhỏ.
- **Source:** [v12 - Conversation: ChatGPT không maximize được]
- **Tag:** [vv12]

- **Fact:** [CONV] Để vô hiệu hóa hoặc thay đổi cách hoạt động của Companion Mode trong ChatGPT, người dùng có thể thay đổi "Companion window hotkey" trong phần Settings hoặc chỉnh sửa file cấu hình `settings.json` tại đường dẫn `C:\Users\<Tên_User>\AppData\Roaming\ChatGPT`.
- **Source:** [v12 - Conversation: ChatGPT không maximize được]
- **Tag:** [vv12]

**2. Lĩnh vực: IoT & Arduino (Phần cứng & Driver)**
- **Fact:** [CONV] Mã nhận diện thiết bị **VID_1A86** và **PID_7523** tương ứng với chip **CH340/CH341 USB-to-Serial Adapter**. Đây là loại chip chuyển đổi giao tiếp UART phổ biến được sử dụng trong các mạch Arduino clone, module ESP8266, ESP32 và các thiết bị nhúng.
- **Source:** [v12 - Conversation: Cài đặt driver USB]
- **Tag:** [vv12]

- **Fact:** [CONV] Lỗi **Code 31** với thông báo **"Object Name already exists"** trên Windows xảy ra khi hệ thống không thể tải driver cho thiết bị USB do xung đột Registry hoặc cài đặt driver không đúng cách.
- **Source:** [v12 - Conversation: Cài đặt driver USB]
- **Tag:** [vv12]

- **Fact:** [CONV] Một phương pháp kỹ thuật để xử lý lỗi driver USB (như CH340) là truy cập Registry Editor theo đường dẫn `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e978-e325-11ce-bfc1-08002be10318}` và xóa các khóa **UpperFilters** hoặc **LowerFilters** nếu có để loại bỏ xung đột.
- **Source:** [v12 - Conversation: Cài đặt driver USB]
- **Tag:** [vv12]

**3. Lĩnh vực: Robotics & Phần cứng hệ thống**
- **Fact:** [CONV] **Driver Chipset** là phần mềm nền tảng giúp hệ điều hành giao tiếp với bo mạch chủ (mainboard), quản lý các tài nguyên quan trọng cho robot và hệ thống nhúng như cổng USB, CPU, RAM, các chuẩn kết nối PCIe, SATA và NVMe.
- **Source:** [v12 - Conversation: Cài đặt driver USB]
- **Tag:** [vv12]

- **Fact:** [CONV] Để xác định chính xác loại chipset và mainboard nhằm cài đặt driver phù hợp, có thể sử dụng công cụ **System Information** của Windows thông qua lệnh `msinfo32` để kiểm tra mục **Baseboard Manufacturer** và **Baseboard Product**.
- **Source:** [v12 - Conversation: Cài đặt driver USB]
- **Tag:** [vv12]