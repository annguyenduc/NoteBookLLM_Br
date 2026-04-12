---
file_id: CONV_Atoms_atoms_v04_2
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms atoms v04 2

# Tài liệu Học Tập - LOM v4.4 Supreme
**Tên Khóa Học:** Thiết Kế Giải Pháp STEM/AI - Vòng Ý Tưởng  
**Mã Học Phần:** STEM_AI_DESIGN_001  
**Phiên bản:** LOM v4.4 Supreme  
**Ngôn ngữ:** Tiếng Việt  

---

## 1. Tổng Quan Khóa Học

### Mục Tiêu Học Tập
Sau khi hoàn thành khóa học này, học sinh sẽ có khả năng:
- Phân tích vấn đề thực tiễn và thiết kế giải pháp công nghệ phù hợp
- Xây dựng sơ đồ thuật toán (flowchart) logic và toàn diện
- Thiết kế giao diện 3D và truyền thông ý tưởng hiệu quả
- Làm việc nhóm theo mô hình chuyên môn hóa vai trò

### Đối Tượng Học Tập
- Học sinh THPT quan tâm đến STEM, IoT và thiết kế giải pháp công nghệ
- Học sinh chuẩn bị tham gia các cuộc thi khoa học kỹ thuật

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 2. Cấu Trúc Nội Dung Học Tập

### 2.1. Module 1: Phân Tích Vấn Đề & Chọn Chủ Đề

#### Bài 1.1: Giới Thiệu Bộ Linh Kiện
**Nội dung:**
- Yolo:Bit/Yolo UNO (vi điều khiển trung tâm)
- Cảm biến DHT20 (nhiệt độ/độ ẩm)
- Cảm biến ánh sáng, độ ẩm đất, siêu âm
- Màn hình LCD 1602
- Bộ phận chấp hành: Servo, Relay, Bơm, Quạt

**Hoạt động:** Học sinh liệt kê chức năng từng linh kiện và khả năng ứng dụng

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

#### Bài 1.2: Ba Chủ Đề Thiết Kế
| Chủ Đề | Mô Tả | Ứng Dụng Thực Tế |
|--------|-------|------------------|
| **A. Nông nghiệp đô thị thông minh** | Tự động tưới, thông gió, giám sát môi trường | Vườn rau trên sân thượng, nhà kính nhỏ |
| **B. Trường học xanh & Tiết kiệm năng lượng** | Tự động bật/tắt thiết bị, cảnh báo tiếng ồn | Phòng học thông minh, thư viện tự động |
| **C. Cảnh báo an toàn & Sức khỏe** | Giám sát chất lượng không khí, tư thế ngồi | Phòng học ergonomics, không gian làm việc an toàn |

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 3. Module 2: Vai Trò & Nhiệm Vụ Chuyên Môn

### 3.1. Vai Trò Lập Trình (Logic & Hệ Thống)

#### 3.1.1. Sơ Đồ Khối Thiết Bị (Block Diagram)
**Yêu cầu:**
- Vẽ sơ đồ thể hiện luồng dữ liệu: Nguồn → Cảm biến (Input) → Vi điều khiển (Processing) → Bộ phận chấp hành (Output) → Hiển thị

**Mẫu sơ đồ tiêu chuẩn:**
```
[Khối Nguồn] → [Khối Cảm Biến] → [Khối Xử Lý] → [Khối Chấp Hành] → [Khối Hiển Thị]
```

#### 3.1.2. Sơ Đồ Thuật Toán (Flowchart)
**Ký hiệu chuẩn:**
- Hình chữ nhật: Hành động/thiết lập
- Hình thoi: Điều kiện/rẽ nhánh
- Mũi tên: Luồng thực thi

