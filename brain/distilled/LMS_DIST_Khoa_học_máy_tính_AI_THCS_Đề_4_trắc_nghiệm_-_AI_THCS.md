# DISTILLED KNOWLEDGE: Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS

Source: [[LMS_RAW_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS.md]] — [🚀 Xem RAW](file:///d:/NoteBookLLM_Br/brain/raw/LMS_RAW_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS.md)

---
title: DISTILLED_Khoa_học_máy_tính_AI_THCS_Đề_4
type: DISTILLED_KNOWLEDGE
---

# PHẦN 1: FACT BANK (Kiến thức chuẩn)

*   **[LMS] [Fact] :: Giao diện Dancing with AI** :: Giao diện lập trình được chia thành 7 khu vực chính: (1) Thanh công cụ, (2) Thư viện khối lệnh, (3) Khu vực lập trình, (4) Sân khấu, (5) Thông tin nhân vật, (6) Danh sách nhân vật, (7) Danh sách phông nền. :: [[Câu 1]]
*   **[LMS] [Fact] :: Khối lệnh báo cáo (Reporter Blocks)** :: Là các khối lệnh có hình oval, luôn trả về một giá trị là chuỗi ký tự hoặc giá trị số. Chúng không thể đứng độc lập mà phải được đặt bên trong các khối lệnh khác. :: [[Câu 2]]
*   **[LMS] [Fact] :: Khối lệnh Ask-Answer** :: Khối lệnh `ask` hiển thị khung nhập liệu; giá trị người dùng nhập vào được lưu trữ duy nhất trong biến `answer`. Khi có một câu hỏi `ask` mới, giá trị cũ trong `answer` sẽ bị ghi đè bởi giá trị mới. :: [[Câu 3, Câu 13]]
*   **[LMS] [Fact] :: Xử lý chuỗi (String Manipulation)** :: Khối `letter (n) of (world)` dùng để lấy ký tự tại vị trí thứ n (bắt đầu từ 1). Khối `length of (world)` dùng để đếm tổng số ký tự trong chuỗi. :: [[Câu 4, Câu 15]]
*   **[LMS] [Fact] :: Biến số (Variables)** :: Khối lệnh biến số (hình oval) có thể lưu trữ và trả về giá trị là một số, một chuỗi ký tự hoặc giá trị logic (True/False). :: [[Câu 6]]
*   **[LMS] [Fact] :: Các khái niệm AI cơ bản** :: 
    - **Artificial Intelligence (AI)**: Trí tuệ con người được mô phỏng bởi máy móc.
    - **Machine Learning**: Máy tính học từ dữ liệu để tạo mô hình dự đoán mà không cần lập trình cụ thể từng bước.
    - **Deep Learning**: Một phương pháp học máy rút ra các đặc trưng phức tạp từ dữ liệu (mô phỏng mạng thần kinh).
    - **Face Recognition**: Tự động xác định danh tính dựa trên đặc điểm khuôn mặt duy nhất. :: [[Câu 9]]
*   **[LMS] [Fact] :: Quy trình Teachable Machine** :: Quy trình chuẩn gồm 5 bước: (1) Truy cập trang web -> (2) Cung cấp dữ liệu (Webcam/Upload) -> (3) Chia nhóm và đặt tên (Classes) -> (4) Huấn luyện mô hình (Train) -> (5) Xuất và lưu trữ mô hình (Export). :: [[Câu 11]]
*   **[LMS] [Fact] :: Extension Translate & Text-to-Speech** :: 
    - `translate () to ()`: Dịch văn bản sang ngôn ngữ đích.
    - `set voice to ()`: Chọn giọng đọc (nữ, nam, mèo...).
    - `set language to ()`: Thiết lập ngôn ngữ mà máy sẽ phát âm. :: [[Câu 7, Câu 24]]
*   **[LMS] [Fact] :: Extension Sensing (Hand/Face/Body)** :: Cho phép máy tính xác định tọa độ (x, y) của các bộ phận cơ thể (ngón tay, mắt, mũi...) trên sân khấu thông qua camera. :: [[Câu 26, Câu 27]]

---

# PHẦN 2: TEST BANK (Ngân hàng đề)

### Question: Giao diện lập trình trên Dancing with AI được chia thành 7 khu vực. Hãy chọn tên phù hợp của các khu vực theo số thứ tự từ 1 đến 7.
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId7.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId7.png)
A. 1-Thanh công cụ; 2-Thư viện khối lệnh; 3-Khu vực lập trình; 4-Sân khấu; 5-Thông tin nhân vật; 6-Danh sách nhân vật; 7-Danh sách phông nền
B. 1-Sân khấu; 2-Thanh công cụ; 3-Thư viện khối lệnh; 4-Khu vực lập trình; 5-Danh sách nhân vật; 6-Thông tin nhân vật; 7-Danh sách phông nền
C. 1-Thanh công cụ; 2-Khu vực lập trình; 3-Thư viện khối lệnh; 4-Sân khấu; 5-Thông tin nhân vật; 6-Danh sách nhân vật; 7-Danh sách phông nền
D. 1-Thanh công cụ; 2-Thư viện khối lệnh; 3-Khu vực lập trình; 4-Sân khấu; 5-Danh sách nhân vật; 6-Thông tin nhân vật; 7-Danh sách phông nền
Correct: A
Explanation: Theo quy ước giao diện Scratch/Dancing with AI: 1 là Toolbar, 2 là Blocks Palette, 3 là Scripts Area, 4 là Stage, 5 là Sprite Info, 6 là Sprite List, 7 là Backdrop List.

