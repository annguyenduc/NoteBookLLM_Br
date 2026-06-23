# **Ngân hàng đề thực hành**

# **TRÍ TUỆ NHÂN TẠO TRUNG HỌC CƠ SỞ**

## **1.1. THÔNG TIN**

- Đối tượng: Giáo viên vừa hoàn thành khóa học Trí tuệ nhân tạo Trung học cơ sở
- Loại tài liệu: **Ngân hàng đề thực hành**, dùng để chọn lọc bài cho đề kiểm tra cuối khóa
- Nội dung ngân hàng: **10 bài tập** lập trình trên Dancing with AI
- Mức độ: Vận dụng tổng hợp (Bloom Level 3), ưu tiên tình huống có thể quan sát và chấm điểm định lượng
- Phần mềm: Dancing with AI (web/app)
- Cách sử dụng: khi dựng đề cuối khóa chính thức, chọn **3 bài phù hợp** từ ngân hàng này để đưa vào template đề thực hành

## **1.2. VẬT TƯ THIẾT BỊ**

| Tên thiết bị | Yêu cầu | Số lượng | Đơn vị |
| :---: | :---: | :---: | :---: |
| Máy tính hoặc máy tính bảng | Có kết nối Internet, trình duyệt Chrome/Edge phiên bản mới nhất | 1 | Cái |
| Camera (webcam hoặc camera tích hợp) | Yêu cầu cho BT5–10 có Face/Body Sensing và Teachable Machine | 1 | Cái |

## **1.3. MA TRẬN NGÂN HÀNG BÀI TẬP**

| Bài tập | Tên bài | Công cụ AI | Độ phức tạp |
| :---: | :--- | :--- | :---: |
| BT1 | Chatbot học từ vựng có phản hồi thông minh | Translate + TTS | 🟠 Cao |
| BT2 | Truyện tương tác đa ngôn ngữ (Thỏ và Nhím) | Translate + TTS | 🟠 Cao |
| BT3 | Trợ lý toán học AI đa chức năng | TTS | 🟠 Cao |
| BT4 | Hệ thống hỏi đáp kiến thức có ghi điểm | Translate + TTS | 🟠 Cao |
| BT5 | Nhân vật AI phản ứng cảm xúc + nhận xét đa ngôn ngữ | Face Sensing + Translate | 🟠 Cao |
| BT6 | Bài tập thể dục AI điều khiển bằng cơ thể | Body Sensing + TTS | 🟠 Cao |
| BT7 | Phòng học ảo đa ngôn ngữ tổng hợp | Translate + TTS + Face Sensing | 🔴 Tổng hợp |
| BT8 | Trò chơi điều khiển bằng khuôn mặt có tính điểm | Face Sensing + TTS | 🔴 Tổng hợp |
| BT9 | Bộ lọc trang sức thực tế ảo + thông báo tiếng Anh | Body Sensing + Translate + TTS | 🔴 Tổng hợp |
| BT10 | Hệ thống điểm danh AI toàn diện | Teachable Machine + TTS + Translate | 🔴 Tổng hợp |

---

# **PHẦN II: BÀI TẬP THỰC HÀNH**

---

## **Bài tập 1: Chatbot học từ vựng có phản hồi thông minh**

### 1. Nội dung đề bài

Lập trình một ứng dụng **dạy từ vựng có AI phản hồi**: nhân vật AI hỏi người dùng một từ tiếng Việt, tự động dịch sang tiếng Anh bằng công cụ Translate, đọc to từ đã dịch bằng TTS, sau đó yêu cầu người dùng gõ lại từ tiếng Anh vừa học. Chương trình kiểm tra đúng/sai, ghi điểm và lặp lại đủ 5 vòng trước khi tổng kết.

### 2. Yêu cầu kỹ thuật chi tiết

**Công cụ AI bắt buộc sử dụng:**
- Extension **Translate** (dịch Việt → Anh)
- Extension **Text to Speech** (đọc to từ đã dịch và phản hồi)

**Cấu tạo / Thành phần bắt buộc:**
- Có ít nhất **1 nhân vật** đóng vai trợ lý AI với **3 trang phục** khác nhau: trang phục "waiting", trang phục "đúng", trang phục "sai"
- Có **1 biến số** `score` hiển thị liên tục trên màn hình
- Có **1 biến số** `round` để đếm và kiểm soát vòng lặp (1 đến 5)

**Hoạt động / Tính năng bắt buộc:**
- Dùng khối lệnh **Ask** nhận từ tiếng Việt từ người dùng
- Dùng **Translate** dịch từ đó sang tiếng Anh, hiển thị bằng **Say** kèm tên ngôn ngữ
- Dùng **TTS Speak** đọc to từ tiếng Anh vừa dịch (set language = tiếng Anh)
- Dùng **Ask** yêu cầu người dùng gõ lại từ tiếng Anh
- Dùng **If…then…else** so sánh câu trả lời với kết quả Translate:
  - Đúng: nhân vật chuyển trang phục "đúng" + **TTS** khen "Correct!" + `score` tăng 1
  - Sai: nhân vật chuyển trang phục "sai" + **TTS** đọc lại từ đúng
- round lặp thực hiện **đúng 5 lần** (kiểm soát bằng biến số `round`)
- Sau 5 vòng: **Say** tổng điểm + **TTS Speak** đọc "Bạn đạt X trên 5 điểm"

### 3. Sản phẩm yêu cầu bàn giao

- **File code:** `.sb3` đặt tên theo mẫu `[Chi nhánh]-[Họ tên]-AI THCS-1.sb3`
  - Ví dụ: `HCM-Nguyen Van An-AI THCS-1.sb3`
- **Ảnh PNG** chụp màn hình toàn bộ khối lệnh logic của nhân vật chính, rõ nét, không mờ
  - Đặt tên: `HCM-Nguyen Van An-AI THCS-1.png`

### 4. Đáp án gợi ý (Kịch bản khối lệnh logic)

```
Khi nhấn cờ xanh:
  Set score = 0
  Set round = 1
  Repeat until round > 5:
    Switch costume → "waiting"
    Ask "Nhập một từ tiếng Việt bạn muốn học:" and wait
    Set vietWord = answer
    Say (join "Tiếng Anh là: " (translate vietWord to "en")) for 2 seconds
    Set TTS language = "en"
    Speak (translate vietWord to "en")
    Ask "Gõ lại từ tiếng Anh vừa nghe:" and wait
    If answer = (translate vietWord to "en") then:
      Switch costume → "đúng"
      Speak "Correct!"
      Change score by 1
    Else:
      Switch costume → "sai"
      Speak (join "Sai rồi! Từ đúng là " (translate vietWord to "en"))
    Change round by 1
    Wait 1 second
  Say (join "Bạn đạt " (join score "/5 điểm!")) for 3 seconds
  Speak (join "Bạn đạt " (join score " trên 5 điểm"))
```

![Đáp án gợi ý BT1](Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media/bt1_code.raw.png)

### 5. Tiêu chí chấm điểm (Rubric định lượng)

