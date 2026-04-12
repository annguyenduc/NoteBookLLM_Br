---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v16_1
  title: atoms_v16_1
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v16) liên quan đến Google Colab, tự động hóa dữ liệu Robotics và xử lý tệp tin:

- **Fact:** Để chạy một cell cụ thể trong Google Colab và tự động chuyển sang cell tiếp theo, người dùng sử dụng tổ hợp phím `Shift + Enter`.
- **Source:** v16 - Section: Chạy từng cell (Mục 3).
- **Tag:** [vv16]

- **Fact:** Để chạy một cell mà không chuyển sang cell tiếp theo trong Google Colab, người dùng sử dụng tổ hợp phím `Ctrl + Enter`.
- **Source:** v16 - Section: Chạy từng cell (Mục 3).
- **Tag:** [vv16]

- **Fact:** Thư viện `gspread` được sử dụng trong môi trường Python để kết nối và thao tác dữ liệu trực tiếp với Google Sheets.
- **Source:** v16 - Section: Chú thích (Bước 1: Cài đặt thư viện).
- **Tag:** [vv16]

- **Fact:** Thư viện `patool` (hoặc `patoolib`) hỗ trợ giải nén nhiều định dạng tệp lưu trữ khác nhau bao gồm cả `.zip` và `.rar` trong môi trường Linux/Colab.
- **Source:** v16 - Section: ASSISTANT code (Phần kiểm tra định dạng file và giải nén).
- **Tag:** [vv16]

- **Fact:** Trong Google Drive API, các thư mục được định danh bằng MimeType là `application/vnd.google-apps.folder`.
- **Source:** v16 - Section: ASSISTANT code (Phần kiểm tra xem link là file hay folder).
- **Tag:** [vv16]

- **Fact:** Công cụ `gdown` cho phép tải toàn bộ thư mục từ Google Drive về môi trường Colab bằng cách sử dụng tham số `--folder` kèm theo URL thư mục.
- **Source:** v16 - Section: ASSISTANT code (Phần tải toàn bộ folder về máy).
- **Tag:** [vv16]

- **Fact:** Để tải tệp tin từ máy tính cá nhân lên Google Colab, sử dụng lệnh `from google.colab import files` và gọi hàm `files.upload()`.
- **Source:** v16 - Section: Sử dụng widget upload của Colab.
- **Tag:** [vv16]

- **Fact:** ID của một tệp tin hoặc thư mục trên Google Drive có thể được trích xuất từ URL thông qua các cấu trúc phổ biến như `/d/ID`, `folders/ID`, hoặc `open?id=ID`.
- **Source:** v16 - Section: ASSISTANT code (Hàm extract_id_from_url).
- **Tag:** [vv16]

- **Fact:** Việc xác thực quyền truy cập của người dùng vào các dịch vụ Google (Drive, Sheets) trong Colab được thực hiện qua lệnh `google.colab.auth.authenticate_user()`.
- **Source:** v16 - Section: ASSISTANT code (Bước 2: Xác thực và kết nối).
- **Tag:** [vv16]

- **Fact:** Google Colab hiện nay đã tích hợp Gemini (AI) trực tiếp vào môi trường lập trình để hỗ trợ giải thích code, sửa lỗi và tạo mã tự động.
- **Source:** [Dữ liệu v16 ghi nhận AI chưa biết về sự tích hợp này tại thời điểm đó].
- **Tag:** [Unverified_Source]