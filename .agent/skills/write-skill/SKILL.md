---
name: write-skill
description: Use when creating a new SKILL.md, editing, rewriting, or updating existing skills (sửa lại, viết lại, viết mới, nâng cấp skill). Do NOT use for general wiki maintenance or ingest tasks.
---

# Write Skill Protocol (NoteBookLLM_Br)

Local adaptation of `obra/superpowers` writing-skills pattern.

## Required Reading (load before writing any skill)
- **Full methodology** → read `.agent/skills/references/superpowers-writing-skills.md`
- **Anthropic official guide** → read `.agent/skills/references/anthropic-best-practices.md`
- **Testing with subagents** → read `.agent/skills/references/testing-skills-subagents.md`

> These files are in `references/` intentionally — they are NOT loaded automatically.
> You MUST read them manually before writing or editing any SKILL.md.

## Core Principle
**Writing skills IS TDD applied to process documentation.**
RED (baseline fail) → GREEN (write skill) → REFACTOR (close loopholes).

Full RED-GREEN-REFACTOR cycle explained in `references/superpowers-writing-skills.md §TDD Mapping`.

## SKILL.md Checklist (run for every new/edited skill)

**BEFORE writing:**
- [ ] Read the 3 reference files above (mandatory, not optional)
- [ ] Run a baseline pressure scenario WITHOUT the skill → document failures verbatim

**Frontmatter rules:**
- [ ] `name`: hyphens only, no special chars, no parentheses
- [ ] `description`: starts with `"Use when..."`, third-person, **NO workflow summary**
- [ ] Description ≤ 500 chars, frontmatter total ≤ 1024 chars

> Full description anti-pattern examples → see `references/superpowers-writing-skills.md §CSO`

**Body rules:**
- [ ] Structure: Overview → When to Use → Core Pattern → Quick Reference → Common Mistakes
- [ ] Body < 500 lines (split to separate `.md` files if larger, link 1 level deep from SKILL.md)
- [ ] Scripts only in `scripts/` — no side-effect logic inside SKILL.md body
- [ ] Heavy reference (>100 lines) → separate file, linked from SKILL.md directly
- [ ] One excellent example, not multi-language

> Progressive disclosure patterns → see `references/anthropic-best-practices.md §Patterns`

**After writing:**
- [ ] Run pressure scenario WITH skill → verify agent complies
- [ ] If agent fails → REFACTOR (see `references/testing-skills-subagents.md §REFACTOR`)
- [ ] Log write to `3-resources/wiki/log.md` (R4 compliance)

## Description Anti-Patterns (CSO Rule — Critical)

```yaml
# ❌ BAD — tóm tắt workflow, agent sẽ shortcut đọc description thay vì đọc skill body
description: "TRIGGER: absorb, merge knowledge... Hợp nhất Atoms vào Synthesis. Dùng sau khi wiki-ingest."

# ✅ GOOD — chỉ nêu triggering conditions, không mô tả quy trình
description: "Use when new Wiki Atoms need merging into Synthesis pages, or when knowledge contradictions are detected."
```

Tại sao quan trọng: agent đọc description trước, nếu description tóm tắt workflow thì agent shortcut — bỏ qua nội dung body. Lỗi này tồn tại trong tất cả 7 wiki skills hiện tại.

## Degrees of Freedom

| Task type | Freedom | Cách viết |
|---|---|---|
| Nhiều cách đều đúng | **High** | Text instructions, trust judgment |
| Có pattern ưu tiên | **Medium** | Steps rõ ràng + flexibility cho edge cases |
| Fragile, phải tuần tự | **Low** | Exact commands, `Do not modify` |

Wiki skills: `wiki-rebuild` = Low | `wiki-absorb` = Low | `wiki-query` = High | `wiki-ingest` = Medium

> Full guidance → `references/anthropic-best-practices.md §Degrees of Freedom`

## Common Mistakes (NoteBookLLM_Br specific)

| Lỗi | Fix |
|---|---|
| Description tóm tắt workflow | Chỉ để triggering conditions ("Use when...") |
| Script logic trong SKILL.md | Move vào `scripts/`, giữ chỉ command trong SKILL.md |
| `@file` links trong SKILL.md | Dùng plain path text (tránh force-load context) |
| Nested references (A→B→C) | Chỉ 1 cấp sâu từ SKILL.md |
| Ghi file mà không log | Luôn append `3-resources/wiki/log.md` (R4) |
| Viết skill trước khi test | Xóa đi, làm lại từ baseline |

## Iron Law
```
NO SKILL WITHOUT A FAILING TEST FIRST
```
Write skill trước khi test? Xóa đi. Làm lại.
Edit skill mà không test? Cùng vi phạm.

Full rationalization table → `references/superpowers-writing-skills.md §Common Rationalizations`
