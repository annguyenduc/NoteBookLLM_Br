---

name: skills-validator
description: "ToT — Tự động kiểm tra cấu trúc và chất lượng các tệp SKILL.md (Script Python Layer 5)."
version: 2.0.0
---

# skills-validator — STEAM Skills Governance Validator (PRO Script)

> **Goal:** Automate governance and quality control (QC) for all 66+ skills in the Kit. Ensure every skill complies with the 9-Layer Skill Engineering structure.

## When to Activate

- After a major batch skill refactor or migration
- After installing new skills from an external source
- When periodic health checks are needed (every 20 sessions or manually)
- When a skill audit is triggered by `skill-forge`

## Instructions

### Audit Logic — 8 Core Criteria

The Python script checks:
1. **YAML Frontmatter:** Valid and includes all required fields (`name`, `description`, `version`).
2. **Metadata Standard:** Description must have a recognized domain prefix (`CORE —`, `K-12 —`, `ToT —`).
3. **Trigger Analysis:** Has an `Example Triggers` section for AI routing recognition.
4. **Quality Gate:** Has a `Quality Gate` section with quantitative or qualitative criteria.
5. **Token Optimization:** File length does not exceed the optimal context limit.
6. **Reference Links:** Cross-references to `k12-shared-references` exist where expected (string existence check only).
7. **Language Rule:** Body content is in English; only `description` frontmatter is in Vietnamese.
8. **Version Format:** Version follows semantic versioning (e.g., `2.0.0`).

### Execution

- **Environment:** Requires Python 3.x with `PyYAML` library.
- **Command:** `python .agent/skills/skills-validator/skill_validator.py`

## Quality Gate (Red Flags)

- ❌ **Structure mismatch:** Files without YAML frontmatter will fail the audit.
- ❌ **Token bloat:** Files > 3000 words will be flagged as FAIL (need to split into layers).
- ❌ **Missing triggers:** Lack of an "activation zone" reduces skill discoverability for the agent.
- ⚠️ Post-check: Always run this validator after every major upgrade or refactor cycle.

## Example Triggers

- "Check the structure of all skills."
- "Run the STEAM skill audit."
- "Validate SKILL.md structure."
- "Are there any skills in the system that don't meet standards?"
