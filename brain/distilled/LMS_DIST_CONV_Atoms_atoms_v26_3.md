---
file_id: CONV_Atoms_atoms_v26_3
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms atoms v26 3

# Tài liệu Học Tập: Ứng Dụng Servo trong Mô Phỏng Mars Rover và Tối Ưu Hóa Gradient Descent

**Phiên bản:** LOM v4.4 Supreme  
**Ngôn ngữ:** Tiếng Việt  
**Môn học:** Kỹ thuật Robot & Tối Ưu Hóa  
**Độ tuổi mục tiêu:** Trung học Phổ thông / Đại học năm nhất  

---

## # Tổng Quan Bài Học

Bài học này giới thiệu cách sử dụng **servo motor** để mô phỏng các chức năng của **Mars Rover** trên sa bàn giấy, đồng thời áp dụng **thuật toán Gradient Descent** để tối ưu hóa các hàm số trong không gian 3D. Học sinh sẽ được trải nghiệm thực hành mô phỏng robot và lập trình thuật toán tối ưu hóa.

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## # Mục Tiêu Học Tập

Sau bài học, học sinh có thể:

- Hiểu và mô tả vai trò của servo trong các cơ cấu điều khiển robot.
- Liệt kê các ứng dụng cụ thể của servo trong mô phỏng hoạt động của Mars Rover.
- Áp dụng thuật toán Gradient Descent để tìm điểm cực tiểu của hàm số hai biến.
- Vẽ đồ thị 3D và biểu diễn quá trình tối ưu hóa bằng thư viện Python.

---

## # Nội Dung Chính

### ## 1. Ứng Dụng Servo trong Mô Phỏng Mars Rover

| STT | Tên Cơ Cấu | Mô Tả Chức Năng | Ứng Dụng Mô Phỏng |
|-----|------------------|------------------|--------------------|
| 1 | Cơ cấu khám phá môi trường | Điều khiển cảm biến di chuyển | Mô phỏng việc tìm hiểu địa hình |
| 2 | Cơ cấu thay đổi tốc độ | Điều chỉnh tốc độ và gia tốc | Thích nghi với địa hình khác nhau |
| 3 | Cơ cấu định vị | Xác định hướng và vị trí | Di chuyển theo lộ trình |
| 4 | Cơ cấu phản lực | Giữ thăng bằng khi gặp chướng ngại | Mô phỏng phản ứng tự động |
| 5 | Cơ cấu nâng hạ | Nâng hạ thiết bị nhẹ | Vận chuyển vật thể không làm hỏng bề mặt |
| 6 | Cơ cấu kích hoạt cần gạt | Kích hoạt công tắc, cảm biến | Mô phỏng thu thập dữ liệu |
| 7 | Cơ cấu thu thập mẫu đất | Mô phỏng việc lấy mẫu | Lưu trữ mẫu vật |
| 8 | Cơ cấu quay camera | Điều chỉnh góc nhìn | Ghi hình môi trường |
| 9 | Cơ cấu cảm biến khí quyển | Đo đạc điều kiện khí hậu | Mô phỏng phân tích khí quyển |
| 10 | Cơ cấu vặn vít | Thực hiện tác vụ lắp ráp | Bảo trì thiết bị |
| 11 | Cơ cấu ném vật | Gửi mẫu vật đến điểm đích | Mô phỏng vận chuyển chính xác |
| 12 | Cơ cấu đào hố | Đào mẫu dưới bề mặt | Nghiên cứu địa chất |
| 13 | Cơ cấu giải cứu | Cứu vật thể bị kẹt | Hỗ trợ robot khác |
| 14 | Cơ cấu tạo hình đa dạng | Thay đổi hình dạng robot | Vượt chướng ngại vật |

