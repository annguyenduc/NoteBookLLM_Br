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
