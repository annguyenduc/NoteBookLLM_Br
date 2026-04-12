Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu Volume v19 liên quan đến tự động hóa, lập trình Google Apps Script và quy trình hệ thống:

- **Fact:** [CONV] Trong Google Apps Script (GAS) dành cho Google Slides, đối tượng slide không có phương thức `.duplicate()` trực tiếp; để sao chép, lập trình viên cần sử dụng `DriveApp` để nhân bản toàn bộ tệp hoặc lặp qua từng phần tử để sao chép thủ công.
- **Source:** [vv19] - Section: ASSISTANT response to "TypeError: sourceSlide.duplicate is not a function"
- **Tag:** [vv19]

- **Fact:** [CONV] Để tạo một slide mới trong bản trình diễn đích dựa trên bố cục của slide nguồn, sử dụng phương thức `destinationPresentation.appendSlide(sourceSlide.getLayout())`.
- **Source:** [vv19] - Section: ASSISTANT response to "TypeError: sourceSlides[i].getMaster is not a function"
- **Tag:** [vv19]

- **Fact:** [CONV] Việc sao chép các hình khối (shapes) giữa các slide yêu cầu truy xuất thuộc tính loại (`getType`), vị trí (`getLeft`, `getTop`) và kích thước (`getWidth`, `getHeight`) để tái tạo bằng `insertShape()`.
- **Source:** [vv19] - Section: ASSISTANT response to "TypeError: sourceSlides[i].getMaster is not a function"
- **Tag:** [vv19]

- **Fact:** [CONV] ID của một bản trình diễn Google Slides được xác định là chuỗi ký tự nằm giữa `/d/` và `/edit` trong địa chỉ URL của trình duyệt.
- **Source:** [vv19] - Section: ASSISTANT response to "ID của google slide"
- **Tag:** [vv19]

- **Fact:** [CONV] Lỗi "Exception: The object could not be found" trong GAS thường xảy ra khi truy cập một slide không tồn tại hoặc ID không hợp lệ; giải pháp khuyến nghị là sử dụng `getSlideById()` để kiểm tra sự tồn tại trước khi thao tác.
- **Source:** [vv19] - Section: ASSISTANT response to "Exception: The object (g249a8dc305e_0_70) could not be found."
- **Tag:** [vv19]

- **Fact:** [CONV] Google Apps Script có thể gặp vấn đề không đồng bộ (asynchrony) với các thay đổi trên trình duyệt, đôi khi cần tải lại trình duyệt hoặc tạm dừng trước khi thực thi lại mã.
- **Source:** [vv19] - Section: ASSISTANT response to "Exception: The object (g22540e2e6d0_0_70) could not be found."
- **Tag:** [vv19]

- **Fact:** [CONV] Quy trình kiểm tra (audit) cho một nền tảng học tập cần phân định rõ 3 vai trò chính: Người Kiểm Tra (Checker), Người Ghi Nhận (Recorder), và Người Điều Phối (Coordinator).
- **Source:** [vv19] - Section: ASSISTANT response to "Tôi muốn làm một quy trình kiểm tra lại platform học toán."
- **Tag:** [vv19]

- **Fact:** [CONV] Một template kiểm tra lời giải toán học tiêu chuẩn bao gồm các tiêu chí: Tính đúng đắn của kết quả, độ chi tiết/logic của bước giải, tính phù hợp của công thức sử dụng và cấu trúc trình bày.
- **Source:** [vv19] - Section: ASSISTANT response to "Tôi muốn làm một quy trình kiểm tra lại platform học toán... viết cho tôi một template"
- **Tag:** [vv19]

- **Fact:** [CONV] Trong GAS, để di chuyển một bản trình diễn mới tạo vào thư mục cụ thể trên Drive, có thể sử dụng `DriveApp.getFolderById(destinationFolderId).createFile(duplicateFile.getBlob())`.
- **Source:** [vv19] - Section: ASSISTANT response to "Exception: The object (g22540e2e6d0_0_70) could not be found."
- **Tag:** [vv19]

- **Fact:** [CONV] Phương thức `setTrashed(true)` trong DriveApp được sử dụng để xóa hoặc đưa tệp vào thùng rác sau khi hoàn tất các thao tác xử lý tạm thời bằng script.
- **Source:** [vv19] - Section: ASSISTANT response to "TypeError: sourceSlide.duplicate is not a function"
- **Tag:** [vv19]