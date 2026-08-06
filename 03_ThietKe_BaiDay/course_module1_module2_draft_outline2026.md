# **TÀI LIỆU KHÓA HỌC: PHÁT TRIỂN ỨNG DỤNG VỚI AI**
### **Mã học phần: AIApp-M2.1 | Bản Draft Hợp Nhất Module 1 & Module 2**

---

# **MODULE 1: NỀN TẢNG GOOGLE AI STUDIO**

*Trong module này, các bạn sẽ làm chủ 3 nội dung cốt lõi về công cụ và trải nghiệm Live Demo:*

- *1.1. Xu hướng Vibe Coding (Lập trình bằng ngôn ngữ tự nhiên)*
- *1.2. Hướng dẫn sử dụng Google AI Studio (Trải nghiệm Live Demo 6 chế độ làm việc)*
- *1.3. Giới hạn về tài khoản (Hạn ngạch Quota, Troubleshooting & An toàn API Key)*

---

> **⏱ Thời lượng:** 90 phút (25 phút Lý thuyết & Case study + 45 phút Trải nghiệm Live Demo Studio + 20 phút Cẩm nang Sự cố & API Key)  
> **🎯 Mục tiêu bài học:**  
> - Hiểu rõ bản chất xu hướng Vibe Coding và sự dịch chuyển từ lập trình viên sang vai trò Kỹ sư Trưởng (Lead Engineer) sư phạm.  
> - Trực tiếp thao tác trên Live Demo ứng dụng Nhận diện cây (Plant ID App) để thành thạo 6 chế độ làm việc của Google AI Studio (Build Mode, Live Preview, Annotation Mode ✏️ với bút vẽ sửa UI...).  
> - Làm chủ thông số hạn ngạch tài khoản miễn phí (RPM 15, RPD 1.000), xử lý 4 sự cố kỹ thuật thường gặp và bảo mật Khóa kết nối ứng dụng (API Key).  
> **📦 Sản phẩm đầu ra:** Khởi tạo tài khoản Google AI Studio + Tạo Khóa API Key an toàn + Trải nghiệm Live Demo 6 chế độ và nghiệm thu Bảng kiểm kỹ năng Module 1.

---

## **1. Nền Tảng Google AI Studio**

### 1.1. Xu hướng Vibe Coding (Lập Trình Bằng Ngôn Ngữ Tự Nhiên)

#### 1.1.1. Sự Dịch Chuyển Lịch Sử Của Ngôn Ngữ Lập Trình

Trong 70 năm qua, ngành khoa học máy tính đã trải qua 3 làn sóng dịch chuyển về ngôn ngữ giao tiếp giữa con người và máy tính:

1. **Thế hệ 1 (Mã máy & Hợp ngữ - Assembly/Machine Code):** Con người phải giao tiếp với máy tính bằng các chuỗi số nhị phân `0` và `1` hoặc các câu lệnh phần cứng phức tạp — cực kỳ khó học và chỉ dành riêng cho các kỹ sư điện tử/phần cứng chuyên sâu.
2. **Thế hệ 2 (Ngôn ngữ bậc cao - C++, Java, Python):** Con người viết mã lệnh dựa trên cú pháp logic nghiêm ngặt — đòi hỏi phải học lập trình bài bản nhiều năm, chỉ cần thiếu 1 dấu chấm phẩy `;` cũng khiến ứng dụng sập (crash).
3. **Thế hệ 3 (Vibe Coding - Ngôn ngữ tự nhiên):** Con người dùng chính **tiếng Việt hoặc tiếng Anh giao tiếp hàng ngày** để mô tả mong muốn — mô hình Trí tuệ nhân tạo (AI - Artificial Intelligence) sẽ tự động biên dịch và sinh ra toàn bộ mã nguồn.

