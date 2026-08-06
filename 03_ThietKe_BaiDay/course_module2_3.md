# MODULE 2+3: Xây Dựng, Kiểm Thử & Hoàn Thiện Ứng Dụng AI
### Khoá Học: Phát Triển Ứng Dụng Với AI

---

> **⏱ Thời lượng:** 180 phút (90 phút Xây dựng + 90 phút Kiểm thử & Hoàn thiện)  
> **🎯 Mục tiêu:** Chuyển bản đặc tả (Product Specification) thành nguyên mẫu Prototype V1, thực hiện kiểm thử 5 lớp, sửa lỗi AI Fabrication và hoàn thiện phiên bản Release Candidate sẵn sàng xuất bản.  
> **📦 Sản phẩm đầu ra:** Prototype V1 → Release Candidate + Task List 4 Phase + Checklist kiểm thử & Đạo đức AI (Điền vào **Hồ Sơ Dự Án — Phần 2 & Phần 3**).

---

## TỔNG QUAN MODULE 2+3

```
Thời gian       Mục     Nội dung chính
────────────────────────────────────────────────────────────────────────────────────────
[PHẦN 1: XÂY DỰNG ỨNG DỤNG — 90 PHÚT]
00:00–15:00     2.1     Khởi tạo dự án & Thiết lập AI Chips ban đầu
15:00–40:00     2.2     Sinh nguyên mẫu đầu tiên (Prototype V1) từ Master Prompt
40:00–55:00     2.3     Review: Đối chiếu Prototype V1 vs. Product Specification
55:00–80:00     2.4     Refine: Cải tiến theo vòng lặp (Task List + Chat Panel + Bút vẽ ✏️)
80:00–90:00     2.5     Quản lý phiên bản (Checkpoint & Restore)
────────────────────────────────────────────────────────────────────────────────────────
[PHẦN 2: KIỂM THỬ, CẢI TIẾN & HOÀN THIỆN — 90 PHÚT]
90:00–115:00    3.1     Kiểm thử 5 lớp & Phát hiện lỗi AI Fabrication
115:00–140:00   3.2     Sửa lỗi thực tế sau kiểm thử (Bug-Driven Optimization)
140:00–160:00   3.3     Đánh giá chất lượng & Trạng thái Release Candidate
160:00–180:00   3.4     Đạo đức AI trong giáo dục — Khung phân tích Mô hình 3 Vai
```

---

# PHẦN 1: XÂY DỰNG ỨNG DỤNG (BUILD)
> **Mục tiêu:** Đưa bản đặc tả Product Spec ở Module 1 vào Google AI Studio Build Mode để sinh ra ứng dụng nguyên mẫu chạy thật (Prototype V1).

---

## 2.1 Khởi Tạo Dự Án & Thiết Lập AI Chips Ban Đầu

**⏱ 15 phút**

### Quy Trình Thao Tác Trực Tiếp Trên Google AI Studio

1. Mở trình duyệt Chrome, truy cập địa chỉ: `https://aistudio.google.com/apps`.
2. Đảm bảo đã đăng nhập bằng **Gmail cá nhân (`@gmail.com`)**. *(Lưu ý: Không dùng tài khoản trường học `@edu` để tránh bị chặn quyền deploy và nạp API)*.
3. Bấm vào nút **`+ New app`** ở góc trên bên trái màn hình.
4. **Thiết lập AI Chips ban đầu:** Tại khung nhập prompt khởi tạo, quan sát danh sách các AI Chips có sẵn bên dưới. Tích chọn bật trước các Chips cần thiết (ví dụ: *Google Search*, *Image Gen*) nếu ứng dụng của bạn cần tính năng tra cứu dữ liệu thời gian thực hoặc sinh ảnh.

> 💡 **Lưu ý sư phạm:** Tại sao phải bật AI Chips ngay từ bước khởi tạo?  
> Các AI Chips thiết lập cấu trúc mã nguồn ban đầu cho mô hình. Nếu bạn không bật từ đầu mà chờ đến khi app đã build xong mới yêu cầu thêm tính năng tìm kiếm hay sinh ảnh, AI Studio sẽ phải refactor lại toàn bộ bộ khung, rất dễ gây ra vỡ giao diện.

---

## 2.2 Sinh Phiên Bản Đầu Tiên (Generate Prototype V1)

