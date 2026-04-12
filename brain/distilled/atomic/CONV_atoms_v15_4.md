Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu v15 theo quy tắc LOM v4.1:

- **Fact:** [CONV] Cấu trúc tệp `.docx` thực chất là một định dạng nén; các hình ảnh nhúng trong tài liệu được lưu trữ tại thư mục nội bộ `word/media`.
- **Source:** [vv15 - Section: Cách thực hiện / Lưu ý giải nén folder media]
- **Tag:** [vv15]

- **Fact:** [CONV] Thư viện `python-docx` được sử dụng để đọc cấu trúc tài liệu Word, cho phép truy cập các đoạn văn (`paragraphs`) và các đối tượng đồ họa thông qua `xpath` với định danh `.//w:drawing`.
- **Source:** [vv15 - Section: Script Python trên Google Colab / rename_images_by_question]
- **Tag:** [vv15]

- **Fact:** [CONV] Trong môi trường Google Colab, thư viện `python-docx` không có sẵn mặc định và phải được cài đặt thông qua lệnh `!pip install python-docx`.
- **Source:** [vv15 - Section: Lỗi ModuleNotFoundError]
- **Tag:** [vv15]

- **Fact:** [CONV] Có thể lập trình để tự động đổi tên hình ảnh trích xuất từ Word dựa trên nội dung văn bản đi kèm (ví dụ: số thứ tự câu hỏi bắt đầu bằng từ khóa "Câu").
- **Source:** [vv15 - Section: rename_images_by_question]
- **Tag:** [vv15]

- **Fact:** [CONV] Lỗi `PackageNotFoundError` trong thư viện `docx` xảy ra khi đường dẫn tệp tin cung cấp không tồn tại hoặc tệp tin không đúng định dạng gói OpenXML.
- **Source:** [vv15 - Section: Lỗi PackageNotFoundError]
- **Tag:** [vv15]

- **Fact:** [CONV] Thư viện `zipfile` của Python cho phép trích xuất chọn lọc (selective extraction) các tệp tin cụ thể từ một tệp nén (như `.docx`) mà không cần giải nén toàn bộ nội dung.
- **Source:** [vv15 - Section: extract_media]
- **Tag:** [vv15]

- **Fact:** [CONV] Crawl data (Web Crawling/Scraping) là quá trình tự động thu thập dữ liệu từ trang web bằng các chương trình gọi là "crawlers" hoặc "spiders" để phục vụ lập chỉ mục tìm kiếm hoặc phân tích dữ liệu.
- **Source:** [vv15 - Section: Crawl data nghĩa là gì?]
- **Tag:** [vv15]

- **Fact:** [CONV] `google.colab.files` cung cấp các phương thức `upload()` và `download()` để tương tác với hệ thống tệp tin cục bộ của người dùng từ môi trường đám mây Colab.
- **Source:** [vv15 - Section: Script Python trên Google Colab]
- **Tag:** [vv15]

- **Fact:** [CONV] Việc nén thư mục dữ liệu thành tệp `.zip` trong Python có thể thực hiện nhanh chóng bằng hàm `shutil.make_archive()`.
- **Source:** [vv15 - Section: Script Python trên Google Colab]
- **Tag:** [vv15]

- **Fact:** [CONV] Các ứng dụng AI và Arduino thường được tích hợp trong các bộ đề trắc nghiệm kỹ thuật (ví dụ: "Đề 4 trắc nghiệm - AI Arduino.docx").
- **Source:** [vv15 - Section: PackageNotFoundError]
- **Tag:** [vv15]