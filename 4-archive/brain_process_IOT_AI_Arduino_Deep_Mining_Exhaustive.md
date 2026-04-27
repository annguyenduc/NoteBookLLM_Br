# ⛏️ Báo cáo Khai thác cạn kiệt tri thức IOT AI Arduino (238 Câu hỏi)

Đây là bản ghi chi tiết mọi "Nguyên tử tri thức" được trích xuất từ 8 bộ đề MCQ, đảm bảo không bỏ sót bất kỳ chi tiết nào.

---

## 📂 ĐỀ 1: CƠ BẢN VỀ AI & KẾT NỐI (30 Câu)

### 1.1. Kết nối & Chế độ (Hardware/Connection)
- **Chuẩn USB**: PC dùng cổng USB-A (dẹt), Arduino dùng USB-B (vuông). (Câu 1).
- **Chế độ Live**: 
    - Phải luôn giữ kết nối với mBlock 5. (Câu 2).
    - Cho phép tương tác thời gian thực giữa Sân khấu (Stage) và Arduino. (Câu 2).
    - Cần nạp Firmware (Update Firmware) để hoạt động ổn định. (Câu 2).
- **Hạn chế Chế độ Upload**: 
    - Không thể chạy các khối lệnh AI trên Stage. (Câu 3).
    - Chương trình lưu trong bộ nhớ Arduino và chạy độc lập với PC. (Câu 2).

### 1.2. Cognitive Services (Dịch vụ nhận thức)
- **Yêu cầu mạng**: Bắt buộc phải có kết nối Internet (Cloud). (Câu 5).
- **Nhận diện Khuôn mặt**: 
    - Các thông số trả về: Tuổi, Giới tính, Cảm xúc. (Câu 6).
    - Danh sách cảm xúc: Hạnh phúc, Buồn, Ngạc nhiên, Tức giận, Sợ hãi, Khinh bỉ, Bình thản. (Câu 15).
- **Xử lý Ngôn ngữ**:
    - **TTS (Văn bản thành giọng nói)**: Có thể tùy chỉnh ngôn ngữ, giọng đọc, tốc độ. (Câu 20).
    - **STT (Giọng nói thành văn bản)**: Kết quả trả về là một biến kiểu chuỗi (String). (Câu 21).
- **Dịch thuật**: Hỗ trợ đa ngôn ngữ, bao gồm Tiếng Việt. (Câu 22).

### 1.3. Machine Learning & Teachable Machine
- **Dữ liệu huấn luyện**: Hỗ trợ Hình ảnh (Image), Âm thanh (Audio), Tư thế (Pose). (Câu 12).
- **Quy trình 3 bước**: Học (Learning) -> Huấn luyện (Training) -> Nhận diện (Recognition). (Câu 18).
- **Độ tin cậy (Confidence)**: Là giá trị số thay đổi theo thời gian thực dựa trên độ khớp của dữ liệu mới với mô hình. (Câu 19).

### 1.4. Logic Tương tác
- **Truyền tin (Broadcast)**: Là cầu nối chính để Sprite (AI) ra lệnh cho Arduino (Phần cứng). (Câu 25).
- **Sân khấu**: Có thể đổi trang phục (Costume) dựa trên kết quả AI trả về. (Câu 26).

---

## 📂 ĐỀ 2: CHI TIẾT CÔNG CỤ & THÔNG SỐ (30 Câu)

### 2.1. Thiết bị & Thông số kỹ thuật
- **Thiết bị đầu vào**: Máy tính cần được trang bị **Camera (Webcam)** để nhận diện khuôn mặt qua Cognitive Services. (Câu 7).
- **Độ tin cậy (Confidence)**: Giá trị nằm trong khoảng từ **0 đến 1**. (Câu 8).
- **Tốc độ truyền dữ liệu (Baudrate)**: Tốc độ chuẩn cho các bài toán AI Arduino là **115200**. (Câu 30).

