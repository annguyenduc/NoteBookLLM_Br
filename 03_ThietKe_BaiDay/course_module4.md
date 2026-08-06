# MODULE 4: Triển Khai Ứng Dụng AI Vào Giảng Dạy
### Khoá Học: Phát Triển Ứng Dụng Với AI

---

> **⏱ Thời lượng:** 90 phút  
> **🎯 Mục tiêu:** Xuất bản ứng dụng công khai lên Internet bằng 1 click, tích hợp sản phẩm AI vào tiến trình dạy học STEM theo quy trình EDP 6 bước cho học sinh và thực hành Demo Day thuyết trình sản phẩm.  
> **📦 Sản phẩm đầu ra:** URL Web App Public + Hồ sơ dự án hoàn chỉnh 4 phần + Kế hoạch triển khai dạy học STEM EDP 6 bước.

---

## TỔNG QUAN MODULE 4

```
Thời gian     Mục       Nội dung chính
─────────────────────────────────────────────────────────────
00:00–20:00   4.1       Xuất bản & Chia sẻ ứng dụng 1-Click (Public URL)
20:00–55:00   4.2       Thiết kế hoạt động dạy học STEM theo quy trình EDP 6 bước
55:00–90:00   4.3       Demo Day thuyết trình sản phẩm & Đánh giá chéo theo Rubric
```

---

## 4.1 Xuất Bản & Chia Sẻ Ứng Dụng 1-Click (Public URL)

**⏱ 20 phút**

Sau khi hoàn thành kiểm thử ở Module 3 và đạt trạng thái Release Candidate, ứng dụng của bạn sẵn sàng được xuất bản để học sinh và đồng nghiệp truy cập trực tiếp từ thiết bị di động.

---

### Quy Trình Publish Ứng Dụng 1-Click Lên Internet

1. Quan sát góc trên bên phải màn hình Google AI Studio Build Mode, bấm vào nút **`Publish`** màu xanh lá cây.
2. Tại bảng tùy chọn hiện ra, dưới mục **Starter Tier**, chọn **`Get Started`** hoặc **`Publish App`**.
3. **Đặt tên URL:** Nhập tên định danh viết liền không dấu, dùng gạch nối (ví dụ: `plant-id-stem-demo` hoặc `app-sinh-hoc-thcs`). Đường link của bạn sẽ có dạng: `https://[ten-app].ai.studio`.
4. Tick chọn vào ô **`Make app publicly accessible`** (Cho phép truy cập công khai).
5. Bấm **`Publish App`**.

```
┌──────────────────────────────────────────────────────────────┐
│  PUBLISH APP                                             [X] │
│                                                              │
│  App Name: [ plant-id-stem-demo                         ]    │
│  Public Link: https://plant-id-stem-demo.ai.studio          │
│                                                              │
│  [x] Make app publicly accessible                            │
│                                                              │
│                   [ Cancel ]   [ PUBLISH APP 🚀 ]            │
└──────────────────────────────────────────────────────────────┘
```

---

### Chia Sẻ Sản Phẩm Cho Học Sinh

Sau khi bấm Publish, AI Studio tự động tạo cho bạn:
- **Đường link URL public:** Có thể dán vào nhóm Zalo/Google Classroom của lớp học.
- **Mã QR Code:** Giáo viên có thể in mã QR dán lên bảng hoặc phiếu giao nhiệm vụ để học sinh quét trực tiếp bằng camera điện thoại ngoài sân trường.

> 💡 **Lưu ý sư phạm & Giới hạn Quota:**  
> - Tài khoản Starter Tier miễn phí cho phép bạn publish ứng dụng chạy thật mà không tốn chi phí host hay domain.  
> - Nếu bạn nhận được thông báo không publish được do vượt giới hạn số lượng app: Hãy quay lại Dashboard (`ai.google.dev`), chọn một app thử nghiệm cũ và bấm **Unpublish** để giải phóng suất publish mới.

---

## 4.2 Thiết Kế Hoạt Động Dạy Học STEM Theo Quy Trình EDP 6 Bước

