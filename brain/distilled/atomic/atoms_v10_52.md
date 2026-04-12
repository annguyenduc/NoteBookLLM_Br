Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn cung cấp (Volume v10) liên quan đến thiết lập môi trường lập trình (Linux/Python) - nền tảng quan trọng cho AI và Robotics, cùng các kỹ thuật bổ trợ trình chiếu:

- **Fact:** Chế độ "Extend" (Win + P) cho phép máy chiếu hiển thị nội dung cố định trong khi người dùng có thể làm việc riêng trên màn hình chính mà không gây gián đoạn bài thuyết trình.
- **Source:** (vv10 - Section: Cách thiết lập "Extend" để máy chiếu hiển thị cố định)
- **Tag:** [vv10]

- **Fact:** Khi đang dùng máy chiếu, việc chuyển đổi màn hình ảo (`Win + Ctrl + Mũi tên`) sẽ khiến nội dung trên máy chiếu thay đổi theo, có thể gây gián đoạn nội dung đang trình chiếu.
- **Source:** (vv10 - Section: Những điều nên tránh khi dùng máy chiếu)
- **Tag:** [vv10]

- **Fact:** WSL (Windows Subsystem for Linux) là giải pháp chạy Ubuntu trực tiếp trên Windows mà không cần cài đặt máy ảo hay khởi động lại máy, tối ưu cho lập trình và tiết kiệm tài nguyên.
- **Source:** (vv10 - Section: 1. Dùng Windows Subsystem for Linux (WSL) – Cách dễ nhất)
- **Tag:** [vv10]

- **Fact:** Lệnh `wsl --install -d Ubuntu` trong PowerShell (quyền Admin) được sử dụng để tự động tải và cài đặt bản phân phối Ubuntu trên Windows.
- **Source:** (vv10 - Section: Cách cài đặt Ubuntu bằng WSL)
- **Tag:** [vv10]

- **Fact:** WSL 2 hỗ trợ chạy các ứng dụng Linux có giao diện đồ họa (GUI) như VS Code hoặc trình duyệt thông qua tính năng WSLg.
- **Source:** (vv10 - Section: Phương án tối ưu: Dùng Windows Subsystem for Linux (WSL 2) - Lưu ý)
- **Tag:** [vv10]

- **Fact:** Để thiết lập môi trường lập trình Python trên Ubuntu (WSL), cần cài đặt các gói `python3`, `python3-pip` và `python3-venv`.
- **Source:** (vv10 - Section: 1️⃣ Cài đặt Python trong WSL 2)
- **Tag:** [vv10]

- **Fact:** Môi trường ảo (venv) trong Python giúp giữ sạch môi trường code và tránh xung đột thư viện giữa các dự án khác nhau.
- **Source:** (vv10 - Section: 2️⃣ Cài đặt môi trường ảo (venv) để code Python)
- **Tag:** [vv10]

- **Fact:** Jupyter Notebook có thể chạy từ WSL và truy cập thông qua trình duyệt trên Windows bằng địa chỉ `http://localhost:8888` với tham số `--no-browser`.
- **Source:** (vv10 - Section: 3️⃣ Cài đặt Jupyter Notebook (nếu cần))
- **Tag:** [vv10]

- **Fact:** Extension "WSL" (hoặc Remote - WSL) trên VS Code cho phép lập trình viên mở trực tiếp thư mục mã nguồn từ môi trường Linux bằng lệnh `code .`.
- **Source:** (vv10 - Section: 4️⃣ Tích hợp WSL với VS Code để lập trình Python tiện hơn)
- **Tag:** [vv10]

- **Fact:** Lệnh `wsl --unregister <Distro>` (ví dụ: `wsl --unregister Debian`) sẽ xóa hoàn toàn một bản phân phối Linux và toàn bộ dữ liệu liên quan khỏi hệ thống WSL.
- **Source:** (vv10 - Section: 2️⃣ Xóa một bản phân phối cụ thể)
- **Tag:** [vv10]

- **Fact:** Lệnh `wsl -l -v` được sử dụng để kiểm tra danh sách các bản phân phối Linux đã cài đặt, trạng thái hoạt động và phiên bản WSL (1 hoặc 2) đang sử dụng.
- **Source:** (vv10 - Section: 1️⃣ Kiểm tra danh sách các bản Linux đang cài)
- **Tag:** [vv10]

- **Fact:** Cấu hình phần cứng có CPU đa nhân (ví dụ: 6 nhân 12 luồng) và GPU (ví dụ: GTX 1650) giúp WSL 2 và các máy ảo (VM) hoạt động mượt mà, hỗ trợ tốt cho các tác vụ tính toán và tăng tốc đồ họa.
- **Source:** (vv10 - Section: Đối với laptop của tôi. Bạn có lời khuyên nào trong 3 cách trên)
- **Tag:** [vv10]

- **Fact:** Một số ứng dụng trên Windows 11 (như ChatGPT, trình duyệt) có xu hướng tự động nhảy về màn hình chính khi mở cửa sổ mới dù đang ở màn hình ảo khác.
- **Source:** (vv10 - Section: USER: Tôi tạo nhiều màn hình ảo...)
- **Tag:** [vv10]

*Lưu ý: Các thông tin về YoloBit và Robotics cụ thể không xuất hiện trực tiếp trong văn bản raw nhưng WSL/Ubuntu/Python là các công cụ nền tảng để thực hiện các nhiệm vụ này.* [Unverified_Source]