> **Khái niệm Vibe Coding:** Do Andrej Karpathy — cựu Giám đốc AI của Tesla và đồng sáng lập OpenAI — chính thức định danh năm 2025. Vibe Coding (Lập trình theo cảm hứng/mô tả tự nhiên) là phương pháp xây dựng phần mềm mà ở đó bạn *chỉ cần mô tả ý định và cảm nhận về sản phẩm*, mô hình ngôn ngữ lớn (LLM - Large Language Model) sẽ đảm nhận 100% việc viết mã lệnh (code HTML, CSS, JavaScript).

> *"Just vibe with the AI. Forget that the code even exists."*  
> *(Hãy cứ tương tác tự nhiên với AI. Hãy quên đi sự tồn tại của mã lệnh.)* — Andrej Karpathy

#### 1.1.2. Tại Sao Giáo Viên STEM Cần Nắm Bắt Vibe Coding?

Trước đây, rào cản lớn nhất ngăn cản giáo viên tạo ra các phần mềm dạy học riêng là **kỹ năng lập trình thủ công**. Quy trình cũ thường kéo dài và tốn kém:

```
[Ý tưởng sư phạm của GV] ➔ [Thuê Lập trình viên] ➔ [Chờ 3-6 tháng phát triển] ➔ [Sản phẩm sai ý đồ]
```

Với **Vibe Coding trên Google AI Studio**, khoảng cách này hoàn toàn bị xóa bỏ:

```
[Ý tưởng sư phạm của GV] ➔ [Mô tả bằng tiếng Việt] ➔ [AI Studio tạo App chạy thật trong 3 phút]
```

Giáo viên — người am hiểu nhất nhu cầu của học sinh và phương pháp dạy học môn STEM — nay có thể **trực tiếp đóng vai trò Kỹ sư Trưởng (Lead Engineer)** để tự sản xuất ứng dụng Web (Web App) phục vụ đúng bài học của mình.

#### 1.1.3. Hai Mặt Của Vibe Coding: Ngẫu Nhiên vs. Có Bản Đặc Tả (Spec-First)

Vibe Coding mang lại tốc độ vượt trội, nhưng cũng ẩn chứa rủi ro nếu người dùng ra lệnh thiếu định hướng:

* **Vibe Coding ngẫu nhiên (Demo A):** Khi bạn gõ câu lệnh ngắn mơ hồ (*"Tạo cho tôi app nhận diện cây"*), AI sẽ tự suy đoán và tạo ra ứng dụng dư thừa tính năng (như cẩm nang tưới nước, phân bón, đồ thị tăng trưởng...) — hoàn toàn không dùng được cho tiết học thực địa Sinh học ngoài sân trường.
* **Spec-First Vibe Coding (Demo B):** Giáo viên chuẩn bị bản đặc tả sản phẩm (Product Specification) gồm 5 thành phần cốt lõi trước khi ra lệnh $\rightarrow$ AI Studio sẽ tạo ra đúng 1 màn hình tinh gọn, tập trung hiển thị đúng các trường thông tin bài học chuẩn xác.

---

### 1.2. Hướng dẫn sử dụng Google AI Studio (Trải Nghiệm Live Demo Studio)

Google AI Studio (Nền tảng phát triển ứng dụng AI của Google tại địa chỉ `aistudio.google.com`) là một môi trường nguyên mẫu nhanh (rapid prototyping environment) cho phép giáo viên biến ý tưởng thành phần mềm mà không cần cài đặt bất kỳ công cụ lập trình nào trên máy tính.

#### 1.2.1. Cấu Trúc 6 Chế Độ Làm Việc Cốt Lõi

