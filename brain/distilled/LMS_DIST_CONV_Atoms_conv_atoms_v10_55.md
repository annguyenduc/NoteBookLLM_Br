---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v10_55
  title: CONV_atoms_v10_55
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp:

- **Fact:** [CONV] Trong Python, `subprocess.run()` với tham số `capture_output=True` dùng để thu thập đầu ra (stdout và stderr), và `text=True` để đảm bảo kết quả trả về dạng chuỗi (string) thay vì bytes.
- **Source:** [v10 - Section: Giải thích từng phần / subprocess.run]
- **Tag:** [vv10]

- **Fact:** [CONV] Các lệnh thực thi qua `subprocess.run()` được chạy tuần tự; Python sẽ chờ lệnh trước đó hoàn thành (ví dụ: `sleep 2`) mới tiếp tục chạy lệnh tiếp theo.
- **Source:** [v10 - Section: Thực thi liên tiếp]
- **Tag:** [vv10]

- **Fact:** [CONV] Thuộc tính `returncode` của đối tượng `CompletedProcess` trả về mã trạng thái của lệnh: giá trị `0` thường là thành công, và giá trị khác `0` (như `2` đối với lệnh `ls`) chỉ thị lỗi.
- **Source:** [v10 - Section: Giải thích từng lệnh / returncode]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `host` là công cụ hệ thống (phổ biến trên Linux/Unix) dùng để tra cứu DNS, địa chỉ IP và tên miền; trên Ubuntu, nó nằm trong gói `dnsutils`.
- **Source:** [v10 - Section: Giải thích các dòng mã / Cách khắc phục FileNotFoundError: host]
- **Tag:** [vv10]

- **Fact:** [CONV] Hàm `os.rename(src, dest)` trong Python sẽ gây lỗi `FileNotFoundError` nếu tệp nguồn không tồn tại hoặc thư mục đích chưa được tạo.
- **Source:** [v10 - Section: Conversation: FileNotFoundError Solution]
- **Tag:** [vv10]

- **Fact:** [CONV] `os.makedirs(path, exist_ok=True)` được sử dụng để tạo thư mục đích (bao gồm cả các thư mục trung gian) và tránh gây lỗi nếu thư mục đã tồn tại.
- **Source:** [v10 - Section: Cách làm / Tạo thư mục test1]
- **Tag:** [vv10]

- **Fact:** [CONV] Hàm `os.rmdir()` chỉ có thể xóa một thư mục nếu nó hoàn toàn rỗng; để xóa thư mục chứa tệp hoặc thư mục con, phải sử dụng `shutil.rmtree()`.
- **Source:** [v10 - Section: os.rmdir là gì]
- **Tag:** [vv10]

- **Fact:** [CONV] Phương thức `.index()` tìm vị trí (chỉ số) đầu tiên của một giá trị trong chuỗi hoặc danh sách; nếu không tìm thấy giá trị, Python sẽ ném ra lỗi `ValueError`.
- **Source:** [v10 - Section: .index () là gì]
- **Tag:** [vv10]

- **Fact:** [CONV] Lỗi `cat: No such file or directory` xuất hiện khi lệnh `cat` không tìm thấy tệp trong thư mục làm việc hiện tại, có thể do sai tên tệp, sai đường dẫn hoặc tệp chưa được tạo.
- **Source:** [v10 - Section: cat variables.py: No such file or directory]
- **Tag:** [vv10]

- **Fact:** [CONV] Trên môi trường WSL (Windows Subsystem for Linux), nếu quên mật khẩu `sudo`, người dùng có thể chuyển sang tài khoản root bằng lệnh `wsl -u root` để đặt lại mật khẩu cho người dùng thường.
- **Source:** [v10 - Section: Cách khắc phục / Thử thay đổi mật khẩu với root]
- **Tag:** [vv10]