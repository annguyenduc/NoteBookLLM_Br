# **MODULE 1: NỀN TẢNG GOOGLE AI STUDIO**
### **Khóa Học: PHÁT TRIỂN ỨNG DỤNG VỚI AI (Mã học phần: AIApp-M2.1)**

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
* **Thao tác chỉnh sửa bằng Annotation Mode ✏️:** Giáo viên dùng chuột khoanh tròn nút "Chụp lại", gõ ghi chú *"Đổi nút này sang màu xanh lá đậm và phóng to font chữ"* ➔ AI tự đọc hình vẽ và điều chỉnh giao diện chuẩn xác ngay lập tức!

> 💡 **Kết luận sư phạm từ Live Demo:**  
> *Chỉ khi giáo viên nắm giữ tư duy Spec-first (bản đặc tả trước ở Demo B), ứng dụng AI sinh ra mới thực sự tinh gọn, đúng mục tiêu bài dạy và không bị tràn lề hay vỡ giao diện như Demo A.*

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

**3 Quy tắc bảo mật giáo viên cần dặn học sinh:**
1. **Không dán công khai:** Tuyệt đối không đưa Khóa API vào mã nguồn gửi lên các trang mạng xã hội hoặc kho lưu trữ công khai.
2. **Sử dụng môi trường nội bộ:** Trong giờ thực hành, hướng dẫn học sinh chạy ứng dụng trực tiếp trong màn hình Live Preview của Google AI Studio.
3. **Thu hồi khi nghi ngờ:** Nếu nghi ngờ lộ chìa khóa, vào mục `Get API Key` trên AI Studio và bấm nút **"Delete / Revoke" (Xóa/Thu hồi)** để tạo khóa mới ngay lập tức.

---

* **★ Thử thách 2 (Hands-on Challenge 2):** Thực hành khởi tạo 01 Khóa API Key cá nhân trên Google AI Studio, dán thử vào khung chạy và thực hiện quy trình kiểm tra bảo mật (Thời lượng thực hành: 10 phút).

---

## **NHỮNG ĐIỂM CỐT LÕI MODULE 1**

* **1. Vibe Coding làm chủ công cụ:** Giáo viên chuyển từ tư duy "người dùng công cụ" sang tư duy "Kỹ sư Trưởng" điều khiển AI sinh mã nguồn bằng ngôn ngữ tự nhiên.
* **2. Khám phá 6 chế độ qua Live Demo Plant ID:** Thành thạo thao tác trên Build Mode, Live Preview và Annotation Mode ✏️ để tương tác trực tiếp với giao diện ứng dụng.
* **3. Quản lý hạn ngạch & Bảo mật API Key:** Kiểm soát giới hạn 15 RPM và 1.000 RPD của tài khoản miễn phí, nằm lòng Cẩm nang Troubleshooting 4 sự cố kỹ thuật.

---

## BẢNG KIỂM NGHIỆM THU KỸ NĂNG MODULE 1 (Checklist)

> Học viên tự kiểm tra danh sách 6 kỹ năng thao tác sau khi hoàn thành Module 1:

- `[ ]` **Kỹ năng 1:** Đăng nhập thành công Google AI Studio tại `aistudio.google.com`.
- `[ ]` **Kỹ năng 2:** Khởi tạo và bảo mật Khóa API Key cá nhân.
- `[ ]` **Kỹ năng 3:** Phân biệt được khi nào dùng Gemini 1.5 Flash và Gemini 2.0 Flash (Multimodal Vision).
- `[ ]` **Kỹ năng 4:** Kích hoạt thành công chế độ xây dựng ứng dụng (Build Mode).
- `[ ]` **Kỹ năng 5:** Sử dụng thành thạo công cụ bút vẽ Annotation Mode ✏️ để phản hồi chỉnh sửa giao diện Live Demo Plant ID App.
- `[ ]` **Kỹ năng 6:** Xử lý được lỗi quá hạn ngạch `429 Too Many Requests`.

> **🔗 SỢI CHỈ ĐỎ BÀN GIAO SANG MODULE 2:**  
> *Sau khi trực tiếp trải nghiệm Live Demo ứng dụng Plant ID ở Module 1, các bạn đã sẵn sàng bước sang **Module 2: Những yếu tố cốt lõi cần xây dựng App, Cấu trúc Prompt & Kiểm thử** để đóng vai Kỹ sư Trưởng tự tay bóc tách 5 thành phần Requirements, vẽ sơ đồ UI Wireframe, biên dịch Master Prompt và chạy Quy trình Kiểm thử 5 Lớp cho chính ứng dụng Plant ID này!*

---

*Module 1 — Phiên bản 4.0 (Gắn Kết Sợi Chỉ Đỏ Live Demo Plant ID)*
