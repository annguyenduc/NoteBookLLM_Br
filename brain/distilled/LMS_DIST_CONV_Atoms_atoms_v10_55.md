---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_55
  title: atoms_v10_55
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v10), tập trung vào lập trình Python và điều khiển hệ thống - những nền tảng quan trọng trong Robotics và AI:

- **Fact:** Trong Python, khi sử dụng `subprocess.run()`, tham số `capture_output=True` dùng để thu thập đầu ra (stdout và stderr), và `text=True` đảm bảo kết quả trả về dưới dạng chuỗi (string) thay vì bytes.
- **Source:** (vv10 - Section: subprocess.run parameters)
- **Tag:** [vv10]

- **Fact:** Các lệnh thực thi qua `subprocess.run()` trong Python được chạy tuần tự; chương trình sẽ chờ lệnh trước đó hoàn thành (kết thúc quá trình) mới tiếp tục chạy lệnh tiếp theo.
- **Source:** (vv10 - Section: Thực thi liên tiếp)
- **Tag:** [vv10]

- **Fact:** Thuộc tính `returncode` của đối tượng `CompletedProcess` (trả về từ `subprocess.run`) cho biết trạng thái kết thúc của lệnh: giá trị `0` thường là thành công, và giá trị khác `0` (ví dụ: `2`) biểu thị lỗi.
- **Source:** (vv10 - Section: Giải thích từng lệnh / Kết quả)
- **Tag:** [vv10]

- **Fact:** Lệnh `host` (tra cứu DNS) trên hệ thống Linux/Ubuntu nằm trong gói `dnsutils`. Nếu gặp lỗi `FileNotFoundError` khi gọi lệnh này từ Python, cần cài đặt bằng lệnh `sudo apt install dnsutils`.
- **Source:** (vv10 - Section: Cách khắc phục FileNotFoundError)
- **Tag:** [vv10]

- **Fact:** Hàm `os.rename(src, dest)` trong Python sẽ gây lỗi `FileNotFoundError` nếu file nguồn không tồn tại hoặc thư mục đích chưa được tạo trước đó.
- **Source:** (vv10 - Section: FileNotFoundError Solution)
- **Tag:** [vv10]

- **Fact:** Để tạo một thư mục mới và đảm bảo không gây lỗi nếu thư mục đã tồn tại, sử dụng `os.makedirs(path, exist_ok=True)`.
- **Source:** (vv10 - Section: Ensure the destination folder exists)
- **Tag:** [vv10]

- **Fact:** Hàm `os.rmdir()` chỉ có thể xóa các thư mục rỗng. Để xóa một thư mục bao gồm cả tệp tin và thư mục con bên trong, cần sử dụng hàm `shutil.rmtree()`.
- **Source:** (vv10 - Section: os.rmdir là gì)
- **Tag:** [vv10]

- **Fact:** Phương thức `.index()` trong Python trả về vị trí (chỉ số) đầu tiên của một giá trị trong chuỗi hoặc danh sách; nếu không tìm thấy giá trị, nó sẽ gây ra lỗi `ValueError`.
- **Source:** (vv10 - Section: .index () là gì)
- **Tag:** [vv10]

- **Fact:** Lỗi "cat: variables.py: No such file or directory" trên terminal xuất hiện khi lệnh `cat` không tìm thấy tệp tin được chỉ định trong thư mục làm việc hiện tại.
- **Source:** (vv10 - Section: cat variables.py)
- **Tag:** [vv10]