**⏱ 25 phút**

### Kỹ Thuật Viết Master Prompt: Intent-Based vs Implementation-Constrained

Để AI Studio sinh ra đúng bộ khung bạn muốn ngay từ lượt gõ đầu tiên, bạn cần kết hợp 2 kỹ thuật viết prompt:

| Kỹ thuật | Bản chất | Ví dụ trong Master Prompt |
|---|---|---|
| **Intent-Based Prompting** | Mô tả *mục tiêu sư phạm* và *trải nghiệm mong muốn* (để AI tự chọn giải pháp kỹ thuật phù hợp) | *"Build a Plant Identifier web app for Vietnamese secondary school biology field trips..."* |
| **Implementation-Constrained** | Ép AI tuân thủ các *ràng buộc cụ thể* về công nghệ, màu sắc, bố cục | *"Display results in a single-page clean card layout with forest green header, NO indoor gardening care features..."* |

---

### Hướng Dẫn Ánh Xạ: Chuyển Product Spec Thành Master Prompt (5 Câu)

Trước khi gõ lệnh, giáo viên tiến hành ánh xạ từng phần trong **Product Specification (Module 1)** thành 5 câu tiếng Anh của Master Prompt:

| Thành phần trong Spec | Nội dung Spec (Ví dụ Plant ID) | Câu lệnh tương ứng trong Master Prompt |
|---|---|---|
| **1. Mục tiêu & Người dùng** | App nhận diện cây cho HS lớp 6 thực địa | `Build a Plant Identifier web app for Vietnamese secondary school biology field trips.` |
| **2. Đầu vào (Input)** | Upload ảnh hoặc chụp lá cây ngoài trường | `Allow students to upload an image or take a photo of a plant/leaf outside the schoolyard.` |
| **3. Đầu ra (Output)** | Tên VN, tên Latin, Họ, Mô tả 2 câu, Độ tin cậy | `Call Gemini Vision to analyze and return ONLY: name_vn, scientific_name, family, description (2 short sentences), confidence_level (High/Medium/Low).` |
| **4. Giao diện (UI/UX)** | 1 màn hình, xanh lá, không tính năng cây cảnh | `Display results in a single-page clean card layout with forest green header, NO unnecessary indoor gardening care features.` |
| **5. Ràng buộc (Constraints)** | Miễn trừ trách nhiệm, nhắc hỏi GV | `Add a disclaimer at bottom "Results for reference only, check with teacher".` |

---

### Master Prompt 5 Thành Phần Chuyển Hóa Từ Product Spec

Dán chính xác Master Prompt sau vào ô *"Build your ideas with Gemini"*:

```text
Build a Plant Identifier web app for Vietnamese secondary school biology field trips.
Allow students to upload an image or take a photo of a plant/leaf outside the schoolyard.
Call Gemini Vision to analyze and return ONLY: name_vn (Vietnamese name), scientific_name (Latin name), family (Plant family), description (2 short sentences describing features), confidence_level (High/Medium/Low).
Display results in a single-page clean card layout with forest green header, NO unnecessary indoor gardening care features (no watering, fertilizer, or soil info), and a disclaimer "Results for reference only, check with teacher".
```

**Thao tác:** Bấm nút **Build** (hoặc tổ hợp phím **Ctrl + Enter**).

Quan sát góc phải màn hình: **Live Preview** bắt đầu dựng giao diện nguyên mẫu (Prototype V1).

> 💡 **Lưu ý sư phạm:** Tại sao Master Prompt lại dùng tiếng Anh dù app phục vụ học sinh Việt Nam?  
> Gemini và bộ dựng mã nguồn của AI Studio xử lý các ràng buộc kỹ thuật (layout, JSON response schema, CSS styling) bằng tiếng Anh chính xác và ổn định hơn 30% so với tiếng Việt. Chúng ta yêu cầu AI trả về dữ liệu hiển thị (`name_vn`, `description`) bằng tiếng Việt, nhưng câu lệnh điều khiển hệ thống nên viết bằng tiếng Anh.

#### ✏️ Hoạt động thực hành: Soạn Master Prompt cho bài toán của bạn (10 phút)
Học viên dùng bảng ánh xạ trên để chuyển bản Product Spec (Phần 1) của mình thành Master Prompt 5 câu và dán vào AI Studio để khởi tạo Prototype V1.