Khi truy cập vào Google AI Studio, giáo viên cần làm chủ 6 thành phần giao diện chính qua ví dụ Live Demo ứng dụng Nhận diện cây (Plant ID App):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            GOOGLE AI STUDIO                                 │
├──────────────────────┬──────────────────────────────┬───────────────────────┤
│ 1. SYSTEM            │ 2. CHAT / PROMPT PANEL       │ 5. LIVE PREVIEW       │
│    INSTRUCTIONS      │    (Khung gõ câu lệnh)        │    (Màn hình ứng dụng │
│   (Thiết lập vai trò)│                              │     thật chạy trực    │
├──────────────────────┼──────────────────────────────┤     tiếp)             │
│ 3. MODEL SELECTION   │ 4. BUILD MODE BUTTON         │                       │
│   (Chọn Gemini 2.0)  │    (Nút kích hoạt sinh App)  ├───────────────────────┤
│                      │                              │ 6. ANNOTATION MODE ✏️ │
│                      │                              │    (Bút vẽ sửa UI)    │
└──────────────────────────────────────────────────────┴───────────────────────┘
```

##### 1. Câu lệnh hệ thống (System Instructions)
* Nơi thiết lập "nhân cách" và ngữ cảnh cho AI.
* *Ví dụ:* *"Bạn là Chuyên gia Phát triển Web và Giáo viên STEM chuyên nghiệp. Hãy tạo ứng dụng nhận diện cây phục vụ học sinh THCS"*.

##### 2. Khung nhập câu lệnh (Chat / Prompt Panel)
* Nơi giáo viên gõ câu lệnh Master Prompt chứa bản đặc tả sản phẩm.

##### 3. Lựa chọn mô hình (Model Selection)
* **Gemini 1.5 Flash:** Tốc độ phản hồi cực nhanh, phù hợp cho bài toán xử lý văn bản đơn giản.
* **Gemini 1.5 Pro:** Tư duy logic sâu, phù hợp cho phân tích dữ liệu phức tạp.
* **Gemini 2.0 Flash / Multimodal:** Hỗ trợ thị giác máy tính (Vision), nhận diện ảnh và video thời gian thực.

##### 4. Chế độ xây dựng ứng dụng (Build Mode)
* Nút tính năng quan trọng nhất — khi bật chế độ này, AI sẽ không trả lời dạng đoạn chat thông thường mà sẽ tự động viết mã nguồn HTML/JS/CSS để tạo ra một ứng dụng hoàn chỉnh.

##### 5. Màn hình xem trước trực tiếp (Live Preview)
* Nằm ở nửa phải màn hình, cho phép giáo viên bấm trải nghiệm ứng dụng Plant ID chạy thật ngay lập tức.

##### 6. Công cụ bút vẽ phản hồi (Annotation Mode ✏️)
* Cho phép giáo viên dùng chuột khoanh tròn trực tiếp lên các phần tử trên giao diện Live Preview của Plant ID App và gõ ghi chú.
* *Ví dụ:* Khoanh tròn vào tiêu đề ➔ gõ ghi chú *"Đổi nút này sang màu xanh lá"*, *"Thu nhỏ font chữ tiêu đề"*. AI sẽ tự đọc hình vẽ và điều chỉnh giao diện theo đúng ý bạn.

---

#### 1.2.2. Quy Trình 3 Bước Trải Nghiệm Live Demo (So Sánh Trực Quan Demo A vs. Demo B)

Để thấy rõ sự khác biệt giữa hai phương pháp lập trình bằng AI, giáo viên thực hành quy trình 3 bước trải nghiệm trực tiếp 2 kịch bản Live Demo trên Google AI Studio:

```
[Bước 1: Đăng nhập]     Truy cập aistudio.google.com ➔ Bấm "Create New Prompt" ➔ Chọn Gemini 2.0 Flash.
           ↓
[Bước 2: Nạp Prompt]    Kích hoạt chế độ Build Mode ➔ Nạp Prompt thử nghiệm (Demo A hoặc Demo B).
           ↓
