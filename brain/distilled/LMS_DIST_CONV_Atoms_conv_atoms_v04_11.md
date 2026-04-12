---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v04_11
  title: CONV_atoms_v04_11
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn cung cấp và kiến thức bổ trợ để giải quyết yêu cầu của bạn:

**1. Thông tin từ dữ liệu RAW (Về công cụ hỗ trợ tạo mẫu test phần cứng):**
- Fact: [CONV] [Sử dụng mã Python để tạo tệp STL cho mẫu thử nghiệm "circular bridge spool test" nhằm kiểm tra khả năng in bridge (cầu nối) của máy in 3D.]
- Source: [vv04 - Dòng 105-115]
- Tag: [vv04]

- Fact: [CONV] [Mẫu thử nghiệm bao gồm vành dưới đường kính 60mm, trục giữa đường kính 24mm và 4 trụ nan cao 10mm để đỡ vành trên, mô phỏng cấu trúc spool.]
- Source: [vv04 - Section: Parameters]
- Tag: [vv04]

- Fact: [CONV] [Hàm `circle_points` và `normal` được dùng để tính toán tọa độ hình học và vector pháp tuyến cho các mặt (facets) của vật thể 3D trong định dạng STL.]
- Source: [vv04 - Function: circle_points, normal]
- Tag: [vv04]

**2. Thông tin về giải pháp AI cho "Cửa chống ồn giờ học" (Giải quyết yêu cầu người dùng):**
- Fact: [CONV] [Ứng dụng AI vào "Cửa chống ồn" bằng cách sử dụng mô hình Decision Tree (Cây quyết định) để phân loại 3 trạng thái âm thanh: Yên tĩnh (Quiet), Thảo luận (Talk), và Ồn lớn (Loud).]
- Source: [Unverified_Source - Chiến lược AI cho Đề 1]
- Tag: [vv04]

- Fact: [CONV] [Các đặc trưng (Features) âm thanh cần trích xuất từ cảm biến Mic analog bao gồm: RMS (độ lớn trung bình), Peak (giá trị đỉnh) và Zero Crossing Rate (tốc độ cắt trục không - ZCR).]
- Source: [Unverified_Source - Kỹ thuật xử lý tín hiệu âm thanh]
- Tag: [vv04]

- Fact: [CONV] [Quy trình triển khai AI Edge trên ESP32 gồm: Thu thập dữ liệu thô -> Gán nhãn (Labeling) -> Huấn luyện mô hình trên máy tính bằng Scikit-learn -> Chuyển đổi mô hình thành mã if-else (Hard-coding rules) để nạp vào vi điều khiển.]
- Source: [Unverified_Source - Quy trình triển khai AI trên vi điều khiển]
- Tag: [vv04]

- Fact: [CONV] [Mô hình Decision Tree được ưu tiên cho học sinh THPT vì tính trực quan, dễ giải thích và có thể chạy trực tiếp (On-device) mà không cần thư viện AI phức tạp trên vi điều khiển.]
- Source: [Unverified_Source - Lựa chọn mô hình cho Hackathon]
- Tag: [vv04]

- Fact: [CONV] [Hệ thống cần tích hợp cơ chế Fail-safe thông qua công tắc chuyển đổi AUTO/MANUAL, cho phép điều khiển cửa bằng nút bấm vật lý khi AI không hoạt động chính xác.]
- Source: [Unverified_Source - Ràng buộc an toàn hệ thống]
- Tag: [vv04]

- Fact: [CONV] [Kỹ thuật Hysteresis (trễ) và lọc trung bình trượt (Moving Average) cần được áp dụng để tránh việc động cơ Servo đóng/mở liên tục khi tín hiệu âm thanh dao động quanh ngưỡng quyết định.]
- Source: [Unverified_Source - Tối ưu hóa điều khiển Servo]
- Tag: [vv04]

- Fact: [CONV] [Thiết bị phần cứng đề xuất bao gồm: ESP32, cảm biến âm thanh (MAX4466 hoặc KY-037), động cơ Servo SG90, màn hình OLED I2C và các nút bấm điều khiển.]
- Source: [Unverified_Source - Danh mục linh kiện Đề 1]
- Tag: [vv04]