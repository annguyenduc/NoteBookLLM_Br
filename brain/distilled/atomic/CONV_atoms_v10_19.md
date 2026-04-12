Dưới đây là các sự kiện (Facts) kỹ thuật về quy trình làm việc với Git và lập trình Python được trích xuất từ dữ liệu cung cấp:

- Fact: [CONV] Lệnh `git status` được sử dụng để kiểm tra trạng thái của kho lưu trữ, giúp xác định tệp nào mới (untracked), tệp nào đã sửa đổi (modified) hoặc đã sẵn sàng để commit (staged).
- Source: [v10 - Section: Review: Tracking Files]
- Tag: [vv10]

- Fact: [CONV] Quy trình lưu trữ thay đổi trong Git gồm hai bước: sử dụng `git add <file>` để đưa thay đổi vào khu vực staging và `git commit -m "Message"` để lưu vĩnh viễn vào lịch sử.
- Source: [v10 - Section: Review: Tracking Files]
- Tag: [vv10]

- Fact: [CONV] Lệnh `git log --oneline` hiển thị lịch sử commit dưới dạng tóm tắt một dòng cho mỗi commit, bao gồm mã commit ID ngắn gọn và thông điệp commit.
- Source: [v10 - Section: 2. Xem lịch sử tóm tắt cho dễ nhìn]
- Tag: [vv10]

- Fact: [CONV] Lệnh `git show <commit-id>` cho phép xem chi tiết các thay đổi trong một commit cụ thể, trong đó dòng bắt đầu bằng dấu cộng (+) là nội dung mới và dấu trừ (-) là nội dung cũ bị xóa.
- Source: [v10 - Section: 3. Xem chi tiết 1 commit cụ thể]
- Tag: [vv10]

- Fact: [CONV] Để so sánh sự khác biệt giữa hai commit bất kỳ, ta sử dụng cú pháp lệnh `git diff <commit-id1> <commit-id2>`.
- Source: [v10 - Section: 4. So sánh giữa 2 commit]
- Tag: [vv10]

- Fact: [CONV] Lệnh `git init` dùng để khởi tạo một kho lưu trữ Git mới, tạo ra một thư mục ẩn `.git` để quản lý dữ liệu phiên bản.
- Source: [v10 - Section: Review: The Basic Git Workflow]
- Tag: [vv10]

- Fact: [CONV] Cấu trúc một commit message chuẩn bao gồm: một dòng tóm tắt ngắn gọn (khoảng 50 ký tự), một dòng trống, và phần thân (body) mô tả chi tiết lý do thay đổi (mỗi dòng không quá 72 ký tự).
- Source: [v10 - Section: Review: Anatomy of a commit message]
- Tag: [vv10]

- Fact: [CONV] Trong Python, module `os` cung cấp hàm `os.path.exists()` để kiểm tra sự tồn tại của một đường dẫn tệp tin, ví dụ như kiểm tra tệp `/run/reboot-required` để xác định hệ thống có cần khởi động lại hay không.
- Source: [v10 - Section: Review: The Basic Git Workflow]
- Tag: [vv10]

- Fact: [CONV] Lệnh `git config -l` được sử dụng để liệt kê toàn bộ các thiết lập cấu hình hiện tại của Git, bao gồm thông tin người dùng như `user.email` và `user.name`.
- Source: [v10 - Section: Review: The Basic Git Workflow]
- Tag: [vv10]

- Fact: [CONV] Khi thực hiện lệnh `git commit` mà không có tham số `-m`, Git sẽ mở trình soạn thảo văn bản mặc định (như nano) để người dùng nhập thông điệp commit nhiều dòng.
- Source: [v10 - Section: ✍️ BƯỚC 3: Thực hiện commit với thông điệp đầy đủ]
- Tag: [vv10]

- Fact: [CONV] Lệnh `chmod +x <file_name>` được sử dụng trong terminal để cấp quyền thực thi cho một tệp script Python.
- Source: [v10 - Section: Review: The Basic Git Workflow]
- Tag: [vv10]

- Fact: [CONV] Trạng thái "working tree clean" thông báo rằng không có thay đổi nào chưa được commit trong thư mục làm việc hiện tại.
- Source: [v10 - Section: Review: Tracking Files]
- Tag: [vv10]

- Fact: [CONV] Việc dán trực tiếp mã nguồn Python vào terminal Bash sẽ gây ra lỗi lệnh không tìm thấy (command not found) hoặc lỗi cú pháp vì Bash không thể biên dịch trực tiếp Python.
- Source: [v10 - Section: USER: def check_reboot(): ...]
- Tag: [vv10]

- Fact: [CON