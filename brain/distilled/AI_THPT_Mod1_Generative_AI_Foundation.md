# AI_THPT_Mod1_Generative_AI_Foundation.md

# Bài 1: Bản chất của Trí tuệ Nhân tạo Sinh tạo (Generative AI)
## Môn: Công nghệ 10 - Chương trình Giáo dục Phổ thông 2018

---

## I. MỤC TIÊU BÀI HỌC

### Kiến thức:
- Hiểu được khái niệm cơ bản về Trí tuệ Nhân tạo Sinh tạo (Generative AI)
- Nắm vững nguyên lý hoạt động của các mô hình ngôn ngữ lớn (LLMs)
- Hiểu rõ khái niệm về xác suất, mô hình xác suất và tokens trong AI
- Nhận biết được hiện tượng "ảo giác" (hallucinations) trong AI

### Kỹ năng:
- Sử dụng thành thạo công cụ AI sinh tạo (Gemini AI) để tạo nội dung
- Thiết kế prompt hiệu quả cho các mục đích cụ thể
- Phân tích và đánh giá độ chính xác của nội dung do AI tạo ra
- Nhận diện các dấu hiệu của thông tin sai lệch do AI tạo ra

### Thái độ:
- Có cái nhìn khách quan về tiềm năng và hạn chế của AI
- Rèn luyện tư duy phản biện khi sử dụng công nghệ AI
- Có trách nhiệm đạo đức khi sử dụng và chia sẻ nội dung do AI tạo ra

---

## II. NỘI DUNG CHÍNH

### 1. Khám phá Trí tuệ Nhân tạo Sinh tạo

#### 1.1. Khái niệm Generative AI

**Generative AI (Trí tuệ Nhân tạo Sinh tạo)** là một nhánh của trí tuệ nhân tạo có khả năng tạo ra nội dung mới như văn bản, hình ảnh, âm thanh, video... dựa trên dữ liệu mà nó đã học được từ quá trình huấn luyện.

**So sánh với các loại AI truyền thống:**
- **AI truyền thống**: Chủ yếu phân tích và phân loại dữ liệu có sẵn
- **Generative AI**: Tạo ra nội dung hoàn toàn mới chưa từng tồn tại

**Ví dụ thực tế:**
- ChatGPT tạo bài viết, trả lời câu hỏi
- DALL-E tạo hình ảnh từ mô tả bằng lời
- GitHub Copilot hỗ trợ lập trình viên viết code

#### 1.2. Sự phát triển của Generative AI

Năm 2022-2023 đánh dấu bước ngoặt với sự ra đời của các mô hình lớn như ChatGPT, Claude, Gemini... khiến AI trở nên phổ biến và dễ tiếp cận hơn bao giờ hết.

### 2. Mô hình ngôn ngữ lớn (Large Language Models - LLMs)

#### 2.1. Cấu trúc cơ bản của LLMs

LLMs là các mô hình máy học được huấn luyện trên lượng dữ liệu văn bản khổng lồ (hàng triệu đến hàng tỷ trang tài liệu). Chúng học các mẫu ngữ pháp, ngữ nghĩa và kiến thức từ dữ liệu này.

**Các thành phần chính:**
- **Dữ liệu huấn luyện**: Hàng triệu tài liệu văn bản từ sách, báo, website...
- **Mạng nơ-ron sâu**: Hệ thống các lớp xử lý thông tin phức tạp
- **Cơ chế chú ý (Attention Mechanism)**: Giúp mô hình tập trung vào các phần quan trọng của đầu vào

#### 2.2. Quá trình huấn luyện

```
Dữ liệu văn bản → Tiền xử lý → Huấn luyện mô hình → Tối ưu hóa → Mô hình LLM
```

Quá trình này mất hàng tuần đến hàng tháng với hàng ngàn máy chủ chuyên dụng.

### 3. Mô hình Xác suất và Tokens

#### 3.1. Mô hình Xác suất trong AI

**Mô hình xác suất** là nền tảng hoạt động của các hệ thống AI hiện đại. Thay vì "hiểu" như con người, AI hoạt động dựa trên việc tính toán xác suất.

**Ví dụ minh họa:**
Khi bạn gõ "Tôi muốn ăn..." - AI sẽ tính toán xác suất các từ tiếp theo dựa trên hàng triệu câu đã học:
- "bữa sáng": 30%
- "cơm trưa": 25% 
- "phở": 20%
- "trái cây": 15%
- "kẹo": 7%
- "gỗ": 3%

AI sẽ chọn từ có xác suất cao nhất hoặc kết hợp ngẫu nhiên theo xác suất để tạo ra câu hoàn chỉnh.

