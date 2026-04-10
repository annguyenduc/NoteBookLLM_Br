# 🏎️ LMS Deep Knowledge: Module Robotics (Robot & Điều khiển)

> **Mô tả**: Tổng hợp tri thức chuyên sâu CHỈ từ các bộ đề mBot 1/2 và Codey Rocky.
> **Kiểm định bởi**: @auditor (AG-SWARM-006)
> **Trạng thái**: ĐÃ CHUẨN HÓA TRÍCH DẪN (Verify bởi @pm v6.2)

---

## 🔩 1. Hệ thống Robot mBot 1 & 2

| Thành phần | mBot 1 (Module 1) | mBot 2 (Module 2) | Trích dẫn nguồn |
| :--- | :--- | :--- | :--- |
| **Bo mạch chính**| **mCore** (dựa trên Arduino Uno). | **CyberPi** (mạnh mẽ hơn, có màn hình màu). | [mBot_01] |
| **Động cơ** | Động cơ DC (điều khiển theo tốc độ -255 đến 255).| Động cơ **Encoder** (điều khiển chính xác góc/vòng). | [mBot_02] |
| **Cổng kết nối**| RJ25 (1-4). Cổng 1/2 thường dùng cảm biến; 3/4 dùng động cơ. | Cổng kết nối cảm biến thế hệ mới (mBuild). | [mBot_01] |
| **Cảm biến Line** | Cảm biến IR (Hồng ngoại) 2 mắt (S1/S2). | Cảm biến **RGB** (Nhận diện màu sắc vạch). | [mBot_01/02] |

---

## 🧸 2. Hệ thống Codey Rocky

- **Cấu trúc**: Phân tách thành 2 phần: **Codey** (Phần thân trên/Bộ não) và **Rocky** (Khung gầm xe). `[Nguồn: Codey_01]`
- **Tương tác**: Sử dụng Ma trận LED để biểu cảm, loa phát âm thanh và các nút nhấn (A, B, C).
- **Cảm biến tích hợp (Codey)**:
    - **Âm thanh/Ánh sáng**: Đo cường độ môi trường.
    - **Con quay hồi chuyển (Gyro)**: Nhận biết hành động: Lắc (Shake), Nghiêng trái/phải, Lật ngửa/úp. `[Nguồn: Codey_01]`
- **Cảm biến IR (Rocky)**: Dùng để dò đường hoặc phát hiện vật cản.

---

## 🕹️ 3. Chế độ Vận hành & Lập trình

- **Chế độ Trực tuyến (Live Mode)**: Robot chạy code trực tiếp từ máy tính/app mBlock qua Bluetooth/USB. Phù hợp để test nhanh. `[Nguồn: mBot_01]`
- **Chế độ Tải lên (Upload Mode)**: Lưu code vào bộ nhớ của robot. Robot có thể chạy độc lập mà không cần kết nối máy tính. `[Nguồn: mBot_02]`
- **Phần mềm mBlock 5**: Nền tảng lập trình kéo thả duy nhất được sử dụng để điều khiển các dòng robot này trong LMS.

---

## 🚩 4. Lỗi thường gặp (Misconceptions)

1. **Sai lệch Sensor**: Nhầm lẫn cảm biến Siêu âm (đo khoảng cách) với cảm biến Dò đường (nhận biết vạch). `[Nguồn: mBot_01]`
2. **Lỗi logic Di chuyển**: Không hiểu quy luật số âm (-) làm động cơ quay ngược. `[Nguồn: mBot_01]`
3. **Lỗi Upload**: Cố gắng nhấn "Upload" khi cáp chưa kết nối hoặc robot đang ở chế độ "Live". `[Nguồn: Codey_01]`

---
*Verify Source Checklist:*
- `[mBot_01]`: LMS_Tests_Robotics_mBot_1_de-trac-nghiem-1-mbot-m1.md
- `[mBot_02]`: LMS_Tests_Robotics_mBot_1+2_de-trac-nghiem-1-mon-mbot-m12.md
- `[Codey_01]`: LMS_Tests_Robotics_Codey_Rocky_de-trac-nghiem-1-codey.md
