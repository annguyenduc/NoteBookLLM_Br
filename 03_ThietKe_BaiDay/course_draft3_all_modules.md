# PHÁT TRIỂN ỨNG DỤNG VỚI AI

**Mã học phần: AIApp-M2.1 | Bản Draft 3 — Hợp Nhất 3 Module**

---

# MỤC LỤC

- Module 1: Nền Tảng Google AI Studio
  - 1.1. Xu hướng Vibe Coding (Lập Trình Bằng Ngôn Ngữ Tự Nhiên)
  - 1.2. Hướng dẫn sử dụng Google AI Studio (6 Chế Độ & Live Demo)
  - 1.3. Giới hạn về tài khoản (Quota, Troubleshooting & API Key Security)
- Module 2: Những Yếu Tố Cốt Lõi Cần Xây Dựng App và Cấu Trúc Prompt
  - 2.1. Những yếu tố cần để xây dựng App
  - 2.2. Thiết kế sản phẩm AI
  - 2.3. Kiểm Thử Ứng Dụng & Sửa Lỗi AI Fabrication
- Module 3: Đạo Đức và Trách Nhiệm AI
  - 3.1. Các Rủi Ro AI Trong Giáo Dục
  - 3.2. Năm Nguyên Tắc Responsible AI
  - 3.3. Khung Phân Tích Đạo Đức AI Cho Giáo Viên
  - 3.4. Triển Khai AI Có Trách Nhiệm Trong Lớp Học

---

# GIỚI THIỆU KHÓA HỌC

Khóa học Phát Triển Ứng Dụng Với AI được thiết kế nhằm trang bị cho giáo viên tư duy Spec-first Vibe Coding — khả năng chuyển hóa ý tưởng sư phạm thành các ứng dụng AI chạy thật mà không cần nền tảng lập trình chuyên sâu.

**Mục tiêu:** Thực hiện bài học này giáo viên sẽ:

- Hiểu rõ bản chất Vibe Coding và triết lý Spec-first trong phát triển ứng dụng với AI.
- Thành thạo 6 chế độ làm việc trên Google AI Studio qua trải nghiệm Live Demo.
- Nắm vững 5 thành phần cốt lõi của Yêu cầu sản phẩm (User, Input, Output, Features, Constraints).
- Thiết kế Data Flow, UI Wireframe và viết Master Prompt hoàn chỉnh.
- Áp dụng 5 nguyên tắc Trí Tuệ Nhân Tạo Có Trách Nhiệm (Responsible AI) trong giảng dạy.

**Hình thức:** Tự học trên elearning + Trao đổi giải đáp thắc mắc.

**Yêu cầu cần đạt:** Thực hiện đủ 3 bài đánh giá (Bài tập thực hành >= 70%, Bài kiểm tra cuối khóa >= 70%, Bài thực hành giảng dạy ĐẠT).

---

# VẬT TƯ THIẾT BỊ

| Tên thiết bị | Yêu cầu | Số lượng |
|---|---|---|
| Máy tính hoặc máy tính bảng | Kết nối Internet, trình duyệt Chrome/Edge mới nhất | 1 cái |
| Tài khoản Google (Gmail) | Dùng để đăng nhập Google AI Studio miễn phí | 1 tài khoản |
| Điện thoại thông minh (Smartphone) | Camera >= 8MP, dùng để thực hành chụp ảnh Live Demo | 1 cái |

---

# MODULE 1: NỀN TẢNG GOOGLE AI STUDIO

*Trong module này, các bạn sẽ làm chủ 3 nội dung cốt lõi về công cụ và tư duy lập trình bằng AI:*

- *1.1. Xu hướng Vibe Coding (Lập trình bằng ngôn ngữ tự nhiên)*
- *1.2. Hướng dẫn sử dụng Google AI Studio (6 chế độ làm việc cốt lõi & Live Demo)*
- *1.3. Giới hạn về tài khoản (Hạn ngạch Quota, Troubleshooting & An toàn API Key)*

**Thời lượng:** 90 phút

**Mục tiêu bài học:**

- Hiểu rõ bản chất xu hướng Vibe Coding và sự dịch chuyển từ lập trình viên sang vai trò Kỹ sư Trưởng (Lead Engineer) sư phạm.
- Thành thạo thao tác trên 6 chế độ làm việc của Google AI Studio (Build Mode, Live Preview, Annotation Mode với bút vẽ sửa UI).
- Nhận biết thông số hạn ngạch tài khoản miễn phí, xử lý 4 sự cố kỹ thuật thường gặp và bảo mật Khóa kết nối ứng dụng (API Key).

**Sản phẩm đầu ra:** Khởi tạo tài khoản Google AI Studio + Tạo Khóa API Key an toàn + Thực hành trải nghiệm 6 chế độ và nghiệm thu Bảng kiểm kỹ năng Module 1.

---

## 1.1. Xu Hướng Vibe Coding (Lập Trình Bằng Ngôn Ngữ Tự Nhiên)

### 1.1.1. Sự Dịch Chuyển Lịch Sử Của Ngôn Ngữ Lập Trình

Trong 70 năm qua, ngành khoa học máy tính đã trải qua 3 làn sóng dịch chuyển về ngôn ngữ giao tiếp giữa con người và máy tính:

- **Thế hệ 1 (Mã máy & Hợp ngữ — Assembly/Machine Code):** Con người phải giao tiếp với máy tính bằng các chuỗi số nhị phân 0 và 1 hoặc các câu lệnh phần cứng phức tạp — cực kỳ khó học và chỉ dành riêng cho các kỹ sư điện tử/phần cứng chuyên sâu.
- **Thế hệ 2 (Ngôn ngữ bậc cao — C++, Java, Python):** Con người viết mã lệnh dựa trên cú pháp logic nghiêm ngặt — đòi hỏi phải học lập trình bài bản nhiều năm, chỉ cần thiếu 1 dấu chấm phẩy cũng khiến ứng dụng sập (crash).
- **Thế hệ 3 (Vibe Coding — Ngôn ngữ tự nhiên):** Con người dùng chính ngôn ngữ giao tiếp hàng ngày để mô tả mong muốn — mô hình Trí tuệ nhân tạo (AI) sẽ tự động biên dịch và sinh ra toàn bộ mã nguồn.

*Khái niệm Vibe Coding: Do Andrej Karpathy — cựu Giám đốc AI của Tesla và đồng sáng lập OpenAI — chính thức định danh năm 2025. Vibe Coding là phương pháp xây dựng phần mềm mà ở đó bạn chỉ cần mô tả ý định và cảm nhận về sản phẩm, mô hình ngôn ngữ lớn (LLM) sẽ đảm nhận 100% việc viết mã lệnh.*