**Ví dụ mẫu:**
```mermaid
flowchart TD
    A[Bắt đầu] --> B[Kiểm tra độ ẩm đất]
    B --> C{Độ ẩm < 30%?}
    C -->|Đúng| D[Bật bơm tưới]
    C -->|Sai| E[Tắt bơm tưới]
    D --> F[Kiểm tra thời gian bơm]
    F --> G{> 5 phút?}
    G -->|Đúng| H[Tắt bơm - bảo vệ}
    G -->|Sai| I[Quay lại kiểm tra]
    E --> I
    H --> I
```

#### 3.1.3. Kịch Bản Xử Lý Lỗi (Fail-Safe)
**Các tình huống cần xử lý:**
- Cảm biến hỏng (trả về giá trị bất thường)
- Nguồn nước cạn (bảo vệ bơm khỏi cháy)
- Ngưỡng an toàn (giới hạn thời gian hoạt động)

#### 3.1.4. Kế Hoạch Kiểm Thử (Test Plan)
**Yêu cầu:** Liệt kê ít nhất 5 tình huống kiểm thử

| STT | Tình Huống | Mục Tiêu Kiểm Thử |
|-----|------------|-------------------|
| 1 | Môi trường khô hạn | Hệ thống kích hoạt bơm đúng lúc |
| 2 | Môi trường ẩm ướt | Hệ thống không bơm thừa |
| 3 | Cảm biến hỏng | Hệ thống không hoạt động sai lệch |
| 4 | Nguồn điện yếu | Hệ thống cảnh báo hoặc tạm dừng |
| 5 | Mất kết nối cảm biến | Hệ thống chuyển sang chế độ an toàn |

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 3.2. Vai Trò Thẩm Mỹ (Thiết Kế 3D & Bao Bì)

#### 3.2.1. Bản Vẽ Phối Cảnh 3D
**Công cụ hỗ trợ:**
- Tinkercad (miễn phí, dễ sử dụng)
- SketchUp (chuyên nghiệp hơn)
- Vẽ tay kỹ thuật (nếu không có máy tính)

**Yêu cầu thiết kế:**
- Vị trí màn hình LCD dễ quan sát
- Lỗ cảm biến cho phép "nhìn" ra ngoài
- Lối luồn dây điện gọn gàng
- Kết cấu chắc chắn, dễ lắp ráp

#### 3.2.2. Thuyết Minh Thiết Kế
**Nội dung cần có:**
- Lý do chọn hình dáng cụ thể
- Vật liệu dự kiến sử dụng
- Tính tiện dụng cho người dùng cuối

#### 3.2.3. Poster Giới Thiệu
**Định dạng:** 1 trang A4
**Nội dung:** Tên dự án, hình ảnh 3D, tính năng nổi bật

![Thiết kế 3D mẫu](../../brain/raw/lms_multi_media_dump/assets/STEM_AI_DESIGN_001_image1.png)

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 3.3. Vai Trò Thuyết Trình (Nội Dung & Pitching)

#### 3.3.1. Bộ Slide (Tối Đa 8 Trang)
**Cấu trúc đề xuất:**
1. Vấn đề thực tế đang gặp phải
2. Giải pháp công nghệ đề xuất
3. Cơ chế hoạt động (minh họa bằng hình ảnh)
4. Tính mới và sáng tạo của giải pháp
5. Khả năng nhân rộng và ứng dụng thực tế
6. Kết quả dự kiến đạt được
7. Kế hoạch triển khai (nếu có)
8. Kết luận và cảm ơn

#### 3.3.2. Kịch Bản Thuyết Trình
**Yêu cầu:**
- Thời lượng: 5 phút
- Ngôn ngữ lôi cuốn, thuyết phục
- Chuẩn bị trả lời câu hỏi phản biện

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 4. Bảng Đánh Giá & Thang Điểm