| STT | Tiêu chí đánh giá | Mức độ mô tả chất lượng đạt yêu cầu | score tối đa |
| :---: | :--- | :--- | :---: |
| **1** | Cấu tạo & Thiết lập | Có đủ 1 nhân vật với 3 trang phục riêng biệt; biến số `score` và `round` được khai báo và hiển thị đúng trên màn hình | **15đ** |
| **2** | Translate hoạt động đúng | Khối lệnh Translate dịch từ tiếng Việt sang tiếng Anh chính xác; kết quả dịch được Say hiển thị trước khi TTS đọc | **25đ** |
| **3** | TTS phát âm đúng ngôn ngữ | TTS Speak đọc từ tiếng Anh với giọng tiếng Anh (set language = English); TTS phản hồi đúng/sai bằng câu hoàn chỉnh | **25đ** |
| **4** | Logic kiểm tra & Tính điểm | If…else so sánh đúng câu trả lời với kết quả Translate; điểm tăng đúng 1 khi đúng, không tăng khi sai; trang phục thay đổi đúng theo trạng thái | **25đ** |
| **5** | round lặp & Tổng kết | Chương trình lặp đúng 5 vòng; sau 5 vòng Say và TTS đọc tổng điểm chính xác | **10đ** |
| | **TỔNG CỘNG** | | **100đ** |

---

## **Bài tập 2: Truyện tương tác đa ngôn ngữ (Thỏ và Nhím)**

### 1. Nội dung đề bài

Lập trình một **truyện ngắn song ngữ có tương tác (minh họa bằng câu chuyện Thỏ và Nhím)**: người dùng chọn ngôn ngữ muốn nghe (tiếng Việt hoặc tiếng Anh), nhân vật kể từng cảnh bằng **giọng TTS** tương ứng, phông nền và trang phục thay đổi theo mỗi cảnh. Người dùng nhấn phím để chuyển sang cảnh tiếp theo. Câu chuyện có ít nhất 4 cảnh.

### 2. Yêu cầu kỹ thuật chi tiết

**Công cụ AI bắt buộc sử dụng:**
- Extension **Translate** (dịch lời thoại sang tiếng Anh khi người dùng chọn)
- Extension **Text to Speech** (đọc lời kể theo ngôn ngữ đã chọn)

**Cấu tạo / Thành phần bắt buộc:**
- Có **≥ 2 nhân vật** trong câu chuyện
- Mỗi trong **4 cảnh** có **Backdrop** và **Costume** riêng biệt
- Có **1 biến số** `language` lưu lựa chọn của người dùng ("1" hoặc "2")

**Hoạt động / Tính năng bắt buộc:**
- Đầu chương trình: **Ask** người dùng chọn ngôn ngữ (nhập "1" cho Việt, "2" cho Anh) → lưu vào biến `language`
- Mỗi cảnh: **If** `language` = "2" thì **Translate** lời thoại sang Anh → **TTS Speak** giọng Anh; ngược lại **TTS Speak** tiếng Việt
- Mỗi cảnh đồng thời **Say** nội dung lời kể trên màn hình song song với TTS
- Chuyển cảnh bằng **phím Space** (Events + Broadcast)
- Cảnh cuối: **TTS** đọc lời kết thúc bằng **cả 2 ngôn ngữ** tuần tự (Việt trước, Anh sau)

### 3. Sản phẩm yêu cầu bàn giao

- **File code:** `.sb3` đặt tên `[Chi nhánh]-[Họ tên]-AI THCS-2.sb3`
- **Ảnh PNG** chụp toàn bộ khối lệnh nhân vật chính — thể hiện rõ cấu trúc 4 cảnh và logic chọn ngôn ngữ
  - Đặt tên: `[Chi nhánh]-[Họ tên]-AI THCS-2.png`

### 4. Đáp án gợi ý (Kịch bản khối lệnh logic)

```
Khi nhấn cờ xanh:
  Ask "Chọn ngôn ngữ: 1 - Tiếng Việt / 2 - Tiếng Anh" and wait
  Set language = answer

  [scene1]
  Switch backdrop → "Forest"
  Switch costume → "rabbit-a"
  Set lời = "Ngày xửa ngày xưa, một chú thỏ kiêu ngạo luôn tự hào mình chạy nhanh nhất khu rừng và thường chế giễu nhím chậm chạp."
  If language = "2":
    Set TTS language = "en"
    Speak (translate lời to "en")
    Say (translate lời to "en") for 4 seconds
  Else:
    Set TTS language = "vi"
    Speak lời
    Say lời for 4 seconds
  Wait until [Space pressed]
  Broadcast "scene2"

[Khi nhận "scene2"]
  Switch backdrop → "Woods"
  Switch costume → "rabbit-b"
  Set lời = "Tức giận vì bị chê bai, nhím đã thách thức thỏ chạy thi. Thỏ kiêu ngạo đồng ý ngay lập tức vì nghĩ mình sẽ thắng dễ dàng."
  If language = "2":
    Set TTS language = "en"
    Speak (translate lời to "en")
    Say (translate lời to "en") for 4 seconds
  Else:
    Set TTS language = "vi"
    Speak lời
    Say lời for 4 seconds
  Wait until [Space pressed]
  Broadcast "scene3"

[Khi nhận "scene3"]
  Switch backdrop → "Blue Sky"
  Switch costume → "rabbit-c"
  Set lời = "Cuộc đua bắt đầu. Thỏ chạy nhanh bỏ xa nhím rồi chủ quan nằm ngủ dưới gốc cây. Nhím vẫn kiên trì, không ngừng chạy từng bước."
  If language = "2":
    Set TTS language = "en"
    Speak (translate lời to "en")
    Say (translate lời to "en") for 4 seconds
  Else:
    Set TTS language = "vi"
    Speak lời
    Say lời for 4 seconds
  Wait until [Space pressed]
  Broadcast "scene4"

[Khi nhận "scene4"]
  Switch backdrop → "Farm"
  Switch costume → "rabbit-a"
  Set lời = "Nhím vượt qua thỏ đang ngủ và về đích trước để giành chiến thắng. Câu chuyện khuyên ta: kiên trì và chăm chỉ sẽ chiến thắng sự kiêu ngạo."
  Set TTS language = "vi"
  Speak lời
  Say lời for 5 seconds
  Wait 1 second
  Set TTS language = "en"
  Speak (translate lời to "en")
  Say (translate lời to "en") for 5 seconds
```

![Đáp án gợi ý BT2](Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media/bt2_code.raw.png)

### 5. Tiêu chí chấm điểm (Rubric định lượng)

