---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_48
  title: atoms_v10_48
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dựa trên dữ liệu RAW được cung cấp (Volume v10), dưới đây là các sự kiện (Facts) được trích xuất về kỹ thuật lập trình Bash và quản trị hệ thống Linux:

- **Fact:** Lệnh `grep " jane " ~/data/list.txt` được sử dụng để lọc chính xác các dòng chứa từ khóa "jane" (có khoảng trắng bao quanh) để tránh nhầm lẫn với các tên tương tự như "janez".
- **Source:** (v10 - Đoạn hội thoại USER/ASSISTANT về Bước 1 & Bước 3)
- **Tag:** [vv10]

- **Fact:** Lệnh `cut -d ' ' -f 3` hoặc `awk '{print $3}'` được dùng để trích xuất cột thứ 3 trong file dữ liệu, thường là nơi chứa đường dẫn file.
- **Source:** (v10 - Giải thích của ASSISTANT về Bước 3 và cách lấy tên file)
- **Tag:** [vv10]

- **Fact:** Lệnh `test -e <đường_dẫn>` (hoặc cú pháp `[ -e <đường_dẫn> ]`) được sử dụng trong script để kiểm tra sự tồn tại của một file hoặc thư mục trên hệ thống.
- **Source:** (v10 - Bước 4: Duyệt qua từng file và kiểm tra)
- **Tag:** [vv10]

- **Fact:** Trong môi trường lab cụ thể này, thư mục `/data/` ở gốc (root) chỉ chứa các file SSH (`id_ed25519`, `known_hosts`), trong khi các file dữ liệu thực tế nằm ở `~/data/` (thư mục home).
- **Source:** (v10 - Kết quả lệnh `ls -l /data/` và `ls ~/data/` của USER)
- **Tag:** [vv10]

- **Fact:** Việc ghi đè nội dung file trong Bash sử dụng ký hiệu `>` (ví dụ: `> oldFiles.txt`), trong khi việc ghi thêm vào cuối file sử dụng ký hiệu `>>`.
- **Source:** (v10 - Giải thích nội dung file `findJane.sh`)
- **Tag:** [vv10]

- **Fact:** Lệnh `chmod +x findJane.sh` là bắt buộc để cấp quyền thực thi cho một file script trước khi chạy bằng lệnh `./findJane.sh`.
- **Source:** (v10 - Bước 3: Tạo script findJane.sh)
- **Tag:** [vv10]

- **Fact:** Biến trong Bash được gán bằng cú pháp `files=$(...)` và được gọi lại bằng ký hiệu `$` (ví dụ: `$files`).
- **Source:** (v10 - Bước 2: Gán kết quả vào biến files)
- **Tag:** [vv10]

- **Fact:** Lệnh `sed 's|^/data/||'` được sử dụng để cắt bỏ chuỗi tiền tố `/data/` ở đầu mỗi dòng dữ liệu nhằm xử lý lại đường dẫn file.
- **Source:** (v10 - Giải pháp sửa lỗi đường dẫn của ASSISTANT)
- **Tag:** [vv10]

- **Fact:** Cấu trúc vòng lặp `for file in $files; do ... done` cho phép thực hiện một chuỗi lệnh lặp lại trên danh sách các phần tử được phân tách bằng khoảng trắng.
- **Source:** (v10 - Bước 4: Duyệt qua từng file)
- **Tag:** [vv10]

- **Fact:** Lỗi "doesn't exist" khi chạy script thường do sự sai lệch giữa đường dẫn được liệt kê trong file text (`list.txt`) và vị trí thực tế của file trên ổ đĩa.
- **Source:** [Unverified_Source] (Dựa trên phân tích logic lỗi của USER trong dữ liệu RAW).