# **MODULE 1: LẬP KẾ HOẠCH PHÁT TRIỂN SẢN PHẨM AI**

*Trong module này, các bạn sẽ tìm hiểu các nội dung:*

- *1.1. AI Trong Giáo Dục, Vibe Coding (Lập Trình Bằng Ngôn Ngữ Tự Nhiên) & Xác Định Bài Toán*
- *1.2. Xác Định Yêu Cầu Sản Phẩm (Requirements)*
- *1.3. Thiết Kế Sản Phẩm AI (Design)*
- *1.4. Viết Product Specification (Bản Đặc Tả Chi Tiết Sản Phẩm)*
- *1.5. Những Điểm Cốt Lõi*

---

> **⏱ Thời lượng:** 90 phút  
> **🎯 Mục tiêu:** Xác định được bài toán, yêu cầu, và hoàn thành bản đặc tả sản phẩm trước khi xây dựng.  
> **📦 Sản phẩm đầu ra:** Bản tóm tắt sản phẩm (Product Brief) + Bản đặc tả chi tiết (Product Specification) + Bản phác thảo giao diện (UI Wireframe) — Điền vào **Hồ Sơ Dự Án — Phần 1**.

---

## **1.1. AI Trong Giáo Dục, Vibe Coding (Lập Trình Bằng Ngôn Ngữ Tự Nhiên) & Xác Định Bài Toán**

**⏱ 25 phút**

### 1.1.1. Năng Lực AI Hiện Đại Trong Dạy Học

AI thế hệ mới không còn là công cụ chỉ dành cho lập trình viên. Hai công nghệ cốt lõi đang thay đổi cách giáo viên có thể tạo ra học liệu và trợ lý học tập:

| Công nghệ | Khả năng | Ứng dụng trong lớp học |
|---|---|---|
| **Mô hình ngôn ngữ lớn (LLM - Large Language Model)** | Hiểu và sinh văn bản, giải thích khái niệm, ra câu hỏi, chấm bài tự luận | Trợ lý câu hỏi ôn tập, chatbot hỗ trợ học sinh |
| **Thị giác máy tính đa phương thức (Multimodal Vision)** | Nhìn thấy và phân tích ảnh, video, sơ đồ | Nhận diện vật thể, phân tích bài làm có hình ảnh, thực địa Sinh học |

Điều đặc biệt: **Bạn không cần biết lập trình để sử dụng cả hai công nghệ trên.** Đây là điểm mấu chốt của khoá học này.

---

### 1.1.2. Vibe Coding (Lập Trình Bằng Ngôn Ngữ Tự Nhiên) Là Gì & Tại Sao Giáo Viên STEM Cần Biết?

> **Khái niệm do Andrej Karpathy — nhà khoa học AI của Tesla và OpenAI — đặt ra năm 2025.**

**Vibe Coding (Lập trình theo cảm hứng/mô tả tự nhiên)** là cách lập trình mới: bạn *mô tả điều bạn muốn* bằng ngôn ngữ tự nhiên, để AI tự sinh ra toàn bộ mã nguồn. Bạn không đọc từng dòng mã lệnh (code). Bạn nhìn kết quả, điều chỉnh theo cảm nhận, và để AI tiếp tục xây dựng.

> *"Just vibe with the AI. Forget that the code even exists."*  
> *(Hãy cứ tương tác tự nhiên với AI. Hãy quên đi sự tồn tại của mã lệnh.)* — Andrej Karpathy

#### Tại Sao Giáo Viên STEM Cần Biết Điều Này?

Vibe Coding phá vỡ rào cản cuối cùng giữa ý tưởng sư phạm và sản phẩm công nghệ:

```
Trước đây:   Ý tưởng GV → Thuê lập trình viên → Chờ 3–6 tháng → Sản phẩm
Vibe Coding: Ý tưởng GV → Mô tả bằng tiếng Việt → AI sinh app → Chạy ngay hôm nay
```

Bạn — người hiểu rõ nhất học sinh mình cần gì — nay có thể **trực tiếp chuyển hoá ý tưởng sư phạm thành sản phẩm chạy thật**, không qua trung gian.

#### Nhưng Vibe Coding Có Một Điểm Yếu Chết Người

