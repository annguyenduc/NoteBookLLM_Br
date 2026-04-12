---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v10_40
  title: CONV_atoms_v10_40
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v10) về lập trình Python, kiểm thử phần mềm và xử lý hệ thống:

- Fact: [CONV] `unittest.main()` là phương thức tự động tìm kiếm tất cả các lớp kế thừa từ `unittest.TestCase` trong file và thực thi toàn bộ các bài kiểm thử (test cases) mà không cần nạp thủ công.
- Source: [vv10] - Section: "Vì sao lại được?"
- Tag: [vv10]

- Fact: [CONV] Trong framework `unittest`, `setUpModule()` được thực thi một lần duy nhất trước khi bất kỳ bài test nào trong module bắt đầu, và `tearDownModule()` thực thi một lần sau khi tất cả các bài test hoàn tất.
- Source: [vv10] - Section: "Các chức năng chính trong file"
- Tag: [vv10]

- Fact: [CONV] Phương thức `assertRaises` được sử dụng để xác minh rằng một hàm sẽ ném ra một ngoại lệ (Exception) cụ thể khi nhận đầu vào không hợp lệ, đây là kỹ thuật quan trọng trong "Testing for Expected Errors".
- Source: [vv10] - Section: "Review: Testing for expected errors"
- Tag: [vv10]

- Fact: [CONV] Dòng Shebang `#!/usr/bin/env python3` ở đầu file script cho phép hệ điều hành (Linux, macOS, WSL) xác định trình thông dịch Python 3 để thực thi file trực tiếp như một chương trình độc lập.
- Source: [vv10] - Section: "Shebang (#!/usr/bin/env python3) là gì?"
- Tag: [vv10]

- Fact: [CONV] Sử dụng cấu trúc `with open(filename) as f:` (Context Manager) giúp tự động đóng file và giải phóng tài nguyên hệ thống ngay cả khi xảy ra lỗi trong quá trình xử lý, thay thế cho việc gọi `f.close()` thủ công.
- Source: [vv10] - Section: "Một số gợi ý cải thiện"
- Tag: [vv10]

- Fact: [CONV] Ngoại lệ `OSError` trong Python là lớp cha của các lỗi liên quan đến hệ thống tệp như `FileNotFoundError` (không tìm thấy tệp) và `PermissionError` (không có quyền truy cập).
- Source: [vv10] - Section: "Phần try-except"
- Tag: [vv10]

- Fact: [CONV] Phương thức `isalnum()` của đối tượng chuỗi (string) trong Python trả về `True` nếu tất cả các ký tự trong chuỗi là chữ cái hoặc chữ số, và `False` nếu có ký tự đặc biệt hoặc khoảng trắng.
- Source: [vv10] - Section: "Check ký tự hợp lệ"
- Tag: [vv10]

- Fact: [CONV] Trong kiểm thử đơn vị (Unit Test), `setUp()` được gọi trước mỗi hàm test đơn lẻ để thiết lập môi trường, và `tearDown()` được gọi ngay sau mỗi hàm test để dọn dẹp dữ liệu.
- Source: [vv10] - Section: "Các chức năng chính trong file"
- Tag: [vv10]

- Fact: [CONV] Việc sử dụng `isinstance(variable, type)` để kiểm tra kiểu dữ liệu đầu vào giúp ngăn chặn lỗi `AttributeError` khi chương trình cố gắng gọi các phương thức không tồn tại trên các kiểu dữ liệu không mong muốn (ví dụ: gọi `.isalnum()` trên một `list`).
- Source: [vv10] - Section: "Nếu muốn bảo vệ code tốt hơn"
- Tag: [vv10]

- Fact: [CONV] Phương thức `.get(key, default)` của Dictionary trong Python cho phép truy xuất giá trị của một khóa với một giá trị mặc định trả về nếu khóa đó không tồn tại, giúp tránh lỗi `KeyError`.
- Source: [vv10] - Section: "Phần đọc file và đếm ký tự"
- Tag: [vv10]