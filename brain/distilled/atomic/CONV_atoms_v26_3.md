Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v26) theo quy tắc LOM v4.1:

- **Fact:** [CONV] Servo được sử dụng trong robot giáo dục để điều khiển các cơ cấu mô phỏng nhiệm vụ Mars Rover như: thu thập mẫu đất, nâng hạ vật thể, mở cửa, vặn vít và đào hố trên sa bàn giấy.
- **Source:** [vv26 - Section: Ý tưởng 11-15 và các bộ ý tưởng 1-5 cho Mars Rover]
- **Tag:** [vv26]

- **Fact:** [CONV] Robot mô phỏng Mars Rover thường tích hợp cảm biến siêu âm (ultrasonic sensor) để nhận biết vật cản và cảm biến dò line để điều hướng di chuyển trên sa bàn.
- **Source:** [vv26 - Section: USER prompt về robot giáo dục]
- **Tag:** [vv26]

- **Fact:** [CONV] Thuật toán Gradient Descent tìm điểm cực tiểu của hàm số bằng cách cập nhật giá trị biến theo công thức: $x_{new} = x_{old} - \eta \cdot \nabla f(x)$, trong đó $\eta$ là tỷ lệ học (learning rate).
- **Source:** [vv26 - Section: Conversation: Gradient Descent for f]
- **Tag:** [vv26]

- **Fact:** [CONV] Đạo hàm riêng (gradient) của hàm số $z = f(x, y) = x^2 + \sin(y)$ là $\nabla z = [2x, \cos(y)]$.
- **Source:** [vv26 - Section: Conversation: Gradient Descent for f]
- **Tag:** [vv26]

- **Fact:** [CONV] Thư viện `plotly.graph_objects` kết hợp với `numpy` cho phép vẽ bề mặt 3D (`go.Surface`) và các điểm dữ liệu trong không gian 3 chiều (`go.Scatter3d`) để trực quan hóa quá trình tối ưu hóa.
- **Source:** [vv26 - Section: Sử dụng plotly.graph_objects và numpy]
- **Tag:** [vv26]

- **Fact:** [CONV] Thuật toán Gradient Descent Momentum cải tiến thuật toán cơ bản bằng cách thêm biến vận tốc ($v$) và hệ số momentum ($\gamma$) để tăng tốc độ hội tụ: $v_{new} = \eta \cdot \text{grad} + \gamma \cdot v_{old}$.
- **Source:** [vv26 - Section: def gradient_descent_momentum]
- **Tag:** [vv26]

- **Fact:** [CONV] Trong lập trình Python, hàm `np.meshgrid` được sử dụng để tạo lưới tọa độ từ các mảng một chiều, phục vụ việc tính toán giá trị hàm số trên một miền không gian (ví dụ: miền $[[-1, 1], [-2\pi, 2\pi]]$).
- **Source:** [vv26 - Section: Giải thích đoạn code chi tiết]
- **Tag:** [vv26]

- **Fact:** [CONV] Các cơ cấu robot dành cho học sinh khối 6 được thiết kế để sử dụng Servo độc lập, không phụ thuộc vào cảm biến phức tạp khác nhằm đảm bảo tính dễ thực hiện và bảo vệ sa bàn giấy.
- **Source:** [vv26 - Section: Ý tưởng 1-5 (Robot giáo dục)]
- **Tag:** [vv26]