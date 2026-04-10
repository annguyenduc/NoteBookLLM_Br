---

name: output-contract
description: "ToT — Kiểm định nội dung đào tạo GV (Andragogy, TPACK, SAMR)."
version: 2.0.0
---

# output-contract — ToT Quality Auditor (PRO — Integrated Auditor)

> **Goal:** Establish an internal quality control system for teacher training materials. Ensure all content achieves **Invisible Excellence** — where pedagogical standards are embedded deeply and invisibly, not worn as decorations.

## When to Activate

- After completing a training module, slide deck, or trainer manual
- Called implicitly by `module-architect`, `rubric-builder`, `assessment-forge` as a post-check
- When a `⚠️ Post-check: Always run /output-contract` note appears in another skill's output
- Before submitting final training materials for review or publication

## Instructions

### Invisible Quality Metrics (Internal Check)

The agent checks these automatically — does NOT print these labels to the user:

| Criterion | Pass Threshold | Check Logic (Hidden) |
|-----------|---------------|---------------------|
| **Andragogy Ratio** | 30-60-10 | Practice/Discussion must occupy the majority of time (> 60%). |
| **Integrated TPACK** | ✅ Pass | T-P-C must be interwoven — no digital tool included "for its own sake." |
| **Implicit SAMR** | ≥ Modification | Activities must have a transformative nature — not just substitution. |
| **Pedagogical Depth** | ✅ Pass | Speaker Notes must contain facilitation scenarios, not just slide explanations. |

### Technical Audit Checklist

- [ ] **No Labeling Check:** Output does NOT contain labels like "SAMR Level", "Tier X", "Kirkpatrick Y."
- [ ] **Scenario Check:** At least one case study or Micro-teaching exercise is present.
- [ ] **Facilitation Check:** Slides contain open-ended facilitation questions for teacher self-reflection.
- [ ] **Authenticity Check:** The project solves a real educational challenge teachers actually face.

## Quality Gate (Red Flags)

- ❌ Writing theoretical standards directly into teaching slides (violates Invisible Excellence).
- ❌ More than 5 bullet points per slide (violates Multimedia Learning Principle).
- ❌ Missing a hands-on worksheet in the participant handout.
- ❌ Framework disconnected from the actual subject context (TPACK failure).

## Example Triggers

- "Check the teacher training module implicitly."
- "Audit the slide scenario against v4.2.0 standards."
- "Validate trainer manual (Integrated standards)."
- "Run the output contract before submitting this module."
