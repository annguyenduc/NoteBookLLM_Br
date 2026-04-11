# ĐỀ KIỂM TRA TRẮC NGHIỆM: AI & Teachable Machine
(Bộ đề chuyên sâu - THCS)

- 10 câu hỏi mẫu (đủ các cấp độ nhận thức)
- Thời gian làm bài: 15 phút
- Nguồn dữ liệu đối soát: `LMS_KB_AI_DEEP.md`

| Nhóm kiến thức | Nhận biết (4 câu) | Thông hiểu / Vận dụng (6 câu) |
| :--- | :--- | :--- |
| Quy trình Teachable Machine | 1, 2 | 5, 8 |
| Các loại mô hình (Image/Pose/Sound) | 3 | 6, 9 |
| Lập trình mBlock M-Learning | 4 | 7, 10 |

---

### Câu 1 (Nhận biết)
Quy trình chuẩn để huấn luyện một mô hình trong Teachable Machine gồm 3 bước chính theo thứ tự nào?
- A/ Train -> Collect -> Export
- B/ Collect -> Train -> Export
- C/ Export -> Collect -> Train
- D/ Train -> Export -> Collect

### Câu 2 (Nhận biết)
Trong bước "Collect" (Thu thập dữ liệu), chúng ta cần làm gì?
- A/ Viết code điều khiển Robot
- B/ Chụp ảnh hoặc ghi âm các mẫu vật thể để dạy cho máy
- C/ Tải mô hình về máy tính
- D/ Xóa các dữ liệu cũ của Google

### Câu 3 (Nhận biết)
Teachable Machine hỗ trợ huấn luyện những loại mô hình nhận diện nào sau đây?
(Nhiều đáp án)
- A/ Image Project (Hình ảnh)
- B/ Audio Project (Âm thanh)
- C/ Pose Project (Tư thế)
- D/ Smell Project (Mùi vị)

### Câu 4 (Nhận biết)
Để sử dụng mô hình AI đã huấn luyện trên mBlock 5, chúng ta cần thêm nhóm lệnh mở rộng nào?
- A/ Cognitive Services
- B/ M-Learning
- C/ Teachable Machine Editor
- D/ AI Maker

### Câu 5 (Thông hiểu)
Tại sao khi huấn luyện mô hình nhận diện "Cái kéo", nếu bạn chỉ chụp 2-3 tấm ảnh thì máy thường nhận diện sai?
- A/ Vì máy tính không thích cái kéo
- B/ Vì dữ liệu quá ít, máy chưa đủ thông tin để học các góc độ khác nhau của vật thể
- C/ Vì camera bị hỏng
- D/ Vì Teachable Machine chỉ chạy được với 1000 tấm ảnh trở lên

### Câu 6 (Thông hiểu)
Sự khác biệt chính giữa "Image Project" và "Pose Project" là gì?
- A/ Image nhận diện màu sắc, Pose nhận diện âm thanh
- B/ Image nhận diện toàn bộ vật thể, Pose tập trung vào các khớp xương và tư thế cơ thể của con người
- C/ Không có sự khác biệt nào
- D/ Pose chỉ dùng được trên điện thoại

### Câu 7 (Thông hiểu)
Quan sát đoạn mã sau trong mBlock:
`Nếu [M-Learning] nhận diện là [Class 1] thì nhân vật nói [Xin chào]`
Nếu máy đang nhận diện vật thể nhưng nhân vật không nói gì, nguyên nhân có thể là?
- A/ Chưa bật loa máy tính
- B/ Chưa kết nối Bluetooth giữa mBlock và mô hình TM
- C/ Vật thể trước camera không thuộc [Class 1] hoặc mô hình chưa được tải (Load) vào mBlock
- D/ Nhân vật đang bị ẩn

### Câu 8 (Vận dụng)
Trong quá trình "Train" (Huấn luyện), nếu bạn thấy chỉ số Accuracy (Độ chính xác) rất thấp, bạn nên thực hiện hành động nào để cải thiện?
- A/ Xóa toàn bộ dự án và làm lại
- B/ Quay lại bước Collect để bổ sung thêm nhiều mẫu ảnh đa dạng hơn và xóa các ảnh bị nhòa
- C/ Ngắt kết nối Internet
- D/ Đổi sang dùng Scratch 3.0

### Câu 9 (Thông hiểu)
Khi sử dụng mô hình "Audio Project", yếu tố nào sau đây sẽ làm giảm độ chính xác của việc nhận diện câu lệnh?
- A/ Phòng quá sáng
- B/ Có quá nhiều tiếng ồn trắng (background noise) lẫn vào khi thu âm mẫu
- C/ Micro có màu đỏ
- D/ Sử dụng tai nghe

### Câu 10 (Vận dụng)
Bạn muốn lập trình một ứng dụng: "Khi máy thấy học sinh giơ tay thì robot sẽ dừng lại". Bạn nên sử dụng sự kết hợp nào?
- A/ Audio Project + Nhóm lệnh Pen
- B/ Pose Project + Nhóm lệnh M-Learning
- C/ Image Project + Nhóm lệnh Music
- D/ Text Project + Nhóm lệnh Sensing

---
**📖 Nguồn đối soát: [LMS_KB_AI_DEEP.md](file:///d:/NoteBookLLM_Br/brain/distilled/LMS_KB_AI_DEEP.md) — Sections: 5, 12, 38, 45.**
