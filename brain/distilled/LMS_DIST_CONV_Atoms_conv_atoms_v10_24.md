---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v10_24
  title: CONV_atoms_v10_24
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v10):

- **Fact:** [CONV] SSH (Secure Shell) sử dụng cổng 22 để thiết lập kết nối giữa client và server.
- **Source:** [Dữ liệu RAW - Section: Configuring SSH]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `ssh-keygen -t rsa -b 2048` được sử dụng để tạo cặp khóa public/private key nhằm xác thực bảo mật.
- **Source:** [Dữ liệu RAW - Section: Generating your key pair]
- **Tag:** [vv10]

- **Fact:** [CONV] Trên hệ điều hành Linux, file cấu hình của SSH daemon (sshd) thường được lưu trữ tại đường dẫn `/etc/ssh/sshd_config`.
- **Source:** [Dữ liệu RAW - Section: Configuring an SSH server]
- **Tag:** [vv10]

- **Fact:** [CONV] MicroK8s là giải pháp Kubernetes được sử dụng để triển khai các cụm (cluster) linh hoạt và bảo mật cho các thiết bị Edge và IoT.
- **Source:** [Dữ liệu RAW - User SSH login output banner]
- **Tag:** [vv10]

- **Fact:** [CONV] WSL2 (Windows Subsystem for Linux) sử dụng một card mạng ảo (virtual network adapter) với dải IP riêng (thường là 172.x.x.x), tách biệt với IP vật lý của máy host Windows.
- **Source:** [Dữ liệu RAW - Assistant response: 1. Vì sao bạn thấy hai địa chỉ IP khác nhau?]
- **Tag:** [vv10]

- **Fact:** [CONV] Để thiết lập đăng nhập SSH không cần mật khẩu, nội dung khóa công khai (public key) của client phải được thêm vào file `~/.ssh/authorized_keys` trên máy chủ.
- **Source:** [Dữ liệu RAW - Assistant response: Bonus: Thêm public key từ WSL vào Windows]
- **Tag:** [vv10]

- **Fact:** [CONV] Trạng thái "filtered" khi quét cổng bằng `nmap` cho thấy cổng đó đang bị chặn bởi tường lửa (firewall) hoặc các thiết bị lọc gói tin.
- **Source:** [Dữ liệu RAW - Assistant response: Kết quả nmap của bạn cho thấy rằng]
- **Tag:** [vv10]

- **Fact:** [CONV] Dấu vân tay (fingerprint) của các máy chủ đã từng kết nối thành công được lưu trữ tại file `~/.ssh/known_hosts` để đối chiếu cho các lần kết nối sau.
- **Source:** [Dữ liệu RAW - Assistant response: Sau khi bạn gõ yes]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `nmap -sn [dải_mạng]` được sử dụng để thực hiện quét ping (ping scan) nhằm xác định các thiết bị đang trực tuyến trong mạng.
- **Source:** [Dữ liệu RAW - Bảng lệnh đầu tiên]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `arp -a` cho phép người dùng xem bảng ARP để đối chiếu giữa địa chỉ IP và địa chỉ vật lý (MAC) của các thiết bị trong cùng mạng cục bộ.
- **Source:** [Dữ liệu RAW - Bảng lệnh đầu tiên]
- **Tag:** [vv10]

- **Fact:** [CONV] Card mạng Killer(R) Wi-Fi 6 AX1650i hỗ trợ chuẩn Wi-Fi 6 (802.11ax) và có khả năng hoạt động ở băng tần 160MHz.
- **Source:** [Dữ liệu RAW - Thông tin Wi-Fi setting của User]
- **Tag:** [vv10]