---

## 2.3 Review: Đối Chiếu Prototype V1 vs. Product Specification

**⏱ 15 phút**

> 💡 **Lý do cần bước Review:** AI là mô hình xác suất. Không bao giờ có chuyện Master Prompt sinh ra sản phẩm hoàn hảo 100% ngay lượt đầu. Bước Review giúp học viên đối chiếu giữa **Cái mong muốn (Spec)** và **Cái AI vừa làm ra (Prototype V1)** để phát hiện điểm lệch trước khi ra lệnh cải tiến.

### Bảng Đánh Giá Đối Chiếu (Review Matrix)

| Hạng mục trong Spec | Trạng thái trên Live Preview (Prototype V1) | Đánh giá |
|---|---|---|
| Giao diện 1 màn hình | Đã có header xanh lá và khung upload ảnh | ✅ Đúng spec |
| Nhận diện ảnh & trả kết quả | Upload ảnh lá bàng ➔ Đã hiện tên Cây Bàng và Tên Latin | ✅ Đúng spec |
| Cảnh báo trạng thái chờ | Nút bấm bị đơ khi bấm phân tích, không có hiệu ứng chờ | ❌ Thiếu Loading Spinner |
| Phản hồi khi ảnh mờ/lỗi | Chưa có thông báo khi người dùng upload file quá 5MB | ❌ Thiếu Error Handling |
| Cấu trúc giao diện | Tiêu đề hơi nhỏ, nút Submit chưa thu hút trên mobile | ❌ Cần tinh chỉnh UI |

#### ✏️ Hoạt động thực hành (5 phút)

Quan sát Live Preview ứng dụng của bạn và điền vào bảng review nhanh:

```
Những điểm AI đã làm ĐÚNG Spec:  _______________________________________________
Những điểm AI làm THIẾU hoặc LỆCH: _______________________________________________
```

---

## 2.4 Refine: Cải Tiến Theo Vòng Lặp (Task List + Chat Panel + Bút Vẽ ✏️)

**⏱ 25 phút**

Sau khi đã có danh sách các điểm thiếu/lệch từ bước Review, **không ra lệnh dồn dập**. Hãy phân rã thành **Task List 4 Phase** và sửa từng bước.

```
Phase 1: Tinh chỉnh Giao diện (UI Framework)
 Phase 2: Tinh chỉnh Xử lý AI (AI Logic & Prompting)
  Phase 3: Bổ sung Hiệu ứng & Trải nghiệm (UX & Loading Effects)
   Phase 4: Xử lý Lỗi & Giới hạn (Error Handling & Constraints)
```

---

### Phương Pháp 1: Ra Lệnh Bằng Chat Panel

Dùng Chat Panel ở cột bên trái để gửi các câu lệnh tinh chỉnh logic hoặc thêm tính năng:

**Ví dụ lệnh bổ sung hiệu ứng Spinner Loading (Phase 3):**
```text
Show a centered spinning loader icon with text "Đang phân tích hình ảnh..." when user submits, and disable the button while processing.
```

---

### Phương Pháp 2: Chỉnh Sửa Trực Quan Bằng Bút Vẽ (Annotation Mode ✏️)

Khi muốn thay đổi màu sắc, kích thước, khoảng cách hoặc vị trí của một phần tử trên màn hình, **không nên tả bằng lời trong Chat Panel** vì AI dễ hiểu nhầm. Hãy dùng **Bút vẽ ✏️**.

#### Các bước thao tác với Bút vẽ:
1. Nhấp vào biểu tượng **`✏️` (Annotation Mode)** nằm ở thanh công cụ phía dưới màn hình Live Preview.
2. Chọn công cụ **Box (Hình chữ nhật)**.
3. Kéo thả chuột khoanh tròn trực tiếp xung quanh **Nút bấm Phân Tích**.
4. Tại ô mô tả xuất hiện bên cạnh, gõ lệnh:
   ```text
   Make this button forest green, add rounded corners (border-radius 12px), and make font bold.
   ```
5. Bấm **Add to chat** ➔ Bấm **Send**.

