Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v10 liên quan đến lập trình Python, xử lý lỗi và kiểm thử phần mềm:

- **Fact:** [Sử dụng phương thức `assertRaises(ExceptionType, function, *args)` trong framework `unittest` để kiểm tra xem một hàm có ném ra ngoại lệ mong muốn khi nhận đầu vào không hợp lệ hay không.]
- **Source:** (v10 - Section: Review: Testing for expected errors)
- **Tag:** [vv10]

- **Fact:** [Ngoại lệ `OSError` là lớp cha bao gồm các lỗi hệ thống tệp phổ biến như `FileNotFoundError` (không tìm thấy tệp) và `PermissionError` (không có quyền truy cập).]
- **Source:** (v10 - Section: Phân tích try-except trong character_frequency)
- **Tag:** [vv10]

- **Fact:** [Từ khóa `raise` được sử dụng để chủ động kích hoạt một ngoại lệ (Exception) trong Python khi chương trình gặp một điều kiện logic không thỏa mãn.]
- **Source:** (v10 - Section: Tự tạo Exception / Phân tích validate_user)
- **Tag:** [vv10]

- **Fact:** [Phương thức `isalnum()` của đối tượng chuỗi (string) trong Python trả về giá trị `True` nếu tất cả các ký tự trong chuỗi đều là chữ cái hoặc chữ số.]
- **Source:** (v10 - Section: Phân tích validate_user, dòng check username.isalnum())
- **Tag:** [vv10]

- **Fact:** [Dòng Shebang `#!/usr/bin/env python3` cho phép hệ điều hành Unix-like (Linux, macOS, WSL) xác định trình thông dịch Python 3 để thực thi tệp tin trực tiếp.]
- **Source:** (v10 - Section: Shebang line là gì)
- **Tag:** [vv10]

- **Fact:** [Hàm `unittest.main()` cung cấp một giao diện dòng lệnh để thực thi tất cả các phương thức kiểm thử (bắt đầu bằng tiền tố `test_`) trong các lớp kế thừa từ `unittest.TestCase`.]
- **Source:** (v10 - Section: Thay bằng unittest.main() được hay không)
- **Tag:** [vv10]

- **Fact:** [Sử dụng Context Manager với cú pháp `with open(filename) as f:` là phương pháp an toàn để xử lý tệp tin vì nó tự động đóng tệp sau khi hoàn thành, ngay cả khi có ngoại lệ xảy ra.]
- **Source:** (v10 - Section: Gợi ý cải thiện character_frequency)
- **Tag:** [vv10]

- **Fact:** [Trong cấu trúc `try-except`, khối `else` sẽ được thực thi nếu không có ngoại lệ nào xảy ra trong khối `try`, và khối `finally` sẽ luôn được thực thi bất kể kết quả.]
- **Source:** (v10 - Section: Thêm finally và else)
- **Tag:** [vv10]

- **Fact:** [Phương thức `dict.get(key, default)` giúp truy xuất giá trị của một khóa trong từ điển và trả về giá trị mặc định nếu khóa đó không tồn tại, giúp tránh lỗi `KeyError`.]
- **Source:** (v10 - Section: Phân tích character_frequency, dòng characters.get(char, 0))
- **Tag:** [vv10]

- **Fact:** [Để một tệp Python có dòng Shebang có thể chạy trực tiếp như một chương trình thực thi trên Linux, người dùng cần cấp quyền thực thi bằng lệnh `chmod +x filename.py`.]
- **Source:** (v10 - Section: Cách chạy file nếu dùng shebang)
- **Tag:** [vv10]