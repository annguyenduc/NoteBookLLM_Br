---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_19
  title: atoms_v10_19
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu RAW (Volume v10) về quy trình làm việc với Git và lập trình Python cơ bản:

- Fact: Quy trình cơ bản để lưu thay đổi vào Git gồm: `git add <file>` để đưa vào khu vực staging và `git commit -m "Thông điệp"` để lưu vào lịch sử.
- Source: [v10 - Section: Review: Tracking Files]
- Tag: [vv10]

- Fact: Lệnh `git status` được sử dụng để theo dõi trạng thái của file, giúp xác định file nào mới (untracked), file nào đã sửa (modified) hoặc đã sẵn sàng để commit.
- Source: [v10 - Section: Review: Tracking Files]
- Tag: [vv10]

- Fact: Lệnh `git log` dùng để xem lịch sử các lần commit; phiên bản `git log --oneline` giúp xem danh sách tóm tắt trên một dòng.
- Source: [v10 - Section: Các cách xem thay đổi giữa các lần git commit]
- Tag: [vv10]

- Fact: Lệnh `git show <commit-id>` hiển thị chi tiết nội dung thay đổi trong một commit cụ thể, bao gồm các dòng bị xóa (đánh dấu `-`) và các dòng được thêm mới (đánh dấu `+`).
- Source: [v10 - Section: Các cách xem thay đổi giữa các lần git commit]
- Tag: [vv10]

- Fact: Lệnh `git diff` dùng để so sánh sự khác biệt giữa các thay đổi chưa commit với lần commit gần nhất, hoặc giữa hai commit bất kỳ bằng cú pháp `git diff <commit-id1> <commit-id2>`.
- Source: [v10 - Section: Các cách xem thay đổi giữa các lần git commit]
- Tag: [vv10]

- Fact: Lệnh `git init` khởi tạo một kho lưu trữ Git mới (empty Git repository) trong thư mục hiện hành.
- Source: [v10 - Section: Review: The Basic Git Workflow]
- Tag: [vv10]

- Fact: Lệnh `git config -l` liệt kê các cấu hình hiện tại của Git như `user.email` và `user.name`.
- Source: [v10 - Section: Review: The Basic Git Workflow]
- Tag: [vv10]

- Fact: Một commit message chuẩn mực bao gồm: dòng tiêu đề ngắn gọn (~50 ký tự), một dòng trống, và phần thân mô tả chi tiết (giữ mỗi dòng dưới 72 ký tự).
- Source: [v10 - Section: Review: Anatomy of a commit message]
- Tag: [vv10]

- Fact: Trong Python, thư viện `shutil` có thể dùng để kiểm tra dung lượng đĩa thông qua hàm `shutil.disk_usage(path)`.
- Source: [v10 - Section: Hướng dẫn chi tiết nếu bạn chưa có sẵn file: 1. Tạo file disk_usage.py]
- Tag: [vv10]

- Fact: Để kiểm tra sự tồn tại của một file hệ thống (như `/run/reboot-required` để xác định máy tính có cần khởi động lại hay không), Python sử dụng hàm `os.path.exists()`.
- Source: [v10 - Section: Review: The Basic Git Workflow - File with code]
- Tag: [vv10]

- Fact: Lệnh `chmod +x <file_name>` được sử dụng trong terminal để cấp quyền thực thi cho các file script Python.
- Source: [v10 - Section: Review: The Basic Git Workflow]
- Tag: [vv10]

- Fact: Khi khởi tạo repo, Git gợi ý có thể đổi tên nhánh mặc định (thường là `master`) sang tên khác như `main` bằng lệnh `git branch -m <name>`.
- Source: [v10 - User input: git init output]
- Tag: [vv10]

- Fact: Lệnh `git restore --staged <file>` hoặc `git reset HEAD <file>` được sử dụng để đưa một file ra khỏi khu vực staging (unstage).
- Source: [v10 - Section: Review: Tracking Files / The Basic Git Workflow]
- Tag: [vv10]

- Fact: Việc dán trực tiếp mã nguồn Python vào terminal Bash sẽ gây ra lỗi cú pháp (`syntax error`) vì Bash không thể biên dịch trực tiếp các từ khóa Python như `def` hay `import`.
- Source: [v10 - User input: Command 'import' not found / Assistant response]
- Tag: [vv10]