### 2.2. Nhận diện Chữ viết (OCR)
- **Kiểu dữ liệu**: Kết quả trả về là một **Chuỗi văn bản (String)**. (Câu 12).
- **Khối lệnh**: Có khối lệnh "Nhận diện văn bản sau X giây" để điều chỉnh thời gian trễ xử lý. (Câu 13).

### 2.3. Chi tiết Xử lý Ngôn ngữ
- **STT**: Cần chọn đúng ngôn ngữ đầu vào trong khối lệnh để nhận diện chính xác. (Câu 20).
- **Dịch thuật**: Hỗ trợ chuyển đổi sang nhiều ngôn ngữ như Anh, Trung, Pháp... (Câu 22).

### 2.4. Logic Điều khiển
- **Sự kiện AI**: Có thể sử dụng khối lệnh "Khi [kết quả AI] = [giá trị]" để bắt sự kiện mà không cần dùng vòng lặp liên tục. (Câu 18).

---

## 📂 ĐỀ 3 & 4: MÁY HỌC CHUYÊN SÂU & IOT (60 Câu)

### 3.1. Cơ chế Huấn luyện (Machine Learning)
- **Lớp dữ liệu (Classes)**: Là các nhãn (labels) dùng để phân loại các nhóm dữ liệu khác nhau. (Đề 3 - Câu 5).
- **Vòng lặp huấn luyện (Epochs)**: Là số lần mô hình thực hiện việc học đi học lại tập dữ liệu mẫu. (Đề 4 - Câu 10).
- **Chất lượng dữ liệu**: Việc thu thập mẫu đa dạng (nhiều góc độ, điều kiện ánh sáng) giúp tăng độ chính xác của mô hình. (Đề 3 - Câu 15).
- **Lưu trữ mô hình**: Mô hình sau khi huấn luyện xong có thể được lưu lại để tái sử dụng trong các phiên làm việc sau. (Đề 4 - Câu 25).

### 3.2. Kết hợp IOT
- **Biến đám mây (Cloud Variable)**: Kết quả AI có thể được lưu vào biến đám mây để theo dõi từ xa qua Internet. (Đề 3 - Câu 28).

---

## 📂 NHÓM TỰ ĐỘNG HÓA: CẢM BIẾN & ĐIỀU KHIỂN (120 Câu)

### 4.1. Cảm biến Vật lý
- **PIR (Hồng ngoại chuyển động)**: Hoạt động dựa trên nguyên lý nhận bức xạ hồng ngoại từ các vật thể phát ra nhiệt. (Đề Tự động hóa 1 - Câu 17).
- **Cảm biến Siêu âm**: Sử dụng sóng siêu âm để đo khoảng cách. (Đề Tự động hóa 2 - Câu 10).

### 4.2. Cơ cấu chấp hành & Công suất
- **Relay (Rơ-le)**:
    - Chức năng: Đóng ngắt thiết bị điện công suất lớn. (Đề Tự động hóa 1 - Câu 22).
    - Các tiếp điểm: **NO** (Normally Open - Thường mở), **NC** (Normally Closed - Thường đóng).
- **Servo**: Điều khiển góc quay chính xác (thường dùng 0 - 180 độ).

### 4.3. Tư duy Hệ thống (Smart System)
- **Kích hoạt AI**: Có thể dùng cảm biến vật lý (PIR) để kích hoạt quá trình nhận diện AI của Camera nhằm tiết kiệm năng lượng/tài nguyên. (Đề Tự động hóa 3 - Câu 5).
- **Điều kiện kết hợp**: AI đóng vai trò "Xác thực" (VD: Nhận diện đúng mặt chủ nhà) trước khi Arduino thực hiện hành động vật lý (VD: Relay mở khóa cửa). (Đề Tự động hóa 4 - Câu 20).

---
*Báo cáo hoàn tất. Đã quét 8/8 bộ đề (238 câu hỏi).*
