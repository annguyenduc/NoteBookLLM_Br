Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume 04:

- **Fact:** Lỗi cổng COM bị chiếm dụng (bận) thường do các ứng dụng như Arduino IDE, VS Code (Serial Monitor/PlatformIO), hoặc các công cụ flash ESP đang chạy nền.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (A. Giải phóng COM5)]
- **Tag:** [vv04]

- **Fact:** Các cổng Bluetooth (thường từ COM3 đến COM9) có thể gây nhiễu và làm rối loạn việc lựa chọn cổng kết nối chính xác cho thiết bị IoT trên Windows.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (B. Giảm nhiễu vì cổng Bluetooth)]
- **Tag:** [vv04]

- **Fact:** Có thể sử dụng **Resource Monitor** (tab CPU -> Associated Handles) để tìm và đóng các tiến trình (process) đang giữ cổng COM cụ thể.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (A. Giải phóng COM5 - Bước 2)]
- **Tag:** [vv04]

- **Fact:** Để khắc phục lỗi cổng bận, người dùng có thể đổi số cổng COM trong **Device Manager** (Port Settings -> Advanced) sang một số mới như COM11, COM12.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (A. Giải phóng COM5 - Bước 4)]
- **Tag:** [vv04]

- **Fact:** Trình duyệt Chrome và Edge hỗ trợ giao thức **Web Serial** để kết nối trực tiếp với phần cứng qua cổng COM, yêu cầu cấp quyền trong Site Settings.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (C. Thiết lập trên trình duyệt)]
- **Tag:** [vv04]

- **Fact:** Bo mạch Yolo:bit thường sử dụng chip giao tiếp USB-to-Serial là **CH340**; driver tương ứng cần được cài đặt để Windows nhận diện thiết bị.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (D. Kiểm tra nhanh phần cứng/driver)]
- **Tag:** [vv04]

- **Fact:** Một số dòng Yolo:bit có thể hiển thị dưới tên **Espressif CDC Device** thay vì CH340 tùy thuộc vào firmware đang chạy.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (A) Lấy lại cổng “sạch”)]
- **Tag:** [vv04]

- **Fact:** Để đưa Yolo:bit vào chế độ **Download/Bootloader**, cần giữ nút **BOOT (IO0)**, nhấn và nhả nút **RESET**, sau đó đợi 1-2 giây rồi mới nhả nút BOOT.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (B) Khôi phục đúng giao diện USB - Bước 2)]
- **Tag:** [vv04]

- **Fact:** Firmware của Yolo:bit có thể được nạp lại bằng công cụ của OhStem hoặc **esptool** với các địa chỉ bộ nhớ chuẩn là 0x1000 (bootloader), 0x8000 (partitions), và 0x10000 (firmware).
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (B) Khôi phục đúng giao diện USB - Bước 2)]
- **Tag:** [vv04]

- **Fact:** Tốc độ Baud (Baud rate) chuẩn để kiểm tra kết nối Serial với các thiết bị này thường là **115200**.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (E. Test độc lập)]
- **Tag:** [vv04]

- **Fact:** Ứng dụng **KidsUp** tích hợp phương pháp Montessori để dạy trẻ học toán tư duy, nhận biết số và phép tính trong phạm vi 50.
- **Source:** [v04 - Section: Hướng dẫn học toán trẻ 3 tuổi - ASSISTANT (Phương pháp Tích hợp)]
- **Tag:** [vv04]

- **Fact:** Máy in 3D **Neptune 4** có các thông số cài đặt in cụ thể, bao gồm cả chế độ chỉ in phần infill.
- **Source:** [v04 - Section: Phân tích thông minh từ Smart Proxy]
- **Tag:** [vv04]