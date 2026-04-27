---
module: "Math 10"
topic: "Giải bài tập cùng AI"
duration: "45 phút"
model: "5E"
---

# Kế hoạch bài dạy (Lesson Plan): Giải bài tập Toán 10 cùng AI (45 phút)

**Mục tiêu:**
- Học sinh biết cách ứng dụng nguyên tắc và cấu trúc Prompt để nhờ AI hỗ trợ giải các bài tập Toán 10.
- Học sinh hiểu được cách dùng AI như một "Trợ giảng ảo", tận dụng tính năng Học có hướng dẫn (Guided Learning) thay vì chỉ lấy đáp án.
- Học sinh áp dụng trách nhiệm khi sử dụng AI: tự duy duy, phản biện, đánh giá và kết hợp ý tưởng.

---

## 1. Gắn kết (Engage) - 5 phút
**Mục đích:** Kích thích sự quan tâm của học sinh đối với việc sử dụng AI trong học tập Toán, từ những khó khăn thực tế.

- **Hoạt động của giáo viên & Học sinh:**
  - **Khởi động & Đặt vấn đề (1 phút):** Giáo viên nêu: "Có bao nhiêu em đã từng bế tắc trước một bài tập Toán 10 hóc búa ở nhà nhưng không có ai để hỏi, và cuối cùng phải tìm đến bạn học AI như Gemini?"
  - **Khảo sát chớp nhoáng (3 phút):** Giáo viên khảo sát nhanh (bằng cách giơ tay, nhắm mắt giơ ngón tay, hoặc dùng công cụ như Slido/Mentimeter) với 2 câu hỏi trọng tâm:
    1. **Mục đích sử dụng:** Khi dùng AI cho bài Toán, em thường làm gì? *(A. Copy thẳng đáp án để nộp / B. Hỏi công thức / C. Yêu cầu AI giảng lại bước giải).*
    2. **Độ tin cậy:** Em đánh giá thế nào về khả năng giải Toán của AI? *(A. Hoàn hảo 100% / B. Thi thoảng sai dấu, nhầm số / C. Hay bịa ra cách giải ảo tưởng khi gặp bài khó).*
  - **Dẫn dắt & Giới thiệu chủ đề (1 phút):** Từ kết quả khảo sát thực tế của lớp (thường sẽ cho thấy học sinh hay chép thẳng kết quả và hay phàn nàn AI giải Toán sai), giáo viên đúc kết lại: "Đó là vì chúng ta chưa biết cách ra lệnh (Prompt) chuẩn môn Toán. Hôm nay, bài học này sẽ giải quyết dứt điểm vấn đề đó bằng cách biến AI thành một 'Trợ giảng ảo' vô cùng đắc lực, giúp các em học hiểu Toán 10 sâu sắc mà không bị AI đánh lừa."

---

## 2. Khám phá (Explore) - 10 phút
**Mục đích:** Học sinh trực tiếp "giải phẫu" lời lệnh để thấy được sự khác biệt về bản chất giữa câu hỏi thông thường và Prompt có cấu trúc (RTC).

- **Hoạt động 1: Thử thách "So kè độ dài" (4 phút):**
  - Giáo viên trình chiếu hai Prompt có độ dài xấp xỉ nhau (~40-45 từ):
    - **Prompt A (Dài mà lười):** *"Tôi đang cần giải bài toán này gấp lắm, bạn hãy giúp tôi giải bài x^2 - 5x + 6 > 0 thật là chi tiết và đầy đủ nhất có thể nhé, vì đây là bài tập quan trọng tôi phải nộp cho thầy giáo ngày mai, bạn cố gắng làm tốt nhé cảm ơn bạn rất nhiều."*
    - **Prompt B (RTC Chất lượng):** *"Đóng vai giáo viên Toán. Hãy hướng dẫn mình các bước xét dấu tam thức x^2 - 5x + 6 để giải bất phương trình. Nhấn mạnh các lỗi sai phổ biến học sinh hay mắc ở phần này khi giải bất phương trình để mình tự rút kinh nghiệm."*
  - Học sinh quan sát kết quả AI trả về: Prompt A chỉ cho đáp án (copy-paste), Prompt B cung cấp bối cảnh sư phạm và "bẫy" cần tránh.
  - Giáo viên đặt câu hỏi: *"Cùng tốn một lượng Token, tại sao Prompt B lại giúp các em thông minh hơn?"* -> Dẫn dắt đến khái niệm cấu trúc mạnh hơn số lượng.
  
