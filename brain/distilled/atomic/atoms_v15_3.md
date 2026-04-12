Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp:

- **Fact:** Hàm `LetterCompiler` sử dụng biểu thức chính quy `re.findall(r'[a-c]', txt)` để tìm kiếm và trích xuất tất cả các ký tự 'a', 'b', và 'c' từ một chuỗi văn bản đầu vào.
- **Source:** (v15 - Section: Cách kiểm tra)
- **Tag:** [vv15]

- **Fact:** Tệp tin định dạng `.docx` có thể được chuyển đổi sang định dạng `.zip` bằng cách đổi phần mở rộng của tệp, cho phép truy cập vào cấu trúc thư mục bên trong của tài liệu Word.
- **Source:** (v15 - Section: Bước 2: Đổi tên file .docx thành .zip)
- **Tag:** [vv15]

- **Fact:** Trong cấu trúc tệp tin của Microsoft Word (.docx), các hình ảnh và tệp GIF được lưu trữ mặc định trong thư mục có đường dẫn `word/media/`.
- **Source:** (v15 - Section: Bước 3: Giải nén chỉ thư mục word/media)
- **Tag:** [vv15]

- **Fact:** Thư viện `zipfile` trong Python cung cấp phương thức `namelist()` để liệt kê tất cả các tệp trong một kho lưu trữ ZIP và phương thức `extract()` để giải nén các tệp cụ thể dựa trên đường dẫn của chúng.
- **Source:** (v15 - Section: Bước 3: Giải nén chỉ thư mục word/media)
- **Tag:** [vv15]

- **Fact:** Khi khai báo đường dẫn thư mục trên hệ điều hành Windows trong Python, việc sử dụng dấu gạch chéo ngược đơn (`\`) có thể gây ra lỗi `SyntaxError: (unicode error) 'unicodeescape'` do Python hiểu nhầm là các ký tự thoát (escape characters).
- **Source:** (v15 - Section: USER: SyntaxError: (unicode error) 'unicodeescape')
- **Tag:** [vv15]

- **Fact:** Để xử lý đường dẫn tệp tin Windows trong Python một cách an toàn, có thể sử dụng "raw string" bằng cách thêm tiền tố `r` trước chuỗi (ví dụ: `r"C:\Users\..."`) hoặc sử dụng dấu gạch chéo xuôi (`/`).
- **Source:** (v15 - Section: 1. Sử dụng dấu gạch chéo xuôi (/) thay cho dấu gạch chéo ngược (\))
- **Tag:** [vv15]

- **Fact:** Trên môi trường Google Colab, thư viện `google.colab.files` cung cấp hàm `upload()` để tải tệp từ máy tính cá nhân lên máy chủ Colab và hàm `download()` để tải tệp từ Colab về máy tính.
- **Source:** (v15 - Section: Bước 1: Tải file .docx lên Google Colab & Bước 5: Tải các file ảnh và GIF về máy tính)
- **Tag:** [vv15]

- **Fact:** Thư viện `shutil` trong Python cung cấp hàm `make_archive()` để nén toàn bộ một thư mục thành một tệp lưu trữ (archive) như định dạng `.zip`.
- **Source:** (v15 - Section: Script chi tiết cho Google Colab - Bước 2)
- **Tag:** [vv15]

- **Fact:** Dữ liệu thực tế cho thấy các tài liệu về "AI Arduino" (ví dụ: "Đề 2 trắc nghiệm - AI Arduino.docx") có dung lượng khoảng 10.6 MB và chứa các thành phần đa phương tiện trong cấu trúc tệp.
- **Source:** (v15 - Section: USER: Đề 2 trắc nghiệm - AI Arduino.docx)
- **Tag:** [vv15]

- **Fact:** Để tự động hóa việc phân loại hình ảnh từ nhiều tệp tài liệu khác nhau, script Python có thể sử dụng `os.path.splitext(file_name)[0]` để lấy tên tệp gốc làm tên thư mục lưu trữ riêng biệt cho phần media của tệp đó.
- **Source:** (v15 - Section: Giải thích: 1. Tạo thư mục riêng)
- **Tag:** [vv15]