Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v23) theo quy tắc LOM v4.1:

- **Fact:** Công thức tính khoảng cách từ cảm biến siêu âm (đơn vị cm) dựa trên thời gian phản hồi là: `distance_cm = duration * 0.034 / 2`.
- **Source:** [vv23] - Section: servo và vật cản (Mã nguồn Arduino).
- **Tag:** [vv23]

- **Fact:** Sử dụng kiểu dữ liệu liệt kê (`enum`) trong lập trình Arduino giúp theo dõi và quản lý các trạng thái của thiết bị (ví dụ: trạng thái `OPEN`, `CLOSED` của Servo) một cách tường minh hơn so với sử dụng biến số nguyên hoặc boolean.
- **Source:** [vv23] - Section: servo và vật cản.
- **Tag:** [vv23]

- **Fact:** PID (Proportional-Integral-Derivative) là một dạng điều khiển phản hồi (feedback control) được sử dụng để duy trì hiệu suất hệ thống tự động thông qua việc đo lường sai khác giữa giá trị thực tế và mục tiêu.
- **Source:** [vv23] - Section: pid trong lập trình robot là gì.
- **Tag:** [vv23]

- **Fact:** Trong cơ chế PID, thành phần Integral (Tích phân) có vai trò loại bỏ sai số còn lại (steady-state error) sau một thời gian dài bằng cách tính tổng tích lũy của sai số.
- **Source:** [vv23] - Section: pid trong lập trình robot là gì.
- **Tag:** [vv23]

- **Fact:** Thành phần Derivative (Đạo hàm) trong PID giúp hạn chế dao động và tránh phản hồi không ổn định bằng cách điều chỉnh tỷ lệ nghịch với tốc độ thay đổi của sai số.
- **Source:** [vv23] - Section: pid trong lập trình robot là gì.
- **Tag:** [vv23]

- **Fact:** Thuật toán Dijkstra được sử dụng để tìm đường đi ngắn nhất từ một đỉnh xuất phát đến tất cả các đỉnh còn lại trong một đồ thị có trọng số không âm.
- **Source:** [vv23] - Section: giải thích thuật toán dijkstra dễ hiểu nhất.
- **Tag:** [vv23]

- **Fact:** Thuật toán "Wall Following" (Đi theo tường) là phương pháp điều khiển robot di chuyển song song với các cạnh của vật cản bằng cách sử dụng cảm biến siêu âm hoặc hồng ngoại để duy trì khoảng cách.
- **Source:** [vv23] - Section: thuật toán đi theo tường của robot.
- **Tag:** [vv23]

- **Fact:** Thuật toán Pledge là một phương pháp điều hướng robot thoát khỏi mê cung bằng cách làm quen dần với môi trường, thường áp dụng hiệu quả cho các mê cung đơn giản không có vòng lặp phức tạp.
- **Source:** [vv23] - Section: Thuật toán Pledge code thử cho tôi.
- **Tag:** [vv23]

- **Fact:** Để robot thoát khỏi mê cung hiệu quả hơn, có thể kết hợp thuật toán tránh vật cản với các thuật toán tìm đường tối ưu như A* (A-star) hoặc Dijkstra.
- **Source:** [vv23] - Section: tôi muốn môt thuật toán robot sử dụng cảm biến siêu âm để thoát khỏi mê cung.
- **Tag:** [vv23]

- **Fact:** Trong lập trình robot tránh vật cản trên lưới (grid) 2D, thuật toán Dijkstra có thể sử dụng hàng đợi ưu tiên (`priority_queue`) để quản lý việc duyệt các ô có khoảng cách nhỏ nhất.
- **Source:** [vv23] - Section: sử dụng thuật toán dijkstra với lập trình robot tránh vật cản dùng 1 cảm biến siêu âm.
- **Tag:** [vv23]