#### 3.2. Khái niệm Tokens

**Token** là đơn vị cơ bản mà AI sử dụng để xử lý văn bản. Một token có thể là:

- **Từ nguyên bản**: "học", "sinh", "viên"
- **Phần của từ**: "học_sinh", "sinh_viên" (trong tiếng Việt), hoặc "un", "happy", "ness" (trong tiếng Anh)
- **Ký tự đặc biệt**: dấu câu, khoảng trắng, ký hiệu

**Ví dụ về tokenization:**
Câu: "Tôi là học sinh lớp 10"
Có thể được chia thành các tokens: ["Tôi", "là", "học", "sinh", "lớp", "10"]

**Tầm quan trọng của tokens:**
- Xác định độ dài đầu vào mà mô hình có thể xử lý
- Ảnh hưởng đến tốc độ và chi phí xử lý
- Quyết định cách mô hình hiểu và tạo văn bản

### 4. Cơ chế Dự đoán và Tạo Văn bản

#### 4.1. Quá trình tạo văn bản

```
Prompt đầu vào → Token hóa → Xử lý qua mạng nơ-ron → Tính xác suất → Chọn token tiếp theo → Lặp lại → Văn bản hoàn chỉnh
```

#### 4.2. Các phương pháp chọn token

- **Greedy decoding**: Luôn chọn token có xác suất cao nhất
- **Sampling**: Chọn token ngẫu nhiên theo phân phối xác suất
- **Top-k sampling**: Chỉ chọn từ k token có xác suất cao nhất
- **Nucleus sampling**: Chọn từ tập hợp các token có tổng xác suất đạt ngưỡng nhất định

### 5. Hiện tượng "Ảo giác" (Hallucinations)

#### 5.1. Định nghĩa và nguyên nhân

**Hallucinations** là hiện tượng AI tạo ra thông tin sai lệch, không chính xác hoặc hoàn toàn bịa đặt, mặc dù có vẻ hợp lý và thuyết phục.

**Nguyên nhân chính:**
- **Thiếu dữ liệu huấn luyện** về chủ đề cụ thể
- **Hiểu sai ngữ cảnh** từ đầu vào
- **Sự kết hợp ngẫu nhiên** của các mẫu đã học
- **Áp lực tạo nội dung** dài và chi tiết

#### 5.2. Các dạng phổ biến

- **Thông tin sai lệch**: Cung cấp số liệu, ngày tháng, tên người không chính xác
- **Sự kiện không tồn tại**: Tạo ra các sự kiện lịch sử giả mạo
- **Trích dẫn sai**: Gán lời nói cho người không từng nói điều đó
- **Chi tiết tưởng tượng**: Thêm các chi tiết không có thật vào nội dung đúng

---

## III. ỨNG DỤNG THỰC TẾ CỦA AI SINH TẠO

### 1. Trong Giáo dục

**Ưu điểm:**
- Hỗ trợ học sinh ôn tập, giải thích khái niệm
- Tạo bài tập, đề thi mẫu
- Cá nhân hóa quá trình học tập

**Nhược điểm:**
- Nguy cơ phụ thuộc quá mức
- Vấn đề đạo văn khi sử dụng nội dung AI
- Sai lệch thông tin ảnh hưởng đến kiến thức

### 2. Trong Công việc

**Ứng dụng:**
- Viết email, báo cáo
- Tạo nội dung marketing
- Hỗ trợ lập trình, phân tích dữ liệu

**Lưu ý:**
- Cần kiểm tra kỹ độ chính xác
- Không nên sử dụng cho tài liệu pháp lý, y tế quan trọng
- Phải ghi rõ nguồn nếu sử dụng nội dung AI

### 3. Trong Sáng tạo

**Khả năng:**
- Viết thơ, truyện ngắn
- Tạo hình ảnh, nhạc nền
- Phát triển ý tưởng sáng tạo

**Giới hạn:**
- Thiếu cảm xúc thực sự
- Không thể thay thế hoàn toàn sáng tạo con người
- Vấn đề bản quyền nội dung

---

## IV. HOẠT ĐỘNG KHÁM PHÁ

### Hoạt động 1: Trải nghiệm AI đầu tiên

**Mục tiêu:** Làm quen với giao diện và khả năng của AI sinh tạo

**Cách thực hiện:**
1. Truy cập Gemini AI hoặc công cụ AI tương tự
2. Nhập prompt đơn giản: "Giới thiệu ngắn gọn về bản thân em"
3. So sánh với cách bạn viết thực tế
4. Ghi nhận sự khác biệt về phong cách, từ ngữ