[Bước 3: Thử Live Demo] Trải nghiệm trên Live Preview ➔ Dùng bút Annotation Mode ✏️ khoanh vùng sửa UI.
```

##### 🔴 KỊCH BẢN LIVE DEMO A — VIBE CODING NGẪU NHIÊN (CẢM TÍNH)
* **Câu lệnh nạp (Prompt A):** `"Tạo cho tôi một ứng dụng nhận diện cây trồng"` *(không có bản đặc tả sản phẩm)*.
* **Kết quả AI sinh ra trên Live Preview:** AI tự suy đoán ý định và tạo ra một ứng dụng quá tải tính năng: cẩm nang hướng dẫn tưới nước, lịch bón phân, đồ thị theo dõi tăng trưởng, diễn đàn chia sẻ...
* **Đánh giá rủi ro sư phạm:** Giao diện bị vỡ hình trên di động, quá nhiều nút bấm rối mắt ngoài trời nắng, học sinh bị xao nhãng và không thể hoàn thành bài thu hoạch Sinh học thực địa.

##### 🟢 KỊCH BẢN LIVE DEMO B — SPEC-FIRST VIBE CODING (CÓ BẢN ĐẶC TẢ PLANT ID APP)
* **Câu lệnh nạp (Prompt B):** Nạp câu lệnh Master Prompt chứa bản đặc tả 5 thành phần (Target User học sinh lớp 6, Input ảnh lá cây < 5MB, Output 5 trường thông tin chuẩn, Core Features, Constraints không đăng nhập/không lưu ảnh).
* **Kết quả AI sinh ra trên Live Preview:** AI Studio Build Mode tạo ra đúng **1 màn hình thẻ tinh gọn (Single-page Card Layout)** với Header xanh lá cây mộc mạc, khung tải ảnh lớn ở trung tâm và thẻ hiển thị 5 trường kết quả rõ ràng.
* **Thao tác chỉnh sửa bằng Annotation Mode ✏️:** Giáo viên dùng chuột khoanh tròn nút *"Chụp lại"*, gõ ghi chú *"Đổi nút này sang màu xanh lá đậm và phóng to font chữ"* ➔ AI tự đọc hình vẽ và điều chỉnh giao diện chuẩn xác ngay lập tức!

---

* **★ Thử thách 1 (Hands-on Live Demo Challenge):** Thực hành mở Google AI Studio, chọn mô hình Gemini 2.0 Flash, gõ câu lệnh trải nghiệm Plant ID App, bật chế độ Build Mode và dùng bút vẽ Annotation Mode ✏️ chỉnh sửa 1 chi tiết giao diện trên Live Preview (Thời lượng thực hành: 15 phút).

---

### 1.3. Giới hạn về tài khoản (Quota, Troubleshooting & API Key Security)

Để vận hành bài dạy ổn định và không bị gián đoạn khi học sinh thực hành, giáo viên cần nắm rõ các thông số kỹ thuật và cẩm nang xử lý sự cố trên tài khoản miễn phí (Free Tier).

#### 1.3.1. Bảng Thông Số Hạn Ngạch Sử Dụng (Quota Table)

| Thông số kỹ thuật | Giới hạn tài khoản Miễn phí | Giải thích sư phạm & Cách quản lý trong lớp học |
|---|---|---|
| **Lượt gọi theo phút (RPM - Requests Per Minute)** | **15 lượt / phút** | Tối đa 15 lần gửi yêu cầu phân tích/phút. **Hướng dẫn HS:** Không nhấp nút "Phân Tích" hoặc "Gửi" liên tục nhiều lần. |
| **Lượt gọi theo ngày (RPD - Requests Per Day)** | **1.000 lượt / ngày** | Tối đa 1.000 lượt phân tích/ngày. Đủ cho 1-2 lớp học thực hành thoải mái trong ngày. |
| **Dung lượng ảnh đầu vào (Input File Size)** | **Tối đa 5MB / ảnh** | Không tải ảnh gốc quá lớn từ camera điện thoại sắc nét. **Cách xử lý:** Thêm chức năng tự động nén ảnh vào bản đặc tả Spec. |
| **Giới hạn đầu ra (Output Token Limit)** | **8.192 tokens / lần** | Đảm bảo mã nguồn ứng dụng sinh ra không bị ngắt giữa chừng. |

#### 1.3.2. Cẩm Nang Xử Lý 4 Sự Cố Kỹ Thuật Thường Gặp (Troubleshooting Guide)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│               CẨM NANG XỬ LÝ SỰ CỐ TRONG LỚP HỌC (TROUBLESHOOTING)          │
├───────────────────────────────────────┬─────────────────────────────────────┤
│ 1. Lỗi '429 Too Many Requests'        │ Chờ 60 giây và nhấn gửi lại (Retry).│
│ 2. Lỗi quá hạn ngạch ngày (Quota Limit)│ Chuyển sang dùng API Key dự phòng.  │
│ 3. Lỗi ảnh quá dung lượng (> 5MB)     │ Dùng công cụ nén ảnh hoặc chụp lại. │
│ 4. Lỗi lộ Khóa API Key                │ Bấm 'Revoke/Delete Key' tạo khóa mới│
└───────────────────────────────────────┴─────────────────────────────────────┘
```