**⏱ 35 phút**

> 💡 **Lưu ý sư phạm cốt lõi:**  
> Mục tiêu tối thượng của khóa học này **không phải là giáo viên làm app cho học sinh dùng**. Mục tiêu là giáo viên **chuyển giao quy trình Spec-first Vibe Coding thành tiến trình học tập EDP 6 bước cho học sinh**, giúp học sinh tự tay bóc tách bài toán và dùng AI Studio kiến tạo giải pháp!

---

### Bảng Chuyển Hóa Từ Tiến Trình Phát Triển Sản Phẩm AI Sang Tiến Trình EDP 6 Bước

```
Tiến trình Spec-first Vibe Coding   ──►   Quy trình EDP 6 bước dạy học STEM
Bài toán thực tế ➔ Bóc tách Yêu cầu       Bước 1: Xác định vấn đề & Yêu cầu
Ý tưởng ➔ Phác thảo Wireframe             Bước 2: Nghiên cứu kiến thức nền
Tạo Product Spec                          Bước 3: Đề xuất & Lựa chọn giải pháp
Build V1 với AI Studio                    Bước 4: Chế tạo nguyên mẫu (Prototype)
Kiểm thử 5 lớp & Fix Fabrication          Bước 5: Thử nghiệm, Đánh giá & Cải tiến
Deploy Public & thuyết trình              Bước 6: Chia sẻ & Thảo luận sản phẩm
```

---

### Chi Tiết Phân Vai 6 Bước EDP Trong Bài Dạy STEM "Thiết Kế Trợ Lý AI Thực Địa"

| Bước EDP | Hoạt động của Học Sinh (Learner) | Vai trò & Hướng dẫn của Giáo Viên (Facilitator) | Sản phẩm học tập |
|---|---|---|---|
| **Bước 1: Xác định vấn đề & Yêu cầu** | Khảo sát khó khăn khi làm bài thu hoạch thực địa Sinh học (không nhớ tên cây, tra sách mất thời gian). Bóc tách bài toán thành 5 yếu tố. | Nêu tình huống thực tế, phát phiếu giao nhiệm vụ, hướng dẫn học sinh phân tích 5 thành phần yêu cầu. | Điền vào **Phần 1: Bài toán & Yêu cầu** |
| **Bước 2: Nghiên cứu kiến thức nền** | Tìm hiểu đặc điểm nhận dạng thực vật trong SGK Sinh học 6 và thử nghiệm demo công nghệ AI Vision. | Định hướng đọc SGK, cung cấp mẫu lá cây thử nghiệm, làm demo nhanh công nghệ AI Vision. | Phác thảo Data Flow và UI Wireframe trên A4 |
| **Bước 3: Đề xuất & Lựa chọn giải pháp** | Tổng hợp kết quả nghiên cứu thành bản **Product Specification** hoàn chỉnh cho nhóm mình. | Hướng dẫn mẫu cấu trúc Product Spec, duyệt tính khả thi và tiêu chí Acceptance Criteria của nhóm. | Bản Product Spec có Scope & Acceptance Criteria |
| **Bước 4: Chế tạo nguyên mẫu** | Đưa Product Spec thành Master Prompt, dùng AI Studio Build Mode để vibe code dựng Prototype V1. Dùng Bút vẽ ✏️ sửa UI. | Quản lý thiết bị/mạng, hỗ trợ giải đáp khi AI hiểu sai prompt, hướng dẫn thao tác Bút vẽ ✏️ và Restore. | URL nguyên mẫu V1 chạy trên điện thoại nhóm |
| **Bước 5: Thử nghiệm, Đánh giá & Cải tiến** | Mang điện thoại ra sân trường chạy Checklist kiểm thử 5 lớp. Upload ảnh mờ để test lỗi AI Fabrication và dán Footer cảnh báo. | Giám sát học sinh kiểm thử thực địa, gợi ý các tình huống test biên, hướng dẫn khắc phục lỗi AI Fabrication. | Release Candidate + Bảng kết quả kiểm thử |
| **Bước 6: Chia sẻ & Thảo luận** | Thuyết trình 3 phút trong Demo Day, cho các nhóm khác quét mã QR dùng thử app và thảo luận Đạo đức AI 3 Vai. | Tổ chức hội đồng Demo Day, điều phối đánh giá chéo theo Rubric 4 tiêu chí, chốt kiến thức và Đạo đức AI. | Phiếu đánh giá chéo theo Rubric 4 tiêu chí |

