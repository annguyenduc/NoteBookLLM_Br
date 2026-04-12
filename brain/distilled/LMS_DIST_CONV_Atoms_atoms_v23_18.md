---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v23_18
  title: atoms_v23_18
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v23) liên quan đến phát triển ứng dụng AI, quản lý môi trường Python và triển khai dự án:

- **Fact:** Lệnh `cd ..` được sử dụng trong Terminal/Command Prompt để quay lại thư mục cha (thư mục trước đó).
- **Source:** (vv23 - Section: USER: cd gì để về thư mục trước)
- **Tag:** [vv23]

- **Fact:** Streamlit tìm kiếm tệp cấu hình bảo mật `secrets.toml` tại hai vị trí mặc định: thư mục `.streamlit` trong thư mục người dùng (User Profile) hoặc thư mục `.streamlit` ngay tại gốc của dự án.
- **Source:** (vv23 - Section: DỮ LIỆU RAW - Lỗi secrets.toml)
- **Tag:** [vv23]

- **Fact:** Để cài đặt hàng loạt các thư viện Python từ tệp danh sách (ví dụ: `libraries.txt`) trên Linux/macOS trong một dòng lệnh, có thể sử dụng: `xargs -a libraries.txt -n 1 pip install`.
- **Source:** (vv23 - Section: ASSISTANT: chạy các câu lệnh trên txt để cài đặt thư viện trong 1 dòng)
- **Tag:** [vv23]

- **Fact:** Trên Windows, lệnh để cài đặt thư viện từ file text theo vòng lặp là: `for /F "usebackq delims=" %i in (libraries.txt) do pip install %i`.
- **Source:** (vv23 - Section: ASSISTANT: chạy các câu lệnh trên txt để cài đặt thư viện trong 1 dòng)
- **Tag:** [vv23]

- **Fact:** Lệnh `pip list` dùng để liệt kê tất cả các thư viện đã cài đặt trong môi trường Python hiện tại, trong khi `pip show <tên_thư_viện>` dùng để kiểm tra thông tin chi tiết của một thư viện cụ thể.
- **Source:** (vv23 - Section: ASSISTANT: kiểm tra xem đã cài đặt thư viện nào)
- **Tag:** [vv23]

- **Fact:** Môi trường ảo (Virtual Environment) trong Python được tạo bằng lệnh `python -m venv venv` nhằm tránh xung đột phiên bản giữa các dự án.
- **Source:** (vv23 - Section: ASSISTANT: Tạo môi trường ảo (Virtual Environment))
- **Tag:** [vv23]

- **Fact:** Để cài đặt tất cả các phụ thuộc (dependencies) của một dự án Python từ tệp tiêu chuẩn, sử dụng lệnh: `pip install -r requirements.txt`.
- **Source:** (vv23 - Section: ASSISTANT: Cài đặt các thư viện từ requirements.txt)
- **Tag:** [vv23]

- **Fact:** Ứng dụng Streamlit được khởi chạy bằng lệnh `streamlit run <tên_file.py>` từ Terminal.
- **Source:** (vv23 - Section: ASSISTANT: Cách chạy Streamlit trực tiếp)
- **Tag:** [vv23]

- **Fact:** Tệp `.gitignore` được sử dụng để chỉ định các tệp hoặc thư mục (như `secrets.toml`, tệp log, thư mục build) mà Git không được theo dõi hoặc đưa vào lịch sử commit nhằm bảo mật và tối ưu dung lượng kho mã nguồn.
- **Source:** (vv23 - Section: ASSISTANT: .gitignore là gì trong dự án)
- **Tag:** [vv23]

- **Fact:** Trong Python, có thể thực hiện import thư viện động dựa trên tên chuỗi bằng cách sử dụng hàm `__import__(library_name)` hoặc module `importlib.util`.
- **Source:** (vv23 - Section: ASSISTANT: import thư viện trong txt)
- **Tag:** [vv23]

- **Fact:** Decorator `@st.cache_data` trong thư viện Streamlit được sử dụng để ghi nhớ (cache) kết quả của các hàm xử lý dữ liệu (như đọc file CSV), giúp tăng tốc độ tải lại trang web.
- **Source:** (vv23 - Section: USER: [Mã nguồn Streamlit mẫu])
- **Tag:** [vv23]

- **Fact:** Lỗi `FileNotFoundError: No secrets files found` trong Streamlit xảy ra khi mã nguồn yêu cầu truy cập thông tin từ `secrets.toml` nhưng tệp này không tồn tại hoặc sai đường dẫn.
- **Source:** (vv23 - Section: ASSISTANT: FileNotFoundError: No secrets files found làm sao sửa lỗi này)
- **Tag:** [vv23]