```
┌────────────────────────────────────────────────────────┐
│ LIVE PREVIEW                                           │
│  ┌──────────────────────────────────────────────────┐  │
│  │ 🌿 Nhận Diện Cây Thực Địa                        │  │
│  │ ┌──────────────────────────────────────────────┐ │  │
│  │ │ ✏️ [ PHÂN TÍCH ]  ← (Khoanh vùng ở đây)     │ │  │
│  │ └──────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
```

> 💡 **Lưu ý sư phạm:** Khi nào dùng Chat Panel, khi nào dùng Bút vẽ ✏️?  
> - **Chat Panel:** Dùng khi sửa logic xử lý, cấu hình prompt Gemini, thêm trường dữ liệu, xử lý file.  
> - **Bút vẽ (✏️):** Dùng khi sửa màu sắc, font chữ, dời vị trí, sửa khoảng cách margins/padding.

---

#### ✏️ Hoạt động thực hành: Lập Task List 4 Phase cho app của bạn (10 phút)

Điền danh sách việc cần làm để gửi lần lượt vào Chat Panel / Bút vẽ:

```
Phase 1 (UI):       _______________________________________________
Phase 2 (AI Logic): _______________________________________________
Phase 3 (UX):       _______________________________________________
Phase 4 (Error):    _______________________________________________
```

---

## 2.5 Quản Lý Phiên Bản (Checkpoint & Restore)

**⏱ 10 phút**

Trong quá trình vibe coding, đôi khi AI sẽ "hiểu nhầm" câu lệnh và sinh ra mã nguồn làm vỡ toàn bộ giao diện hoặc mất tính năng cũ. **Đừng hoảng loạn!**

### Cơ Chế Checkpoint Tự Động

Mỗi lần bạn gửi 1 câu lệnh trong Chat Panel và AI Studio hoàn thành việc sinh code, hệ thống tự động tạo ra 1 **Checkpoint (Điểm sao lưu)** trong lịch sử chat.

### Thao Tác Phục Hồi (Restore)
1. Cuộn danh sách chat ở cột bên trái lên câu lệnh ở phiên bản ổn định gần nhất.
2. Tìm nút **`Restore`** (hoặc biểu tượng xoay ngược) xuất hiện dưới đoạn tin nhắn đó.
3. Bấm **Restore** ➔ AI Studio sẽ lập tức đưa toàn bộ mã nguồn và giao diện Live Preview quay trở về đúng trạng thái tại thời điểm đó.

> ⚠️ **Lưu ý quan trọng để giữ mã nguồn sạch:**  
> - Không ra quá nhiều yêu cầu phức tạp trong 1 câu lệnh (mỗi lần chỉ sửa 1-2 chi tiết).  
> - Nếu thử ra lệnh 2 lần mà AI vẫn làm sai, hãy bấm **Restore** về bản cũ và viết lại câu lệnh rõ ràng hơn, thay vì tiếp tục cãi nhau với AI trong ô chat.

---

```
════════════════════════════════════════════════════════════════════════════════
🎯 SẢN PHẨM HOÀN THÀNH SAU PHẦN 1 (BUILD):
1. Prototype Version 1 chạy được trực tiếp trên Live Preview.
2. Task List 4 Phase đã được thực thi (Điền vào Hồ Sơ Dự Án — Phần 2).
════════════════════════════════════════════════════════════════════════════════
```

---

# PHẦN 2: KIỂM THỬ, CẢI TIẾN & HOÀN THIỆN (VALIDATE)
> **Mục tiêu:** Đưa ứng dụng qua quy trình kiểm thử 5 lớp, phát hiện và khắc phục hiện tượng ảo giác AI (Fabrication), đảm bảo an toàn sư phạm trước khi xuất bản.

---

## 3.1 Kiểm Thử 5 Lớp & Phát Hiện Lỗi AI Fabrication

**⏱ 25 phút**

Một ứng dụng chạy được trên màn hình chưa chắc đã đủ an toàn để mang vào lớp học. Bạn cần thực hiện **Checklist kiểm thử 5 lớp**:

```
Lớp 1: Happy Path (Chạy chuẩn) ──► Lớp 2: Edge Cases (Trường hợp biên)
 ──► Lớp 3: AI Fabrication Guard (Chống ảo giác AI) ──► Lớp 4: Responsive UI (Thiết bị di động)
  ──► Lớp 5: Security & Privacy (An toàn dữ liệu)
```

---

