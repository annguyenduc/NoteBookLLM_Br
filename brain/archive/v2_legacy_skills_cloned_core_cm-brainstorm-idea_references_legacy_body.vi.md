# 💡 Brainstorm Idea (LITE)

> **Goal:** Hiểu sâu bản chất vấn đề trước khi lập kế hoạch. Sử dụng tư duy hệ thống (TRIZ) và thiết kế (Design Thinking) để đưa ra 2-3 phương án giải quyết tối ưu, tránh việc nhảy vội vào code khi chưa rõ ràng.

## 🚀 The 5-Phase Strategic Workflow
| Phase | Action | Goal |
|---|---|---|
| **1. Discover** | Codebase Scan + User Interview. | Hiểu hiện trạng & Nỗi đau (Pain points). |
| **2. Define** | TRIZ 9 Windows Analysis. | Xác định "Vấn đề thực sự" (Real Problem). |
| **3. Develop** | Ideation (Diverge). | Đề xuất 2-3 Option khác biệt về bản chất. |
| **4. Evaluate** | Scoring Matrix (Converge). | Chấm điểm & Khuyến nghị Option tốt nhất. |
| **5. Handoff** | Package cho `cm-planning`. | Chuyển giao ngữ cảnh sạch để lập kế hoạch. |

## 📐 TRIZ 9 Windows Matrix
Phân tích vấn đề qua 3 tầng hệ thống và 3 mốc thời gian:
- **Tầng:** Siêu hệ thống (Ecosystem) / Hệ thống (Product) / Hệ thống con (Components).
- **Thời gian:** Quá khứ / Hiện tại / Tương lai.

## 📈 Multi-Dimensional Scoring
Chấm điểm các Option dựa trên:
- **Tech (25%):** Khả thi, bảo trì, mở rộng.
- **Product (30%):** Giá trị người dùng, PMF.
- **Design (20%):** UX/UI, độ tinh tế (Polish).
- **Business (25%):** ROI, Tốc độ ra mắt, Chiến lược.

## 🏗️ UI Preview Integration (Phase 4.5)
Nếu Option liên quan đến UI, đề xuất User xem Preview trước khi Plan:
- **Tool:** Tự động chọn Google Stitch (Nhanh) hoặc Pencil (Kiểm soát chi tiết).
- **Action:** Ủy quyền cho `cm-ui-preview` tạo concept screens.

## 🚨 Quality Gate (Red Flags)
- ❌ Chỉ đưa ra **MỘT** phương án duy nhất (Không có lựa chọn = Phân tích kém).
- ❌ Propose 4+ phương án (Gây tê liệt quyết định).
- ❌ Nhảy thẳng vào Planning khi chưa qua bước Define vấn đề thực sự.
- ❌ Bỏ qua bước ước tính công sức (Effort Estimation) cho mỗi Option.

## 💡 Example Triggers
- "Chúng ta nên cải tiến tính năng này như thế nào?"
- "Brainstorm các hướng phát triển tiếp theo cho dự án."
- "Phân tích 9 Windows cho vấn đề hiệu suất tải trang."