| Tiêu Chí | Trọng Số | Mô Tả Chi Tiết | Điểm Tối Đa |
|----------|----------|----------------|-------------|
| **Tư Duy Logic (Lập Trình)** | 35 điểm | Sơ đồ khối đúng chuẩn; Thuật toán chặt chẽ; Có xử lý trường hợp ngoại lệ | 35 |
| **Thẩm Mỹ & Thiết Kế (3D)** | 25 điểm | Bản vẽ rõ ràng, khả thi; Poster chuyên nghiệp | 25 |
| **Kỹ Năng Truyền Thông (Thuyết Trình)** | 25 điểm | Slide hấp dẫn; Nội dung thuyết phục; Trả lời phản biện tốt | 25 |
| **Tính Sáng Tạo & Khả Thi** | 10 điểm | Ý tưởng mới lạ; Thực hiện được với thiết bị có sẵn | 10 |
| **Hồ Sơ & Tổ Chức** | 5 điểm | Nộp đúng hạn; File khoa học; Đặt tên chuẩn | 5 |
| **Tổng Cộng** | **100 điểm** | | |

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 5. Hướng Dẫn Nộp Bài

### 5.1. Định Dạng Nộp Bài
- Tất cả file nén vào 1 file `.zip` hoặc `.rar`
- Tên file: `TUYENCHON_TEN-DOI_TEN-TRUONG.zip`

### 5.2. Danh Sách File Bắt Buộc
- Sơ đồ khối thiết bị (PDF/JPG)
- Flowchart thuật toán (PDF/JPG)
- Bản vẽ 3D (STL/PDF)
- Poster giới thiệu (JPG/PDF)
- Bộ slide thuyết trình (PPTX/PDF)
- Kịch bản thuyết trình (DOCX/PDF)

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 6. Bài Tập Thực Hành

### 6.1. Worksheet: Phân Tích Vấn Đề
**Họ và tên:** _________________  
**Lớp:** _________________  
**Nhóm:** _________________  

#### Câu 1: Chọn chủ đề và lý do
Chủ đề đã chọn: ________________________  
Lý do chọn: ________________________

#### Câu 2: Liệt kê linh kiện cần dùng
| STT | Tên Linh Kiện | Chức Năng | Vai Trò Trong Dự Án |
|-----|---------------|-----------|-------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

#### Câu 3: Vẽ sơ đồ thuật toán đơn giản
(Vẽ flowchart cho một chức năng chính của dự án)

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 7. Quiz Kiểm Tra

### Câu 1: Ký hiệu nào trong flowchart biểu diễn điều kiện?
A. Hình chữ nhật  
B. Hình thoi  
C. Hình tròn  
D. Hình tam giác  

### Câu 2: Khi độ ẩm đất dưới 30%, hệ thống nên làm gì?
A. Bật bơm tưới  
B. Tắt bơm tưới  
C. Không làm gì  
D. Cảnh báo người dùng  

### Câu 3: Mục đích của xử lý lỗi fail-safe là gì?
A. Tăng tốc độ hệ thống  
B. Bảo vệ thiết bị khỏi hư hại  
C. Giảm chi phí  
D. Tăng tính năng  

**Đáp án:** 1.B, 2.A, 3.B

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 8. Scenario Học Tập

### Tình Huống: Thiết Kế Hệ Thống Tưới Cây Thông Minh
**Bối cảnh:** Trường học muốn trồng rau sạch trong vườn trường nhưng thiếu nhân lực chăm sóc thường xuyên.

**Yêu cầu học sinh:**
1. Phân tích vấn đề (thiếu người tưới, không biết khi nào cây cần nước)
2. Thiết kế giải pháp sử dụng cảm biến độ ẩm đất
3. Vẽ flowchart điều khiển bơm tự động
4. Thiết kế vỏ bảo vệ cho hệ thống
5. Chuẩn bị thuyết trình giải pháp trước BGK

**Gợi ý:** Học sinh nên tính đến việc bảo vệ bơm không chạy khi không có nước, và giới hạn thời gian tưới để tránh ngập úng.

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

**Tài liệu được xây dựng theo chuẩn LOM v4.4 Supreme**  
**Bản quyền thuộc về Content Engineering Team**  
**Liên hệ: [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)**