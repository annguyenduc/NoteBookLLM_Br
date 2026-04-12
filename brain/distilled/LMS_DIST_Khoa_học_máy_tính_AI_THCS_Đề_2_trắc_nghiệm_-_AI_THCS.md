# DISTILLED KNOWLEDGE: Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS

Source: [[LMS_RAW_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS.md]] — [🚀 Xem RAW](file:///d:/NoteBookLLM_Br/brain/raw/LMS_RAW_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS.md) — [🚀 Xem RAW](file:///d:/NoteBookLLM_Br/brain/raw/LMS_RAW_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS.md)

---
title: Tri thức chưng cất - Đề 2 Trắc nghiệm AI THCS
source: [[LMS_RAW_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS.md]]
type: DISTILLED_KNOWLEDGE
---

# PHẦN 1: FACT BANK (Kiến thức chuẩn)

*   **[LMS] [Fact] :: Giao diện lập trình Dancing with AI/Scratch** :: Giao diện gồm 7 khu vực chính: (1) Thanh công cụ - Toolbar, (2) Thư viện khối lệnh - Blocks palette, (3) Khu vực lập trình - Scripts area, (4) Sân khấu - Stage, (5) Thông tin nhân vật - Sprite info, (6) Danh sách nhân vật - Sprite list, (7) Danh sách phông nền - Backdrop list. :: [[Câu 2]]
*   **[LMS] [Fact] :: Tương tác người dùng với khối lệnh Ask-Answer** :: Khối lệnh `ask [văn bản] and wait` dùng để hiển thị câu hỏi và dừng chương trình cho đến khi người dùng nhập dữ liệu. Dữ liệu nhập vào được lưu trữ trong biến hệ thống `answer`. :: [[Câu 3, Câu 6]]
*   **[LMS] [Fact] :: Xử lý chuỗi (String Manipulation)** :: Khối lệnh `letter [n] of [văn bản]` trả về ký tự tại vị trí thứ n. Khối lệnh `[văn bản] contains [ký tự]` kiểm tra sự tồn tại của ký tự trong chuỗi (trả về True/False). Khối lệnh `length of [văn bản]` trả về tổng số ký tự. :: [[Câu 4, Câu 16, Câu 17]]
*   **[LMS] [Fact] :: Cơ chế Broadcast - Receive** :: Dùng để truyền tín hiệu giữa các nhân vật. Khi một nhân vật phát tin (`broadcast`), các nhân vật khác có khối lệnh `when I receive [tin nhắn]` sẽ thực hiện hành động tương ứng. :: [[Câu 5, Câu 22]]
*   **[LMS] [Fact] :: Khái niệm AI và Machine Learning** :: 
    *   **AI (Trí tuệ nhân tạo):** Trí tuệ con người được mô phỏng bởi máy móc.
    *   **Machine Learning (Máy học):** Quá trình máy tính học từ dữ liệu để tạo mô hình dự đoán mà không cần lập trình cụ thể từng bước.
    *   **Deep Learning (Học sâu):** Một phương pháp học máy rút ra các đặc trưng phức tạp từ dữ liệu.
    *   **Face Recognition (Nhận diện khuôn mặt):** Tự động xác định danh tính dựa trên đặc điểm khuôn mặt. :: [[Câu 8, Câu 9]]
*   **[LMS] [Fact] :: Tiện ích mở rộng (Extensions)** :: 
    *   **Translate:** Dịch văn bản sang ngôn ngữ khác.
    *   **Text to Speech:** Chuyển đổi văn bản thành giọng nói.
    *   **Hand/Face/Body Sensing:** Sử dụng camera để nhận diện vị trí các bộ phận cơ thể và cảm xúc khuôn mặt. :: [[Câu 7, Câu 10, Câu 23, Câu 25, Câu 26]]
*   **[LMS] [Fact] :: Quy trình Teachable Machine** :: Gồm các bước: (1) Đặt tên và thu thập dữ liệu (chụp ảnh/ghi âm), (2) Huấn luyện mô hình (Train), (3) Kiểm tra kết quả (Preview), (4) Xuất bản/Tải lên đám mây để sử dụng trong lập trình. :: [[Câu 11, Câu 28]]
*   **[LMS] [Fact] :: Quản lý danh sách (List)** :: Các thao tác cơ bản gồm: `add [item] to [list]` (thêm phần tử), `delete [index] of [list]` (xóa phần tử), `replace item [index] of [list] with [văn bản]` (thay thế phần tử). :: [[Câu 18, Câu 19, Câu 21]]

---

# PHẦN 2: TEST BANK (Ngân hàng đề)

### Question 1:
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId7.gif)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId7.gif)
Câu lệnh nào có tác dụng tạo hiệu ứng cho nhân vật trên?
A. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId8.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId8.png)
B. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId9.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId9.png)
C. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId10.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId10.png)
D. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId11.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId11.png)
**Correct:** B
**Explanation:** Khối lệnh `change [color] effect by [25]` tạo ra sự thay đổi màu sắc liên tục cho nhân vật như trong hình ảnh minh họa.

