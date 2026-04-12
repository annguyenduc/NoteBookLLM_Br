---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v14_5
  title: atoms_v14_5
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp:

- **Fact:** Module Bluetooth HC-06 là thiết bị dùng cho giao tiếp serial, phổ biến trong các dự án DIY, IoT và điều khiển từ xa.
- **Source:** Section: Conversation: Bluetooth module HC-06
- **Tag:** [vv14]

- **Fact:** Module HC-06 chỉ hỗ trợ chế độ Slave (thiết bị nhận lệnh), không thể tự khởi tạo kết nối như module HC-05.
- **Source:** Section: Conversation: Bluetooth module HC-06
- **Tag:** [vv14]

- **Fact:** HC-06 giao tiếp qua chuẩn UART (RX, TX), cho phép tích hợp dễ dàng với các vi điều khiển như Arduino, ESP32.
- **Source:** Section: Conversation: Bluetooth module HC-06
- **Tag:** [vv14]

- **Fact:** Phạm vi hoạt động thông thường của module HC-06 là khoảng 10 mét tùy môi trường.
- **Source:** Section: Conversation: Bluetooth module HC-06
- **Tag:** [vv14]

- **Fact:** Module HC-06 hoạt động với nguồn 3.3V hoặc 5V, nhưng mức tín hiệu logic cho các chân TX/RX là 3.3V.
- **Source:** Section: Conversation: Bluetooth module HC-06
- **Tag:** [vv14]

- **Fact:** HC-06 sử dụng giao thức Bluetooth Serial (Bluetooth 2.0), không phải Bluetooth Low Energy (BLE).
- **Source:** Section: Conversation: Bluetooth module HC-06 - Mục 1. Khả năng hỗ trợ của HC-06 và iOS
- **Tag:** [vv14]

- **Fact:** Hệ điều hành iOS (như trên iPhone 11 Pro Max) ưu tiên hỗ trợ BLE và không hỗ trợ giao tiếp Bluetooth 2.0 serial thông qua các ứng dụng mặc định.
- **Source:** Section: Conversation: Bluetooth module HC-06 - Mục 1. Khả năng hỗ trợ của HC-06 và iOS
- **Tag:** [vv14]

- **Fact:** Mã PIN mặc định để ghép nối với HC-06 thường là "1234" hoặc "0000".
- **Source:** Section: Conversation: Bluetooth module HC-06 - Mục 4. Một số lưu ý khi làm việc với HC-06
- **Tag:** [vv14]

- **Fact:** Tốc độ baud rate mặc định của module HC-06 thông thường là 9600 baud.
- **Source:** Section: Conversation: Bluetooth module HC-06 - Mục 4. Một số lưu ý khi làm việc với HC-06
- **Tag:** [vv14]

- **Fact:** Khi kết nối HC-06 với Arduino Uno, chân RX của module cần dùng bộ chia áp để giảm tín hiệu từ 5V xuống 3.3V nhằm đảm bảo an toàn.
- **Source:** Section: Conversation: Bluetooth module HC-06 - Bước 1: Kết nối phần cứng
- **Tag:** [vv14]

- **Fact:** Thư viện SoftwareSerial được sử dụng trên Arduino Uno để thiết lập giao tiếp serial với module Bluetooth qua các chân digital (ví dụ chân 10 và 11).
- **Source:** Section: Conversation: Bluetooth module HC-06 - Bước 2: Code lập trình trên Arduino
- **Tag:** [vv14]