*"Just vibe with the AI. Forget that the code even exists." — Andrej Karpathy*
*(Hãy cứ tương tác tự nhiên với AI. Hãy quên đi sự tồn tại của mã lệnh.)*

### 1.1.2. Tại Sao Giáo Viên Cần Nắm Bắt Vibe Coding?

Trước đây, rào cản lớn nhất ngăn cản giáo viên tạo ra các phần mềm dạy học riêng là kỹ năng lập trình thủ công. Quy trình cũ thường kéo dài và tốn kém:

```
[Ý tưởng sư phạm của GV] -> [Thuê Lập trình viên] -> [Chờ 3-6 tháng] -> [Sản phẩm sai ý đồ]
```

Với Vibe Coding trên Google AI Studio, khoảng cách này hoàn toàn bị xóa bỏ:

```
[Ý tưởng sư phạm của GV] -> [Mô tả bằng tiếng Việt] -> [AI Studio tạo App chạy thật trong 3 phút]
```

**Case Study thực tế trong giảng dạy STEM:**

- Môn Sinh học (THCS): Giáo viên tạo App Plant ID cho học sinh chụp ảnh lá cây ngoài sân trường — AI phân tích tên tiếng Việt, tên Latin, họ thực vật và mức độ tin cậy ngay tại chỗ.
- Môn Vật Lý (THPT): Giáo viên tạo App Physics Solver cho học sinh tải ảnh sơ đồ mạch điện — AI phân tích và đưa ra câu hỏi gợi ý tư duy.
- Môn Hóa học (THCS): Giáo viên tạo App Chemical Balancer giúp học sinh nhập phương trình hóa học — AI nhận diện và cân bằng phương trình kèm giải thích.

### 1.1.3. Hai Mặt Của Vibe Coding: Ngẫu Nhiên vs. Có Bản Đặc Tả (Spec-First)

- **Vibe Coding ngẫu nhiên (Demo A):** Gõ câu lệnh ngắn mơ hồ, AI tự suy đoán và tạo ra ứng dụng dư thừa tính năng — hoàn toàn không dùng được cho tiết học thực địa.
- **Spec-First Vibe Coding (Demo B):** Giáo viên chuẩn bị bản đặc tả sản phẩm gồm 5 thành phần cốt lõi trước khi ra lệnh — AI Studio tạo ra đúng 1 màn hình tinh gọn, đúng yêu cầu.

---

## 1.2. Hướng Dẫn Sử Dụng Google AI Studio

Google AI Studio (aistudio.google.com) là môi trường nguyên mẫu nhanh (rapid prototyping environment) cho phép giáo viên biến ý tưởng thành phần mềm không cần cài đặt công cụ lập trình.

### 1.2.1. Cấu Trúc 6 Chế Độ Làm Việc Cốt Lõi

1. **Câu lệnh hệ thống (System Instructions):** Nơi thiết lập nhân cách và ngữ cảnh cho AI.
2. **Khung nhập câu lệnh (Chat / Prompt Panel):** Nơi giáo viên gõ Master Prompt chứa bản đặc tả.
3. **Lựa chọn mô hình (Model Selection):** Gemini Flash (nhanh), Gemini Pro (sâu), Gemini Multimodal (nhận diện ảnh Vision).
4. **Chế độ xây dựng ứng dụng (Build Mode):** Khi bật, AI tự động viết mã nguồn HTML/JS/CSS tạo ứng dụng hoàn chỉnh.
5. **Màn hình xem trước trực tiếp (Live Preview):** Trải nghiệm ứng dụng chạy thật ngay lập tức.
6. **Công cụ bút vẽ phản hồi (Annotation Mode):** Khoanh tròn trực tiếp lên giao diện và gõ ghi chú — AI tự điều chỉnh theo đúng ý bạn.

### 1.2.2. Quy Trình 3 Bước Khởi Tạo Dự Án Đầu Tiên

```
Bước 1: Đăng nhập  -> Truy cập aistudio.google.com bằng tài khoản Google.
Bước 2: Tạo Prompt -> Bấm Create New Prompt -> Chọn Gemini 2.0 Flash -> Bật Build Mode.
Bước 3: Live Demo  -> Nạp Prompt Plant ID -> Trải nghiệm Live Preview -> Dùng Annotation Mode sửa UI.
```

★ **Thử thách 1:** Thực hành mở Google AI Studio, chọn Gemini 2.0 Flash, bật Build Mode và tạo ứng dụng đầu tiên (10 phút).

### 1.2.3. Trình Diễn Trực Tiếp — So Sánh Demo A và Demo B

**Bối cảnh:** Giáo viên dẫn học sinh THCS đi thực địa môn Sinh học. Học sinh phải phân biệt các loại cây và viết báo cáo. Hạn chế: học sinh khó phân biệt cây khi quan sát.

**TRÌNH DIỄN A — Vibe Coding Không Có Kế Hoạch:**

Câu lệnh nạp vào AI Studio:

```
Tạo cho tôi app nhận diện cây
```

Kết quả: AI tạo ra ứng dụng quá tải với cẩm nang chăm sóc cây cảnh đa tab, lịch tưới nước, bón phân — hoàn toàn lạc đề với bài học thực địa Sinh học THCS.

*Lưu ý: AI tưởng bạn làm ứng dụng chăm sóc cây cảnh trong nhà. Ví dụ: chụp chiếc xe vẫn có phần hướng dẫn tưới nước.*

**TRÌNH DIỄN B — Spec-First Vibe Coding:**

Trước khi gõ lệnh, giáo viên đã chuẩn bị bản đặc tả:

- Người dùng mục tiêu: Học sinh lớp 6 ngoài sân trường
- Đầu vào: Ảnh chụp lá cây từ điện thoại
- Đầu ra: Tên tiếng Việt, tên khoa học, mô tả 2 câu, thang độ tin cậy
- Ràng buộc: Không đăng nhập, không lưu dữ liệu

Câu lệnh (Master Prompt 5 thành phần):

```
Build a Plant Identifier web app for Vietnamese secondary school biology field trips.
Allow students to upload an image or take a photo of a plant/leaf outside the schoolyard.
Call Gemini API to analyze and return ONLY: name_vn, scientific_name, family,
description (2 short sentences), confidence_level (High/Medium/Low).
Display results in a single-page clean card layout with forest green header,
NO indoor gardening care features, and a disclaimer: Results for reference only.
```

Kết quả: Chỉ có 1 file giao diện, hiển thị đúng 5 trường chuẩn bài học Sinh học THCS, không có tính năng thừa.

