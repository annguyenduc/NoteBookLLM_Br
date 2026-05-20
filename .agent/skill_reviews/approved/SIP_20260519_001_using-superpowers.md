# SKILL_IMPROVEMENT_PROPOSAL

```yaml
proposal_id: SIP_20260519_001
skill_id: using-superpowers
current_version: [READ_FROM_SKILL_MD — không có version field trong frontmatter]
proposed_version: minor bump
source_run_id: conversation/01d1150c-bb7b-4ef8-90b0-ae8edbb39fb0
trigger: repeated_failure
severity: medium
approval_required: true
```

## Evidence

Phiên 2026-05-19 (conversation 01d1150c):
- Turn 1: Agent đọc `mcp-builder` SKILL.md nhưng **không announce** "Using mcp-builder to..."
- Turn 2: Agent sửa `SKILLS_INDEX.md` nhưng **không announce** skill nào được dùng
- User phải hỏi trực tiếp: *"bạn đang dùng các skill nào? vì sao không báo cáo cho tôi như đã đề cập"*
- Agent thừa nhận lỗi tại chỗ — xác nhận đây là pattern lặp lại, không phải lỗi cá biệt.

## Problem

`using-superpowers` SKILL.md yêu cầu rõ tại dòng 59:
```
"Announce: 'Using [skill] to [purpose]'"
```

Và tại dòng 13:
```
IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.
```

Gap hiện tại: Skill không có cơ chế **enforce announcement** đủ mạnh ở đầu response. Agent đọc skill, áp dụng logic bên trong, nhưng bỏ qua bước announce vì bước này không có **explicit checkpoint** bắt trước khi write bất kỳ output nào.

## Proposed Change (Approved Version)

Đề xuất thêm một section **"MANDATORY ANNOUNCEMENT CHECKLIST"** ngay sau phần "The Rule" (dòng 47), biến hướng dẫn mềm thành checkpoint cứng:

```markdown
## MANDATORY ANNOUNCEMENT CHECKLIST

Before writing any user-facing output or taking any action:

1. Identify all skills that may apply to the task.
2. Invoke/read each applicable skill before acting.
3. Make the first visible line:
   `🔧 Using [skill] to [purpose]`
4. If multiple skills apply, announce all of them in the same first line or consecutive first lines.
5. Only then proceed with the task.

Hard rule: if an applicable skill was used but not announced before the task response/action, the response is invalid and must be restarted.
```

## Regression Case

### Regression Case 1:
- Input: User nói "cập nhật file X cho đúng với hiện tại"
- Expected: Agent response bắt đầu bằng `🔧 Using cm-core-edit-pro to...` trước khi làm bất cứ điều gì
- Current (broken): Agent đọc file và sửa ngay, announce thiếu hoặc không có.

### Regression Case 2:
- Input: "Sửa file X theo diff này"
- Expected first line: "🔧 Using cm-core-edit-pro to apply a surgical file edit"
- Then: read/patch/validate.
- Broken behavior: patch first, announce later, or no announce.

## Risk

**medium** — Thay đổi bổ sung checklist rõ ràng, không làm thay đổi các quy tắc lõi khác. Rủi ro quá tải token đã được AN loại bỏ khi lược bớt điều kiện "1% chance".

## AN Decision

```yaml
AN Decision:
  status: "Approve with modification"
  proposal_id: "SIP_20260519_001"
  apply_mode: "surgical diff"
  target_skill: "using-superpowers/SKILL.md"
  version_bump: "minor"
  risk: "medium"
  approved_at: "2026-05-19T09:24:17+07:00"
```
