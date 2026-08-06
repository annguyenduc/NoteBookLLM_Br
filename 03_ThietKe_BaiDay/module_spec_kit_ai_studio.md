# Thiết Kế Module Chi Tiết (Phiên Bản v2.5 — Spec-First Product Development for STEM Educators)
## Khóa Học: Phát Triển Sản Phẩm AI Cho Giáo Viên STEM Bằng Google AI Studio

> **Triết lý cốt lõi:** Khóa học không dạy mẹo gõ prompt vụn vặt (*Prompt-first*), mà dạy **tư duy phát triển sản phẩm AI có hệ thống (*Spec-first*)**:  
> $$\text{Bài toán } \rightarrow \text{Yêu cầu } \rightarrow \text{Đặc tả } \rightarrow \text{Khởi tạo với AI } \rightarrow \text{Đánh giá \& Cải tiến } \rightarrow \text{Triển khai}$$
> Học viên không học lập trình. Học viên thực thi trực tiếp bằng ngôn ngữ tự nhiên trên Google AI Studio Build Mode và chuyển giao thành tiến trình bài dạy STEM theo quy trình EDP cho học sinh.
>
> **Phiên bản:** 2.5 (Chuẩn hóa quy trình Spec-first) | **Ngày:** 2026-07-22

---

## 📑 MỤC LỤC TÀI LIỆU

