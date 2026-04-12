Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v10) liên quan đến hạ tầng điều khiển và quản lý mã nguồn trong IoT, Robotics và AI:

- **Fact:** [CONV] SSH (Secure Shell) là giao thức mạng cho phép truy cập an toàn vào máy tính từ xa thông qua một mạng không bảo mật.
- **Source:** [vv10] - Section: The SSH protocol
- **Tag:** [vv10]

- **Fact:** [CONV] Giao thức (Protocol) là một tập hợp các quy tắc quy định cách thức hai đối tượng giao tiếp với nhau, thường được công bố dưới dạng tiêu chuẩn mở để đảm bảo tính tương thích giữa các thiết bị.
- **Source:** [vv10] - Section: What is a protocol?
- **Tag:** [vv10]

- **Fact:** [CONV] SSH hoạt động dựa trên nguyên lý mã hóa khóa công khai (public-key encryption), sử dụng cặp khóa gồm khóa công khai (public key) lưu trên máy chủ và khóa riêng tư (private key) lưu tại máy khách.
- **Source:** [vv10] - Section: The SSH protocol (How it secures)
- **Tag:** [vv10]

- **Fact:** [CONV] Trong SSH, chỉ có khóa riêng tư của máy chủ mới có thể giải mã được thông điệp đã được mã hóa bằng khóa công khai tương ứng, giúp bảo mật dữ liệu ngay cả khi bị chặn trên đường truyền.
- **Source:** [vv10] - Section: The SSH protocol (How it secures)
- **Tag:** [vv10]

- **Fact:** [CONV] SSH thường được sử dụng để đăng nhập từ xa vào máy chủ Linux/Unix, mã hóa việc truyền tập tin và quản lý các thiết bị mạng như router.
- **Source:** [vv10] - Section: Using the SSH protocol
- **Tag:** [vv10]

- **Fact:** [CONV] Việc truyền tập tin an toàn qua SSH được thực hiện thông qua giao thức SCP (Secure Copy Protocol) hoặc SFTP (Secure File Transfer Protocol).
- **Source:** [vv10] - Section: Using the SSH protocol
- **Tag:** [vv10]

- **Fact:** [CONV] SSH hỗ trợ kỹ thuật "tunneling" (chuyển tiếp cổng mạng) để truy cập các dịch vụ nằm sau tường lửa hoặc chạy ứng dụng giao diện đồ họa (GUI) từ xa qua X forwarding.
- **Source:** [vv10] - Section: Using the SSH protocol
- **Tag:** [vv10]

- **Fact:** [CONV] Mặc định, máy khách SSH kết nối với máy chủ thông qua cổng phần mềm số 22.
- **Source:** [vv10] - Section: Configuring SSH
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `ssh-keygen -t rsa -b 2048` được sử dụng để tạo cặp khóa RSA với độ dài 2048 bit nhằm xác thực không cần mật khẩu.
- **Source:** [vv10] - Section: Generating your key pair
- **Tag:** [vv10]

- **Fact:** [CONV] Các khóa SSH thường được lưu trữ trong thư mục ẩn `.ssh` tại thư mục gốc (home directory) của người dùng.
- **Source:** [vv10] - Section: Generating your key pair
- **Tag:** [vv10]

- **Fact:** [CONV] SSH-agent là chương trình quản lý các khóa SSH và passphrase, giúp người dùng không phải nhập lại mật khẩu khóa mỗi khi sử dụng.
- **Source:** [vv10] - Section: Generating your key pair
- **Tag:** [vv10]

- **Fact:** [CONV] Trên hệ điều hành Linux, tệp cấu hình chính của máy chủ SSH (daemon) nằm tại đường dẫn `/etc/ssh/sshd_config`.
- **Source:** [vv10] - Section: Configuring an SSH server
- **Tag:** [vv10]

- **Fact:** [CONV] Lỗi "ssh: connection refused" thường là dấu hiệu cho thấy dịch vụ SSH daemon chưa được cài đặt hoặc chưa được kích hoạt trên máy đích.
- **Source:** [vv10] - Section: Configuring an SSH server
- **Tag:** [vv10]

- **Fact:** [CONV] PuTTY là một phần mềm mã nguồn mở phổ biến hỗ trợ SSH cho các hệ điều hành Windows, Mac và Unix.
- **Source:** [vv10] - Section: Configuring an SSH server
- **Tag:** [vv10]

- **Fact:** [CONV] SSH sẽ đưa ra cảnh báo "Remote host identification has changed" nếu khóa công khai của máy chủ thay đổi, đây có thể là dấu hiệu của một cuộc tấn công nghe lén (eavesdropping).
- **Source:** [vv10] - Section: Pro Tips
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `git config --global credential.helper cache` cho phép Git ghi nhớ thông tin đăng nhập (username/password) tạm thời trong bộ nhớ đệm.