| STT | Tiêu chí đánh giá | Mức độ mô tả chất lượng đạt yêu cầu | score tối đa |
| :---: | :--- | :--- | :---: |
| **1** | Cấu tạo & Thành phần | Có ≥ 2 nhân vật; đủ 4 cảnh với Backdrop và Costume riêng biệt mỗi cảnh; biến `language` được khai báo | **15đ** |
| **2** | Logic chọn ngôn ngữ | Ask nhận lựa chọn đúng; If…else phân nhánh Việt/Anh chính xác cho cả 4 cảnh | **25đ** |
| **3** | TTS + Translate hoạt động | TTS đọc đúng ngôn ngữ theo lựa chọn; Translate dịch đúng; cảnh cuối TTS đọc cả 2 ngôn ngữ | **30đ** |
| **4** | Tương tác chuyển cảnh | Người dùng nhấn phím chuyển cảnh đúng thứ tự; Broadcast hoạt động chính xác 4/4 cảnh | **20đ** |
| **5** | Thẩm mỹ & Đóng gói | Say hiển thị chữ đồng thời với TTS; nội dung câu chuyện logic, liên kết; không lỗi trình tự | **10đ** |
| | **TỔNG CỘNG** | | **100đ** |

---

## **Bài tập 3: Trợ lý toán học AI đa chức năng**

### 1. Nội dung đề bài

Lập trình một **trợ lý toán học AI hoàn chỉnh**: thực hiện đủ 4 phép toán cơ bản, đọc to kết quả bằng giọng TTS với câu đầy đủ, lưu lịch sử 3 phép tính gần nhất vào List để hiển thị lại khi người dùng yêu cầu, và xử lý trường hợp chia cho 0 bằng thông báo lỗi qua TTS.

### 2. Yêu cầu kỹ thuật chi tiết

**Công cụ AI bắt buộc sử dụng:**
- Extension **Text to Speech** (đọc kết quả và thông báo bằng giọng nói)

**Cấu tạo / Thành phần bắt buộc:**
- **1 biến số** `calcResult` lưu kết quả phép tính
- **1 List** `history` tối đa 3 mục, lưu dạng "X [phép toán] Y = Z"
- **Biến số** `num1`, `num2`, `operation` lưu dữ liệu nhập vào

**Hoạt động / Tính năng bắt buộc:**
- Dùng **Ask** nhận lần lượt: số thứ nhất, số thứ hai, và lựa chọn phép toán (1=Cộng, 2=Trừ, 3=Nhân, 4=Chia)
- **If…then…else** phân nhánh đủ 4 phép, tính bằng Operators → lưu vào `calcResult`
- Xử lý đặc biệt: nếu chọn Chia và số thứ hai = 0 → **TTS Speak** "Không thể chia cho số 0" thay vì tính
- **TTS Speak** đọc câu đầy đủ: "[Số 1] [phép toán] [Số 2] bằng [calcResult]"
- Lưu vào **List** `history`: nếu List đã có 3 mục → xóa mục cũ nhất trước khi thêm mới
- Khi người dùng nhập "5" (xem lịch sử) → **Say** tuần tự 3 phép tính trong List
- **Loop**: sau mỗi phép tính hỏi "Tiếp tục? (1=Có / 5=Xem lịch sử / 0=Thoát)"

### 3. Sản phẩm yêu cầu bàn giao

- **File code:** `.sb3` đặt tên `[Chi nhánh]-[Họ tên]-AI THCS-3.sb3`
- **Ảnh PNG** chụp toàn bộ khối lệnh — thể hiện rõ If…else 4 nhánh, TTS, List và logic lịch sử
  - Đặt tên: `[Chi nhánh]-[Họ tên]-AI THCS-3.png`

### 4. Đáp án gợi ý (Kịch bản khối lệnh logic)

```
Khi nhấn cờ xanh:
  Delete all of history
  Set operation = "1"
  Repeat until operation = "0":
    Ask "Nhập số thứ nhất:" → Set num1 = answer
    Ask "Nhập số thứ hai:" → Set num2 = answer
    Ask "Phép toán (1=Cộng 2=Trừ 3=Nhân 4=Chia 5=history 0=Thoát):" → Set operation = answer

    If operation = "1": Set calcResult = num1 + num2
    If operation = "2": Set calcResult = num1 - num2
    If operation = "3": Set calcResult = num1 * num2
    If operation = "4":
      If num2 = 0: TTS Speak "Không thể chia cho số 0"
      Else: Set calcResult = num1 / num2
    If operation = "5": [Say từng mục trong List history]

    If operation ≠ "0" AND operation ≠ "5":
      TTS Speak (join num1 " [phép] " (join num2 " bằng " calcResult))
      If length of history = 3: Delete item 1 of history
      Add (join num1 " [phép] " (join num2 " = " calcResult)) to history
```

![Đáp án gợi ý BT3](Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media/bt3_code.raw.png)

### 5. Tiêu chí chấm điểm (Rubric định lượng)

| STT | Tiêu chí đánh giá | Mức độ mô tả chất lượng đạt yêu cầu | score tối đa |
| :---: | :--- | :--- | :---: |
| **1** | Cấu tạo & Thành phần | Biến `calcResult`, `num1`, `num2`, `operation` được khai báo; List `history` tồn tại và hiển thị | **10đ** |
| **2** | 4 phép toán & Xử lý chia 0 | Cả 4 phép tính cho kết quả đúng; trường hợp chia cho 0: TTS thông báo lỗi, không tính | **35đ** |
| **3** | TTS đọc câu đầy đủ | TTS Speak đọc câu hoàn chỉnh "X [phép] Y bằng Z" cho mọi phép tính hợp lệ | **25đ** |
| **4** | List lịch sử 3 mục | List lưu đúng định dạng; khi đủ 3 mục, mục cũ nhất bị xóa trước khi thêm; hiển thị đúng khi xem | **20đ** |
| **5** | round lặp & Thoát | Chương trình tiếp tục hỏi sau mỗi phép tính; thoát đúng khi người dùng nhập 0 | **10đ** |
| | **TỔNG CỘNG** | | **100đ** |

---

## **Bài tập 4: Hệ thống hỏi đáp kiến thức có ghi điểm**

### 1. Nội dung đề bài

Lập trình một **hệ thống quiz kiến thức 5 câu**: lưu câu hỏi và đáp án vào List, lần lượt đọc câu hỏi bằng TTS, nhận câu trả lời từ người dùng, kiểm tra đúng/sai và ghi điểm. Cuối cùng một nhân vật thứ hai xuất hiện qua Broadcast, dịch thông báo kết quả sang tiếng Anh bằng Translate và đọc to bằng TTS.

### 2. Yêu cầu kỹ thuật chi tiết

**Công cụ AI bắt buộc sử dụng:**
- Extension **Text to Speech** (đọc câu hỏi và phản hồi)
- Extension **Translate** (dịch thông báo tổng kết sang tiếng Anh)

**Cấu tạo / Thành phần bắt buộc:**
- **2 List**: `questions` (5 câu) và `answers` (5 đáp án tương ứng)
- **Biến số** `score` (đếm câu đúng) và `round` (đếm câu hỏi hiện tại, từ 1 đến 5)
- **Nhân vật thứ 2** nhận Broadcast để hiển thị kết quả cuối

