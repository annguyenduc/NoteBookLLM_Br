Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume 03 (v03) về các chủ đề IoT, Arduino, YoloBit, Robotics và AI:

- **Fact:** Máy in 3D Neptune 4 (bao gồm các dòng Plus, Max, Pro) có nhiệt độ vòi phun (nozzle) tối đa là 300 °C.
- **Source:** v03 - Conversation: Nhiệt độ sấy mực ẩm (ASSISTANT response)
- **Tag:** [vv03]

- **Fact:** Nhiệt độ chuyển thủy tinh (glass transition temperature) của nhựa in 3D loại PLA là khoảng 55 °C; nếu vượt quá mức này nhựa sẽ bị biến dạng hoặc dính lại.
- **Source:** v03 - Section: 1. Hiểu về giới hạn của PLA
- **Tag:** [vv03]

- **Fact:** Khi sấy cuộn nhựa PLA bị ẩm bằng bàn nhiệt (heatbed) của máy in 3D, nhiệt độ khuyến nghị an toàn là từ 45 °C – 50 °C trong khoảng 4 – 8 giờ.
- **Source:** v03 - Section: 2. Thiết lập an toàn trên Neptune 4
- **Tag:** [vv03]

- **Fact:** Cảm biến PIR (hồng ngoại thụ động) cần thời gian khởi động (warm-up) từ 20 – 60 giây sau khi cấp nguồn để ổn định tín hiệu.
- **Source:** v03 - Conversation: Giải thích cảm biến PIR (Mục 1: Cách PIR "đúng")
- **Tag:** [vv03]

- **Fact:** Logic hoạt động tiêu chuẩn của cảm biến PIR là: mức HIGH (1/True) khi phát hiện chuyển động và mức LOW (0/False) khi không có chuyển động.
- **Source:** v03 - Section: 0 là true, 1 là false đúng hay sai
- **Tag:** [vv03]

- **Fact:** Cảm biến vật cản hồng ngoại (IR Obstacle Sensor) hoạt động theo cơ chế active-LOW: trả về giá trị 0 (LOW) khi có vật cản và 1 (HIGH) khi không có vật cản do có mạch transistor đảo.
- **Source:** v03 - Section: 2. Vì sao IR vật cản cho ra 0 khi có vật cản?
- **Tag:** [vv03]

- **Fact:** Trên hệ sinh thái Yolo Uno/OhStem, cảm biến ánh sáng (LDR) trả về giá trị Analog trong khoảng 0 – 4095, với đặc điểm giá trị thấp khi ánh sáng mạnh và giá trị cao khi trời tối.
- **Source:** v03 - Section: BẢNG LOGIC TÍN HIỆU CẢM BIẾN THƯỜNG DÙNG VỚI YOLO UNO
- **Tag:** [vv03]

- **Fact:** Lệnh G-code `M140` dùng để đặt nhiệt độ bàn in (không chờ), trong khi lệnh `M190` yêu cầu máy in đợi cho đến khi bàn nhiệt đạt đúng nhiệt độ mục tiêu mới thực hiện lệnh tiếp theo.
- **Source:** v03 - Section: Create a G-code file (G-code comments)
- **Tag:** [vv03]

- **Fact:** Cảm biến ngọn lửa (Flame Sensor) và cảm biến va chạm (Touch/Collision) thường hoạt động theo logic active-LOW (trả về 0 khi phát hiện lửa hoặc khi bị nhấn).
- **Source:** v03 - Section: BẢNG LOGIC TÍN HIỆU CẢM BIẾN THƯỜNG DÙNG VỚI YOLO UNO
- **Tag:** [vv03]

- **Fact:** Để chống nhiễu (debounce) cho cảm biến PIR trên Yolo Uno, có thể sử dụng thuật toán yêu cầu đọc được cùng một giá trị liên tiếp (ví dụ 5 lần) trước khi xác nhận thay đổi trạng thái.
- **Source:** v03 - Section: 1) Bố cục khối chuẩn (Yolo UNO – D5)
- **Tag:** [vv03]