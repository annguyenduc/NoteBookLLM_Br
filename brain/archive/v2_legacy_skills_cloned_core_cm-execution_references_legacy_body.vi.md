# 🚀 Execution Engine (LITE)

> **Goal:** Thực thi kế hoạch một cách hệ thống, tối ưu tốc độ thông qua xử lý song song (TRIZ-Parallel) và đảm bảo chất lượng bằng vòng lặp tự trị (RARV).

## 🛠️ Execution Modes
| Mode | When to Use | Strategy |
|---|---|---|
| **A: Batch** | Kế hoạch có các checkpoint rõ ràng. | Thực thi 3 tasks → Báo cáo → Feedback → Tiếp tục. |
| **B: Subagent**| Các task độc lập trong cùng session. | 1 subagent/task + Quy trình review 2 bước. |
| **C: Parallel** | Hệ thống bị hỏng ở nhiều module độc lập. | 1 agent cho mỗi module để tránh xung đột context. |
| **D: RARV** | Thực thi tự trị hoàn toàn (Autonomous). | **R**eason → **A**ct → **R**eflect → **V**erify. |
| **E: TRIZ-Parallel**| Cần Tốc độ + Chất lượng tối đa. | Phân đoạn task theo dependency graph + Quality Gates. |

## ⚖️ Two-Stage Review (Subagent Mode B)
Quy trình "Review Chéo" bắt buộc khi giao việc cho Subagent để bảo vệ chất lượng dự án (Subagent-Driven-Development):
1. **Stage 1 (Spec Compliance - Yêu cầu):** So sánh kết quả Subagent trả về với thiết kế/mục tiêu ban đầu. Phải đáp ứng ĐÚNG & ĐỦ logic thiết kế. Nếu sai/thiếu -> Từ chối kết quả.
2. **Stage 2 (Code Quality - Chất lượng):** Chỉ khi Stage 1 pass, lúc này mới đánh giá Code Smell, Security (XSS, Injection, Path Traversal) và TDD Coverage. NẾU dở -> Bắt refactor.

## 🛡️ Security Rules (Cấm vi phạm)
- **Frontend:** Không dùng `innerHTML` với dữ liệu thô (Tránh XSS). Dùng `textContent`.
- **Backend (Python):** Không dùng `shell=True` trong `subprocess`. Dùng list arguments.
- **Path Safety:** Luôn dùng `safe_resolve()` để chặn Path Traversal.

## 📐 RARV Operation Loop (Mode D)
1. **Reason:** Đọc `cm-tasks.json` → Chọn task ưu tiên cao nhất.
2. **Act:** Sử dụng skill chuyên biệt (cm-tdd, cm-debugging) để xử lý.
3. **Reflect:** Cập nhật kết quả vào bộ nhớ và task log.
4. **Verify:** Chạy `cm-quality-gate`. Nếu FAIL → Retry (Max 3 lần) → Nếu vẫn FAIL → Block.

## 🚨 Quality Gate (Red Flags)
- ❌ Thực thi khi chưa Audit Skill Coverage (Thiếu công cụ cần thiết).
- ❌ Merge code khi Tests đang fail hoặc chưa qua Review.
- ❌ Không cập nhật trạng thái Task vào `cm-tasks.json` theo thời gian thực.
- ❌ Bỏ qua Pre-flight check của `cm-codeintell` dẫn đến sửa nhầm module.

## 💡 Example Triggers
- "Bắt đầu thực thi Batch 1 của implementation plan."
- "Chạy chế độ TRIZ-Parallel cho các task UI này."
- "RARV: Tự động hoàn thành danh sách task trong backlog."