**Hoạt động / Tính năng bắt buộc:**
- Trước khi bắt đầu: **Thêm 5 câu hỏi vào List `questions`** và **5 đáp án vào List `answers`** (nội dung về AI hoặc lập trình kéo-thả)
- Dùng **biến số `round`** để lần lượt lấy câu hỏi theo index từ List
- Mỗi câu: **TTS Speak** đọc câu hỏi → **Ask** nhận trả lời → **If** so sánh với đáp án trong List
- Đúng: `score` +1 + TTS "Chính xác!"; Sai: TTS đọc đáp án đúng
- Sau 5 câu: **Broadcast** → nhân vật 2 xuất hiện
- Nhân vật 2: tạo câu nhận xét tiếng Việt theo mức điểm → **Translate** sang Anh → **TTS** đọc cả 2

### 3. Sản phẩm yêu cầu bàn giao

- **File code:** `.sb3` đặt tên `[Chi nhánh]-[Họ tên]-AI THCS-4.sb3`
- **Ảnh PNG** chụp toàn bộ khối lệnh nhân vật chính (chuỗi hỏi đáp) + nhân vật thứ 2 (tổng kết)
  - Đặt tên: `[Chi nhánh]-[Họ tên]-AI THCS-4.png`

### 4. Đáp án gợi ý (Kịch bản khối lệnh logic)

```
[Nhân vật 1 - Quiz Master]
Khi nhấn cờ xanh:
  Set score = 0, Set round = 1
  Add "Translate là gì?" to questions
  Add "Công cụ dịch ngôn ngữ" to answers
  [... thêm 4 câu/đáp án nữa về nội dung khoá học ...]

  Repeat until round > 5:
    TTS Speak (item round of questions)
    Ask (item round of questions) and wait
    If answer = (item round of answers):
      TTS Speak "Chính xác!"
      Change score by 1
    Else:
      TTS Speak (join "Sai! answers là " (item round of answers))
    Change round by 1
  Broadcast "calcResult"

[Nhân vật 2 - Tổng kết]
Khi nhận "calcResult":
  Set nhận xét = (join "Bạn đạt " (join score "/5 điểm!"))
  If score = 5: Set nhận xét = "Xuất sắc! Bạn đạt 5/5 điểm!"
  Say nhận xét for 3 seconds
  TTS (lang vi) Speak nhận xét
  TTS (lang en) Speak (translate nhận xét to "en")
```

![Đáp án gợi ý BT4](Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media/bt4_code.raw.png)

### 5. Tiêu chí chấm điểm (Rubric định lượng)

| STT | Tiêu chí đánh giá | Mức độ mô tả chất lượng đạt yêu cầu | score tối đa |
| :---: | :--- | :--- | :---: |
| **1** | Cấu tạo & List | 2 List được khai báo với đủ 5 câu hỏi và 5 đáp án hợp lệ; biến score và round đúng | **15đ** |
| **2** | TTS đọc câu hỏi | TTS Speak đọc đúng từng câu hỏi theo thứ tự từ List; Ask nhận trả lời sau khi TTS đọc xong | **20đ** |
| **3** | Logic kiểm tra & score | If so sánh đúng câu trả lời với đáp án trong List; điểm tăng chính xác; TTS phản hồi đúng/sai | **30đ** |
| **4** | Broadcast & Nhân vật 2 | Broadcast hoạt động sau câu 5; nhân vật 2 xuất hiện đúng; tổng kết có Translate + TTS cả 2 ngôn ngữ | **25đ** |
| **5** | Thẩm mỹ & Đóng gói | Chương trình chạy mượt, không lỗi; 5 câu hỏi liên quan đến AI/lập trình kéo-thả | **10đ** |
| | **TỔNG CỘNG** | | **100đ** |

---

## **Bài tập 5: Nhân vật AI phản ứng cảm xúc + nhận xét đa ngôn ngữ**

### 1. Nội dung đề bài

Lập trình chương trình **đọc cảm xúc AI song ngữ**: camera liên tục nhận diện biểu cảm người dùng bằng Face Sensing. Khi phát hiện mỗi biểu cảm, nhân vật thay đổi trang phục và phông nền tương ứng, đồng thời hiển thị lời nhận xét tiếng Việt và tự dịch sang tiếng Anh bằng Translate. Nhận diện và phản ứng được ít nhất 3 biểu cảm khác nhau.

### 2. Yêu cầu kỹ thuật chi tiết

**Công cụ AI bắt buộc sử dụng:**
- **Face Sensing** (nhận diện biểu cảm khuôn mặt liên tục)
- Extension **Translate** (dịch lời nhận xét sang tiếng Anh)

**Cấu tạo / Thành phần bắt buộc:**
- Nhân vật phản ứng có **≥ 4 trang phục**: 1 trang phục "waiting" + 3 trang phục ứng với 3 biểu cảm
- **≥ 3 Backdrop** khác nhau ứng với 3 biểu cảm
- Camera bật ở chế độ phù hợp, độ trong suốt điều chỉnh để thấy cả người dùng lẫn nhân vật

**Hoạt động / Tính năng bắt buộc:**
- Camera bật ngay khi chương trình khởi động
- round lặp **Forever**: liên tục kiểm tra biểu cảm bằng Face Sensing Events
- Nhận diện **≥ 3 biểu cảm** (ví dụ: vui/mỉm cười, buồn, ngạc nhiên, mở miệng...)
- Mỗi biểu cảm kích hoạt: **Switch Costume** + **Switch Backdrop** + **Say** lời nhận xét tiếng Việt
- Ngay sau Say tiếng Việt: dùng **Translate** dịch lời đó sang Anh → **Say** bản dịch trong 2 giây
- Trạng thái mặc định (không phát hiện biểu cảm): nhân vật về trang phục "waiting" + **Say** "Nhìn vào camera nào!"

### 3. Sản phẩm yêu cầu bàn giao

- **File code:** `.sb3` đặt tên `[Chi nhánh]-[Họ tên]-AI THCS-5.sb3`
- **Ảnh PNG** chụp toàn bộ khối lệnh — thể hiện rõ Forever loop, 3 Face Sensing Event blocks, Switch Costume/Backdrop, Say + Translate
  - Đặt tên: `[Chi nhánh]-[Họ tên]-AI THCS-5.png`

### 4. Đáp án gợi ý (Kịch bản khối lệnh logic)

```
Khi nhấn cờ xanh:
  Turn video on
  Set video transparency to 30
  Switch costume → "waiting"
  Say "Nhìn vào camera nào!"

[Face Sensing Event: Khi phát hiện biểu cảm "Vui"]
  Switch costume → "smile"
  Switch backdrop → "smile"
  Set lời = "Bạn đang rất vui vẻ!"
  Say lời for 2 seconds
  Say (translate lời to "en") for 2 seconds

[Face Sensing Event: Khi phát hiện biểu cảm "Buồn"]
  Switch costume → "sad"
  Switch backdrop → "sad"
  Set lời = "Có chuyện gì buồn vậy?"
  Say lời for 2 seconds
  Say (translate lời to "en") for 2 seconds

[Face Sensing Event: Khi phát hiện biểu cảm "Ngạc nhiên"]
  Switch costume → "surprise"
  Switch backdrop → "surprise"
  Set lời = "Wow, bạn ngạc nhiên quá!"
  Say lời for 2 seconds
  Say (translate lời to "en") for 2 seconds
```

