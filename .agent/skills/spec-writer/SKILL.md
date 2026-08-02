---
name: spec-writer
description: Use when an EduResearch Hub task needs a spec-first design folder, a fresh SPEC.md, or a rewrite of spec artifacts for multi-step curriculum design, research tasks, or system changes. Do NOT use for simple read-only questions or tasks already covered by an existing canonical skill.
---

# Spec Writer (EduResearch Hub)

## Overview

Skill này tạo và duy trì các spec-first task artifacts cho `NoteBookLLM_Br` (EduResearch Hub).

Nguyên tắc cốt lõi: Quản trị bản địa trước $\rightarrow$ Viết Spec artifacts $\rightarrow$ Duyệt từ User/AN $\rightarrow$ Thực thi các bước tiếp theo.

## When to Use

Sử dụng skill này khi:
- Một nhiệm vụ sẽ thay đổi khung chương trình, bài giảng, quy trình nghiên cứu, workflows, skills, rules, hoặc cấu trúc workspace.
- Cần tạo một spec-first folder mới: `specs/YYYY-MM-DD_task-name/SPEC.md`
- Cần dọn dẹp hoặc viết lại spec artifacts trước khi thiết kế bài giảng hoặc phát triển.
- Chưa có skill chuyên biệt phù hợp dưới `.agent/skills/`.

## Anti-Triggers

- KHÔNG dùng cho câu trả lời một dòng, dịch thuật, hoặc định dạng đơn giản.
- KHÔNG dùng để bỏ qua các skill bản địa đã có (ví dụ: `edu-lesson-designer`, `course-writer`).
- KHÔNG dùng để tự ý thực thi code/bài viết trước khi `SPEC.md` được duyệt.

## Source Priority (Thứ Tự Ưu Tiên Nguồn Rule)

Tuân thủ đúng thứ tự:

1. `AGENTS.md`
2. `CONTINUITY.md`
3. `.agent/rules/`
4. Current task artifacts trong `specs/<spec-id>/`
5. Upstream references (Superpowers, PRISMA 2020 framework, Anthropic K-12 standards, Bloom's Taxonomy)

Nếu bất kỳ khung tham chiếu bên ngoài nào xung đột với quản trị bản địa, từ chối quy tắc bên ngoài và làm theo quy tắc bản địa.

## Workflow

### 1. Kiểm tra Quản trị Bản địa
Trước khi viết, đọc các file cần thiết:
- `AGENTS.md`
- `.agent/rules/`

### 2. Kiểm tra Skill Bản địa Hiện Có
Kiểm tra `.agent/skills/` xem đã có skill phù hợp chưa. Nếu có skill chuẩn (ví dụ `course-writer`), chuyển sang dùng skill đó trừ khi user yêu cầu quy trình spec-first.

### 3. Tạo Artifact Kiểm Soát Đầu Tiên
Artifact kiểm soát đầu tiên luôn là:
`specs/YYYY-MM-DD_task-name/SPEC.md`

Chưa tạo `CHECKLIST.md`, `PLAN.md`, hay `TASKS.md` trước khi `SPEC.md` được duyệt trừ khi có chỉ định.

### 4. Cấu Trúc File SPEC.md Standard
Mỗi `SPEC.md` cho Edu Research / Lesson Design cần định nghĩa:
- **Objective** (Mục tiêu bài giảng/nghiên cứu)
- **Target Audience & Standards** (Khung năng lực Toán/STEM, Bloom's level)
- **Evidence Base / References** (Cơ sở lý luận & bằng chứng)
- **Approval Gates** (Các cổng bàn giao & duyệt)
- **Forbidden Actions** (Các hành vi cấm)
- **Expected Deliverables** (Sản phẩm đầu ra dự kiến: giáo án 3 mức, đề thi, SLR review)

### 5. Yêu Cầu Duyệt Trước Khi Triển Khai
Không thực thi trước khi duyệt. Sau khi `SPEC.md` được duyệt, tạo các file tiếp theo theo thứ tự:
1. `CHECKLIST.md`
2. `PLAN.md`
3. `TASKS.md`
4. `REPORT.md` (khi hoàn thành)

## Quick Reference

- File đầu tiên: `specs/YYYY-MM-DD_task-name/SPEC.md`
- Gate đầu tiên: Kiểm tra quản trị bản địa & duyệt SPEC.md
- File sau khi duyệt: `CHECKLIST.md`, `PLAN.md`, `TASKS.md`
