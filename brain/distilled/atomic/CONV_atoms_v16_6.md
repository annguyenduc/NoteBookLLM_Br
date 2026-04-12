Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v16), tập trung vào các kỹ thuật xử lý dữ liệu và lập trình bổ trợ cho AI và hệ thống điều khiển:

- **Fact:** [CONV] Cụm biểu thức chính quy `([0-5][0-9])` được sử dụng để kiểm tra tính hợp lệ của số phút (từ 00 đến 59) trong các định dạng thời gian.
- **Source:** [v16 - Section: Cấu trúc của cụm ([0-5][0-9])]
- **Tag:** [vv16]

- **Fact:** [CONV] Trong Python, tiền tố `r` trước một chuỗi (raw string) giúp trình thông dịch coi các dấu gạch chéo ngược `\` là ký tự thuần túy, ngăn chặn việc diễn giải chúng thành các chuỗi thoát (escape sequences).
- **Source:** [v16 - Section: Question 4 - Raw strings]
- **Tag:** [vv16]

- **Fact:** [CONV] Ký tự `\w` trong biểu thức chính quy khớp với các chữ cái (bao gồm cả Unicode), chữ số và dấu gạch dưới `_`, trong khi `[A-Za-z0-9]` chỉ khớp với các ký tự Latinh và số cơ bản.
- **Source:** [v16 - Section: \w có tương đương với [A-Za-z0-9] không]
- **Tag:** [vv16]

- **Fact:** [CONV] Cú pháp `(?:...)` tạo ra một nhóm không ghi nhớ (non-capturing group), cho phép nhóm các thành phần để áp dụng lượng từ mà không lưu trữ kết quả khớp vào bộ nhớ đệm của hệ thống.
- **Source:** [v16 - Section: (?:-[0-9]{4}) có nghĩa là gì]
- **Tag:** [vv16]

- **Fact:** [CONV] Lượng từ `+` (plus character) trong Regex xác định rằng phần tử đứng trước nó phải xuất hiện ít nhất một lần hoặc nhiều lần liên tiếp.
- **Source:** [v16 - Section: What does the plus character [+] do in regex?]
- **Tag:** [vv16]

- **Fact:** [CONV] Lượng từ `?` trong biểu thức chính quy biểu thị sự xuất hiện "không hoặc một lần", biến phần tử đứng trước nó thành một thành phần tùy chọn trong chuỗi khớp.
- **Source:** [v16 - Section: (?:-[0-9]{4})? kí tự '?']
- **Tag:** [vv16]

- **Fact:** [CONV] Phương thức `.group(0)` trong thư viện `re` của Python trả về toàn bộ chuỗi khớp, trong khi các chỉ số từ 1 trở đi truy cập vào các nhóm bắt (capturing groups) cụ thể.
- **Source:** [v16 - Section: .group() là gì]
- **Tag:** [vv16]

- **Fact:** [CONV] Khi sử dụng hàm `re.split()` với biểu thức chính quy nằm trong dấu ngoặc đơn `()`, các ký tự phân tách (delimiters) sẽ được giữ lại và trả về như một phần của danh sách kết quả.
- **Source:** [v16 - Section: re.split(r"[.?!]", ...) khác gì với re.split(r"([.?!])", ...)]
- **Tag:** [vv16]

- **Fact:** [CONV] Việc truy cập trực tiếp vào chỉ số nhóm (ví dụ: `result[1]`) từ kết quả của `re.search()` mà không kiểm tra giá trị `None` sẽ gây ra lỗi `TypeError` nếu không tìm thấy chuỗi khớp.
- **Source:** [v16 - Section: Giải thích vì sao đoạn code trên sai]
- **Tag:** [vv16]

- **Fact:** [CONV] Để khớp các từ viết tắt nằm trong dấu ngoặc đơn bao gồm cả chữ và số, có thể sử dụng mẫu biểu thức chính quy `r'\([A-Za-z0-9]+\)'`.
- **Source:** [v16 - Section: Giải thích: pattern = r'\([A-Za-z0-9]+\)']
- **Tag:** [vv16]