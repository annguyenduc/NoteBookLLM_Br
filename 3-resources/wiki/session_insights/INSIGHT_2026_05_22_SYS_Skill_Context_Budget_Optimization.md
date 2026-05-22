---
file_id: "INSIGHT_SYS_Skill_Context_Budget_Optimization"
title: "Session Insight: Skill Context Budget Optimization (Phase 3A + 3B)"
type: "insight"
tags:
  - "Session_Log"
  - "System_Optimization"
  - "Skill_Management"
  - "Git_Workflow"
status: "DRAFT"
source_file: ""
source_ref: ""
created: "2026-05-22"
last_updated: "2026-05-22"
---

## For future Claude (AI Preamble)
> Phiên làm việc tập trung vào tối ưu hóa token budget của lớp Skill (21 tệp SKILL.md) theo 2 pha: Phase 3A rút gọn YAML frontmatter description xuống ≤ 30 từ bằng surgical regex, Phase 3B tách `obsidian-bases/SKILL.md` (498 dòng) thành SKILL.md (164 dòng) + BASES_REFERENCE.md. Kết quả: `overall_policy_result` chuyển từ FAIL → PASS_WITH_WARNING. Phát hiện và xử lý 2 lỗi kỹ thuật nhỏ nhưng có rủi ro cao: regex `\s*` nuốt blank line, và file mới tạo bị untracked trong nested repo.

# Nhật ký & Bài học hệ thống (Session Insight)

## 1. Mục tiêu phiên làm việc (Session Objectives)
- Giảm token overhead của skill layer trong runtime context mà không thay đổi hành vi vault.
- Phase 3A: Rút gọn `description` frontmatter của 21 tệp SKILL.md về ≤ 30 từ.
- Phase 3B: Tái cấu trúc `obsidian-bases/SKILL.md` (> 400 dòng) bằng cách tách phần reference chi tiết ra file riêng `BASES_REFERENCE.md`.

## 2. Kết quả đạt được (Outcomes)
- Phase 3A: 21/21 tệp SKILL.md description ≤ 30 từ, YAML validate PASS.
- Phase 3B: `obsidian-bases/SKILL.md` giảm từ 498 → 164 dòng. `BASES_REFERENCE.md` (mới) lưu toàn bộ nội dung reference.
- Token budget: `static_repository_budget` giảm ~1,069 tokens (62,058 → 60,989).
- `overall_policy_result`: **FAIL → PASS_WITH_WARNING** (xóa được 1 issue HIGH).
- Merge thành công `agent/20260522-skill-context-budget` vào `main` (commit `4f1dfa4`).
- Nested repo `obsidian-skills` commit `7be41ab` được đồng bộ đúng cách về vault root.

## 3. Vấn đề phát sinh & Khắc phục (Issues & Resolutions)

- **Vấn đề 1 — Regex `\s*` nuốt blank line sau frontmatter**
  - **Biểu hiện:** `git diff --stat` mỗi file hiện `3 +--` thay vì `2 +-` (có 1 dòng xóa thừa là blank line sau `---`).
  - **Root cause:** Pattern `r'^---\s*\n(.*?)\n---\s*\n'` — `\s*` khớp cả `\n`, nên nó nuốt blank line giữa `---` đóng và heading `# ...`. Khi file được reconstruct, blank line mất đi.
  - **Fix:** Đổi `\s*` thành `[ \t]*` (chỉ khớp space/tab trên cùng dòng). Sau fix mỗi file đúng `2 +-` — đúng 1 dòng description thay đổi.
  - **AN phát hiện:** Sau khi review diff 4 file mẫu, thấy pattern `-\n # Heading` không lẽ ra có; yêu cầu restore + chạy lại trước khi duyệt Phase 3A.

- **Vấn đề 2 — `BASES_REFERENCE.md` untracked trong nested repo**
  - **Biểu hiện:** `git diff --stat` của nested repo chỉ hiện `SKILL.md | 347 +---` (347 dòng xóa) nhưng KHÔNG hiện file mới `BASES_REFERENCE.md`.
  - **Root cause:** `git diff` chỉ hiển thị tracked files. File mới tạo chưa được `git add` nên ở trạng thái `??` (untracked). Nếu commit ngay lúc đó thì toàn bộ nội dung reference bị mất silently.
  - **Fix:** `git -C <nested-repo> add skills/obsidian-bases/SKILL.md skills/obsidian-bases/references/BASES_REFERENCE.md`. Status đổi từ `??` → `A` (staged new file).
  - **AN phát hiện:** Nhận thấy `git diff --stat` không hiện file mới; yêu cầu chạy `git status --short` trước khi duyệt commit.

- **Vấn đề 3 — Nested repo pointer chưa đồng bộ về vault root sau merge**
  - **Biểu hiện:** Sau merge vào `main`, `git status` tại vault root vẫn hiện `modified: .agent/skills/references/obsidian-skills (new commits)`.
  - **Root cause:** Commit `7be41ab` của nested repo chỉ tồn tại trong worktree's copy của nested repo, chưa được fast-forward về nested repo tại vault root.
  - **Kết quả thực tế:** Server restart đã vô tình dọn worktree; Git object sharing khiến nested repo tại vault root cũng có `7be41ab` sẵn. Sau server restart, `git status` sạch, `ls-tree` và `rev-parse HEAD` của nested repo khớp nhau.
  - **Lesson:** Không nên dựa vào Git object sharing ngầm. Cần fetch/fast-forward tường minh TRƯỚC khi xóa worktree.

## 4. Bài học hệ thống (System Learnings / Instincts)

- **Instinct #1 — Regex frontmatter:** Dùng `[ \t]*` thay `\s*` sau `---` delimiter khi parse YAML frontmatter bằng regex. `\s*` nuốt newline, vi phạm surgical change rule.
- **Instinct #2 — New file trong nested repo:** Sau khi tạo file mới trong nested Git repo, BẮT BUỘC chạy `git status --short`. `git diff --stat` không hiển thị untracked files — đây là blind spot nghiêm trọng.
- **Instinct #3 — Nested repo sync trước cleanup:** Trước khi xóa worktree chứa nested repo, phải xác nhận commit mới đã có tại nested repo gốc (vault root). Check: `git ls-tree HEAD <path>` phải match `git -C <nested-repo-root> rev-parse HEAD`.
- **Instinct #4 — Skill split pattern:** Khi SKILL.md > 400 dòng, tách thành SKILL.md (workflow + guardrails + 1 quick example ≤ 300 dòng) + `references/<NAME>_REFERENCE.md` (bảng đầy đủ, ví dụ chi tiết — không auto-load).

## 5. Đề xuất cho phiên sau (Next Steps)
- [ ] Xem xét xử lý 2 issue MEDIUM còn lại: `worktree-agent.md` (238 dòng > 200) và `mcp-builder/SKILL.md` (description 39 từ > 30) — nếu muốn đạt `overall_policy_result: PASS` hoàn toàn.
- [ ] Xem xét push nested repo `obsidian-skills` lên remote nếu cần portability sang máy khác.
- [ ] Xem xét xử lý `.gitignore` và `CONTINUITY.md` runtime state đang modified.
