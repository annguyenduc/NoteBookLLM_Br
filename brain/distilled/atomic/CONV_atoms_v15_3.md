Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu cung cấp:

- **Fact:** [CONV] Hàm `LetterCompiler` sử dụng biểu thức chính quy `re.findall(r'[a-c]', txt)` để tìm và trả về danh sách các ký tự 'a', 'b', và 'c' xuất hiện trong một chuỗi văn bản.
- **Source:** [vv15 - Section: Cách kiểm tra]
- **Tag:** [vv15]

- **Fact:** [CONV] File tài liệu định dạng `.docx` thực chất là một tệp nén; người dùng có thể đổi đuôi thành `.zip` để truy cập vào cấu trúc thư mục bên trong, nơi hình ảnh và tệp GIF được lưu trữ tại đường dẫn `word/media`.
- **Source:** [vv15 - Section: Conversation: Chuyển đổi và giải nén]
- **Tag:** [vv15]

- **Fact:** [CONV] Trong môi trường Google Colab, thư viện `google.colab.files` cung cấp hàm `files.upload()` để mở hộp thoại tải tệp từ máy tính cục bộ lên server và `files.download()` để tải tệp từ server về máy tính.
- **Source:** [vv15 - Section: Bước 1 & Bước 5 trong hướng dẫn Colab]
- **Tag:** [vv15]

- **Fact:** [CONV] Thư viện `zipfile` của Python hỗ trợ phương thức `zip_ref.namelist()` để liệt kê tất cả các tệp bên trong một file nén và `zip_ref.extract()` để giải nén các tệp cụ thể theo điều kiện lọc (như lọc theo thư mục `word/media/`).
- **Source:** [vv15 - Section: Bước 3: Giải nén chỉ thư mục word/media]
- **Tag:** [vv15]

- **Fact:** [CONV] Lỗi `SyntaxError: (unicode error) 'unicodeescape'` thường xảy ra trên Windows khi đường dẫn tệp chứa dấu gạch chéo ngược `\` đơn lẻ; cách khắc phục là sử dụng raw string (thêm tiền tố `r`), dùng dấu gạch chéo xuôi `/`, hoặc dùng hai dấu gạch chéo ngược `\\`.
- **Source:** [vv15 - Section: ASSISTANT phản hồi về lỗi SyntaxError]
- **Tag:** [vv15]

- **Fact:** [CONV] Thư viện `shutil` trong Python được sử dụng để thực hiện các thao tác tệp cao cấp, bao gồm hàm `shutil.make_archive()` để nén toàn bộ một thư mục thành tệp định dạng `.zip`.
- **Source:** [vv15 - Section: Script chi tiết cho Google Colab & Phản hồi về lỗi NameError]
- **Tag:** [vv15]

- **Fact:** [CONV] Để xử lý hàng loạt tệp trong một thư mục bằng Python, có thể sử dụng `os.listdir()` kết hợp với vòng lặp `for` và kiểm tra phần mở rộng tệp bằng phương thức `.endswith('.docx')`.
- **Source:** [vv15 - Section: Script tự động từ đường dẫn đã cho]
- **Tag:** [vv15]

- **Fact:** [CONV] Việc đổi tên tệp hoặc phần mở rộng của tệp trong Python được thực hiện thông qua hàm `os.rename(old_name, new_name)`.
- **Source:** [vv15 - Section: Bước 2: Đổi tên file .docx thành .zip]
- **Tag:** [vv15]