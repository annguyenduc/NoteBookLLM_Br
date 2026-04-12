Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v16) liên quan đến lập trình Python - nền tảng quan trọng trong điều khiển Robotics, IoT và xử lý dữ liệu AI:

- **Fact:** [CONV] Sử dụng hàm `os.path.getmtime(filename)` để lấy mốc thời gian (timestamp) sửa đổi cuối cùng của một tệp tin và `os.path.getctime(filename)` để lấy thời gian tạo tệp.
- **Source:** [vv16] - Section: Python File/Date Handling (Assistant's explanation of `file_date` function).
- **Tag:** [vv16]

- **Fact:** [CONV] Để định dạng đối tượng `datetime` thành chuỗi theo chuẩn `yyyy-mm-dd`, có thể sử dụng phương thức `.strftime('%Y-%m-%d')` hoặc sử dụng định dạng trực tiếp trong chuỗi: `"{:%Y-%m-%d}".format(date)`.
- **Source:** [vv16] - Section: Python File/Date Handling (Assistant's response to "cách tách lấy thời gian").
- **Tag:** [vv16]

- **Fact:** [CONV] `os.path.getsize(filename)` là hàm dùng để trả về kích thước của một tệp tin tính theo đơn vị byte.
- **Source:** [vv16] - Section: Python File/Date Handling (Assistant's response to `create_python_script`).
- **Tag:** [vv16]

- **Fact:** [CONV] Để lấy đường dẫn tuyệt đối của thư mục cha từ thư mục làm việc hiện tại, sử dụng kết hợp: `os.path.abspath(os.path.join(os.getcwd(), ".."))`.
- **Source:** [vv16] - Section: Python File/Date Handling (Assistant's response to `parent_directory`).
- **Tag:** [vv16]

- **Fact:** [CONV] Timestamp là một giá trị số nguyên biểu thị số giây trôi qua kể từ mốc Epoch (00:00:00 UTC ngày 1/1/1970). Nó có ưu điểm là tính di động cao, dễ so sánh và không phụ thuộc vào múi giờ.
- **Source:** [vv16] - Section: Python File/Date Handling (Assistant's response to "timestamp là gì").
- **Tag:** [vv16]

- **Fact:** [CONV] Lỗi `IsADirectoryError: [Errno 21]` xảy ra khi người dùng cố gắng mở một đường dẫn bằng lệnh `open()` với chế độ ghi (`"w"`) nhưng đường dẫn đó hiện đang là một thư mục thay vì một tệp tin.
- **Source:** [vv16] - Section: Python Error Handling (Assistant's response to `IsADirectoryError`).
- **Tag:** [vv16]

- **Fact:** [CONV] Đối tượng trả về từ `csv.reader(f)` là một iterator (đối tượng lặp). Để xem được nội dung bên trong file CSV, cần lặp qua đối tượng này bằng vòng lặp (ví dụ: `for row in csv_f:`) hoặc chuyển đổi nó sang danh sách (list).
- **Source:** [vv16] - Section: CSV Processing (Assistant's response to "Tôi muốn đọc kết quả trong đó").
- **Tag:** [vv16]

- **Fact:** [CONV] Lỗi `ValueError: not enough values to unpack` khi xử lý CSV thường do dòng dữ liệu bị trống hoặc không đủ số lượng cột như kỳ vọng khi thực hiện gán đa biến (unpacking).
- **Source:** [vv16] - Section: CSV Processing (Assistant's response to `ValueError`).
- **Tag:** [vv16]

- **Fact:** [CONV] Trong Visual Studio Code, phím tắt để phóng to màn hình Terminal là `Ctrl + Shift + =` (Windows/Linux) hoặc `Cmd + Shift + =` (macOS).
- **Source:** [vv16] - Section: Environment Setup (Assistant's response to "phóng to màn hình terminal").
- **Tag:** [vv16]

- **Fact:** [CONV] Thư viện `os` và `datetime` là các module tiêu chuẩn trong Python thường được dùng để quản lý hệ thống tệp và dữ liệu thời gian trong các ứng dụng tự động hóa (Automation). [Unverified_Source: Các thư viện này cũng là nền tảng để quản lý log dữ liệu cảm biến trong IoT và Robotics].
- **Source:** [vv16] - Section: Python File/Date Handling.
- **Tag:** [vv16] / [Unverified_Source]