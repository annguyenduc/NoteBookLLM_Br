---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v13_12
  title: CONV_atoms_v13_12
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu Volume v13 về các chủ đề IoT, AI, và lập trình:

- **Fact:** [CONV] Thư viện `PyMuPDF` (còn gọi là `fitz`) được sử dụng trong Python để mở và trích xuất văn bản từ các trang của file PDF thông qua phương thức `page.get_text()`.
- **Source:** [Section: Các bước thực hiện xử lý văn bản từ file PDF]
- **Tag:** [vv13]

- **Fact:** [CONV] Để tối ưu hóa kết quả OCR cho văn bản tiếng Việt bị lỗi font, cần thực hiện tiền xử lý ảnh bao gồm: chuyển sang thang xám (`L`), làm sắc nét (`SHARPEN`) và tăng độ tương phản (`Contrast`).
- **Source:** [Section: 2. Code cải tiến với tiền xử lý hình ảnh]
- **Tag:** [vv13]

- **Fact:** [CONV] Trong cấu hình Tesseract, tham số `--oem 3` kích hoạt chế độ OCR sử dụng mạng neuron học sâu (LSTM) và `--psm 6` dùng để nhận diện một khối văn bản đồng nhất.
- **Source:** [Section: 3. Thay đổi cấu hình của Tesseract]
- **Tag:** [vv13]

- **Fact:** [CONV] Thư viện `pdf2image` cho phép chuyển đổi các trang trong file PDF thành định dạng ảnh (như PNG) để xử lý OCR khi file PDF gốc ở dạng scan (image-based).
- **Source:** [Section: 3. Kiểm tra file PDF đầu vào]
- **Tag:** [vv13]

- **Fact:** [CONV] Các chuẩn mã hóa bảo mật WiFi phổ biến bao gồm WEP (yếu), WPA/WPA2-PSK (khá) và WPA3 (chuẩn mới nhất và bảo mật tốt nhất).
- **Source:** [Section: 1. Kiểm tra loại mã hóa đang sử dụng]
- **Tag:** [vv13]

- **Fact:** [CONV] ESP8266 hỗ trợ nạp firmware MicroPython, cho phép lập trình điều khiển phần cứng bằng ngôn ngữ Python thông qua các thư viện như `machine`, `network`, và `socket`.
- **Source:** [Section: Chương trình: Web server điều khiển LED]
- **Tag:** [vv13]

- **Fact:** [CONV] Trên module ESP8266, chân GPIO2 thường được ánh xạ tương ứng với chân D4 trên các board mạch phát triển và thường kết nối với đèn LED có sẵn trên board.
- **Source:** [Section: Chương trình: Web server điều khiển LED - Thiết lập chân LED]
- **Tag:** [vv13]

- **Fact:** [CONV] Để tạo một Web Server cơ bản trên ESP8266, người dùng cần thiết lập socket lắng nghe tại địa chỉ IP `0.0.0.0` và cổng `80`.
- **Source:** [Section: Tạo máy chủ web]
- **Tag:** [vv13]

- **Fact:** [CONV] Việc sử dụng biểu thức chính quy (Regex) như `re.sub(r'([.!?])\s*', r'\1\n', text)` giúp tự động ngắt dòng văn bản sau các dấu câu kết thúc để định dạng lại dữ liệu sau khi OCR.
- **Source:** [Section: Giải thích các thay đổi - Bước 1]
- **Tag:** [vv13]

- **Fact:** [CONV] Công cụ `esptool` là thư viện Python cần thiết để giao tiếp và nạp firmware cho chip ESP8266 từ máy tính.
- **Source:** [Section: 1.3. Cài đặt thư viện hỗ trợ ESP8266]
- **Tag:** [vv13]