**Câu hỏi suy ngẫm:**
- Nội dung do AI tạo ra có giống cách bạn suy nghĩ không?
- Bạn nhận thấy điểm mạnh và điểm yếu gì của AI?

### Hoạt động 2: Thử nghiệm với các prompt khác nhau

**Mục tiêu:** Hiểu cách prompt ảnh hưởng đến kết quả

**Yêu cầu:**
- Tạo 3 prompt khác nhau cho cùng một chủ đề (ví dụ: "Lợi ích của việc đọc sách")
- Prompt 1: Đơn giản, chung chung
- Prompt 2: Có yêu cầu cụ thể về độ dài, phong cách
- Prompt 3: Có yêu cầu về đối tượng người đọc

**Quan sát:**
- So sánh độ dài, chất lượng, mức độ phù hợp của các kết quả
- Rút ra quy tắc viết prompt hiệu quả

### Hoạt động 3: Phát hiện "ảo giác"

**Mục tiêu:** Rèn luyện kỹ năng kiểm tra độ chính xác của AI

**Cách thực hiện:**
1. Hỏi AI về một sự kiện lịch sử cụ thể
2. Kiểm tra thông tin trên các nguồn đáng tin cậy
3. Ghi nhận các sai lệch (nếu có)
4. Thảo luận về lý do xảy ra sai lệch

**Ví dụ:** Hỏi AI về ngày sinh của một nhân vật lịch sử và kiểm tra lại

---

## V. BÀI TẬP THỰC HÀNH

### Bài tập 1: Phân tích Tokens

**Yêu cầu:** Hãy phân tích câu sau thành các tokens:
"Công nghệ AI đang thay đổi cách chúng ta học tập và làm việc."

**Gợi ý:** Có thể có nhiều cách phân tích khác nhau tùy theo hệ thống tokenization.

### Bài tập 2: Thiết kế Prompt hiệu quả

**Tình huống:** Bạn cần AI giúp viết một bài văn nghị luận về "Tác hại của mạng xã hội với học sinh".

**Yêu cầu:** 
- Viết 2 phiên bản prompt:
  - Prompt kém hiệu quả (thiếu cụ thể)
  - Prompt hiệu quả (có cấu trúc rõ ràng)

**Đánh giá:** So sánh kết quả từ 2 prompt và rút ra bài học.

### Bài tập 3: Nhận diện Hallucinations

**Cho đoạn văn sau do AI tạo ra:**
"Trong trận chiến Đống Đa năm 981, vua Lê Hoàn đã đánh bại quân Tống xâm lược. Chiến thắng này mở đầu cho thời kỳ độc lập lâu dài của Đại Việt."

**Nhiệm vụ:**
- Chỉ ra các sai lệch trong đoạn văn
- Giải thích tại sao AI lại tạo ra thông tin sai lệch
- Viết lại đoạn văn chính xác

---

## VI. KIẾN THỨC BỔ SUNG

### 1. Lịch sử phát triển AI

- **1956**: Thuật ngữ "Trí tuệ Nhân tạo" được đặt ra tại Hội nghị Dartmouth
- **1960s-1970s**: Giai đoạn "Mùa đông AI" đầu tiên
- **1980s-1990s**: AI chuyên gia phát triển mạnh
- **2000s**: Máy học (Machine Learning) bắt đầu phát triển
- **2010s**: Deep Learning và Neural Networks bùng nổ
- **2020s**: Generative AI trở nên phổ biến

### 2. Các mô hình AI nổi bật

- **GPT series** (OpenAI): ChatGPT, GPT-4
- **Claude** (Anthropic): Tập trung vào an toàn AI
- **Gemini** (Google): Tích hợp đa phương tiện
- **LLaMA** (Meta): Mô hình mã nguồn mở

### 3. Giới hạn của AI hiện tại

- **Không có ý thức**: AI không thực sự "hiểu" mà chỉ mô phỏng hành vi
- **Không có cảm xúc**: Không thể trải nghiệm cảm xúc như con người
- **Phụ thuộc dữ liệu huấn luyện**: Bị giới hạn bởi những gì đã học
- **Không có kiến thức ngoài huấn luyện**: Không biết thông tin sau ngày cutoff

---

## VII. HƯỚNG DẪN GIÁO VIÊN

### 1. Chuẩn bị trước buổi học

**Thiết bị cần thiết:**
- Máy tính/laptop/tablet có kết nối internet
- Tài khoản truy cập công cụ AI (Gemini, ChatGPT, v.v.)
- Máy chiếu hoặc màn hình chia sẻ

