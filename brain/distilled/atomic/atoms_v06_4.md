Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu về cấu hình in 3D cho dự án Robotics (Robot Strandbeest):

- **Fact:** Thiết lập in 3D cho các bộ phận robot Strandbeest trên máy Elegoo Neptune 4 (chạy Klipper) sử dụng hai mức độ phân giải lớp in (layer height) là 0.2mm (tiêu chuẩn) và 0.1mm (mịn).
- **Source:** [v06 - Section: DỮ LIỆU RAW - Fine 0.1 mm variants]
- **Tag:** [vv06]

- **Fact:** Thông số in cho chi tiết trục khuỷu (Crank) của robot yêu cầu bật Support Everywhere, Support Interface dày 0.8mm (khoảng 4 lớp ở độ phân giải 0.2mm), mật độ Interface 100% kiểu Lines và khoảng cách Z là 0.2mm để dễ bóc tách.
- **Source:** [v06 - Section: ASSISTANT response - Bước C & phần Support Interface]
- **Tag:** [vv06]

- **Fact:** Các chi tiết truyền động như bánh răng (Gear60) và kẹp quạt (Fanclip) yêu cầu độ bền cơ học cao với mật độ lấp đầy (Infill) từ 40% đến 50% kiểu Grid và sử dụng Brim 4mm để chống cong vênh.
- **Source:** [v06 - Section: ASSISTANT response - Bước C & GEAR_STRONG]
- **Tag:** [vv06]

- **Fact:** Cấu hình in nhựa PLA tối ưu cho linh kiện robot bao gồm: nhiệt độ vòi phun 206°C, bàn nhiệt 55°C, tốc độ rút nhựa (Retraction) 0.7mm ở 35mm/s và tốc độ in thành ngoài (Outer Wall) chậm ở mức 25mm/s để đảm bảo độ chính xác.
- **Source:** [v06 - Section: ASSISTANT response - Bước B — Điền thông số cho Strandbeest_BASE]
- **Tag:** [vv06]

- **Fact:** Để đảm bảo các khớp nối của robot (như phần chân - leg) không bị bó cứng do sai số lớp in đầu tiên, thông số 'Initial Layer Horizontal Expansion' được thiết lập giá trị âm (-0.20mm).
- **Source:** [v06 - Section: ASSISTANT response - Bước B — Điền thông số cho Strandbeest_BASE]
- **Tag:** [vv06]

- **Fact:** Danh sách linh kiện robot Strandbeest được phân loại theo mục đích sử dụng: nhóm BASE (leg, end, siderod, stand, fan), nhóm CRANK (trục khuỷu cần hỗ trợ) và nhóm GEAR (bánh răng chịu lực).
- **Source:** [v06 - Section: ASSISTANT response - 3) Dùng profile nào cho file nào]
- **Tag:** [vv06]