# **BẢN DUYỆT RIÊNG CÂU 22-30**
## **Môn: Trí tuệ nhân tạo Trung học**

Tài liệu này dùng để duyệt lại cụm `Câu 22-30` theo nguyên tắc:
- Mỗi câu có `dàn ý thiết kế` trước khi viết câu hỏi hoàn chỉnh.
- Độ khó tăng dần từ `Câu 22` đến `Câu 30`.
- Câu khó được tạo bằng cách `tổ hợp nhiều kiến thức đơn giản` của các câu trước.
- Mỗi câu có sẵn `ảnh review` và `file .sb3` để human mở trên playground kiểm tra.

Mẫu comment:

```md
### Comment của AN
- Quyết định: Giữ / Sửa nhẹ / Viết lại
- Độ khó:
- Kiến thức dùng:
- Tình huống:
- Đáp án / bẫy sai:
- Ghi chú thêm:
```

---

## **Câu 22** [Hiểu - Vận dụng nhẹ]
### 1. Dàn ý thiết kế
- **Mục tiêu kiến thức:**
  - Hiểu vai trò của vòng lặp `forever`.
  - Hiểu cơ chế bám đuổi vị trí khuôn mặt bằng Face Sensing.
- **Tổ hợp kiến thức:**
  - 1 ý về cảm biến khuôn mặt.
  - 1 ý về vòng lặp liên tục.
- **Lý do độ khó:**
  - Đây là câu mở đầu của cụm 22-30, chỉ kiểm tra học sinh có hiểu vì sao hiệu ứng bám mặt phải chạy liên tục hay không.
- **Bẫy sai cần tạo:**
  - Nhầm `forever` với tối ưu camera.
  - Nhầm `forever` với xoay nhân vật.

### 2. Review Media
![Câu 22](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_22.png)

- File dự án để load trên playground: [cau_22.sb3](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_22.sb3)

### 3. Câu hỏi hoàn chỉnh
Trong dự án Face Filter, học sinh muốn một sticker vương miện chỉ xuất hiện khi người chơi đang cười và luôn bám theo khuôn mặt theo thời gian thực. Vì sao phần kiểm tra biểu cảm và cập nhật vị trí sticker nên được đặt trong vòng lặp `forever`?

- A. Vì chương trình cần liên tục kiểm tra người chơi còn đang cười hay không và liên tục cập nhật lại vị trí sticker; nếu không, hiệu ứng chỉ chạy một lần rồi dừng.
- B. Vì đặt trong `forever` sẽ làm camera tự tăng độ phân giải để nhận diện nụ cười tốt hơn.
- C. Vì chỉ khi đặt trong `forever` thì sticker mới tự quay theo góc nghiêng của đầu.
- D. Vì `forever` làm giảm dung lượng bộ nhớ mà dự án sử dụng khi bật camera lâu.

- **Đáp án đúng:** A
- **Giải thích ngắn:** Biểu cảm khuôn mặt và vị trí các điểm nhận diện thay đổi liên tục. Nếu không đặt trong `forever`, chương trình chỉ kiểm tra hoặc cập nhật một lần nên sticker không thể hiện/ẩn và bám đuổi mượt theo thời gian thực.

### Comment của AN
- Quyết định: Express chuyển thành true/false nên sẽ hiển thị nhấp nháy? cần điều chỉnh lại giá trị express để chắc chắn hơn
- Độ khó: Tăng thêm độ khó. nên có biến số để làm nhiễu. 
- Kiến thức dùng:
- Tình huống: 
- Đáp án / bẫy sai: Độ dài các đáp án không cùng độ dài. 
- Ghi chú thêm:

---

## **Câu 23** [Vận dụng]
### 1. Dàn ý thiết kế
- **Mục tiêu kiến thức:**
  - Biến số đếm.
  - Vòng lặp `forever`.
  - Chống cộng dồn bằng `wait until`.
- **Tổ hợp kiến thức:**
  - 1 ý về cảm biến biểu cảm.
  - 1 ý về biến số.
  - 1 ý về chốt trạng thái trong vòng lặp.
- **Lý do độ khó:**
  - Câu này bắt đầu yêu cầu học sinh so sánh hai lời giải, không chỉ nhận diện một block riêng lẻ.