### Thực Hành Chạy Kiểm Thử 5 Lớp (Test Execution)

#### 🧪 Lớp 1 — Happy Path (Trường hợp lý tưởng)
- **Thao tác:** Upload một bức ảnh lá bàng chụp rõ nét, đủ ánh sáng.
- **Kỳ vọng:** App trả về chính xác: *Tên VN: Cây Bàng*, *Latin: Terminalia catappa*, *Độ tin cậy: Cao*.

#### 🧪 Lớp 2 — Edge Cases (Trường hợp biên)
- **Thao tác:** Upload một bức ảnh mờ, bị tối góc, hoặc ảnh chụp một chiếc ghế nhựa / mặt người.
- **Kỳ vọng:** App không bị vỡ giao diện (crash), không báo lỗi code đỏ.

#### 🧪 Lớp 3 — AI Fabrication Guard (Phát hiện lỗi bịa đặt thông tin)
- **Hiện tượng thực tế:** Khi upload ảnh chiếc ghế nhựa, Gemini Vision cố tình đoán mò và trả về: *"Tên VN: Cây Ghế Nhựa, Họ: Nhựa học, Độ tin cậy: Trung bình"*.
- **Phân tích lỗi:** Đây là hiện tượng **AI Fabrication (Ảo giác / Bịa đặt dữ liệu)**. AI bị ép phải trả về kết quả nên nó tự "sáng tác" thông tin không có thật. Trong giáo dục, điều này cực kỳ nguy hiểm vì làm học sinh tiếp thu kiến thức sai lệch.

#### 🧪 Lớp 4 — Responsive UI (Màn hình di động)
- **Thao tác:** Bấm biểu tượng chuyển đổi góc nhìn di động (Mobile View) trên Live Preview.
- **Phát hiện:** Nút bấm chụp ảnh bị tràn khung, chữ tiêu đề bị đè lên hình ảnh.

#### 🧪 Lớp 5 — Security & Privacy (Dữ liệu học sinh)
- **Kiểm tra:** Đảm bảo app không đòi quyền truy cập micro, không lưu ảnh lên cơ sở dữ liệu công khai, không yêu cầu điền họ tên học sinh.

---

#### ✏️ Hoạt động thực hành: Chạy Checklist kiểm thử 5 lớp cho app của bạn (10 phút)

Ghi nhận kết quả test thực tế vào bảng dưới đây:

| Lớp kiểm thử | Hành động test trên app của bạn | Kết quả (Đạt / Lỗi) | Lỗi phát hiện (nếu có) |
|---|---|---|---|
| 1. Happy Path | _____________________________________ | `[ ] Đạt  [ ] Lỗi` | ___________________ |
| 2. Edge Case | _____________________________________ | `[ ] Đạt  [ ] Lỗi` | ___________________ |
| 3. AI Fabrication | _____________________________________ | `[ ] Đạt  [ ] Lỗi` | ___________________ |
| 4. Responsive UI | _____________________________________ | `[ ] Đạt  [ ] Lỗi` | ___________________ |
| 5. Security/Privacy | _____________________________________ | `[ ] Đạt  [ ] Lỗi` | ___________________ |

---

## 3.2 Sửa Lỗi Thực Tế Sau Kiểm Thử (Bug-Driven Optimization)

**⏱ 25 phút**

> 💡 **Sự khác biệt với Cải tiến ở Module 2:** Cải tiến ở Module 2 là làm theo Task List kế hoạch để dựng khung V1. Cải tiến ở Module 3 là **sửa lỗi thực tế phát sinh sau khi test (Bug-Driven Optimization)** để đưa app đạt chuẩn xuất bản công khai.

---

### Khắc Phục Lỗi AI Fabrication Trong Chat Panel

Để triệt tiêu hiện tượng AI tự sáng tác tên cây khi gặp ảnh không rõ ràng, gửi câu lệnh ép điều kiện khắt khe sau vào Chat Panel:

```text
Update Gemini prompt instructions: If the image is blurry, dark, or not clearly a plant, DO NOT guess or fabricate details. You MUST set name_vn to "Không xác định" and confidence to "Low" with a warning badge saying "Ảnh không rõ ràng, vui lòng chụp lại hoặc hỏi giáo viên".
```

