# 📊 BÁO CÁO CHI TIẾT HẠN MỨC, MÃ MODEL ID GỌI API, ỨNG DỤNG GỢI Ý & PHÂN LOẠI FREE TIER - GEMINI API

- **Thời gian cập nhật:** 21/07/2026 (11:14:00 +07:00)
- **Nguồn dữ liệu:** Google AI Studio Dashboard
- **Phạm vi áp dụng:** Khóa học *"Phát triển sản phẩm AI cho Giáo viên STEM"* & Lập trình API / Build Mode

---

## 🟢 PHẦN 1: BẢNG MÔ HÌNH HOẠT ĐỘNG TRÊN FREE TIER (KÈM MÃ API MODEL ID & ỨNG DỤNG GỢI Ý)

Đây là các mô hình sẵn có hạn mức trên gói **Free Tier**. Dưới đây là **Mã Model ID chính xác để điền vào Code / API Call / Secret Config** cùng với **Ứng dụng gợi ý**:

| Tên mô hình (Model Name) | Mã Model ID gọi API (API Model String) | Quota Thực tế (RPM / TPM / RPD) | Ứng dụng gợi ý cho Giáo viên & Học sinh (Suggested Use-Cases) | Đánh giá & Lưu ý vận hành |
|---|---|---|---|---|
| **Gemini 3.5 Flash** | `gemini-3.5-flash` <br>*(hoặc `gemini-3.5-flash-latest`)* | 2 / 5 RPM <br> 3.08K / 250K TPM <br> 8 / 20 RPD | 💻 **Vibe Coding trong AI Studio Build Mode**, Xây dựng Web App full-stack React/Node, Phân tích đa phương thức (Ảnh lá cây), Viết tài liệu Spec & Plan. | 🔥 **Mô hình thông minh nhất trên Free Tier.** Cho chất lượng code và giao diện mượt nhất. Hạn mức **20 yêu cầu/ngày**, thích hợp cho Giảng viên Demo. |
| **Gemini 3.1 Flash Lite** | `gemini-3.1-flash-lite` <br>*(hoặc `gemini-3.1-flash-lite-latest`)* | 4 / 15 RPM <br> 457 / 250K TPM <br> 5 / 500 RPD | ⚡ **Chatbot tư vấn học tập, Trắc nghiệm tự động, Phân loại lá cây/động vật siêu nhanh, Chấm điểm bài tập ngắn.** | 🚀 **Tốt nhất cho lớp học đông.** Hạn mức ngày khổng lồ (**500 yêu cầu/ngày**), tần suất 15 RPM giúp cả lớp 30 học sinh thực hành không lo bị ngắt. |
| **Gemma 4 31B** | `gemma-4-31b-it` <br>*(hoặc `gemma-4-31b`)* | 4 / 30 RPM <br> 612 / 16K TPM <br> 7 / 14.4K RPD | 📚 **Xử lý hàng loạt tài liệu (Batch processing), Tóm tắt giáo án dài, Trích xuất dữ liệu thô, Chạy prompt dạng mã nguồn mở.** | 📦 Mô hình nguồn mở với hạn mức ngày cực lớn (**14,400 RPD**), tốc độ 30 RPM cao nhất. |
| **Gemini 2.5 Flash** | `gemini-2.5-flash` | 3 / 5 RPM <br> 452 / 250K TPM <br> 3 / 20 RPD | 🔍 Tra cứu kiến thức tiêu chuẩn, Hỏi đáp giáo án STEM cơ bản, Đọc file PDF/Hình ảnh đơn giản. | ⚙️ Mô hình tiêu chuẩn thế hệ 2.5, hoạt động ổn định cho tác vụ thường nhật. |
| **Gemini 2.5 Flash Lite** | `gemini-2.5-flash-lite` | 1 / 10 RPM <br> 1 / 250K TPM <br> 1 / 20 RPD | 🧪 Trích xuất JSON siêu nhẹ, Phân loại từ khóa, Kiểm tra lỗi cú pháp prompt. | ⚡ Tốc độ phản hồi cực nhanh, làm helper function cho ứng dụng. |
| **Gemini 3.1 Flash TTS** | `gemini-3.1-flash-tts` | 0 / 3 RPM <br> 0 / 10K TPM <br> 0 / 10 RPD | 🔊 **Chuyển bài giảng/Tên cây Latinh thành giọng nói (Text-to-Speech)** cho app Tiếng Anh/Sinh học. | 🎵 Hỗ trợ 10 lượt phát âm giọng nói/ngày trên gói miễn phí. |
| **Imagen 4 Generate** | `imagen-3.0-generate-002` <br>*(hoặc `imagen-4-generate`)* | 0 / 25 RPD | 🎨 **Tạo ảnh minh họa linh vật STEM, Ảnh nền bài giảng, Sáng tạo hình ảnh học tập chất lượng cao.** | 🖼️ Cho phép tạo 25 hình ảnh AI độ phân giải cao mỗi ngày bằng hàm `generateImages`. |
| **Gemini Robotics ER 1.6** | `gemini-robotics-er-1.6-preview` | 0 / 5 RPM <br> 0 / 250K TPM <br> 0 / 20 RPD | 🤖 **Lập trình điều khiển Robot STEM, Cảm biến Arduino/Raspberry Pi, Nhận diện không gian học tập.** | 🦾 Mô hình AI chuyên dụng cho các dự án phần cứng STEM. |

