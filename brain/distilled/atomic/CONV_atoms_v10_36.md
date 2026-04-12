Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật đã được trích xuất và chưng cất từ nguồn dữ liệu **Volume v10** về lập trình Python và Unit Test:

- **Fact:** [CONV] Một class Python cơ bản bao gồm các thành phần: `class` (khai báo), `__init__` (hàm khởi tạo tự động chạy khi tạo đối tượng), `self` (tham chiếu chính đối tượng đó), thuộc tính (dữ liệu lưu trữ) và phương thức (hành động).
- **Source:** (v10 - Section: 1. Cấu trúc một class Python cơ bản)
- **Tag:** [vv10]

- **Fact:** [CONV] Trong lập trình hướng đối tượng Python, `self` luôn là tham số đầu tiên trong mọi phương thức (method) để định danh "cái tôi" của đối tượng, giúp phân biệt dữ liệu giữa các đối tượng khác nhau được tạo ra từ cùng một class.
- **Source:** (v10 - Section: Giải thích dễ hiểu & Một số lưu ý cho người mới)
- **Tag:** [vv10]

- **Fact:** [CONV] Khi sử dụng thư viện `unittest`, lớp kế thừa từ `unittest.TestCase` không cần khai báo `__init__` thủ công vì framework này đã tự động quản lý việc khởi tạo để phục vụ chạy kiểm thử tự động.
- **Source:** (v10 - Section: Tại sao trong unittest không thấy __init__()?)
- **Tag:** [vv10]

- **Fact:** [CONV] Thay vì sử dụng `__init__` để chuẩn bị dữ liệu trong Unit Test, lập trình viên nên sử dụng phương thức `setUp()` để thiết lập môi trường hoặc dữ liệu mẫu trước mỗi test case.
- **Source:** (v10 - Section: Tóm gọn cực ngắn - unittest)
- **Tag:** [vv10]

- **Fact:** [CONV] Kỹ thuật "Dictionary Mapping" là phương pháp chuyên nghiệp để thay thế các cấu trúc `if-else` hoặc `if-elif` phức tạp, giúp mã nguồn ngắn gọn, dễ bảo trì và tối ưu tốc độ truy xuất dữ liệu.
- **Source:** (v10 - Section: Tối ưu cách trên bằng dictionary mapping)
- **Tag:** [vv10]

- **Fact:** [CONV] Phương thức `dict.get(key, default)` trong Python giúp truy cập giá trị của từ điển một cách an toàn, tránh lỗi `KeyError` gây dừng chương trình (crash) bằng cách trả về một giá trị mặc định nếu khóa không tồn tại.
- **Source:** (v10 - Section: giải thích vì sao dùng get() và nếu không dùng get())
- **Tag:** [vv10]

- **Fact:** [CONV] Theo chuẩn PEP8, mã nguồn Python chuyên nghiệp cần tuân thủ: thụt lề 4 khoảng trắng (spaces), cách một dòng trắng giữa các phương thức/class, và sử dụng khối `if __name__ == "__main__":` để kiểm soát thực thi.
- **Source:** (v10 - Section: Chuẩn hóa PEP8 & Bonus: Cách chạy chuẩn)
- **Tag:** [vv10]

- **Fact:** [CONV] Để kiểm tra sự tồn tại của một khóa trong từ điển mà không làm dừng chương trình khi duyệt danh sách, có thể kết hợp `dict.get()` với cấu trúc điều kiện `if price is not None` để xử lý các trường hợp ngoại lệ.
- **Source:** (v10 - Section: Nếu tôi mong muốn loại bánh không có trong dict...)
- **Tag:** [vv10]

- **Fact:** [CONV] Trên hệ điều hành Ubuntu (WSL), có thể kích hoạt môi trường lập trình Python bằng lệnh `python3` trong Terminal của VSCode và thoát bằng lệnh `exit()` hoặc tổ hợp phím `Ctrl + D`.
- **Source:** (v10 - Section: Các bước mở lại Python trên Ubuntu WSL bằng VSCode)
- **Tag:** [vv10]