### Question 2:
Giao diện lập trình trên Dancing with AI được chia thành 7 khu vực. Hãy chọn tên phù hợp của các khu vực:
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId12.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId12.png)
**Correct:** 
1- Thanh công cụ (toolbar)
2- Thư viện khối lệnh (blocks palette)
3- Khu vực lập trình (scripts area)
4- Sân khấu (stage)
5- Thông tin nhân vật (sprite infor)
6- Danh sách nhân vật (sprite list)
7- Danh sách phông nền (backdrop list)
**Explanation:** Đây là cấu trúc chuẩn của giao diện Scratch và các phần mềm dựa trên Scratch như Dancing with AI.

### Question 3:
Câu lệnh nào giúp máy tính “Lưu trữ văn bản người dùng nhập vào” với người dùng?
A. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId13.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId13.png)
B. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId14.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId14.png)
C. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId15.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId15.png)
D. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId16.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId16.png)
**Correct:** A
**Explanation:** Khối lệnh `ask [ ] and wait` dùng để nhận dữ liệu nhập từ bàn phím và lưu vào biến `answer`.

### Question 4:
Nhân vật sẽ hiển thị gì khi sử dụng đoạn lệnh bên dưới?
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId17.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId17.png)
A. a
B. p
C. l
D. Tất cả đều sai
**Correct:** B
**Explanation:** `letter 2 of apple` là ký tự thứ 2 của từ "apple", đó là chữ "p".

### Question 5:
Cho đoạn chương trình gồm 3 nhân vật “Thầy bói”, “Nút Có”, “Nút Không” hoạt động như gif sau:
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId18.gif)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId18.gif)
Biết rằng nhân vật “Thầy bói” được lập trình như sau:
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId19.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId19.png)
Đoạn lệnh nào sau đây phù hợp cho 2 nhân vật “Nút Có”, “Nút Không” để chúng xuất hiện ngay vừa khi “Thầy bói” vừa hoàn thành câu hỏi.
A. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId20.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId20.png)
B. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId21.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId21.png)
C. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId22.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId22.png)
D. [![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId23.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId23.png)
**Correct:** A
**Explanation:** Nhân vật Thầy bói phát tin nhắn "Hỏi xong", do đó các nút cần khối lệnh `when I receive [Hỏi xong]` để thực hiện lệnh `show`.

### Question 6:
Nhận định nào sau đây là đúng khi nói về biến số “answer” ?
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId24.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId24.png)
A. Mang giá trị True
B. Mang giá trị False
C. Mang giá trị là một số
D. Mang giá trị là một chuỗi
**Correct:** D
**Explanation:** Biến `answer` lưu trữ dữ liệu người dùng nhập vào từ bàn phím dưới dạng một chuỗi ký tự (string).

### Question 7:
Sự khác nhau giữa 2 câu lệnh sau là gì?
[![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId25.png)](file:///d:/NoteBookLLM_Br/brain/assets/LMS_IMG_Khoa_học_máy_tính_AI_THCS_Đề_2_trắc_nghiệm_-_AI_THCS_rId25.png)
![Image](../assets/LMS_IMG_Khoa_học_máy_tính_AI