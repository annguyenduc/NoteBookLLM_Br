# Khóa Học: Phát Triển Ứng Dụng Với AI

> **Dành cho:** Giáo viên STEM / Giáo viên muốn dạy AI ứng dụng
> **Mục tiêu cốt lõi:** Không dạy công cụ — dạy **tư duy phát triển sản phẩm AI**
> **Phiên bản:** 1.0 — Draft thiết kế khóa học
> **Ngày:** 2026-07-21

---

## Triết Lý Thiết Kế Khóa Học

Hầu hết khóa học AI dạy theo thứ tự: **Công cụ → Tính năng → Bài tập**.

Khóa học này dạy theo thứ tự: **Bài toán → Tư duy → Công cụ**.

Học viên ra khỏi lớp không chỉ biết dùng AI Studio — mà biết **tại sao dùng** và **khi nào dùng** nó trong một quy trình phát triển thực sự.

### Vòng Lặp Cốt Lõi (PSPTI Loop)

```
Problem (Bài toán thực tế)
    ↓
Spec (Đặc tả yêu cầu)
    ↓
Plan (Lập kế hoạch kiến trúc)
    ↓
Prototype (Làm nguyên mẫu bằng AI Studio + Vibe Coding)
    ↓
Test (Kiểm thử bằng Checklist)
    ↓
Iterate (Cải tiến theo phản hồi)
```

### So Sánh Tư Duy

| Dạy theo kiểu CŨ | Dạy theo PSPTI |
|---|---|
| Hôm nay học AI Studio | Học qua bài toán thực tế |
| Mai học API | Công cụ xuất hiện đúng lúc cần |
| Mốt học HTML | Học viên hiểu "tại sao" dùng tool đó |
| Kỹ năng gắn với tool | Kỹ năng chuyển được sang mọi nền tảng |

---

## Cấu Trúc Khóa Học

### Tổng Quan

| Thông tin | Chi tiết |
|---|---|
| Tên khóa | Phát Triển Ứng Dụng Với AI |
| Đối tượng | Giáo viên STEM, cấp THCS–THPT |
| Thời lượng | 8 buổi × 2 tiết (hoặc 4 ngày intensif) |
| Hình thức | Thực hành project-based, mỗi module 1 mini-app |
| Đầu ra | Mỗi học viên có ≥ 1 mini-app AI hoàn chỉnh |

---

## Module 0: Khai Mạc — "Tại Sao AI Cần Quy Trình?"

**Mục tiêu:** Xây dựng tư duy. Không viết code.

**Hoạt động:**
- Thảo luận: Bạn đã từng thất bại với một ý tưởng vì không có kế hoạch chưa?
- Demo: Xem 2 cách làm cùng 1 app (vibe coding bừa vs. PSPTI)
- Giới thiệu vòng lặp **PSPTI** và lý do nó hoạt động

**Câu hỏi kết buổi:**
> Bài toán giảng dạy nào khiến bạn cảm thấy "ước gì có AI làm giúp việc này"?

---

## Module 1: SPEC — Đặc Tả Yêu Cầu (Nói Rõ Trước Khi Làm)

**Mục tiêu:** Học viên viết được Spec 1 trang cho bất kỳ ý tưởng AI nào.

### Lý Thuyết (30 phút)

**Spec là gì?**
Spec (Specification) = tài liệu mô tả rõ ràng **bài toán cần giải** và **tiêu chí thành công**, trước khi viết bất kỳ dòng code nào.

**Template Spec (1 trang A4):**

```
TÊN DỰ ÁN: ____________________

BÀI TOÁN:
- Người dùng là ai?
- Họ đang gặp vấn đề gì?
- Vấn đề này xảy ra khi nào / ở đâu?

INPUT (Đầu vào):
- Người dùng cung cấp gì? (ảnh / văn bản / giọng nói / ...)

OUTPUT (Đầu ra):
- Hệ thống trả về gì? (tên / số liệu / mô tả / ...)

TIÊU CHÍ THÀNH CÔNG:
- Khi nào thì bài toán được coi là giải xong?
- Làm sao biết AI đang trả lời đúng?

GIỚI HẠN (Out of scope):
- Tính năng nào KHÔNG làm ở phiên bản 1?
```

### Thực Hành (60 phút)

**Ví dụ demo — App nhận diện cây:**