- **Bẫy sai cần tạo:**
  - Nghĩ rằng `wait 1 giây` là đủ chính xác cho mọi tình huống.
  - Nghĩ khối `not` làm điều kiện sai hoàn toàn.

### 2. Review Media
![Câu 23A](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_23_a.png)
![Câu 23B](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_23_b.png)

- File dự án khớp với ảnh A: [cau_23_a.sb3](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_23_a.sb3)
- File dự án khớp với ảnh B: [cau_23_b.sb3](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_23_b.sb3)
- File dự án tổng quát của câu: [cau_23.sb3](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_23.sb3)

### 3. Câu hỏi hoàn chỉnh
Trong ứng dụng đếm số lần cười bằng Face Sensing, học sinh muốn tránh lỗi vòng lặp `forever` chạy quá nhanh làm biến `Số lần cười` bị cộng nhiều lần trong khi người dùng chỉ cười một lần kéo dài. Hai học sinh đề xuất:

- Học sinh A: Sau khi tăng biến, chèn `đợi 1 giây`.
- Học sinh B: Sau khi tăng biến, chèn `đợi đến khi <không còn cười>`.

Nhận định nào đúng nhất?

- A. Giải pháp của học sinh A tối ưu hơn vì làm camera quét chậm lại, giảm nhiễu tốt hơn.
- B. Cả hai giải pháp đều sai vì khối nhận diện biểu cảm không thể đi cùng khối `đợi`.
- C. Giải pháp của học sinh A chỉ tạm thời và có thể vẫn cộng sai hoặc bỏ sót; giải pháp của học sinh B tối ưu hơn vì chốt đúng theo trạng thái cười thực tế.
- D. Giải pháp của học sinh B sai vì dùng `không phải` sẽ làm điều kiện luôn sai.

- **Đáp án đúng:** C
- **Giải thích ngắn:** `wait 1 giây` chỉ là khoảng trễ cố định, không bám theo thời gian cười thực tế. `wait until <not smiling>` mới thật sự khóa lượt đếm hiện tại cho đến khi người dùng dừng cười.

### Comment của AN
- Quyết định:
- Độ khó:
- Kiến thức dùng:
- Tình huống:
- Đáp án / bẫy sai:
- Ghi chú thêm:

---

## **Câu 24** [Vận dụng]
### 1. Dàn ý thiết kế
- **Mục tiêu kiến thức:**
  - Biến số lưu lựa chọn.
  - Dữ liệu chuỗi.
  - Hàm `độ dài`.
  - Rẽ nhánh lồng nhau.
- **Tổ hợp kiến thức:**
  - 1 ý về nhập dữ liệu.
  - 1 ý về kiểm tra độ dài chuỗi.
  - 1 ý về cấu trúc `if` lồng nhau.
- **Lý do độ khó:**
  - Học sinh phải mô phỏng luồng chạy cụ thể của chương trình chứ không chỉ giải thích khái niệm.
- **Bẫy sai cần tạo:**
  - Chỉ nhìn lựa chọn ngôn ngữ mà quên điều kiện độ dài.
  - Nhầm sang nhánh tiếng Pháp.

### 2. Review Media
![Câu 24](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_24.png)

- File dự án để load trên playground: [cau_24.sb3](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_24.sb3)

### 3. Câu hỏi hoàn chỉnh
Học sinh lập trình ứng dụng dịch thuật đa ngôn ngữ như sau:

- Nếu `Lựa chọn = 1` thì:
  - Nếu `độ dài của (Câu gốc) > 10` thì nói `"Too long"`.
  - Ngược lại thì nói bản dịch tiếng Anh.
- Nếu không phải `1` thì nói bản dịch tiếng Pháp.

Người dùng nhập `Lựa chọn = 1` và nhập câu `"Chào Việt Nam"`. Kết quả nào đúng?

- A. Chương trình nói bản dịch tiếng Anh `"Hello Vietnam"`.
- B. Chương trình nói `"Too long"`.
- C. Chương trình nói bản dịch tiếng Pháp.
- D. Chương trình không nói gì vì logic bị xung đột.

- **Đáp án đúng:** B
- **Giải thích ngắn:** `"Chào Việt Nam"` dài hơn 10 ký tự nên chương trình vào nhánh con báo `"Too long"` và không đi đến phần dịch tiếng Anh.

