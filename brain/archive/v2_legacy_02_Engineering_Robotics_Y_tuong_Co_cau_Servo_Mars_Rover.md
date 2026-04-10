---
tags: #robotics #mars-rover #education #grade6
created: 2026-04-07
last_updated: 2026-04-07
links: [[_index]], [[Antigravity_Obsidian_Memory_LOM]]
---

# Title: Ý tưởng Cơ cấu Servo cho Mars Rover Mô phỏng (Khối 6)

## 🎯 Context & Purpose
Tài liệu này tổng hợp các ý tưởng thiết kế cơ cấu sử dụng Servo (tối đa 2) dành cho học sinh khối 6 thực hiện các nhiệm vụ mô phỏng Mars Rover trên sa bàn giấy. Mục tiêu là kết hợp khả năng di chuyển, cảm biến siêu âm (tránh vật cản) và các tương tác vật lý mô phỏng nhiệm vụ thực tế của Perseverance.

## 🧠 Core Principles / Summary
- **Tiêu chuẩn "Không phá hoại"**: Do sa bàn làm bằng giấy, các cơ cấu gắp/đào phải nhẹ nhàng, không sử dụng lực quá lớn hoặc vật liệu sắc nhọn.
- **Tiết kiệm tài nguyên**: Tối đa 2 servo để giảm độ phức tạp về lập trình và cấp nguồn cho học sinh trung học cơ sở.
- **Mô phỏng thực tế**: Mỗi cơ cấu phải gắn liền với một nhiệm vụ khoa học thực tế của NASA (ví dụ: lấy mẫu đất, quét radar, hướng anten).

## 🛠️ Implementation / Details

### 1. Cơ cấu Đào & Thu thập Mẫu (Excavation)
- **Nguyên lý**: 2 Servo. Servo 1 điều khiển cánh tay (Lên/Xuống), Servo 2 điều khiển gầu xúc (Mở/Đóng).
- **Ứng dụng**: Mô phỏng việc thu thập mẫu đất để nghiên cứu địa chất.

### 2. Cơ cấu Nâng hạ Mẫu đất (Soil Lifting)
- **Nguyên lý**: Đặt mẫu đất (viên giấy cuộn) ở hai bên hông Rover.
- **Phát hiện**: Sử dụng cảm biến siêu âm quét ngang hoặc lập trình quỹ đạo để Rover di chuyển tới vị trí định sẵn.
- **Thực thi**: Servo nâng hạ một ngàm kẹp hoặc khay để đưa mẫu đất lên thân máy.

### 3. Cơ cấu Quét Cảm biến (Sensor Scanning)
- **Nguyên lý**: Gắn cảm biến siêu âm lên 1 servo xoay.
- **Ứng dụng**: Mô phỏng việc quét radar radar hoặc camera toàn cảnh (Panoramic) để lập bản đồ địa hình.

### 4. Cơ cấu Hướng Anten (Communication)
- **Nguyên lý**: Servo xoay một mô hình anten về phía "Trái đất" (vị trí cố định trên sa bàn).
- **Ứng dụng**: Mô phỏng việc truyền dữ liệu khoa học về trung tâm điều khiển.

## 🔗 Relations & Dependencies (Graph Weaving)
- Cấp trên: [[Antigravity_Obsidian_Memory_LOM]]
- Liên quan: [[v2_legacy_02_Engineering_Robotics_Tich_hop_TM_Yolo_UNO]] (về xử lý hình ảnh), [[v2_legacy_02_Engineering_Robotics_Ky_thuat_bu_tru_in_3D]] (về chế tạo cơ cấu).

## 🛡️ Reconciliation (Lưu vết thay đổi)
- **Status**: #active
- **Lưu ý**: Các ý tưởng này tập trung vào tính khả thi cho lớp 6 (Low entry barrier). Các phiên bản cao cấp hơn có thể tích hợp AI Vision để tự nhận diện mẫu đất.
