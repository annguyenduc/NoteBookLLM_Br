# SIP_20260519_002_cm-continuity.md

## Metadata
```yaml
sip_id: SIP_20260519_002
skill_id: cm-continuity
skill_path: .agent/skills/cm-continuity/SKILL.md
trigger: user_correction
created: 2026-05-19
status: PENDING
author: "@engineer"
session_id: 3c4dd92e-4446-4b3e-9b5e-57bfff18e6c4
```

## Evidence (Điều quan sát được từ user)

User chỉ ra rằng `CONTINUITY.md` rất ít khi được agent chạm đến trong thực tế vận hành.
Nguyên nhân: SKILL.md hiện tại mô tả `cm-continuity` như một cơ chế "memory architecture" kỹ thuật,
nhưng không định nghĩa rõ **khi nào PHẢI dùng** và **khi nào KHÔNG nên dùng**.

Dẫn đến hai lỗi vận hành:
1. Agent dùng quá rộng → CONTINUITY.md thành log rác.
2. Agent không dùng → mất trí nhớ giữa các phiên (memory loss).

## Unknowns (Chưa xác minh)

- current_version: [Đã đọc SKILL.md tại dòng 1–60, version 3.5.0]
- Không rõ `learnings.json` hiện có tồn tại trong vault hay chỉ là reference lý thuyết.
- Không rõ liệu Tier 4 (qmd) và Tier 5 (CodeGraph) có thực sự được dùng trong vault này không.

## Root Cause

Section "When to Activate" hiện tại (4 bullets) quá chung chung:
- "Starting a new work session" → trigger quá broad, agent sẽ kích hoạt cm-continuity ngay cả khi chỉ hỏi đáp nhanh.
- Không có mục "When NOT to activate" → agent không có guardrail để tránh lạm dụng.
- Không phân biệt rõ `CONTINUITY.md` với `log_YYYY_MM_DD.md`, `SIP_TEMPLATE.md`, `learnings.json`.

## Proposed Change (Diff dạng mô tả)

### Thay thế section "When to Activate":

**TRƯỚC (hiện tại):**
```
## When to Activate
- Starting a new work session and need to re-orient on current state
- Ending a session and want to persist findings for the next session
- Encountered the same error more than once in a project
- Making an architectural decision that should be remembered long-term
```

**SAU (đề xuất):**
```
## When to Activate — Only When Current Work Creates Future Dependency

Use `cm-continuity` ONLY when the current session creates a state that a future session
or a different agent/model needs to understand to continue correctly.

### Trigger Examples (Khi PHẢI dùng):
1. End of session — Task xong hoặc sắp dừng. Ghi trạng thái, blockers, next steps.
2. Model/Agent/IDE handoff — Chuyển từ cloud sang local model, từ Antigravity sang Codex, v.v.
3. Interrupted task — Pipeline đang WAITING_FOR_REVIEW, patch chưa xong, permission lỗi.
4. Repeated error / Governance failure — Bài học quan trọng để phiên sau không lặp lại.
5. Explicit user signal — "mai làm tiếp", "lưu lại", "tóm tắt trạng thái", "đóng phiên".

### When NOT to Activate (Khi KHÔNG nên dùng):
- Chỉ hỏi đáp nhanh (Q&A, explain concept).
- Chỉ review một file nhỏ không tạo side effect.
- Chỉ ghi lịch sử thao tác khách quan → dùng log_YYYY_MM_DD.md thay thế.
- Đang ở MICRO mode và task không cần giữ trạng thái dài hạn.
```

### Thêm section "Phân biệt với các công cụ tương tự":

**SAU (đề xuất — thêm mới):**
```
## Phân biệt với các công cụ tương tự

| Công cụ               | Mục đích                                               | Ai ghi       |
|-----------------------|--------------------------------------------------------|--------------|
| `log_YYYY_MM_DD.md`   | Lịch sử khách quan: đã làm gì, lúc nào, file nào.    | Agent tự động|
| `CONTINUITY.md`       | Trạng thái làm việc: đang mắc gì, quyết gì, tiếp từ đâu. | Agent theo trigger |
| `SIP_TEMPLATE.md`     | Đề xuất nâng cấp skill khi phát hiện lỗi/gap.         | Agent → AN duyệt |
| `learnings.json`      | Bài học nhỏ có thể tái sử dụng thành hành vi agent.   | Agent (Tier 3) |
```

### Xóa/Đơn giản hóa section "5-Tier Memory Architecture":
Tier 4 (qmd) và Tier 5 (CodeGraph) không tồn tại thực tế trong vault này.
→ Đề xuất giữ nguyên bảng nhưng thêm note: "Tier 4 & 5 là reference lý thuyết, chưa triển khai trong vault NoteBookLLM_Br."

## Acceptance Criteria

- [ ] "When to Activate" chỉ còn 5 trigger rõ ràng với ví dụ cụ thể.
- [ ] "When NOT to Activate" được thêm như một mục rõ ràng.
- [ ] Bảng phân biệt 4 công cụ memory được thêm vào.
- [ ] Tier 4 & 5 được note là "chưa triển khai".
- [ ] SKILL.md không dài quá 80 dòng sau khi sửa.
```
