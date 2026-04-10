# 🎨 UI Preview Orchestrator (LITE)

> **Goal:** "Thấy trước khi xây". Chuyển đổi các yêu cầu mơ hồ thành "Bản thiết kế kỹ thuật" (Construction Blueprint) để Google Stitch hoặc Pencil.dev tạo ra Prototype chuyên nghiệp, nhất quán với thương hiệu.

## 🚀 The 5-Step Design Pipeline
1. **P1: Preflight:** Xác định mục tiêu (Mới vs Sửa) và kiểm tra kết nối MCP (Stitch/Pencil).
2. **P2: Extraction:** Tìm `DESIGN.md` hoặc Design Tokens hiện có làm "Source of Truth".
3. **P3: Enhancement:** Nâng cấp Prompt thô thành Blueprint chi tiết (Vibe, Palette, Typography, Layout).
4. **P4: Execution:** Gọi `create_project` và `generate_screen_from_text`. Trình link cho User.
5. **P5: Finalization:** User chọn: **Xác nhận** (Để AI viết code) / **Sửa** (Iterate) / **Bỏ qua**.

## 📐 Prompt Enhancement Structure
Không bao giờ gửi prompt ngắn kiểu "Làm trang login". Phải cấu trúc:
- **Project Vibe:** Bối cảnh, đối tượng người dùng, phong cách (Hiện đại, tối giản).
- **Design System:** Nền tảng (Web/Mobile), Palette màu (Hex), Typography, Border-radius.
- **Page Structure:** Chia nhỏ thành các khu vực: Nav, Hero, Main Area, Action Bar (CTA).

## 🛠️ Tool Interaction
- **Google Stitch:** Nhanh, tạo Prototype từ văn bản. Dùng `generate_screen_from_text`.
- **Pencil.dev:** Kiểm soát chi tiết mức pixel, đồng bộ Design System. Dùng `batch_design`.
- **Continuity:** Lưu trạng thái thiết kế vào `.stitch/next-prompt.md` để đồng bộ phiên sau.

## 🚨 Quality Gate (Red Flags)
- ❌ Viết code React/Vue ngay lập tức mà chưa qua bước xác nhận Prototype.
- ❌ Gửi prompt quá mơ hồ cho Stitch dẫn đến kết quả không như ý.
- ❌ Giả định kết quả thành công khi MCP bị lỗi (Không được "ảo tưởng" link).
- ❌ Quên áp dụng các luật UX cơ bản (Miller's Law, Fitts's Law) vào bản thiết kế.

## 💡 Example Triggers
- "Thiết kế trang Dashboard cho ứng dụng quản lý tài chính."
- "Dùng Stitch để tạo Prototype cho Landing Page này."
- "Cải thiện giao diện hiện tại cho chuyên nghiệp hơn."