---

#### ✏️ Hoạt động thực hành: Lập Kế hoạch bài dạy STEM EDP 6 bước của bạn (15 phút)

Học viên dùng bảng phân vai trên để hoàn thành Kế hoạch triển khai cho bài dạy của mình (Điền vào **Hồ Sơ Dự Án — Phần 4**).

---

## 4.3 Demo Day Thuyết Trình Sản Phẩm & Đánh Giá Chéo

**⏱ 35 phút**

### Kịch Bản Thuyết Trình Mẫu Trong Demo Day (3 Phút / Nhóm)

Giáo viên thực hiện thuyết trình mẫu (hoặc hướng dẫn đại diện nhóm học sinh) theo đúng **Rubric 4 tiêu chí**:

> *"Kính chào thầy cô và các bạn, tôi xin đại diện nhóm trình bày sản phẩm: App Trợ Lý Thực Vật Học Plant ID.*
>
> **1. BÀI TOÁN & YÊU CẦU (Tiêu chí 1):**  
> Học sinh lớp 6 trường tôi gặp khó khăn khi đi học thực địa Sinh học ngoài sân trường. Chúng tôi đã bóc tách bài toán thành 5 yếu tố yêu cầu cụ thể về người dùng, input, output, chức năng và ràng buộc an toàn dữ liệu.
>
> **2. DEMO SẢN PHẨM TRÊN URL PUBLIC (Tiêu chí 2):**  
> Xin mời thầy cô truy cập đường link `plant-id-stem-demo.ai.studio`. Tôi upload chiếc lá bàng này... bấm phân tích... như thầy cô thấy, app hiện đúng tên Cây Bàng, tên Latin Terminalia catappa và mác 'Độ tin cậy: Cao' kèm dòng ghi chú khuyến cáo an toàn ở chân trang.
>
> **3. TƯ DUY PHÁT TRÌỂN THEO TIẾN TRÌNH SPEC-FIRST (Tiêu chí 3):**  
> Bài học lớn nhất của tôi là áp dụng tư duy Spec-first: bóc tách Yêu cầu ➔ viết Product Spec ➔ Sinh Prototype V1 ➔ Review kết quả ➔ Refine bằng bút vẽ. Khi gặp lỗi, nút Restore Checkpoint chính là cứu cánh giúp sửa app nhanh chóng.
>
> **4. PHƯƠNG ÁN CHUYỂN GIAO SƯ PHẠM (Tiêu chí 4):**  
> Tôi chuyển hóa Hồ sơ dự án này thành bài dạy 2 tiết theo tiến trình EDP 6 bước cho học sinh: học sinh xác định bài toán ➔ bóc tách yêu cầu ➔ thiết kế UI/UX ➔ tự dùng AI Studio tạo app ➔ kiểm thử 5 lớp và thảo luận về đạo đức AI khi sử dụng sản phẩm. Xin cảm ơn!"*

---

### Đánh Giá Chéo Theo Rubric (Peer Assessment)

Mỗi học viên / nhóm sử dụng **Rubric Đánh Giá Demo Day (Phụ lục B)** để đánh giá chéo bài thuyết trình của các nhóm khác.

---

```
════════════════════════════════════════════════════════════════════════════════
🎯 SẢN PHẨM HOÀN THÀNH SAU MODULE 4:
1. URL Web App public công khai trên Internet.
2. Kế hoạch bài dạy STEM EDP 6 bước (Điền vào Hồ Sơ Dự Án — Phần 4).
3. Hồ sơ dự án Google Doc hoàn chỉnh cả 4 Phần.
════════════════════════════════════════════════════════════════════════════════
```

---

