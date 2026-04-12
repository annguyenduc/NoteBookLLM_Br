Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v10) về lập trình Python, nền tảng quan trọng cho IoT, Robotics và AI:

- **Fact:** Simple Test là phương pháp sử dụng câu lệnh `if` để so sánh kết quả thực tế của hàm với giá trị kỳ vọng nhằm phát hiện lỗi sớm và tiết kiệm thời gian kiểm thử thủ công.
- **Source:** [v10 - Section: 3. Lý do dùng Simple Test]
- **Tag:** [vv10]

- **Fact:** Unit Test là phương pháp kiểm tra tự động các đơn vị mã nguồn nhỏ (hàm) thông qua module `unittest` tích hợp sẵn trong Python.
- **Source:** [v10 - Section: 1. Unit Test là gì? / 2. Dùng module unittest trong Python]
- **Tag:** [vv10]

- **Fact:** Để `unittest` tự động nhận diện và thực thi, tên các hàm kiểm tra bên trong class test bắt buộc phải bắt đầu bằng tiền tố `test_`.
- **Source:** [v10 - Section: 🎯 Những lưu ý quan trọng (Unit Test)]
- **Tag:** [vv10]

- **Fact:** Class test trong Python phải kế thừa từ `unittest.TestCase` để sử dụng các phương thức kiểm tra như `assertEqual`, `assertTrue`, hoặc `assertFalse`.
- **Source:** [v10 - Section: 3. Cách viết một Unit Test / 4. Các phương thức kiểm tra phổ biến]
- **Tag:** [vv10]

- **Fact:** Cấu trúc `try/except` được sử dụng để xử lý ngoại lệ (Exceptions), ngăn chương trình bị dừng đột ngột (crash) khi gặp các lỗi như chia cho 0 (`ZeroDivisionError`) hoặc ép kiểu sai (`ValueError`).
- **Source:** [v10 - Section: 🛠️ Tóm tắt nhanh phần Handling Errors]
- **Tag:** [vv10]

- **Fact:** Trong xử lý lỗi, khối `else` sẽ thực thi nếu không có lỗi xảy ra trong `try`, và khối `finally` sẽ luôn luôn thực thi bất kể có lỗi hay không.
- **Source:** [v10 - Section: 4. Dùng else và finally]
- **Tag:** [vv10]

- **Fact:** Class trong Python đóng vai trò là một khuôn mẫu (template/blueprint) để tạo ra các đối tượng (objects), giúp gom nhóm dữ liệu (thuộc tính) và hành động (phương thức) lại với nhau.
- **Source:** [v10 - Section: 🧠 Class trong Python là gì?]
- **Tag:** [vv10]

- **Fact:** Phương thức `__init__` là hàm khởi tạo đặc biệt, tự động chạy khi một đối tượng được tạo ra để thiết lập các thuộc tính ban đầu cho đối tượng đó.
- **Source:** [v10 - Section: 📚 1. Cấu trúc một class Python cơ bản]
- **Tag:** [vv10]

- **Fact:** Từ khóa `self` đại diện cho chính đối tượng đang được thao tác, cho phép truy cập và quản lý dữ liệu riêng biệt của từng đối tượng trong cùng một class.
- **Source:** [v10 - Section: 🧠 Giải thích dễ hiểu (Class)]
- **Tag:** [vv10]

- **Fact:** Kỹ thuật slicing `[::-1]` trong Python thường được sử dụng để đảo ngược chuỗi, ứng dụng trong các thuật toán kiểm tra chuỗi đối xứng (Palindrome).
- **Source:** [v10 - Section: 🎯 Gợi ý để làm (Bài tập Unit Test nâng cao)]
- **Tag:** [vv10]

- **Fact:** Lệnh `unittest.main()` được sử dụng để kích hoạt trình chạy kiểm thử tự động, quét toàn bộ file để tìm và thực thi các class kế thừa từ `unittest.TestCase`.
- **Source:** [v10 - Section: 🎯 Những lưu ý quan trọng (Unit Test)]
- **Tag:** [vv10]