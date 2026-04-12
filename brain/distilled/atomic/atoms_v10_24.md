Dưới đây là các sự kiện (Facts) kỹ thuật được trích xuất từ dữ liệu RAW (Volume v10) liên quan đến hạ tầng mạng, quản lý thiết bị từ xa (SSH) và môi trường lập trình:

- **Fact:** SSH (Secure Shell) là giao thức kết nối giữa client và server thông qua cổng phần mềm số 22.
- **Source:** (v10 - Section: Configuring SSH)
- **Tag:** [vv10]

- **Fact:** Lệnh `ssh-keygen -t rsa -b 2048` được sử dụng để tạo cặp khóa công khai/riêng tư (public/private key pair) nhằm xác thực kết nối mà không cần mật khẩu.
- **Source:** (v10 - Section: Generating your key pair)
- **Tag:** [vv10]

- **Fact:** Các khóa SSH được lưu trữ mặc định trong thư mục ẩn `.ssh` tại thư mục home của người dùng.
- **Source:** (v10 - Section: Generating your key pair)
- **Tag:** [vv10]

- **Fact:** Thành phần máy chủ SSH chạy ngầm được gọi là "daemon" (sshd), có file cấu hình chính tại `/etc/ssh/sshd_config` trên hệ điều hành Linux.
- **Source:** (v10 - Section: Configuring an SSH server)
- **Tag:** [vv10]

- **Fact:** Tính năng Port Forwarding (chuyển tiếp cổng) trong SSH cho phép truy cập các dịch vụ bị chặn bởi tường lửa, nhưng thường bị tắt mặc định vì lý do bảo mật.
- **Source:** (v10 - Section: Pro Tips)
- **Tag:** [vv10]

- **Fact:** WSL2 (Windows Subsystem for Linux) hoạt động trên một mạng ảo riêng biệt (thường là dải `172.x.x.x`) so với mạng Wi-Fi vật lý của máy chủ Windows (thường là dải `192.168.x.x`).
- **Source:** (v10 - Assistant: Vì sao bạn thấy hai địa chỉ IP khác nhau?)
- **Tag:** [vv10]

- **Fact:** Lệnh `nmap -p 22 <IP>` được sử dụng để quét và kiểm tra trạng thái của cổng SSH trên một thiết bị trong mạng.
- **Source:** (v10 - Assistant: Kiểm tra nhanh)
- **Tag:** [vv10]

- **Fact:** Khi kết nối SSH lần đầu đến một máy chủ, SSH client sẽ hiển thị dấu vân tay (fingerprint) của máy chủ và yêu cầu người dùng xác nhận để lưu vào file `known_hosts`.
- **Source:** (v10 - Section: Connecting for the first time)
- **Tag:** [vv10]

- **Fact:** Trên Windows, dịch vụ OpenSSH Server có thể được cài đặt thông qua PowerShell bằng lệnh `Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0`.
- **Source:** (v10 - Assistant: Bước 1: Bật SSH Server trên Windows)
- **Tag:** [vv10]

- **Fact:** Kubernetes (MicroK8s) được ứng dụng để triển khai các cụm (cluster) an toàn và linh hoạt cho các thiết bị Edge và IoT.
- **Source:** (v10 - User: SSH login output - Ubuntu banner)
- **Tag:** [vv10]

- **Fact:** Giao diện `lo` (loopback interface) với địa chỉ `127.0.0.1` được sử dụng để thiết bị tự liên lạc với chính nó và không dùng để kết nối mạng bên ngoài.
- **Source:** (v10 - Assistant: Giao diện lo (loopback))
- **Tag:** [vv10]

- **Fact:** Trạng thái cổng "filtered" trong kết quả quét `nmap` cho thấy có tường lửa (firewall) đang chặn các gói tin truy cập vào cổng đó.
- **Source:** (v10 - Assistant: Cổng 22 (SSH) filtered)
- **Tag:** [vv10]