## 📋 HỒ SƠ DỰ ÁN — PHẦN 4 (Mẫu điền)

```
================================================================================
PHẦN 4: KẾ HOẠCH TRIỂN KHAI BÀI DẠY STEM
(Hoàn thành ở Module 4)
================================================================================
Tên bài dạy: ___________________________________________________________________
Môn học / Khối lớp: ________________________________ | Thời lượng: ______ tiết

TIẾN TRÌNH DẠY HỌC EDP 6 BƯỚC:
1. Bước 1 (Xác định vấn đề): Học sinh thực hiện __________________________________
   Vai trò GV: _________________________________________________________________
2. Bước 2 (Kiến thức nền): Học sinh thực hiện ________________────────────────────
   Vai trò GV: _________________________________________________________________
3. Bước 3 (Đề xuất giải pháp): Học sinh lập bản Product Spec _____________________
   Vai trò GV: _________________________________________________________________
4. Bước 4 (Chế tạo mẫu): Học sinh dùng AI Studio Build Mode tạo app _____________
   Vai trò GV: _________________________________________________________________
5. Bước 5 (Thử nghiệm & Cải tiến): Chạy checklist kiểm thử 5 lớp _________________
   Vai trò GV: _________________________________________________________________
6. Bước 6 (Chia sẻ & Đánh giá): Thuyết trình Demo Day & Thảo luận Đạo đức AI _____
   Vai trò GV: _________________________________________________________________

ĐƯỜNG LINK APP PUBLIC: https://________________________.ai.studio
```

---

---

# 📎 PHỤ LỤC TÀI LIỆU KHOÁ HỌC

---

## 📄 PHỤ LỤC A: MẪU "HỒ SƠ DỰ ÁN" ĐÃ ĐIỀN HOÀN CHỈNH (PLANT ID)

```markdown
HỒ SƠ DỰ ÁN: App Nhận Diện Cây Trồng Thực Địa (Plant ID)
Họ và tên GV: Nguyễn Văn A | Trường: THCS... | Môn giảng dạy: Sinh học THCS

==================================================
PHẦN 1: BÀI TOÁN, YÊU CẦU & ĐẶC TẢ SẢN PHẨM (SPEC)
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
   - [x] Nhận diện đúng ít nhất 4 loài cây phổ biến trong sân trường (Cây Bàng, Phượng, Bằng Lăng, Sứ).
   - [x] Giao diện hiển thị tốt trên điện thoại di động (Responsive UI).
   - [x] Trả về nhãn "Không xác định" khi ảnh mờ hoặc không chứa cây trồng.

==================================================
PHẦN 2: DANH SÁCH VIỆC CẦN LÀM - TASK LIST FOR AI
==================================================
- [x] Phase 1 (UI Framework): Master Prompt tạo khung app và vùng upload dropzone (Prototype V1).
- [x] Phase 2 (AI Logic): Cài đặt Gemini Vision nhận diện tên cây và trả kết quả JSON tiếng Việt.
- [x] Phase 3 (UX & Effects): Thêm spinner loading "Đang phân tích hình ảnh..." và footer disclaimer.
- [x] Phase 4 (Error Handling): Thêm thông báo nếu file upload > 5MB.

==================================================
PHẦN 3: CHECKLIST KIỂM THỬ & ĐẠO ĐỨC AI
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

==================================================
PHẦN 4: KẾ HOẠCH TRIỂN KHAI BÀI DẠY STEM
==================================================
Tên bài dạy: Thiết Kế Trợ Lý AI Nhận Diện Thực Vật Sân Trường (Sinh học 6) | Thời lượng: 2 tiết
- Tiến trình EDP 6 bước: HS xác định bài toán ➔ NCKT nền ➔ Lập Product Spec ➔ Build trên AI Studio ➔ Kiểm thử 5 lớp ➔ Thuyết trình Demo Day.
- URL App Public: https://plant-id-stem-demo.ai.studio
```

---

## 📊 PHỤ LỤC B: RUBRIC ĐÁNH GIÁ DEMO DAY (MODULE 4)

