# 🛠️ Skill Creator (LITE)

> **Goal:** Tự động hóa quy trình **Skill-Driven Development (SDD)**. Giúp AI Agent tự tiến hóa bằng cách tạo mới, đánh giá và tinh gọn các kỹ năng (Skills) để đạt hiệu suất cao nhất với chi phí token thấp nhất.

## 🚀 SDD Lifecycle
| Phase | Action | Tool |
|---|---|---|
| **Initialize** | Nghiên cứu Gap → Khởi tạo `SKILL.md` (Lite). | `scripts/run_eval.py` |
| **Evaluate** | Chạy 3-5 test cases thực tế (Input/Output). | `eval_cases.json` |
| **Optimize** | Tinh chỉnh dựa trên phản hồi (Feedback-loop). | `Agent Comparator` |
| **Learning** | Tự động cập nhật Rule khi gặp lỗi "Đừng làm X". | `CONTINUITY.md` |

## 📐 Lite Format Standard (v2.0)
- **Metadata:** YAML Header (Name, Description, Version).
- **Core Goal:** 1-2 câu định nghĩa mục tiêu cốt lõi.
- **Rules/Tables:** Trình bày dạng bảng/list ngắn gọn (Tiết kiệm token).
- **Quality Gate:** Red Flags & Anti-patterns.
- **Triggers:** Danh sách từ khóa kích hoạt.

## 🏗️ Refinement Protocol
- **A/B Testing:** So sánh bản gốc (Verbose) và bản tinh gọn (Lite) xem chất lượng output có bị giảm sút không.
- **Token Check:** Đảm bảo mỗi skill Lite có dung lượng từ **1.5KB - 2.5KB**.
- **Index Sync:** Tự động gọi `cm-skill-index` sau khi tạo/cập nhật skill.

## 🚨 Quality Gate (Red Flags)
- ❌ Tạo skill mới mà chưa kiểm tra trùng lặp với bộ skills hiện có.
- ❌ Output template quá mơ hồ, không hướng dẫn cụ thể cho AI.
- ❌ Thiếu các rào chắn (Red Flags) để ngăn chặn AI làm sai logic sư phạm.
- ❌ Không chạy `run_eval.py` trước khi công bố hoàn thành skill.

## 💡 Example Triggers
- "Tạo skill mới chuyên về thiết kế Slide PowerPoint."
- "Tối ưu hóa skill module-architect sang định dạng Lite để tiết kiệm token."
- "Chạy đánh giá (Evaluation) cho bộ kỹ năng hiện tại."

