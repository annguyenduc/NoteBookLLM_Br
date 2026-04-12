---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v10_11
  title: CONV_atoms_v10_11
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v10) liên quan đến nền tảng hệ điều hành và lập trình (nền tảng cho IoT, Robotics và AI):

- **Fact:** [CONV] Lệnh `free -h` được sử dụng để hiển thị thông tin về bộ nhớ RAM và swap của hệ thống dưới dạng đơn vị dễ đọc (human-readable) như GB, MB. [Unverified_Source: Đây là thao tác quan trọng để giám sát tài nguyên khi vận hành các mô hình AI hoặc tác vụ Robotics trên các máy tính nhúng như Raspberry Pi].
- **Source:** [Phần: Additional commands - free]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `kill PID` gửi tín hiệu `SIGTERM` đến một tiến trình cụ thể thông qua mã định danh (PID) để yêu cầu kết thúc tiến trình đó một cách an toàn. [Unverified_Source: Thường dùng để dừng các script điều khiển robot hoặc các tiến trình xử lý dữ liệu IoT chạy ngầm].
- **Source:** [Phần: Operating with processes - kill PID / Question 2]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `chmod` được sử dụng để thay đổi quyền truy cập của file (như quyền đọc `+r`), cho phép quản lý quyền thực thi và bảo mật trên hệ thống Linux. [Unverified_Source: Cần thiết khi cấu hình quyền truy cập cổng giao tiếp phần cứng cho các thiết bị IoT].
- **Source:** [Phần: Managing files and directories - chmod/chown/chgrp]
- **Tag:** [vv10]

- **Fact:** [CONV] Trong Python, đối tượng `sys.stdin` từ module `sys` được sử dụng để đọc dữ liệu từ luồng đầu vào chuẩn (standard input). [Unverified_Source: Ứng dụng trong việc nhận lệnh điều khiển hoặc dữ liệu từ cảm biến thông qua đường ống dẫn dữ liệu (pipeline)].
- **Source:** [Phần: Question 3: Practice Quiz]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `top` cung cấp bảng theo dõi thời gian thực về các tiến trình đang tiêu thụ nhiều tài nguyên CPU nhất trên hệ thống. [Unverified_Source: Giúp lập trình viên tối ưu hóa hiệu suất cho các thuật toán AI xử lý thị giác hoặc tính toán phức tạp].
- **Source:** [Phần: Operating with processes - top]
- **Tag:** [vv10]

- **Fact:** [CONV] Từ khóa `raise` trong Python cho phép lập trình viên chủ động kích hoạt một ngoại lệ (exception) để dừng chương trình ngay lập tức khi phát hiện điều kiện bất hợp lệ. [Unverified_Source: Giúp bảo vệ logic điều khiển Robotics, ngăn chặn các hành động sai sót gây hư hỏng phần cứng].
- **Source:** [Phần: ASSISTANT's explanation: raise trong Python là gì?]
- **Tag:** [vv10]

- **Fact