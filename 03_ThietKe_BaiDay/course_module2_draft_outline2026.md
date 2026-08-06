# **MODULE 2: NHỮNG YẾU TỐ CỐT LÕI CẦN XÂY DỰNG APP, CẤU TRÚC PROMPT & KIỂM THỬ**
### **Khóa Học: PHÁT TRIỂN ỨNG DỤNG VỚI AI (Mã học phần: AIApp-M2.1)**

*Trong module này, các bạn sẽ đóng vai Kỹ sư Trưởng (Lead Engineer) để tự tay thiết kế và kiểm thử ứng dụng Nhận diện cây (Plant ID App) từ Live Demo ở Module 1 qua 3 phần trọng tâm:*

- *2.1. Những Yếu Tố Cần Để Xây Dựng App (Phân tích Ngữ cảnh Sư phạm & 5 Thành phần Requirements)*
- *2.2. Vận Dụng Thiết Kế App & Cấu Trúc Prompt (Data Flow, UI Wireframe, Master Prompt, Đánh giá UX Microsoft & Product Specification)*
- *2.3. Kiểm Thử Ứng Dụng & Sửa Lỗi AI Fabrication (Quy trình Kiểm thử 5 Lớp & Trạng thái Release Candidate)*

---

> **⏱ Thời lượng:** 90 phút (30 phút Phân tích Ngữ cảnh & Yêu cầu Plant ID + 30 phút Thiết kế App, Master Prompt & Đánh giá UX + 30 phút Kiểm thử 5 Lớp & Sửa lỗi)  
> **🎯 Mục tiêu bài học:**  
> - Phân tích bài toán sư phạm và bóc tách chính xác 5 thành phần Yêu cầu sản phẩm (Requirements Breakdown) cho ứng dụng Nhận diện cây (Plant ID App).  
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

Mọi ứng dụng AI giáo dục chuẩn mực đều được cấu thành từ 5 yếu tố cốt lõi sau. Đây là "ngôn ngữ giao tiếp chung" giữa giáo viên và mô hình AI khi lập trình bằng ngôn ngữ tự nhiên (Vibe coding):

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
* **Câu hỏi định hướng:** Ai sẽ trực tiếp thao tác trên ứng dụng này? Độ tuổi, trình độ công nghệ và hoàn cảnh sử dụng là gì?
* *Áp dụng vào Plant ID App:* "Học sinh lớp 6 THCS, dùng điện thoại di động ngoài sân trường khi học thực địa môn Sinh học, ánh sáng thay đổi".

##### 2. Dữ Liệu Đầu Vào (Input)
* **Câu hỏi định hướng:** Người dùng đưa dữ liệu gì vào ứng dụng? Định dạng là gì? Giới hạn dung lượng ra sao?
* *Áp dụng vào Plant ID App:* Ảnh chụp lá cây hoặc thân cây từ camera điện thoại. Định dạng JPG/PNG. Dung lượng tối đa 5MB.

##### 3. Kết Quả Đầu Ra (Output)
* **Câu hỏi định hướng:** Ứng dụng sẽ phân tích và trả về những trường thông tin cụ thể nào?
* *Áp dụng vào Plant ID App:* Tên tiếng Việt (VD: Cây Bàng), Tên Latin, Họ thực vật, Mô tả 2 câu ngắn gọn và Độ tin cậy (Confidence Level).

##### 4. Chức Năng Cốt Lõi (Core Features)
* **Câu hỏi định hướng:** Ứng dụng cần có những nút bấm/thao tác chính nào?
* *Áp dụng vào Plant ID App:* Khung tải ảnh, Nút "Phân Tích", Thẻ kết quả, Nút "Chụp lại" và Thanh trạng thái "Đang phân tích...".

##### 5. Ràng Buộc Kỹ Thuật & Đạo Đức (Constraints)
* **Câu hỏi định hướng:** Ứng dụng **KHÔNG ĐƯỢC** làm gì?
* *Áp dụng vào Plant ID App:* Không lưu dữ liệu HS, không bắt đăng nhập, không nhận ảnh > 5MB, không đoán mò khi ảnh mờ.

> 💡 **Lăng kính kỹ thuật**  
> *Ràng buộc sản phẩm (Constraints) thường bị bỏ sót vì người dùng hay tập trung vào "muốn làm gì" hơn là "không được làm gì". Trong giáo dục, ràng buộc bảo vệ quyền riêng tư học sinh là bắt buộc về mặt pháp lý và đạo đức.*

