---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v12_1
  title: atoms_v12_1
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu Volume 12 liên quan đến IoT, Arduino, và AI:

- **Fact:** Chip chuyển đổi USB-to-Serial CH340/CH341 có mã nhận diện phần cứng là VID_1A86 và PID_7523.
- **Source:** (v12 - Section: Conversation: Cài đặt driver USB)
- **Tag:** [vv12]

- **Fact:** Chip CH340/CH341 thường được sử dụng trong các mạch Arduino clone, ESP8266, ESP32 và các module giao tiếp USB-to-RS232/TTL.
- **Source:** (v12 - Section: Conversation: Cài đặt driver USB - ASSISTANT response)
- **Tag:** [vv12]

- **Fact:** Driver chính thức cho các thiết bị sử dụng chip CH340/CH341 có thể được tải xuống từ trang web của nhà sản xuất WCH (wch.cn).
- **Source:** (v12 - Section: Conversation: Cài đặt driver USB - Cách khắc phục)
- **Tag:** [vv12]

- **Fact:** Lỗi Code 31 ("Object Name already exists") trên Windows xảy ra khi hệ thống không thể tải driver cho thiết bị USB do xung đột driver hoặc lỗi trong Registry sau khi nâng cấp hệ điều hành.
- **Source:** (v12 - Section: Conversation: Cài đặt driver USB - Cách khắc phục lỗi Code 31)
- **Tag:** [vv12]

- **Fact:** Mã GUID lớp thiết bị (Class GUID) cho các cổng COM và LPT (thường dùng cho Arduino/Robotics) trong Registry Windows là `{4d36e978-e325-11ce-bfc1-08002be10318}`.
- **Source:** (v12 - Section: Conversation: Cài đặt driver USB - USER input & Cách 2)
- **Tag:** [vv12]

- **Fact:** Để xử lý xung đột driver USB trong Registry, người dùng có thể tìm đến khóa Class GUID tương ứng và xóa hai giá trị "UpperFilters" và "LowerFilters".
- **Source:** (v12 - Section: Conversation: Cài đặt driver USB - Cách 2: Kiểm tra Windows Registry)
- **Tag:** [vv12]

- **Fact:** Driver chipset là phần mềm trung gian giúp hệ điều hành giao tiếp với các thành phần trên bo mạch chủ như cổng USB, CPU, RAM và các bộ điều khiển lưu trữ.
- **Source:** (v12 - Section: Conversation: Cài đặt driver USB - Driver chipset là gì)
- **Tag:** [vv12]

- **Fact:** Ứng dụng ChatGPT Desktop có tính năng "Companion Window" (cửa sổ đồng hành) thường được kích hoạt bằng tổ hợp phím Alt + Space, có thể gây nhầm lẫn với menu quản lý cửa sổ mặc định của Windows.
- **Source:** (v12 - Section: Conversation: ChatGPT không maximize được)
- **Tag:** [vv12]

- **Fact:** File cấu hình của ứng dụng ChatGPT Desktop (chứa cài đặt phím tắt như `companion_window_hotkey`) được lưu trữ tại đường dẫn `C:\Users\<Tên_User>\AppData\Roaming\ChatGPT\settings.json`.
- **Source:** (v12 - Section: Conversation: ChatGPT không maximize được - Cách 2: Tắt Companion Window)
- **Tag:** [vv12]