**Tài liệu chuẩn bị:**
- Phiếu học tập cho học sinh
- Mẫu prompt tham khảo
- Danh sách ví dụ về hallucinations

### 2. Phương pháp giảng dạy

**Phương pháp khuyến khích:**
- Học qua trải nghiệm thực tế
- Học hợp tác theo nhóm nhỏ
- Đặt câu hỏi mở để kích thích tư duy
- Liên hệ thực tiễn thường xuyên

**Lưu ý khi sử dụng AI trong lớp:**
- Không để học sinh phụ thuộc hoàn toàn
- Hướng dẫn cách kiểm tra độ chính xác
- Nhấn mạnh vấn đề đạo đức và bản quyền

### 3. Đánh giá học sinh

**Theo dõi trong quá trình học:**
- Mức độ tham gia hoạt động
- Khả năng đặt câu hỏi và phản biện
- Kỹ năng sử dụng công cụ AI

**Bài tập đánh giá:**
- Thiết kế prompt hiệu quả
- Phân tích kết quả AI tạo ra
- Nhận diện và sửa lỗi thông tin

### 4. Lưu ý đặc biệt

**An toàn thông tin:**
- Không chia sẻ thông tin cá nhân nhạy cảm với AI
- Cảnh báo học sinh về rủi ro bảo mật

**Đạo đức AI:**
- Không sử dụng AI để gian lận trong học tập
- Luôn ghi rõ nguồn khi sử dụng nội dung AI
- Tránh lan truyền thông tin sai lệch

---

## VIII. CÂU HỎI ÔN TẬP

### Câu hỏi trắc nghiệm

1. **Token trong AI là gì?**
   a) Một loại tiền điện tử
   b) Đơn vị cơ bản để xử lý văn bản
   c) Tên gọi của mô hình AI
   d) Phần mềm diệt virus

2. **Hiện tượng "hallucinations" trong AI có nghĩa là gì?**
   a) AI bị lỗi phần cứng
   b) AI tạo ra thông tin sai lệch
   c) AI không thể xử lý văn bản
   d) AI bị nhiễm virus

3. **LLMs là viết tắt của cụm từ nào?**
   a) Large Language Models
   b) Little Learning Machines
   c) Logical Language Methods
   d) Linear Logic Models

### Câu hỏi tự luận

1. **Giải thích tại sao AI không thực sự "hiểu" như con người mà chỉ dựa trên xác suất?**

2. **Liệt kê 3 ứng dụng thực tế của AI sinh tạo trong cuộc sống hàng ngày và nêu ưu-nhược điểm của từng ứng dụng.**

3. **Thiết kế một prompt hiệu quả để yêu cầu AI giúp bạn viết một bài văn nghị luận về "Bảo vệ môi trường".**

---

## IX. MỞ RỘNG KIẾN THỨC

### 1. Đọc thêm

- "Life 3.0" - Max Tegmark: Về tương lai của trí tuệ nhân tạo
- "The Alignment Problem" - Brian Christian: Về việc hướng dẫn AI hoạt động đúng mục tiêu
- Các bài báo khoa học về transformer architecture và attention mechanism

### 2. Tham khảo trực tuyến

- Papers with Code: https://paperswithcode.com/
- Hugging Face: https://huggingface.co/
- AI Safety resources: https://aisafety.info/

### 3. Dự án nhỏ

**Ý tưởng:** Thiết kế một ứng dụng nhỏ sử dụng API của mô hình AI để giải quyết một vấn đề cụ thể trong trường học (ví dụ: tạo bài tập toán, dịch thuật, kiểm tra chính tả...)

---

## X. KẾT LUẬN

Bài học này giúp học sinh hiểu rõ bản chất hoạt động của AI sinh tạo, từ đó sử dụng công nghệ này một cách thông minh và có trách nhiệm. Việc hiểu rõ giới hạn và tiềm năng của AI sẽ giúp học sinh chuẩn bị tốt hơn cho tương lai trong thời đại số hóa.

**Những điểm cần nhớ:**
- AI là công cụ hỗ trợ, không phải thay thế con người
- Luôn kiểm tra độ chính xác của thông tin do AI tạo ra
- Sử dụng AI có đạo đức và trách nhiệm
- Tiếp tục học hỏi và cập nhật kiến thức về AI

---

**Tài liệu tham khảo:**
- Bộ GD&ĐT (2018). Chương trình giáo dục phổ thông 2018 - Môn Công nghệ
- Brown et al. (2020). Language Models are Few-Shot Learners
- Vaswani et al. (2017). Attention Is All You Need
- Các tài liệu hướng dẫn sử dụng Gemini AI của Google