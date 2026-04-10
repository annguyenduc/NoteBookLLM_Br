# 🚀 Document Publishing (LITE)

> **Goal:** Tự động hóa sản xuất tài liệu STEAM chuyên sâu (Lesson plan, Slide, Digibook) thông qua chuỗi kỹ năng (Skill Chain) có kiểm soát chất lượng (Quality Gate).

## 🛠️ 3-Step Pipeline Flow
| Step | Action | Delegate Skills |
|---|---|---|
| **1. CONTENT** | Soạn thảo 5E/SOP/Worksheet. | `module-architect`, `cm-dockit`, `steam-content-factory`. |
| **2. RENDER** | HTML Preview (Review bố cục). | `cm-vn-typography`, `math-renderer`. |
| **3. PUBLISH** | Convert HTML → Final Output. | `cm-pptx-converter` (PPTX/DOCX). |

## 📐 Design & Styling (B2B Standards)
- **Palette:** Navy (`#134A85`) Header, Off-white background.
- **Font:** Montserrat (Heading), Arial (Body).
- **Presentation:** 16:9 ratio, **KHÔNG dùng `overflow-y: auto`**.
- **Media:** `max-height: 55vh` cho ảnh slide.

## 🚨 Quality Gate (Red Flags)
- ❌ Slide vượt quá 5 bullet points (Bắt buộc phải tách Slide).
- ❌ Thiếu dấu tiếng Việt hoặc vỡ font (Dùng `cm-vn-typography`).
- ❌ Render không khớp với PPTX Converter (Kiểm tra lại CSS rules).
- ❌ Chạy Bước 3 khi Bước 2 chưa được người dùng duyệt (Review required).

## 💡 Example Triggers
- "Tạo tài liệu B2B cho bài học AI lớp 10."
- "Làm slide đào tạo giáo viên từ bài soạn 5E."
- "Xuất bản bộ giáo án word cho module Robotics."

