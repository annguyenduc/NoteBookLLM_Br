---
file_id: LMS_KB_AI_V4.1
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS KB AI V4.1

# 🤖 NỘI DUNG DAO TẠO: TRÍ TUỆ NHÂN TẠO VÀ ROBOTICS (LOM v4.4 Supreme)

---

## 📚 MÔ TẢ KHÓA HỌC

| **Thông tin** | **Chi tiết** |
|---------------|--------------|
| **Tên khóa học** | Trí tuệ nhân tạo và Robotics |
| **Mã học phần** | AI4ROBOTS |
| **Thời lượng** | 60 giờ (45 giờ lý thuyết + 15 giờ thực hành) |
| **Đối tượng** | Học sinh THCS/THPT |
| **Ngôn ngữ giảng dạy** | Tiếng Việt |
| **Mức độ** | Cơ bản đến trung cấp |
| **Loại hình** | Lý thuyết kết hợp thực hành |
| **Phương pháp** | Dạy học dự án, học qua trải nghiệm |

---

## 🎯 MỤC TIÊU HỌC TẬP

### **Mục tiêu chung**
Khóa học nhằm trang bị cho học sinh kiến thức nền tảng về trí tuệ nhân tạo và robotics, đồng thời phát triển kỹ năng tư duy phản biện, giải quyết vấn đề và làm việc nhóm.

### **Mục tiêu cụ thể**
Sau khóa học, học sinh có thể:

