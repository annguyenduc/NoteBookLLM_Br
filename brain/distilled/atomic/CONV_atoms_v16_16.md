Dưới đây là đáp án cho các câu hỏi về Regular Expressions (Regex) và công cụ `grep`:

### Đáp án trắc nghiệm:

1.  **Question 1:** Which of the following expressions uses a reserved character that can represent any single character?
    *   **Đáp án:** `grep f.n /usr/share/text` (Ký tự dấu chấm `.` là ký tự đại diện cho bất kỳ ký tự đơn nào).

2.  **Question 2:** A programmer is writing a script to help a store manager find the product numbers... Which of the following methods should they use?
    *   **Đáp án:** **Use regex to find the patterns that match the product number.** (Regex được thiết kế tối ưu để tìm kiếm các chuỗi tuân theo một định dạng/mẫu cụ thể).

3.  **Question 3:** The circumflex [^] and the dollar sign [$] are anchor characters. What do these anchor characters do in regex?
    *   **Đáp án:** **Match the start and end of a line** (Dấu `^` khớp với điểm bắt đầu dòng và `$` khớp với điểm kết thúc dòng).

4.  **Question 4:** When using regex, some characters represent particular types of characters... What are these characters collectively known as?
    *   **Đáp án:** **Reserved characters** (Hoặc thường được gọi là metacharacters/special characters trong các tài liệu kỹ thuật).

5.  **Question 5:** What is grep?
    *   **Đáp án:** **A command-line regex tool** (Grep là công cụ dòng lệnh dùng để tìm kiếm các dòng văn bản khớp với biểu thức chính quy).

--------------------------------------------------

### Trích xuất tri thức (Facts) theo chuẩn LOM v4.1:

- **Fact:** [CONV] Ký tự dấu chấm `.` trong biểu thức chính quy (Regex) là một ký tự dành riêng đại diện cho chính xác một ký tự bất kỳ.
- **Source:** [User Quiz Data - Question 1]
- **Tag:** [vv16]

- **Fact:** [CONV] Biểu thức chính quy (Regex) là phương pháp hiệu quả nhất để tìm kiếm các mẫu dữ liệu lặp lại như mã số sản phẩm trong tài liệu văn bản.
- **Source:** [User Quiz Data - Question 2]
- **Tag:** [vv16]

- **Fact:** [CONV] Các ký tự neo (Anchor characters) bao gồm `^` (khớp đầu dòng) và `$` (khớp cuối dòng) dùng để định vị vị trí của mẫu tìm kiếm.
- **Source:** [User Quiz Data - Question 3]
- **Tag:** [vv16]

- **Fact:** [CONV] `grep` là một tiện ích dòng lệnh tiêu chuẩn trên các hệ thống Unix/Linux chuyên dùng để lọc và tìm kiếm văn bản dựa trên Regex.
- **Source:** [User Quiz Data - Question 5]
- **Tag:** [vv16]

- **Fact:** [CONV] Các ký tự có ý nghĩa đặc biệt trong Regex như `$`, `^`, và `.` được phân loại là các ký tự dành riêng (Reserved characters).
- **Source:** [User Quiz Data - Question 4]
- **Tag:** [vv16]