### Comment của AN
- Quyết định:
- Độ khó:
- Kiến thức dùng:
- Tình huống:
- Đáp án / bẫy sai:
- Ghi chú thêm:

---

## **Câu 25** [Vận dụng]
### 1. Dàn ý thiết kế
- **Mục tiêu kiến thức:**
  - Bám theo điểm khuôn mặt.
  - Thay đổi tọa độ `x/y`.
  - Phân tích lỗi hành vi trong `forever`.
- **Tổ hợp kiến thức:**
  - 1 ý về Face Sensing.
  - 1 ý về hệ tọa độ.
  - 1 ý về drift do cộng dồn trong vòng lặp.
- **Lý do độ khó:**
  - Học sinh phải phát hiện lỗi logic động, không chỉ nhận diện ý tưởng “bù tọa độ”.
- **Bẫy sai cần tạo:**
  - Tưởng chỉ cần thấy `nose bridge` + `change y` là đúng.
  - Đổ lỗi cho `on-flipped`.

### 2. Review Media
![Câu 25](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_25.png)

- File dự án để load trên playground: [cau_25.sb3](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_25.sb3)

### 3. Câu hỏi hoàn chỉnh
Trong dự án Face Filter, học sinh muốn đặt sticker mũ cao hơn đầu người chơi nên dùng kịch bản: bám `nose bridge`, sau đó `change y by 120` bên trong vòng lặp `forever`. Phân tích nào đúng nhất?

- A. Kịch bản có nguy cơ làm sticker liên tục bị cộng dồn theo trục `y`; nếu việc bám lại điểm mặt không ổn định, sticker có thể trôi dần và biến mất khỏi màn hình.
- B. Kịch bản sai vì `nose bridge` không bao giờ được dùng làm điểm mốc trong Face Sensing.
- C. Kịch bản sai vì chế độ `on-flipped` làm Face Sensing không còn hoạt động.
- D. Kịch bản hoàn toàn chuẩn, đây là cách tối ưu để giữ sticker cố định trên đầu.

- **Đáp án đúng:** A
- **Giải thích ngắn:** `change y by 120` trong `forever` là lệnh cộng dồn lặp lại. Nếu vị trí nền không được reset ổn định mỗi chu kỳ, sticker có thể bị đẩy trôi dần theo thời gian.

### Comment của AN
- Quyết định:
- Độ khó:
- Kiến thức dùng:
- Tình huống:
- Đáp án / bẫy sai:
- Ghi chú thêm:

---

## **Câu 26** [Vận dụng cao]
### 1. Dàn ý thiết kế
- **Mục tiêu kiến thức:**
  - Bám đuổi khuôn mặt.
  - Sự kiện nhắm mắt.
  - Âm thanh `play sound until done`.
  - Tách script để tránh nghẽn.
- **Tổ hợp kiến thức:**
  - 1 ý về Face Sensing theo vị trí.
  - 1 ý về cảm biến biểu cảm.
  - 1 ý về âm thanh chặn luồng.
  - 1 ý về đa luồng trong Scratch.
- **Lý do độ khó:**
  - Đây là câu tổ hợp đầu tiên có thêm yếu tố hiệu năng và cấu trúc chương trình.
- **Bẫy sai cần tạo:**
  - Chèn `wait 0.1 giây`.
  - Đổi loại cảm biến.
  - Đổi chế độ camera.

### 2. Review Media
![Câu 26](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_26.png)

- File dự án để load trên playground: [cau_26.sb3](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_26.sb3)

### 3. Câu hỏi hoàn chỉnh
Học sinh lập trình sticker kính mát bám theo khuôn mặt bằng Face Sensing. Đồng thời, khi người chơi nhắm mắt, chương trình phát `sound pop` và tăng điểm. Học sinh ghép toàn bộ vào một vòng lặp `forever` duy nhất, làm sticker bám rất giật và chậm. Giải pháp nào tối ưu nhất?

