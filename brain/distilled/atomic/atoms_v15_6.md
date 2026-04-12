Chào bạn, tôi là @scout. Dựa trên dữ liệu từ **Volume v15**, tôi xin trích xuất các sự kiện kỹ thuật liên quan đến lập trình Python và hệ thống (nền tảng quan trọng cho IoT, Robotics và AI) như sau:

- **Fact:** Cú pháp của biểu thức điều kiện (conditional expression) hay toán tử ba ngôi trong Python là: `value_if_true if condition else value_if_false`.
- **Source:** v15 - Section: Giải thích Conditional Expression.
- **Tag:** [vv15]

- **Fact:** Thư viện `unittest` là một framework tích hợp sẵn trong Python dùng để kiểm tra từng phần nhỏ của mã nguồn (Unit Testing) nhằm phát hiện lỗi sớm.
- **Source:** v15 - Section: Khái Niệm Cơ Bản (Unit Testing).
- **Tag:** [vv15]

- **Fact:** `pytest` là framework kiểm tra mạnh mẽ hơn `unittest`, hỗ trợ "fixtures" để thiết lập môi trường và cung cấp thông báo lỗi chi tiết hơn.
- **Source:** v15 - Section: Các Tính Năng Chính của pytest / So sánh unittest và pytest.
- **Tag:** [vv15]

- **Fact:** Mã thoát (exit code) bằng **0** có nghĩa là chương trình hoặc script đã kết thúc thành công mà không có lỗi.
- **Source:** v15 - Section: Câu hỏi 4 (Lệnh và mã thoát).
- **Tag:** [vv15]

- **Fact:** Lệnh `echo $?` được sử dụng trong hệ thống (Linux/Unix) để in ra giá trị thoát của một script vừa thực thi.
- **Source:** v15 - Section: Câu hỏi 1 (Lệnh và mã thoát).
- **Tag:** [vv15]

- **Fact:** Khi sử dụng hàm `input()` trong Python để nhận dữ liệu từ người dùng, chương trình đang sử dụng dòng I/O là **STDIN**.
- **Source:** v15 - Section: Câu hỏi 3 (Lệnh và mã thoát).
- **Tag:** [vv15]

- **Fact:** Hàm `subprocess.run()` trong Python trả về một đối tượng kiểu `CompletedProcess` sau khi lệnh hệ thống chạy xong.
- **Source:** v15 - Section: Câu hỏi 1 (subprocess).
- **Tag:** [vv15]

- **Fact:** Tham số `cwd` (current working directory) trong module `subprocess` cho phép thay đổi thư mục thực thi lệnh của tiến trình con.
- **Source:** v15 - Section: Câu hỏi 2 (subprocess).
- **Tag:** [vv15]

- **Fact:** Khi một tiến trình con (child process) được chạy bằng module `subprocess`, tiến trình cha (parent process) sẽ bị chặn (blocked) cho đến khi tiến trình con kết thúc.
- **Source:** v15 - Section: Câu hỏi 3 (subprocess).
- **Tag:** [vv15]

- **Fact:** Để lưu trữ đầu ra của một lệnh hệ thống khi dùng `subprocess.run`, cần đặt tham số `capture_output=True`.
- **Source:** v15 - Section: Câu hỏi 4 (subprocess).
- **Tag:** [vv15]

- **Fact:** `sys.argv[1]` là cách để script Python chấp nhận đối số dòng lệnh (ví dụ: đường dẫn đến file log) truyền vào từ terminal.
- **Source:** v15 - Section: Câu hỏi 1 (Log processing).
- **Tag:** [vv15]

- **Fact:** Cấu trúc dữ liệu **Dictionary** (từ điển) thường được sử dụng để đếm tần suất xuất hiện của các lỗi cụ thể trong quá trình xử lý log.
- **Source:** v15 - Section: Câu hỏi 2 (Log processing).
- **Tag:** [vv15]

- **Fact:** Python là ngôn ngữ nền tảng được sử dụng rộng rãi để lập trình cho các thiết bị IoT (như Raspberry Pi) và điều khiển robot nhờ khả năng tương tác hệ thống mạnh mẽ qua module `os` và `subprocess`.
- **Source:** [Nội dung suy luận từ các công cụ hệ thống trong text]
- **Tag:** [Unverified_Source]

--------------------------------------------------
**Ghi chú từ @scout:** Dữ liệu RAW tập trung vào kỹ năng lập trình Python hệ thống và kiểm thử, vốn là kiến thức bổ trợ cực kỳ quan trọng để xây dựng phần mềm ổn định cho Robotics và AI. Các thông tin cụ thể về phần cứng Arduino hay YoloBit không xuất hiện trong đoạn dữ liệu này.