Vibe Coding mạnh khi bạn biết **mình muốn gì**. Nhưng nếu bạn chỉ *"cảm giác muốn cái gì đó hữu ích"* — AI sẽ đoán mò và cho ra sản phẩm không ai dùng được.

---

### 1.1.3. Trình Diễn Trực Tiếp (Live Demo) So Sánh — Vibe Code Bừa vs Spec-First Vibe Coding (Lập Trình Có Bản Đặc Tả)

> **Mục đích:** Cho học viên thấy tận mắt sự khác biệt giữa lập trình bừa theo cảm tính và lập trình có bản đặc tả (Spec-first).

#### Trình Diễn A (Demo A) — Vibe Coding Không Có Kế Hoạch

**Lệnh gõ vào AI Studio (Chế độ xây dựng ứng dụng):**
```
Tạo cho tôi app nhận diện cây
```

**Kết quả thực tế:** AI Studio tự động tách thành nhiều thành phần giao diện rời (`CameraCapture.tsx` - Nút chụp ảnh, `PlantDetails.tsx` - Chi tiết cây, `HistoryList.tsx` - Lịch sử tra cứu) kèm cẩm nang chăm sóc cây cảnh đa tab — rất hoành tráng nhưng **dư thừa tính năng và lạc đề** hoàn toàn so với bài học thực địa Sinh học THCS.

> Kết quả: AI tưởng bạn làm ứng dụng chăm sóc cây cảnh trong nhà, không có tính năng chụp ảnh ngoài trời, không có thông tin khoa học chuẩn môn Sinh học.

#### Trình Diễn B (Demo B) — Spec-first Vibe Coding (Lập Trình Theo Bản Đặc Tả)

**Trước khi gõ lệnh, giáo viên đã chuẩn bị bản đặc tả:**
- *Người dùng mục tiêu (Target User):* Học sinh lớp 6 ngoài sân trường
- *Đầu vào (Input):* Ảnh chụp lá cây từ điện thoại
- *Đầu ra (Output):* Tên tiếng Việt, tên khoa học, mô tả 2 câu, thang độ tin cậy
- *Ràng buộc (Constraints):* Không đăng nhập, không lưu dữ liệu

**Lệnh gõ vào AI Studio (Lệnh điều khiển tối ưu - Master Prompt gồm 5 thành phần):**
```
Build a Plant Identifier web app for Vietnamese secondary school biology field trips.
Allow students to upload an image or take a photo of a plant/leaf outside the schoolyard.
Call Gemini Vision to analyze and return ONLY: name_vn (Vietnamese name),
scientific_name (Latin name), family (Plant family), description (2 short sentences),
confidence_level (High/Medium/Low).
Display results in a single-page clean card layout with forest green header,
NO unnecessary indoor gardening care features (no watering, fertilizer, or soil info),
and a disclaimer "Results for reference only, check with teacher".
```

**Kết quả thực tế:** Chỉ có **1 file giao diện duy nhất (`App.tsx`)**, hiển thị đúng 5 trường chuẩn bài học Sinh học THCS, không có bất kỳ tính năng thừa nào.

> Kết quả: Mất 5 phút chuẩn bị bản đặc tả (Spec) + 3 phút xây dựng (Build) = Ứng dụng chạy thật, đúng yêu cầu.

---

### 1.1.4. Triết Lý Khoá Học & Xác Định Bài Toán Thực Tế

> **Khoá học này không dạy lập trình thủ công. Khoá học này dạy bạn Spec-first Vibe Coding (Lập trình bằng AI dựa trên bản đặc tả trước).**

```
Bài toán → Yêu cầu → Bản đặc tả (Spec) → Lập trình với AI (Vibe Code) → Đánh giá → Cải tiến → Triển khai
```

Spec-first Vibe Coding = Biết mình muốn gì (Spec) + Để AI thực hiện (Vibe Code).  
Hai phần này không thể tách rời. **Module 1 dạy phần lập kế hoạch và đặc tả. Module 2+3 dạy phần xây dựng và kiểm thử.**

---

#### Xác Định Bài Toán Thực Tế

Trước khi viết bất cứ đặc tả nào, bạn cần trả lời 3 câu hỏi nền tảng:

| Câu hỏi | Ví dụ minh hoạ (Plant ID) |
|---|---|
| **Ai gặp vấn đề?** | Học sinh lớp 6 khi học thực địa Sinh học ngoài sân trường |
| **Vấn đề là gì?** | Không nhớ tên cây, không mang sách giáo khoa, dễ tra cứu nhầm |
| **Dùng AI có phù hợp không?** | Rất phù hợp — AI Vision nhận diện ảnh tức thì, không cần kết nối cơ sở dữ liệu lớn |

> 💡 **Lăng kính kỹ thuật**  
> *Câu hỏi thứ ba thường bị bỏ qua. Không phải bài toán nào cũng cần AI. Nếu câu trả lời là "một tờ phiếu bài tập in sẵn cũng giải quyết được" — thì không cần xây app.*

* **Thử thách 1**: Điền vào ô bên dưới cho bài toán của **chính bạn**:

```
Ai gặp vấn đề?    _______________________________________________
Vấn đề là gì?     _______________________________________________
Dùng AI có phù hợp không?  _______________________________________________
Lý do:            _______________________________________________
```

---

## **1.2. Xác Định Yêu Cầu Sản Phẩm (Requirements)**

**⏱ 25 phút**

> 💡 **Lăng kính kỹ thuật**  
> *Câu nói "Tôi muốn làm app AI hỗ trợ học sinh ôn tập" KHÔNG PHẢI là yêu cầu sản phẩm — đó chỉ là ý tưởng mơ hồ. Nếu bạn gõ câu này vào Google AI Studio, AI sẽ tự đoán và sinh ra một ứng dụng... rất có thể không giống những gì bạn hình dung (đây chính là Demo A bạn vừa thấy). Yêu cầu thực sự phải bóc tách thành 5 thành phần rõ ràng sau đây.*

---

### 1.2.1. Người Dùng Mục Tiêu (Target User)

**Câu hỏi định hướng:** Ai sẽ dùng ứng dụng này? Trong hoàn cảnh nào?

Mô tả càng cụ thể càng tốt — vì AI sẽ dùng thông tin này để thiết kế giao diện người dùng (UI) phù hợp với ngữ cảnh thực tế.

| Mô tả chung chung (không dùng) | Mô tả cụ thể (nên dùng) |
|---|---|
| "Học sinh" | "Học sinh lớp 6 THCS, dùng điện thoại Android ngoài sân trường, ánh sáng thay đổi" |
| "Giáo viên" | "Giáo viên Vật Lý THPT, soạn bài trên laptop tại nhà, không rành công nghệ" |

**Ví dụ (Plant ID - App Nhận diện cây):** Học sinh lớp 6 THCS, sử dụng điện thoại di động khi tham gia tiết học thực địa Sinh học ngoài sân trường.

---

### 1.2.2. Dữ Liệu Đầu Vào (Input)

**Câu hỏi định hướng:** Người dùng đưa thông tin gì vào ứng dụng? Định dạng là gì? Giới hạn ra sao?

Thường là: văn bản, hình ảnh, tập tin, âm thanh, hoặc lựa chọn từ danh sách.

**Ví dụ (Plant ID):** Ảnh chụp lá cây hoặc toàn cây từ camera điện thoại. Định dạng JPG/PNG. Dung lượng tối đa 5MB.

---

### 1.2.3. Kết Quả Đầu Ra (Output)

**Câu hỏi định hướng:** Ứng dụng sẽ trả về thông tin gì? Trình bày như thế nào?

Định nghĩa từng trường thông tin cụ thể — đây là phần quan trọng nhất để AI không tự ý sáng tác thêm tính năng thừa.

**Ví dụ (Plant ID):**
- Tên tiếng Việt (VD: Cây Bàng)
- Tên khoa học Latin (VD: Terminalia catappa)
- Họ thực vật (VD: Combretaceae)
- Mô tả đặc điểm (2 câu ngắn gọn, ngôn ngữ phù hợp học sinh lớp 6)
- Mức độ tin cậy: Cao / Trung bình / Thấp (Confidence Level)

---

