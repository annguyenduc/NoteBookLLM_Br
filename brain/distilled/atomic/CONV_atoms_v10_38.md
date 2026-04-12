Chào bạn, tôi là @scout. Dựa trên dữ liệu từ **Volume v10 (Study guide: Unit tests)**, tôi xin trích xuất các sự kiện kỹ thuật phục vụ cho việc phát triển phần mềm trong các lĩnh vực AI, Robotics và hệ thống nhúng (YoloBit/Python) như sau:

- **Fact:** [CONV] Unit tests được thiết kế để kiểm tra các phần mã nhỏ nhất (như một hàm hoặc phương thức đơn lẻ) nhằm đảm bảo tính chính xác của từng bộ phận cấu thành hệ thống.
- **Source:** Đoạn 1 - "Unit tests are designed to test small pieces of code, like a single function or method..."
- **Tag:** [vv10]

- **Fact:** [CONV] Việc kiểm thử đơn vị giúp cô lập lỗi, cho phép phát hiện và sửa bug sớm trong quá trình phát triển trước khi chúng trở thành vấn đề lớn và tốn kém.
- **Source:** Đoạn 1 - "Unit testing helps to isolate errors so bugs can be identified and fixed earlier on..."
- **Tag:** [vv10]

- **Fact:** [CONV] `unittest` là một framework kiểm thử đơn vị trong Python dựa trên các khái niệm lập trình hướng đối tượng (OOP).
- **Source:** Đoạn 2 - "object-oriented concepts of unittest, a unit testing framework in Python..."
- **Tag:** [vv10]

- **Fact:** [CONV] Để tạo các ca kiểm thử (Test cases), lập trình viên cần viết các lớp con (subclasses) kế thừa từ `unittest.TestCase`.
- **Source:** Section: Test cases - "To write test cases, developers need to write subclasses of TestCase..."
- **Tag:** [vv10]

- **Fact:** [CONV] Trình chạy test (test runner) chỉ nhận diện các phương thức là bài kiểm tra nếu tên phương thức đó bắt đầu bằng tiền tố `test`.
- **Source:** Section: Test cases - "implement a test method that starts with the name test."
- **Tag:** [vv10]

- **Fact:** [CONV] Các phương thức Assertion (như `assertEqual`, `assertTrue`, `assertFalse`, `assertRaises`) được sử dụng thay cho câu lệnh `assert` tiêu chuẩn để trình chạy test có thể thu thập kết quả và tạo báo cáo.
- **Source:** Section: Assertions - "Each of these assert methods is used in place of the standard assert statement..."
- **Tag:** [vv10]

- **Fact:** [CONV] Phương thức `assertRaises(ExceptionType)` cho phép kiểm tra xem một ngoại lệ cụ thể có được ném ra đúng lúc hay không, giúp đảm bảo khả năng xử lý lỗi của chương trình.
- **Source:** Section: Assertions - "assertRaises... allows you to test whether exceptions are raised when they should be..."
- **Tag:** [vv10]

- **Fact:** [CONV] Giao diện dòng lệnh (CLI) của Python cho phép chạy kiểm thử linh hoạt cho toàn bộ module, một class cụ thể hoặc chỉ một phương thức đơn lẻ.
- **Source:** Section: Command-line interface - "run tests from modules, classes, or even individual test methods."
- **Tag:** [vv10]

- **Fact:** [CONV] Unit testing là quy trình bắt buộc khi phát triển các thuật toán điều khiển Robot hoặc xử lý dữ liệu AI bằng Python để đảm bảo độ tin cậy của hệ thống.
- **Source:** Kiến thức bổ trợ về quy trình phát triển kỹ thuật.
- **Tag:** [Unverified_Source]

- **Fact:** [CONV] Đối với các thiết bị như YoloBit (chạy MicroPython), các nguyên lý của `unittest` có thể được áp dụng để kiểm tra logic điều khiển cảm biến và động cơ.
- **Source:** Kiến thức ứng dụng Python trong Robotics/IoT.
- **Tag:** [Unverified_Source]