- A. Đổi điều kiện nhắm mắt thành điều kiện cười để camera xử lý nhanh hơn.
- B. Tách thành hai script song song: một script chỉ bám vị trí khuôn mặt, một script xử lý nhắm mắt, âm thanh và điểm số.
- C. Chèn `đợi 0.1 giây` vào cuối vòng lặp chung để máy đỡ quá tải.
- D. Tắt `on-flipped` và chuyển sang `on`.

- **Đáp án đúng:** B
- **Giải thích ngắn:** Phần âm thanh kiểu `until done` có thể chặn vòng lặp nếu ghép chung với phần bám vị trí. Tách script giúp phần bám mặt chạy liên tục, còn phần xử lý sự kiện chạy riêng.

### Comment của AN
- Quyết định:
- Độ khó:
- Kiến thức dùng:
- Tình huống:
- Đáp án / bẫy sai:
- Ghi chú thêm:

---

## **Câu 27** [Vận dụng cao]
### 1. Dàn ý thiết kế
- **Mục tiêu kiến thức:**
  - Boolean biểu cảm.
  - Giá trị số của cường độ biểu cảm.
  - So sánh ngưỡng.
  - Kiểm soát nhiễu.
- **Tổ hợp kiến thức:**
  - 1 ý về Face Sensing Boolean.
  - 1 ý về dữ liệu số 0-100.
  - 1 ý về logic ngưỡng.
  - 1 ý về chất lượng trải nghiệm người dùng.
- **Lý do độ khó:**
  - Câu này buộc học sinh chọn đúng loại dữ liệu cảm biến, không chỉ đúng cú pháp.
- **Bẫy sai cần tạo:**
  - Dùng `đang cười?` thay cho đo cường độ.
  - Dùng `wait`.
  - Dùng camera mode như một cách sửa logic.

### 2. Review Media
Không bắt buộc có ảnh riêng cho câu này. Nếu cần thêm media sau, nên render block giá trị `[mức độ biểu cảm [smile]]`.

### 3. Câu hỏi hoàn chỉnh
Trong dự án nhận diện cảm xúc, học sinh muốn đổi phông nền sang `"Vui vẻ"` chỉ khi người dùng cười thật tươi. Nếu dùng khối Boolean `[đang cười [smile]?]`, phông nền bị đổi ngay cả khi người dùng chỉ cười nhẹ. Cách sửa nào tối ưu nhất?

- A. Dùng khối giá trị `[mức độ biểu cảm [smile]]` và so sánh với một ngưỡng cao, ví dụ `> 80`.
- B. Dùng khối `[không phải [đang cười [smile]?]]` để lọc nhiễu.
- C. Chèn `đợi 5 giây` sau khi phát hiện cười.
- D. Chuyển camera sang chế độ không lật gương.

- **Đáp án đúng:** A
- **Giải thích ngắn:** Khối Boolean chỉ cho biết có/không có cười. Muốn phân biệt cười nhẹ và cười rõ, phải dùng giá trị số cường độ biểu cảm rồi so với ngưỡng.

### Comment của AN
- Quyết định:
- Độ khó:
- Kiến thức dùng:
- Tình huống:
- Đáp án / bẫy sai:
- Ghi chú thêm:

---

## **Câu 28** [Vận dụng cao]
### 1. Dàn ý thiết kế
- **Mục tiêu kiến thức:**
  - Nhận diện nụ cười.
  - Biến số đếm.
  - Danh sách lưu lịch sử.
  - Lỗi cộng dồn trong `forever`.
  - Chốt trạng thái bằng `wait until`.
- **Tổ hợp kiến thức:**
  - 1 ý về cảm biến biểu cảm.
  - 1 ý về biến số.
  - 1 ý về danh sách.
  - 1 ý về debounce/chống lặp.
  - 1 ý về phân tích lỗi dữ liệu.
- **Lý do độ khó:**
  - Đây là câu đầu tiên buộc học sinh nhìn một lỗi đồng thời làm sai cả `biến số` lẫn `danh sách`.
- **Bẫy sai cần tạo:**
  - Tưởng lỗi do chưa xóa danh sách lúc đầu.
  - Tưởng lỗi do khai báo trùng tên biến.

### 2. Review Media
![Câu 28 block](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_28_block.png)
![Câu 28 main](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_28.png)

- File dự án khớp với ảnh block: [cau_28_block.sb3](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_28_block.sb3)
- File dự án khớp với ảnh chính: [cau_28.sb3](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_28.sb3)

