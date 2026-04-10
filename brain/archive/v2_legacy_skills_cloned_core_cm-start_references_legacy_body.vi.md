# 🚀 Workflow Orchestrator (LITE)

> **Goal:** Kích hoạt quy trình làm việc từ ý tưởng đến sản phẩm hoàn chỉnh. Phân tích độ phức tạp, thiết lập bộ nhớ và điều phối các kỹ năng (Skills) phù hợp để thực thi mục tiêu của User.

## 🛠️ The Startup Sequence
1. **Load Memory:** Đọc `CONTINUITY.md` → Cập nhật `Active Goal` với mục tiêu mới.
2. **Skill Check:** Quét Triggers trong yêu cầu → Nếu thiếu Skill → `npx skills find`.
3. **Intelligence Setup:** Chạy `cm-codeintell` để lấy cấu trúc Skeleton dự án.
4. **Complexity Detection:** Phân loại yêu cầu theo các cấp độ L0 đến L3.

## 📊 Project Complexity Levels
| Level | Scope | Recommended Workflow |
|---|---|---|
| **L0 (Micro)** | Sửa lỗi nhỏ, 1 file. | `cm-tdd` → `cm-quality-gate`. |
| **L1 (Small)** | Tính năng nhỏ, <3 file. | `cm-planning` (Lite) → `tdd` → `safe-deploy`. |
| **L2 (Medium)**| Tính năng phức tạp. | `brainstorm` → `planning` → `tdd` + `execution`. |
| **L3 (Large)** | Module mới/Refactor lớn.| `brainstorm` (Mandatory) → `planning` → `sprint`. |

## 📐 Progress Tracking
- **Task Breakdown:** Tự động chia nhỏ mục tiêu thành các task L1-L4 trong `task.md`.
- **Command:** Gợi ý User dùng `/cm-dashboard` để xem Kanban hoặc `/cm-status`.
- **Handoff:** Chuyển giao ngữ cảnh cho `cm-planning` hoặc `cm-execution`.

## 🚨 Quality Gate (Red Flags)
- ❌ Nhảy vào thực thi mà chưa xác định được cấp độ phức tạp (L-Level).
- ❌ Bỏ qua bước kiểm tra danh tính (`cm-identity-guard`) khi làm dự án mới.
- ❌ Không cập nhật bộ nhớ làm việc ngay từ bước Start.
- ❌ Thiếu các bước kiểm tra công nghệ (Skill Coverage) dẫn đến dùng sai công cụ.

## 💡 Example Triggers
- "/cm-start [mục tiêu của bạn]"
- "Bắt đầu làm tính năng X."
- "Khởi động quy trình cho task Y."

## Phase Mode (v5)
When taxonomy or skill-pack refactor is requested, run in 2 phases:
1. Phase 1 - Stabilize: fix broken links, add alias mapping, run validator.
2. Phase 2 - Refactor: rename legacy folders, sync frontmatter names, update index/router.

Hard rule: do not merge Phase 2 until Phase 1 checks pass.