*Kết quả: 5 phút chuẩn bị Spec + 10 phút Build = Ứng dụng chạy thật, đúng yêu cầu.*

---

## 1.3. Giới Hạn Về Tài Khoản (Quota, Troubleshooting & API Key Security)

### 1.3.1. Bảng Thông Số Hạn Ngạch Sử Dụng (Quota Table)

| Thông số kỹ thuật | Giới hạn Miễn phí | Cách quản lý trong lớp học |
|---|---|---|
| Lượt gọi theo phút (RPM) | 15 lượt / phút | Không nhấp nút Phân Tích liên tục |
| Lượt gọi theo ngày (RPD) | 1.000 lượt / ngày | Đủ cho 1-2 lớp thực hành trong ngày |
| Dung lượng ảnh đầu vào | Tối đa 5MB / ảnh | Thêm tính năng nén ảnh vào bản Spec |
| Giới hạn đầu ra (Output Token) | 8.192 tokens / lần | Đảm bảo mã nguồn không bị ngắt |

*Lưu ý: Chính sách có thể thay đổi theo Google. Cần đọc Rate Limit nếu gặp lỗi.*

### 1.3.2. Cẩm Nang Xử Lý 4 Sự Cố Kỹ Thuật Thường Gặp

| Sự cố | Nguyên nhân | Cách xử lý |
|---|---|---|
| Lỗi 429 Too Many Requests | Nhiều học sinh bấm cùng lúc, vượt 15 RPM | Chờ 60 giây, đếm nhịp trước khi bấm lại |
| Lỗi hết hạn ngạch ngày (Quota Exceeded) | Quá nhiều lớp dùng 1 tài khoản trong ngày | Chuẩn bị sẵn tài khoản Google dự phòng |
| Lỗi ảnh quá dung lượng (> 5MB) | Học sinh chụp chế độ HD/4K | Hướng dẫn cài camera độ phân giải tiêu chuẩn |
| Lỗi lộ Khóa API Key | Dán API Key lên mạng công khai | Bấm Revoke/Delete Key tạo khóa mới ngay |

### 1.3.3. Quy Tắc An Toàn & Bảo Mật Khóa API

*CẢNH BÁO BẢO MẬT: Khóa API (API Key) như chìa khóa nhà. Nếu lộ ra ngoài, người khác có thể dùng trộm hạn ngạch 1.000 RPD của bạn.*

3 Quy tắc bảo mật:

- **Không dán công khai:** Không đưa API Key lên mạng xã hội hoặc kho lưu trữ công khai.
- **Sử dụng môi trường nội bộ:** Chạy ứng dụng trong Live Preview của Google AI Studio.
- **Thu hồi khi nghi ngờ:** Vào Get API Key trên AI Studio và bấm Delete/Revoke để tạo khóa mới.

★ **Thử thách 2:** Khởi tạo 01 Khóa API Key cá nhân và thực hiện quy trình kiểm tra bảo mật (10 phút).

---

## NHỮNG ĐIỂM CỐT LÕI MODULE 1

- **Vibe Coding làm chủ công cụ:** Giáo viên chuyển sang vai trò Kỹ sư Trưởng điều khiển AI bằng ngôn ngữ tự nhiên.
- **Khám phá 6 chế độ Google AI Studio:** Thành thạo Build Mode, Live Preview và Annotation Mode.
- **Quản lý hạn ngạch & Bảo mật API Key:** Kiểm soát 15 RPM / 1.000 RPD và nắm lòng Cẩm nang Troubleshooting 4 sự cố.

## BẢNG KIỂM NGHIỆM THU KỸ NĂNG MODULE 1

*Học viên tự kiểm tra 6 kỹ năng sau khi hoàn thành Module 1:*

- [ ] Kỹ năng 1: Đăng nhập thành công Google AI Studio tại aistudio.google.com.
- [ ] Kỹ năng 2: Khởi tạo và bảo mật Khóa API Key cá nhân.
- [ ] Kỹ năng 3: Phân biệt khi nào dùng Gemini 1.5 Flash và Gemini 2.0 Flash (Multimodal Vision).
- [ ] Kỹ năng 4: Kích hoạt thành công chế độ xây dựng ứng dụng (Build Mode).
- [ ] Kỹ năng 5: Sử dụng thành thạo công cụ bút vẽ Annotation Mode để chỉnh sửa giao diện.
- [ ] Kỹ năng 6: Xử lý được lỗi quá hạn ngạch 429 Too Many Requests.

*Bàn giao sang Module 2: Sau khi làm chủ nền tảng Google AI Studio, các bạn sẵn sàng học 5 thành phần Requirement, thiết kế UI/UX và biên dịch Master Prompt hoàn chỉnh.*

---

# MODULE 2: NHỮNG YẾU TỐ CỐT LÕI CẦN XÂY DỰNG APP VÀ CẤU TRÚC PROMPT

*Trong module này, các bạn sẽ làm chủ 3 phần trọng tâm:*

- *2.1. Những Yếu Tố Cần Để Xây Dựng App (Xác định bài toán & 5 Thành phần Requirements)*
- *2.2. Thiết Kế Sản Phẩm AI (Data Flow, UI Wireframe, UX Microsoft & Master Prompt)*
- *2.3. Kiểm Thử Ứng Dụng & Sửa Lỗi AI Fabrication (Quy trình 5 Lớp & Release Candidate)*

**Thời lượng:** 90 phút

**Mục tiêu bài học:**

- Xác định bài toán thực tế và bóc tách chính xác 5 thành phần Yêu cầu sản phẩm (Requirements Breakdown).
- Thiết kế Data Flow, UI Wireframe, đánh giá 4 tiêu chí UX Microsoft và biên dịch Master Prompt 5 thành phần.
- Thực hành Kiểm thử 5 Lớp (5-Layer Testing), phát hiện lỗi AI Fabrication và nghiệm thu Release Candidate.

**Sản phẩm đầu ra:** Product Specification + UI Wireframe + Checklist 5 Lớp — Điền vào Hồ Sơ Dự Án Phần 1 & 2.

---

## 2.1. Những Yếu Tố Cần Để Xây Dựng App

Quy trình Spec-first Vibe Coding:

```
Bài toán -> Yêu cầu -> Bản đặc tả (Spec) -> Lập trình với AI (Vibe Code) -> Đánh giá -> Cải tiến -> Triển khai
```

### 2.1.1. Xác Định Bài Toán Thực Tế (Problem Framing)

Trước khi viết đặc tả, trả lời 3 câu hỏi nền tảng:

