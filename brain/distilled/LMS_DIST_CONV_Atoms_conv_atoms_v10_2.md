---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v10_2
  title: CONV_atoms_v10_2
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v10:

- **Fact:** [CONV] Simple Test là phương pháp sử dụng các câu lệnh `if` để so sánh giá trị thực tế của hàm với kết quả mong đợi nhằm phát hiện lỗi sớm và tiết kiệm thời gian kiểm thử thủ công.
- **Source:** [v10 - Section: 2. Tạo các kiểm tra đơn giản & 3. Lý do dùng Simple Test]
- **Tag:** [vv10]

- **Fact:** [CONV] Unit Test là phương pháp kiểm tra tự động các đơn vị mã nguồn nhỏ, sử dụng module `unittest` có sẵn trong Python để đảm bảo logic hàm chạy đúng trong nhiều trường hợp.
- **Source:** [v10 - Section: 1. Unit Test là gì? & 2. Dùng module unittest trong Python]
- **Tag:** [vv10]

- **Fact:** [CONV] Khi viết Unit Test với module `unittest`, các hàm kiểm tra bắt buộc phải bắt đầu bằng tiền tố `test_` và nằm trong một class kế thừa từ `unittest.TestCase`.
- **Source:** [v10 - Section: 3. Cách viết một Unit Test & 🎯 Những lưu ý quan trọng]
- **Tag:** [vv10]

- **Fact:** [CONV] Cấu trúc `try/except` được sử dụng để xử lý các ngoại lệ (Exceptions) như `ZeroDivisionError` (chia cho 0) hoặc `ValueError` (ép kiểu sai), giúp chương trình không bị crash khi gặp lỗi vận hành.
- **Source:** [v10 - Section: 2. Dùng try/except để xử lý lỗi & 📌 Một số lỗi thường gặp]
- **Tag:** [vv10]

- **Fact:** [CONV] Trong cấu trúc xử lý lỗi, khối `else` sẽ thực thi nếu không có lỗi xảy ra trong `try`, và khối `finally` sẽ luôn luôn thực thi bất kể có lỗi hay không (thường dùng để giải phóng tài nguyên).
- **Source:** [v10 - Section: 4. Dùng else và finally]
- **Tag:** [vv10]

- **Fact:** [CONV] Class trong Python là một khuôn mẫu (template) để tạo ra đối tượng (object), cho phép gom nhóm dữ liệu (thuộc tính) và hành động (phương thức) vào một thực thể duy nhất.
- **Source:** [v10 - Section: 🧠 Class trong Python là gì? & 📚 Tại sao cần dùng Class?]
- **Tag:** [vv10]

- **Fact:** [CONV] Hàm `__init__` (constructor) trong class Python là hàm khởi tạo tự động chạy khi một đối tượng được tạo ra, sử dụng tham số `self` để đại diện cho chính đối tượng đó và quản lý dữ liệu riêng biệt.
- **Source:** [v10 - Section: 1. Cấu trúc một class Python cơ bản & 🧠 Giải thích dễ hiểu]
- **Tag:** [vv10]

- **Fact:** [CONV] Thuật toán kiểm tra chuỗi đối xứng (Palindrome) trong Python có thể thực hiện bằng cách chuyển chuỗi về chữ thường, xóa khoảng trắng và so sánh với chuỗi đảo ngược bằng kỹ thuật slicing `[::-1]`.
- **Source:** [v10 - Section: 🎯 Gợi ý để làm (is_palindrome)]
- **Tag:** [vv10]

- **Fact:** [CONV] Việc áp dụng Unit Test và xử lý lỗi (Error Handling) là nền tảng quan trọng để phát triển các hệ thống điều khiển Robot và thiết bị IoT ổn định, tránh các hành vi không xác định của phần cứng.
- **Source:** [Phân tích ứng dụng lập trình trong Robotics/IoT]
- **Tag:** [Unverified_Source]

- **Fact:** [CONV] Python là ngôn ngữ lập trình cốt lõi thường được sử dụng để tương tác với hệ điều hành và lập trình các bo mạch vi điều khiển hỗ trợ MicroPython như YoloBit.
- **Source:** [Bối cảnh khóa học Google IT Automation with Python]
- **Tag:** [Unverified_Source]