```
TÊN DỰ ÁN: Plant Identifier

BÀI TOÁN:
- Người dùng: Học sinh THCS, đang học sinh vật
- Vấn đề: Không biết tên cây khi đi thực địa
- Khi nào: Giờ thực hành ngoài trời, không có sách

INPUT:
- Ảnh lá cây hoặc toàn cây (chụp bằng điện thoại)

OUTPUT:
- Tên cây (tiếng Việt + tên khoa học)
- Họ thực vật
- Mô tả ngắn (2-3 câu)
- Độ tin cậy (cao / trung bình / thấp)

TIÊU CHÍ THÀNH CÔNG:
- Nhận diện đúng ≥ 70% ảnh cây phổ biến ở Việt Nam
- Kết quả hiển thị trong < 5 giây
- Học sinh lớp 6 đọc hiểu được kết quả

NGOÀI PHẠM VI (v1):
- Không lưu lịch sử
- Không cần đăng nhập
- Không nhận diện cây độc hại / cây thuốc đặc biệt
```

**Bài tập thực hành:**
Học viên tự chọn 1 bài toán từ công việc giảng dạy thực tế → viết Spec.

**Checklist Spec hợp lệ:**
- [ ] Đã xác định đúng người dùng cuối?
- [ ] Input và output cụ thể, không mơ hồ?
- [ ] Tiêu chí thành công đo lường được?
- [ ] Đã liệt kê những gì KHÔNG làm?

---

## Module 2: AI CÓ GIẢI ĐƯỢC KHÔNG? — Phân Tích Khả Thi

**Mục tiêu:** Học viên biết AI phù hợp với loại bài toán nào, tránh xây app không khả thi.

### Lý Thuyết (30 phút)

**AI làm được tốt:**
- Phân loại hình ảnh (ảnh → nhãn)
- Tóm tắt văn bản dài
- Trả lời câu hỏi từ tài liệu
- Tạo nội dung sáng tạo (câu hỏi, bài tập, ví dụ)
- Dịch thuật, giải thích khái niệm

**AI làm không tốt (hoặc không nên dùng):**
- Tính toán số học phức tạp (cần code / máy tính)
- Dữ liệu thời gian thực (giá cổ phiếu, thời tiết hiện tại)
- Thông tin cá nhân học sinh (privacy)
- Quyết định pháp lý / y tế quan trọng

**Ma trận quyết định:**

| Bài toán | Dùng AI? | Lý do |
|---|---|---|
| Nhận diện ảnh | ✅ Rất phù hợp | Vision AI mạnh |
| Tóm tắt tài liệu | ✅ Rất phù hợp | LLM giỏi tổng hợp |
| Tính điểm thi | ⚠️ Cẩn thận | Cần chính xác tuyệt đối |
| Tư vấn tâm lý học sinh | ❌ Không nên | Cần con người |
| Dữ liệu học sinh cá nhân | ❌ Không nên | Vấn đề privacy |

### Thực Hành (60 phút)
Học viên lấy Spec từ Module 1 → chạy qua ma trận → quyết định "Đây có phải bài toán AI giải được không?"

---

## Module 3: PLAN — Kiến Trúc Hệ Thống

**Mục tiêu:** Học viên vẽ được "luồng dữ liệu" của app trước khi code.

### Lý Thuyết (30 phút)

**Plan là gì?**
Plan = sơ đồ kiến trúc mô tả dữ liệu chạy từ đâu → đi qua gì → ra đâu.

**Template Plan (sơ đồ):**

```
[INPUT]
    ↓
[XỬ LÝ TRƯỚC] (nếu cần: resize ảnh, clean text...)
    ↓
[AI MODEL] (Gemini / Vision / API nào?)
    ↓
[PROMPT] (câu lệnh hướng dẫn AI)
    ↓
[XỬ LÝ SAU] (format kết quả, lọc, dịch...)
    ↓
[OUTPUT HIỂN THỊ]
```

**Ví dụ — Plant Identifier:**

```
[Ảnh lá cây từ người dùng]
    ↓
[Upload file ảnh]
    ↓
[Gemini Vision API]
    ↓
[Prompt: "Nhận diện loài cây trong ảnh.
  Trả về: tên tiếng Việt, tên khoa học,
  họ thực vật, mô tả 2 câu, độ tin cậy.
  Format: JSON."]
    ↓
[Parse JSON kết quả]
    ↓
[Hiển thị card kết quả trên HTML]
```