![Đáp án gợi ý BT5](Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media/bt5_code.raw.png)

### 5. Tiêu chí chấm điểm (Rubric định lượng)

| STT | Tiêu chí đánh giá | Mức độ mô tả chất lượng đạt yêu cầu | score tối đa |
| :---: | :--- | :--- | :---: |
| **1** | Cấu tạo & Camera | Camera bật đúng khi khởi động; độ trong suốt điều chỉnh hợp lý; ≥ 4 trang phục và ≥ 3 Backdrop được tạo | **15đ** |
| **2** | Face Sensing ≥ 3 biểu cảm | Chương trình phản ứng đúng với ít nhất 3 biểu cảm; mỗi biểu cảm kích hoạt đúng Costume + Backdrop tương ứng | **35đ** |
| **3** | Translate song ngữ | Sau mỗi lời nhận xét tiếng Việt, Translate dịch sang Anh và Say hiển thị bản dịch; nội dung 2 ngôn ngữ khớp nhau | **30đ** |
| **4** | Trạng thái chờ | Khi không phát hiện biểu cảm, nhân vật về trang phục mặc định và hiển thị lời chờ | **10đ** |
| **5** | Thẩm mỹ & Đóng gói | Chương trình phản ứng mượt mà; nội dung lời nhận xét phù hợp với biểu cảm | **10đ** |
| | **TỔNG CỘNG** | | **100đ** |

---

## **Bài tập 6: Bài tập thể dục AI điều khiển bằng cơ thể**

### 1. Nội dung đề bài

Lập trình ứng dụng **thể dục thông minh AI**: nhân vật hướng dẫn viên bám theo một bộ phận cơ thể người dùng qua Body Sensing. TTS đếm số động tác to thành tiếng sau mỗi lần người dùng giơ tay vượt ngưỡng. Khi đủ 10 lần, TTS chúc mừng và nhân vật đổi trang phục "completed". Nhấn Space để bắt đầu lại từ 0.

### 2. Yêu cầu kỹ thuật chi tiết

**Công cụ AI bắt buộc sử dụng:**
- **Body Sensing** (theo dõi tọa độ cổ tay liên tục)
- Extension **Text to Speech** (đếm số động tác và chúc mừng)

**Cấu tạo / Thành phần bắt buộc:**
- **1 biến số** `count` hiển thị liên tục trên màn hình
- **1 biến số** `isCounted` (giá trị 0 hoặc 1) để tránh đếm nhiều lần trong 1 động tác
- Nhân vật có **≥ 2 trang phục**: "exercise" và "completed"

**Hoạt động / Tính năng bắt buộc:**
- Camera bật; nhân vật bám theo **cổ tay trái** (wrist coordinate) qua Body Sensing trong **Forever**
- Phát hiện động tác: khi tọa độ Y của cổ tay **< 100** (tay giơ cao vượt ngưỡng) **AND** `isCounted` = 0:
  - `count` tăng 1; `isCounted` = 1
  - **TTS Speak** đọc số đếm tương ứng: "Một!", "Hai!", ... "Mười!"
- Khi tay hạ xuống (Y > 150): reset `isCounted` = 0 (cho phép đếm lần tiếp theo)
- Khi `count` = 10: đổi costume "completed" + **TTS** "Xuất sắc! Bạn đã hoàn thành 10 lần!"
- Nhấn **Space**: `count` = 0, `isCounted` = 0, costume về "exercise"

### 3. Sản phẩm yêu cầu bàn giao

- **File code:** `.sb3` đặt tên `[Chi nhánh]-[Họ tên]-AI THCS-6.sb3`
- **Ảnh PNG** chụp toàn bộ khối lệnh — thể hiện rõ Body Sensing, biến đếm, TTS và logic ngưỡng Y
  - Đặt tên: `[Chi nhánh]-[Họ tên]-AI THCS-6.png`

### 4. Đáp án gợi ý (Kịch bản khối lệnh logic)

```
Khi nhấn cờ xanh:
  Set count = 0
  Set isCounted = 0
  Switch costume → "exercise"
  Turn video on
  Forever:
    Go to x:(x of [left wrist]), y:(y of [left wrist])
    If (y of [left wrist]) < 100 AND isCounted = 0:
      Change count by 1
      Set isCounted = 1
      TTS Speak (item count of ["Một","Hai","Ba","Bốn","Năm","Sáu","Bảy","Tám","Chín","Mười"])
      If count = 10:
        Switch costume → "completed"
        TTS Speak "Xuất sắc! Bạn đã hoàn thành 10 lần!"
        Stop this script
    If (y of [left wrist]) > 150:
      Set isCounted = 0

Khi nhấn [Space]:
  Set count = 0
  Set isCounted = 0
  Switch costume → "exercise"
```

![Đáp án gợi ý BT6](Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media/bt6_code.raw.png)

### 5. Tiêu chí chấm điểm (Rubric định lượng)

| STT | Tiêu chí đánh giá | Mức độ mô tả chất lượng đạt yêu cầu | score tối đa |
| :---: | :--- | :--- | :---: |
| **1** | Cấu tạo & Camera | Camera bật; nhân vật bám đúng vị trí cổ tay trong Forever; 2 trang phục tồn tại và hiển thị đúng | **15đ** |
| **2** | Body Sensing bám cơ thể | Nhân vật di chuyển chính xác theo tọa độ cổ tay (x, y) liên tục không bị giật | **25đ** |
| **3** | Đếm động tác đúng | Biến `isCounted` ngăn đếm nhiều lần trong 1 động tác; `count` tăng đúng 1 mỗi lần giơ tay qua ngưỡng; hiển thị đúng | **30đ** |
| **4** | TTS đếm & Chúc mừng | TTS đọc đúng số thứ tự sau mỗi động tác; khi đủ 10 lần TTS chúc mừng và nhân vật đổi costume | **20đ** |
| **5** | Reset & Đóng gói | Space reset đúng tất cả biến về 0 và costume về trạng thái ban đầu; chương trình chạy mượt | **10đ** |
| | **TỔNG CỘNG** | | **100đ** |

---

## **Bài tập 7: Phòng học ảo đa ngôn ngữ tổng hợp**

### 1. Nội dung đề bài

Lập trình một **phòng học ảo AI toàn diện**: người dùng chọn chủ đề muốn học trong 3 chủ đề về AI, nhân vật giáo viên ảo dạy nội dung bằng TTS đồng thời dịch sang tiếng Anh bằng Translate. Sau khi nghe xong, Face Sensing phát hiện học sinh mỉm cười đồng ý để tự động chuyển phần tiếp theo. Tích hợp đủ 3 công cụ AI: Translate + TTS + Face Sensing.

### 2. Yêu cầu kỹ thuật chi tiết

**Công cụ AI bắt buộc sử dụng:**
- Extension **Translate** (dịch nội dung bài học sang tiếng Anh)
- Extension **Text to Speech** (đọc nội dung bài + tóm tắt cuối)
- **Face Sensing** (phát hiện học sinh đồng ý để chuyển bài)

