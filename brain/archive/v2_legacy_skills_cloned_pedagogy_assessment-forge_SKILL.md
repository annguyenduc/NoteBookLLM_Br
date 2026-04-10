---

name: assessment-forge
description: "ToT — Đánh giá năng lực sư phạm giảng viên và mức độ vận dụng TPACK bằng tiêu chí có minh chứng."
version: 2.0.0
---

# assessment-forge — Trainer Competency Evaluator (PRO — Integrated)

> **Goal:** Design evidence-based teacher competency assessments. Standards are baked deeply into the quality of the pedagogical output — not surfaced as framework labels.

## When to Activate

- Designing a post-training competency evaluation for teachers
- Creating classroom observation tools for STEAM/Robotics projects
- Building self-reflection instruments for trainer self-assessment
- Auditing training outcomes against Guskey's 5-tier impact model

## Instructions

### Dual-Mode Logic (Mandatory)

> [!IMPORTANT]
> **Check Intent:** If the target is a **student quiz or student rubric**, the agent must STOP and ask: "I detect you may want to create an assessment for students. Do you want Student mode (Bloom taxonomy) or Trainer competency mode?"

### Integrated Evaluation Audit

- **Implicit Behavior (L3 Kirkpatrick):** Evaluate how teachers apply technology to solve specific pedagogical problems in actual classroom settings.
- **Evidence Collection:** Require concrete artifacts: lesson recording video, sample lesson plan, student robot product guided by the teacher.
- **Pedagogical Shift Measurement:** Measure the shift from "lecture delivery" to "guided inquiry facilitation."

### Comprehensive Evaluation Areas

| Area | What to Measure |
|------|----------------|
| **Technical Literacy** | Can apply tools to produce solutions — not just name them. |
| **Curriculum Redesign** | Can transform traditional content into integrated STEAM content. |
| **Student Impact** | Level of student agency and creative thinking under teacher guidance. |
| **Reflection Ability** | Teacher can self-identify competency gaps and build an improvement plan. |

### Global Standards Alignment

- **Guskey's Model:** Evaluate impact across 5 deep tiers (Participant Reactions → Learning → Organization Support → Use of New Knowledge → Student Learning Outcomes).
- **ISTE Compliance:** Evaluate teacher as Learner, Leader, Citizen, Collaborator, Designer, Facilitator, and Analyst.

## Quality Gate (Red Flags)

- ❌ Using multiple-choice tests to evaluate integrated pedagogical competency (P-C).
- ❌ Missing specific feedback guidance for teachers after the evaluation.
- ⚠️ Post-check: Always run `/output-contract` to audit for objectivity errors.

## Example Triggers

- "Design a teacher competency assessment after a CPD module series."
- "Create a classroom observation tool for a Robotics project."
- "Build a self-reflection checklist for STEAM master trainers."
