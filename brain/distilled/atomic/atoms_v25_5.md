Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu RAW (Volume v25) về AI, Robotics và lập trình:

- **Fact:** Hàm `np.where` trong NumPy được sử dụng để phân loại mẫu dựa trên ngưỡng (threshold). Ví dụ: nếu xác suất dự đoán lớp 1 lớn hơn ngưỡng, mẫu được gán nhãn là 3, ngược lại là 2.
- **Source:** [vv25] - Section: y_pred = np.where(y_pred_prob[:, 1] > threshold, 3, 2) giải thích.
- **Tag:** [vv25]

- **Fact:** Trong bài toán phân loại Iris với 3 đặc trưng, Decision Boundary là một mặt phẳng được xác định bởi phương trình: $w_1x_1 + w_2x_2 + w_3x_3 + bias = 0$.
- **Source:** [vv25] - Section: dùng thư viện plotly để vẽ và sử dụng Vẽ decision boundary.
- **Tag:** [vv25]

- **Fact:** Thư viện Plotly có thể vẽ Decision Boundary 3D bằng cách tạo lưới dữ liệu (meshgrid) và sử dụng hàm `go.Surface` kết hợp với `go.Scatter3d` để hiển thị các điểm dữ liệu.
- **Source:** [vv25] - Section: dùng thư viện plotly để vẽ và sử dụng Vẽ decision boundary.
- **Tag:** [vv25]

- **Fact:** Lỗi `ModuleNotFoundError: No module named 'torch'` xảy ra khi thư viện PyTorch chưa được cài đặt. Có thể cài đặt bằng lệnh `pip install torch` hoặc `conda install pytorch`.
- **Source:** [vv25] - Section: ModuleNotFoundError Traceback.
- **Tag:** [vv25]

- **Fact:** Sự khác biệt giữa `flatten()` và `ravel()` trong NumPy: `flatten()` trả về một bản sao (copy) độc lập, trong khi `ravel()` trả về một view (chỉ nhìn) trỏ đến dữ liệu gốc; thay đổi trên `ravel()` sẽ ảnh hưởng đến mảng gốc.
- **Source:** [vv25] - Section: flatten với ravel khác nhau chỗ nào.
- **Tag:** [vv25]

- **Fact:** Cảm biến ánh sáng trên Robot Mars Rover có thể dùng để phân loại vật liệu dựa trên mức độ phản xạ, tìm kiếm nguồn sáng trong hang động hoặc điều khiển năng lượng (tắt hệ thống khi ánh sáng thấp).
- **Source:** [vv25] - Section: Robot Mô Phỏng Sa Bàn.
- **Tag:** [vv25]

- **Fact:** Cảm biến nhiệt độ trên Robot giáo dục có thể dùng để xác định vùng khí hậu, tìm kiếm điểm nóng (núi lửa, dòng dung nham) hoặc đo khả năng dẫn nhiệt của vật liệu trên sa bàn.
- **Source:** [vv25] - Section: Robot Mô Phỏng Sa Bàn.
- **Tag:** [vv25]

- **Fact:** Robot có thể sử dụng cảm biến nhiệt độ để suy ra thông tin về độ ẩm môi trường thông qua việc nhận biết các sự thay đổi nhiệt độ không thường xuyên.
- **Source:** [vv25] - Section: Robot Mô Phỏng Sa Bàn - Ý tưởng 12.
- **Tag:** [vv25]

- **Fact:** Trong giáo dục Robot, kiến thức về "Biến số" có thể được lồng ghép thông qua việc đọc giá trị từ cảm biến ánh sáng và nhiệt độ để điều khiển hành vi của Robot.
- **Source:** [vv25] - Section: Chuyên gia về đặt tên cho bài học Robot.
- **Tag:** [vv25]

- **Fact:** Một kịch bản học tập Robot thú vị thường bao gồm cốt truyện: Rover thám hiểm Sao Hỏa, làm quen với khí hậu/địa hình và thực hiện nhiệm vụ lập trình di chuyển cơ bản.
- **Source:** [vv25] - Section: Chuyên gia về đặt tên cho bài học Robot (phần cuối).
- **Tag:** [vv25]