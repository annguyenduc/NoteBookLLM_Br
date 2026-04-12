Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cấu hình Pymakr và các phản hồi liên quan:

- **Fact:** Cấu hình kết nối mặc định của Pymakr (pymakr.connection) được thiết lập sử dụng cổng `COM32` với tốc độ `baudrate` là `115200`.
- **Source:** Dữ liệu JSON, phần "pymakr.connection".
- **Tag:** [vv13]

- **Fact:** Tất cả các thiết bị Serial (từ COM3 đến COM32) trong danh sách cấu hình đều sử dụng thông tin xác thực mặc định là `username`: "micro" và `password`: "python".
- **Source:** Dữ liệu JSON, phần "pymakr.devices.configs".
- **Tag:** [vv13]

- **Fact:** Thuộc tính `autoConnect` của các cổng Serial được thiết lập giá trị `onLostConnection`, cho phép thiết bị tự động kết nối lại khi bị ngắt quãng.
- **Source:** Dữ liệu JSON, thuộc tính "autoConnect" trong các mục "serial://".
- **Tag:** [vv13]

- **Fact:** Cấu hình dự án Pymakr sử dụng danh sách `py_ignore` để loại trừ các thư mục và tệp tin hệ thống bao gồm: `.vscode`, `.gitignore`, `.git`, `env`, và `venv`.
- **Source:** Đoạn mã JSON cấu hình dự án "pym".
- **Tag:** [vv13]

- **Fact:** Lỗi `debug.showDeviceSummary` xảy ra do lỗi logic "Cannot destructure property 'device' of 'undefined'", thường xuất hiện khi extension không tìm thấy đối tượng thiết bị đang hoạt động.
- **Source:** Thông báo lỗi hệ thống trong phần USER cung cấp.
- **Tag:** [vv13]

- **Fact:** Để chỉnh sửa cấu hình Pymakr thủ công trên VS Code, người dùng cần truy cập vào tệp `settings.json` thông qua lệnh `Preferences: Open User Settings (JSON)`.
- **Source:** Phản hồi hướng dẫn trong phần ASSISTANT và xác nhận của USER.
- **Tag:** [vv13]

- **Fact:** Ngoài các cổng Serial, cấu hình còn chứa một định danh thiết bị đặc biệt là `"0001"` với các thông số tương tự như các cổng COM.
- **Source:** Dữ liệu JSON, phần cuối của "pymakr.devices.configs".
- **Tag:** [vv13]