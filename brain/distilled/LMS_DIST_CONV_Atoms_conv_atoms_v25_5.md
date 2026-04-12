---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v25_5
  title: CONV_atoms_v25_5
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu RAW (Volume v25) về AI, Robotics và lập trình:

- Fact: [CONV] Hàm `np.where` được sử dụng để phân loại mẫu vào các lớp (ví dụ: lớp 2 hoặc lớp 3) bằng cách so sánh xác suất dự đoán của mô hình với một ngưỡng (threshold) nhất định.
- Source: [vv25] - Section: y_pred = np.where(...) giải thích
- Tag: [vv25]

- Fact: [CONV] Để vẽ decision boundary cho bài toán phân loại Iris với 3 đặc trưng, có thể sử dụng mặt phẳng được xác định bởi phương trình $w_1x_1 + w_2x_2 + w_3x_3 + bias = 0$.
- Source: [vv25] - Section: dùng thư viện plotly để vẽ và sử dụng Vẽ decision boundary
- Tag: [vv25]

- Fact: [CONV] Trong thư viện NumPy, `flatten()` trả về một bản sao (copy) của mảng gốc, trong khi `ravel()` trả về một "view" (chỉ nhìn) dẫn đến việc thay đổi giá trị trên mảng `ravel` sẽ làm thay đổi mảng gốc.
- Source: [vv25] - Section: flatten với ravel khác nhau chỗ nào
- Tag: [vv25]

- Fact: [CONV] Cảm biến nhiệt độ trên robot mô phỏng (Mars Rover) có thể được sử dụng để xác định các vùng nhiệt độ khác nhau, tìm kiếm điểm nóng (núi lửa, dòng dung nham) hoặc đo khả năng dẫn nhiệt của vật liệu trên sa bàn.
- Source: [vv25] - Section: Robot Mô Phỏng Sa Bàn (Ý tưởng 2, 3, 11)
- Tag: [vv25]

- Fact: [CONV] Cảm biến ánh sáng có thể giúp robot tự động điều chỉnh hướng di chuyển để tận dụng nguồn sáng tốt nhất hoặc điều khiển tiết kiệm năng lượng bằng cách tắt hệ thống khi ánh sáng thấp.
- Source: [vv25] - Section: Robot Mô Phỏng Sa Bàn (Ý tưởng 5, 7)
- Tag: [vv25]

- Fact: [CONV] Việc cài đặt thư viện PyTorch (`torch`) có thể thực hiện thông qua lệnh `pip install torch` hoặc `conda install pytorch` tùy thuộc vào môi trường quản lý gói đang sử dụng.
- Source: [vv25] - Section: ModuleNotFoundError: No module named 'torch'
- Tag: [vv25]

- Fact: [CONV] Robot mô phỏng có thể sử dụng cảm biến ánh sáng để đo lường quang phổ của môi trường, từ đó phân tích thành phần hóa học hoặc dấu hiệu sự sống trên sa bàn giấy.
- Source: [vv25] - Section: Robot Mô Phỏng Sa Bàn (Ý tưởng 6)
- Tag: [vv25]

- Fact: [CONV] Trong VSCode, để cài đặt thư viện mới, người dùng cần mở terminal tích hợp (Ctrl + `), kích hoạt môi trường ảo và chọn đúng trình thông dịch Python (interpreter) ở góc dưới bên trái cửa sổ.
- Source: [vv25] - Section: nếu tôi đang sử dụng vscode thì sao
- Tag: [vv25]