| Câu hỏi | Ví dụ minh hoạ (Plant ID App) |
|---|---|
| Ai gặp vấn đề? | Học sinh lớp 6 khi học thực địa Sinh học ngoài sân trường |
| Vấn đề là gì? | Không nhớ tên cây, không mang sách giáo khoa, dễ tra cứu nhầm |
| Dùng AI có phù hợp không? | Rất phù hợp — AI Vision nhận diện ảnh tức thì, không cần cơ sở dữ liệu lớn |

*Lăng kính kỹ thuật: Câu hỏi thứ ba thường bị bỏ qua. Không phải bài toán nào cũng cần AI. Nếu một tờ phiếu bài tập in sẵn cũng giải quyết được — thì không cần xây app.*

★ **Thử thách:** Điền vào ô bên dưới cho bài toán của chính bạn:

```
Ai gặp vấn đề?              _______________________________________________
Vấn đề là gì?               _______________________________________________
Dùng AI có phù hợp không?   _______________________________________________
Lý do:                      _______________________________________________
```

### 2.1.2. 5 Thành Phần Yêu Cầu Sản Phẩm Cốt Lõi (Requirements Breakdown)

Mọi ứng dụng AI giáo dục chuẩn mực đều được cấu thành từ 5 yếu tố cốt lõi:

| Thành phần | Câu hỏi định hướng | Áp dụng Plant ID App |
|---|---|---|
| 1. Người dùng mục tiêu (Target User) | Ai dùng? Trong ngữ cảnh nào? | Học sinh lớp 6, điện thoại ngoài sân trường |
| 2. Dữ liệu đầu vào (Input) | Đưa thông tin gì vào App? | Ảnh JPG/PNG, tối đa 5MB |
| 3. Kết quả đầu ra (Output) | App trả về thông tin gì? | Tên VN, Tên Latin, Họ TV, Mô tả 2 câu, Độ tin cậy |
| 4. Chức năng cốt lõi (Core Features) | Nút bấm & thao tác chính? | Khung upload, Nút Phân Tích, Thẻ kết quả, Nút Chụp lại |
| 5. Ràng buộc (Constraints) | App KHÔNG ĐƯỢC làm gì? | Không lưu dữ liệu HS, không bắt đăng nhập, giới hạn 5MB |

*Lăng kính kỹ thuật: Ràng buộc sản phẩm (Constraints) thường bị bỏ sót. Trong môi trường giáo dục, ràng buộc về quyền riêng tư học sinh là bắt buộc về mặt pháp lý và đạo đức.*

★ **Thử thách:** Điền bảng 5 thành phần cho bài toán của bạn:

```
1. Người dùng mục tiêu:  ___________________________________
2. Dữ liệu đầu vào:     ___________________________________
3. Kết quả đầu ra:      ___________________________________
4. Chức năng cốt lõi:   ___________________________________
5. Ràng buộc:           Không ___________________________
```

---

## 2.2. Thiết Kế Sản Phẩm AI

*Lăng kính kỹ thuật: Thiết kế thực sự là quyết định luồng dữ liệu (Data Flow) và trải nghiệm người dùng (UX) trước khi viết bất kỳ dòng lệnh nào. Bước này giúp ra lệnh cho AI đúng hướng.*

### 2.2.1. Thiết Kế Luồng Dữ Liệu (Data Flow)

Vẽ sơ đồ mô tả dữ liệu di chuyển từ Input qua AI đến Output:

```
[Học sinh chụp / upload ảnh]
            |
[App hiển thị Đang phân tích...]
            |
[Gửi ảnh đến Gemini Vision API]
            |
   [Gemini phân tích hình ảnh]
         /              \
       CÓ              KHÔNG
        |                |
[Hiển thị thẻ kết quả]  [Hiển thị Không xác định]
 Tên VN, Latin, Mô tả,   + Lời khuyên hỏi GV
 Độ tin cậy: Cao
```

### 2.2.2. Thiết Kế Giao Diện (UI Wireframe)

Phác thảo bố cục màn hình chính — bản vẽ kiến trúc mô tả cho AI:

```
+--------------------------------------+
|  Nhận Diện Cây Thực Địa              | <- Header xanh lá
|  [Sinh học lớp 6 - THCS]            |
+--------------------------------------+
|   [ Chụp ảnh / Upload ảnh ]         | <- Vùng upload lớn, dễ bấm
+--------------------------------------+
|           [ PHÂN TÍCH ]              | <- Nút bấm lớn kích hoạt AI
+--------------------------------------+
|  Đang phân tích hình ảnh...         | <- Trạng thái chờ (Loading)
+--------------------------------------+
|  Tên tiếng Việt: Cây Bàng           | <- Thẻ hiển thị kết quả
|  Latin: Terminalia catappa          |
|  Mô tả: Cây thân gỗ...              |
|  Độ tin cậy: Cao                    |
+--------------------------------------+
|  [ Chụp lại ]                        | <- Nút thực hiện lại
+--------------------------------------+
|  Kết quả mang tính tham khảo        | <- Chú thích miễn trừ trách nhiệm
+--------------------------------------+
```

### 2.2.3. Thiết Kế Trải Nghiệm Người Dùng (UX theo 4 Tiêu Chí Microsoft)

Microsoft định nghĩa UX tốt qua 4 tiêu chí — bộ công cụ tự đánh giá sản phẩm trước khi mang vào lớp:

| Tiêu chí | Câu hỏi kiểm tra | Áp dụng Plant ID App |
|---|---|---|
| Useful — Có ích | Ứng dụng giải quyết đúng bài toán thực tế không? | ĐẠT — Phục vụ trực tiếp bài thu hoạch thực địa Sinh học |
| Reliable — Đáng tin cậy | AI trung thực thông báo khi không chắc chắn không? | ĐẠT — Hiển thị Độ tin cậy: Thấp kèm lời khuyên hỏi GV |
| Accessible — Dễ tiếp cận | Học sinh không giỏi công nghệ có dễ dùng không? | ĐẠT — Nút chụp to ở trung tâm, không cần đăng nhập |
| Pleasant — Dễ chịu | Giao diện thân thiện, phù hợp ngữ cảnh không? | ĐẠT — Tông xanh lá mộc mạc, font to dễ đọc ngoài trời nắng |

*Lăng kính kỹ thuật: Tiêu chí Reliable (Đáng tin cậy) đặc biệt quan trọng. AI không bao giờ được trả lời chắc chắn khi đang đoán mò — điều này rèn luyện học sinh tư duy phản biện với công nghệ AI.*