---

### 2.2. Vận dụng thiết kế App & Cấu trúc Prompt

#### 2.2.1. Thiết Kế Luồng Dữ Liệu (Data Flow) & Phác Thảo Giao Diện (UI Wireframe Cho Plant ID)

##### 1. Thiết kế Luồng dữ liệu (Data Flow - Luồng Di Chuyển Dữ Liệu):
Vẽ sơ đồ mô tả dữ liệu di chuyển từ đầu vào (Input) qua xử lý AI đến kết quả đầu ra (Output) cho Plant ID App:

```
[Học sinh chụp/upload ảnh]
         ↓
[Hiển thị trạng thái "Đang phân tích..."]
         ↓
[Gửi ảnh đến mô hình Gemini Vision API]
         ↓
   ┌─────────────────────────────┐
   │ Gemini phân tích hình ảnh   │
   │ → Nhận diện được cây không? │
   └─────────────────────────────┘
         ↓                    ↓
   [Hiển thị thẻ kết quả]   [Hiển thị "Không xác định"
    Tên, Latin, Mô tả,        + Lời khuyên hỏi GV]
    Độ tin cậy: Cao]
```

##### 2. Bản phác thảo giao diện 1 màn hình (UI Wireframe Plant ID App):

```
┌─────────────────────────────────┐
│  Nhận Diện Cây Thực Địa        │  ← Header: tiêu đề ứng dụng
│  [Sinh học lớp 6 - THCS]       │
├─────────────────────────────────┤
│                                 │
│   [ Chụp ảnh / Upload ảnh ]    │  ← Khung upload ảnh lớn, dễ bấm
│   [ Kéo thả ảnh vào đây ]      │
│                                 │
├─────────────────────────────────┤
│         [ PHÂN TÍCH ]          │  ← Nút bấm lớn kích hoạt AI
├─────────────────────────────────┤
│  Đang phân tích hình ảnh...    │  ← Thanh trạng thái chờ (Loading)
├─────────────────────────────────┤
│  Tên tiếng Việt: Cây Bàng     │  ← Thẻ hiển thị kết quả
│  Latin: Terminalia catappa     │
│  Mô tả: Cây thân gỗ...        │
│  Độ tin cậy: Cao               │
├─────────────────────────────────┤
│  [ Chụp lại ]                  │  ← Nút thực hiện lại
├─────────────────────────────────┤
│  Kết quả mang tính tham khảo  │  ← Chú thích miễn trừ trách nhiệm
└─────────────────────────────────┘
```

---

#### 2.2.2. Cấu Trúc Master Prompt (Lệnh Điều Khiển Tối Ưu 5 Thành Phần Cho Plant ID)

