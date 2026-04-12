Chào bạn, tôi là @scout. Dựa trên dữ liệu từ Volume v13 (nội dung hội thoại về quản lý dữ liệu trình duyệt và hệ thống), tôi xin trích xuất các sự kiện kỹ thuật liên quan đến môi trường phần mềm và hệ thống (nền tảng cho AI/Robotics/IoT) như sau:

- **Fact**: [CONV] Thư mục AppData\Local lưu trữ cache driver, shader cache và dữ liệu tạm từ NVIDIA GPU, phát sinh trong quá trình xử lý đồ họa hoặc chạy phần mềm chuyên dụng.
- **Source**: [vv13 - Section 5: NVIDIA]
- **Tag**: [vv13]

- **Fact**: [CONV] Các môi trường và công cụ phát triển phổ biến như Python, Anaconda và VSCode thường lưu trữ dữ liệu cài đặt và cấu hình trong thư mục AppData thay vì Program Files.
- **Source**: [vv13 - Section 6: Programs hoặc thư mục liên quan phần mềm cài đặt]
- **Tag**: [vv13]

- **Fact**: [CONV] Tham số dòng lệnh `--user-data-dir` cho phép thay đổi đường dẫn lưu trữ toàn bộ dữ liệu người dùng của trình duyệt (nhân Chromium) sang một vị trí hoặc ổ đĩa khác.
- **Source**: [vv13 - Cách xử lý để giảm dung lượng tăng trên ổ C - Bước 1]
- **Tag**: [vv13]

- **Fact**: [CONV] Tham số `--disk-cache-dir` được sử dụng để tách biệt và chỉ định thư mục lưu trữ bộ nhớ đệm (cache) của trình duyệt, giúp tối ưu không gian ổ đĩa hệ thống.
- **Source**: [vv13 - Cách xử lý để giảm dung lượng tăng trên ổ C - Bước 1]
- **Tag**: [vv13]

- **Fact**: [CONV] Để khởi chạy một hồ sơ người dùng cụ thể trong môi trường có nhiều profile, tham số `--profile-directory="Tên_Profile"` (ví dụ: "Profile 2") được sử dụng trong chuỗi lệnh thực thi.
- **Source**: [vv13 - Cập nhật đường dẫn với tham số --profile-directory]
- **Tag**: [vv13]

- **Fact**: [CONV] Các trình duyệt hiện đại lưu trữ báo cáo lỗi (crash reports), nhật ký (logs) và tệp cấu hình tại đường dẫn cục bộ `AppData\Local\Microsoft\Edge`.
- **Source**: [vv13 - 2. Cache hệ thống hoặc dữ liệu khác trong AppData]
- **Tag**: [vv13]

- **Fact**: [CONV] Các công cụ phân tích như TreeSize Free hoặc WinDirStat được sử dụng để quét và xác định chính xác các thư mục chiếm dụng tài nguyên đĩa lớn trên hệ điều hành Windows.
- **Source**: [vv13 - Cách xác định thư mục nào chiếm nhiều dung lượng nhất]
- **Tag**: [vv13]

- **Fact**: [CONV] Việc thay đổi tham số shortcut của trình duyệt có thể kích hoạt cảnh báo bảo mật từ Microsoft Defender SmartScreen do nhận diện sai lệch cấu trúc thực thi mặc định.
- **Source**: [vv13 - Cách khắc phục tình trạng này]
- **Tag**: [vv13]

--------------------------------------------------
*Lưu ý: Dữ liệu raw tập trung vào quản lý hệ thống và trình duyệt, không chứa thông tin trực tiếp về phần cứng Arduino, YoloBit hoặc các thuật toán AI cụ thể.*