#### 1.3.3. Quy Tắc An Toàn & Bảo Mật Khóa API (API Key Security)

> ⚠️ **CẢNH BÁO BẢO MẬT HẠN NGẠCH**  
> *Khóa API (API Key) đóng vai trò như "chìa khóa nhà" của bạn. Nếu lộ Khóa API ra bên ngoài, người khác có thể dùng trộm hạn ngạch 1.000 RPD của bạn, khiến ứng dụng trên lớp học của học sinh bị dừng hoạt động.*

---

## **NHỮNG ĐIỂM CỐT LÕI MODULE 1**

* **1. Vibe Coding làm chủ công cụ:** Giáo viên chuyển từ tư duy "người dùng công cụ" sang tư duy "Kỹ sư Trưởng" điều khiển AI sinh mã nguồn bằng ngôn ngữ tự nhiên.
* **2. Khám phá 6 chế độ qua Live Demo Plant ID:** Thành thạo thao tác trên Build Mode, Live Preview và Annotation Mode ✏️ để tương tác trực tiếp với giao diện ứng dụng.
* **3. Quản lý hạn ngạch & Bảo mật API Key:** Kiểm soát giới hạn 15 RPM và 1.000 RPD của tài khoản miễn phí, nằm lòng Cẩm nang Troubleshooting 4 sự cố kỹ thuật.

---

# **MODULE 2: NHỮNG YẾU TỐ CỐT LÕI CẦN XÂY DỰNG APP, CẤU TRÚC PROMPT & KIỂM THỬ**

*Trong module này, các bạn sẽ đóng vai Kỹ sư Trưởng (Lead Engineer) để tự tay thiết kế và kiểm thử ứng dụng Nhận diện cây (Plant ID App) từ Live Demo ở Module 1 qua 3 phần trọng tâm:*

- *2.1. Những Yếu Tố Cần Để Xây Dựng App (Bóc tách 5 thành phần Requirements Plant ID)*
- *2.2. Vận Dụng Thiết Kế App & Cấu Trúc Prompt (Data Flow, UI Wireframe, Master Prompt, Đánh giá UX Microsoft & Product Specification)*
- *2.3. Kiểm Thử Ứng Dụng & Sửa Lỗi AI Fabrication (Quy trình Kiểm thử 5 Lớp & Trạng thái Release Candidate)*

---

