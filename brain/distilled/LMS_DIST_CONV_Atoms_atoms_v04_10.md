---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v04_10
  title: atoms_v04_10
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v04:

**1. Lĩnh vực: IoT & Cảm biến (Sensor Logic)**
- **Fact:** Logic quyết định đóng cửa (`close_door = 1`) dựa trên 3 ngưỡng cảm biến: Khoảng cách < 25cm, Tiếng ồn > 65dB, hoặc Nhiệt độ > 38°C.
- **Source:** (vv04 - Section: Python Code / Reference rules)
- **Tag:** [vv04]

**2. Lĩnh vực: AI & Data Science (Metrics)**
- **Fact:** Các chỉ số đo lường hiệu quả của mô hình phân loại (Classification) bao gồm: Accuracy (Độ chính xác), Precision (Độ chính xác dương tính), Recall (Độ nhạy) và F1-score.
- **Source:** (vv04 - Section: Python Code / Metrics and confusion matrix)
- **Tag:** [vv04]

**3. Lĩnh vực: Robotics & In 3D (Cấu hình Infill-only)**
- **Fact:** Để in 3D chỉ có phần lõi (infill) mà không có vỏ, cần thiết lập: Wall Line Count = 0, Top Layers = 0 và Bottom Layers = 0.
- **Source:** (vv04 - Section: Conversation / Cách thiết lập “Infill-only”)
- **Tag:** [vv04]

**4. Lĩnh vực: Robotics & In 3D (Xử lý bám dính bàn in)**
- **Fact:** Để đế in (Brim) dễ gỡ và tự tách khỏi vật thể, cần thiết lập Brim Distance từ 0.1mm đến 0.3mm.
- **Source:** (vv04 - Section: Conversation / Nếu do Build Plate Adhesion)
- **Tag:** [vv04]

**5. Lĩnh vực: Robotics & In 3D (Cấu hình Support)**
- **Fact:** Khoảng cách Z giữa Support và vật thể (Support Z Distance) nên đặt ≥ chiều dày lớp in (thường là 0.2mm - 0.3mm) để dễ dàng bóc tách.
- **Source:** (vv04 - Section: Conversation / Nếu do Support chạm đáy)
- **Tag:** [vv04]

**6. Lĩnh vực: Robotics & In 3D (Kỹ thuật in Bridge - Bắc cầu)**
- **Fact:** Thông số tối ưu khi in Bridge cho nhựa PLA trên máy Neptune 4 bao gồm: Quạt làm mát 100%, Tốc độ in (Bridge Speed) giảm xuống 25-35 mm/s và Flow (Lưu lượng) giảm còn 90-95%.
- **Source:** (vv04 - Section: Conversation / Bật gì? & Đặt giá trị)
- **Tag:** [vv04]

**7. Lĩnh vực: Robotics & In 3D (Vase Mode)**
- **Fact:** Chế độ in "Vase Mode" (Spiralize Outer Contour) tạo ra vật thể có thành mỏng 1 lớp, không nắp và không có phần lõi (infill).
- **Source:** (vv04 - Section: Conversation / Trường hợp bạn định nói “vase mode”)
- **Tag:** [vv04]