### 3. Câu hỏi hoàn chỉnh
Trong dự án “App nhận biết cảm xúc người học online”, mỗi khi phát hiện người dùng cười, hệ thống tăng biến `Số lần cười` thêm 1 và thêm chữ `"Vui vẻ"` vào danh sách `Nhật ký cảm xúc`. Khi chạy thử, học sinh chỉ cười một lần nhưng danh sách bị ghi lặp hàng chục lần và biến đếm tăng vọt. Giải thích nào đúng nhất?

- A. Do danh sách chưa được xóa trước khi bắt đầu, nên toàn bộ dữ liệu cũ bị lặp lại.
- B. Do điều kiện cười vẫn liên tục đúng trong `forever`; cần chèn `đợi đến khi không còn cười` để chặn ghi lặp trong cùng một lượt cười.
- C. Do biến đếm bị trùng tên với một biến khác nên tự tăng nhiều lần.
- D. Do camera phản hồi chậm nên phải tăng tốc xử lý video trong cài đặt.

- **Đáp án đúng:** B
- **Giải thích ngắn:** Một nụ cười có thể kéo dài 1-2 giây, trong khi `forever` chạy rất nhanh. Nếu không có chốt trạng thái, chương trình sẽ coi một lượt cười là rất nhiều lần cười liên tiếp.

### Comment của AN
- Quyết định:
- Độ khó:
- Kiến thức dùng:
- Tình huống:
- Đáp án / bẫy sai:
- Ghi chú thêm:

---

## **Câu 29** [Vận dụng cao]
### 1. Dàn ý thiết kế
- **Mục tiêu kiến thức:**
  - `ask and wait`.
  - Biến hệ thống `answer`.
  - Biến trung gian tự tạo.
  - Rẽ nhánh theo lựa chọn.
  - Translate/Text to Speech.
- **Tổ hợp kiến thức:**
  - 1 ý về nhập dữ liệu nhiều bước.
  - 1 ý về ghi đè dữ liệu hệ thống.
  - 1 ý về lưu trạng thái trung gian.
  - 1 ý về ứng dụng dịch thuật.
  - 1 ý về hậu quả logic sai.
- **Lý do độ khó:**
  - Câu này yêu cầu hiểu chuỗi sự kiện theo thời gian và hiểu biến hệ thống có thể bị ghi đè.
- **Bẫy sai cần tạo:**
  - Đổ lỗi cho Translate/TTS.
  - Đổ lỗi cho so sánh chuỗi.
  - Đổ lỗi cho “chưa nạp từ điển”.

### 2. Review Media
![Câu 29](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_29.png)

- File dự án để load trên playground: [cau_29.sb3](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_29.sb3)

### 3. Câu hỏi hoàn chỉnh
Học sinh lập trình ứng dụng dịch thuật: đầu tiên hỏi người dùng chọn ngôn ngữ đích (`1-Anh`, `2-Pháp`), sau đó hỏi tiếp câu cần dịch. Cuối chương trình, học sinh dùng trực tiếp khối `answer` để kiểm tra xem người dùng đã chọn `1` hay `2`. Khi chạy thử, dù người dùng chọn `1`, chương trình vẫn đi vào nhánh tiếng Pháp. Giải thích nào đúng nhất?

- A. Do `answer` luôn bị cập nhật theo câu hỏi mới nhất; cần lưu kết quả câu hỏi thứ nhất vào một biến trung gian ngay sau khi hỏi.
- B. Do Scratch không hỗ trợ so sánh bằng với dữ liệu kiểu chuỗi.
- C. Do Translate và Text to Speech xung đột khi dùng trong cùng một script.
- D. Do thư viện dịch thuật chưa nạp đủ dữ liệu ngôn ngữ.

- **Đáp án đúng:** A
- **Giải thích ngắn:** Sau câu hỏi thứ hai, `answer` không còn chứa lựa chọn ngôn ngữ nữa mà chứa nội dung câu cần dịch. Nếu không lưu lựa chọn đầu tiên vào biến riêng, phần rẽ nhánh cuối sẽ kiểm tra sai dữ liệu.