**Cần quyết định trong Plan:**
1. Dùng model AI nào? (Gemini Flash / Pro / Vision)
2. Prompt strategy: zero-shot hay few-shot?
3. Output format: JSON / plain text / markdown?
4. Giao diện: HTML đơn giản / web app?

### Thực Hành (60 phút)
Học viên vẽ Plan cho app của mình (dùng giấy hoặc draw.io).

---

## Module 4: AI STUDIO — Thử Nghiệm Prompt

**Mục tiêu:** Học viên dùng AI Studio để viết và cải thiện prompt trước khi code.

### Lý Thuyết (20 phút)

**Nguyên tắc viết Prompt tốt:**

```
[ROLE] Bạn là chuyên gia sinh vật học...
[TASK] Hãy nhận diện loài cây trong ảnh...
[FORMAT] Trả về JSON với các trường: name, scientific_name...
[CONSTRAINTS] Nếu không chắc, hãy nói rõ độ tin cậy thấp...
[EXAMPLES] (few-shot nếu cần)
```

**Vòng lặp cải thiện Prompt:**
```
Viết prompt v1
    ↓
Test với 5 ví dụ khác nhau
    ↓
Ghi nhận kết quả sai / thiếu
    ↓
Điều chỉnh prompt
    ↓
Test lại
```

### Thực Hành (70 phút)

**Phần 1 — Demo live (20 phút):**
Giáo viên demo trực tiếp trên AI Studio:
- Nhập prompt v1
- Test với ảnh dễ → ảnh khó → ảnh mờ
- Xem kết quả sai → phân tích tại sao → sửa prompt

**Phần 2 — Học viên tự làm (50 phút):**
- Mở AI Studio với Spec + Plan đã viết
- Viết prompt v1 → test → ghi log → cải thiện ≥ 3 vòng

**Prompt Testing Log:**

| Version | Thay đổi | Test case | Kết quả | Quyết định |
|---|---|---|---|---|
| v1 | Prompt cơ bản | Ảnh rõ | Đúng 4/5 | Cần cải thiện |
| v2 | Thêm few-shot | Ảnh mờ | Đúng 3/5 | Tiếp tục |
| v3 | Thêm format JSON | Ảnh góc lạ | Đúng 4/5 | Chốt dùng |

---

## Module 5: PROTOTYPE — Vibe Coding Tạo Mini App

**Mục tiêu:** Học viên tạo được app HTML chạy được từ prompt đã chốt.

### Lý Thuyết (20 phút)

**Vibe Coding là gì?**
Vibe Coding = dùng AI để viết code thay vì tự viết từng dòng.
Học viên mô tả → AI sinh code → học viên kiểm tra → chỉnh sửa.

**Quy trình Vibe Coding:**
```
[Spec + Plan + Prompt đã chốt]
    ↓
[Yêu cầu AI tạo HTML/JS]
    ↓
[Mở file, chạy thử]
    ↓
[Phát hiện lỗi / thiếu]
    ↓
[Yêu cầu AI sửa]
    ↓
[Lặp lại cho đến khi Checklist xanh hết]
```

**Prompt tạo app mẫu:**
```
Tạo cho tôi một file HTML đơn giản, single-page, không cần server:
- Cho phép upload ảnh
- Gọi Gemini Vision API với key: [API_KEY]
- Dùng prompt sau: [PROMPT ĐÃ CHỐT]
- Hiển thị kết quả dạng card với: tên cây, tên khoa học, mô tả
- Style đơn giản, dùng màu xanh lá
- Không dùng framework, chỉ HTML + CSS + JS thuần
```

### Thực Hành (70 phút)

**Phần 1 — Demo tạo app (20 phút):**
Giáo viên demo: từ prompt → ra file HTML → chạy trên browser.

**Phần 2 — Học viên tự tạo (50 phút):**
Mỗi học viên dùng AI để tạo mini app từ Spec + Plan + Prompt của mình.

**Deliverable của Module 5:**
- File `index.html` chạy được trên browser
- Kết nối được Gemini API
- Có giao diện cơ bản cho input → output

---

## Module 6: TEST — Kiểm Thử Bằng Checklist

