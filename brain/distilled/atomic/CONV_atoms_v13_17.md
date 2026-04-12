Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cấu hình Pymakr (Volume v13):

- **Fact:** [CONV] Pymakr sử dụng định dạng URI `serial://COM[số]` để định danh và quản lý các cổng kết nối vật lý của thiết bị IoT.
- **Source:** [v13 - Section: pymakr.devices.configs]
- **Tag:** [vv13]

- **Fact:** [CONV] Thông tin xác thực mặc định cho các thiết bị MicroPython trong cấu hình này được thiết lập với username là "micro" và password là "python".
- **Source:** [v13 - Các trường "username" và "password" trong cấu hình serial]
- **Tag:** [vv13]

- **Fact:** [CONV] Tính năng tự động kết nối lại của Pymakr được điều khiển bởi thuộc tính `autoConnect`, với giá trị "onLostConnection" để duy trì liên lạc khi thiết bị mất tín hiệu.
- **Source:** [v13 - Trường "autoConnect" trong các block cấu hình]
- **Tag:** [vv13]

- **Fact:** [CONV] Cấu hình Pymakr cho phép quản lý đồng thời danh sách nhiều cổng COM (ví dụ: COM3, COM8, COM13, COM14, COM18, COM19, COM20, COM27, COM29) và các thiết bị định danh bằng ID (như "0001").
- **Source:** [v13 - Danh sách các key trong đối tượng "pymakr.devices.configs"]
- **Tag:** [vv13]

- **Fact:** [CONV] Thuộc tính `rootPath` trong cấu hình thiết bị mặc định được để giá trị `null`, cho phép người dùng xác định thư mục gốc để đồng bộ mã nguồn lên thiết bị IoT.
- **Source:** [v13 - Trường "rootPath" trong cấu hình serial]
- **Tag:** [vv13]

- **Fact:** [CONV] Pymakr hỗ trợ thuộc tính `hidden` (kiểu boolean) để ẩn hoặc hiện thiết bị trong giao diện quản lý của tiện ích.
- **Source:** [v13 - Trường "hidden" trong cấu hình thiết bị]
- **Tag:** [vv13]

- **Fact:** [CONV] Cấu hình dự án Pymakr sử dụng trường `py_ignore` để loại bỏ các thư mục không cần thiết như `.vscode`, `.git`, `env`, `venv` khỏi quá trình đồng bộ lên mạch điều khiển.
- **Source:** [v13 - Section: py_ignore configuration]
- **Tag:** [vv13]