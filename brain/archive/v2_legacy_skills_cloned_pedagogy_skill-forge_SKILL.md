---

name: skill-forge
description: "ToT — Agent tự cải tiến và nâng cấp bộ STEAM K-12 Skills Pack."
version: 2.0.0
---

# skill-forge — Skill Evolution Engine (LITE)

> **Goal:** Maintain system evolution by detecting knowledge gaps (skill gaps) and automating the process of creating and upgrading skills via Skill-Driven Development (SDD).

## When to Activate

- `skill-gaps.md` has 2 or more entries requiring new skills
- User feedback or corrections indicate a skill needs upgrading
- Periodic audit of the full skill set (every 20 sessions or manually triggered)
- After a major refactor — verificy no skill overlaps or broken links remain

## Instructions

### 3 Operation Modes

| Mode | Trigger | Action |
|------|---------|--------|
| **CREATE** | `skill-gaps.md` ≥ 2 entries. | Research → Draft `SKILL.md` (Lite format) → Register in Index. |
| **UPGRADE** | User feedback / corrections. | Read `learnings.md` → Refactor template → Bump version number. |
| **AUDIT** | Every 20 sessions or manually. | Review all 66 skills → Check overlap & broken links. |

### New Skill Structure (Lite Standard)

1. **YAML Header:** Metadata (name, description in Vietnamese, version, tags).
2. **Goal Section:** Core purpose (1-2 sentences in English).
3. **Instruction Table:** Process or rules in table format.
4. **Quality Gate:** Red Flags & anti-patterns.
5. **Triggers:** Example Triggers in both English and Vietnamese.

### System Registration (Final Step — Always Required)

- Update `SKILLS_INDEX.md`.
- Register in `gemini-extension.json`.
- Record the change in `CONTINUITY.md`.

## Quality Gate (Red Flags)

- ❌ Creating a new skill with > 30% overlap with an existing skill.
- ❌ Missing foundational pedagogical framework (5E, PBL, Bloom).
- ❌ Output template too vague to produce consistent results.
- ❌ Forgetting to update the Index after creating or upgrading a skill.

## Example Triggers

- "Create a new skill specializing in Science Fair competitions for Grade 8."
- "Upgrade module-architect to add a section on disability inclusion."
- "Audit the entire current skill set."
- "Run UPGRADE mode on the assessment-forge skill."