**Thao tác kiểm tra lại (Re-test):** Upload lại ảnh chiếc ghế nhựa ➔ App lập tức hiển thị thẻ màu vàng: *"Tên: Không xác định | Độ tin cậy: Thấp"*. 

✅ **Lỗi Fabrication đã được khắc phục hoàn toàn!**

---

### Sửa Lỗi Responsive Di Động Bằng Bút Vẽ (✏️)

1. Bật giao diện Live Preview ở chế độ Mobile View.
2. Bật công cụ **Bút vẽ ✏️**, khoanh tròn vùng nút bấm bị tràn khung.
3. Gõ lệnh:
   ```text
   Fix responsive layout for mobile screens: make all buttons width 100% with padding 12px, adjust container max-width to 480px centered.
   ```
4. Bấm **Add to chat** ➔ Bấm **Send**.

---

## 3.3 Đánh Giá Chất Lượng & Trạng Thái Release Candidate

**⏱ 20 phút**

Trước khi xuất bản, đối chiếu ứng dụng hiện tại với bản **Product Specification (Phần 1)** và danh sách **Acceptance Criteria**:

### Mẫu Đối Chiếu Cho Ứng Dụng Ví Dụ (Plant ID):
```
[x] Nhận diện đúng ≥ 4 loài cây sân trường phổ biến (Bàng, Phượng, Bằng Lăng, Sứ).
[x] Giao diện responsive hiển thị cân đối trên màn hình điện thoại.
[x] Trả về nhãn "Không xác định" khi ảnh mờ, tối hoặc không chứa cây trồng.
[x] Không bị crash hay vỡ khung khi người dùng thao tác sai.
[x] Chân trang (Footer) dán rõ dòng chữ cảnh báo an toàn sư phạm.
```

---

#### ✏️ Hoạt động thực hành: Tự đánh giá Acceptance Criteria cho app của bạn (5 phút)

Tick vào các tiêu chí app của bạn đã đạt được:

```
[ ] Tiêu chí 1: ___________________________________________________________
[ ] Tiêu chí 2: ___________________________________________________________
[ ] Tiêu chí 3: ___________________________________________________________
[ ] Giao diện responsive chạy mượt trên điện thoại di động
[ ] Đã dán nhãn cảnh báo miễn trừ trách nhiệm / an toàn sư phạm ở chân trang
```

> 💡 **Hướng dẫn xử lý khi chưa đạt:**  
> Nếu còn tiêu chí chưa tick `[ ]`: Copy đúng tiêu chí đó gửi vào Chat Panel kèm câu lệnh:  
> *"Fix the app to ensure this requirement is met: [Tiêu chí chưa đạt]"*.  
> Khi tất cả các tiêu chí đều đạt `[x]`, ứng dụng chính thức đạt trạng thái **Release Candidate (Sẵn sàng xuất bản)**.

---

## 3.4 Đạo Đức AI Trong Giáo Dục — Khung Phân Tích Mô Hình 3 Vai

**⏱ 20 phút**

### Tình Huống Dẫn Dắt

> *Một học sinh sử dụng app nhận diện cây trồng thực địa. Học sinh chụp ảnh một loài nấm dại ngoài sân trường. AI nhận diện sai thành nấm rơm ăn được. Học sinh hái nấm mang về nhà nấu ăn và bị ngộ độc.*

**Ai chịu trách nhiệm trong tình huống này?**

---

### Khung Phân Tích Đạo Đức AI Theo Mô Hình 3 Vai (3-Role Responsible AI Framework)

Để xây dựng một sản phẩm AI an toàn trong môi trường giáo dục, giáo viên cần xem xét trách nhiệm qua 3 vai trò:

```
                  ┌───────────────────────────────┐
                  │ 1. NGƯỜI DÙNG (Học sinh)      │
                  │ Rủi ro tin tuyệt đối vào AI   │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
┌───────────────────────────────┐   ┌───────────────────────────────┐
│ 2. NHÀ PHÁT TRIỂN (Giáo viên) │ ◄─┤ 3. HỆ THỐNG AI (Gemini Studio)│
│ Trách nhiệm cảnh báo & Hướng  │   │ Cấu hình độ tin cậy & Giới    │
│ dẫn tư duy phản biện          │   │ hạn khả năng suy luận         │
└───────────────────────────────┘   └───────────────────────────────┘
```