**Cấu tạo / Thành phần bắt buộc:**
- **≥ 3 chủ đề** về nội dung khoá học (ví dụ: AI là gì, Translate hoạt động thế nào, Teachable Machine là gì)
- Mỗi chủ đề có **Backdrop** riêng
- **Biến số** `currentLesson` theo dõi đang ở chủ đề nào
- **Nhân vật giáo viên ảo** + **1 nhân vật nút "Học lại"** (ẩn ban đầu)

**Hoạt động / Tính năng bắt buộc:**
- **Ask** người dùng chọn chủ đề → **Broadcast** kích hoạt cảnh học tương ứng
- Mỗi cảnh: **TTS** đọc nội dung bài học tiếng Việt + **Say** đồng thời + sau đó **Translate** sang Anh → **Say** bản dịch
- Sau khi TTS đọc xong: chờ **Face Sensing** phát hiện biểu cảm "mỉm cười" → **Broadcast** sang bài tiếp
- Sau bài 3: **TTS** đọc tóm tắt toàn bộ + **Translate** sang Anh + **TTS** đọc bản Anh
- Nhấn phím **R**: **Broadcast** reset về Ask chọn chủ đề

### 3. Sản phẩm yêu cầu bàn giao

- **File code:** `.sb3` đặt tên `[Chi nhánh]-[Họ tên]-AI THCS-7.sb3`
- **Ảnh PNG** chụp toàn bộ khối lệnh — thể hiện rõ Ask + Broadcast, cảnh học mẫu (TTS + Translate + Face Sensing chuyển bài), và khối tóm tắt
  - Đặt tên: `[Chi nhánh]-[Họ tên]-AI THCS-7.png`

### 4. Đáp án gợi ý (Kịch bản khối lệnh logic)

```
Khi nhấn cờ xanh:
  Set currentLesson = 1
  Ask "Chọn chủ đề (1=AI là gì / 2=Translate / 3=Teachable Machine):" and wait
  Broadcast (join "Bài " answer)

[Khi nhận "Bai 1"]
  Switch backdrop → "AI"
  Set nội dung = "AI là Trí tuệ nhân tạo, giúp máy tính học và đưa ra quyết định."
  TTS (vi) Speak nội dung
  Say nội dung for 4 seconds
  Say (translate nội dung to "en") for 4 seconds
  Wait until [Face Sensing: smile detected]
  Broadcast "Bai 2"

[Khi nhận "Bai 2"] → [tương tự, chủ đề Translate]
[Khi nhận "Bai 3"] → [tương tự, chủ đề Teachable Machine]
[Khi nhận "Bai 4" - Kết thúc]
  Set tóm tắt = "Bạn đã hoàn thành 3 chủ đề AI quan trọng!"
  TTS (vi) Speak tóm tắt
  TTS (en) Speak (translate tóm tắt to "en")
  Show [nút Học lại]

[Khi nhấn R]: Broadcast "Reset" → quay về Ask chủ đề
```

![Đáp án gợi ý BT7](Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media/bt7_code.raw.png)

### 5. Tiêu chí chấm điểm (Rubric định lượng)

| STT | Tiêu chí đánh giá | Mức độ mô tả chất lượng đạt yêu cầu | score tối đa |
| :---: | :--- | :--- | :---: |
| **1** | Cấu tạo & ≥ 3 chủ đề | Có đủ 3 chủ đề với Backdrop riêng; Broadcast kích hoạt đúng cảnh theo lựa chọn của người dùng | **15đ** |
| **2** | TTS + Translate song ngữ | TTS đọc nội dung tiếng Việt; Translate dịch đúng sang Anh và Say hiển thị cho cả 3 chủ đề | **30đ** |
| **3** | Face Sensing chuyển bài | Face Sensing phát hiện biểu cảm đồng ý và tự động chuyển sang bài kế tiếp đúng thứ tự (1→2→3) | **25đ** |
| **4** | Tóm tắt & Reset | Tóm tắt cuối có TTS + Translate song ngữ; Reset (phím R) hoạt động đúng, trở về chọn chủ đề | **20đ** |
| **5** | Thẩm mỹ & Đóng gói | Nội dung 3 chủ đề liên quan trực tiếp đến khoá học AI THCS; chương trình chạy mượt không lỗi | **10đ** |
| | **TỔNG CỘNG** | | **100đ** |

---

## **Bài tập 8: Trò chơi điều khiển bằng khuôn mặt có tính điểm**

### 1. Nội dung đề bài

Lập trình trò chơi tương tác AI: nhân vật "cái rổ" di chuyển trái/phải theo **tọa độ X khuôn mặt người dùng** (Face Sensing) để bắt các bóng rơi ngẫu nhiên từ trên xuống. Có đồng hồ đếm ngược 30 giây và bảng điểm hiển thị liên tục. Khi hết giờ, TTS đọc kết quả và nhân vật thứ 2 hiển thị tổng kết. Nhấn Space để chơi lại.

### 2. Yêu cầu kỹ thuật chi tiết

**Công cụ AI bắt buộc sử dụng:**
- **Face Sensing** (nhân vật rổ bám theo tọa độ X khuôn mặt)
- Extension **Text to Speech** (đọc kết quả cuối trò chơi)

**Cấu tạo / Thành phần bắt buộc:**
- **Nhân vật Rổ**: bám X khuôn mặt, cố định tại Y = -150
- **Nhân vật Bóng**: xuất hiện X ngẫu nhiên (-200 đến 200), rơi từ Y=170 xuống Y=-180
- **Biến số** `score` và `time` (đếm ngược từ 30), hiển thị liên tục
- **Nhân vật Tổng kết**: ẩn ban đầu, xuất hiện sau Broadcast "gameOver"

**Hoạt động / Tính năng bắt buộc:**
- Camera bật; Rổ bám **X khuôn mặt** liên tục (Forever), Y cố định -150
- Bóng rơi liên tục: Change Y by -10 mỗi vòng
- Khi bóng chạm Y < -170: reset lên X ngẫu nhiên, Y = 170
- Khi bóng chạm Rổ: `score` +1 + **TTS Speak** "Bat duoc!" + reset bóng về vị trí mới
- `time` đếm ngược mỗi giây (Wait 1 giây, Change by -1)
- Khi `time` = 0: dừng → **Broadcast** "gameOver"
- Nhân vật Tổng kết xuất hiện: **Say** điểm + **TTS Speak** "Bạn đạt [X] điểm!"
- Nhấn **Space**: reset `score` = 0, `time` = 30, ẩn Tổng kết

### 3. Sản phẩm yêu cầu bàn giao

- **File code:** `.sb3` đặt tên `[Chi nhánh]-[Họ tên]-AI THCS-8.sb3`
- **Ảnh PNG** chụp toàn bộ khối lệnh: nhân vật Rổ (Face Sensing + Forever), nhân vật Bóng (rơi + chạm + Broadcast), nhân vật Tổng kết
  - Đặt tên: `[Chi nhánh]-[Họ tên]-AI THCS-8.png`

