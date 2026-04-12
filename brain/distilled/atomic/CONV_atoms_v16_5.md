Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu **Volume v16** liên quan đến lập trình Python, xử lý luồng dữ liệu và biểu thức chính quy (Regular Expression) - những nền tảng quan trọng trong Robotics và AI.

### Danh sách sự kiện (Facts) - Volume v16

1. **Fact:** [CONV] Có ba cách chính để chạy script Python trong VS Code: sử dụng Terminal với lệnh `python tên_tệp.py`, sử dụng phím tắt (`F5` hoặc `Shift + Enter`), hoặc nhấp vào biểu tượng "Run" ở góc trên bên phải.
   - **Source:** [v16 - Section: Code (View > Terminal) và chạy lệnh]
   - **Tag:** [vv16]

2. **Fact:** [CONV] Shebang (`#!/usr/bin/env python3`) là dòng mã ở đầu tệp Python cho phép script tự xác định trình thông dịch và chạy trực tiếp từ dòng lệnh mà không cần gõ tiền tố `python`.
   - **Source:** [v16 - Section: Khi nào nên sử dụng Shebang]
   - **Tag:** [vv16]

3. **Fact:** [CONV] Để một script có thể thực thi trực tiếp trên Unix/Linux, cần sử dụng lệnh `chmod +x tên_tệp.py` để thiết lập quyền thực thi.
   - **Source:** [v16 - Section: Ví dụ về Shebang trong tệp Python]
   - **Tag:** [vv16]

4. **Fact:** [CONV] Trong Python, hàm `input()` nhận dữ liệu từ đầu vào tiêu chuẩn (STDIN), trong khi hàm `print()` gửi dữ liệu đến đầu ra tiêu chuẩn (STDOUT). Các thông báo lỗi hệ thống thường được gửi đến luồng lỗi tiêu chuẩn (STDERR).
   - **Source:** [v16 - Section: Nội dung của streams.py]
   - **Tag:** [vv16]

5. **Fact:** [CONV] Lệnh `echo $?` trong môi trường shell được sử dụng để in ra giá trị thoát (exit status) của lệnh vừa thực hiện; giá trị `0` mặc định là thành công, các giá trị khác `0` biểu thị lỗi.
   - **Source:** [v16 - Section: Question 1 (Exit value)]
   - **Tag:** [vv16]

6. **Fact:** [CONV] Trong thư viện `re` của Python, các ký tự đại diện phổ biến bao gồm: `\d` (chữ số), `\w` (chữ cái, chữ số, gạch dưới), `\s` (khoảng trắng), `^` (bắt đầu chuỗi) và `$` (kết thúc chuỗi).
   - **Source:** [v16 - Section: Special Characters in Python RE]
   - **Tag:** [vv16]

7. **Fact:** [CONV] Dấu gạch ngang `-` bên trong ngoặc vuông `[]` của biểu thức chính quy sẽ được hiểu là một ký tự bình thường nếu nó nằm ở vị trí không tạo ra một phạm vi (ví dụ: nằm ở cuối hoặc ngay sau `\w`).
   - **Source:** [v16 - Section: Sự khác biệt chính (giữa hai biểu thức chính quy)]
   - **Tag:** [vv16]

8. **Fact:** [CONV] Để kiểm tra định dạng thời gian 12 giờ (ví dụ: 12:45pm), biểu thức chính quy hiệu quả là `r'^(1[0-2]|0?[1-9]):([0-5][0-9]) ?([aApP][mM])?$'`.
   - **Source:** [v16 - Section: Giải thích biểu thức chính quy (check_time)]
   - **Tag:** [vv16]

9. **Fact:** [CONV] Phương pháp để xác định các ký tự đặc biệt (không phải chữ và số) trong một chuỗi là sử dụng mẫu phủ định trong RE: `[^a-zA-Z0-9\s]`.
   - **Source:** [v16 - Section: Sử dụng Regular Expression (xác định ký tự đặc biệt)]
   - **Tag:** [vv16]

10. **Fact:** [CONV] Việc xây dựng biểu thức chính quy cho các phạm vi số phức tạp (như giờ 1-12) đòi hỏi việc kết hợp các lựa chọn thay thế bằng ký tự `|` (ví dụ: `1[0-2]` cho 10-12 và `0?[1-9]` cho 1-9).
    - **Source:** [v16 - Section: Bước 4: Tạo biểu thức chính quy hoàn chỉnh]
    - **Tag:** [vv16]

--------------------------------------------------
**Ghi chú:** Các kiến thức về xử lý chuỗi và luồng dữ liệu này là nền tảng để lập trình robot (Robotics) nhận lệnh từ cảm biến hoặc giao tiếp qua mạng (IoT). [Unverified_Source]