### 1.2.4. Chức Năng Cốt Lõi (Core Features)

**Câu hỏi định hướng:** Ứng dụng cần có những nút bấm/tính năng chính nào để người dùng thao tác?

Liệt kê từng tính năng dưới dạng động từ hành động.

**Ví dụ (Plant ID):**
- Khung xem ảnh tải lên (Kéo thả ảnh drag-drop hoặc nút chọn file)
- Nút "Phân Tích" kích hoạt mô hình Gemini Vision API
- Thẻ kết quả hiển thị thông tin phân tích
- Nút "Chụp lại" để xoá kết quả cũ và bắt đầu lại
- Thanh trạng thái chờ xử lý (Loading state: "Đang phân tích...")

---

### 1.2.5. Ràng Buộc Kỹ Thuật & Đạo Đức (Constraints)

**Câu hỏi định hướng:** Ứng dụng **KHÔNG ĐƯỢC** làm gì? Giới hạn kỹ thuật và an toàn dữ liệu là gì?

Đây là phần giúp bạn kiểm soát rủi ro — đặc biệt quan trọng với quyền riêng tư của học sinh.

**Ví dụ (Plant ID):**
- Không lưu trữ ảnh hoặc dữ liệu cá nhân của học sinh
- Không yêu cầu đăng nhập tài khoản
- Không nhận file ảnh dung lượng lớn hơn 5MB
- Không trả về tên cây khi AI không đủ tin cậy (phải hiển thị "Không xác định")

> 💡 **Lăng kính kỹ thuật**  
> *Ràng buộc sản phẩm (Constraints) thường bị bỏ sót vì học viên tập trung vào "muốn làm gì" hơn là "không được làm gì". Nhưng trong môi trường giáo dục, ràng buộc về quyền riêng tư học sinh là bắt buộc về mặt pháp lý và đạo đức.*

---

### 1.2.6. Hoạt Động Thực Hành Soạn Thảo Yêu Cầu Sản Phẩm

* **Thử thách 2**: Điền bảng 5 thành phần yêu cầu cho bài toán của bạn:

```
1. Người dùng mục tiêu (Target User):
   _______________________________________________

2. Dữ liệu đầu vào (Input):
   _______________________________________________

3. Kết quả đầu ra (Output) — liệt kê từng trường:
   - _______________________________________________
   - _______________________________________________
   - _______________________________________________

4. Chức năng cốt lõi (Core Features):
   - _______________________________________________
   - _______________________________________________
   - _______________________________________________

5. Ràng buộc kỹ thuật & đạo đức (Constraints) — những gì app KHÔNG ĐƯỢC làm:
   - Không _______________________________________________
   - Không _______________________________________________
```

---

## **1.3. Thiết Kế Sản Phẩm AI (Design)**

**⏱ 25 phút**

> 💡 **Lăng kính kỹ thuật**  
> *Nhiều người nghĩ thiết kế là vẽ giao diện đẹp. Thiết kế thực sự là quyết định luồng di chuyển dữ liệu (Data Flow) và trải nghiệm người dùng (UX) trước khi viết bất kỳ dòng lệnh nào. Bước này giúp bạn ra lệnh cho AI (vibe code) đúng hướng, không bị lạc trong các lệnh sửa đổi vô tận.*

### 1.3.1. Thiết Kế Luồng Hoạt Động (Data Flow - Luồng Dữ Liệu)

Vẽ sơ đồ mô tả dữ liệu di chuyển từ đầu vào (Input) qua AI xử lý đến kết quả đầu ra (Output) như thế nào. Dùng mũi tên đơn giản — không cần phần mềm phức tạp.

**Ví dụ (Plant ID - Luồng dữ liệu nhận diện cây):**

