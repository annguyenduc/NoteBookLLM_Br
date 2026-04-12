---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v13_12
  title: atoms_v13_12
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu **Volume v13** liên quan đến IoT, AI và xử lý dữ liệu:

- **Fact:** Sử dụng thư viện `PyMuPDF` (được import dưới tên `fitz`) để trích xuất văn bản từ các file PDF trong môi trường Python.
- **Source:** v13 - Section: Các bước thực hiện (Xử lý văn bản từ file PDF)
- **Tag:** [vv13]

- **Fact:** Sử dụng biểu thức chính quy `re.sub(r'([.!?])\s*', r'\1\n', text)` để tự động thêm dấu xuống dòng sau các dấu câu kết thúc (chấm, hỏi, chấm phẩy), giúp định dạng lại văn bản sau khi nhận diện OCR.
- **Source:** v13 - Section: Giải thích các thay đổi
- **Tag:** [vv13]

- **Fact:** Để cải thiện độ chính xác của OCR Tesseract khi gặp lỗi font, cần tiền xử lý ảnh bằng cách chuyển sang thang xám (Grayscale), làm sắc nét (Sharpen) và tăng độ tương phản (Contrast) thông qua thư viện PIL.
- **Source:** v13 - Section: 2. Code cải tiến với tiền xử lý hình ảnh
- **Tag:** [vv13]

- **Fact:** Cấu hình Tesseract với tham số `--oem 3` để sử dụng chế độ học sâu (Neural networks) và `--psm 6` để nhận diện một khối văn bản thống nhất.
- **Source:** v13 - Section: 3. Thay đổi cấu hình của Tesseract
- **Tag:** [vv13]

- **Fact:** Các chuẩn mã hóa bảo mật WiFi bao gồm WEP (bảo mật yếu), WPA/WPA2-PSK (phổ biến và an toàn hơn), và WPA3 (chuẩn mới nhất và bảo mật tốt nhất hiện nay).
- **Source:** v13 - Section: 1. Kiểm tra loại mã hóa đang sử dụng
- **Tag:** [vv13]

- **Fact:** Trên module ESP8266, chân cắm D4 thường tương ứng với GPIO2, thường được mặc định kết nối với đèn LED tích hợp trên board.
- **Source:** v13 - Section: Chương trình: Web server điều khiển LED
- **Tag:** [vv13]

- **Fact:** Thư viện `network` và `socket` trong MicroPython cho phép ESP8266 kết nối mạng WiFi và khởi tạo một Web Server để điều khiển các chân GPIO thông qua giao thức HTTP.
- **Source:** v13 - Section: Chương trình: Web server điều khiển LED
- **Tag:** [vv13]

- **Fact:** Thư viện `pdf2image` được sử dụng để chuyển đổi các trang của file PDF thành định dạng ảnh (PNG/JPG) nhằm hỗ trợ việc nhận diện văn bản bằng OCR đối với các file PDF dạng scan.
- **Source:** v13 - Section: 3. Kiểm tra file PDF đầu vào
- **Tag:** [vv13]

- **Fact:** Địa chỉ IP mặc định để truy cập vào giao diện cấu hình quản trị của hầu hết các router/modem thường là `192.168.1.1` hoặc `192.168.0.1`.
- **Source:** v13 - Section: 2. Kiểm tra trên router/modem
- **Tag:** [vv13]

- **Fact:** Thonny IDE, uPyCraft IDE và Visual Studio Code là các công cụ phổ biến được sử dụng để lập trình và nạp firmware MicroPython cho chip ESP8266.
- **Source:** v13 - Section: Hướng dẫn nạp mã vào ESP8266
- **Tag:** [vv13]