> **Lưu ý:** Các cơ cấu này đều được điều khiển bằng **servo motor**, giúp mô phỏng chính xác các hành vi của robot thật trong môi trường giả lập [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

### ## 2. Tối Ưu Hóa với Gradient Descent

#### ### 2.1. Giới Thiệu

Gradient Descent là một thuật toán tối ưu hóa được sử dụng để tìm điểm cực tiểu của hàm số bằng cách cập nhật các tham số theo hướng ngược với gradient.

#### ### 2.2. Công Thức Toán Học

Hàm số cần tối ưu:  
$$
z = f(x,y) = x^2 + \sin(y)
$$

Gradient tương ứng:
$$
\nabla z = [2x, \cos(y)]
$$

#### ### 2.3. Gradient Descent với Momentum

Công thức cập nhật:
$$
v_{new} = \eta \cdot \text{grad}(x_{old}) + \gamma \cdot v_{old}
$$
$$
x_{new} = x_{old} - v_{new}
$$

Trong đó:
- $ \eta $: learning rate
- $ \gamma $: hệ số momentum

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## # Worksheet: Thực Hành Mô Phỏng và Tối Ưu Hóa

### ## A. Câu Hỏi Trắc Nghiệm

1. Cơ cấu nào sau đây **không** phải là ứng dụng của servo trong mô phỏng Mars Rover?
   - a) Cơ cấu đào hố
   - b) Cơ cấu phát điện
   - c) Cơ cấu quay camera
   - d) Cơ cấu nâng hạ

2. Gradient của hàm $ f(x,y) = x^2 + \sin(y) $ là gì?
   - a) $ [x, \sin(y)] $
   - b) $ [2x, \cos(y)] $
   - c) $ [2x^2, \cos(y)] $
   - d) $ [2x, -\cos(y)] $

3. Trong Gradient Descent với Momentum, biến $ v $ đại diện cho gì?
   - a) Giá trị hàm số
   - b) Tốc độ cập nhật
   - c) Gradient
   - d) Hệ số học

### ## B. Bài Tập Lập Trình

Sử dụng Python, thư viện `numpy`, `plotly.graph_objects`, và `np.meshgrid`, hãy:

- Vẽ đồ thị 3D của hàm $ f(x,y) = x^2 + \sin(y) $
- Áp dụng thuật toán Gradient Descent để tìm điểm cực tiểu
- Biểu diễn đường đi của thuật toán lên đồ thị

---

## # Quiz: Kiểm Tra Nhanh

### Câu 1:
Servo có thể được dùng để mô phỏng chức năng nào sau đây của Mars Rover?

- A. Di chuyển trên địa hình gồ ghề
- B. Giao tiếp với Trái Đất
- C. Tạo ra điện năng
- D. Tất cả các đáp án trên

### Câu 2:
Trong thuật toán Gradient Descent, nếu gradient tại điểm hiện tại là dương, thì bước tiếp theo sẽ:

- A. Tăng tham số
- B. Giảm tham số
- C. Không thay đổi
- D. Không thể xác định

### Câu 3:
Thư viện nào sau đây **không** được sử dụng để vẽ đồ thị 3D trong bài học?

- A. `plotly.graph_objects`
- B. `matplotlib.pyplot`
- C. `numpy`
- D. `np.meshgrid`

---

## # Scenario: Thiết Kế Một Mars Rover Mini

### Tình Huống:

Bạn là kỹ sư robot, được yêu cầu thiết kế một **Mars Rover mini** mô phỏng hoạt động trên sa bàn giấy. Bạn cần chọn ít nhất 5 cơ cấu sử dụng servo để mô phỏng các hành vi sau:

- Khám phá địa hình
- Thu thập mẫu vật
- Gửi dữ liệu về trạm điều khiển
- Di chuyển linh hoạt
- Tự bảo vệ khỏi chướng ngại vật

### Yêu Cầu:

- Liệt kê 5 cơ cấu servo phù hợp.
- Mô tả ngắn gọn cách mỗi cơ cấu hoạt động.
- Vẽ sơ đồ nguyên lý kết nối servo và cảm biến (nếu có).

---

## # Tài Nguyên Học Tập

- [Link GitHub chứa mã nguồn minh họa](https://github.com/example/mars-rover-servo)
- [Video hướng dẫn mô phỏng robot với servo](https://youtube.com/example)
- [Tài liệu tham khảo về Gradient Descent](https://example.com/gd-tutorial)

---

## # Đính kèm Hình Ảnh

![minh họa rover servo](../../brain/raw/lms_multi_media_dump/assets/vv26_image1.png)  
*Minh họa mô phỏng Mars Rover sử dụng servo*

---

**Kết thúc tài liệu học tập.**  
[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)