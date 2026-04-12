---
file_id: CONV_Atoms_conv_atoms_v23_20
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms conv atoms v23 20

# Tài liệu Học Tập: Giới thiệu về Robot và Ứng Dụng

## Thông tin chung

| Thuộc tính | Mô tả |
|------------|-------|
| **Tiêu đề** | Giới thiệu về Robot và Các Loại Robot Phổ Biến |
| **Mô tả ngắn** | Bài học giới thiệu các khái niệm cơ bản về robot, phân loại robot theo thiết kế và chức năng, cũng như ứng dụng của chúng trong đời sống và khoa học. |
| **Đối tượng học viên** | Sinh viên kỹ thuật, lập trình viên, người quan tâm đến công nghệ robot |
| **Thời lượng** | 60 phút |
| **Ngôn ngữ** | Tiếng Việt |

---

## Mục tiêu học tập

Sau khi hoàn thành bài học này, học viên sẽ có thể:

- Định nghĩa được robot và vai trò của nó trong khoa học và công nghệ.
- Phân biệt được 5 loại robot chính dựa trên thiết kế và chức năng.
- Hiểu được nguyên lý hoạt động và ứng dụng của từng loại robot.
- Nắm được một số ứng dụng robot trong lĩnh vực thám hiểm không gian.

---

## Nội dung bài học

### 1. Robot là gì?

Robot là sự giao thoa giữa khoa học, kỹ thuật và công nghệ để tạo ra các cỗ máy (robot) nhằm thay thế hoặc mô phong các hành động của con người [^1].

![Giới thiệu về robot](../../brain/raw/lms_multi_media_dump/assets/vv23_image1.png)

[^1]: [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### 2. Phân loại robot

Robot có 5 loại chính dựa trên thiết kế và chức năng:

| Loại robot | Mô tả | Ví dụ |
|------------|-------|-------|
| **Lập trình sẵn (Pre-programmed)** | Hoạt động trong môi trường được kiểm soát để thực hiện các tác vụ đơn điệu | Cánh tay cơ khí trong dây chuyền lắp ráp ô tô |
| **Giống người (Humanoid)** | Được thiết kế để bắt chước hành vi và ngoại hình con người | Sophia (Hanson Robotics), Atlas (Boston Dynamics) |
| **Tự hành (Autonomous)** | Sử dụng cảm biến để nhận biết môi trường và hệ thống ra quyết định để hoạt động không cần giám sát | Máy hút bụi Roomba |
| **Điều khiển từ xa (Tele-operated)** | Bán tự hành, được điều khiển từ khoảng cách an toàn qua mạng không dây | Robot sửa ống nước dưới đáy biển |
| **Tăng cường (Augmenting)** | Giúp nâng cao hoặc thay thế khả năng của con người | Chi giả robot, khung xương ngoài (exoskeletons) |

[^2]: [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### 3. Ứng dụng robot trong thám hiểm không gian

#### 3.1. Robot thám hiểm sao Hỏa (Rover)

- Không sử dụng joystick để điều khiển trực tiếp.
- Kỹ sư gửi lệnh từ Trái Đất qua đêm, Rover thực hiện vào ngày hôm sau.
- Có thể di chuyển theo lệnh cụ thể hoặc tự tìm đường bằng camera 3D [^3].

#### 3.2. Thiết bị trên robot thám hiểm

| Thiết bị | Chức năng |
|----------|-----------|
| **SuperCam** | Sử dụng tia laser để xác định thành phần hóa học trong đá từ khoảng cách lên tới 7 mét |
| **MEDA** | Nghiên cứu thời tiết và khí quyển của sao Hỏa |
| **HazCams** | Phát hiện và tránh chướng ngại vật nguy hiểm |

[^3]: [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bảng thuật ngữ

| Thuật ngữ | Định nghĩa |
|-----------|------------|
| **Cross-entropy** | Đại lượng đo lường sự khác biệt giữa hai phân bố xác suất (thực tế và dự đoán), thường dùng để đánh giá mô hình học máy trong các bài toán phân loại |
| **PID Control** | Thuật toán điều khiển phản hồi dùng trong điều khiển robot theo quỹ đạo |
| **Exoskeleton** | Khung xương ngoài hỗ trợ vận động cho con người |
| **API Key** | Chuỗi ký tự xác thực dùng trong lập trình ứng dụng |

---

## Bài tập thực hành

### Câu hỏi trắc nghiệm

1. Robot nào sau đây hoạt động trong môi trường được kiểm soát để thực hiện các tác vụ đơn điệu?
   - A. Humanoid
   - B. Autonomous
   - C. Pre-programmed
   - D. Tele-operated

2. Thiết bị nào trên robot thám hiểm sao Hỏa được dùng để phân tích thành phần hóa học của đá?
   - A. MEDA
   - B. HazCams
   - C. SuperCam
   - D. Camera 3D

3. Công cụ nào trong Python được dùng để quản lý thông tin nhạy cảm như API Key?
   - A. `st.session_state`
   - B. `st.secrets`
   - C. `st.cache_data`
   - D. `st.experimental_memo`

### Câu hỏi tự luận

1. Hãy mô tả nguyên lý hoạt động của robot tự hành (autonomous robot) và nêu một ví dụ thực tế.
2. Giải thích tại sao robot thám hiểm sao Hỏa không thể điều khiển bằng joystick như các robot trên Trái Đất.

---

## Tài liệu tham khảo

- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Ghi chú cho giảng viên

- Bài học này phù hợp để giảng dạy trong môn Kỹ thuật Robot hoặc Nhập môn Trí tuệ nhân tạo.
- Có thể mở rộng thêm phần lập trình điều khiển robot bằng Python nếu học viên đã có kiến thức lập trình cơ bản.
- Nên sử dụng video minh họa hoạt động của robot trong thực tế để tăng hiệu quả giảng dạy.