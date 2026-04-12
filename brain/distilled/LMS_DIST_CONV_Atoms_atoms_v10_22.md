---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_22
  title: atoms_v10_22
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn cung cấp về giao thức SSH và quản lý mã nguồn:

- **Fact:** Giao thức SSH (Secure Shell) cho phép truy cập an toàn vào máy tính thông qua một mạng không bảo mật bằng cách kết nối qua cổng 22.
- **Source:** (vv10 - Section: Configuring SSH)
- **Tag:** [vv10]

- **Fact:** SSH hoạt động dựa trên nguyên lý mã hóa khóa công khai (public-key encryption), sử dụng một cặp khóa gồm khóa công khai (public key) lưu trên server và khóa riêng tư (private key) lưu tại máy khách.
- **Source:** (vv10 - Section: The SSH protocol)
- **Tag:** [vv10]

- **Fact:** Lệnh để tạo cặp khóa RSA với độ dài 2048 bit là `ssh-keygen -t rsa -b 2048`.
- **Source:** (vv10 - Section: Generating your key pair)
- **Tag:** [vv10]

- **Fact:** Các khóa SSH được lưu trữ mặc định trong một thư mục ẩn tên là `.ssh` nằm trong thư mục gốc (home directory) của người dùng.
- **Source:** (vv10 - Section: Generating your key pair)
- **Tag:** [vv10]

- **Fact:** Khóa riêng tư (private key) đóng vai trò là phương thức xác thực và mã hóa, giúp người dùng không cần nhập mật khẩu khi kết nối với server.
- **Source:** (vv10 - Section: Using the SSH protocol)
- **Tag:** [vv10]

- **Fact:** SSH hỗ trợ truyền file an toàn thông qua giao thức SCP (Secure Copy Protocol) hoặc SFTP (Secure File Transfer Protocol).
- **Source:** (vv10 - Section: Using the SSH protocol)
- **Tag:** [vv10]

- **Fact:** SSH có tính năng chuyển tiếp cổng (port forwarding) hoặc "tunneling" để truy cập các dịch vụ mạng bị chặn bởi tường lửa.
- **Source:** (vv10 - Section: Using the SSH protocol)
- **Tag:** [vv10]

- **Fact:** Trên hệ điều hành Linux, tệp cấu hình của trình chủ SSH (SSH daemon) thường nằm tại đường dẫn `/etc/ssh/sshd_config`.
- **Source:** (vv10 - Section: Configuring an SSH server)
- **Tag:** [vv10]

- **Fact:** Khi kết nối lần đầu, SSH sẽ hiển thị dấu vân tay (fingerprint) của khóa máy chủ để người dùng xác nhận độ tin cậy trước khi lưu vào danh sách `known hosts`.
- **Source:** (vv10 - Section: Connecting for the first time)
- **Tag:** [vv10]

- **Fact:** Cảnh báo "Remote host identification has changed" xuất hiện khi khóa công khai của server thay đổi, đây có thể là dấu hiệu của một cuộc tấn công nghe lén (eavesdropping).
- **Source:** (vv10 - Section: Pro Tips)
- **Tag:** [vv10]

- **Fact:** Lệnh `git config --global credential.helper cache` được sử dụng để ghi nhớ thông tin đăng nhập GitHub tạm thời, giúp tránh việc phải nhập lại username/password nhiều lần.
- **Source:** (vv10 - Section: Basic interaction with GitHub)
- **Tag:** [vv10]

- **Fact:** Lệnh `git commit -a -m` cho phép thực hiện commit trực tiếp các thay đổi trên các tệp đã được theo dõi mà không cần chạy lệnh `git add` riêng biệt.
- **Source:** (vv10 - Section: Basic interaction with GitHub)
- **Tag:** [vv10]