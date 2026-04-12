---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v13_16
  title: CONV_atoms_v13_16
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp:

- Fact: [CONV] Extension **PyMakr** (phát triển bởi Pycom) trên Visual Studio Code được sử dụng để lập trình và kết nối với các thiết bị IoT như ESP8266.
- Source: [v13 - Bước 1: Kiểm tra lại cài đặt PyMakr]
- Tag: [vv13]

- Fact: [CONV] Cấu hình kết nối cho PyMakr trong tệp `settings.json` bao gồm hai thông số quan trọng là cổng kết nối (`port`) và tốc độ baud (`baudrate`), thường mặc định là **115200**.
- Source: [v13 - Bước 3: Kiểm tra cài đặt trong settings.json]
- Tag: [vv13]

- Fact: [CONV] PyMakr yêu cầu môi trường máy tính phải cài đặt **Python** và thư viện **PySerial** (`pip install pyserial`) để thực hiện giao tiếp qua cổng COM.
- Source: [v13 - Mục 2: Kiểm tra cài đặt Python và Thư viện PySerial]
- Tag: [vv13]

- Fact: [CONV] Các lệnh điều khiển thiết bị phổ biến trong PyMakr bao gồm: `Connect all devices` (Kết nối thiết bị), `Sync file to device` (Đồng bộ tệp) và `Upload current file` (Tải tệp hiện tại lên thiết bị).
- Source: [v13 - Mục 4: Kiểm tra lại Command Palette]
- Tag: [vv13]

- Fact: [CONV] Khi không tìm thấy Node.js trên hệ thống, PyMakr sẽ tự động chuyển sang sử dụng các tệp nhị phân được xây dựng sẵn (**prebuild binaries**).
- Source: [v13 - Phản hồi về lỗi "Node not found"]
- Tag: [vv13]

- Fact: [CONV] Chip cầu nối USB-to-UART thường gặp trên các mạch ESP8266 là **Silicon Labs CP210x**, được hệ thống nhận diện thông qua driver tương ứng để tạo cổng COM ảo.
- Source: [v13 - Log hệ thống: Silicon Labs CP210x USB to UART Bridge (COM32)]
- Tag: [vv13]

- Fact: [CONV] Lỗi `Cannot read properties of undefined (reading 'project')` trong PyMakr thường xuất hiện khi extension không xác định được thư mục dự án hoặc thư mục làm việc hiện tại đang trống.
- Source: [v13 - Phản hồi về lỗi "connectAllInProject"]
- Tag: [vv13]

- Fact: [CONV] Để gỡ lỗi (debug) kết nối, người dùng có thể truy cập log chi tiết bằng cách mở cửa sổ **Output** (`Ctrl + Shift + U`) và chọn mục **PyMakr** từ menu thả xuống.
- Source: [v13 - Cách chọn Chọn PyMakr từ danh sách Log]
- Tag: [vv13]

- Fact: [CONV] Thao tác nhấn nút **Reset** hoặc **Flash** trên board mạch ESP8266 là một bước khắc phục phổ biến để đưa thiết bị về trạng thái sẵn sàng nhận tín hiệu đồng bộ từ phần mềm.
- Source: [v13 - Bước 4: Reset lại ESP8266 và thử lại]
- Tag: [vv13]

- Fact: [CONV] Trong cấu hình nâng cao của PyMakr (`pymakr.devices.configs`), mỗi cổng serial có thể thiết lập các thuộc tính như `autoConnect` (tự động kết nối lại khi mất tín hiệu), `username` và `password` (mặc định thường là micro/python).
- Source: [v13 - Cấu trúc file JSON cấu hình thiết bị]
- Tag: [vv13]