### Comment của AN
- Quyết định:
- Độ khó:
- Kiến thức dùng:
- Tình huống:
- Đáp án / bẫy sai:
- Ghi chú thêm:

---

## **Câu 30** [Vận dụng cao - tổ hợp mạnh]
### 1. Dàn ý thiết kế
- **Mục tiêu kiến thức:**
  - Phát hiện nhắm mắt.
  - Phát âm thanh.
  - Tăng biến đếm.
  - Tắt video.
  - Hiểu camera để lại ảnh tĩnh.
  - Dùng `stop this script` để chặn lặp vô hạn.
- **Tổ hợp kiến thức:**
  - 1 ý về cảm biến nhắm mắt.
  - 1 ý về vòng lặp `forever`.
  - 1 ý về âm thanh + biến số.
  - 1 ý về trạng thái video off.
  - 1 ý về ảnh tĩnh vẫn bị nhận diện.
  - 1 ý về lệnh dừng script.
- **Lý do độ khó:**
  - Đây là câu cuối nên phải là câu tổ hợp của nhiều lỗi nhỏ:
    - điều kiện cảm biến,
    - biến số,
    - âm thanh,
    - vòng lặp,
    - video off,
    - dừng luồng.
- **Bẫy sai cần tạo:**
  - Đổ lỗi cho xung đột âm thanh và camera.
  - Chỉ reset biến số.
  - Chèn `wait` thay vì dừng script.

### 2. Review Media
![Câu 30](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_30.png)

- File dự án để load trên playground: [cau_30.sb3](GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media/cau_30.sb3)

### 3. Câu hỏi hoàn chỉnh
Trong dự án “Trò chơi chụp ảnh tự động bằng nháy mắt”, học sinh lập trình như sau: nếu phát hiện khuôn mặt và người chơi nhắm mắt thì chương trình phát `sound pop`, tăng biến `Số ảnh chụp` thêm 1, rồi `tắt camera`. Khi chạy thử, camera tắt đúng nhưng âm thanh vẫn tiếp tục phát lặp lại và biến số tăng liên tục làm treo chương trình. Nguyên nhân và cách sửa đúng nhất là gì?

- A. Do âm thanh và camera xung đột tiến trình; cần tách thành hai script song song.
- B. Do Face Sensing vẫn tiếp tục nhận diện trạng thái nhắm mắt trên ảnh tĩnh cuối cùng sau khi tắt camera; cần thêm `stop this script` ngay sau khi `video off`.
- C. Do biến `Số ảnh chụp` chưa được đặt lại về 0; chỉ cần reset biến là đủ.
- D. Do cần chèn `đợi 1 giây` trước khi `video off` để camera tắt ổn định hơn.

- **Đáp án đúng:** B
- **Giải thích ngắn:** `video off` không xóa ngay hình cuối cùng khỏi sân khấu. Nếu script vẫn tiếp tục chạy trong `forever`, bộ nhận diện có thể vẫn thấy trạng thái nhắm mắt trên ảnh tĩnh đó và tiếp tục kích hoạt điều kiện. Phải dừng hẳn script sau khi tắt video.

### Comment của AN
- Quyết định:
- Độ khó:
- Kiến thức dùng:
- Tình huống:
- Đáp án / bẫy sai:
- Ghi chú thêm:

---

## **Nhận xét tổng thể về độ khó**
- `Câu 22-24`: kiểm tra 2-3 mảnh kiến thức, chủ yếu là hiểu và mô phỏng luồng chạy.
- `Câu 25-27`: chuyển sang phân tích lỗi hành vi động, bắt đầu có tư duy sửa lỗi và chọn đúng loại dữ liệu/loại block.
- `Câu 28-30`: là nhóm tổ hợp mạnh, mỗi câu ghép 4-6 mảnh kiến thức đơn giản thành một lỗi thực tế hơn.
- `Câu 30` là câu khó nhất vì học sinh phải đồng thời hiểu cảm biến, vòng lặp, biến số, âm thanh, trạng thái video, và lệnh dừng script.

## **Comment tổng thể của AN**
- Nhịp tăng độ khó từ 22 -> 30:
- Câu nào còn quá dễ:
- Câu nào còn chưa đủ tổ hợp kiến thức:
- Câu nào nên viết lại hoàn toàn:
- Ghi chú chung:
