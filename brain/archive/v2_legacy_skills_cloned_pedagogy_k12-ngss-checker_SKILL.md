---

name: k12-ngss-checker
description: "K-12 — Kiểm tra và căn chỉnh bài dạy với chuẩn NGSS (Mỹ) và GDPT 2018 (Việt Nam)."
version: 2.0.0
---

# k12-ngss-checker — Dual-Standard Alignment Checker (PRO v1.1.0)

> **Goal:** Analyze how well a lesson's content aligns with international (NGSS) and national Vietnamese (GDPT 2018) competency frameworks. Ensure lessons are not just engaging but also pedagogically sound and standards-compliant.

## When to Activate

- Checking a STEAM lesson plan against NGSS and GDPT 2018 standards
- Identifying competency gaps in a unit plan
- Generating an alignment matrix for a training module or course
- Aligning a Python or CS lesson to Vietnam's Tin học 2018 framework

## Instructions

### Dual-Standard Alignment Protocol

Use data from `k12-shared-references (Sections 5 & 6)` for cross-referencing.

1. **Standards Mapping:** List the competency codes directly developed in the lesson (e.g., SEP 3, CCC 2, NLa, NLc).
2. **Gap Analysis:** Identify missing components (e.g., SEP 3 is present but CCC 4 Systems is missing).
3. **Actionable Suggestions:** Propose specific activities to fill gaps (e.g., "Add a block diagram to address CCC 4").

### Alignment Matrix Blueprint

Reporting structure for instructional designers:

| Activity | 🇺🇸 NGSS 3D | 🇻🇳 GDPT 2018 | Pedagogical Notes |
|---------|------------|-------------|-----------------|
| Lab: Experiment | SEP 3, CCC 2 | NLc (IT), KHTN 2 | Students design their own Guided Inquiry protocol. |
| Group Discussion | SEP 7, CCC 4 | NLe (Collaboration) | Reasoning based on data evidence. |
| Project Pitch | SEP 8 | NLd (Self-learning) | Communicating scientific information. |

### Gap Analysis Levels

| Level | Description | Goal |
|-------|-------------|------|
| **Level 1 (Low)** | Only surface contact (e.g., knows the name of a tool — NLa). | Baseline. |
| **Level 2 (Mid)** | Can operate the tool (NLa — operational). | Target minimum. |
| **Level 3 (High)** | Creates/solves problems (NLc — optimizing). | Target for at least 1 core competency. |

## Quality Gate (Red Flags)

- ❌ **Standard Washing:** Listing a standard code (e.g., SEP 1) without a corresponding activity in the lesson.
- ❌ **Pedagogical Jargon Leak:** Exposing standard codes in student-facing materials (standards must remain implicit).
- ❌ **Single-Standard:** Aligning only to NGSS without GDPT 2018 (or vice versa).
- ⚠️ Post-check: Ensure the lesson retains creativity and engagement after being "standardized."

## Example Triggers

- "Scan NGSS standards for this lesson."
- "Create a GDPT 2018 alignment matrix for this ToT module."
- "Find competency gaps (Gap Analysis) in this unit plan."
- "Align this Python lesson with the CS strand of Tin học 2018."
