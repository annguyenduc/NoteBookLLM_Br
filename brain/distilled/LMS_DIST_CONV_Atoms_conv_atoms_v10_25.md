---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v10_25
  title: CONV_atoms_v10_25
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ tài liệu hướng dẫn về Git và quy trình làm việc (Workflow) trong phát triển phần mềm (nền tảng cho các dự án AI, Robotics và IoT):

- **Fact:** [CONV] Thiết lập danh tính người dùng trong Git bằng lệnh `git config --global user.name "Name"` và `git config --global user.email "user@example.com"` để định danh các commit.
- **Source:** Section: Configure Git.
- **Tag:** [vv10]

- **Fact:** [CONV] GitHub yêu cầu sử dụng Personal Access Token (PAT) thay cho mật khẩu truyền thống để xác thực các thao tác clone và push qua giao thức HTTPS.
- **Source:** Section: Generating a Personal Access Token.
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `git status` được sử dụng để kiểm tra trạng thái của các tệp, phân biệt giữa tệp đã chỉnh sửa (modified), tệp đã đưa vào vùng chờ (staged) và tệp chưa được theo dõi.
- **Source:** Section: Edit the file and add it to the repository.
- **Tag:** [vv10]

- **Fact:** [CONV] `git add` là thao tác chuyển nội dung từ thư mục làm việc (working directory) vào khu vực staging để chuẩn bị cho lần commit kế tiếp.
- **Source:** Section: Edit the file and add it to the repository.
- **Tag:** [vv10]

- **Fact:** [CONV] Một Git commit đóng vai trò như một bản lưu (snapshot) ghi lại trạng thái hiện tại của các thay đổi đã được staging kèm theo thông điệp mô tả.
- **Source:** Section: Edit the file and add it to the repository.
- **Tag:** [vv10]

- **Fact:** [CONV] Quy trình `Pull-Merge-Push` được sử dụng để giải quyết xung đột (conflict) khi có nhiều người cùng thay đổi trên một tệp ở kho lưu trữ từ xa (remote repository).
- **Source:** Section: Review: The Pull-Merge-Push Workflow.
- **Tag:** [vv10]

- **Fact:** [CONV] Khi xảy ra xung đột (conflict), Git sẽ đánh dấu các phần khác biệt trong tệp bằng các ký hiệu `<<<<<<<`, `=======`, và `>>>>>>>` để người dùng xử lý thủ công.
- **Source:** Section: Review: The Pull-Merge-Push Workflow - Step: git pull.
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `git log --graph --oneline` cung cấp cái nhìn trực quan về lịch sử các nhánh và các lần merge trong dự án.
- **Source:** Section: Review: The Pull-Merge-Push Workflow - Code output.
- **Tag:** [vv10]

- **Fact:** [CONV] Git là công cụ quản lý phiên bản mã nguồn nền tảng, cho phép các kỹ sư AI và Robotics theo dõi lịch sử thay đổi thuật toán và mã điều khiển phần cứng.
- **Source:** [Nội dung tổng quát về Git trong lập trình Python].
- **Tag:** [Unverified_Source]