- **Hoạt động 2: "X-quang Prompt" - Giải phẫu RTC (6 phút):**
  - > 📱 **[GV chiếu 1 mã QR duy nhất — Phút 0 đầu tiết]** — Học sinh quét mã → vào **Dashboard** → chọn **🛠️ Thẻ RTC Builder** theo hướng dẫn bằng lời.
  - **Nhiệm vụ:** Học sinh sử dụng 3 màu sắc (hoặc ký hiệu) để gạch chân các thành phần trong Prompt B trên giấy, **đồng thời thử điền chính xác R·T·C vào ô digital trên điện thoại**:
    - **R (Role)**: Bạn là ai? (Giáo viên Toán).
    - **T (Task)**: Bạn làm gì? (Hướng dẫn xét dấu tam thức).
    - **C (Context)**: Làm như thế nào? (Nêu lỗi sai phổ biến để rút kinh nghiệm).
  - Học sinh đúc kết: RTC tạo ra một **Gia sư thông minh**, còn Non-RTC chỉ là một **Máy giải bài** dù viết dài bao nhiêu đi nữa.

- **Chốt ý kiến thức:** Giáo viên nhấn mạnh: *"Sự khác biệt không nằm ở độ dài, mà nằm ở **Cấu trúc**. Đừng lãng phí lời nói vào sự van xin ("gấp lắm", "giúp mình"), hãy tập trung vào Cấu trúc (RTC)."*

---

## 3. Giải thích (Explain) - 8 phút
**Mục đích:** Giải thích cách thức tận dụng tính năng "Học có hướng dẫn" (Guided Learning) để học sâu chứ không giải giùm.

- **Hoạt động của giáo viên:**
  - Giải thích việc AI có thể làm gia sư như thế nào. Không chỉ đưa ra kết quả, mà chúng ta cần AI:
    - **Hướng dẫn từng bước**: Suy ngẫm tiến trình giải, biết cách trình bày rõ ràng.
    - **Giải thích cách làm**: Hiểu rõ kiến thức nào được dùng, sự liên kết giữa các bước.
    - **Gợi ý bài tập rèn luyện**: Rèn luyện củng cố và phát hiện điểm yếu để cải thiện.
  - **Khái niệm "Vòng lặp phản hồi" (The Feedback Loop):** Giáo viên giải thích: "Prompt không phải là một phát súng duy nhất, mà là một cuộc đối thoại". 
    - **Bước 1 (Input):** Đưa đề bài và bối cảnh (RTC).
    - **Bước 2 (Evaluate):** HS đánh giá câu trả lời của AI (Có sai dấu không? Logic có hợp lý không?).
    - **Bước 3 (Refine):** Phản hồi lại AI (Yêu cầu giải thích chỗ chưa hiểu hoặc sửa lỗi sai).
- **Hoạt động của giáo viên & Học sinh:**
  - **Trình chiếu mẫu & Giải phẫu Vòng lặp (5 phút):** Giáo viên trình chiếu một đoạn hội thoại có sẵn (hoặc thao tác trực tiếp) về bài toán Đại số Tổ hợp:
    - **Đề bài:** "Cho một nhóm gồm 10 học sinh. 
    (1) Có bao nhiêu cách chọn ra 3 bạn để đi trực nhật? 
    (2) Có bao nhiêu cách chọn ra 3 bạn để phân công làm Tổ trưởng, Tổ phó và Thư ký?"
    - **Thao tác 1 (Prompt 1):** Giáo viên dán Prompt RTC -> Cả lớp quan sát AI giải ý (1). 
      *(Nội dung: "Hãy đóng vai gia sư Toán lớp 10. Hãy hướng dẫn mình cách giải ý (1) của bài toán trên và giải thích tại sao lại dùng Tổ hợp (C) thay vì Chỉnh hợp.")*
    - **Thao tác 2 (Prompt 2 - Vòng lặp):** Giáo viên dán Prompt phản hồi yêu cầu so sánh -> Cả lớp quan sát AI giải thích sự khác biệt.
      *(Nội dung: "Bây giờ hãy so sánh với ý (2). Tại sao khi có tên chức danh cụ thể thì kết quả lại khác đi? Hãy giải thích bản chất của 'thứ tự' để mình không bao giờ bị nhầm lẫn lần sau.")*
  - **Phân tích & Đúc kết (3 phút):** 
    - GV giải thích khái niệm **"Vòng lặp phản hồi" (The Feedback Loop)**: "Prompt không phải là một phát súng duy nhất, mà là một cuộc đối thoại". 
    - HS quan sát và nhận ra: AI không chỉ cho đáp án, mà còn hiểu được bối cảnh "thứ tự" khi ta biết cách vặn lại nó.
  - Học sinh ghi chú lại "Cẩm nang Vòng lặp Prompt AI" môn Toán.

