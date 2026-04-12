---
file_id: CONV_Atoms_atoms_v01_11
category: Uncategorized
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms atoms v01 11

# Tài liệu Học tập: Thiết kế 3D và In 3D Cơ bản với Tinkercad & Cura
**Phiên bản:** LOM v4.4 Supreme  
**Ngôn ngữ:** Tiếng Việt  
**Chủ đề:** Thiết kế 3D, In 3D, Tinkercad, Cura  

---

## Mục tiêu Học tập
Sau khi hoàn thành bài học này, học sinh sẽ có thể:
- Đăng nhập vào lớp học Tinkercad sử dụng Class code và nickname.
- Sử dụng các công cụ cơ bản trong Tinkercad để thiết kế mô hình 3D.
- Áp dụng các kỹ thuật thiết kế như tạo lỗ, căn chỉnh, nhóm đối tượng.
- Xuất file STL và chuẩn bị mô hình để in 3D bằng phần mềm Cura.
- Hiểu và điều chỉnh các thông số cơ bản trong Cura để tối ưu hóa quá trình in.

---

## Nội dung Bài học

### 1. Giới thiệu về Tinkercad

Tinkercad là một nền tảng thiết kế 3D trực tuyến miễn phí, thân thiện với người mới bắt đầu. Giao diện đơn giản giúp học sinh dễ dàng tạo ra các mô hình 3D cơ bản phục vụ cho học tập và in ấn.

#### 1.1. Đăng nhập vào lớp học
- Giáo viên cần cung cấp **Class code** và **nickname** để học sinh đăng nhập vào lớp học [vv01].
- Học sinh truy cập trang tinkercad.com, chọn "Classes", nhập Class code và nickname để tham gia.

#### 1.2. Giao diện và các tính năng cơ bản
- **Learning Center**: Nơi cung cấp các bài học và hướng dẫn tự học [vv01].
- **Gallery**: Thư viện tham khảo thiết kế từ các tài khoản khác [vv01].
- **Workplane**: Mặt phẳng làm việc chính để đặt và thiết kế các đối tượng.

#### 1.3. Điều hướng trong không gian 3D
- **Xoay và thay đổi góc nhìn**: Nhấn giữ chuột phải và di chuyển chuột [vv01].
- **Trở về góc nhìn mặc định**: Sử dụng công cụ "Home" (biểu tượng ngôi nhà) [vv01].

---

### 2. Các công cụ và thao tác cơ bản trong Tinkercad

#### 2.1. Phím tắt hữu ích
| Phím tắt | Chức năng |
|----------|-----------|
| Ctrl+C | Sao chép đối tượng |
| Ctrl+V | Dán đối tượng |
| Ctrl+D | Nhân bản đối tượng |
| Ctrl+G | Nhóm các đối tượng |
| Ctrl+Shift+G | Bỏ nhóm đối tượng |
| Ctrl+Z | Hoàn tác |
| Ctrl+H | Ẩn đối tượng |
[Source: v01 - Section: Mẫu dữ liệu trong sheet Questions - Q6] [vv01]

#### 2.2. Di chuyển và định vị đối tượng
- **Nâng/hạ đối tượng**: Kéo mũi tên màu đen phía trên vật thể hoặc dùng tổ hợp phím **Ctrl + mũi tên lên/xuống** [vv01].
- **Xoay đối tượng**: Sử dụng thanh trượt góc hoặc nhập trực tiếp giá trị vào ô chỉ số góc. Để đưa đối tượng về vị trí góc ban đầu, nhập giá trị **0** vào ô chỉ số góc [vv01].

#### 2.3. Chọn nhiều đối tượng
- **Chọn riêng lẻ**: Nhấn giữ phím **Shift** và click chuột trái vào từng đối tượng [vv01].
- **Công cụ Nhóm và Căn chỉnh**: Chỉ khả dụng khi chọn từ **hai đối tượng trở lên** [vv01].

#### 2.4. Kỹ thuật "Duplicate and Repeat"
- Khi sử dụng **Ctrl+D** để nhân bản, người dùng **không được bỏ chọn đối tượng** sau khi nhấn phím và thực hiện thao tác biến đổi đầu tiên [vv01].

---

### 3. Kỹ thuật thiết kế nâng cao

#### 3.1. Tạo lỗ trống trong đối tượng
- Tạo một bản sao có kích thước nhỏ hơn đối tượng chính.
- Chuyển đối tượng nhỏ sang chế độ **"Hole"**.
- Thực hiện lệnh **Group** với đối tượng chính để tạo lỗ [vv01].

#### 3.2. Kỹ thuật "Dog-bone relief"
- Thêm các lỗ tròn nhỏ (r ≈ 0.3–0.5 mm) tại các góc trong của mô hình để giúp các chi tiết có góc vuông lắp lọt vào lỗ in FDM dễ dàng hơn do hạn chế của vòi phun khi tạo góc vuông tuyệt đối [vv01].

---

