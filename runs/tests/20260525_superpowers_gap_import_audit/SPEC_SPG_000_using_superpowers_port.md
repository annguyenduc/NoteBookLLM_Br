# SPEC-SPG-000: Port and Normalize using-superpowers as bootstrap standard (REVISED)

> **Trạng thái:** DỰ THẢO ĐÃ CẬP NHẬT (Chờ phê duyệt - Requires AN GO)
> **Mã hiệu:** SPEC-SPG-000
> **Giai đoạn:** Giai đoạn 2 — Core Phase 0 Adoption (Kích hoạt cổng chào)
> **Mục tiêu:** Port và chuẩn hóa `using-superpowers` của Superpowers làm chuẩn bootstrap chính cho Antigravity, tích hợp phần thích nghi cục bộ của vault theo các nguyên tắc an toàn nâng cao.

---

## 1. Bối cảnh & Lý do
Kỹ năng `using-superpowers` là kim chỉ nam kỷ luật để Agent nhận diện, lựa chọn và đọc các kỹ năng phương pháp luận đầu phiên. Bản sửa đổi này bổ sung các nguyên tắc tối ưu hóa token budget, phân cấp độ ưu tiên chỉ thị, định rõ ranh giới brainstorming và synthesis, đồng thời thiết lập phương án khôi phục (rollback) và kiểm thử (testing) chặt chẽ.

---

## 2. Mã nguồn nguồn & Đích đến
*   **Mã nguồn tham chiếu (Source):** `workspaces/refs/superpowers/skills/using-superpowers/SKILL.md`
*   **Tệp tin đích (Target Destination):** `.agent/skills/using-superpowers/SKILL.md`

---

## 3. Nội dung thiết kế kỹ thuật (Implementation Details)

Tệp tin đích `.agent/skills/using-superpowers/SKILL.md` sẽ được tạo ra bằng cách gộp bản gốc của Superpowers với các cấu phần thích nghi đặc thù sau:

### A. Phân cấp độ ưu tiên chỉ thị (Instruction Priority)
*   **Mức 1 (Cao nhất):** Chỉ thị trực tiếp từ người dùng trong chat và tệp tin luật lõi `AGENTS.md`.
*   **Mức 2:** Các kỹ năng phương pháp luận của Superpowers (override hành vi mặc định khi có xung đột).
*   **Mức 3:** Tệp tin lưu trạng thái liên phiên **`CONTINUITY.md`** (chỉ đóng vai trò là **state memory** phục vụ tính liên tục ngữ cảnh, tuyệt đối không đứng ngang hàng hay override chỉ thị trực tiếp hoặc `AGENTS.md`).
*   **Mức 4 (Thấp nhất):** System prompt mặc định.

### B. Tối ưu hóa Token Budget trước Clarifying Questions
*   Trước khi đưa ra câu hỏi làm rõ (clarifying questions) cho người dùng, Agent **chỉ được phép kiểm tra các tệp nhẹ như index hoặc router** (`lightweight router/index check`).
*   Tuyệt đối **không nạp toàn bộ tệp tin skill dài** nếu chưa xác định chắc chắn hướng định tuyến dự kiến (`likely route`), tránh gây lãng phí Token Budget và làm phình context vô ích.

### C. Định rõ ranh giới Brainstorming & Synthesis
*   **Ranh giới `brainstorming`:** Kỹ năng này chỉ được phép sử dụng cho mục đích tìm kiếm, khám phá ý tưởng và phác thảo thiết kế nháp (exploration & design). **Cấm tuyệt đối** việc Agent tự ý tạo mới, thăng cấp (promote), hoặc ghi đè các canonical atom trực tiếp. Mọi canonical atom bắt buộc phải đi qua ingest/absorb workflow chính quy và có sự phê duyệt tường minh (AN GO).
*   **Phạm vi `synthesis_guard.py`:** Chỉ kích hoạt bắt buộc trước khi thực hiện hành động ghi (write operation) vào các thư mục chịu sự kiểm soát tổng hợp (*synthesis-controlled paths* - ví dụ: `3-resources/wiki/`). Nếu phát hiện thiếu guard hoặc guard bị lỗi, Agent **phải dừng ngay lập tức và báo cáo lỗi** cho người dùng, cấm bypass.

### D. Thông báo linh hoạt (`🔧 Using...`)
*   Dòng thông báo kích hoạt kỹ năng `🔧 Using [skill] to [purpose]` **chỉ bắt buộc hiển thị trong audit/test mode**.
*   Đối với **normal user-facing mode** (trò chuyện thường nhật với người dùng), Agent không bắt buộc phải xuất dòng này nhằm duy trì hội thoại tự nhiên, sạch sẽ.

---

## 4. Dự thảo nội dung tệp tin đích `.agent/skills/using-superpowers/SKILL.md`