| Vai trò | Rủi ro / Trách nhiệm | Giải pháp thiết kế trên App |
|---|---|---|
| **1. Người dùng (Học sinh)** | Nguy cơ "mù quáng" tin vào kết quả của AI mà không kiểm chứng thực tế | Thiết kế câu lệnh hướng dẫn học sinh luôn đối chiếu mẫu lá thật với SGK |
| **2. Nhà phát triển (Giáo viên)** | Trách nhiệm sư phạm khi đưa công cụ AI chưa hoàn hảo cho học sinh | Thêm Footer disclaimer: *"Kết quả mang tính tham khảo, bắt buộc xác nhận với GV"* |
| **3. Hệ thống AI (Gemini API)** | Khả năng xảy ra hiện tượng ảo giác (Fabrication) khi thiếu thông tin | Cấu hình Gemini trả về nhãn *"Độ tin cậy: Thấp"* khi thông tin không rõ ràng |

> 💡 **Lưu ý sư phạm:** Công cụ AI trong lớp học **không bao giờ thay thế vai trò của giáo viên hay tri thức trong SGK**. Sản phẩm AI tốt nhất là sản phẩm biết khuyến khích học sinh quay trở lại quan sát thực tế và thảo luận với thầy cô!

---

## 📦 SẢN PHẨM SAU MODULE 2+3

Kết thúc Module 2+3, học viên hoàn thành Phần 2 và Phần 3 trong Hồ Sơ Dự Án:

1. **Ứng dụng Release Candidate** chạy hoàn chỉnh trên Live Preview.
2. **Hồ sơ dự án Phần 2:** Task List 4 Phase hoàn chỉnh.
3. **Hồ sơ dự án Phần 3:** Bảng kết quả kiểm thử 5 lớp + Khung phân tích Đạo đức AI 3 Vai.

---

## 📋 HỒ SƠ DỰ ÁN — PHẦN 2 & PHẦN 3 (Mẫu điền)

```
================================================================================
PHẦN 2: DANH SÁCH VIỆC CẦN LÀM - TASK LIST FOR AI
(Hoàn thành ở Module 2)
================================================================================

- [x] Phase 1 (UI Framework): Master Prompt tạo khung app và vùng upload dropzone.
- [x] Phase 2 (AI Logic): Cài đặt Gemini Vision nhận diện tên cây và trả kết quả JSON tiếng Việt.
- [x] Phase 3 (UX & Effects): Thêm spinner loading "Đang phân tích hình ảnh..." và footer disclaimer.
- [x] Phase 4 (Error Handling & Constraints): Thêm thông báo nếu file upload > 5MB.

================================================================================
PHẦN 3: CHECKLIST KIỂM THỬ & ĐẠO ĐỨC AI
(Hoàn thành ở Module 3)
================================================================================

1. BẢNG KẾT QUẢ KIỂM THỬ THỰC TẾ (Verification Matrix):
   - [x] Lớp 1 (Happy Path): Upload ảnh lá bàng rõ ➔ Hiện đúng tên Cây Bàng, mác "Độ tin cậy: Cao".
   - [x] Lớp 2 (Edge Case): Upload ảnh mặt người/ảnh tối ➔ Hiện "Không xác định", không vỡ app.
   - [x] Lớp 3 (Fabrication Guard): AI không bịa đặt thông tin khi gặp vật thể không phải cây.
   - [x] Lớp 4 (Responsive UI): Giao diện hiển thị vừa vặn trên điện thoại di động.
   - [x] Lớp 5 (Privacy): App không lưu trữ dữ liệu cá nhân hay ảnh của học sinh.

2. KHUNG PHÂN TÍCH ĐẠO ĐỨC AI (3-Role Responsible AI Framework):
   - Người dùng (Học sinh): Rủi ro ngộ nhận ➔ Yêu cầu học sinh đối chiếu kết quả với mẫu thực vật thật.
   - Nhà phát triển (Giáo viên): Trách nhiệm cảnh báo ➔ Dán nhãn miễn trừ trách nhiệm ở chân trang.
   - Hệ thống AI: Kiểm soát ảo giác ➔ Ép Gemini trả nhãn "Độ tin cậy: Thấp" khi thông tin không rõ.
```

---

*Module 2+3 — Phiên bản 1.1 | Khoá học: Phát Triển Ứng Dụng Với AI*
