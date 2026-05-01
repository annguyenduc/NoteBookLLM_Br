---
trigger: model_decision
---

# 🧩 ECC CORE RULES (v1.0)

> **Mô hình**: Planner -> TDD -> Reviewer

## 1. Vai trò Planner (@pm / @scout)
- Luôn phải lập kế hoạch (`implementation_plan.md`) trước khi thực hiện các thay đổi phức tạp.
- Yêu cầu feedback từ người dùng (`request_feedback = true`) cho các quyết định kiến trúc.

## 2. Vai trò TDD (@engineer / @healer)
- Viết test/tiêu chí kiểm tra trước khi viết logic.
- Sử dụng cơ chế `Self-healing` để tự sửa lỗi dựa trên log terminal.

## 3. Vai trò Reviewer (@librarian / @qa)
- Rà soát tính toàn vẹn của LOM và các liên kết `[[Wikilinks]]`.
- Đảm bảo tuân thủ `CLAUDE.md`.

---
*Thuộc dự án: NoteBookLLM_Br | Workflow: ECC Transition*