---

## 4. Vận dụng (Elaborate) - 20 phút
**Mục đích:** Học sinh trực tiếp viết Prompt và thực hành giải bài tập Toán 10 cùng AI.

- **Hoạt động của giáo viên & Học sinh:**
  - **Hướng dẫn thực hành (3 phút):**
    - > 📱 **[Hướng dẫn bằng lời — Phút 23]** — “Các em vào lại Dashboard → chọn 📐 **Toán Học 10** → chọn chủ đề → bấm **Sao chép Prompt** → dán vào Gemini.” (Cùng 1 mã QR đã quét từ đầu tiết.)
    - Giáo viên giới thiệu nhanh cách dùng: Chọn chủ đề → Bấm **"Sao chép Prompt"** → Dán vào Gemini. Chia theo 3 mức độ (Dễ - Trung bình - Khó).
  - **Thực hành "Vòng lặp 3 Pha - Triple A" (12 phút):** Mỗi cá nhân/nhóm tự chọn 1 chủ đề bất kỳ và bắt đầu làm việc với Gemini theo quy trình:
    - **Pha 1: ASK (Ra lệnh RTC):** Thay số liệu bài tập của em vào mẫu Prompt tối ưu.
    - **Pha 2: ASSESS (Đánh giá ngược):** Dừng lại quan sát. AI giải đúng hay sai? Có bước nào "ảo tưởng" không? Tự nháp thử và so sánh.
    - **Pha 3: ADJUST (Tinh chỉnh):** Gửi Prompt phản hồi: *"Bạn nhầm chỗ này rồi..."*; *"Hãy giải thích kỹ hơn bước [X]"*; hoặc *"Cảm ơn, hãy tạo bài tập tương tự để mình thử sức"*.
  - **Đấu trường Prompt - Thuyết trình (5 phút):** 
    - Giáo viên mời 2-3 nhóm lên bảng trình diễn "chiến tích".
    - Mỗi nhóm có 60 giây để chia sẻ: **Đề bài nhóm chọn - Prompt sáng tạo nhất - Bài học quý giá AI đã dạy**.
  - **Phản hồi & Chốt chặn (2 phút):** 
    - Giáo viên vinh danh các nhóm có tư duy "Ép AI dạy mình" thay vì "Ép AI làm hộ".
    - **Chốt chặn Kiến thức & Tư duy:** Giáo viên tổng quát hóa: *"Toán học hôm nay chỉ là một ví dụ. Nguyên tắc cốt lõi khi dùng AI ở mọi môn là: **Kiến thức nền là bộ lọc sự thật**. Các em cần nắm vững lý thuyết (Toán phải nhớ điều kiện, Văn phải nhớ bối cảnh, Anh phải nhớ ngữ pháp) để không bị AI dẫn dắt sai hướng. AI là trợ lực, nhưng trí tuệ của các em mới là người cầm lái."*

---

## 5. Đánh giá (Evaluate) - 5 phút
**Mục đích:** Đánh giá sự chuyển đổi nhận thức về phương pháp học tập và đạo đức sử dụng AI.

- **Hoạt động của giáo viên & Học sinh:**
  - **Đối soát Slido (2 phút):** Giáo viên hiển thị lại kết quả khảo sát đầu giờ và so sánh với trải nghiệm thực tế trong lớp. 
  - **Câu hỏi tư duy (2 phút):** Giáo viên đặt một tình huống phản biện: *"Nếu Gemini đưa ra một bước giải trông rất logic nhưng kết quả lại khác với tính toán của em, em sẽ làm gì?"*
    - **A:** Tin AI tuyệt đối vì nó thông minh hơn.
    - **B:** Tin mình tuyệt đối.
    - **C:** Yêu cầu AI giải thích lại bước đó và đối soát với kiến thức giáo viên đã dạy để tìm ra chỗ sai.
    - **D:** Sử dụng một công cụ kiểm chứng thứ ba (Máy tính cầm tay, sách giáo khoa hoặc thảo luận với bạn học).
    - **E:** Gửi chính bài giải nháp của mình lên và yêu cầu AI: *"Hãy so sánh cách làm của mình và của bạn, ai là người đang nhầm lẫn ở đâu?"*
  - **Thông điệp cuối (1 phút):** Giáo viên tổng kết: *"Sự khác biệt giữa một 'Cỗ máy chép bài' và một 'Học sinh ưu tú' nằm ở chỗ biết dùng AI như một người đồng nghiệp để phản biện và phát triển tư duy. Hãy chọn là người làm chủ công nghệ."*