---

## 🔴 PHẦN 2: BẢNG CÁC MÔ HÌNH BỊ KHÓA TRÊN FREE TIER (`0 / 0`) & LÝ DO CHI TIẾT

Dưới đây là danh sách các mô hình hiển thị chỉ số **`0 / 0`** (Không có hạn mức) trên gói Free Tier:

| Tên mô hình (Model Name) | Mã Model ID gọi API (API Model String) | Phân loại | Ứng dụng gợi ý nếu được kích hoạt | Lý do không sử dụng được trên Free Tier hiện tại |
|---|---|---|---|---|
| **Gemini 2.5 Pro** & **3.1 Pro** | `gemini-2.5-pro` <br> `gemini-3.1-pro` | Pro Text-out | 🧩 Giải các bài toán STEM chuyên sâu phức tạp, Refactor dự án code lớn, Viết sách/tài liệu khoa học. | ⛔ **Yêu cầu Tài khoản Trả phí (Paid Tier / Pay-as-you-go).** Các dòng **Pro** tốn tài nguyên tính toán cao nên Google không cấp quota miễn phí mặc định. |
| **Nano Banana Series** *(Gemini Flash Image)* | `gemini-2.5-flash-image` <br> `nano-banana-2-gemini-3.1-flash-image` | Multi-modal Image | 🖼️ Sửa ảnh thông minh, Chèn vật thể AI trực tiếp trên màn hình Live Preview của App. | ⛔ **Tài khoản Free Tier bị khóa Quotas (0/0 RPD).** Gọi mã `gemini-2.5-flash-image` bằng API sẽ bị lỗi HTTP 403/404 (`QuotaExceeded` hoặc `Model Not Found`). |
| **Deep Research Pro Preview** | `deep-research-pro-preview` | Agent Tool | 🔬 Tự động thu thập, tổng hợp và viết báo cáo nghiên cứu từ hàng ngàn tài liệu web. | ⛔ **Tính năng Enterprise / Paid Agent.** Chỉ dành cho tài khoản nâng cao có liên kết thẻ thanh toán (Billing Enabled). |
| **Computer Use Preview** | `computer-use-preview` | Agent Tool | 🖥️ AI tự động điều khiển chuột, bàn phím và thao tác ứng dụng trên máy tính. | ⛔ **Tính năng Preview Giới Hạn (Gated Preview).** Yêu cầu đăng ký danh sách chờ (Waitlist) & đăng ký Billing dự án Google Cloud. |
| **Veo 3 Series** *(Generate)* | `veo-3-generate` <br>*(Fast: `veo-3-fast-generate`)* | Video Generation | 🎬 Tạo video hoạt hình minh họa bài giảng STEM, Video thí nghiệm khoa học mô phỏng. | ⛔ **Mô hình Video AI chi phí cao.** Chỉ hỗ trợ qua dự án Google Cloud Vertex AI (Paid Project) hoặc dự án có cấu hình Billing riêng. |
| **Lyria 3 Clip** | `lyria-3-clip` | Audio/Music | 🎼 Sáng tác nhạc nền cho trò chơi học tập STEM, Hiệu ứng âm thanh giáo dục. | ⛔ **Mô hình Thử nghiệm Đối tác (Partner Preview).** Chưa mở rộng công khai trên Free Tier API. |
| **Gemini 3.5 Live Translate** | `gemini-3.5-live-translate` | Live API | 🎙️ Phiên dịch trực tiếp thời gian thực cuộc gọi thoại/video song ngữ trên App. | ⛔ **Yêu cầu kênh kết nối WebSocket/Streaming trả phí.** Gói Free Tier không mở băng thông Live Stream thời gian thực. |