```markdown
---
name: using-superpowers
description: Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions
---

<SUBAGENT-STOP>
If you were dispatched as a subagent to execute a specific task, skip this skill.
</SUBAGENT-STOP>

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. This is not optional. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

## Instruction Priority

Superpowers skills override default system prompt behavior, nhưng **chỉ thị của người dùng luôn có mức ưu tiên cao nhất**:

1. **User's explicit instructions & AGENTS.md** — Highest priority (Quyết định tối cao của AN)
2. **Superpowers skills** — Override default system behavior where they conflict
3. **CONTINUITY.md** — State memory phục vụ liên phiên, không dùng để override chỉ thị trực tiếp hay luật lõi.
4. **Default system prompt** — Lowest priority

**NoteBookLLM_Br Overrides & Ranh giới an toàn:**
- `brainstorming` skill: Chỉ dùng cho exploration/design nháp. Cấm tuyệt đối tự ý tạo/promote/ghi đè canonical atom khi chưa có ingest workflow và AN GO.
- `synthesis/` directory: Bắt buộc gọi `synthesis_guard.py` check trước mọi write operation vào synthesis-controlled paths. Nếu guard thiếu/lỗi, PHẢI DỪNG LẠI và báo cáo lỗi ngay lập tức.
- **Git Safety Rule:** Cấm tuyệt đối Agent tự động commit hoặc push code lên remote.

## How to Access Skills & Platform Adaptation

In **Antigravity engine**, skills are local Markdown files located under `.agent/skills/`. 
- **Activation tool:** Để kích hoạt và đọc kỹ năng, agents sử dụng công cụ `view_file` trên tệp `SKILL.md` tương ứng.
- **Token Optimization Rule:** Trước khi đưa ra clarifying question, chỉ check lightweight router/index trước; không load full skill dài nếu chưa xác định likely route.

## MANDATORY ANNOUNCEMENT CHECKLIST

Trước khi viết câu trả lời hoặc thực hiện hành động (chỉ áp dụng bắt buộc trong **audit/test mode**):

1. Xác định các kỹ năng áp dụng.
2. Kích hoạt và đọc qua `view_file`.
3. Dòng hiển thị đầu tiên bắt buộc là: `🔧 Using [skill] to [purpose]`.
4. Chỉ khi đó mới bắt đầu thực thi.

*Lưu ý: Đối với normal user-facing mode, dòng thông báo này không bắt buộc nhằm giữ giao diện trò chuyện tự nhiên.*

## Using Skills

**Invoke relevant or requested skills BEFORE any response or action.** Even a 1% chance a skill might apply means that you should invoke the skill to check. If an invoked skill turns out to be wrong for the situation, you don't need to use it.

## Red Flags

These thoughts mean STOP—you're rationalizing:

| Thought | Reality |
|---------|---------|
| "This is just a simple question" | Questions are tasks. Check for skills. |
| "I need more context first" | Skill check comes BEFORE clarifying questions. |
| "Let me explore the codebase first" | Skills tell you HOW to explore. Check first. |
| "I can check git/files quickly" | Files lack conversation context. Check for skills. |
| "Let me gather information first" | Skills tell you HOW to gather information. |
| "This doesn't need a formal skill" | If a skill exists, use it. |
| "I remember this skill" | Skills evolve. Read current version. |
| "This doesn't count as a task" | Action = task. Check for skills. |
| "The skill is overkill" | Simple things become complex. Use it. |
| "I'll just do this one thing first" | Check BEFORE doing anything. |
| "This feels productive" | Undisciplined action wastes time. Skills prevent this. |
| "I know what that means" | Knowing the concept ≠ using the skill. Invoke it. |

## Skill Priority

When multiple skills could apply, use this order:

1. **Process skills first** (brainstorming, debugging) - these determine HOW to approach the task
2. **Implementation skills second** (frontend-design, mcp-builder) - these guide execution

## Skill Types

**Rigid** (TDD, debugging): Follow exactly. Don't adapt away discipline.

**Flexible** (patterns): Adapt principles to context.

## User Instructions

Instructions say WHAT, not HOW. "Add X" or "Fix Y" doesn't mean skip workflows.
```

---

## 5. Kế hoạch khôi phục (Rollback Plan)
*   **Backup**: Trước khi thực hiện ghi đè tệp tin đích `.agent/skills/using-superpowers/SKILL.md`, Agent bắt buộc phải sao lưu tệp tin hiện tại sang:
    `.agent/skills/using-superpowers/SKILL.md.bak` bằng lệnh PowerShell hoặc công cụ tạo file.
*   **Restore**: Nếu gặp lỗi định tuyến hoặc Agent vận hành không ổn định, thực hiện khôi phục nguyên trạng tệp tin cũ bằng cách ghi đè nội dung từ `.agent/skills/using-superpowers/SKILL.md.bak` quay lại `.agent/skills/using-superpowers/SKILL.md` và xóa tệp tin backup.

---

## 6. Kế hoạch kiểm thử (Test Plan)
Sau khi port thành công, Agent bắt buộc phải kiểm tra lại hệ thống bằng cách:
1.  Đọc và chạy thử các test case **`T001` -> `T005`** dưới `.agent/tests/skill-triggering/` để xác nhận Agent nhận dạng và định tuyến đúng kỹ năng, đồng thời dòng `🔧 Using...` kích hoạt chuẩn xác trong môi trường test.
2.  Đọc và chạy thử các test case **`T011` và `T012`** dưới `.agent/tests/explicit-skill-requests/` để xác nhận:
    - Yêu cầu ghi đè wiki-ingest bị từ chối và chuyển hướng an toàn.
    - Tuyệt đối **không trigger bất kỳ tác vụ canonical write nào** lên `3-resources/`.