### 2.2.4. Cấu Trúc Master Prompt (Lệnh Điều Khiển Tối Ưu 5 Thành Phần)

Master Prompt chứa đầy đủ bản đặc tả để đưa vào Build Mode. Cấu trúc 5 thành phần:

```
[1. VAI TRÒ (Role)]       : You are an expert Web Developer & STEM Teacher.
[2. BÀI TOÁN (Context)]   : Build a Plant Identifier app for biology field trips.
[3. ĐẶC TẢ (Input/Output)]: Input: Leaf image. Output ONLY: 5 exact fields.
[4. GIAO DIỆN (UI/UX)]    : Mobile-first 1-page layout, green header.
[5. RÀNG BUỘC (Constraints)]: NO indoor care info, NO login, include disclaimer.
```

Master Prompt mẫu hoàn chỉnh:

```
Act as an expert Web Developer and STEM Educator.
Build a Plant Identifier web application for Vietnamese secondary school biology
field trips. Allow students to upload an image or take a photo of a plant/leaf.
Call Gemini Vision API to analyze and return ONLY 5 exact fields:
1. name_vn (Vietnamese name)
2. scientific_name (Latin name)
3. family (Plant family)
4. description (2 short simple sentences)
5. confidence_level (High/Medium/Low)
Display results in a single-page clean card layout with forest green header.
RÀNG BUỘC: NO unnecessary indoor gardening care features.
NO user login or registration required. NO student data or photo storage.
Footer disclaimer: Results for reference only, check with teacher.
```

### 2.2.5. Viết Product Specification (Bản Đặc Tả Chi Tiết Sản Phẩm)

*Lăng kính kỹ thuật: Product Specification chỉ cần đủ để trả lời: Nếu AI đọc tờ này, nó có biết cần làm gì không?*

Ví dụ Bản Đặc Tả Sản Phẩm Hoàn Chỉnh (Plant ID Spec):

```
PRODUCT SPECIFICATION — Ứng Dụng Nhận Diện Cây Trồng Thực Địa
Phiên bản: v1.0

1. MÔ TẢ SẢN PHẨM
   Ứng dụng AI hỗ trợ học sinh lớp 6 nhận diện tên cây bằng ảnh chụp từ
   điện thoại, phục vụ bài học thực địa Sinh học.

2. PHẠM VI PHIÊN BẢN 1 (Tính năng SẼ làm)
   - Nhận ảnh upload hoặc chụp trực tiếp từ camera
   - Phân tích qua Gemini API và trả về 5 trường chuẩn
   - Hiển thị cảnh báo khi độ tin cậy ở mức thấp
   - Giao diện tối ưu di động (mobile-first), 1 màn hình

3. NGOÀI PHẠM VI (Tính năng KHÔNG làm ở v1)
   - Không lưu lịch sử tra cứu
   - Không có bản đồ phân bố cây
   - Không chạy chế độ offline

4. YÊU CẦU CHI TIẾT
   Target User : Học sinh lớp 6 THCS, dùng điện thoại ngoài sân
   Input       : Ảnh JPG/PNG từ camera/upload, tối đa 5MB
   Output      : Tên VN, Tên Latin, Họ TV, Mô tả 2 câu, Độ tin cậy
   Features    : Upload ảnh, Nút Phân Tích, Thẻ kết quả, Nút Chụp lại
   Constraints : Không lưu dữ liệu HS, không bắt đăng nhập, 5MB max

5. TIÊU CHÍ NGHIỆM THU (Điều kiện ĐẠT)
   [ ] Nhận diện chính xác >= 4 loài cây sân trường phổ biến
   [ ] Giao diện hiển thị tốt trên điện thoại di động (responsive)
   [ ] Trả về Không xác định khi ảnh mờ hoặc không chứa cây
   [ ] Không bị crash khi tải file > 5MB
   [ ] Footer có nhãn cảnh báo miễn trừ trách nhiệm (disclaimer)
   [ ] Đạt 4 tiêu chí UX Microsoft (Useful, Reliable, Accessible, Pleasant)
```

---

## 2.3. Kiểm Thử Ứng Dụng & Sửa Lỗi AI Fabrication

### 2.3.1. Quy Trình Kiểm Thử 5 Lớp (5-Layer Testing Framework)

| Lớp | Tên | Kịch bản kiểm thử | Kết quả mong đợi |
|---|---|---|---|
| 1 | Luồng chính (Happy Path) | Upload ảnh lá bàng rõ nét | Trả đúng 5 trường kết quả |
| 2 | Trường hợp biên (Edge Case) | Upload ảnh mờ/tối/chụp nghiêng | Hiện Độ tin cậy: Thấp + lời khuyên hỏi GV |
| 3 | Chống ảo giác AI (AI Fabrication) | Upload ảnh xe máy / mặt người | Hiện Không xác định — KHÔNG tự bịa tên cây |
| 4 | Giao diện di động (Responsive UI) | Mở trên điện thoại 375px | Tự động co giãn, bố cục không vỡ |
| 5 | An toàn & Riêng tư (Privacy) | Kiểm tra DevTools Network | Không có request lưu ảnh/dữ liệu lên server |

### 2.3.2. Sửa Lỗi Dựa Trên Phản Hồi

```
[Phát hiện lỗi] -> [Khoanh vùng bằng Annotation Mode] -> [Mô tả lỗi trong Chat Panel]
     -> [AI sửa mã nguồn] -> [Kiểm tra lại trên Live Preview] -> [Lưu Checkpoint]
```

### 2.3.3. Trạng Thái Nghiệm Thu Release Candidate

Bảng Kiểm Nghiệm Thu Sản Phẩm:

```
BANG KIEM NGHIEM THU SAN PHAM (ACCEPTANCE CHECKLIST)

[ ] 1. Chạy đúng 100% luồng chính Happy Path (5 trường kết quả)
[ ] 2. Không bị crash khi gặp file ảnh mờ hoặc file > 5MB
[ ] 3. Không bị lỗi AI Fabrication khi upload ảnh xe máy / mặt người
[ ] 4. Giao diện hiển thị chuẩn responsive trên điện thoại
[ ] 5. Có nhãn cảnh báo miễn trừ trách nhiệm ở chân trang (Footer)
[ ] 6. Đạt 4 tiêu chí UX Microsoft (Useful, Reliable, Accessible, Pleasant)
```

---

## NHỮNG ĐIỂM CỐT LÕI MODULE 2

- **Xác định bài toán sư phạm trước:** Trả lời 3 câu hỏi nền tảng trước khi viết bất cứ đặc tả nào.
- **5 thành phần Requirements là ngôn ngữ giao tiếp với AI:** Target User, Input, Output, Features, Constraints.
- **Thiết kế trước — Vibe Code sau:** Hoàn thành Data Flow + UI Wireframe + UX Microsoft trước khi gõ Master Prompt.
- **Kiểm thử 5 lớp trước khi đưa vào lớp học:** Phát hiện và sửa lỗi AI Fabrication trước khi học sinh tiếp xúc.

## SẢN PHẨM SAU MODULE 2

| Sản phẩm | Mô tả chi tiết | Kiểm tra |
|---|---|---|
| Bản tóm tắt sản phẩm (Product Brief) | 3 câu hỏi nền tảng (Ai? Vấn đề gì? AI phù hợp không?) | [ ] |
| Bản đặc tả chi tiết (Product Specification) | 5 Requirements + Scope v1 + Out of Scope + Acceptance Criteria | [ ] |
| Phác thảo giao diện (UI Wireframe) | Bản phác thảo bố cục 1 màn hình | [ ] |
| Checklist Kiểm thử 5 Lớp | Bảng ghi kết quả 5 lớp kiểm thử | [ ] |

---

## HỒ SƠ DỰ ÁN — PHẦN 1 & 2 (Mẫu điền)

*Sao chép mẫu này vào Google Doc và điền trong suốt Module 2.*

```
HỒ SƠ DỰ ÁN: [Tên Ứng Dụng]
Họ và tên GV: _____________ | Trường: _____________ | Môn: _____________

PHẦN 1: BÀI TOÁN, YÊU CẦU & ĐẶC TẢ SẢN PHẨM

A. BÀI TOÁN THỰC TẾ
   Ai gặp vấn đề?   ________________________________________________
   Vấn đề là gì?    ________________________________________________
   AI phù hợp vì?   ________________________________________________

B. YÊU CẦU SẢN PHẨM (5 Thành phần)
   1. Target User:   ________________________________________________
   2. Input:         ________________________________________________
   3. Output:        ________________________________________________
   4. Core Features: ________________________________________________
   5. Constraints:   Không __________________________________________

C. THIẾT KẾ SẢN PHẨM
   Data Flow: [Input] -> [Xử lý AI] -> [Output]
   UI Wireframe:    ________________________________________________
   UX Microsoft:
   - Useful:        ________________________________________________
   - Reliable:      ________________________________________________
   - Accessible:    ________________________________________________
   - Pleasant:      ________________________________________________

D. TIÊU CHÍ NGHIỆM THU
   [ ] ________________________________________________
   [ ] Giao diện hiển thị tốt trên điện thoại (responsive)

PHẦN 2: KIỂM THỬ & NGHIỆM THU

E. KẾT QUẢ KIỂM THỬ 5 LỚP
   Lớp 1 (Happy Path)      : [ ] ĐẠT  [ ] CHƯA ĐẠT
   Lớp 2 (Edge Case)       : [ ] ĐẠT  [ ] CHƯA ĐẠT
   Lớp 3 (AI Fabrication)  : [ ] ĐẠT  [ ] CHƯA ĐẠT
   Lớp 4 (Responsive UI)   : [ ] ĐẠT  [ ] CHƯA ĐẠT
   Lớp 5 (Privacy & Safety): [ ] ĐẠT  [ ] CHƯA ĐẠT

F. TRẠNG THÁI NGHIỆM THU
   [ ] ĐẠT Release Candidate — Sản phẩm sẵn sàng đưa vào lớp học
   [ ] Cần chạy lại — Lỗi: ________________________________________
```

---

# MODULE 3: ĐẠO ĐỨC VÀ TRÁCH NHIỆM AI

*Trong module này, các bạn sẽ tìm hiểu và vận dụng:*

- *3.1. Các Rủi Ro AI Thường Gặp Trong Giáo Dục*
- *3.2. Năm Nguyên Tắc Trí Tuệ Nhân Tạo Có Trách Nhiệm (Responsible AI)*
- *3.3. Khung Phân Tích Đạo Đức AI Cho Giáo Viên*
- *3.4. Triển Khai AI Có Trách Nhiệm Trong Lớp Học*

**Thời lượng:** 60 phút

**Mục tiêu bài học:**

- Nhận diện và phân loại 4 nhóm rủi ro AI phổ biến trong môi trường giáo dục.
- Nắm vững và vận dụng 5 nguyên tắc Responsible AI vào thiết kế ứng dụng STEM.
- Xây dựng kế hoạch triển khai AI an toàn và có đạo đức cho tiết học cụ thể.

**Sản phẩm đầu ra:** Bảng Kiểm Đạo Đức AI (Ethics Checklist) + Kế hoạch triển khai AI có trách nhiệm trong lớp học.

---

## 3.1. Các Rủi Ro AI Thường Gặp Trong Giáo Dục

### 3.1.1. Rủi Ro Thông Tin Sai Lệch (AI Hallucination & Fabrication)

AI có thể ảo giác (hallucinate) — tự bịa ra thông tin nghe có vẻ chắc chắn nhưng hoàn toàn sai sự thật.

**Ví dụ thực tế:**

- Plant ID App nhận diện sai loại cây nhưng trả về Độ tin cậy: Cao — học sinh ghi nhầm vào bài thu hoạch.
- Chatbot giải bài Toán đưa ra đáp án sai nhưng trình bày rất logic và tự tin.

**Biện pháp kiểm soát:**

- Bắt buộc ứng dụng hiển thị Confidence Level và lời khuyên Hỏi lại giáo viên.
- Thiết kế Constraints: Nếu không chắc chắn, hiển thị Không xác định thay vì đoán mò.
- Dạy học sinh tư duy phản biện: Luôn đặt câu hỏi AI có thể sai không?

### 3.1.2. Rủi Ro Quyền Riêng Tư (Privacy Risk)

Dữ liệu cá nhân học sinh có thể bị thu thập và lưu trữ mà không có sự đồng ý.

**Ví dụ thực tế:**

- Ứng dụng yêu cầu học sinh đăng nhập bằng tài khoản Google — lịch sử tra cứu bị lưu lại.
- Camera tự động lưu ảnh chụp của học sinh lên server bên thứ ba.

**Biện pháp kiểm soát:**

- Đưa Không lưu trữ dữ liệu học sinh vào Constraints bắt buộc của mọi Product Specification.
- Chạy ứng dụng trong Live Preview — dữ liệu không rời khỏi phiên làm việc.
- Kiểm tra tab Network trong DevTools để xác minh không có request gửi dữ liệu đi.

### 3.1.3. Rủi Ro Phụ Thuộc AI (AI Dependency Risk)