---

## ❓ PHẦN 3: GIẢI MÃ LỖI — VÌ SAO THAY `imagen-4-generate` BẰNG `gemini-2.5-flash-image` KHÔNG TẠO ĐƯỢC ẢNH?

Khi anh thay chuỗi `imagen-4-generate` bằng `gemini-2.5-flash-image` (hoặc các mô hình thuộc dòng Nano Banana Image) trong code và chạy thử, chương trình báo lỗi hoặc không sinh ra ảnh. Dưới đây là **3 nguyên nhân kỹ thuật chính**:

### 1. Nguyên nhân 1: Free Tier không được cấp Quota cho `gemini-2.5-flash-image`
* Hãy nhìn vào bảng Dashboard của anh: Mô hình **`Nano Banana (Gemini 2.5 Flash Preview Image)`** hiển thị chỉ số **`0 / 0`** (0 RPM, 0 TPM, 0 RPD).
* Google khóa toàn bộ endpoint này đối với API Key miễn phí. Khi gọi qua API, Google Server lập tức trả về lỗi: `403 Quota Exceeded` hoặc `404 Model Not Found`.
* Ngược lại, **`Imagen 4 Generate`** (`imagen-3.0-generate-002`) được cấp **25 RPD/ngày miễn phí**.

### 2. Nguyên nhân 2: Khác biệt về Phương thức trong SDK (`generateImages` vs `generateContent`)
* **Imagen 4** là mô hình chuyên sinh ảnh thuần túy, phải gọi bằng phương thức:
  ```typescript
  // Node.js SDK
  const result = await ai.models.generateImages({
    model: "imagen-3.0-generate-002", // hoặc imagen-4-generate
    prompt: "A cute green plant mascot",
    config: { numberOfImages: 1, outputMimeType: "image/png" }
  });
  ```
* **Gemini Flash Image** là mô hình ngôn ngữ hỗ trợ xuất ảnh đa phương thức, phải gọi bằng `generateContent` kèm cấu hình `responseMimeType`:
  ```typescript
  // Nếu dùng Gemini Flash Image (Chỉ chạy được trên Paid Tier)
  const result = await ai.models.generateContent({
    model: "gemini-2.5-flash-image", // Bị khóa trên Free Tier!
    contents: ["Generate an image of a cute green plant mascot"],
    config: { responseMimeType: "image/png" }
  });
  ```
  Nếu anh dùng hàm `generateImages` mà truyền vào `gemini-2.5-flash-image`, SDK sẽ báo lỗi không khớp phương thức.

---

## 💡 HƯỚNG DẪN XỬ LÝ CHO GIẢO VIÊN & LẬP TRÌNH VIÊN (RECOMMENDED SOLUTIONS)

### 🛠️ CÁCH 1: Dùng đúng Imagen 4 / Imagen 3 trên Free Tier (25 ảnh/ngày)
Sử dụng chuẩn Model ID **`imagen-3.0-generate-002`** hoặc **`imagen-4-generate`** với hàm `generateImages`:

* **Mẫu Code Python:**
  ```python
  from google import genai

  client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

  result = client.models.generate_images(
      model="imagen-3.0-generate-002",
      prompt="A cute green plant mascot illustration for STEM biology class",
      config=dict(number_of_images=1, aspect_ratio="1:1")
  )

  # Lấy ảnh
  for generated_image in result.generated_images:
      image_bytes = generated_image.image.image_bytes
  ```

### 🎨 CÁCH 2: Dùng `gemini-3.5-flash` Sinh Code SVG / Canvas (0đ - Không tốn Quota Imagen)
Trong AI Studio Build Mode, để tạo hình ảnh/icon minh họa cho Web App mà không tốn 25 lượt/ngày của Imagen, ta có thể yêu cầu **`gemini-3.5-flash`** vẽ trực tiếp bằng code SVG:

* **Prompt cho AI Studio:**
  ```text
  Create a React component for a cute plant mascot rendered purely using SVG code.
  Do not call external image APIs.
  ```
* **Ưu điểm:** Chạy 100% miễn phí, đẹp mắt, tự động co giãn (responsive), không bao giờ bị lỗi API Key hay hết Quota ảnh!

---

*Báo cáo giải mã lỗi API được cập nhật trực tiếp vào tài liệu.*  
*Đường dẫn tệp:* `D:\NoteBookLLM_Br\workspaces\learning\outputs\bao_cao_quota_su_dung_gemini_api.md`