### 4. Đáp án gợi ý (Kịch bản khối lệnh logic)

```
[Nhân vật Rổ]
Khi nhấn cờ xanh:
  Turn video on
  Forever:
    Go to x:(x of face) y:-150

[Nhân vật Bóng]
Khi nhấn cờ xanh:
  Set score = 0, Set time = 30
  Go to x:(pick random -200 to 200) y:170
  Repeat until time = 0:
    Change Y by -10
    If Y < -170: Go to x:(pick random -200 to 200) y:170
    If touching [Rổ]:
      Change score by 1
      TTS Speak "Bat duoc!"
      Go to x:(pick random -200 to 200) y:170
    Wait 0.05 seconds
  Broadcast "gameOver"

[Đồng hồ - script song song]
Khi nhấn cờ xanh:
  Repeat until time = 0:
    Wait 1 second
    Change time by -1

[Nhân vật Tổng kết]
Khi nhấn cờ xanh: Hide
Khi nhận "gameOver":
  Show
  Say (join "Bạn đạt " (join score " điểm!")) for 3 seconds
  TTS Speak (join "Bạn đạt " (join score " điểm!"))

[Khi nhấn Space]:
  Set score = 0, Set time = 30
  Hide [Tổng kết]
```

![Đáp án gợi ý BT8](Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media/bt8_code.raw.png)

### 5. Tiêu chí chấm điểm (Rubric định lượng)

| STT | Tiêu chí đánh giá | Mức độ mô tả chất lượng đạt yêu cầu | score tối đa |
| :---: | :--- | :--- | :---: |
| **1** | Face Sensing điều khiển Rổ | Rổ bám chính xác tọa độ X khuôn mặt trong suốt trò chơi; Y cố định -150 không bị nhảy | **25đ** |
| **2** | Bóng rơi & Logic chạm | Bóng rơi liên tục; reset đúng vị trí khi chạm đáy hoặc chạm Rổ; `score` tăng đúng 1 mỗi lần bắt được | **30đ** |
| **3** | Đếm ngược 30 giây | `time` đếm ngược đúng từng giây; khi về 0, trò chơi dừng và Broadcast kích hoạt Tổng kết | **20đ** |
| **4** | TTS kết quả & Reset | TTS đọc đúng tổng điểm khi kết thúc; Space reset đúng tất cả biến và ẩn Tổng kết | **15đ** |
| **5** | Thẩm mỹ & Đóng gói | Chương trình chạy mượt, bóng và rổ phân biệt rõ; không lỗi đếm điểm sai | **10đ** |
| | **TỔNG CỘNG** | | **100đ** |

---

## **Bài tập 9: Bộ lọc trang sức thực tế ảo + thông báo tiếng Anh**

### 1. Nội dung đề bài

Lập trình **bộ lọc AR song ngữ toàn diện**: ≥ 4 đồ vật trang sức (mũ, bông tai trái, bông tai phải, ≥ 1 vật tự chọn) bám theo đúng vị trí bộ phận khuôn mặt qua Body Sensing liên tục. Nhấn Space để tất cả đổi trang phục ngẫu nhiên cùng lúc. Mỗi lần đổi: nhân vật tự mô tả bộ trang sức tiếng Việt → Translate sang Anh → TTS đọc to bản tiếng Anh.

### 2. Yêu cầu kỹ thuật chi tiết

**Công cụ AI bắt buộc sử dụng:**
- **Body Sensing** (bám theo tọa độ face parts liên tục)
- Extension **Translate** (dịch mô tả trang sức sang tiếng Anh)
- Extension **Text to Speech** (đọc mô tả tiếng Anh)

**Cấu tạo / Thành phần bắt buộc:**
- **≥ 4 nhân vật đồ vật**: Mũ, Bông tai trái, Bông tai phải, ≥ 1 vật tự chọn
- Mỗi đồ vật có **≥ 3 trang phục (costume)** khác nhau
- **1 biến số** `costumeIndex` chia sẻ giữa bông tai trái và phải để giữ cùng index
- **1 nhân vật Người dẫn** để Say mô tả và TTS

**Hoạt động / Tính năng bắt buộc:**
- Mỗi đồ vật bám đúng **face part coordinate** trong **Forever**:
  - Mũ → đỉnh đầu (top of head)
  - Bông tai trái → tai trái (left ear)
  - Bông tai phải → tai phải (right ear)
- Nhấn **Space**: **Broadcast** "changeJewelry"
  - Mỗi đồ vật nhận Broadcast → đổi costume ngẫu nhiên (pick random 1 to 3)
  - 2 bông tai: đổi cùng `costumeIndex` (pick random 1 lần, lưu vào biến, cả 2 cùng switch)
- Sau đổi: Người dẫn **Say** mô tả tiếng Việt → **Translate** sang Anh → **TTS Speak** mô tả Anh

### 3. Sản phẩm yêu cầu bàn giao

- **File code:** `.sb3` đặt tên `[Chi nhánh]-[Họ tên]-AI THCS-9.sb3`
- **Ảnh PNG** chụp toàn bộ khối lệnh: mỗi đồ vật (Forever Body Sensing) + Space trigger + Broadcast receiver + Người dẫn (Translate + TTS)
  - Đặt tên: `[Chi nhánh]-[Họ tên]-AI THCS-9.png`

### 4. Đáp án gợi ý (Kịch bản khối lệnh logic)

```
[Mũ]
Khi nhấn cờ xanh:
  Turn video on
  Forever: Go to x:(x of [top of head]), y:(y of [top of head])
Khi nhận "changeJewelry":
  Switch costume to (pick random 1 to 3)

[Bông tai trái]
Khi nhấn cờ xanh:
  Forever: Go to x:(x of [left ear]), y:(y of [left ear])
Khi nhận "changeJewelry":
  Switch costume to costumeIndex

[Bông tai phải]
Khi nhấn cờ xanh:
  Forever: Go to x:(x of [right ear]), y:(y of [right ear])
Khi nhận "changeJewelry":
  Switch costume to costumeIndex

[Khi nhấn Space - script ở nhân vật chính]:
  Set costumeIndex = (pick random 1 to 3)
  Broadcast "changeJewelry"

[Người dẫn]
Khi nhận "changeJewelry":
  Wait 0.5 seconds
  Set mô tả = "Bộ trang sức mới thật lộng lẫy!"
  Say mô tả for 2 seconds
  TTS (lang en) Speak (translate mô tả to "en")
```

![Đáp án gợi ý BT9](Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media/bt9_code.raw.png)

### 5. Tiêu chí chấm điểm (Rubric định lượng)

