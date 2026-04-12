---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v16_1
  title: CONV_atoms_v16_1
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu Volume 16 (v16) theo quy tắc LOM v4.1:

- **Fact:** [CONV] Để chạy một cell cụ thể trong Google Colab, người dùng có thể nhấn vào biểu tượng `Run` (hình tam giác), nhấn `Shift + Enter` (chạy và chuyển sang cell tiếp theo), hoặc `Ctrl + Enter` (chạy và giữ nguyên vị trí).
- **Source:** (v16 - Section: Conversation: Chạy cell trên Colab - Mục 3: Chạy từng cell)
- **Tag:** [vv16]

- **Fact:** [CONV] Trong Google Colab, menu `Runtime` cung cấp các tùy chọn `Run all` (chạy toàn bộ notebook), `Interrupt execution` (tạm dừng) và `Restart runtime` (khởi động lại môi trường).
- **Source:** (v16 - Section: Conversation: Chạy cell trên Colab - Mục 4 & 5)
- **Tag:** [vv16]

- **Fact:** [CONV] Thư viện `gspread` được sử dụng để tương tác với Google Sheets, trong khi `PyDrive` hoặc `google-api-python-client` được dùng để thao tác với dữ liệu trên Google Drive.
- **Source:** (v16 - Section: Conversation: Chạy cell trên Colab - Chú thích mã nguồn)
- **Tag:** [vv16]

- **Fact:** [CONV] Để xác thực quyền truy cập tài khoản Google trong môi trường Colab, sử dụng lệnh `from google.colab import auth` và `auth.authenticate_user()`.
- **Source:** (v16 - Section: Conversation: Chạy cell trên Colab - Bước 2 trong mã mẫu)
- **Tag:** [vv16]

- **Fact:** [CONV] Việc giải nén file trực tiếp trên Google Drive thông qua Colab giúp tiết kiệm thời gian và băng thông so với việc tải về máy tính cá nhân.
- **Source:** (v16 - Section: Conversation: Chạy cell trên Colab - Yêu cầu của USER)
- **Tag:** [vv16]

- **Fact:** [CONV] Để upload file (ví dụ file JSON) từ máy tính lên Google Colab, sử dụng module `from google.colab import files` với lệnh `files.upload()`.
- **Source:** (v16 - Section: Conversation: Chạy cell trên Colab - Hướng dẫn upload file JSON)
- **Tag:** [vv16]

- **Fact:** [CONV] Thư viện `patool` (patoolib) hỗ trợ giải nén nhiều định dạng file lưu trữ khác nhau bao gồm cả `.zip` và `.rar` trong môi trường Python.
- **Source:** (v16 - Section: Conversation: Chạy cell trên Colab - Mã nguồn cập nhật)
- **Tag:** [vv16]

- **Fact:** [CONV] Công cụ `gdown` có thể được sử dụng trong Colab để tải tệp tin hoặc toàn bộ thư mục từ Google Drive thông qua dòng lệnh (ví dụ: `gdown --folder <link>`).
- **Source:** (v16 - Section: Conversation: Chạy cell trên Colab - Mã nguồn xử lý lỗi 404)
- **Tag:** [vv16]

- **Fact:** [CONV] MimeType `application/vnd.google-apps.folder` được Google Drive API sử dụng để xác định một đối tượng là thư mục thay vì tệp tin thông thường.
- **Source:** (v16 - Section: Conversation: Chạy cell trên Colab - Mã nguồn kiểm tra mime_type)
- **Tag:** [vv16]

- **Fact:** [CONV] ID của tệp tin hoặc thư mục trên Google Drive có thể được trích xuất từ URL bằng Regex thông qua các mẫu phổ biến như `/d/([ID])`, `folders/([ID])`, hoặc `open?id=([ID])`.
- **Source:** (v16 - Section: Conversation: Chạy cell trên Colab - Hàm extract_id_from_url)
- **Tag:** [vv16]

- **Fact:** [CONV] Gemini (trong bối cảnh công nghệ chung) có thể là một giao thức mạng nhẹ (Gemini Protocol) thay thế cho HTTP, tập trung vào chia sẻ văn bản đơn giản.
- **Source:** (v16 - Section: Conversation: Chạy cell trên Colab - Giải thích về Gemini)
- **Tag:** [vv16]

- **Fact:** [CONV] Google Colab có khả năng kết nối và đọc dữ liệu trực tiếp từ một Google Sheet cụ thể thông qua `spreadsheet_id` và `worksheet_name`.
- **Source:** (v16 - Section: Conversation: Chạy cell trên Colab - Bước 4: Đọc dữ liệu)
- **Tag:** [vv16]