Master Prompt là câu lệnh hoàn chỉnh chứa đầy đủ bản đặc tả để đưa vào Google AI Studio Build Mode nhằm kích hoạt AI sinh ứng dụng Plant ID chuẩn xác:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                      CẤU TRÚC MASTER PROMPT 5 THÀNH PHẦN                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ [1. VAI TRÒ (Role)]          : You are an expert Web Developer & STEM Teacher.│
│ [2. BÀI TOÁN (Context)]       : Build a Plant Identifier app for biology.   │
│ [3. ĐẶC TẢ (Input/Output)]    : Input: Leaf image. Output ONLY: name_vn,     │
│                                scientific_name, family, description,        │
│                                confidence_level.                            │
│ [4. GIAO DIỆN (UI/UX)]        : Mobile-first 1-page layout, green header.   │
│ [5. RÀNG BUỘC (Constraints)]  : NO indoor care info, NO login required,     │
│                                include disclaimer "Check with teacher".     │
└─────────────────────────────────────────────────────────────────────────────┘
```

##### Đoạn Master Prompt Mẫu Cho Ứng Dụng Plant ID (Gõ vào AI Studio Build Mode):

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

---

#### 2.2.3. Đánh Giá Trải Nghiệm Người Dùng (UX theo 4 Tiêu Chí Microsoft Cho Plant ID)

Sau khi vẽ sơ đồ Luồng dữ liệu (2.2.1) và biên dịch Master Prompt (2.2.2), giáo viên sử dụng bộ 4 tiêu chí trải nghiệm người dùng (UX - User Experience) của Microsoft để đánh giá chất lượng sản phẩm vừa tạo ra:

| Tiêu chí UX | Câu hỏi kiểm tra sư phạm | Áp dụng đánh giá trên Plant ID App |
|---|---|---|
| **1. Useful (Có ích)** | Ứng dụng có giải quyết đúng bài toán thực tế không? | ĐẠT — Phục vụ trực tiếp việc ghi bài thu hoạch thực địa môn Sinh học |
| **2. Reliable (Đáng tin cậy)** | AI có trung thực thông báo khi không chắc chắn không? | ĐẠT — Hiển thị "Độ tin cậy: Thấp" kèm lời khuyên *"Hỏi lại giáo viên"* khi ảnh mờ |
| **3. Accessible (Dễ dùng)** | Học sinh không giỏi công nghệ có dễ dùng không? | ĐẠT — Nút chụp to ở trung tâm màn hình, không cần đăng nhập phức tạp |
| **4. Pleasant (Dễ chịu)** | Giao diện có thân thiện, phù hợp ngữ cảnh không? | ĐẠT — Tông màu xanh lá mộc mạc, font chữ to rõ khi xem ngoài trời nắng |

---

#### 2.2.4. Mẫu Bản Đặc Tả Sản Phẩm Hoàn Chỉnh (Product Specification)

Product Specification là tài liệu tổng hợp **Bài toán + Yêu cầu + Thiết kế + UX** thành 1 trang chuẩn hóa. Đây chính là đầu ra quan trọng nhất của Module 2:

```
══════════════════════════════════════════════════════════════
PRODUCT SPECIFICATION (BẢN ĐẶC TẢ SẢN PHẨM)
Ứng Dụng Nhận Diện Cây Trồng Thực Địa (Plant ID App)
Mã học phần: AIApp-M2.1 | Phiên bản: v1.0
══════════════════════════════════════════════════════════════

1. MÔ TẢ SẢN PHẨM (Product Description)
   Ứng dụng AI hỗ trợ học sinh lớp 6 nhận diện tên cây trồng bằng
   ảnh chụp từ điện thoại, phục vụ bài học thực địa Sinh học.

2. PHẠM VI PHIÊN BẢN 1 (Scope v1 - Tính năng SẼ làm)
   - Nhận ảnh tải lên (upload) hoặc chụp trực tiếp từ camera điện thoại
   - Phân tích qua Gemini Vision API và trả về kết quả 5 trường chuẩn
   - Hiển thị thông báo cảnh báo khi độ tin cậy của AI ở mức thấp
   - Giao diện tối ưu di động (mobile-first), 1 màn hình duy nhất

3. NGOÀI PHẠM VI THỰC HIỆN (Out of Scope - Tính năng KHÔNG làm ở v1)
   - Không làm tính năng lưu lịch sử tra cứu
   - Không làm bản đồ vị trí phân bố cây
   - Không chạy chế độ ngoại tuyến (offline - không có mạng Internet)

4. YÊU CẦU CHI TIẾT (Detailed Requirements)
   Người dùng mục tiêu (Target User) : Học sinh lớp 6 THCS, dùng điện thoại ngoài sân
   Dữ liệu đầu vào (Input)          : Ảnh JPG/PNG từ camera/upload, tối đa 5MB
   Kết quả đầu ra (Output)         : Tên VN, Tên Latin, Họ TV, Mô tả 2 câu, Độ tin cậy
   Chức năng cốt lõi (Core Features): Tải ảnh/Chụp ảnh, Nút Phân Tích, Thẻ kết quả, Chụp lại
   Ràng buộc (Constraints)          : Không lưu dữ liệu HS, không bắt đăng nhập, giới hạn 5MB

5. TIÊU CHÍ NGHIỆM THU (Acceptance Criteria - Điều kiện ĐẠT)
   [ ] Nhận diện chính xác ≥ 4 loài cây sân trường phổ biến
   [ ] Giao diện tự động co giãn (responsive) hiển thị tốt trên điện thoại di động
   [ ] Trả về "Không xác định" khi ảnh mờ hoặc không chứa cây
   [ ] Không bị lỗi sập ứng dụng (crash) khi người dùng tải file > 5MB
   [ ] Chân trang (Footer) có nhãn cảnh báo miễn trừ trách nhiệm (disclaimer)
