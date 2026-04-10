# 💻 DevOps & IT Automation Wiki (Master)

> **Mô tả**: Tổng hợp các giải pháp lập trình Python, quản trị hệ thống Windows/Network và các kịch bản tự động hóa (Automation) được tích lũy từ thực tế vận hành.

## 1. 🐍 Python Development & Best Practices
- **Coding Style**: Áp dụng DRY (Don't Repeat Yourself), đặt tên biến gợi nhớ, và ưu tiên self-documenting code.
- **Thuật toán cốt lõi**: Phân biệt Loop (while vs for), kỹ thuật đệ quy (Recursion) và tối ưu hóa hiệu suất mã nguồn.
- **Xử lý lỗi**: Các lỗi phổ biến như `FileNotFoundError`, `ModuleNotFoundError` và cách debug nhanh trong VS Code.
- **Prompt Engineering**: Kỹ thuật viết prompt để AI chuyển đổi mã nguồn hoặc sinh code ESP8266/Python hiệu quả.

## 2. 🌐 Networking & IT Infrastructure
- **Networking Basics**: Kiến thức về IP Addressing, WAN/LAN Area loops, và xử lý sự cố kết nối Site-to-Site.
- **Power Shell & Terminal**: Các lệnh khởi chạy Gateway, quản lý Port (4000) và điều phối MCP Servers.
- **Windows Optimization**: Quản lý màn hình ảo (Win 11), giải phóng dung lượng SSD/RAM, và xử lý các lỗi driver USB/COM.

### SOP Phân tích Log & Quản trị Hệ thống
- **Phân tích Log (File Mining)**:
    - `tail -f /var/log/syslog`: Giám sát log thời gian thực.
    - `grep -i "error" logfile.txt`: Tìm kiếm lỗi (không phân biệt hoa thường).
    - `cut -d',' -f2 log.csv | sort | uniq -c`: Trích xuất cột, sắp xếp và đếm tần suất.
- **Quản lý Tiến trình & Signals**:
    - `top` hoặc `htop`: Giám sát tài nguyên hệ thống.
    - `kill -15 <pid>`: Gửi tín hiệu kết thúc nhẹ nhàng (Graceful shutdown).
    - `kill -9 <pid>`: Buộc dừng ngay lập tức (Force kill).

### SOP Kiểm thử Phần mềm (Testing)
- **Framework**: Ưu tiên **Pytest** vì tính linh hoạt và dễ đọc.
- **Error Handling**: 
    - Luôn sử dụng `try-except` cho các thao tác I/O hoặc API.
    - Sử dụng `pytest.raises` để kiểm tra các trường hợp bắt buộc phải văng lỗi.
- **Tổ chức file**: Tách biệt thư mục `src/` và `tests/`.

## 3. 🤖 Automation Scripts & Tools
- **Google Workspace**: Tự động hóa Google Form, script tạo file Excel từ Google Sheets, và quản lý lịch học qua Checkbox.
- **Web Scraping & Data**: Khái niệm Crawl data cơ bản và các kịch bản tự động click/chuông báo bằng Python.
- **Utilities**: Tool đăng ký Gmail, tạo định danh (ID) cho biến/đối tượng, và chuyển đổi định dạng tệp hàng loạt.

---
*Ghi chú: Nội dung được hợp nhất từ 49 tệp công nghệ & IT legacy.*
*Tham khảo chi tiết tại bộ lưu trữ Archive/v2_legacy.*