**Mục tiêu:** Học viên biết cách test app AI một cách có hệ thống.

### Lý Thuyết (20 phút)

**Tại sao AI app cần test khác code thông thường?**
- AI có thể "tự tin sai" (hallucination)
- Kết quả phụ thuộc vào chất lượng input
- Cần test cả happy path lẫn edge cases

**Template Checklist Test:**

```
HAPPY PATH (Input chuẩn):
- [ ] Upload ảnh rõ nét → kết quả đúng?
- [ ] Text tiếng Việt đủ dấu → kết quả đúng?
- [ ] Kết quả hiển thị trong < X giây?

EDGE CASES (Input bất thường):
- [ ] Ảnh mờ → xử lý như thế nào?
- [ ] Ảnh không phải đối tượng cần nhận diện → báo lỗi?
- [ ] File quá lớn → có thông báo?
- [ ] Không có mạng → app crash hay báo lỗi đẹp?

AI BEHAVIOR:
- [ ] Khi không chắc, AI có nói "không biết" không?
- [ ] Kết quả có nhất quán qua nhiều lần test không?
- [ ] Output format có đúng như mong đợi không?

UX:
- [ ] Học sinh lớp 6 dùng được mà không cần hướng dẫn?
- [ ] Có thông báo loading khi đang xử lý?
- [ ] Kết quả dễ đọc, không bị vỡ layout?
```

### Thực Hành (70 phút)
Học viên chạy checklist với app của mình → ghi nhận lỗi → ưu tiên sửa.

**Bug Tracking Log:**

| Lỗi | Mức độ | Nguyên nhân | Cách sửa |
|---|---|---|---|
| Ảnh PNG không load được | Critical | Chưa handle PNG | Sửa code upload |
| Kết quả hiển thị chậm | Medium | Không có loading spinner | Thêm UI feedback |
| Tên cây tiếng Anh thay vì Việt | Low | Prompt chưa chỉ định ngôn ngữ | Thêm vào prompt |

---

## Module 7: ITERATE — Cải Tiến Theo Phản Hồi

**Mục tiêu:** Học viên lập kế hoạch phát triển phiên bản 2 dựa trên feedback thực tế.

### Lý Thuyết (20 phút)

**Vòng lặp Iterate:**
```
[Thu thập feedback từ người dùng thật]
    ↓
[Phân loại: Bug / Feature request / UX issue]
    ↓
[Ưu tiên theo impact × effort]
    ↓
[Chọn 3-5 cải tiến cho v2]
    ↓
[Viết Spec bổ sung cho v2]
    ↓
[Lặp lại PSPTI]
```

**Ma trận ưu tiên (Impact × Effort):**

|  | Effort Thấp | Effort Cao |
|---|---|---|
| Impact Cao | ⭐ Làm ngay | 📋 Lên kế hoạch |
| Impact Thấp | 🔄 Nếu có thời gian | ❌ Bỏ qua |

### Thực Hành (70 phút)

**Phần 1 — User Testing nội bộ (30 phút):**
Học viên hoán đổi app cho nhau → người dùng thật là học viên khác → thu feedback.

**Phần 2 — Lập roadmap v2 (40 phút):**
Dựa trên feedback → viết Spec bổ sung cho phiên bản 2.

**Ví dụ roadmap Plant Identifier:**

```
Phiên bản 1 (đã xong):
- Nhận diện cây từ ảnh
- Hiển thị tên + mô tả

Phiên bản 2 (dựa trên feedback):
- Lưu lịch sử 10 cây gần nhất (localStorage)
- Xuất kết quả thành PDF
- Thêm nút "Tìm thêm thông tin" → link Wikipedia

Phiên bản 3 (tương lai):
- Nhận diện offline (model nhỏ)
- Giọng nói đọc kết quả
- Chia sẻ lên lớp học
```

---

## Module 8: SHOWCASE — Trình Bày & Phản Tư

**Mục tiêu:** Củng cố tư duy, xây dựng thói quen trình bày như kỹ sư.

### Hoạt Động (90 phút)

**Phần 1 — Demo Day (60 phút):**
Mỗi học viên demo app trong 5 phút theo cấu trúc:

```
1. Bài toán: "Học sinh của tôi gặp khó khăn khi..."
2. Spec: "Tôi đặc tả app như sau..."
3. Plan: "Kiến trúc là..."
4. Prototype: [Demo live]
5. Kết quả test: "Checklist đạt X/Y"
6. Bài học: "Điều tôi học được từ quy trình PSPTI..."
7. Roadmap: "Phiên bản 2 sẽ có..."
```

**Phần 2 — Retrospective (30 phút):**

Câu hỏi phản tư:
- Bước nào trong PSPTI tốn thời gian nhất?
- Nếu làm lại, bạn sẽ thay đổi gì ở Spec?
- Prompt nào hiệu quả nhất? Tại sao?
- Bạn sẽ dạy quy trình này cho học sinh của mình như thế nào?

---

## Phụ Lục A: Ví Dụ Dự Án Phù Hợp Với Giáo Viên STEM

| Bài toán | App | Công nghệ | Độ phức tạp |
|---|---|---|---|
| Chấm bài luận nhanh | AI Grading Assistant | Gemini Text | ⭐⭐ |
| Giải thích khái niệm khó | Concept Explainer | Gemini + Prompt | ⭐⭐ |
| Nhận diện cây / động vật | Plant/Animal ID | Gemini Vision | ⭐⭐ |
| Tạo câu hỏi ôn tập | Quiz Generator | Gemini Text | ⭐⭐ |
| Dịch và tóm tắt tài liệu | Doc Summarizer | Gemini Text | ⭐ |
| Nhận diện lỗi toán học từ ảnh | Math Error Detector | Gemini Vision | ⭐⭐⭐ |
| Phân loại câu hỏi theo bloom | Bloom Classifier | Gemini Text | ⭐⭐⭐ |
| Tạo câu chuyện từ ảnh | Story from Photo | Gemini Vision | ⭐⭐ |

---

## Phụ Lục B: Chuyển Hóa Cho Học Sinh

Khi giáo viên dạy lại học sinh, có thể đơn giản hóa PSPTI thành:

**"5 bước của một kỹ sư AI nhí":**

```
1. TÔI MUỐN LÀM GÌ? → Viết 3 câu mô tả bài toán
2. AI CÓ GIÚP ĐƯỢC KHÔNG? → Trả lời có/không + lý do
3. APP CỦA TÔI TRÔNG NHƯ THẾ NÀO? → Vẽ sơ đồ trên giấy
4. LÀM THỬ! → Dùng AI Studio + Vibe Coding
5. APP CÓ CHẠY ĐÚNG KHÔNG? → Checklist 5 câu hỏi
```

**Template Spec đơn giản cho học sinh (1/2 trang A4):**

```
App của tôi tên là: ____________________

Nó giúp: ______________________ (1 câu)

Người dùng đưa vào: __________________ (ảnh / văn bản / ...)

App trả về: _____________________ (kết quả gì?)

Tôi biết app đúng khi: _________________ (tiêu chí cụ thể)
```

---

## Phụ Lục C: Tài Nguyên Đề Xuất

| Công cụ | Mục đích | Link |
|---|---|---|
| Google AI Studio | Test prompt, lấy API key | aistudio.google.com |
| Gemini API Docs | Tham khảo API | ai.google.dev |
| draw.io | Vẽ sơ đồ Plan | app.diagrams.net |
| CodePen / JSFiddle | Test HTML nhỏ | codepen.io |
| Google Colab | Notebook Python | colab.research.google.com |

---

## Tóm Tắt — Điểm Khác Biệt Của Khóa Học Này

> **Khóa học này không dạy AI Studio. Khóa học này dạy tư duy phát triển sản phẩm AI — và AI Studio chỉ là một công cụ trong quy trình đó.**

Học viên ra về với:
1. ✅ **Tư duy**: Biết đặt câu hỏi đúng trước khi code
2. ✅ **Quy trình**: PSPTI áp dụng được cho bất kỳ bài toán AI nào
3. ✅ **Sản phẩm**: ≥ 1 mini app AI chạy thực trên browser
4. ✅ **Kỹ năng chuyển đổi**: Quy trình này dùng được trên Cursor, Claude, ChatGPT, hay bất kỳ AI tool nào trong tương lai

---

*Tài liệu này là bản thiết kế để thảo luận, không phải tài liệu giảng dạy cuối cùng.*
*Phiên bản tiếp theo sẽ bao gồm: slide bài giảng, video demo, bài tập từng module.*