> **⏱ Thời lượng:** 90 phút (30 phút Phân tích Yêu cầu Plant ID + 30 phút Thiết kế App, Master Prompt & Đánh giá UX + 30 phút Kiểm thử 5 Lớp & Sửa lỗi)  
> **🎯 Mục tiêu bài học:**  
> - Bóc tách chính xác 5 thành phần Yêu cầu sản phẩm (Requirements Breakdown) cho ứng dụng Nhận diện cây (Plant ID App).  
> - Thiết kế sơ đồ luồng dữ liệu (Data Flow), bản phác thảo giao diện (UI Wireframe), làm chủ công thức biên dịch Lệnh điều khiển tối ưu (Master Prompt 5 thành phần) và đánh giá 4 tiêu chí trải nghiệm người dùng (UX - User Experience) của Microsoft.  
> - Thực hành Quy trình Kiểm thử 5 Lớp (5-Layer Testing Framework), phát hiện lỗi ảo giác AI (AI Fabrication) và nghiệm thu sản phẩm đạt trạng thái Release Candidate.  
> **📦 Sản phẩm đầu ra:** Bản đặc tả chi tiết (Product Specification) + Bản phác thảo giao diện (UI Wireframe) + Checklist Kiểm thử 5 Lớp $\rightarrow$ Điền hoàn chỉnh vào **Hồ Sơ Dự Án — Phần 1 & Phần 2**.

---

## **2. Những Yếu Tố Cốt Lõi Cần Xây Dựng App, Cấu Trúc Prompt & Kiểm Thử**

### 2.1. Những yếu tố cần để xây dựng App (Bóc tách từ Live Demo Plant ID)

Từ trải nghiệm Live Demo ứng dụng Nhận diện cây (Plant ID App) trên Google AI Studio ở Module 1, các bạn tiến hành phân tích bài toán sư phạm và bóc tách các yếu tố cốt lõi trước khi viết câu lệnh.

#### 2.1.1. Phân Tích Bài Toán Sư Phạm & Ngữ Cảnh Sử Dụng (Target User & Problem Framing)

Trước khi xác định các tính năng kỹ thuật, Kỹ sư Trưởng (giáo viên STEM) phải trả lời 3 câu hỏi định hình bài toán sư phạm:

1. **Bài toán thực tế cần giải quyết:** Học sinh đi thực địa Sinh học ngoài sân trường gặp khó khăn trong việc tra cứu tên và đặc điểm cây trồng. Nếu dùng sách giáo khoa thì cồng kềnh, nếu tìm trên mạng thì gặp quá nhiều thông tin tạp nham.
2. **Chân dung Người dùng mục tiêu (Target User):** Học sinh lớp 6 THCS, chưa có nhiều kỹ năng công nghệ phức tạp, thao tác ứng dụng trên điện thoại di động thông minh (Smartphone) trong điều kiện ánh sáng ngoài trời nắng.
3. **Điều kiện hạ tầng & Ngữ cảnh sử dụng:** Mạng Internet di động (3G/4G) ngoài sân trường có thể không ổn định, thiết bị sử dụng là camera điện thoại có độ phân giải khác nhau.

---

#### 2.1.2. 5 Thành Phần Yêu Cầu Sản Phẩm Cốt Lõi (Requirements Breakdown Cho Plant ID App)

Mọi ứng dụng AI giáo dục chuẩn mực đều được cấu thành từ 5 yếu tố cốt lõi sau:

```
   ┌─────────────────────────────────────────────────────────────────┐
   │            5 THÀNH PHẦN YÊU CẦU SẢN PHẨM CỐT LÕI                │
   ├─────────────────────────────────────────────────────────────────┤
   │ 1. NGƯỜI DÙNG MỤC TIÊU (Target User) : Ai dùng? Trong ngữ cảnh nào?│
   │ 2. DỮ LIỆU ĐẦU VÀO (Input)            : Đưa thông tin gì vào App?│
   │ 3. KẾT QUẢ ĐẦU RA (Output)            : App trả về thông tin gì? │
   │ 4. CHỨC NĂNG CỐT LÕI (Core Features)  : Nút bấm & thao tác chính │
   │ 5. RÀNG BUỘC (Constraints)            : Giới hạn App KHÔNG ĐƯỢC làm│
   └─────────────────────────────────────────────────────────────────┘
```