```

---

## **2.3. Kiểm Thử Ứng Dụng & Sửa Lỗi AI Fabrication**

**⏱ 30 phút**

Sau khi biên dịch Master Prompt và kích hoạt AI Studio Build Mode để sinh ra ứng dụng Plant ID, giáo viên tiến hành **Quy trình Kiểm thử 5 Lớp (5-Layer Testing Framework)** trên chính ứng dụng này để phát hiện rủi ro ảo giác AI (AI Fabrication - AI tự bịa thông tin) trước khi mang vào dạy học.

### 2.3.1. Quy Trình Kiểm Thử 5 Lớp (5-Layer Testing Framework Cho Plant ID)

1. **Lớp 1: Luồng chính (Happy Path Testing):** Upload ảnh lá bàng rõ ➔ Trả đúng 5 trường kết quả.
2. **Lớp 2: Trường hợp biên (Edge Cases Testing):** Upload ảnh mờ/tối ➔ Hiện cảnh báo *"Độ tin cậy: Thấp"*.
3. **Lớp 3: Chống ảo giác (AI Fabrication Guard):** Upload ảnh xe máy/mặt người ➔ Hiện *"Không xác định"*, tuyệt đối không tự bịa tên cây.
4. **Lớp 4: Giao diện di động (Responsive UI Testing):** Tự động co giãn vừa vặn trên di động 375px.
5. **Lớp 5: An toàn & Riêng tư (Privacy & Safety Testing):** Không lưu trữ dữ liệu hay ảnh học sinh.

---

### 2.3.2. Quy Trình Sửa Lỗi Dựa Trên Phản Hồi (Bug-Driven Optimization)

Khoanh vùng lỗi bằng bút **Annotation Mode ✏️** ➔ Ra lệnh sửa trong Chat Panel ➔ Bấm lưu điểm **Checkpoint**.

---

### 2.3.3. Trạng Thái Nghiệm Thu Release Candidate (Sẵn Sàng Xuất Bản)

Plant ID App được công nhận đạt trạng thái **Release Candidate (Bản nguyên mẫu sẵn sàng xuất bản)** khi vượt qua 100% các tiêu chuẩn kiểm thử trong Bảng kiểm 6 điều kiện.

---

## **NHỮNG ĐIỂM CỐT LÕI MODULE 2**

* **1. Phân tích ngữ cảnh & 5 thành phần Yêu cầu:** Target User, Input, Output, Core Features và Constraints là bộ khung định hình mọi ứng dụng AI.
* **2. Thiết kế App & Đánh giá UX Microsoft:** Tối ưu sơ đồ Data Flow, vẽ Wireframe, biên dịch Master Prompt và đánh giá 4 tiêu chí UX (Useful, Reliable, Accessible, Pleasant).
* **3. Công thức Master Prompt 5 thành phần:** Biên dịch bản đặc tả thành câu lệnh tiếng Anh/tiếng Việt tối ưu để kích hoạt AI Studio Build Mode cho Plant ID App.
* **4. Kiểm thử 5 Lớp (5-Layer Testing):** Làm chủ kỹ thuật phát hiện lỗi AI Fabrication và đưa ứng dụng Plant ID đạt trạng thái Release Candidate sẵn sàng cho tiết học.

---

## SẢN PHẨM SAU MODULE 2

| Sản phẩm | Mô tả chi tiết | Trạng thái |
|---|---|---|
| **Bản tóm tắt sản phẩm (Product Brief)** | 3 câu hỏi nền tảng (Ai gặp vấn đề? Vấn đề gì? AI có phù hợp không?) | `[ ]` |
| **Bản đặc tả chi tiết (Product Specification)** | 5 thành phần yêu cầu + Scope v1 + Out of Scope + Tiêu chí nghiệm thu (Acceptance Criteria) | `[ ]` |
| **Phác thảo giao diện (UI Wireframe)** | Bản phác thảo bố cục 1 màn hình ứng dụng Plant ID kèm các ghi chú nút bấm | `[ ]` |
| **Checklist Kiểm thử 5 Lớp** | Bảng ghi nhận kết quả kiểm thử Happy Path, Edge Case, AI Fabrication, Responsive và Privacy | `[ ]` |

---

*Module 2 — Phiên bản 6.0 (Bối Cảnh & Requirements Đầy Đủ)*