```
[Người dùng chụp/upload ảnh]
         ↓
[App hiển thị trạng thái "Đang phân tích..."]
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

* **Thử thách 3**: Phác thảo sơ đồ luồng dữ liệu (Data Flow) của bạn (5 phút) — Dùng giấy hoặc gõ ngay vào Hồ sơ dự án.

---

### 1.3.2. Thiết Kế Giao Diện (UI Wireframe - Phác Thảo Bố Cục)

Phác thảo bố cục màn hình chính (UI Wireframe - Bản phác thảo giao diện). Đây sẽ là "bản vẽ kiến trúc" mà bạn mô tả cho AI khi lập trình bằng tiếng Việt.

**Ví dụ (Plant ID) — Bản phác thảo giao diện 1 màn hình:**

```
┌─────────────────────────────────┐
│  Nhận Diện Cây Thực Địa        │  ← Header: tiêu đề ứng dụng
│  [Sinh học lớp 6 - THCS]       │
├─────────────────────────────────┤
│                                 │
│   [ Chụp ảnh / Upload ảnh ]    │  ← Vùng upload lớn, dễ bấm
│   [ Kéo thả ảnh vào đây ]      │
│                                 │
├─────────────────────────────────┤
│         [ PHÂN TÍCH ]          │  ← Nút bấm lớn kích hoạt AI
├─────────────────────────────────┤
│  Đang phân tích hình ảnh...    │  ← Trạng thái chờ (Loading)
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

### 1.3.3. Thiết Kế Trải Nghiệm Người Dùng (UX - User Experience theo 4 Tiêu Chí Microsoft)

Microsoft định nghĩa trải nghiệm người dùng tốt (UX - User Experience) qua 4 tiêu chí cốt lõi. Đây là bộ công cụ để bạn tự đánh giá sản phẩm trước khi mang vào lớp học:

| Tiêu chí | Câu hỏi kiểm tra | Áp dụng vào ứng dụng Plant ID |
|---|---|---|
| **Useful — Có ích** | Ứng dụng có giải quyết đúng bài toán thực tế không? | Phục vụ trực tiếp việc ghi bài thu hoạch thực địa Sinh học |
| **Reliable — Đáng tin cậy** | AI có trung thực thông báo khi không chắc chắn không? | Hiển thị "Độ tin cậy: Thấp" kèm lời khuyên hỏi GV |
| **Accessible — Dễ tiếp cận** | Học sinh không giỏi công nghệ có dễ dùng không? | Nút chụp to ở trung tâm, không cần đăng nhập |
| **Pleasant — Dễ chịu** | Giao diện có thân thiện, phù hợp ngữ cảnh không? | Tông xanh lá mộc mạc, font chữ to dễ đọc ngoài trời nắng |

> 💡 **Lăng kính kỹ thuật**  
> *Tiêu chí Reliable (Đáng tin cậy) đặc biệt quan trọng với ứng dụng giáo dục. AI không bao giờ được trả lời chắc chắn khi thực ra đang đoán mò — điều này rèn luyện cho học sinh tư duy phản biện với công nghệ AI.*

* **Thử thách 4**: Tự đánh giá ý tưởng của bạn theo 4 tiêu chí UX (5 phút):

```
Useful (Có ích)         — App của tôi giải quyết bài toán: __________
Reliable (Đáng tin)     — App sẽ xử lý khi không chắc chắn bằng cách: __________
Accessible (Dễ dùng)   — Người dùng dễ dàng thao tác vì: __________
Pleasant (Dễ chịu)      — Giao diện phù hợp ngữ cảnh vì: __________
```

---

## **1.4. Viết Product Specification (Bản Đặc Tả Chi Tiết Sản Phẩm)**

**⏱ 15 phút**

Product Specification là tài liệu tổng hợp **Bài toán + Yêu cầu + Thiết kế** thành 1 trang có cấu trúc. Đây là thứ bạn sẽ đưa cho AI để bắt đầu vibe code ở Module 2.

> 💡 **Lăng kính kỹ thuật**  
> *Product Specification không phải là tài liệu kỹ thuật dày hàng trăm trang. Đối với khoá học này, Spec chỉ cần đủ để trả lời: "Nếu AI đọc tờ này, nó có biết cần làm gì không?"*

### 1.4.1. Cấu Trúc Bản Đặc Tả Sản Phẩm (Product Specification - 5 Thành Phần)

**1. Mô tả sản phẩm (Product Description - Tổng quan ứng dụng)**  
1–2 câu mô tả ngắn gọn ứng dụng làm gì và phục vụ cho đối tượng nào.