1. [Pre-session Checklist (Gửi trước khi bắt đầu)](#-pre-session-checklist-gửi-trước-khi-bắt-đầu)
2. [Bản Đồ Khóa Học & Chuỗi Sản Phẩm (Deliverables)](#-bản-đồ-khóa-học--chuỗi-sản-phẩm-deliverables)
3. [Thông Tin Chung & Hồ Sơ Dự Án](#-thông-tin-chung--hồ-sơ-dự-án)
4. [Outline Tổng Quan Khóa Học](#-outline-tổng-quan-khóa-học)
5. [Nội Dung Chi Tiết 4 Module](#-module-1-lập-kế-hoạch-phát-triển-sản-phẩm-ai)
   - [Module 1: Lập Kế Hoạch Phát Triển Sản Phẩm AI](#-module-1-lập-kế-hoạch-phát-triển-sản-phẩm-ai)
   - [Module 2: Xây Dựng Ứng Dụng Với Google AI Studio Build Mode](#-module-2-xây-dựng-ứng-dụng-với-google-ai-studio-build-mode)
   - [Module 3: Kiểm Thử, Cải Tiến & Hoàn Thiện Ứng Dụng AI](#-module-3-kiểm-thử-cải-tiến--hoàn-thiện-ứng-dụng-ai)
   - [Module 4: Triển Khai Ứng Dụng AI Vào Giảng Dạy](#-module-4-triển-khai-ứng-dụng-ai-vào-giảng-dạy)
6. [Phụ Lục A: Mẫu "Hồ Sơ Dự Án" Đã Điền Sẵn Complete (Plant ID)](#-phụ-lục-a-mẫu-hồ-sơ-dự-án-đã-điền-sẵn-hoàn-chỉnh)
7. [Phụ Lục B: Rubric Đánh Giá Demo Day](#-phụ-lục-b-rubric-đánh-giá-demo-day)
8. [Phụ Lục C: Bảng Xử Lý Lỗi Thường Gặp & Lưu Ý Quota](#-phụ-lục-c-bảng-xử-lý-lỗi-thường-gặp)
9. [Phụ Lục D: Glossary 1 Trang (Giải Nghĩa Thuật Ngữ)](#-phụ-lục-d-glossary-1-trang-giải-nghĩa-thuật-nghữ)

---

## 📋 PRE-SESSION CHECKLIST (Gửi Trước 2 Ngày)

- [ ] **Tài khoản Google:** Có sẵn tài khoản **Gmail cá nhân (`@gmail.com`)**. *(Lưu ý: KHÔNG dùng email trường học `@edu` hay `@kdi.edu.vn` vì bị khóa quyền deploy và gặp lỗi API)*.
- [ ] **Trình duyệt:** Cài đặt Chrome phiên bản mới nhất trên máy tính.
- [ ] **Cấu hình Chrome:** Đã cho phép cookies cho domain `ai.google.dev` trong Settings.
- [ ] **Truy cập thử:** Mở thành công trang `https://aistudio.google.com/apps`.
- [ ] **Chuẩn bị ý tưởng:** Suy nghĩ sẵn 1 bài toán thực tế trong giảng dạy STEM mà bạn ước AI có thể giúp giải quyết.

---

## 🗺️ BẢN ĐỒ KHÓA HỌC & CHUỖI SẢN PHẨM (DELIVERABLES)

```
Module 1: PLAN       → Module 2: BUILD     → Module 3: VALIDATE  → Module 4: DEPLOY
Lập Kế Hoạch           Xây Dựng              Kiểm Thử & Hoàn Thiện Triển Khai Giảng Dạy
(Brief & Spec)         (Prototype V1)        (Release Candidate)   (Public App & Lesson Plan)
```

### 🎯 Chuỗi Sản Phẩm Học Viên Thu Được Sau Mỗi Module:
1. **Sau Module 1:** Product Brief + Product Specification + Wireframe giao diện (Hoàn thành **Phần 1** Hồ sơ dự án).
2. **Sau Module 2:** Prototype Version 1 + Task List (Hoàn thành **Phần 2** Hồ sơ dự án).
3. **Sau Module 3:** Release Candidate + Checklist kiểm thử và Đạo đức AI (Hoàn thành **Phần 3** Hồ sơ dự án).
4. **Sau Module 4:** Ứng dụng AI hoàn chỉnh (URL public) + Hồ sơ dự án hoàn chỉnh + Kế hoạch triển khai dạy học STEM.

---

## 🎯 THÔNG TIN CHUNG & HỒ SƠ DỰ ÁN

| Hạng mục | Chi tiết |
|---|---|
| Đối tượng | Giáo viên STEM THCS – THPT |
| Thời lượng | 4 Module × 90 phút (Project-based) |
| Hình thức nộp bài | **1 Google Doc duy nhất duy trì xuyên suốt 4 Module** tên là `"Hồ sơ dự án: [Tên App]"` |
| Công cụ thực thi | Google AI Studio Build Mode (`+ New app`) |
| Sản phẩm đầu ra | URL Web App public chạy thật dạng `https://[ten-app].ai.studio` |

---

## 📅 OUTLINE TỔNG QUAN KHÓA HỌC

### MODULE 1. LẬP KẾ HOẠCH PHÁT TRIỂN SẢN PHẨM AI
* **1.1. AI trong giáo dục & Xác định bài toán:** Vai trò của AI trong dạy học, các mô hình AI hiện nay, Ai gặp vấn đề? Vấn đề là gì? Dùng AI có phù hợp không?, So sánh Demo A (prompt ngắn) vs. Demo B (có đặc tả).
* **1.2. Xác định yêu cầu (Requirements):** Phân tích 5 yếu tố cốt lõi: Người dùng, Input, Output, Chức năng chính, Ràng buộc (Constraints - VD: không lưu dữ liệu học sinh, dung lượng ảnh < 5MB).
* **1.3. Thiết kế sản phẩm AI (Design):** Thiết kế luồng hoạt động (Data Flow), Wireframe giao diện (UI), Trải nghiệm người dùng (UX 4 tiêu chí Microsoft).
* **1.4. Viết đặc tả sản phẩm (Specification):** Mô tả sản phẩm, Phạm vi (Scope), Tiêu chí hoàn thành (Acceptance Criteria).
* **Sản phẩm sau Module:** Product Brief + Product Specification + Wireframe giao diện.

### MODULE 2. XÂY DỰNG ỨNG DỤNG VỚI GOOGLE AI STUDIO BUILD MODE
* **2.1. Khởi tạo dự án:** Giao diện Build Mode, Thiết lập AI Chips ban đầu, Quy trình chuyển hóa từ Đặc tả sang mã nguồn.
* **2.2. Sinh phiên bản đầu tiên (Generate Prototype V1):** Chuyển Product Specification thành Master Prompt (Hướng dẫn viết prompt: Intent-Based vs Implementation-Constrained, Cấu trúc prompt 5 thành phần), Sinh nguyên mẫu Prototype V1 trên Live Preview.
* **2.3. Đánh giá kết quả (Review):** Quan sát màn hình Live Preview, so sánh giữa sản phẩm AI vừa sinh ra và bản Product Specification ban đầu để nhận biết cái gì đúng, cái gì lệch.
* **2.4. Cải tiến theo vòng lặp (Refine):** Phân rã yêu cầu thành Task List 4 Phase, làm việc với Chat Panel, dùng bút vẽ (Annotation Mode ✏️) để sửa giao diện trực quan.
* **2.5. Quản lý phiên bản:** Checkpoint, Restore, Quản lý các phiên bản ứng dụng, những lưu ý khi phát triển.
* **Sản phẩm sau Module:** Prototype Version 1 + Task List 4 Phase.

### MODULE 3. KIỂM THỬ, CẢI TIẾN & HOÀN THIỆN ỨNG DỤNG AI
* **3.1. Kiểm thử ứng dụng:** Kiểm thử chức năng (Happy Path, Edge Cases), Kiểm thử giao diện di động, Kiểm thử phản hồi AI (AI Behavior & Fabrication Guard), Ghi nhận danh sách lỗi.
* **3.2. Cải tiến ứng dụng sau kiểm thử:** Sửa lỗi xử lý AI (Fix AI Behavior/Fabrication), Sửa lỗi giao diện bằng Bút vẽ (Annotation Mode ✏️), Tối ưu UX sau kiểm thử.
* **3.3. Đánh giá chất lượng:** Đánh giá độ ổn định và độ chính xác theo Product Specification & Tiêu chí hoàn thành (Acceptance Criteria).
* **3.4. Đạo đức AI trong giáo dục:** Hallucination, Kiểm chứng thông tin, Quyền riêng tư & Dữ liệu, Sử dụng AI có trách nhiệm (Khung phân tích 3 Vai).
* **Sản phẩm sau Module:** Release Candidate (Phiên bản sẵn sàng triển khai) + Checklist kiểm thử & Đạo đức AI.

### MODULE 4. TRIỂN KHAI ỨNG DỤNG AI VÀO GIẢNG DẠY
* **4.1. Xuất bản và chia sẻ ứng dụng:** Publish ứng dụng (Starter Tier Public URL 1-click), Chia sẻ cho người dùng (URL/QR Code), Quản lý phiên bản xuất bản.
* **4.2. Thiết kế hoạt động dạy học:** Tích hợp ứng dụng AI vào tiến trình dạy học (chuyển đổi thành Quy trình EDP 6 bước cho học sinh STEM), Chuẩn bị học liệu.
* **4.3. Đánh giá và cải tiến sau triển khai:** Thu thập phản hồi, Cải tiến nâng cấp, Demo Day & Đánh giá chéo theo Rubric 4 tiêu chí.
* **Sản phẩm sau Module:** Ứng dụng AI công khai + Hồ sơ dự án hoàn chỉnh + Kế hoạch triển khai trong dạy học STEM.

---

---

# MODULE 1: Lập Kế Hoạch Phát Triển Sản Phẩm AI

> **Thời lượng:** 90 phút | **Mục tiêu:** Xác định được bài toán, yêu cầu và hoàn thành bản đặc tả sản phẩm trước khi xây dựng.  
> **Sản phẩm đầu ra:** Product Brief + Product Specification + Wireframe giao diện (Điền vào Hồ sơ dự án Google Doc Phần 1).

## Nội dung

### 1.1. AI Trong Giáo Dục & Xác Định Bài Toán (20 phút)
* **Năng lực AI hiện đại trong dạy học:** Tổng quan vai trò của AI, các mô hình ngôn ngữ (LLM) và thị giác máy tính (Multimodal Vision) làm trợ lý học tập cho học sinh.
* **Xác định bài toán thực tế:**
  * *Ai gặp vấn đề?* (VD: Học sinh lớp 6 khi đi học thực địa Sinh học ngoài sân trường).
  * *Vấn đề là gì?* (Không nhớ tên cây, không mang sách giáo khoa, dễ nhầm lẫn các loài thực vật).
  * *Dùng AI có phù hợp không?* (Rất phù hợp vì AI Vision nhận diện ảnh tức thì ngay ngoài sân trường).
* **Live Demo So Sánh (Cú hích nhận thức):**
  * *Demo A (Gõ prompt vụn vặt tự phát — `nhận-diện-cây-xanh.zip`):* Cho học viên thấy gõ prompt 6 từ mơ hồ sẽ làm AI tự sinh app cẩm nang chăm sóc cây cảnh rườm rà, lạc đề.
  * *Demo B (Phát triển có Kế hoạch & Đặc tả — `plant-identifier.zip`):* Cho học viên thấy khi có Kế hoạch và Đặc tả chuẩn, ta kiểm soát AI thu gọn app lại đúng 5 trường chuẩn bài học Sinh học.

### 1.2. Xác Định Yêu Cầu Sản Phẩm (Requirements) (25 phút)
> 💡 **Lưu ý sư phạm:** Một câu nói như *"Tôi muốn AI chấm bài"* KHÔNG PHẢI là yêu cầu. Hướng dẫn học viên bóc tách bài toán thành 5 thành phần yêu cầu rõ ràng:

* **1. Người dùng (Target User):** Học sinh lớp 6 THCS.
* **2. Đầu vào (Input):** Ảnh chụp lá cây/toàn cây từ camera điện thoại.
* **3. Đầu ra (Output):** Tên tiếng Việt, tên khoa học (Latin), mô tả đặc điểm 2 câu, mức độ tin cậy.
* **4. Chức năng chính (Core Features):** Khung xem ảnh chụp, nút "Phân Tích", thẻ hiển thị kết quả, nút chụp lại.
* **5. Ràng buộc (Constraints):** KHÔNG lưu trữ dữ liệu cá nhân học sinh, KHÔNG yêu cầu đăng nhập, giới hạn dung lượng ảnh < 5MB.

### 1.3. Thiết Kế Sản Phẩm AI (Design) (25 phút)
* **Thiết kế luồng hoạt động (Data Flow):** Vẽ sơ đồ luồng di chuyển dữ liệu (`Chụp ảnh ➔ Hiện trạng thái Loading ➔ Gemini Vision API ➔ Hiển thị thẻ kết quả`).
* **Thiết kế giao diện (UI Wireframe):** Phác thảo giao diện 1 màn hình đơn giản trên giấy hoặc slide.
* **Thiết kế trải nghiệm người dùng (UX):** Áp dụng 4 tiêu chí UX của Microsoft:
  * *Useful (Có ích):* Giải quyết đúng nhu cầu làm bài thu hoạch thực địa.
  * *Reliable (Đáng tin):* Hiển thị mác *"Mức độ tin cậy: Thấp"* kèm lời khuyên hỏi giáo viên khi ảnh mờ.
  * *Accessible (Dễ dùng):* Nút chụp to rõ ở trung tâm màn hình, không cần đăng nhập.
  * *Pleasant (Dễ chịu):* Tông màu xanh lá cây mát mắt, font chữ to rõ dễ đọc ngoài trời.

### 1.4. Viết Product Specification (Specification) (20 phút)
* Tổng hợp Bài toán + Yêu cầu + Thiết kế thành bản **Product Specification** hoàn chỉnh trong Hồ sơ dự án Google Doc Phần 1.
* Xác định rõ phạm vi sản phẩm (Scope v1) và những gì KHÔNG làm ở v1 (Out of scope).
* Xác định **Tiêu chí hoàn thành (Acceptance Criteria)** để kiểm thử ở Module 3.

---

---

# MODULE 2: Xây Dựng Ứng Dụng Với Google AI Studio Build Mode

> **Thời lượng:** 90 phút | **Mục tiêu:** Chuyển bản đặc tả (Product Specification) thành phiên bản nguyên mẫu (Prototype Version 1).  
> **Sản phẩm đầu ra:** Prototype Version 1 (App chạy được) + Task List (Điền vào Hồ sơ dự án Google Doc Phần 2).

## Nội dung

### 2.1. Khởi Tạo Dự Án (15 phút)
* Mở Google AI Studio Build Mode (`https://aistudio.google.com/apps`) ➔ Click **+ New app**.
* **Thiết lập AI Chips ban đầu:** Tích chọn bật trước các AI Chips cần thiết (VD: *Google Search*, *Image Gen*) ngay ở màn hình khởi tạo để AI thiết lập đúng cấu trúc ban đầu.
* Tổng quan quy trình chuyển hóa từ Đặc tả (Product Specification) sang mã nguồn.

### 2.2. Sinh Phiên Bản Đầu Tiên (Generate Prototype V1) (25 phút)
* **Hướng dẫn viết prompt (Chuyển Product Spec thành yêu cầu cho AI):**
  * *Mô tả mục tiêu (Intent-Based Prompting):* Nói AI biết mình muốn đạt kết quả gì (để AI tự lựa chọn công nghệ).
  * *Chỉ định cách thực hiện (Implementation-Constrained Prompting):* Yêu cầu AI phải dùng công nghệ, thư viện hoặc kiến trúc cụ thể (VD: *"Use MediaPipe for hand gesture"*).
* **Cấu trúc prompt gồm 5 thành phần:**
  1. Build a [Loại app] for [Người dùng].
  2. Allow users to [Đầu vào].
  3. Call Gemini to return: [Kết quả trả về].
  4. If confidence is low, return "Unknown" with Low confidence.
  5. Use a clean design with [Màu sắc / Phong cách].
* **Sinh Prototype V1:** Bấm **Build (Ctrl+Enter)** ➔ Quan sát khung ứng dụng sơ khởi xuất hiện trên Live Preview bên phải.

### 2.3. Đánh Giá Kết Quả (Review) (15 phút)
> 💡 **Lý do cần bước Review:** AI là mô hình xác suất. Khi Prototype V1 xuất hiện, học viên cần đối chiếu trực tiếp giữa **Cái mong muốn (Spec)** và **Cái AI vừa làm ra (Prototype V1)** để phát hiện cái gì đúng, cái gì còn thiếu/lệch trước khi ra lệnh cải tiến.

* Học viên quan sát giao diện Live Preview và đánh giá:
  * AI đã dựng đúng bộ khung upload ảnh chưa?
  * Màu sắc và cỡ chữ đã phù hợp chưa?
  * Đã có thông báo trạng thái chờ (loading) và hiển thị mác tin cậy chưa?

### 2.4. Cải Tiến Theo Vòng Lập (Refine) (25 phút)
* **Phân rã yêu cầu thành Task List 4 Phase:**
  * *Phase 1 (Giao diện):* Điều chỉnh màu sắc header, cỡ chữ, nút bấm.
  * *Phase 2 (Xử lý AI):* Tinh chỉnh câu lệnh Gemini trả về kết quả tiếng Việt chuẩn.
  * *Phase 3 (Hiệu ứng):* Thêm spinner loading khi đang phân tích.
  * *Phase 4 (Báo lỗi):* Thông báo khi dung lượng ảnh > 5MB.
* **Làm việc với Chat Panel:** Nhập từng câu lệnh từ Task List vào ô chat để cải tiến từng bước.
* **Sử dụng Bút vẽ (Annotation Mode ✏️):** Bật bút vẽ ➔ Khoanh trực tiếp quanh vùng bị lệch trên Live Preview ➔ Ra lệnh cho AI sửa chính xác vùng đã khoanh.

### 2.5. Quản Lý Phiên Bản (Checkpoint & Restore) (10 phút)
* **Sử dụng Checkpoint & Restore:** Khi AI làm hỏng giao diện, cuộn Chat Panel lên và bấm **Restore** để quay về phiên bản ổn định trước đó.
* Những lưu ý quan trọng để giữ mã nguồn ứng dụng sạch sẽ, không bị phồng to.

---

---

# MODULE 3: Kiểm Thử, Cải Tiến & Hoàn Thiện Ứng Dụng AI

> **Thời lượng:** 90 phút | **Mục tiêu:** Hoàn thiện ứng dụng trước khi triển khai (Release Candidate).  
> **Sản phẩm đầu ra:** Release Candidate (Phiên bản sẵn sàng triển khai) + Checklist kiểm thử & Đạo đức AI (Điền vào Hồ sơ dự án Google Doc Phần 3).

## Nội dung

### 3.1. Kiểm Thử Ứng Dụng (25 phút)
* **Kiểm thử chức năng (Happy Path & Edge Cases):** Test trường hợp ảnh chụp lý tưởng (lá bàng rõ nét) vs. ảnh mờ, ảnh tối, ảnh mặt người.
* **Kiểm thử giao diện di động:** Kiểm tra tính responsive và bố cục hiển thị trên màn hình điện thoại.
* **Kiểm thử phản hồi AI (AI Behavior & Fabrication Guard):** Kiểm tra xem AI có bị bịa đặt thông tin (**Fabrication**) khi thiếu dữ liệu không, có trả về nhãn *"Unknown"* hoặc *"Độ tin cậy: Thấp"* đúng như đặc tả không.
* **Ghi nhận danh sách lỗi:** Liệt kê các lỗi thực tế cần khắc phục.

### 3.2. Cải Tiến Ứng Dụng Sau Kiểm Thử (25 phút)
> 💡 **Sự khác biệt với Cải tiến ở Module 2:** Cải tiến ở Module 2 là làm theo Task List kế hoạch để dựng khung V1. Cải tiến ở Module 3 là **sửa lỗi thực tế phát sinh sau khi test (Bug-Driven Optimization)** để đưa app đạt chuẩn xuất bản công khai.

* **Sửa lỗi xử lý AI (Fix AI Behavior & Fabrication Bugs):** Tinh chỉnh câu lệnh Gemini trong Chat Panel để khắc phục các lỗi phát hiện từ bước 3.1 (VD: Ép Gemini bắt buộc trả về "Unknown" khi gặp ảnh mờ/tối).
* **Sửa lỗi giao diện phát sinh bằng Bút vẽ (Annotation Mode ✏️):** Bật bút vẽ ✏️ ➔ Khoanh quanh các vùng bị vỡ/lệch giao diện trên Live Preview di động ➔ Ra lệnh cho AI sửa đúng vị trí.
* **Tối ưu trải nghiệm người dùng sau kiểm thử (Post-Testing UX Refinement):** Bổ sung nhãn cảnh báo an toàn và chuẩn hóa giao diện dựa trên 4 tiêu chí UX (Useful, Reliable, Accessible, Pleasant).

### 3.3. Đánh Giá Chất Lượng (20 phút)
* Đánh giá độ ổn định và độ chính xác của ứng dụng dựa trên bản **Product Specification** và các **Tiêu chí hoàn thành (Acceptance Criteria)** đã lập ở Module 1.
* Xác nhận ứng dụng đã đạt trạng thái **Release Candidate (Sẵn sàng triển khai)**.

### 3.4. Đạo Đức AI Trong Giáo Dục (20 phút)
* **Phân tích rủi ro AI:** Hiện tượng ảo giác (Hallucination), nguy cơ ngộ nhận kiến thức, bảo mật quyền riêng tư dữ liệu học sinh.
* **Khung phân tích Đạo đức AI theo Mô hình 3 Vai:**
  * *Vai 1 — Người dùng (Học sinh):* Rủi ro khi tin tuyệt đối vào AI.
  * *Vai 2 — Nhà phát triển (Giáo viên):* Trách nhiệm ghi nhãn cảnh báo an toàn trên app.
  * *Vai 3 — Hệ thống AI:* Cấu hình prompt kèm thang đánh giá độ tin cậy.
* Hoàn thành **Checklist kiểm thử & Đạo đức AI** trong Hồ sơ dự án Google Doc.

---

---

# MODULE 4: Triển Khai Ứng Dụng AI Vào Giảng Dạy

> **Thời lượng:** 90 phút | **Mục tiêu:** Đưa ứng dụng vào hoạt động và xây dựng kế hoạch sử dụng trong lớp học STEM.  
> **Sản phẩm đầu ra:** Ứng dụng AI công khai + Hồ sơ dự án hoàn chỉnh + Kế hoạch triển khai trong dạy học STEM (Tiến trình EDP 6 bước).

## Nội dung

### 4.1. Xuất Bản Và Chia Sẻ Ứng Dụng (20 phút)
* **Publish ứng dụng 1-Click:** Click nút **Publish** màu xanh lá ➔ Chọn Starter Tier ➔ Nhập tên URL ➔ Bấm **Publish App** để nhận link công khai `https://[ten-app].ai.studio` và mã QR Code.
* **Chia sẻ cho người dùng:** Gửi link URL/mã QR cho học sinh mở trực tiếp trên thiết bị di động.
* **Quản lý các phiên bản xuất bản.**

### 4.2. Thiết Kế Hoạt Động Dạy Học (35 phút)
* **Xác định mục tiêu bài học STEM:** Tích hợp sản phẩm AI vào chương trình môn học.
* **Thiết kế hoạt động học tập (Chuyển đổi thành Quy trình EDP 6 bước cho học sinh):**
  1. *Bước 1: Xác định vấn đề* ➔ Học sinh mô tả nhu cầu thực tế.
  2. *Bước 2: Nghiên cứu kiến thức nền* ➔ Học sinh trải nghiệm thử demo công nghệ AI.
  3. *Bước 3: Đề xuất & Lựa chọn giải pháp* ➔ Học sinh phác thảo ý tưởng ứng dụng.
  4. *Bước 4: Chế tạo mẫu* ➔ Học sinh dùng AI Studio Build Mode tạo app.
  5. *Bước 5: Thử nghiệm & Đánh giá* ➔ Chạy checklist kiểm thử và sửa giao diện.
  6. *Bước 6: Chia sẻ & Thảo luận* ➔ Thuyết trình sản phẩm và thảo luận Đạo đức AI.
* **Chuẩn bị học liệu & Kế hoạch triển khai lớp học.**

### 4.3. Đánh Giá Và Cải Tiến Sau Triển Khai (35 phút)
* **Thu thập phản hồi & Cải tiến:** Lập kênh tiếp nhận phản hồi của học sinh để định hướng nâng cấp phiên bản tiếp theo.
* **Demo Day & Đánh giá chéo:** Học viên thuyết trình 3 phút về ứng dụng và kế hoạch bài dạy của mình dựa trên **Rubric 4 tiêu chí (Phụ lục B)**:
  1. Bài toán rõ ràng.
  2. Sản phẩm chạy thực tế trên URL.
  3. Tư duy phát triển có quy trình.
  4. Kế hoạch triển khai bài dạy EDP hiệu quả.

---

---

## 📎 PHỤ LỤC A: MẪU "HỒ SƠ DỰ ÁN" ĐÃ ĐIỀN SẴN (PLANT IDENTIFIER)

```markdown
HỒ SƠ DỰ ÁN: App Nhận Diện Cây Trồng Thực Địa (Plant ID)
Họ và tên GV: Nguyễn Văn A | Trường: THCS... | Môn giảng dạy: Sinh học THCS

==================================================
PHẦN 1: BÀI TOÁN, YÊU CẦU & ĐẶC TẢ SẢN PHẨM (SPEC)
(Chuyển hóa từ spec-template.md — Hoàn thành ở Module 1)
==================================================
1. Bài toán thực tế (Problem & Context):
   - Đối tượng sử dụng: Học sinh lớp 6 khi tham gia học thực địa Sinh học ngoài sân trường.
   - Vấn đề gặp phải: Học sinh không nhớ tên cây, không mang sách giáo khoa, dễ tra cứu nhầm lẫn.
   - Giải pháp AI: App nhận diện cây qua ảnh chụp camera điện thoại giúp học sinh tra cứu tức thì.

2. Bóc tách yêu cầu (Requirements):
   - Đầu vào (Input): Ảnh chụp lá cây/toàn cây từ camera điện thoại.
   - Đầu ra (Output): Tên tiếng Việt, tên khoa học (Latin), họ thực vật, mô tả 2 câu, thang độ tin cậy.
   - Chức năng cốt lõi: Khung xem ảnh, nút Phân Tích, thẻ hiển thị kết quả, nút Chụp lại.
   - Ràng buộc & Giới hạn: KHÔNG lưu trữ dữ liệu cá nhân học sinh, KHÔNG yêu cầu đăng nhập, file ảnh < 5MB.

3. Thiết kế sản phẩm & UI/UX (Design):
   - Luồng hoạt động: Upload/Capture ➔ Gemini Vision API ➔ Result Card Display.
   - 4 Tiêu chí UX (Microsoft):
     * Useful: Phục vụ trực tiếp việc ghi bài thu hoạch thực địa.
     * Reliable: Hiện "Mức độ tin cậy: Thấp" kèm lời khuyên hỏi giáo viên nếu ảnh mờ/tối.
     * Accessible: Nút chụp to, giao diện 1 màn hình duy nhất.
     * Pleasant: Tông màu xanh lá thực vật thân thiện.

4. Tiêu chí hoàn thành (Acceptance Criteria):
   - [ ] Nhận diện đúng ít nhất 4 loài cây phổ biến trong sân trường (Cây Bàng, Phượng, Bằng Lăng, Sứ).
   - [ ] Giao diện hiển thị tốt trên điện thoại di động (Responsive UI).
   - [ ] Trả về nhãn "Không xác định" khi ảnh mờ hoặc không chứa cây trồng.

==================================================
PHẦN 2: DANH SÁCH VIỆC CẦN LÀM - TASK LIST FOR AI
(Chuyển hóa từ plan-template.md & tasks-template.md — Hoàn thành ở Module 2)
==================================================
- [x] Phase 1 (UI Framework): Master Prompt tạo khung app và vùng upload dropzone (Prototype V1).
- [x] Phase 2 (AI Logic): Cài đặt Gemini Vision nhận diện tên cây và trả kết quả JSON tiếng Việt.
- [x] Phase 3 (UX & Effects): Thêm spinner loading "Đang phân tích hình ảnh..." và footer disclaimer.
- [x] Phase 4 (Error Handling): Thêm thông báo nếu file upload > 5MB.

==================================================
PHẦN 3: CHECKLIST KIỂM THỬ & ĐẠO ĐỨC AI
(Chuyển hóa từ report-template.md — Hoàn thành ở Module 3)
==================================================
1. Bảng kết quả kiểm thử thực tế (Verification Matrix):
   - [x] Happy Path: Upload ảnh lá bàng ➔ Hiện đúng tên Cây Bàng, mác "Độ tin cậy: Cao".
   - [x] Edge Case: Upload ảnh mặt người/ảnh mờ ➔ Hiện "Không xác định", không bị crash app.
   - [x] Chống bịa đặt dữ liệu (AI Fabrication Guard): AI không tự bịa tên cây khi ảnh thiếu chi tiết.
   - [x] Responsive UI: Nút bấm và thẻ kết quả hiển thị vừa vặn trên Chrome di động.

2. Khung phân tích Đạo đức AI (3-Role Responsible AI Framework):
   - Người dùng (Học sinh): Nguy cơ ngộ nhận ➔ Yêu cầu học sinh đối chiếu kết quả với mẫu lá thật.
   - Nhà phát triển (Giáo viên): Trách nhiệm cảnh báo ➔ Dán rõ nhãn miễn trừ trách nhiệm ở chân trang.
   - Hệ thống AI: Kiểm soát ảo giác AI ➔ Cấu hình Gemini Temperature = 0.1 và yêu cầu độ tin cậy.
```

---

## 📊 PHỤ LỤC B: RUBRIC ĐÁNH GIÁ DEMO DAY (MODULE 4)

| Tiêu chí | Chưa Đạt (1đ) | Đạt (2đ) | Tốt (3đ) |
|---|---|---|---|
| **1. Bài toán & Yêu cầu** | Không nêu được người dùng/vấn đề | Nêu được bài toán chung chung | Nêu rõ người dùng + bài toán + bóc tách 5 yếu tố yêu cầu cụ thể |
| **2. Sản phẩm chạy thực tế** | Link URL không mở được | Link URL mở được, còn 1-2 lỗi nhỏ | App chạy mượt trên điện thoại, xử lý tốt các trường hợp biên |
| **3. Tư duy phát triển** | Không giải thích được cách làm | Mô tả được các bước ra lệnh cho AI | Giải thích rõ tiến trình Spec-first từ Yêu cầu ➔ Spec ➔ Review ➔ Refine |
| **4. Kế hoạch giảng dạy** | Không hình dung được cách dạy lại cho học sinh | Mô tả được ý tưởng dạy chung chung | Trình bày được Kế hoạch bài dạy EDP 6 bước áp dụng ngay vào tiết dạy STEM |

---

## 🛠️ PHỤ LỤC C: BẢNG XỬ LÝ LỖI THƯỜNG GẶP

| Lỗi gặp phải | Nguyên nhân | Cách khắc phục ngay |
|---|---|---|
| `"An internal error occurred"` | Dùng email trường (`@edu`) | **Chuyển sang dùng Gmail cá nhân (`@gmail.com`)** |
| Preview bị màn hình đen | Trình duyệt chặn cookies | Mở Chrome Settings → Allow cookies `ai.google.dev` |
| AI sửa hỏng giao diện | AI sinh code nhầm | Tìm điểm lưu trong Chat panel → Click **Restore** |
| Không bấm nút Publish được | Đã publish 2 apps trước đó | Vào Dashboard → Unpublish 1 app cũ |

---

## 📖 PHỤ LỤC D: GLOSSARY 1 TRANG (GIẢI NGHĨA THUẬT NGỮ)

| Thuật ngữ | Giải thích đơn giản |
|---|---|
| **Yêu cầu (Requirements)** | Bóc tách bài toán thành người dùng, input, output, chức năng và ràng buộc. |
| **Đặc tả sản phẩm (Product Spec)** | Tài liệu tổng hợp mô tả "cần làm gì và tại sao" trước khi bắt tay xây dựng. |
| **Build Mode** | Chế độ tạo ứng dụng trực tiếp bằng câu lệnh ngôn ngữ tự nhiên trong Google AI Studio. |
| **Live Preview** | Màn hình bên phải xem trực tiếp ứng dụng thật đang hoạt động. |
| **Annotation Mode (✏️)** | Công cụ dùng bút vẽ khoanh tròn lên màn hình để bảo AI sửa giao diện. |
| **Checkpoint & Restore** | Điểm tự động lưu lịch sử — giúp quay về bản cũ nếu AI làm hỏng app. |
| **AI Chips** | Các nút bấm tích hợp nhanh tính năng nâng cao (bản đồ, tìm kiếm, tạo ảnh). |
| **Publish / Deploy** | Xuất bản ứng dụng thành đường link công khai trên Internet để ai cũng mở được. |
| **Fabrication (Bịa đặt dữ liệu)** | Khái niệm kiểm thử: AI tự "sáng tạo" thêm thông tin không tồn tại khi thiếu ràng buộc. |

---

*Tài liệu thiết kế chi tiết khóa học — Phiên bản 2.5 (Spec-First Product Development)*
