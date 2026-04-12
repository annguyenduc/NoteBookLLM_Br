Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v23:

- **Fact:** [CONV] Sử dụng kiểu dữ liệu liệt kê `enum` trong lập trình Arduino giúp quản lý và theo dõi các trạng thái của Servo (ví dụ: `OPEN`, `CLOSED`) một cách tường minh hơn so với việc sử dụng biến số nguyên hoặc boolean.
- **Source:** [v23] - Section: servo và vật cản.
- **Tag:** [vv23]

- **Fact:** [CONV] Công thức tính khoảng cách (cm) từ dữ liệu thời gian phản hồi (`duration`) của cảm biến siêu âm trong Arduino là: `distance_cm = duration * 0.034 / 2`.
- **Source:** [v23] - Hàm `loop()` trong các ví dụ mã nguồn Arduino.
- **Tag:** [vv23]

- **Fact:** [CONV] Trong lập trình Robot, PID (Proportional-Integral-Derivative) là một dạng điều khiển phản hồi được sử dụng để duy trì các thông số như vị trí, góc, hoặc tốc độ dựa trên sự sai khác giữa giá trị thực tế và giá trị mục tiêu.
- **Source:** [v23] - Section: PID trong lập trình robot là gì.
- **Tag:** [vv23]

- **Fact:** [CONV] Ba thành phần chính của bộ điều khiển PID bao gồm: **Proportional** (Tương ứng - điều chỉnh theo sai số hiện tại), **Integral** (Tích phân - loại bỏ sai số tích lũy theo thời gian), và **Derivative** (Đạo hàm - hạn chế dao động dựa trên tốc độ thay đổi sai số).
- **Source:** [v23] - Section: PID trong lập trình robot là gì (Mục 1, 2, 3).
- **Tag:** [vv23]

- **Fact:** [CONV] Thuật toán Dijkstra được sử dụng trong lập trình robot để tìm đường đi ngắn nhất từ một đỉnh xuất phát đến tất cả các đỉnh còn lại trong một đồ thị có trọng số không âm.
- **Source:** [v23] - Section: giải thích thuật toán dijkstra dễ hiểu nhất.
- **Tag:** [vv23]

- **Fact:** [CONV] Thuật toán "Wall Following" (Đi theo tường) là phương pháp điều khiển robot di chuyển song song với các cạnh của vật cản bằng cách sử dụng cảm biến siêu âm hoặc hồng ngoại để duy trì khoảng cách ổn định.
- **Source:** [v23] - Section: Thuật toán đi theo tường của robot.
- **Tag:** [vv23]

- **Fact:** [CONV] Thuật toán Pledge là một phương pháp điều hướng giúp robot thoát khỏi các mê cung đơn giản (không có vòng lặp không mong muốn) bằng cách kết hợp việc đi theo tường và theo dõi hướng di chuyển.
- **Source:** [v23] - Section: Thuật toán Pledge code thử cho tôi.
- **Tag:** [vv23]

- **Fact:** [CONV] Để phát hiện hướng di chuyển của tàu hỏa trên cùng một đường ray, có thể sử dụng hai cảm biến siêu âm đặt ở hai đầu; hệ thống sẽ kích hoạt Servo khi một trong hai cảm biến phát hiện vật cản dưới ngưỡng khoảng cách cho phép (threshold).
- **Source:** [v23] - Section: sử dụng 2 cảm biến siêu âm để phát hiện tàu đang đi từ hướng nào.
- **Tag:** [vv23]