---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v02_7
  title: CONV_atoms_v02_7
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v02 về IoT, YoloBit và Robotics:

- **Fact:** [CONV] Thuật toán EMA (Exponential Moving Average) giúp triệt tiêu nhiễu ánh sáng nhỏ, giúp giá trị cảm biến mượt hơn và tránh hiện tượng LED bị nhấp nháy.
- **Source:** [vv02] - Section 5: Tại sao thuật toán này tối ưu?
- **Tag:** [vv02]

- **Fact:** [CONV] Thuật toán Median-3 (lấy trung vị của 3 mẫu đo liên tiếp) giúp loại bỏ các giá trị đo sai biệt ("nhảy" số) do phản xạ bề mặt khi sử dụng cảm biến siêu âm.
- **Source:** [vv02] - Section 5: Tại sao thuật toán này tối ưu?
- **Tag:** [vv02]

- **Fact:** [CONV] Cơ chế Hysteresis (trễ) ngăn chặn việc thiết bị thay đổi trạng thái liên tục khi giá trị cảm biến dao động quanh ngưỡng (threshold).
- **Source:** [vv02] - Section 5: Tại sao thuật toán này tối ưu?
- **Tag:** [vv02]

- **Fact:** [CONV] Trong hiệu chuẩn ánh sáng, dải an toàn (gap) tối thiểu nên đặt là 120 hoặc bằng 10% dải đo thực tế (`0.1 * (L_bright - L_dark)`).
- **Source:** [vv02] - Section 6: Hiệu chuẩn nhanh
- **Tag:** [vv02]

- **Fact:** [CONV] Để lọc nhiễu đột biến (outlier), nếu độ chênh lệch giữa giá trị thô và giá trị EMA lớn hơn ngưỡng `L_outlier`, mẫu đó sẽ bị bỏ qua và không cập nhật vào EMA.
- **Source:** [vv02] - Phần giải thích về lọc nhiễu EMA và Outlier
- **Tag:** [vv02]

- **Fact:** [CONV] Trên board mạch Yolo UNO, chân D13 hỗ trợ xuất tín hiệu PWM (điều khiển độ sáng LED), trong khi chân D3 thường được dùng cho giao tiếp I2C SDA nên không được gán chức năng PWM trong firmware mặc định của OhStem.
- **Source:** [vv02] - Phần giải thích chân PWM trên Yolo UNO
- **Tag:** [vv02]

- **Fact:** [CONV] Khối lệnh "xuất ra giá trị analog" trên app.ohstem.vn chuẩn hóa giá trị đầu vào từ 0 đến 100 (tương ứng 0% - 100% công suất PWM).
- **Source:** [vv02] - Phần giải thích giá trị map 0-100 sang PWM
- **Tag:** [vv02]

- **Fact:** [CONV] Chỉ số Gamma (thường từ 1.4 đến 2.0) được áp dụng khi điều khiển LED để bù đắp đặc tính phi tuyến của mắt người, giúp cảm giác về độ sáng thay đổi tự nhiên hơn.
- **Source:** [vv02] - Section 3: Tính độ sáng LED theo môi trường
- **Tag:** [vv02]

- **Fact:** [CONV] Kiến trúc lập trình tối ưu cho AIoT là "không chặn" (non-blocking), sử dụng các bộ lập lịch sự kiện (timer) thay vì sử dụng lệnh tạm dừng (`delay`) dài để đảm bảo hệ thống phản hồi đa tác vụ.
- **Source:** [vv02] - Phần 10 tối ưu quan trọng: Mục 1 & 2
- **Tag:** [vv02]

- **Fact:** [CONV] Để tránh tình trạng "bão tin nhắn" (message storm) làm treo hệ thống IoT, dữ liệu cảm biến chỉ nên được gửi lên server định kỳ từ 5-15 giây hoặc chỉ gửi khi có sự thay đổi giá trị vượt ngưỡng quy định.
- **Source:** [vv02] - Phần 10 tối ưu quan trọng: Mục 5
- **Tag:** [vv02]

- **Fact:** [CONV] Cơ chế Fail-safe trong hệ thống AIoT cho phép thiết bị tự động chuyển về chế độ điều khiển bằng các luật logic cục bộ (if-else) nếu bị mất kết nối với server AI hoặc Internet.
- **Source:** [vv02] - Phần 10 tối ưu quan trọng: Mục 7
- **Tag:** [vv02]

- **Fact:** [CONV] Giá trị ADC của cảm biến ánh sáng trên Yolo UNO thường nằm trong dải từ 0 (tối) đến 4095 (sáng).
- **Source:** [vv02] - Bảng biến cho cảm biến ánh sáng (LDR)
- **Tag:** [vv02]