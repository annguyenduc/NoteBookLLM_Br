---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v12_8
  title: CONV_atoms_v12_8
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu Volume v12 liên quan đến IoT, lập trình Python và cấu hình công cụ hỗ trợ (VS Code, Pymakr):

- **Fact:** [CONV] Lộ trình học Python cơ bản ước tính cần khoảng 100–140 giờ, với 50% thời gian dành cho thực hành, có thể hoàn thành trong 2–4 tháng.
- **Source:** [v12 - Section: Tổng thời gian ước tính]
- **Tag:** [vv12]

- **Fact:** [CONV] Để thiết lập môi trường lập trình Python trên VS Code, cần cài đặt "Python Extension" chính thức từ Microsoft thông qua Extensions Marketplace.
- **Source:** [v12 - Section: 1. Cài đặt môi trường phát triển trong VS Code]
- **Tag:** [vv12]

- **Fact:** [CONV] Việc chọn môi trường Python (Interpreter) trong VS Code được thực hiện qua Command Palette (Ctrl+Shift+P) với lệnh `Python: Select Interpreter`.
- **Source:** [v12 - Section: 2. Cấu hình VS Code cho Python]
- **Tag:** [vv12]

- **Fact:** [CONV] Linting là công cụ giúp phát hiện lỗi cú pháp (ví dụ: Pylint, Flake8), còn Formatting giúp tự động định dạng mã nguồn theo chuẩn (ví dụ: Black, autopep8).
- **Source:** [v12 - Section: 2. Cấu hình VS Code cho Python]
- **Tag:** [vv12]

- **Fact:** [CONV] Extension Pymakr (thường dùng cho IoT/MicroPython) sử dụng giao thức Serial qua cổng COM với tốc độ baudrate mặc định là 115200 để kết nối thiết bị.
- **Source:** [v12 - Section: USER settings.json dump]
- **Tag:** [vv12]

- **Fact:** [CONV] Cấu hình mặc định cho các thiết bị vi điều khiển trong Pymakr thường sử dụng username là "micro" và password là "python".
- **Source:** [v12 - Section: USER settings.json dump]
- **Tag:** [vv12]

- **Fact:** [CONV] Thuộc tính `autoConnect` trong cấu hình Pymakr với giá trị `onLostConnection` cho phép tự động kết nối lại thiết bị nếu đường truyền bị ngắt.
- **Source:** [v12 - Section: USER settings.json dump]
- **Tag:** [vv12]

- **Fact:** [CONV] Công cụ Black được cấu hình làm `formatting.provider` trong VS Code với tham số mặc định độ dài dòng là 88 ký tự (`--line-length=88`).
- **Source:** [v12 - Section: Cấu hình settings.json]
- **Tag:** [vv12]

- **Fact:** [CONV] Có thể sử dụng file `tasks.json` trong thư mục `.vscode` để tạo các tác vụ tự động hóa (Tasks), giúp chuyển đổi nhanh cấu hình giữa Pylint và Flake8 mà không cần sửa file settings thủ công.
- **Source:** [v12 - Section: 3. Cấu hình file tasks.json]
- **Tag:** [vv12]

- **Fact:** [CONV] Các thư viện bổ trợ cho việc thực hành IoT và xử lý dữ liệu như `pandas` (xử lý bảng), `datetime` (thời gian) và các công cụ linting được cài đặt thông qua trình quản lý gói `pip`.
- **Source:** [v12 - Section: 4. Bài thực hành gợi ý & Cài đặt cơ bản cho Linting và Formatting]
- **Tag:** [vv12]

- **Fact:** [CONV] Pymakr là công cụ phổ biến để lập trình các dòng mạch hỗ trợ MicroPython như YoloBit hoặc ESP32 trực tiếp trên VS Code.
- **Source:** [Dựa trên ngữ cảnh sử dụng Pymakr và thông tin "micro/python"]
- **Tag:** [Unverified_Source]

- **Fact:** [CONV] Việc ẩn các file cache như `__pycache__` hoặc `*.pyc` trong VS Code Explorer giúp giao diện làm việc gọn gàng hơn, được cấu hình qua mục `files.exclude` trong `settings.json`.
- **Source:** [v12 - Section: Cấu hình đề xuất]
- **Tag:** [vv12]