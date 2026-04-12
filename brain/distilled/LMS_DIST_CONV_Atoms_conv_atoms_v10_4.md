---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v10_4
  title: CONV_atoms_v10_4
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v10) liên quan đến lập trình Python - nền tảng quan trọng trong phát triển IoT, Robotics và AI:

- **Fact:** [CONV] Sử dụng phương thức `.get()` khi truy xuất dữ liệu từ Dictionary trong Python giúp chương trình không bị crash (lỗi KeyError) nếu khóa (key) không tồn tại.
- **Source:** [Đoạn: Cách làm - lookup dictionary]
- **Tag:** [vv10]

- **Fact:** [CONV] Để kiểm soát dữ liệu khi lookup dictionary, có thể kiểm tra giá trị trả về từ `.get()`; nếu kết quả là `None`, nghĩa là key đó không tồn tại trong hệ thống.
- **Source:** [Đoạn: Cách làm - lookup dictionary]
- **Tag:** [vv10]

- **Fact:** [CONV] Để vận hành môi trường lập trình Linux (Ubuntu) ngay trong VSCode trên Windows, cần sử dụng tính năng `Remote-WSL: New Window` thông qua Command Palette (`Ctrl + Shift + P`).
- **Source:** [Đoạn: Hướng dẫn mở lại đúng Ubuntu WSL Terminal trong VSCode]
- **Tag:** [vv10]

- **Fact:** [CONV] Trong môi trường Ubuntu/WSL, lệnh `python3` được sử dụng để khởi động Python interactive shell hoặc thực thi các tệp tin mã nguồn `.py`.
- **Source:** [Đoạn: Chạy Python interactive shell]
- **Tag:** [vv10]

- **Fact:** [CONV] Một thực hành tốt (Best Practice) trong phát triển phần mềm là tách biệt file logic xử lý (ví dụ: `cake_factory.py`) và file kiểm thử (ví dụ: `test_cake_factory.py`).
- **Source:** [Đoạn: Cách tổ chức project đúng chuẩn]
- **Tag:** [vv10]

- **Fact:** [CONV] Thư viện `unittest` là công cụ tiêu chuẩn trong Python để viết Unit Test; các hàm kiểm thử bắt buộc phải bắt đầu bằng tiền tố `test_` để hệ thống tự động nhận diện.
- **Source:** [Đoạn: Lưu ý quan trọng về Unit Test]
- **Tag:** [vv10]

- **Fact:** [CONV] Kỹ thuật "Dictionary Mapping" (sử dụng từ điển để ánh xạ giá trị) là phương pháp tối ưu để thay thế các cấu trúc `if-else` rườm rà khi cần gán thuộc tính dựa trên điều kiện (như giá cả, chất liệu vải).
- **Source:** [Đoạn: Mẹo nhỏ để làm bài - Clothing Factory]
- **Tag:** [vv10]

- **Fact:** [CONV] Trong lập trình hướng đối tượng (OOP) Python, phương thức `__init__` đóng vai trò hàm khởi tạo, thiết lập các giá trị ban đầu cho đối tượng khi class được instanced.
- **Source:** [Đoạn: File code chính: cake_factory.py]
- **Tag:** [vv10]

- **Fact:** [CONV] Việc sử dụng Type Hinting (như `List[str]`) trong Python giúp định nghĩa rõ ràng kiểu dữ liệu trả về của hàm, hỗ trợ quá trình gỡ lỗi và phát triển hệ thống phức tạp.
- **Source:** [Đoạn: File code chính: pizza_factory.py]
- **Tag:** [vv10]

- **Fact:** [CONV] Các phương thức assert như `assertEqual`, `assertIn`, `assertNotIn` trong class `unittest.TestCase` được dùng để xác thực tính đúng đắn của dữ liệu trong quá trình kiểm thử.
- **Source:** [Đoạn: File test: test_cake_factory.py]
- **Tag:** [vv10]