| STT | Tiêu chí đánh giá | Mức độ mô tả chất lượng đạt yêu cầu | score tối đa |
| :---: | :--- | :--- | :---: |
| **1** | Body Sensing ≥ 4 đồ vật | Cả 4 đồ vật bám đúng face part tương ứng liên tục; mũ đúng vị trí đỉnh đầu, 2 bông tai đúng 2 tai | **35đ** |
| **2** | Bông tai giống nhau | 2 bông tai luôn cùng costume index sau mỗi lần đổi (dùng biến `costumeIndex` chia sẻ, không đổi riêng lẻ) | **20đ** |
| **3** | Random costume + Broadcast | Space kích hoạt Broadcast; tất cả đổi costume ngẫu nhiên cùng lúc; mỗi đồ vật có ≥ 3 costume | **20đ** |
| **4** | Translate + TTS song ngữ | Sau mỗi lần đổi: Translate mô tả sang Anh đúng; TTS đọc to bản dịch tiếng Anh | **15đ** |
| **5** | Thẩm mỹ & Đóng gói | Trang sức rõ ràng trên camera; không bị lag hoặc lệch vị trí khi di chuyển | **10đ** |
| | **TỔNG CỘNG** | | **100đ** |

---

## **Bài tập 10: Hệ thống điểm danh AI toàn diện**

### 1. Nội dung đề bài

Lập trình **hệ thống điểm danh AI toàn diện** tích hợp toàn bộ kiến thức khoá học: huấn luyện Teachable Machine để nhận diện 3 thành viên, kết nối vào Dancing with AI. Trong 30 giây đếm ngược, AI nhận diện ai xuất hiện → ghi tên vào List → TTS đọc tên tiếng Việt. Khi hết giờ, nhân vật tổng kết tính số vắng, Translate sang Anh và TTS thông báo kết quả song ngữ.

### 2. Yêu cầu kỹ thuật chi tiết

**Công cụ AI bắt buộc sử dụng:**
- **Teachable Machine** (nhận diện 3 thành viên — huấn luyện trước khi lập trình)
- Extension **Text to Speech** (đọc tên khi điểm danh + thông báo tổng kết)
- Extension **Translate** (dịch thông báo tổng kết sang tiếng Anh)

**Cấu tạo / Thành phần bắt buộc:**
- **Teachable Machine** được huấn luyện đủ **≥ 3 nhãn** (3 thành viên) + 1 nhãn "Không ai" (background)
- **1 List** `presentList` lưu tên các thành viên đã xuất hiện
- **Biến số** `time` đếm ngược từ 30, hiển thị liên tục
- **Nhân vật Tổng kết** (ẩn ban đầu, xuất hiện sau Broadcast "timeUp")

**Hoạt động / Tính năng bắt buộc:**
- Kết nối model Teachable Machine qua Extension ML trong Dancing with AI
- Khi TM nhận diện 1 thành viên **VÀ** tên đó **chưa có trong List** `presentList`:
  - **Thêm tên** vào List
  - **TTS Speak** đọc "[Tên] đã điểm danh!"
  - **Say** tên thành viên trên màn hình trong 2 giây
- `time` đếm ngược mỗi giây; khi = 0: dừng nhận diện + **Broadcast** "timeUp"
- Nhân vật Tổng kết:
  - Tính `presentCount = length of List presentList`
  - Tạo câu thông báo: "Có X/3 thành viên điểm danh"
  - **TTS (vi)** Speak câu đó
  - **Translate** sang Anh → **TTS (en)** Speak bản dịch

### 3. Sản phẩm yêu cầu bàn giao

- **File code:** `.sb3` đặt tên `[Chi nhánh]-[Họ tên]-AI THCS-10.sb3`
- **Ảnh PNG** chụp toàn bộ khối lệnh: nhân vật chính (TM + List + TTS đọc tên) + nhân vật Tổng kết (Translate + TTS 2 ngôn ngữ)
  - Đặt tên: `[Chi nhánh]-[Họ tên]-AI THCS-10.png`

### 4. Đáp án gợi ý (Kịch bản khối lệnh logic)

```
Khi nhấn cờ xanh:
  Delete all of presentList
  Set time = 30
  Show [nhân vật chính], Hide [Tổng kết]

[Đồng hồ - script song song]
  Repeat until time = 0:
    Wait 1 second
    Change time by -1
  Broadcast "timeUp"

[Nhận diện - script song song]
  Repeat until time = 0:
    If [TM label = "Thành viên 1"] AND NOT (presentList contains "TV1"):
      Add "TV1" to presentList
      TTS (vi) Speak "Thành viên 1 đã điểm danh!"
      Say "✓ Thành viên 1" for 2 seconds
    If [TM label = "Thành viên 2"] AND NOT (presentList contains "TV2"):
      Add "TV2" to presentList
      TTS (vi) Speak "Thành viên 2 đã điểm danh!"
      Say "✓ Thành viên 2" for 2 seconds
    If [TM label = "Thành viên 3"] AND NOT (presentList contains "TV3"):
      Add "TV3" to presentList
      TTS (vi) Speak "Thành viên 3 đã điểm danh!"
      Say "✓ Thành viên 3" for 2 seconds
    Wait 0.5 seconds

[Nhân vật Tổng kết]
Khi nhận "timeUp":
  Show
  Set presentCount = length of presentList
  Set thông báo = (join "Có " (join presentCount "/3 thành viên điểm danh."))
  Say thông báo for 3 seconds
  TTS (lang vi) Speak thông báo
  Wait 1 second
  TTS (lang en) Speak (translate thông báo to "en")
```

![Đáp án gợi ý BT10](Ngan_hang_de_thuc_hanh_AI_THCS_10_bai-Media/bt10_code.raw.png)

### 5. Tiêu chí chấm điểm (Rubric định lượng)

| STT | Tiêu chí đánh giá | Mức độ mô tả chất lượng đạt yêu cầu | score tối đa |
| :---: | :--- | :--- | :---: |
| **1** | Teachable Machine | Model TM được huấn luyện ≥ 3 nhãn thành viên + 1 nhãn background; kết nối thành công vào Dancing with AI và phân biệt đúng 3 người | **30đ** |
| **2** | List điểm danh không trùng | Tên thành viên được thêm vào List đúng 1 lần (If kiểm tra chưa có); TTS đọc tên đúng khi nhận diện; List hiển thị trên màn hình | **25đ** |
| **3** | Đồng hồ 30 giây & Broadcast | `time` đếm ngược đúng từng giây; khi = 0 dừng nhận diện và Broadcast kích hoạt Tổng kết | **20đ** |
| **4** | Tổng kết song ngữ | Tính đúng số thành viên điểm danh; TTS đọc kết quả tiếng Việt; Translate sang Anh đúng; TTS đọc lại tiếng Anh | **15đ** |
| **5** | Thẩm mỹ & Đóng gói | Chương trình chạy mượt; có Wait 0.5s giữa các lần kiểm tra TM tránh nhận diện liên tục; giao diện rõ ràng | **10đ** |
| | **TỔNG CỘNG** | | **100đ** |

---

*Ngày soạn: 2026-06-19 | Người soạn: [Tên giáo viên] | Người review: [Tên reviewer]*

*Trạng thái: PREVIEW_ASSESSMENT — Cần human review và bổ sung ảnh PNG code mẫu trước khi phát hành chính thức*