| Tiêu chí | Chưa Đạt (1đ) | Đạt (2đ) | Tốt (3đ) |
|---|---|---|---|
| **1. Bài toán & Yêu cầu** | Không nêu được người dùng/vấn đề | Nêu được bài toán chung chung | Nêu rõ người dùng + bài toán + bóc tách 5 yếu tố yêu cầu cụ thể |
| **2. Sản phẩm chạy thực tế** | Link URL không mở được | Link URL mở được, còn 1-2 lỗi nhỏ | App chạy mượt trên điện thoại, xử lý tốt các trường hợp biên |
| **3. Tư duy phát triển** | Không giải thích được cách làm | Mô tả được các bước ra lệnh cho AI | Giải thích rõ tiến trình Spec-first từ Yêu cầu ➔ Spec ➔ Review ➔ Refine bằng bút vẽ |
| **4. Kế hoạch giảng dạy** | Không hình dung được cách dạy lại cho học sinh | Mô tả được ý tưởng dạy chung chung | Trình bày được Kế hoạch bài dạy EDP 6 bước áp dụng ngay vào tiết dạy STEM |

---

## 🛠️ PHỤ LỤC C: BẢNG XỬ LÝ LỖI THƯỜNG GẶP

| Lỗi gặp phải | Nguyên nhân | Cách khắc phục ngay |
|---|---|---|
| `"An internal error occurred"` | Dùng email trường (`@edu`) | **Chuyển sang dùng Gmail cá nhân (`@gmail.com`)** |
| Preview bị màn hình đen | Trình duyệt chặn cookies | Mở Chrome Settings → Allow cookies `ai.google.dev` |
| AI sửa hỏng giao diện | AI sinh code nhầm | Tìm điểm lưu trong Chat panel → Click **Restore** |
| Không bấm nút Publish được | Đã publish 2 apps trước đó | Vào Dashboard → Unpublish 1 app thử nghiệm cũ |
| AI tự bịa đặt tên cây (Fabrication) | Chưa có ràng buộc độ tin cậy | Dán câu lệnh ép Gemini trả nhãn "Không xác định" khi ảnh mờ |

---

## 📖 PHỤ LỤC D: GLOSSARY GIẢI NGHĨA THUẬT NGỮ

| Thuật ngữ | Giải thích đơn giản |
|---|---|
| **Vibe Coding** | Lập trình bằng cách mô tả ý định bằng ngôn ngữ tự nhiên, để AI tự sinh toàn bộ code. |
| **Spec-first Vibe Coding** | Triết lý lập trình với AI: Phải lập kế hoạch & viết đặc tả (Spec) chuẩn trước khi để AI sinh code. |
| **Yêu cầu (Requirements)** | Bóc tách bài toán thành người dùng, input, output, chức năng và ràng buộc. |
| **Đặc tả sản phẩm (Product Spec)** | Tài liệu tổng hợp mô tả "cần làm gì và tại sao" trước khi bắttay xây dựng. |
| **Build Mode** | Chế độ tạo ứng dụng trực tiếp bằng câu lệnh ngôn ngữ tự nhiên trong Google AI Studio. |
| **Live Preview** | Màn hình bên phải xem trực tiếp ứng dụng thật đang hoạt động. |
| **Annotation Mode (✏️)** | Công cụ dùng bút vẽ khoanh tròn lên màn hình để bảo AI sửa giao diện. |
| **Checkpoint & Restore** | Điểm tự động lưu lịch sử — giúp quay về bản cũ nếu AI làm hỏng app. |
| **Publish / Deploy** | Xuất bản ứng dụng thành đường link công khai trên Internet để ai cũng mở được. |
| **AI Fabrication (Ảo giác AI)** | Khái niệm kiểm thử: AI tự "sáng tạo" thêm thông tin không tồn tại khi thiếu ràng buộc khắt khe. |
| **Release Candidate** | Phiên bản ứng dụng đã vượt qua kiểm thử, sẵn sàng để xuất bản công khai. |

---

*Module 4 & Phụ lục — Phiên bản 1.1 | Khoá học: Phát Triển Ứng Dụng Với AI*
