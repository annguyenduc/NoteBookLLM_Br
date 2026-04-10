---

name: k12-output-contract
description: "K-12 — Output Contract + Self-Check định lượng chuẩn Master AI."
version: 2.0.0
---

# k12-output-contract — STEAM K-12 Quality Auditor (PRO v1.10)

> **Goal:** Apply strict quantitative criteria to self-audit the quality of lessons, units, and rubrics. Ensure all output meets the "System Design for AI" and "Invisible Excellence" standards.

## When to Activate

- After completing a lesson plan, unit, or assessment
- When any other skill outputs a `⚠️ Post-check: Always run /k12-output-contract` note
- Before publishing or submitting any STEAM educational material
- When doing a quality audit pass on a batch of lesson plans

## Instructions

### Quality Scoring Rubric (Thresholds)

> All products must score ≥ 80% total to be approved for publishing.

| Criterion | Weight | Pass Threshold | How to Measure |
|-----------|--------|---------------|----------------|
| **Bloom Level** | 20% | ≥ Level 3 (Apply) | At least 2 leading verbs at Apply level or above. |
| **Active Learning** | 30% | **37/63 Rule** | Trainer speaks ≤ 37%. Student activity ≥ 63%. |
| **EDP/5E Flow** | 20% | 100% logical | Steps must connect (e.g., Explain must resolve what was observed in Explore). |
| **UNESCO / ISTE** | 20% | Level 2 (Deepen) | Must integrate UNESCO AI Competency Framework or ISTE standards. |
| **Invisible Standards** | 10% | Absolute | NO pedagogical terminology in student-facing content. |

### Detailed Audit Checklist

#### For Lesson Plans
- [ ] **ABCD Objectives:** Does it include Audience, Behaviour, Condition, Degree?
- [ ] **5E Ratio:** Does the **Explore** phase occupy ≥ 40% of lesson time?
- [ ] **Analogy:** At least 1 analogy for each difficult technical concept? (Ref: `k12-examples-bank`).

#### For Assessment Systems
- [ ] **MCQ:** At least 1 distractor option based on a real student misconception?
- [ ] **Rubric:** Criteria are quantitative (counts, time, evidence) — not subjective adjectives?
- [ ] **Error Analysis:** Does it ask students to explain "Why did the error happen?" not just "Fix the error?"

#### For ToT Content (UNESCO & Teacher Competency)
- [ ] **Human-centric:** Does the module include a discussion about human responsibility when using AI?
- [ ] **Ready to Teach:** Do teachers practice handling at least 2 real pedagogical scenarios?
- [ ] **Assessment:** Does the competency test include all 3 parts: Knowledge, Pipeline Skills, and Pedagogy?

## Quality Gate (Red Flags)

- ❌ **Qualitative words:** Using "good", "nice", "beautiful" in rubrics without measurable boundaries.
- ❌ **Jargon Leak:** Exposing "Bloom", "SAMR" labels in student-facing slides.
- ❌ **Passive Learning:** Lecture slides occupy > 40% of module time.

## Example Triggers

- "Audit this chatbot lesson plan product."
- "Check the quality of this robot project rubric."
- "Evaluate this ToT module against UNESCO standards."
- "Self-check implicit standards for this AI lesson."