##### 1. Người Dùng Mục Tiêu (Target User)
* *Áp dụng vào Plant ID App:* "Học sinh lớp 6 THCS, dùng điện thoại di động ngoài sân trường khi học thực địa môn Sinh học, ánh sáng thay đổi".

##### 2. Dữ Liệu Đầu Vào (Input)
* *Áp dụng vào Plant ID App:* Ảnh chụp lá cây hoặc thân cây từ camera điện thoại. Định dạng JPG/PNG. Dung lượng tối đa 5MB.

##### 3. Kết Quả Đầu Ra (Output)
* *Áp dụng vào Plant ID App:* Tên tiếng Việt (VD: Cây Bàng), Tên Latin, Họ thực vật, Mô tả 2 câu và Độ tin cậy (Confidence Level).

##### 4. Chức Năng Cốt Lõi (Core Features)
* *Áp dụng vào Plant ID App:* Khung tải ảnh, Nút "Phân Tích", Thẻ kết quả, Nút "Chụp lại" và Thanh trạng thái "Đang phân tích...".

##### 5. Ràng Buộc Kỹ Thuật & Đạo Đức (Constraints)
* *Áp dụng vào Plant ID App:* Không lưu dữ liệu HS, không bắt đăng nhập, không nhận ảnh > 5MB, không đoán mò khi ảnh mờ.

---

### 2.2. Vận dụng thiết kế App & Cấu trúc Prompt

#### 2.2.1. Thiết Kế Luồng Dữ Liệu (Data Flow) & Phác Thảo Giao Diện (UI Wireframe Cho Plant ID)

##### 1. Thiết kế Luồng dữ liệu (Data Flow):
```
[Học sinh chụp/upload ảnh] ➔ [Hiển thị "Đang phân tích..."] ➔ [Gửi Gemini Vision API]
                                                                    ↓
   [Hiển thị thẻ kết quả 5 trường]  (Nhận diện được cây?) ➔ [Hiển thị "Không xác định"]
```

##### 2. Bản phác thảo giao diện 1 màn hình (UI Wireframe Plant ID App):
```
┌─────────────────────────────────┐
│  Nhận Diện Cây Thực Địa        │  ← Header xanh lá
├─────────────────────────────────┤
│   [ Chụp ảnh / Upload ảnh ]    │  ← Khung upload lớn
├─────────────────────────────────┤
│         [ PHÂN TÍCH ]          │  ← Nút kích hoạt AI
├─────────────────────────────────┤
│  Tên tiếng Việt: Cây Bàng     │  ← Thẻ kết quả
│  Latin: Terminalia catappa     │
│  Độ tin cậy: Cao               │
├─────────────────────────────────┤
│  Kết quả mang tính tham khảo  │  ← Footer disclaimer
└─────────────────────────────────┘
```

#### 2.2.2. Cấu Trúc Master Prompt (Lệnh Điều Khiển Tối Ưu Cho Plant ID)

```text
Act as an expert Web Developer and STEM Educator.
Build a Plant Identifier web application for Vietnamese secondary school biology field trips.
Allow students to upload an image or take a photo of a plant/leaf outside the schoolyard.
Call Gemini Vision API to analyze and return ONLY 5 exact fields:
1. name_vn (Vietnamese name)
2. scientific_name (Latin name)
3. family (Plant family)
4. description (2 short simple sentences)
5. confidence_level (High/Medium/Low)

Display results in a single-page clean card layout with forest green header and a large capture button.
RÀNG BUỘC (Constraints):
- NO unnecessary indoor gardening care features (no watering, fertilizer, or soil info).
- NO user login or registration required.
- NO student data or photo storage.
- Include a footer disclaimer: "Results for reference only, please check with your teacher".
```

#### 2.2.3. Đánh Giá Trải Nghiệm Người Dùng (UX theo 4 Tiêu Chí Microsoft Cho Plant ID)

