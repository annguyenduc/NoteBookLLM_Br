Chào bạn, tôi là **@scout**. Dựa trên dữ liệu từ **Volume v10**, tôi xin trích xuất các sự kiện kỹ thuật liên quan đến nền tảng điều hành và lập trình (vốn là nền tảng cho IoT, Robotics và AI) như sau:

--------------------------------------------------

- **Fact:** Lệnh `mv` trong Linux được sử dụng để di chuyển một hoặc nhiều tệp vào thư mục khác, hoặc dùng để đổi tên tệp (bao gồm cả việc thay đổi chữ hoa/thường do Linux phân biệt kiểu chữ).
- **Source:** (v10 - Section: Managing files and directories)
- **Tag:** [vv10]

- **Fact:** Lệnh `cut` cho phép trích xuất các trường (fields) dữ liệu từ file; ví dụ: `cut -f1 -d","` trích xuất cột đầu tiên từ file CSV, hoặc `cut -c1-3` để trích xuất các ký tự cụ thể.
- **Source:** (v10 - Section: Operating with the content of files)
- **Tag:** [vv10]

- **Fact:** Lệnh `sort -n` được sử dụng để sắp xếp các nội dung trong file theo giá trị số (numerically), khác với `sort` mặc định sắp xếp theo bảng chữ cái.
- **Source:** (v10 - Section: Operating with the content of files)
- **Tag:** [vv10]

- **Fact:** Lệnh `free -h` hiển thị thông tin về bộ nhớ hệ thống (RAM) dưới các đơn vị dễ đọc như GB, MB thay vì byte đơn thuần.
- **Source:** (v10 - Section: Additional commands)
- **Tag:** [vv10]

- **Fact:** Trong quản lý luồng (streams), toán tử `2>` được sử dụng để chuyển hướng luồng lỗi tiêu chuẩn (standard error) của một kịch bản hoặc lệnh vào một tệp riêng biệt.
- **Source:** (v10 - Section: Managing streams)
- **Tag:** [vv10]

- **Fact:** Lệnh `kill` khi thực hiện trong terminal sẽ mặc định gửi tín hiệu `SIGTERM` đến tiến trình (process) được chỉ định qua PID để yêu cầu kết thúc tiến trình đó.
- **Source:** (v10 - Section: Operating with processes / Practice Quiz Q2)
- **Tag:** [vv10]

- **Fact:** Để đọc dữ liệu từ luồng nhập tiêu chuẩn (standard input) trong ngôn ngữ Python, lập trình viên cần sử dụng đối tượng tệp `stdin` từ module `sys`.
- **Source:** (v10 - Practice Quiz Q3)
- **Tag:** [vv10]

- **Fact:** Từ khóa `raise` trong Python được sử dụng để chủ động thông báo một ngoại lệ (exception), giúp dừng chương trình ngay lập tức khi phát hiện điều kiện bất hợp lệ để bảo vệ logic hệ thống.
- **Source:** (v10 - Section: raise trong Python là gì?)
- **Tag:** [vv10]

- **Fact:** Các lệnh Linux cơ bản và kỹ thuật điều hướng luồng (Pipes/Redirections) là nền tảng thiết yếu để lập trình viên tương tác với hệ điều hành, quản lý tệp tin và tiến trình trên các hệ thống máy chủ hoặc thiết bị nhúng.
- **Source:** (v10 - Section: Study guide: Basic Linux commands / Redirections, Pipes, and Signals)
- **Tag:** [vv10] [Unverified_Source: Liên kết ứng dụng vào IoT/Robotics]

--------------------------------------------------
**Ghi chú từ @scout:** Dữ liệu RAW tập trung vào kỹ năng Linux CLI và Python cơ bản, đây là các kỹ năng bổ trợ quan trọng để cấu hình các thiết bị IoT (như Raspberry Pi) hoặc điều khiển robot chạy trên nền tảng Linux (như ROS).