Dưới đây là các sự kiện kỹ thuật về IoT, Arduino, AI và mBlock được trích xuất từ nguồn dữ liệu Volume v07:

- **Fact:** [CONV] Trong chế độ Live mode của mBlock 5, các biến được tạo với tùy chọn "For all sprites" (biến toàn cục) có thể được chia sẻ và sử dụng chung giữa phần giao diện (Sprites) và phần cứng (Devices như Arduino Uno).
- **Source:** [v07 - Conversation: Thuật toán mBlock5 LED - Section: Cách làm đúng (Live mode)]
- **Tag:** [vv07]

- **Fact:** [CONV] Khối lệnh "digital write pin [D] [HIGH/LOW]" trong mBlock 5 sử dụng menu chọn cố định cho trạng thái HIGH/LOW, không cho phép lồng trực tiếp các biến số vào vị trí này.
- **Source:** [v07 - Conversation: Thuật toán mBlock5 LED - Section: D3 = (blinkState) không lồng các khối block này vào nhau được]
- **Tag:** [vv07]

- **Fact:** [CONV] mBlock 5 không hỗ trợ khối lệnh "else if" trực tiếp; người dùng phải thực hiện logic rẽ nhánh nhiều điều kiện bằng cách lồng các khối "if-else" vào nhau.
- **Source:** [v07 - Conversation: Thuật toán mBlock5 LED - Section: mblock cũng không có khối else if mà chỉ có if - else]
- **Tag:** [vv07]

- **Fact:** [CONV] Để lập trình hiệu ứng chớp tắt LED mà không gây trễ (delay) cho các sự kiện điều khiển khác, kỹ thuật sử dụng khối "timer" để kiểm tra thời gian và đảo trạng thái biến (ví dụ: `1 - blinkState`) được ưu tiên hơn khối lệnh "wait".
- **Source:** [v07 - Conversation: Thuật toán mBlock5 LED - Section: Lý do dùng timer thay vì wait]
- **Tag:** [vv07]

- **Fact:** [CONV] Extension Teachable Machine trên mBlock yêu cầu trình duyệt (như Chrome) phải cho phép cửa sổ bật lên (pop-up) và quyền truy cập Camera để có thể mở trang huấn luyện mô hình (Model Training page).
- **Source:** [v07 - Conversation: Thuật toán mBlock5 LED - Section: Tôi không sử dụng được extension teachable machine]
- **Tag:** [vv07]

- **Fact:** [CONV] Extension "Machine Learning 2.0" (hỗ trợ Image/Audio/Pose) là một phương án thay thế tích hợp sẵn trong mBlock, giúp thu thập dữ liệu và huấn luyện AI ngay trong ứng dụng mà ít phụ thuộc vào cửa sổ pop-up bên ngoài.
- **Source:** [v07 - Conversation: Thuật toán mBlock5 LED - Section: 7) Phương án thay thế khi TM vẫn trục trặc]
- **Tag:** [vv07]

- **Fact:** [CONV] Khi điều khiển LED bằng Arduino, cần kết nối theo sơ đồ: Chân Pin số → điện trở (220–330Ω) → chân dương LED; chân âm LED nối vào GND.
- **Source:** [v07 - Conversation: Thuật toán mBlock5 LED - Section: Mục tiêu & chế độ chạy]
- **Tag:** [vv07]

- **Fact:** [CONV] Trong lập trình thiết bị (Device) trên mBlock, việc thiết lập chế độ chân (set pin mode) thành "OUTPUT" là bước bắt buộc trước khi thực hiện lệnh ghi tín hiệu (digital write).
- **Source:** [v07 - Conversation: Thuật toán mBlock5 LED - Section: Lỗi hay gặp & cách tránh]
- **Tag:** [vv07]