Sau khi vẽ sơ đồ Luồng dữ liệu (2.2.1) và biên dịch Master Prompt (2.2.2), giáo viên sử dụng bộ 4 tiêu chí trải nghiệm người dùng (UX - User Experience) của Microsoft để đánh giá chất lượng sản phẩm vừa tạo ra:

| Tiêu chí UX | Câu hỏi kiểm tra sư phạm | Áp dụng đánh giá trên Plant ID App |
|---|---|---|
| **1. Useful (Có ích)** | Ứng dụng có giải quyết đúng bài toán thực tế không? | ĐẠT — Phục vụ trực tiếp việc ghi bài thu hoạch thực địa môn Sinh học |
| **2. Reliable (Đáng tin cậy)** | AI có trung thực thông báo khi không chắc chắn không? | ĐẠT — Hiển thị "Độ tin cậy: Thấp" kèm lời khuyên *"Hỏi lại giáo viên"* khi ảnh mờ |
| **3. Accessible (Dễ dùng)** | Học sinh không giỏi công nghệ có dễ dùng không? | ĐẠT — Nút chụp to ở trung tâm màn hình, không cần đăng nhập phức tạp |
| **4. Pleasant (Dễ chịu)** | Giao diện có thân thiện, phù hợp ngữ cảnh không? | ĐẠT — Tông màu xanh lá mộc mạc, font chữ to rõ khi xem ngoài trời nắng |

#### 2.2.4. Mẫu Bản Đặc Tả Sản Phẩm Hoàn Chỉnh (Product Specification)

Product Specification tổng hợp 5 phần: Mô tả sản phẩm, Scope v1 (SẼ làm), Out of Scope (KHÔNG làm), Requirements và Tiêu chí nghiệm thu (Acceptance Criteria).

---

## **2.3. Kiểm Thử Ứng Dụng & Sửa Lỗi AI Fabrication**

### 2.3.1. Quy Trình Kiểm Thử 5 Lớp (5-Layer Testing Framework)

1. **Lớp 1: Luồng chính (Happy Path):** Upload ảnh lá bàng rõ ➔ Trả đúng 5 trường kết quả.
2. **Lớp 2: Trường hợp biên (Edge Case):** Upload ảnh mờ/tối ➔ Hiện cảnh báo *"Độ tin cậy: Thấp"*.
3. **Lớp 3: Chống ảo giác (AI Fabrication Guard):** Upload ảnh xe máy/mặt người ➔ Hiện *"Không xác định"*, tuyệt đối không tự bịa tên cây.
4. **Lớp 4: Giao diện di động (Responsive UI):** Tự động co giãn vừa vặn trên di động 375px.
5. **Lớp 5: An toàn & Riêng tư (Privacy & Safety):** Không lưu trữ dữ liệu hay ảnh học sinh.

### 2.3.2. Sửa Lỗi Dựa Trên Phản Hồi (Bug-Driven Optimization)
Khoanh vùng lỗi bằng bút **Annotation Mode ✏️** ➔ Ra lệnh sửa trong Chat Panel ➔ Bấm lưu điểm **Checkpoint**.

### 2.3.3. Trạng Thái Nghiệm Thu Release Candidate
Hoàn thành Bảng kiểm 6 tiêu chuẩn nghiệm thu sản phẩm sẵn sàng đưa vào lớp học.

---

## **NHỮNG ĐIỂM CỐT LÕI MODULE 1 & MODULE 2**

* **Module 1:** Thành thạo 6 chế độ làm việc trên Google AI Studio, làm chủ tư duy Vibe Coding và kiểm soát hạn ngạch Quota 15 RPM / 1.000 RPD.
* **Module 2:** Đóng vai Kỹ sư Trưởng bóc tách 5 Requirements, vẽ Wireframe, biên dịch Master Prompt, đánh giá UX Microsoft và chạy Kiểm thử 5 Lớp nghiệm thu sản phẩm.

---

*Bản Draft Hợp Nhất Module 1 & Module 2 — Phiên bản KDI 2026+ (Chuẩn Logic UX)*