| **Mức độ** | **Kỹ năng** | **Mô tả chi tiết** |
|------------|-------------|-------------------|
| **Hiểu biết** | Kiến thức cơ bản | Giải thích được các khái niệm cơ bản về AI, học máy, và robotics [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |
| **Vận dụng** | Thực hành kỹ thuật | Thiết kế và lập trình robot đơn giản tích hợp AI [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |
| **Phân tích** | Đánh giá hiệu suất | Phân tích và đánh giá hiệu suất mô hình AI trong các tình huống thực tế [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |
| **Sáng tạo** | Phát triển dự án | Xây dựng dự án AI/Robotics giải quyết vấn đề cụ thể [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |

---

## 🧩 NỘI DUNG CHI TIẾT

### **Bài 1: Giới thiệu về AI và Robotics**

#### **1.1. Khái niệm AI**
- **AI (Trí tuệ nhân tạo)**: Hệ thống máy tính có khả năng thực hiện các nhiệm vụ thường yêu cầu trí thông minh con người [[vv01]]
- **Học máy (Machine Learning)** và **Học sâu (Deep Learning)**: Các phương pháp huấn luyện mô hình từ dữ liệu [[vv21]]
- **Ứng dụng AI trong Robotics**: Tích hợp AI để robot có khả năng nhận thức và ra quyết định [[vv01]]

#### **1.2. Khái niệm Robotics**
- **Định nghĩa và lĩnh vực liên ngành**: Khoa học và kỹ thuật thiết kế, xây dựng và vận hành robot [[vv01]]
- **Các thành phần cơ bản của robot**: Cảm biến, bộ điều khiển, cơ cấu chấp hành, phần mềm điều khiển [[vv01]]

#### **1.3. Hệ sinh thái phần cứng**
- **YoloBit, Arduino, Halocode**: Các nền tảng lập trình nhúng phổ biến [[vv01]]
- **OhStem, Rover V2**: Bộ kit robotics dành cho giáo dục [[vv08]]

---

### **Bài 2: Cảm biến và dữ liệu trong AI**

#### **2.1. Các loại cảm biến phổ biến**
- **DHT11/LM35** (nhiệt độ), **HC-SR04** (siêu âm), **PIR** (chuyển động), **MPU-6050** (gia tốc), **MQ-2** (khí gas) [[vv01]]
- **Sóng siêu âm và ứng dụng**: Nguyên lý hoạt động và ứng dụng trong đo khoảng cách [[vv22]]

#### **2.2. Thu thập và xử lý dữ liệu**
- **Tiền xử lý dữ liệu**: Làm sạch, chuẩn hóa, chuẩn bị dữ liệu cho huấn luyện [[vv24]]
- **Xử lý giá trị thiếu (NaN)**: Phương pháp xử lý dữ liệu bị thiếu hoặc lỗi [[vv23]]

---

### **Bài 3: Học máy cơ bản**

#### **3.1. Phân loại và hồi quy**
- **Phân biệt giữa Regression và Classification**: Hai loại bài toán chính trong học máy [[vv23]]
- **Linear Regression**: Mô hình tuyến tính cho bài toán hồi quy [[vv23]]
- **Logistic Regression**: Mô hình cho bài toán phân loại nhị phân [[vv23]]

#### **3.2. Phân cụm**
- **K-means clustering**: Thuật toán phân cụm không giám sát [[vv23]]

#### **3.3. Đánh giá mô hình**
- **Accuracy, Precision, Recall, F1-score**: Các chỉ số đánh giá mô hình phân loại [[vv04]]
- **MSE, R-squared**: Các chỉ số đánh giá mô hình hồi quy [[vv23]]

---

### **Bài 4: TinyML và AI trên thiết bị nhúng**

#### **4.1. Giới thiệu TinyML**
- **Định nghĩa và mục tiêu**: AI trên thiết bị vi điều khiển có tài nguyên hạn chế [[vv01]]
- **Ứng dụng: Magic Wand (đũa phép AI)**: Ví dụ minh họa ứng dụng TinyML [[vv01]]

#### **4.2. Kỹ thuật tối ưu mô hình**
- **Lượng tử hóa (quantization)**: Giảm kích thước mô hình bằng cách giảm độ chính xác [[vv01]]
- **Cắt tỉa (pruning)**: Loại bỏ các thành phần không cần thiết trong mô hình [[vv02]]

#### **4.3. Framework hỗ trợ**
- **TensorFlow Lite for Microcontrollers (TFLM)**: Framework chạy AI trên vi điều khiển [[vv01]]
- **Edge Impulse**: Nền tảng phát triển AI cho thiết bị IoT [[vv01]]

---

### **Bài 5: Lập trình AI với Python**

#### **5.1. Ngôn ngữ Python trong AI**
- **Python là nền tảng**: Ngôn ngữ lập trình phổ biến trong AI và khoa học dữ liệu [[vv01]]
- **Quản lý phiên bản Python**: Công cụ quản lý môi trường và thư viện [[vv01]]

#### **5.2. Thư viện AI phổ biến**
- **scikit-learn, NumPy, Pandas**: Thư viện cơ bản cho xử lý dữ liệu và học máy [[vv23]]
- **OpenCV, TensorFlow**: Thư viện cho thị giác máy tính và học sâu [[vv03]]

#### **5.3. Xây dựng mô hình đơn giản**
- **Linear Regression từ đầu**: Hiểu bản chất thuật toán [[vv25]]
- **KNN và K-means**: Các thuật toán cơ bản trong học máy [[vv25]]

---

### **Bài 6: Tích hợp AI vào hệ thống nhúng**

#### **6.1. Giao tiếp giữa AI và vi điều khiển**
- **Teachable Machine + Serial Communication**: Tích hợp mô hình AI với phần cứng [[vv01]]
- **Web Serial Bridge**: Kết nối trình duyệt với thiết bị phần cứng [[vv01]]

#### **6.2. Giao thức IoT**
- **MQTT, Wi-Fi**: Giao thức truyền thông trong hệ thống IoT [[vv01]]
- **Dashboard IoT (OhStem)**: Giao diện giám sát và điều khiển từ xa [[vv01]]

#### **6.3. Cơ chế an toàn (Fail-safe)**
- **Timeout, Lockout, Manual Override**: Các cơ chế đảm bảo an toàn hệ thống [[vv04]]
- **Hysteresis chống nhấp nháy**: Kỹ thuật ổn định tín hiệu đầu ra [[vv02]]

---

### **Bài 7: Thiết kế dự án AI/Robotics**

#### **7.1. Quy trình thiết kế**
- **Phân tích – Thiết kế – Phát triển – Triển khai – Đánh giá (ADDIE)**: Quy trình phát triển học tập [[vv03]]

#### **7.2. Phương pháp sư phạm**
- **5E (Engage–Explore–Explain–Elaborate–Evaluate)**: Mô hình dạy học trải nghiệm [[vv03]]
- **Dạy học dự án (Project-based learning)**: Học qua thực hiện dự án thực tế [[vv03]]

#### **7.3. Ví dụ dự án**
- **Robot nhận diện vật thể**: Tự động phân loại và xử lý vật thể [[vv19]]
- **Hệ thống điều khiển ánh sáng thông minh**: Tự động điều chỉnh ánh sáng theo môi trường [[vv02]]

---

## 📋 WORKSHEET HỌC TẬP

### **Worksheet 1: Thiết lập môi trường lập trình**

**Mục tiêu:** Cài đặt và cấu hình môi trường phát triển cho AI và Robotics

**Nhiệm vụ:**
1. Cài đặt Python 3.8 trở lên
2. Cài đặt Arduino IDE và các thư viện hỗ trợ
3. Cài đặt thư viện Python: `numpy`, `pandas`, `tensorflow`
4. Kết nối phần cứng: YoloBit, cảm biến DHT11, HC-SR04
5. Kiểm tra kết nối và truyền nhận dữ liệu cơ bản

**Đánh giá:**
- ✅ Môi trường lập trình hoạt động tốt
- ✅ Kết nối phần cứng thành công
- ✅ Truyền nhận dữ liệu ổn định

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### **Worksheet 2: Thu thập dữ liệu cảm biến**

**Mục tiêu:** Thu thập và xử lý dữ liệu từ các cảm biến phổ biến

**Nhiệm vụ:**
1. Lập trình đọc dữ liệu từ cảm biến DHT11 (nhiệt độ, độ ẩm)
2. Lập trình đọc dữ liệu từ cảm biến HC-SR04 (khoảng cách)
3. Ghi dữ liệu vào file CSV
4. Hiển thị dữ liệu trên serial monitor
5. Phân tích sơ bộ dữ liệu thu thập được

**Đánh giá:**
- ✅ Đọc dữ liệu chính xác
- ✅ Ghi dữ liệu thành file
- ✅ Xử lý dữ liệu thiếu (nếu có)

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### **Worksheet 3: Huấn luyện mô hình đơn giản**

**Mục tiêu:** Sử dụng công cụ trực tuyến để huấn luyện mô hình AI

**Nhiệm vụ:**
1. Sử dụng Teachable Machine để tạo mô hình phân loại hình ảnh
2. Thu thập dữ liệu huấn luyện (ít nhất 100 mẫu mỗi lớp)
3. Huấn luyện mô hình với độ chính xác > 85%
4. Xuất mô hình dưới dạng TensorFlow.js
5. Kiểm thử mô hình với dữ liệu mới

**Đánh giá:**
- ✅ Mô hình đạt độ chính xác yêu cầu
- ✅ Có thể phân loại đúng dữ liệu mới
- ✅ Mô hình được xuất thành công

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### **Worksheet 4: Tích hợp mô hình vào vi điều khiển**

**Mục tiêu:** Chạy mô hình AI trên thiết bị nhúng và tích hợp với hệ thống IoT

**Nhiệm vụ:**
1. Chuyển đổi mô hình sang TensorFlow Lite
2. Nạp mô hình vào ESP32
3. Thiết lập giao tiếp serial giữa PC và ESP32
4. Gửi kết quả phân loại lên dashboard OhStem
5. Tạo giao diện điều khiển từ xa

**Đánh giá:**
- ✅ Mô hình chạy ổn định trên ESP32
- ✅ Giao tiếp serial hoạt động
- ✅ Dữ liệu hiển thị trên dashboard

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### **Worksheet 5: Dự án cuối khóa**

**Mục tiêu:** Xây dựng dự án hoàn chỉnh tích hợp AI và Robotics

**Yêu cầu:**
- Làm việc theo nhóm 2-3 người
- Dự án phải tích hợp ít nhất 2 cảm biến
- Dự án phải có thành phần AI (phân loại, hồi quy, hoặc điều khiển)
- Có giao diện giám sát và điều khiển
- Có cơ chế an toàn fail-safe

**Ví dụ dự án:**
- Robot tránh vật cản thông minh
- Hệ thống phân loại rác tự động
- Robot nhận diện và theo dõi vật thể
- Hệ thống an ninh thông minh

**Đánh giá:**
- ✅ Ý tưởng sáng tạo và thực tế
- ✅ Công nghệ được áp dụng hiệu quả
- ✅ Hệ thống hoạt động ổn định
- ✅ Có cơ chế an toàn đầy đủ

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 🧪 QUIZ ĐÁNH GIÁ

### **Quiz 1: Khái niệm AI và Robotics**

**Thời gian:** 30 phút  
**Hình thức:** Trắc nghiệm và tự luận ngắn

**Câu hỏi:**

1. **AI là gì?** [[vv21]]
   - A. Artificial Intelligence
   - B. Automatic Interface
   - C. Advanced Internet
   - D. Applied Informatics

2. **Học máy khác học sâu như thế nào?** [[vv01]]
   - A. Học sâu là một nhánh của học máy
   - B. Học máy là một nhánh của học sâu
   - C. Chúng là hai lĩnh vực độc lập
   - D. Không có sự khác biệt

3. **Cảm biến PIR hoạt động như thế nào?** [[vv03]]
   - A. Đo sóng siêu âm
   - B. Phát hiện bức xạ hồng ngoại
   - C. Đo điện trở
   - D. Đo từ trường

4. **Viết định nghĩa ngắn gọn về robotics.** [[vv01]]

5. **Liệt kê 3 thành phần cơ bản của robot.** [[vv01]]

**Đáp án:**
1. A
2. A
3. B
4. Robotics là lĩnh vực nghiên cứu và phát triển các hệ thống robot tự động, bao gồm cả phần cứng và phần mềm.
5. Cảm biến, bộ điều khiển, cơ cấu chấp hành

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### **Quiz 2: Học máy cơ bản**

**Thời gian:** 30 phút  
**Hình thức:** Trắc nghiệm và tự luận ngắn

**Câu hỏi:**

1. **Phân biệt hồi quy và phân loại.** [[vv23]]
   - A. Hồi quy dự đoán giá trị liên tục, phân loại dự đoán lớp rời rạc
   - B. Phân loại dự đoán giá trị liên tục, hồi quy dự đoán lớp rời rạc
   - C. Không có sự khác biệt
   - D. Cả hai đều dự đoán lớp rời rạc

2. **Viết công thức Linear Regression.** [[vv25]]
   - A. y = mx + b
   - B. y = ax² + bx + c
   - C. y = sin(x)
   - D. y = e^x

3. **Giải thích ý nghĩa của MSE.** [[vv23]]
   - A. Mean Squared Error - sai số bình phương trung bình
   - B. Maximum Squared Error - sai số bình phương tối đa
   - C. Minimum Squared Error - sai số bình phương tối thiểu
   - D. Mean Standard Error - sai số chuẩn trung bình

4. **K-means là thuật toán gì?** [[vv23]]

5. **Accuracy là gì? Cho ví dụ minh họa.** [[vv04]]

**Đáp án:**
1. A
2. A
3. A
4. K-means là thuật toán phân cụm không giám sát, chia dữ liệu thành k nhóm dựa trên khoảng cách.
5. Accuracy là tỷ lệ số dự đoán đúng trên tổng số dự đoán. Ví dụ: nếu có 100 dự đoán thì 85 đúng, accuracy là 85%.

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### **Quiz 3: TinyML và IoT**

**Thời gian:** 30 phút  
**Hình thức:** Trắc nghiệm và tự luận ngắn

**Câu hỏi:**

1. **TinyML là gì?** [[vv01]]
   - A. AI trên thiết bị vi điều khiển
   - B. AI trên máy tính cá nhân
   - C. AI trên điện thoại
   - D. AI trên máy chủ

2. **Các kỹ thuật tối ưu mô hình TinyML?** [[vv02]]
   - A. Lượng tử hóa và cắt tỉa
   - B. Tăng cường dữ liệu
   - C. Chọn đặc trưng
   - D. Tất cả các đáp án trên

3. **Vai trò của MQTT trong IoT?** [[vv01]]
   - A. Giao thức truyền thông nhẹ
   - B. Giao thức truyền hình ảnh
   - C. Giao thức âm thanh
   - D. Giao thức video

4. **Giải thích tại sao cần tối ưu mô hình cho thiết bị nhúng.** [[vv01]]

5. **Liệt kê 3 lợi ích của TinyML.** [[vv01]]

**Đáp án:**
1. A
2. A
3. A
4. Thiết bị nhúng có tài nguyên hạn chế (RAM, ROM, CPU), nên cần tối ưu mô hình để phù hợp.
5. Tiết kiệm năng lượng, xử lý cục bộ, bảo mật dữ liệu, chi phí thấp.

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 🎭 TÌNH HUỐNG MINH HỌA

### **Scenario: Robot giao hàng thông minh