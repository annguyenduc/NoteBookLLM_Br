---
file_id: CONV_Atoms_conv_atoms_v04_2
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms conv atoms v04 2

# Tài liệu Học tập: Tuyển chọn Đội tuyển THPT - Vòng "Hồ sơ Ý tưởng"

## Thông tin chung
- **Khóa học**: Tư duy Hệ thống và Logic Vận hành
- **Mức độ**: Trung học Phổ thông
- **Thời lượng**: 8 tuần
- **Định dạng**: Dự án nhóm
- **Nguồn**: [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## # Mục tiêu học tập

Sau khi hoàn thành khóa học này, học sinh sẽ:

- Hiểu và áp dụng **tư duy hệ thống** trong thiết kế sản phẩm công nghệ
- Xây dựng **sơ đồ thuật toán** đơn giản với điều kiện rẽ nhánh
- Thiết kế **giao diện vật lý** phù hợp với chức năng kỹ thuật
- Trình bày **giải pháp công nghệ** một cách thuyết phục

---

## # Bài học 1: Giới thiệu Tư duy Hệ thống

### ## Mục tiêu bài học
- Nhận diện các thành phần cơ bản của một hệ thống tự động
- Hiểu mối quan hệ giữa đầu vào, xử lý và đầu ra
- Phân biệt vai trò trong nhóm kỹ thuật

### ## Nội dung chính

> **Tư duy hệ thống** là khả năng nhìn nhận một vấn đề như một tổng thể gồm nhiều thành phần tương tác với nhau để đạt được mục tiêu chung.

#### Các thành phần chính của hệ thống:
1. **Đầu vào (Input)**: Cảm biến, dữ liệu môi trường
2. **Xử lý (Processing)**: Vi điều khiển, thuật toán
3. **Đầu ra (Output)**: Thiết bị chấp hành, hiển thị
4. **Phản hồi (Feedback)**: Kiểm tra, điều chỉnh

![System Thinking Overview](../../brain/raw/lms_multi_media_dump/assets/system_thinking_image1.png)

---

## # Bài học 2: Vai trò trong Nhóm Kỹ thuật

### ## Mục tiêu bài học
- Hiểu rõ trách nhiệm của từng vai trò
- Biết cách phối hợp làm việc nhóm hiệu quả
- Chuẩn bị sản phẩm theo yêu cầu chuyên môn

### ## Ba vai trò chính

| Vai trò | Chuyên môn | Sản phẩm đầu ra |
|---------|------------|-----------------|
| **Lập trình** | Logic hệ thống, thuật toán | Sơ đồ khối, Flowchart, Kế hoạch kiểm thử |
| **Thiết kế 3D** | Thiết kế vật lý, mỹ thuật kỹ thuật | Bản vẽ 3D, File STL, Bố trí linh kiện |
| **Thuyết trình** | Truyền thông, phân tích giải pháp | Slide, Poster, Kịch bản vận hành |

---

## # Bài học 3: Chủ đề Dự án

### ## Mục tiêu bài học
- Chọn chủ đề phù hợp với năng lực nhóm
- Hiểu yêu cầu kỹ thuật của từng chủ đề
- Xác định mục tiêu cụ thể cho dự án

### ## Ba chủ đề lựa chọn

#### 1. Hệ thống Nhà kính thông minh
- **Mục tiêu**: Tự động điều chỉnh nhiệt độ, độ ẩm, ánh sáng
- **Thiết bị chính**: Cảm biến nhiệt độ, độ ẩm, ánh sáng; Quạt, đèn LED, servo điều khiển cửa

#### 2. Lớp học xanh & Tiết kiệm năng lượng
- **Mục tiêu**: Quản lý đèn, quạt, cửa dựa trên sự hiện diện và môi trường
- **Thiết bị chính**: Cảm biến chuyển động, cảm biến ánh sáng; Relay điều khiển đèn, servo điều khiển cửa

#### 3. Trạm chăm sóc cây đô thị tự động
- **Mục tiêu**: Tưới thông minh, nhận diện người đi đường
- **Thiết bị chính**: Cảm biến siêu âm, cảm biến độ ẩm đất; Bơm nước, cảm biến mưa

---

## # Worksheet 1: Phân tích Hệ thống

### ## Hướng dẫn
Hoàn thành bảng sau cho chủ đề đã chọn:

| Thành phần | Mô tả chi tiết | Thiết bị sử dụng | Kết nối với |
|------------|----------------|------------------|-------------|
| **Đầu vào** | Cảm biến nào? | | |
| **Xử lý** | Vi điều khiển? | | |
| **Đầu ra** | Thiết bị chấp hành? | | |
| **Hiển thị** | Màn hình? | | |

### ## Câu hỏi phản biện
1. Nếu cảm biến hỏng, hệ thống sẽ xử lý như thế nào?
2. Làm thế nào để kiểm tra hệ thống hoạt động đúng?
3. Có yếu tố môi trường nào ảnh hưởng đến hoạt động?

---

## # Worksheet 2: Thiết kế Flowchart Cơ bản

### ## Mẫu thuật toán đơn giản

```
Bắt đầu
  ↓
Đọc cảm biến
  ↓
So sánh ngưỡng
  ↓
Nếu ĐÚNG → Thực hiện hành động
  ↓
Nếu SAI → Không làm gì / Hành động khác
  ↓
Kết thúc
```

### ## Bài tập thực hành
Vẽ flowchart cho tình huống:
- **Nếu nhiệt độ > 30°C thì bật quạt, ngược lại thì tắt**
- **Nếu độ ẩm < 40% thì bật bơm tưới, ngược lại thì tắt**

---

## # Quiz: Kiến thức Cơ bản

### ## Câu 1
Tư duy hệ thống là gì?
- A. Chỉ tập trung vào một phần
- B. Nhìn nhận vấn đề như một tổng thể
- C. Làm việc độc lập
- D. Chỉ quan tâm đến kết quả

### ## Câu 2
Thành phần nào không thuộc hệ thống?
- A. Đầu vào
- B. Xử lý
- C. Người dùng
- D. Đầu ra

### ## Câu 3
Flowchart dùng để làm gì?
- A. Vẽ tranh
- B. Mô tả thuật toán
- C. Thiết kế 3D
- D. Viết code

---

## # Scenario: Tình huống Giả định

### ## Bối cảnh
Nhóm bạn được giao nhiệm vụ thiết kế hệ thống **Lớp học xanh** cho trường. Hệ thống phải:
- Tự động tắt đèn khi không có người
- Điều chỉnh quạt theo nhiệt độ
- Có màn hình hiển thị trạng thái

### ## Yêu cầu
1. **Lập trình viên**: Vẽ sơ đồ khối và flowchart
2. **Thiết kế viên**: Thiết kế vỏ máy, bố trí cảm biến
3. **Thuyết trình viên**: Chuẩn bị slide giới thiệu giải pháp

### ## Gợi ý giải pháp
- Cảm biến chuyển động để phát hiện người
- Cảm biến nhiệt độ để điều khiển quạt
- Màn hình LCD hiển thị nhiệt độ và trạng thái đèn

---

## # Rubric Đánh giá

| Tiêu chí | Mức tối đa (10 điểm) | Mức trung bình (5 điểm) | Mức thấp (1 điểm) |
|----------|---------------------|------------------------|-------------------|
| **Tư duy Logic** | Sơ đồ đầy đủ, thuật toán chặt chẽ, xử lý lỗi tốt | Có sơ đồ, thuật toán cơ bản | Thiếu sơ đồ hoặc logic sai |
| **Thiết kế 3D** | Sáng tạo, khả thi, bố trí hợp lý | Có thiết kế, chưa tối ưu | Thiết kế không khả thi |
| **Trình bày** | Chuyên nghiệp, thuyết phục, rõ ràng | Có trình bày, còn thiếu sót | Trình bày kém, khó hiểu |

---

## # Tài nguyên hỗ trợ

- [Mẫu sơ đồ khối](../templates/block_diagram_template.md)
- [Hướng dẫn vẽ flowchart](../guides/flowchart_guide.md)
- [Video hướng dẫn Tinkercad](../videos/tinkercad_tutorial.md)
- [Mẫu slide thuyết trình](../templates/presentation_template.md)

---

## # Ghi chú quan trọng

> Học sinh không cần biết lập trình chi tiết hay nối chân mạch. Tập trung vào **luồng dữ liệu** và **tư duy logic** là trọng tâm chính của vòng tuyển chọn này [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).