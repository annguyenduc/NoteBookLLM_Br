---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v02_3
  title: atoms_v02_3
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v02:

**1. Sự kiện về IoT & Phần cứng AI**
- **Fact:** Mạch Yolo UNO sử dụng vi điều khiển ESP32-S3 hai nhân 240MHz, tích hợp bộ nhớ Flash 4MB, PSRAM 8MB và có khả năng tăng tốc xử lý AI.
- **Source:** [v02 - Section: Giới thiệu và bối cảnh (Cải thiện hiệu suất... Yolo UNO)]
- **Tag:** [vv02]

- **Fact:** Thuật toán FOMO (Faster Objects, More Objects) cho phép phát hiện vật thể thời gian thực bằng cách theo dõi tâm điểm (centroid) thay vì khung bao (bounding box), giúp tối ưu cho vi điều khiển.
- **Source:** [v02 - Section: Lựa chọn mô hình máy học nhẹ và hiệu quả]
- **Tag:** [vv02]

- **Fact:** MCUNet là kiến trúc mạng nơ-ron được thiết kế để chạy deep learning trực tiếp trên các chip có tài nguyên cực kỳ hạn chế.
- **Source:** [v02 - Section: Lựa chọn mô hình máy học nhẹ và hiệu quả]
- **Tag:** [vv02]

- **Fact:** Mạng CNN Micro Speech dùng cho nhận dạng từ khóa có thể nén xuống kích thước khoảng 20–50 KB (định dạng int8) mà vẫn đảm bảo độ chính xác.
- **Source:** [v02 - Section: Bảng so sánh mô hình/thuật toán nhẹ]
- **Tag:** [vv02]

**2. Sự kiện về Tối ưu hóa AI (TinyML)**
- **Fact:** Kỹ thuật lượng tử hóa (Quantization) chuyển đổi trọng số từ số thực 32-bit sang 8-bit giúp giảm kích thước mô hình khoảng 4 lần và tăng tốc độ suy luận trên thiết bị IoT.
- **Source:** [v02 - Section: Nén và tối ưu hóa mô hình học máy - Lượng tử hóa]
- **Tag:** [vv02]

- **Fact:** Kỹ thuật Pruning (tỉa mạng) giúp loại bỏ các kết nối trọng số ít đóng góp, giúp giảm bộ nhớ và giảm hiện tượng quá khớp (overfitting).
- **Source:** [v02 - Section: Nén và tối ưu hóa mô hình học máy - Pruning]
- **Tag:** [vv02]

- **Fact:** Việc áp dụng bộ lọc trung bình động (moving average) hoặc bộ lọc thông thấp cho dữ liệu cảm biến giúp giảm nhiễu đầu vào cho mô hình AI trên ESP32.
- **Source:** [v02 - Section: Cải tiến việc thu thập và tiền xử lý dữ liệu cảm biến]
- **Tag:** [vv02]

**3. Sự kiện về Robotics & Máy in 3D**
- **Fact:** Đối với máy in 3D direct-drive (như Neptune 4), thông số khoảng lùi (retraction) tối ưu cho nhựa PLA thường là 0.6–1.0 mm với tốc độ 25–35 mm/s.
- **Source:** [v02 - Section: Sửa máy in đùn mực - B) Đùn quá nhiều trên bản in]
- **Tag:** [vv02]

- **Fact:** Kỹ thuật "heat-tighten" yêu cầu siết chặt vòi phun (nozzle) khi đang ở nhiệt độ cao (khoảng 230°C) để đảm bảo không có khe hở giữa nozzle và heatbreak.
- **Source:** [v02 - Section: Sửa máy in đùn mực - A) Đùn/rao rỉ mực quanh đầu nóng]
- **Tag:** [vv02]

- **Fact:** Phương pháp Cold-pull để thông tắc nhựa PLA thực hiện bằng cách gia nhiệt lên 220°C, sau đó hạ nhiệt xuống 90–100°C rồi rút mạnh sợi nhựa ra.
- **Source:** [v02 - Section: Cắm mực vào nhưng không thấy mực chảy ra - 2) Cold-pull]
- **Tag:** [vv02]

- **Fact:** Lệnh G-code M92 được sử dụng để hiệu chuẩn thông số E-steps của bộ đùn nhựa, sau đó dùng M500 để lưu vào bộ nhớ máy in.
- **Source:** [v02 - Section: Sửa máy in đùn mực - B) Đùn quá nhiều trên bản in]
- **Tag:** [vv02]

**4. Sự kiện về Chứng chỉ Công nghệ (Cloud)**
- **Fact:** Chứng chỉ AWS Certified Cloud Practitioner (CLF-C02) có lệ phí thi là 100 USD, gồm 65 câu hỏi trong thời gian 90 phút.
- **Source:** [v02 - Section: 1) AWS – rẻ & dễ vào việc]
- **Tag:** [vv02]

- **Fact:** Chương trình Microsoft Virtual Training Days (MVTD) cung cấp voucher giảm giá 50% lệ phí thi các chứng chỉ Fundamentals (như AZ-900).
- **Source:** [v02 - Section: 2) Microsoft Azure – rẻ & nhiều cơ hội doanh nghiệp]
- **Tag:** [vv02]