### 4. Giới thiệu về phần mềm Cura

Cura là phần mềm slicer phổ biến được sử dụng để chuẩn bị mô hình 3D cho quá trình in. Nó chuyển đổi file STL thành các lệnh mà máy in 3D có thể hiểu và thực hiện.

#### 4.1. Chế độ "Uniform Scaling"
- Đảm bảo tỷ lệ giữa các trục (X, Y, Z) được giữ nguyên khi thay đổi kích thước của một trục bất kỳ [vv01].

#### 4.2. Các thông số tối ưu hóa tốc độ in
- **Giảm độ đặc (infill)**: Giảm mật độ vật liệu bên trong mô hình.
- **Tăng bề dày lớp in (layer height)**: Giảm số lượng lớp cần in.
- **Tăng tốc độ in (print speed)**: Tăng tốc độ di chuyển của đầu in [vv01].

#### 4.3. Chế độ bám dính bàn in
- **Skirt**: Vết in xung quanh mô hình, giúp kiểm tra đầu phun.
- **Brim**: Vết in dính trực tiếp vào mô hình, tăng độ bám.
- **Raft**: Lớp đệm dưới mô hình, phù hợp với các bề mặt khó bám [vv01].

---

### 5. Điều chỉnh bản vẽ cho phù hợp với máy in FDM

#### 5.1. Kích thước lỗ và trục
- Khi thiết lập **Horizontal Expansion = +0.125 mm**, biên XY sẽ dịch ra ngoài 0.125 mm mỗi phía, dẫn đến:
  - Kích thước ngoài tăng **+0.25 mm**.
  - Kích thước lỗ/rãnh giảm **-0.25 mm** [vv01].
- Đối với trục có đường kính **Ø2.00 mm**, kích thước thiết kế trên CAD được gợi ý là **2.35 mm - 2.45 mm** để đạt được độ lắp vừa (snug fit) [vv01].

---

## Bài tập Thực hành

### Bài 1: Tạo mô hình đơn giản
1. Đăng nhập vào lớp học Tinkercad sử dụng Class code và nickname được cung cấp.
2. Tạo một khối lập phương và một hình trụ.
3. Di chuyển hình trụ lên trên khối lập phương.
4. Nhóm hai đối tượng lại với nhau.
5. Xuất file STL và lưu lại.

### Bài 2: Tạo lỗ trống
1. Tạo một khối lập phương lớn.
2. Tạo một khối lập phương nhỏ hơn, đặt bên trong khối lớn.
3. Chuyển khối nhỏ sang chế độ "Hole".
4. Nhóm hai khối lại để tạo lỗ trống.
5. Xuất file STL.

### Bài 3: Sử dụng Cura
1. Mở file STL đã tạo trong Cura.
2. Điều chỉnh các thông số: infill, layer height, print speed.
3. Xem trước quá trình in và xuất file G-code.

---

## Kiểm tra Đánh giá

### Câu hỏi Trắc nghiệm
1. Để đăng nhập vào lớp học Tinkercad, học sinh cần cung cấp những thông tin nào?
   - A. Email và mật khẩu
   - B. Class code và nickname
   - C. Tên người dùng và mật khẩu
   - D. Mã xác nhận và email

2. Phím tắt nào được sử dụng để nhân bản đối tượng trong Tinkercad?
   - A. Ctrl+C
   - B. Ctrl+V
   - C. Ctrl+D
   - D. Ctrl+G

3. Chế độ nào trong Cura giúp tăng độ bám của mô hình vào bàn in?
   - A. Skirt
   - B. Brim
   - C. Raft
   - D. Tất cả đều đúng

### Câu hỏi Tự luận
1. Giải thích kỹ thuật "dog-bone relief" và tại sao nó quan trọng trong thiết kế cho in 3D FDM.
2. Mô tả quy trình từ thiết kế mô hình 3D trong Tinkercad đến khi in ra thành phẩm bằng máy in FDM.

---

## Tài nguyên Hỗ trợ

- [Hướng dẫn sử dụng Tinkercad](https://www.tinkercad.com/learn)
- [Tài liệu Cura chính thức](https://ultimaker.com/software/cura)
- [Video hướng dẫn thiết kế 3D cơ bản](https://www.youtube.com/watch?v=example_video)

---

## Ghi chú và Dẫn nguồn

- Mọi sự kiện và kiến thức trong tài liệu này đều được dẫn nguồn từ: [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) [vv01]
- Hình ảnh minh họa: ![Giao diện Tinkercad](../../brain/raw/lms_multi_media_dump/assets/CONV_Atoms_atoms_v01_11_image1.png)
- Hình ảnh minh họa: ![Giao diện Cura](../../brain/raw/lms_multi_media_dump/assets/CONV_Atoms_atoms_v01_11_image2.png)

---

**Tài liệu được tạo bởi @engineer - Content Engineer**  
**Ngày tạo:** 2025-04-05  
**Phiên bản:** 1.0