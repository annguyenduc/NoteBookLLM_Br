---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v04_6
  title: CONV_atoms_v04_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v04):

- **Fact:** [CONV] Excalidraw là công cụ ưu tiên cho việc vẽ sơ đồ và làm việc ngoại tuyến (offline), trong khi FigJam phù hợp cho các hoạt động cần tính năng bình chọn (vote), bộ đếm giờ (timer) và mẫu (template) sẵn có khi có mạng ổn định.
- **Source:** [v04 - Section: Kết luận nhanh]
- **Tag:** [vv04]

- **Fact:** [CONV] Padlet mạnh về thu thập ý tưởng dạng thẻ và hình ảnh nhưng yếu hơn Excalidraw/FigJam trong việc vẽ sơ đồ luồng (flowchart), sơ đồ khối và cây quyết định (decision tree).
- **Source:** [v04 - Section: So với Padlet]
- **Tag:** [vv04]

- **Fact:** [CONV] Quy trình brainstorm 60 phút cho dự án kỹ thuật/IoT bao gồm: Warm-up (5'), How Might We (10'), SCAMPER (10'), Sensor-Logic-Actuator Canvas (15'), Dot-vote (10') và Decision Tree mini (10').
- **Source:** [v04 - Section: Format hoạt động 60 phút (mẫu)]
- **Tag:** [vv04]

- **Fact:** [CONV] Một bản thiết kế hệ thống IoT (Sensor-Logic-Actuator Canvas) tiêu chuẩn cần tối thiểu 3 cảm biến, 2 cơ cấu chấp hành và phần logic phải thể hiện được các ngưỡng (threshold) và sai số trễ (hysteresis).
- **Source:** [v04 - Section: Format hoạt động 60 phút (mẫu) & Bộ template]
- **Tag:** [vv04]

- **Fact:** [CONV] Cây quyết định (Decision Tree) mini cho dự án Robotics/AI nên có từ 6–8 nút quyết định và phải bao gồm hộp Fail-safe với các tính năng như timeout, lockout, hoặc chế độ điều khiển thủ công (Manual).
- **Source:** [v04 - Section: Format hoạt động 60 phút (mẫu) & Bộ template]
- **Tag:** [vv04]

- **Fact:** [CONV] Tiêu chí kỹ thuật để tuyển chọn học sinh THPT (Bảng C) thi AI bao gồm: tư duy thuật toán, toán nền tảng (xác suất thống kê, ma trận), lập trình Python (NumPy, Pandas) và kiến thức AI/ML cơ bản (supervised/unsupervised, overfitting, metrics).
- **Source:** [v04 - Section: B) Năng lực & kỹ năng (70 điểm)]
- **Tag:** [vv04]

- **Fact:** [CONV] Cấu hình máy tính cá nhân khuyến nghị cho học sinh tham gia học và thi AI là CPU tối thiểu 4 nhân/8 luồng (4C/8T) và RAM từ 8GB đến 16GB.
- **Source:** [v04 - Section: A) Điều kiện tối thiểu]
- **Tag:** [vv04]

- **Fact:** [CONV] Trong Google Sheets, để tự động tạo danh sách tuần (ví dụ: 08/09 - 12/09), có thể sử dụng hàm `=ARRAYFORMULA(TEXT(Ngày_Bắt_Đầu + 7*SEQUENCE(1; Số_Tuần; 0; 1); "dd/mm") & " - " & TEXT(Ngày_Bắt_Đầu + 7*SEQUENCE(1; Số_Tuần; 0; 1) + 4; "dd/mm"))`.
- **Source:** [v04 - Section: Conversation: Google Sheets tự tạo tuần]
- **Tag:** [vv04]

- **Fact:** [CONV] Khi sử dụng Google Sheets với thiết lập Locale là Việt Nam, dấu phân tách các tham số trong hàm phải là dấu chấm phẩy (;) thay vì dấu phẩy (,).
- **Source:** [v04 - Section: Conversation: Google Sheets tự tạo tuần]
- **Tag:** [vv04]