**2. Phạm vi phiên bản 1 (Scope v1 - Các chức năng thực hiện)**  
Những chức năng ứng dụng SẼ thực hiện trong phiên bản đầu tiên.

**3. Ngoài phạm vi thực hiện (Out of Scope - Các chức năng chưa làm)**  
Những chức năng ứng dụng KHÔNG làm trong v1 — nhằm đặt kỳ vọng đúng cho giáo viên và hướng dẫn AI không làm thừa.

**4. Yêu cầu chi tiết (Detailed Requirements - 5 thành phần cốt lõi)**  
5 thành phần yêu cầu đã chuẩn bị ở mục 1.2 (Target User - Người dùng, Input - Đầu vào, Output - Đầu ra, Core Features - Chức năng cốt lõi, Constraints - Ràng buộc).

**5. Tiêu chí nghiệm thu sản phẩm (Acceptance Criteria - Điều kiện kiểm thử)**  
Danh sách kiểm tra cụ thể: "Ứng dụng đạt chuẩn khi..." — đây là thước đo bạn sử dụng ở Module 3 để nghiệm thu sản phẩm.

---

### 1.4.2. Ví Dụ Bản Đặc Tả Sản Phẩm Hoàn Chỉnh (Plant ID Spec)

```
══════════════════════════════════════════════════════════════
PRODUCT SPECIFICATION (BẢN ĐẶC TẢ SẢN PHẨM)
Ứng Dụng Nhận Diện Cây Trồng Thực Địa
Phiên bản: v1.0 | Ngày soạn: ___________
══════════════════════════════════════════════════════════════

1. MÔ TẢ SẢN PHẨM (Product Description)
   Ứng dụng AI hỗ trợ học sinh lớp 6 nhận diện tên cây trồng bằng
   cách chụp ảnh từ điện thoại, phục vụ bài học thực địa Sinh học.

2. PHẠM VI PHIÊN BẢN 1 (Scope v1 - Tính năng SẼ làm)
   - Nhận ảnh tải lên (upload) hoặc chụp trực tiếp từ camera điện thoại
   - Phân tích qua Gemini Vision API và trả về kết quả 5 trường chuẩn
   - Hiển thị thông báo cảnh báo khi độ tin cậy của AI ở mức thấp
   - Giao diện tối ưu di động (mobile-first - thiết kế ưu tiên màn hình điện thoại), 1 màn hình duy nhất

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

* **Thử thách 5**: Hoàn thành bản đặc tả sản phẩm (Product Specification) của bạn (10 phút) — Dùng mẫu trên và điền vào Hồ Sơ Dự Án — Phần 1.

---

## **1.5. Những Điểm Cốt Lõi**

* **Spec-first Vibe Coding là chìa khóa:** Đừng bắt đầu gõ mã lệnh (code) hoặc câu lệnh điều khiển (prompt) khi chưa chuẩn bị Bản đặc tả sản phẩm (Product Specification) rõ ràng.
* **Nắm vững 5 thành phần Yêu cầu (Requirements):** Người dùng mục tiêu (Target User), Dữ liệu đầu vào (Input), Kết quả đầu ra (Output), Chức năng cốt lõi (Core Features) và Ràng buộc kỹ thuật & đạo đức (Constraints).
* **Ràng buộc (Constraints) bảo vệ sản phẩm:** Luôn đặt giới hạn để AI không tự ý sáng tác thêm các tính năng không cần thiết.
* **Thiết kế trải nghiệm người dùng (UX) trước khi xây dựng:** Tuân thủ 4 tiêu chí Có ích (Useful), Đáng tin cậy (Reliable), Dễ tiếp cận (Accessible) và Dễ chịu (Pleasant) của Microsoft.
* **Tiêu chí nghiệm thu (Acceptance Criteria):** Thước đo chính xác để kiểm thử và nghiệm thu sản phẩm ở Module 3.

---

## SẢN PHẨM SAU MODULE 1

Kết thúc Module 1, bạn phải có đủ 3 sản phẩm dưới đây trong Hồ Sơ Dự Án — Phần 1:

| Sản phẩm | Mô tả chi tiết | Kiểm tra |
|---|---|---|
| **Bản tóm tắt sản phẩm (Product Brief)** | 3 câu hỏi nền tảng (Ai gặp vấn đề? Vấn đề gì? AI có phù hợp không?) | `[ ]` |
| **Bản đặc tả chi tiết (Product Specification)** | 5 thành phần yêu cầu + Phạm vi (Scope v1) + Ngoài phạm vi (Out of Scope) + Tiêu chí nghiệm thu (Acceptance Criteria) | `[ ]` |
| **Phác thảo giao diện (UI Wireframe)** | Bản phác thảo bố cục 1 màn hình ứng dụng (vẽ tay hoặc mô tả văn bản) | `[ ]` |

> **Bàn giao sang Module 2:** Bạn sẽ dùng **Bản đặc tả sản phẩm (Product Specification)** này làm đầu vào để soạn Master Prompt (Lệnh điều khiển tối ưu), khởi động chế độ xây dựng (Build Mode) trên Google AI Studio và bắt đầu quy trình lập trình bằng AI (Vibe Coding) trực tiếp. Bản đặc tả không rõ ràng = sản phẩm AI sinh ra sẽ bị lạc hướng.

---

## HỒ SƠ DỰ ÁN — PHẦN 1 (Mẫu điền)

> Sao chép mẫu này vào Google Doc của bạn và điền vào trong suốt Module 1.

```
══════════════════════════════════════════════════════════════
HỒ SƠ DỰ ÁN: [Tên Ứng Dụng (App) của bạn]
Họ và tên GV: ____________ | Trường: ____________ | Môn: ____________
══════════════════════════════════════════════════════════════