Học sinh và giáo viên có thể trở nên phụ thuộc quá mức vào AI, mất đi khả năng tư duy độc lập.

**Ví dụ thực tế:**

- Học sinh không cố gắng tự quan sát và mô tả đặc điểm cây vì đã có Plant ID App làm thay.
- Giáo viên ngừng cập nhật kiến thức chuyên môn vì đã có AI soạn bài.

**Biện pháp kiểm soát:**

- Thiết kế AI như trợ lý kiểm tra chứ không phải người làm thay — học sinh vẫn phải tự quan sát trước khi dùng App.
- Đặt câu hỏi tư duy sau khi học sinh nhận kết quả: Em có đồng ý với kết quả này không? Tại sao?

### 3.1.4. Rủi Ro Thiên Kiến (AI Bias Risk)

Mô hình AI được huấn luyện trên dữ liệu có thể không đại diện đầy đủ, dẫn đến kết quả thiên vị.

**Ví dụ thực tế:**

- Plant ID App nhận diện tốt cây phổ biến ở phương Tây nhưng kém chính xác với cây nhiệt đới Việt Nam.
- App đánh giá bài văn có xu hướng cho điểm cao hơn với văn phong chuẩn mực phương Tây.

**Biện pháp kiểm soát:**

- Kiểm thử ứng dụng với dữ liệu đa dạng (cây nhiệt đới, học sinh từ nhiều vùng miền).
- Thông báo cho học sinh về giới hạn: Ứng dụng có thể nhận diện tốt hơn với một số loại cây nhất định.

---

## 3.2. Năm Nguyên Tắc Trí Tuệ Nhân Tạo Có Trách Nhiệm (Responsible AI)

Các tổ chức lớn (Google, Microsoft, UNESCO) đã xây dựng nguyên tắc hướng dẫn phát triển AI có trách nhiệm. Trong giáo dục, 5 nguyên tắc này là bắt buộc:

| Nguyên tắc | Định nghĩa | Áp dụng Plant ID App |
|---|---|---|
| 1. Công bằng (Fairness) | AI phục vụ tất cả người dùng như nhau | Kiểm thử với ảnh cây từ nhiều vùng miền Việt Nam |
| 2. Minh bạch (Transparency) | AI rõ ràng về cách hoạt động và giới hạn | Hiển thị Confidence Level, ghi chú Kết quả tham khảo |
| 3. Quyền riêng tư (Privacy) | AI bảo vệ dữ liệu cá nhân người dùng | Không lưu ảnh hay dữ liệu học sinh |
| 4. Trách nhiệm giải trình (Accountability) | Phải có người chịu trách nhiệm khi AI sai | Giáo viên chịu trách nhiệm về kết quả AI cho học sinh |
| 5. An toàn (Safety) | AI không gây hại cho người dùng | Không nhận diện khuôn mặt học sinh, không nội dung độc hại |

### 3.2.1. Nguyên Tắc Công Bằng (Fairness)

*Câu hỏi kiểm tra: Ứng dụng của tôi có hoạt động tốt như nhau với tất cả học sinh trong lớp không?*

- Ứng dụng phải hoạt động đúng cho học sinh dùng điện thoại đắt tiền lẫn điện thoại bình dân.
- AI không được vô tình phân biệt đối xử dựa trên giọng nói, chính tả hay cách diễn đạt của học sinh.
- Dữ liệu huấn luyện AI phải đại diện đa dạng — không bỏ sót nhóm học sinh thiểu số hay vùng sâu vùng xa.

### 3.2.2. Nguyên Tắc Minh Bạch (Transparency)

*Câu hỏi kiểm tra: Học sinh có hiểu rõ AI đang làm gì và có thể sai ở đâu không?*

- Luôn hiển thị mức độ tin cậy (Confidence Level) của kết quả AI.
- Bắt buộc có Disclaimer: Kết quả mang tính tham khảo, hỏi lại giáo viên để xác nhận.
- Giải thích cho học sinh AI hoạt động dựa trên xác suất, không phải sự thật tuyệt đối.

### 3.2.3. Nguyên Tắc Quyền Riêng Tư (Privacy)

*Câu hỏi kiểm tra: Ứng dụng có thu thập và lưu bất kỳ dữ liệu nào của học sinh không?*

- Ứng dụng không được lưu trữ ảnh, giọng nói hay bài làm học sinh trên bất kỳ server nào mà không có sự đồng ý.
- Học sinh dưới 13 tuổi cần có sự đồng ý của phụ huynh trước khi sử dụng ứng dụng AI thu thập dữ liệu.
- Tuân thủ quy định bảo vệ dữ liệu của nhà trường và Bộ Giáo dục.

### 3.2.4. Nguyên Tắc Trách Nhiệm Giải Trình (Accountability)

*Câu hỏi kiểm tra: Nếu AI sai và học sinh ghi nhầm vào bài, ai chịu trách nhiệm?*

- Giáo viên — không phải AI — là người chịu trách nhiệm cuối cùng về chất lượng thông tin học sinh tiếp nhận.
- Mọi kết quả AI đưa ra cần được giáo viên xác minh trước khi trở thành kiến thức chính thống.
- Khi AI gây sự cố, nhà trường cần có quy trình xử lý rõ ràng.

### 3.2.5. Nguyên Tắc An Toàn (Safety)

*Câu hỏi kiểm tra: Ứng dụng AI có thể gây hại gì cho học sinh của tôi không?*

- Ứng dụng không được trả về nội dung không phù hợp lứa tuổi học sinh.
- Thiết kế Constraints nghiêm ngặt để AI chỉ hoạt động trong phạm vi bài học đã định.
- Không để AI nhận diện, lưu trữ hay xử lý hình ảnh khuôn mặt học sinh.

---

## 3.3. Khung Phân Tích Đạo Đức AI Cho Giáo Viên

Trước khi triển khai ứng dụng AI vào lớp học, giáo viên sử dụng Bảng Kiểm Đạo Đức AI:

```
BANG KIEM ĐẠO ĐỨC AI — TRƯỚC KHI TRIỂN KHAI VÀO LỚP HỌC

Tên ứng dụng: ___________________________ | Giáo viên: _________________________

NGUYÊN TẮC 1 — CÔNG BẰNG (FAIRNESS)
[ ] Ứng dụng hoạt động tốt trên cả điện thoại giá rẻ lẫn đắt tiền
[ ] Đã kiểm thử với dữ liệu đa dạng (cây nhiệt đới, học sinh nhiều vùng miền)
[ ] Không có tính năng phân biệt đối xử vô tình nào

NGUYÊN TẮC 2 — MINH BẠCH (TRANSPARENCY)
[ ] Hiển thị mức độ tin cậy (Confidence Level) của kết quả AI
[ ] Có chú thích miễn trừ trách nhiệm (Disclaimer) rõ ràng
[ ] Giáo viên đã giải thích cho học sinh về giới hạn của AI

NGUYÊN TẮC 3 — QUYỀN RIÊNG TƯ (PRIVACY)
[ ] Ứng dụng KHÔNG lưu ảnh hoặc dữ liệu cá nhân học sinh
[ ] KHÔNG yêu cầu học sinh đăng nhập bằng tài khoản cá nhân
[ ] Đã kiểm tra DevTools: không có request gửi dữ liệu lên server

NGUYÊN TẮC 4 — TRÁCH NHIỆM GIẢI TRÌNH (ACCOUNTABILITY)
[ ] Giáo viên hiểu rõ nguyên lý hoạt động cơ bản của AI trong ứng dụng
[ ] Có quy trình xử lý khi AI sai (giáo viên xác nhận lại kết quả)
[ ] Học sinh biết rằng kết quả AI cần được giáo viên xem xét

NGUYÊN TẮC 5 — AN TOÀN (SAFETY)
[ ] Ứng dụng không thể trả về nội dung không phù hợp lứa tuổi
[ ] Constraints đã được thiết kế để giới hạn phạm vi hoạt động của AI
[ ] Không có tính năng nhận diện khuôn mặt học sinh

KẾT LUẬN:
[ ] ĐẠT — Ứng dụng sẵn sàng triển khai vào lớp học
[ ] CHƯA ĐẠT — Cần chỉnh sửa trước: _________________________________________
```

---

## 3.4. Triển Khai AI Có Trách Nhiệm Trong Lớp Học

### 3.4.1. Quy Trình Triển Khai 4 Bước

```
Bước 1: KHAI BÁO
  Trước tiết học, giáo viên giải thích rõ với học sinh:
  - Đây là ứng dụng AI, không phải nguồn thông tin chính thức
  - AI có thể sai — học sinh cần tự suy nghĩ và kiểm tra lại
  - Không nhập thông tin cá nhân vào ứng dụng

Bước 2: HƯỚNG DẪN SỬ DỤNG CÓ TRÁCH NHIỆM
  - Chỉ ra rõ các trường Confidence Level (Độ tin cậy)
  - Dạy học sinh đọc Disclaimer trước khi dùng kết quả
  - Khuyến khích học sinh đặt câu hỏi AI có thể sai không?

Bước 3: GIÁM SÁT TRONG QUÁ TRÌNH THỰC HÀNH
  - Quan sát học sinh sử dụng ứng dụng
  - Can thiệp ngay khi phát hiện kết quả AI sai hoặc bất thường
  - Thu thập phản hồi của học sinh về trải nghiệm sử dụng

Bước 4: PHÂN TÍCH SAU TIẾT HỌC
  - Thảo luận: AI đã giúp được gì? AI có gì còn hạn chế?
  - Ghi nhận các trường hợp AI sai để cải tiến bản đặc tả (Spec)
  - Chia sẻ kinh nghiệm với đồng nghiệp để cùng học hỏi
```

### 3.4.2. Câu Hỏi Thảo Luận Cho Học Sinh

Sau khi học sinh sử dụng ứng dụng, giáo viên dẫn dắt thảo luận:

- Em thấy kết quả AI vừa trả về có đúng không? Em kiểm tra bằng cách nào?
- Nếu AI sai nhưng em không biết, điều gì có thể xảy ra?
- AI cần thông tin gì từ em để cho kết quả chính xác hơn?
- Nếu em là người tạo ra ứng dụng này, em sẽ thêm cảnh báo gì để học sinh không bị nhầm?

---

## NHỮNG ĐIỂM CỐT LÕI MODULE 3

- **Nhận diện 4 rủi ro AI trong giáo dục:** Thông tin sai lệch (AI Hallucination), Quyền riêng tư (Privacy), Phụ thuộc AI (Dependency) và Thiên kiến (AI Bias).
- **5 Nguyên tắc Responsible AI:** Công bằng, Minh bạch, Quyền riêng tư, Trách nhiệm giải trình và An toàn.
- **Bảng Kiểm Đạo Đức AI là cổng nghiệm thu bắt buộc:** Mọi ứng dụng AI đưa vào lớp học phải vượt qua 5 nguyên tắc này trước khi triển khai.
- **Giáo viên là người chịu trách nhiệm cuối cùng:** AI là công cụ hỗ trợ — giáo viên vẫn đảm bảo chất lượng và an toàn cho học sinh.

## SẢN PHẨM SAU MODULE 3

| Sản phẩm | Mô tả chi tiết | Kiểm tra |
|---|---|---|
| Bảng Kiểm Đạo Đức AI (Ethics Checklist) | 5 nhóm tiêu chí Responsible AI áp dụng vào ứng dụng của mình | [ ] |
| Kế hoạch triển khai có trách nhiệm | 4 bước Khai báo, Hướng dẫn, Giám sát và Phân tích sau tiết học | [ ] |
| Câu hỏi thảo luận học sinh | Ít nhất 3 câu hỏi tư duy phản biện về AI cho học sinh | [ ] |

---

# TỔNG KẾT KHÓA HỌC

Hành Trình 3 Module:

```
MODULE 1: NỀN TẢNG          MODULE 2: XÂY DỰNG & KIỂM THỬ    MODULE 3: ĐẠO ĐỨC
Google AI Studio             5 Requirements                    Responsible AI
6 Chế Độ Làm Việc  -->      Data Flow + UI Wireframe  -->     5 Nguyên Tắc
Live Demo A vs B             Master Prompt                     Triển Khai An Toàn
Quota & API Key              5-Layer Testing
```

Kết thúc khóa học này, giáo viên không chỉ biết dùng AI — mà đã trở thành Kỹ sư Trưởng Sư Phạm (Pedagogical Lead Engineer) với 4 năng lực:

1. **Nhìn thấy bài toán** thực tế của học sinh mà công nghệ có thể giải quyết.
2. **Thiết kế giải pháp** bằng ngôn ngữ tự nhiên thay vì mã lệnh thủ công.
3. **Kiểm thử và nghiệm thu** sản phẩm AI trước khi đưa vào lớp học.
4. **Triển khai có trách nhiệm** theo 5 nguyên tắc Responsible AI để bảo vệ học sinh.

---

*Phát Triển Ứng Dụng Với AI — Mã học phần AIApp-M2.1*
*Bản Draft 3 — Ngày soạn: 08/2026*
