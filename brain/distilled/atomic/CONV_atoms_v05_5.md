Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v05) về chủ đề máy in 3D Neptune 4, OctoPrint và thiết lập Slicer:

- **Fact:** [CONV] [Thông số cấu hình Printer Profile cho Neptune 4: Hình dạng Rectangular, Bàn nhiệt (Heated Bed) 225 × 225 mm, Chiều cao 265 mm, Gốc tọa độ (Origin) ở Lower Left, Nozzle mặc định 0.4 mm.]
- **Source:** [DỮ LIỆU RAW - Mục 3: Printer Profile]
- **Tag:** [vv05]

- **Fact:** [CONV] [Kết nối Serial cho máy in thường sử dụng cổng /dev/ttyACM0 hoặc /dev/ttyUSB0 với Baudrate phổ biến là 250000 hoặc 115200.]
- **Source:** [DỮ LIỆU RAW - Mục 4: Serial Connection]
- **Tag:** [vv05]

- **Fact:** [CONV] [Địa chỉ IP dạng 169.254.x.x (APIPA) trên máy in cho thấy thiết bị không lấy được IP từ DHCP (lỗi kết nối mạng), cần kiểm tra lại cấu hình Wi-Fi hoặc cáp LAN.]
- **Source:** [DỮ LIỆU RAW - Phần: Cách 2 — Cấu hình Wi-Fi dongle đúng cách]
- **Tag:** [vv05]

- **Fact:** [CONV] [Máy in Neptune 4 chạy firmware Klipper nhưng không tích hợp sẵn Wi-Fi; để dùng Wi-Fi cần USB Dongle tương thích (ví dụ TP-Link TL-WN725N chipset Realtek 8188EUS) và nạp file cấu hình wpa_supplicant-wlan0.conf.]
- **Source:** [DỮ LIỆU RAW - Phần: Cách 2 / Vì sao chắc Neptune 4...]
- **Tag:** [vv05]

- **Fact:** [CONV] [Khoảng cách khe hở khớp (joint clearance) trong in 3D bị ảnh hưởng bởi Horizontal Expansion: giá trị dương (+) làm khe nhỏ lại, giá trị âm (-) làm khe rộng ra.]
- **Source:** [DỮ LIỆU RAW - Phần: Những thông số ảnh hưởng trực tiếp đến khe hở]
- **Tag:** [vv05]

- **Fact:** [CONV] [Chế độ Slicing Tolerance "Exclusive" giúp giữ khe hở hẹp tốt hơn so với "Inclusive" (dễ gây dính khớp).]
- **Source:** [DỮ LIỆU RAW - Phần: Những thông số ảnh hưởng trực tiếp đến khe hở]
- **Tag:** [vv05]

- **Fact:** [CONV] [Cách thêm Support Blocker trong Elegoo Cura: Chọn model -> Nhấp biểu tượng Support Blocker ở thanh công cụ bên trái -> Nhấp chuột vào vị trí trên model để tạo khối.]
- **Source:** [DỮ LIỆU RAW - Phần: A) Thêm Support Blocker]
- **Tag:** [vv05]

- **Fact:** [CONV] [Để tùy chỉnh thông số cho một vùng cục bộ (modifier), chọn Support Blocker và chuyển Mesh Type sang "Modify settings for overlaps" trong phần Per-Model Settings.]
- **Source:** [DỮ LIỆU RAW - Phần: B) Biến Support Blocker thành “modifier”]
- **Tag:** [vv05]

- **Fact:** [CONV] [Lỗi không thể Slice "all set as modifier meshes" thường do người dùng thiết lập nhầm model chính thành dạng modifier thay vì "Normal Model".]
- **Source:** [DỮ LIỆU RAW - Phần: Cách sửa nhanh (60 giây)]
- **Tag:** [vv05]

- **Fact:** [CONV] [Tính năng "Elephant Foot Compensation" (bù chân voi) giúp ngăn chặn việc các lớp in đầu tiên bị bè ra gây dính hoặc kẹt khe hở ở mặt đáy chi tiết.]
- **Source:** [DỮ LIỆU RAW - Phần: 2) Ảnh hưởng Z / lớp đầu]
- **Tag:** [vv05]