---

## 6. Phụ lục: Kỹ thuật Trình chiếu "Chiến tích"
Để phần thuyết trình 5 phút diễn ra mượt mà, giáo viên lựa chọn 1 trong 2 phương án kỹ thuật sau:

- **Phương án A (Bảng ghim số - Padlet):**
  - **Chuẩn bị:** Giáo viên tạo một bảng Padlet, dán mã QR truy cập vào Slide/Cẩm nang.
  - **Thực hiện:** Cuối phần thực hành, học sinh chụp ảnh màn hình (Screenshot) kết quả AI và đăng lên Padlet **kèm theo nhật ký vòng lặp**:
    - **Lần 1:** Prompt RTC (Copy/Paste).
    - **Lần 2:** "Bạn nhầm ở..." hoặc "Giải thích thêm..." (Phần quan trọng nhất).
    - **Kết quả:** Bài toán hoàn thiện đã được kiểm chứng.
    - 📸 [Ảnh kết quả Gemini]
  - **Trình chiếu:** Giáo viên mở Padlet trên máy tính, cả lớp thấy "Bức tường tri thức". Click vào thẻ bất kỳ để phóng to. Dùng chế độ **Slideshow** (nút ⋯ → Present) để trình chiếu chuyên nghiệp từng bài.
  - **Lưu ý kỹ thuật phóng to:** Nhấn `Ctrl + +` để zoom in trình duyệt, hoặc dùng `F11` full-screen, hoặc click thẳng vào thẻ để Padlet tự phóng to popup.

- **Phương án B (Sử dụng Gemini Express Hub):** 
  - Tận dụng tính năng "Chia sẻ liên kết" (Share link) của Gemini. Học sinh sao chép link cuộc hội thoại và gửi vào nhóm Zalo/Lớp học. Giáo viên chỉ việc click link để show toàn bộ hội thoại.

- **Phương án C (Antigravity Presentation Bridge - Cho Windows LTSC/Không Internet):**
  - **Mô tả:** Sử dụng "Cầu nối trình chiếu" tích hợp sẵn trong Smart Router để hiển thị trực tiếp AI lên Slide mà không cần Add-in Store.
  - **Cách dùng:** 
    1. Chạy Smart Router trên máy tính. 
    2. Mở trình duyệt (Chrome/Edge) và truy cập `http://localhost:4000/present`.
    3. Nhấn **F11** để vào chế độ Toàn màn hình.
    4. Giáo viên mở Tab Chat Dashboard ở cửa sổ khác để ra lệnh; kết quả sẽ tự động đẩy sang màn hình Presentation View với font chữ siêu lớn.
  - **Mẹo (App Mode):** Để trông như một phần mềm chuyên nghiệp không có thanh Tab, hãy tạo shortcut trình duyệt với đuôi: `--app=http://localhost:4000/present`.

- **Quy tắc thuyết trình 60 giây:** 
  1. Chiếu màn hình bài giải.
  2. Nói rõ: "Nhóm em đã thêm từ khóa [X] vào Prompt và kết quả là AI đã giải thích [Y] thay vì chỉ cho đáp án."
  3. Một bài học tâm đắc nhất.

---

## 7. Dặn dò & Tài liệu sau buổi học
- **Mở rộng kho tri thức:** Các em có thể sử dụng **Gemini Express Hub** để lấy các mẫu Prompt tối ưu cho môn **Ngữ Văn** (Phân tích hình tượng văn học) và **Tiếng Anh** (Luyện viết thư, sửa lỗi ngữ pháp).
- **Thông điệp cuối:** AI là "Cánh tay nối dài" của trí tuệ, không phải "Bộ não thay thế". Hãy học cách làm chủ công nghệ để trở thành những người học tập chủ động.
- **Tài liệu số:** Truy cập link/QR code của lớp để tải file **PDF Cẩm nang học tập** về điện thoại dùng mọi lúc mọi nơi.

---
*Kế hoạch bài dạy được tinh gọn và chuẩn hóa cho tiết học 45 phút.*