### Question: Nhận định nào sau đây là đúng đối với các khối lệnh báo cáo?
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId8.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId8.png)
A. Luôn cho giá trị là True hoặc False
B. Luôn cho giá trị là một chuỗi ký tự hoặc giá trị số
C. Khối lệnh báo cáo còn được gọi là khối lệnh Boolean
D. Khối lệnh có thể đặt bên trên hoặc dưới khối lệnh khác
Correct: B
Explanation: Khối lệnh báo cáo (hình oval) trả về giá trị dữ liệu (số hoặc chữ). Khối hình lục giác mới là khối Boolean (True/False). Khối báo cáo không thể đứng độc lập để ghép trên/dưới mà phải nằm trong ô tham số.

### Question: Khi chạy chương trình dưới đây và người dùng nhập vào “20 + 30” vào khung trả lời, nhân vật sẽ nói gì?
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId9.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId9.png)
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId10.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId10.png)
A. Nhân vật nói: “20 + 30”
B. Nhân vật nói: “50”
C. Nhân vật nói: ”answer”
D. Nhân vật không nói gì cả do câu lệnh không có ý nghĩa
Correct: A
Explanation: Biến `answer` lưu trữ chính xác chuỗi ký tự người dùng nhập vào. Vì người dùng nhập chuỗi "20 + 30" nên máy tính hiểu đó là văn bản, không phải phép toán.

### Question: Nhân vật sẽ hiển thị gì khi sử dụng đoạn lệnh bên dưới?
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId11.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId11.png)
A. a
B. p
C. l
D. Tất cả đều sai
Correct: B
Explanation: Lệnh `letter 2 of apple` lấy ký tự thứ 2 của từ "apple", đó là chữ "p".

### Question: Cho đoạn chương trình nhân vật “Thầy bói” như hình. Đoạn lệnh nào phù hợp cho 2 nhân vật “Nút Có”, “Nút Không” để chúng xuất hiện ngay khi “Thầy bói” vừa hoàn thành câu hỏi?
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId13.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId13.png)
A. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId14.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId14.png)
B. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId15.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId15.png)
C. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId16.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId16.png)
D. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId17.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId17.png)
Correct: A
Explanation: Nhân vật Thầy bói phát tin nhắn "Hỏi xong". Do đó, các nút cần lệnh "When I receive Hỏi xong" thì mới thực hiện lệnh "show".

### Question: Nhận định nào sau đây là đúng khi nói về khối lệnh biến số (Variable) như hình? (Nhiều đáp án)
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId18.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_4_trắc_nghiệm_-_AI_THCS_rId18.png)
A. Có thể mang giá trị True hoặc False
B. Có thể mang giá trị là một chuỗi ký tự
C. Có thể mang giá trị là một số
D. Có thể đặt trên hoặc dưới câu lệnh khác
Correct: A, B, C
Explanation: Biến trong Scratch rất linh hoạt, có thể chứa số, chữ hoặc giá trị logic. Tuy nhiên, nó là khối báo cáo (oval) nên không thể ghép trên/dưới như khối lệnh thực thi (stack blocks).

### Question: Ứng dụng nào sau đây KHÔNG sử dụng công nghệ nhận diện khuôn mặt?
A. Mở khóa điện thoại thông minh
B. App filter trên camera
C. Nhận diện mọi người trên mạng xã hội
D. Phân tích thị trường chứng khoán
Correct: D
Explanation: Phân tích chứng khoán sử dụng phân tích dữ liệu số và thuật toán dự báo tài chính, không liên quan đến hình ảnh khuôn mặt.

### Question: Khối lệnh nào có chức năng phát hiện một cảm xúc trên khuôn mặt?
A. ![Image](../assets/LMS_IMG