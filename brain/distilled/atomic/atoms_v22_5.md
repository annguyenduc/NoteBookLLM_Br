Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v22) liên quan đến lập trình điều khiển và xử lý dữ liệu (nền tảng cho AI và hệ thống IoT):

- **Fact:** Trong biểu thức chính quy (RegExp), cờ `m` (multiline) cho phép neo `^` khớp với điểm bắt đầu của mỗi dòng trong một chuỗi văn bản có nhiều dòng, thay vì chỉ khớp với điểm bắt đầu của toàn bộ chuỗi.
- **Source:** [Dữ liệu RAW - Section: ASSISTANT trả lời về cờ 'g' và 'gm']
- **Tag:** [vv22]

- **Fact:** Ký hiệu `\b` (word boundary) trong RegExp được sử dụng để xác định ranh giới từ, đảm bảo từ khóa được tìm kiếm là một từ độc lập, không phải là một phần của một từ khác (ví dụ: khớp "Sử" nhưng không khớp "Sử dụng").
- **Source:** [Dữ liệu RAW - Section: ASSISTANT giải thích về `var regex = new RegExp("^" + word + "\\b", "g");`]
- **Tag:** [vv22]

- **Fact:** Để tối ưu hóa hiệu suất khi xử lý dữ liệu lớn trong Google Sheets (thường dùng trong logging dữ liệu IoT), việc sử dụng `getValues()` để lấy mảng hai chiều và `setValues()` để cập nhật hàng loạt hiệu quả hơn việc lặp qua từng ô bằng `getValue()` và `setValue()`.
- **Source:** [Dữ liệu RAW - Section: ASSISTANT trả lời về việc thêm hàng loạt]
- **Tag:** [vv22]

- **Fact:** Hệ tọa độ R1C1 là phương thức tham chiếu ô bằng số thứ tự hàng (Row) và cột (Column), thay vì sử dụng chữ cái cho cột như định dạng A1 (ví dụ: R2C3 tương đương với ô C2).
- **Source:** [Dữ liệu RAW - Section: ASSISTANT giải thích về R1C1]
- **Tag:** [vv22]

- **Fact:** Phương thức `getRangeList()` trong Apps Script trả về một đối tượng `RangeList` chứa danh sách nhiều phạm vi ô khác nhau, trong khi `getRange()` chỉ trả về một đối tượng `Range` duy nhất.
- **Source:** [Dữ liệu RAW - Section: ASSISTANT giải thích sự khác nhau giữa getRange và getRangeList]
- **Tag:** [vv22]

- **Fact:** Phương thức `indexOf()` trong JavaScript trả về giá trị `0` nếu một chuỗi con được tìm thấy ngay tại vị trí bắt đầu của chuỗi mục tiêu, thường được dùng để kiểm tra tiền tố của dữ liệu.
- **Source:** [Dữ liệu RAW - Section: ASSISTANT sửa lại mã nguồn sử dụng indexOf]
- **Tag:** [vv22]

- **Fact:** Trong JavaScript, toán tử `==` thực hiện so sánh bằng cách chuyển đổi kiểu dữ liệu về cùng một loại (type coercion), trong khi `===` thực hiện so sánh nghiêm ngặt cả về giá trị và kiểu dữ liệu.
- **Source:** [Dữ liệu RAW - Section: ASSISTANT giải thích về toán tử ===]
- **Tag:** [vv22]