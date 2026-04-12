---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_37
  title: atoms_v10_37
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp (Volume v10) liên quan đến lập trình Python, môi trường phát triển và quy trình kiểm thử - những nền tảng quan trọng trong Robotics và AI:

- **Fact:** Để thực thi một file script Python trực tiếp từ terminal thay vì sử dụng shell tương tác, người dùng sử dụng lệnh `python3 tên_file.py`.
- **Source:** [vv10 - Section: uốn chạy file .py thay vì shell]
- **Tag:** [vv10]

- **Fact:** Lệnh `python3 --version` được sử dụng để kiểm tra sự hiện diện và xác định phiên bản Python đang được cài đặt trong môi trường hệ thống.
- **Source:** [vv10 - Section: Tổng kết nhanh]
- **Tag:** [vv10]

- **Fact:** Trong môi trường Windows, để làm việc với các lệnh hệ thống Linux (như `os`, `bash`, đường dẫn Linux) trong các khóa học tự động hóa, cần sử dụng terminal Ubuntu WSL thay vì PowerShell hay CMD.
- **Source:** [vv10 - Section: Vì sao chưa đúng?]
- **Tag:** [vv10]

- **Fact:** Để mở môi trường Ubuntu WSL trong VSCode, người dùng sử dụng Command Palette (`Ctrl + Shift + P`) và chọn lệnh `Remote-WSL: New Window`.
- **Source:** [vv10 - Section: Bước 1: Mở Command Palette]
- **Tag:** [vv10]

- **Fact:** Một cấu trúc dự án phần mềm chuyên nghiệp yêu cầu tách biệt mã nguồn logic (ví dụ: `cake_factory.py`) và mã nguồn kiểm thử (ví dụ: `test_cake_factory.py`) vào các file riêng biệt.
- **Source:** [vv10 - Section: Tổ chức project đúng chuẩn]
- **Tag:** [vv10]

- **Fact:** Framework `unittest` của Python yêu cầu các file kiểm thử và các hàm kiểm thử bên trong phải bắt đầu bằng tiền tố `test_` để có thể tự động nhận diện và thực thi.
- **Source:** [vv10 - Section: Lưu ý quan trọng]
- **Tag:** [vv10]

- **Fact:** Phương thức `unittest.main()` được sử dụng trong file test để kích hoạt trình tự động tìm kiếm và chạy tất cả các test cases thuộc lớp kế thừa từ `unittest.TestCase`.
- **Source:** [vv10 - Section: Lưu ý quan trọng]
- **Tag:** [vv10]

- **Fact:** Các phương thức kiểm thử phổ biến trong `unittest` bao gồm `assertEqual` (kiểm tra giá trị bằng nhau), `assertIn` (kiểm tra sự tồn tại trong danh sách) và `assertNotIn`.
- **Source:** [vv10 - Section: Ví dụ cụ thể / test_cake_factory.py]
- **Tag:** [vv10]

- **Fact:** Kỹ thuật Dictionary Mapping trong Python giúp tối ưu hóa mã nguồn, thay thế các cấu trúc if-else phức tạp khi cần gán giá trị dựa trên các điều kiện đầu vào như loại sản phẩm hoặc kích cỡ.
- **Source:** [vv10 - Section: Mẹo nhỏ để làm bài]
- **Tag:** [vv10]

- **Fact