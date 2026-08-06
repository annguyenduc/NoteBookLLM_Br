# BỘ KỊCH BẢN DEMO & HƯỚNG DẪN THỰC HÀNH CHI TIẾT
## Khóa Học: Phát Triển Sản Phẩm AI Cho Giáo Viên STEM Bằng Google AI Studio
### Đi Kèm Tài Liệu Thiết Kế Module `module_spec_kit_ai_studio.md` (v2.5)

> **Mục đích tài liệu:** Cung cấp script thoại, câu lệnh prompt chính xác, thao tác từng bước và phản hồi kỳ vọng cho TOÀN BỘ các bài demo & thực hành từ Module 1 đến Module 4 theo quy trình Spec-first (*Problem ➔ Requirements ➔ Specification ➔ Build ➔ Validate ➔ Deploy*).
>
> **Ngày phát hành:** 2026-07-22 | **Phiên bản:** 2.5

---

## 📑 MỤC LỤC KỊCH BẢN DEMO

1. [MODULE 1: LẬP KẾ HOẠCH PHÁT TRIỂN SẢN PHẨM AI](#-module-1-lập-kế-hoạch-phát-triển-sản-phẩm-ai)
   - [1.1. Demo So Sánh: Demo A vs. Demo B](#11-demo-so-sánh-trực-tiếp-từ-2-sản-phẩm-thực-tế-demo-a-vs-demo-b)
   - [1.2. Demo Bóc Tách Yêu Cầu (Requirements Extraction)](#12-demo-bóc-tách-yêu-cầu-requirements-extraction)
2. [MODULE 2: XÂY DỰNG ỨNG DỤNG VỚI GOOGLE AI STUDIO BUILD MODE](#-module-2-xây-dựng-ứng-dụng-với-google-ai-studio-build-mode)
   - [2.1. Demo Khởi Tạo Dự Án & Sinh Prototype V1](#21-demo-khởi-tạo-dự-án--sinh-prototype-v1)
   - [2.2. Demo Đánh Giá Kết Quả (Review) & Lập Task List](#22-demo-đánh-giá-kết-quả-review--lập-task-list)
   - [2.3. Demo Cải Tiến Theo Vòng Lặp Bằng Chat Panel & Bút Vẽ (✏️)](#23-demo-cải-tiến-theo-vòng-lặp-bằng-chat-panel--bút-vẽ-)
3. [MODULE 3: KIỂM THỬ, CẢI TIẾN & HOÀN THIỆN ỨNG DỤNG AI](#-module-3-kiểm-thử-cải-tiến--hoàn-thiện-ứng-dụng-ai)
   - [3.1. Demo Kiểm Thử 5 Lớp & Phát Hiện Lỗi AI Fabrication](#31-demo-kiểm-thử-5-lớp--phát-hiện-lỗi-ai-fabrication)
   - [3.2. Demo Sửa Lỗi Thực Tế Sau Kiểm Thử (Bug-Driven Optimization)](#32-demo-sửa-lỗi-thực-tế-sau-kiểm-thử-bug-driven-optimization)
   - [3.3. Demo Thảo Luận Tình Huống Đạo Đức AI Theo Mô Hình 3 Vai](#33-demo-thảo-luận-tình-huống-đạo-đức-ai-theo-mô-hình-3-vai)
4. [MODULE 4: TRIỂN KHAI ỨNG DỤNG AI VÀO GIẢNG DẠY](#-module-4-triển-khai-ứng-dụng-ai-vào-giảng-dạy)
   - [4.1. Thao Tác Deploy 1-Click Lên Internet (Public URL)](#41-thao-tác-deploy-1-click-lên-internet-public-url)
   - [4.2. Kịch Bản Thuyết Trình Mẫu Trong Demo Day (3 Phút)](#42-kịch-bản-thuyết-trình-mẫu-trong-demo-day-3-phút)

---

---

# 📌 MODULE 1: LẬP KẾ HOẠCH PHÁT TRIỂN SẢN PHẨM AI

### 1.1. Demo So Sánh Trực Tiếp Từ 2 Sản Phẩm Thực Tế (Demo A vs. Demo B)
* **Mục tiêu:** So sánh mã nguồn và giao diện thực tế của 2 file ZIP xuất ra từ AI Studio: `nhận-diện-cây-xanh.zip` (Demo A - Prompt ngắn) và `plant-identifier.zip` (Demo B - Có Kế hoạch & Đặc tả) để thấy rõ sự khác biệt giữa App mặc định và App tùy biến theo đặc tả.

* **🔴 DEMO A — Prompt ngắn (`nhận-diện-cây-xanh.zip`):**  
  * **Thao tác:** Truy cập `https://aistudio.google.com/apps` → Click **+ New app** → Dán câu lệnh:
    ```text
    Tạo cho tôi app nhận diện cây
    ```
  * **Đặc điểm:** AI Studio tự động tách thành các component rời (`CameraCapture.tsx`, `PlantDetails.tsx`, `HistoryList.tsx`) và cẩm nang chăm sóc cây cảnh đa tab. Rất hoành tráng nhưng **bị thừa vãi tính năng & lạc đề** so với bài học thực địa Sinh học THCS.

* **🟢 DEMO B — Có Kế hoạch & Master Prompt đầy đủ (`plant-identifier.zip`):**  
  * **Thao tác:** Click **+ New app** mở workspace mới → Dán Master Prompt đầy đủ:
    ```text
    Build a Plant Identifier web app for Vietnamese secondary school biology field trips.
    Allow students to upload an image or take a photo of a plant/leaf outside the schoolyard.
    Call Gemini Vision to analyze and return ONLY: name_vn (Vietnamese name), scientific_name (Latin name), family (Plant family), description (2 short sentences describing features), confidence_level (High/Medium/Low).
    Display results in a single-page clean card layout with forest green header, NO unnecessary indoor gardening care features (no watering, fertilizer, or soil info), and a disclaimer "Results for reference only, check with teacher".
    ```
  * **Đặc điểm:** Chỉ có **1 file giao diện duy nhất (`src/App.tsx`)**, hiển thị đúng 5 trường chuẩn bài học Sinh học THCS.

* **Lời thoại chốt của Giảng viên:**
  > *"Thầy cô quan sát nhé: Khi gõ prompt ngắn (Demo A), AI Studio tự sinh ra 1 loạt Component và cẩm nang tưới nước vì nó tưởng ta làm app cây cảnh trong nhà. Khi ta đưa bản lập kế hoạch & đặc tả chuẩn vào (Demo B), ta ép AI Studio thu gọn lại thành 1 file duy nhất với 5 trường dữ liệu chuẩn môn Sinh học, cắt bỏ mọi component thừa thãi. Việc lập kế hoạch phát triển giúp ta kiểm soát phạm vi sản phẩm!"*

---

### 1.2. Demo Bóc Tách Yêu Cầu (Requirements Extraction)
* **Mục tiêu:** Hướng dẫn học viên chuyển đổi một mong muốn mơ hồ (VD: *"Tôi muốn làm app nhận diện thực vật"*) thành bảng Yêu cầu 5 thành phần chuẩn xác.
* **Kịch bản thực hành:**
  * Trainer đưa ra câu nói mơ hồ: *"Giáo viên muốn có một app hỗ trợ học sinh học Sinh học ngoài sân trường"*.
  * Trainer hướng dẫn GV điền vào Hồ sơ dự án Google Doc:
    1. **Người dùng:** Học sinh lớp 6 THCS.
    2. **Đầu vào:** Ảnh chụp lá cây/toàn cây từ điện thoại.
    3. **Đầu ra:** Tên tiếng Việt, tên Latin, mô tả ngắn 2 câu, thang độ tin cậy.
    4. **Chức năng chính:** Khung xem ảnh, nút Phân Tích, thẻ hiển thị kết quả, nút Chụp lại.
    5. **Ràng buộc (Constraints):** Không lưu dữ liệu cá nhân học sinh, không cần đăng nhập, file ảnh < 5MB.

---

---

# 📌 MODULE 2: XÂY DỰNG NGUYÊN MẪU VỚI GOOGLE AI STUDIO BUILD MODE

### 2.1. Demo Khởi Tạo Dự Án & Sinh Prototype V1
* **Thao tác:**
  1. Mở `https://aistudio.google.com/apps` ➔ Click **+ New app**.
  2. Trước khi bấm Build, tích chọn các AI Chips mong muốn (VD: tick chọn *Google Search* và *Image Gen*).
  3. Nhập Master Prompt 5 thành phần vào ô *"Build your ideas with Gemini"*:
     ```text
     Build a Plant Identifier web app for Vietnamese secondary school students.
     1. App type: Single-page web app for biology field trips.
     2. Core Feature: Allow users to upload an image of a plant/leaf or take a photo.
     3. AI Processing: Send image to Gemini Vision. Return JSON containing: name_vn, name_scientific, family, description, confidence (High/Medium/Low).
     4. Behavior: If image is not a plant, set name_vn to "Unknown plant" and confidence to "Low".
     5. Interface: Clean mobile-friendly layout, forest green header, card result view, and disclaimer at bottom "Results for reference only".
     ```
  4. Nhấn **Build (Ctrl+Enter)** ➔ Quan sát khung ứng dụng Prototype V1 xuất hiện trên Live Preview.

---

### 2.2. Demo Đánh Giá Kết Quả (Review) & Lập Task List
* **Thao tác:** Học viên đối chiếu trực tiếp giữa Prototype V1 trên Live Preview và bản Product Specification ở Module 1:
  * *Đánh giá:* AI đã làm đúng bộ khung upload và trả về kết quả tiếng Việt, nhưng tiêu đề còn nhỏ, thiếu spinner loading và chưa thông báo khi file ảnh quá 5MB.
  * *Lập Task List 4 Phase:* Lập danh sách 4 lệnh tinh chỉnh để chuẩn bị gửi vào Chat Panel.

---

### 2.3. Demo Cải Tiến Theo Vòng Lặp Bằng Chat Panel & Bút Vẽ (✏️)
* **Gõ lệnh vào Chat Panel:**
  ```text
  Show a centered spinning loader icon with text "Đang phân tích hình ảnh..." when user submits, and disable the button while processing.
  ```
* **Sử dụng Bút vẽ (Annotation Mode ✏️):**
  1. Click icon **✏️ (Bút vẽ)** dưới màn hình Live Preview.
  2. Chọn công cụ **Box (Hình chữ nhật)**, kéo khoanh tròn quanh nút "Submit".
  3. Gõ vào ô mô tả: *"Make this button forest green, add rounded corners (border-radius 12px), and make font bold"* ➔ Click **Add to chat**.

---

---

# 📌 MODULE 3: KIỂM THỬ, CẢI TIẾN & HOÀN THIỆN ỨNG DỤNG AI

### 3.1. Demo Kiểm Thử 5 Lớp & Phát Hiện Lỗi AI Fabrication
* **Chạy Checklist 5 lớp kiểm thử:**
  1. *Happy Path:* Upload ảnh lá bàng rõ nét ➔ AI hiện đúng tên Cây Bàng, mác "Độ tin cậy: Cao".
  2. *Edge Case & Fabrication:* Upload ảnh mờ/tối ➔ Phát hiện AI tự ý bịa đặt thông tin (Fabrication) thay vì trả về "Unknown".
  3. *Responsive UI:* Chuyển sang chế độ màn hình điện thoại ➔ Phát hiện nút chụp bị lệch khung.

---

### 3.2. Demo Sửa Lỗi Thực Tế Sau Kiểm Thử (Bug-Driven Optimization)
* **Khắc phục lỗi AI Fabrication trong Chat Panel:**
  ```text
  Update Gemini prompt instructions: If the image is blurry, dark, or not clearly a plant, DO NOT guess or fabricate details. You MUST set name_vn to "Không xác định" and confidence to "Low" with a warning badge.
  ```
* **Sửa lỗi lệch giao diện bằng Bút vẽ (Annotation Mode ✏️):** Bật bút vẽ ✏️ ➔ Khoanh vùng nút chụp bị lệch trên Live Preview ➔ Báo AI điều chỉnh CSS margin/padding cho cân đối.
* **Xác nhận trạng thái Release Candidate:** App đạt độ ổn định cao, sẵn sàng xuất bản công khai.

---

### 3.3. Demo Thảo Luận Tình Huống Đạo Đức AI Theo Mô Hình 3 Vai
* **Tình huống dẫn dắt:** Học sinh chụp ảnh lá độc ➔ AI nhận diện sai thành rau thơm ➔ Học sinh hái ăn bị ngộ độc.
* **Mô hình 3 Vai:**
  * *Vai 1 — Người dùng (Học sinh):* Rủi ro khi tin hoàn toàn vào AI.
  * *Vai 2 — Nhà phát triển (Giáo viên):* Trách nhiệm ghi nhãn cảnh báo an toàn trên app.
  * *Vai 3 — Hệ thống AI:* Cấu hình prompt kèm thang đánh giá độ tin cậy.

---

---

# 📌 MODULE 4: TRIỂN KHAI ỨNG DỤNG AI VÀO GIẢNG DẠY

### 4.1. Thao Tác Deploy 1-Click Lên Internet (Public URL)
1. Click nút **Publish** màu xanh lá ở góc trên bên phải màn hình AI Studio.
2. Tại Starter Tier ➔ Chọn **Get Started / Publish App**.
3. Nhập tên URL không dấu (VD: `plant-id-stem-demo`).
4. Tick chọn `Make app publicly accessible` ➔ Bấm **Publish App**.
5. Nhận đường link công khai và mã QR code để quét trực tiếp trên điện thoại di động.

---

### 4.2. Kịch Bản Thuyết Trình Mẫu Trong Demo Day (3 Phút)
Giảng viên làm mẫu bài thuyết trình theo Rubric 4 tiêu chí:

```text
"Kính chào thầy cô, tôi xin đại diện nhóm trình bày sản phẩm: App Trợ Lý Thực Vật Học Plant ID.

1. BÀI TOÁN & YÊU CẦU (Tiêu chí 1):
   Học sinh lớp 6 trường tôi gặp khó khăn khi đi học thực địa Sinh học ngoài sân trường. Chúng tôi đã bóc tách bài toán thành 5 yếu tố yêu cầu cụ thể về người dùng, input, output, chức năng và ràng buộc an toàn dữ liệu.

2. DEMO SẢN PHẨM TRÊN URL PUBLIC (Tiêu chí 2):
   Xin mời thầy cô truy cập đường link plant-id-stem-demo.ai.studio. Tôi upload chiếc lá bàng này... bấm phân tích... như thầy cô thấy, app hiện đúng tên Cây Bàng, tên Latin Terminalia catappa và mác 'Độ tin cậy: Cao' kèm dòng ghi chú khuyến cáo an toàn ở chân trang.

3. TƯ DUY PHÁT TRÌỂN THEO TIẾN TRÌNH SPEC-FIRST (Tiêu chí 3):
   Bài học lớn nhất của tôi là áp dụng tư duy Spec-first: bóc tách Yêu cầu ➔ viết Product Spec ➔ Sinh Prototype V1 ➔ Review kết quả ➔ Refine bằng bút vẽ. Khi gặp lỗi, nút Restore Checkpoint chính là cứu cánh giúp sửa app nhanh chóng.

4. PHƯƠNG ÁN CHUYỂN GIAO SƯ PHẠM (Tiêu chí 4):
   Tôi chuyển hóa Hồ sơ dự án này thành bài dạy 2 tiết theo tiến trình EDP 6 bước cho học sinh: học sinh xác định bài toán ➔ bóc tách yêu cầu ➔ thiết kế UI/UX ➔ tự dùng AI Studio tạo app ➔ kiểm thử 5 lớp và thảo luận về đạo đức AI khi sử dụng sản phẩm. Xin cảm ơn!"
```

---

*Bộ kịch bản demo và hướng dẫn thực hành chi tiết — Phiên bản 2.5*  
*Đồng bộ 100% với tài liệu `module_spec_kit_ai_studio.md` (v2.5)*