PHẦN 1: BÀI TOÁN, YÊU CẦU & ĐẶC TẢ SẢN PHẨM (PRODUCT SPECIFICATION)
(Hoàn thành ở Module 1)

──────────────────────────────────────────────────────────────
A. BÀI TOÁN THỰC TẾ (Problem & Context - Ngữ cảnh & Bài toán)
──────────────────────────────────────────────────────────────
Ai gặp vấn đề?   _______________________________________________
Vấn đề là gì?    _______________________________________________
AI phù hợp vì?   _______________________________________________

──────────────────────────────────────────────────────────────
B. YÊU CẦU SẢN PHẨM (Requirements - 5 Thành phần cốt lõi)
──────────────────────────────────────────────────────────────
1. Người dùng mục tiêu (Target User):
   _______________________________________________

2. Dữ liệu đầu vào (Input):
   _______________________________________________

3. Kết quả đầu ra (Output) — liệt kê từng trường:
   - _______________________________________________
   - _______________________________________________
   - _______________________________________________

4. Chức năng cốt lõi (Core Features):
   - _______________________________________________
   - _______________________________________________
   - _______________________________________________

5. Ràng buộc kỹ thuật & đạo đức (Constraints):
   - Không _______________________________________________
   - Không _______________________________________________

──────────────────────────────────────────────────────────────
C. THIẾT KẾ SẢN PHẨM (Design & UX - Luồng dữ liệu & Giao diện)
──────────────────────────────────────────────────────────────
Luồng dữ liệu (Data Flow):
[Input - Đầu vào] → [Xử lý AI] → [Output - Đầu ra]

Bản phác thảo giao diện (UI Wireframe - Mô tả bố cục màn hình):
_______________________________________________

Trải nghiệm người dùng (UX - 4 tiêu chí Microsoft):
- Useful (Có ích)         : _______________________________________________
- Reliable (Đáng tin cậy) : _______________________________________________
- Accessible (Dễ dùng)   : _______________________________________________
- Pleasant (Dễ chịu)      : _______________________________________________

──────────────────────────────────────────────────────────────
D. TIÊU CHÍ NGHIỆM THU (Acceptance Criteria - Điều kiện ĐẠT)
──────────────────────────────────────────────────────────────
[ ] _______________________________________________
[ ] _______________________________________________
[ ] _______________________________________________
[ ] Giao diện hiển thị tự động tối ưu (responsive) trên điện thoại
[ ] Xử lý đúng trường hợp dữ liệu đầu vào không hợp lệ
```

---

*Module 1 — Phiên bản 1.0 | Khoá học: Phát Triển Ứng Dụng Với AI*

