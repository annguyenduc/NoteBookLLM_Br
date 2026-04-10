---


name: cm-jtbd
description: "CORE — Áp dụng lý thuyết Jobs-To-Be-Done để hiểu học sinh/giáo viên thực sự 'thuê' chương trình này để làm gì."
version: 2.0.0
---

# cm-jtbd — Jobs-To-Be-Done Analysis (LITE)

> **Goal:** Understand the "Job" that customers "hire" a product/service to do. Shift the focus from product features to human motivations and outcomes.

## When to Activate

- Defining who the target audience is and what they actually need
- Evaluating a product decision or curriculum design from the user's perspective
- Identifying why users might drop an existing solution for a new one
- Prioritizing features or content by opportunity score

## Instructions

### Job Statement Formula

```
When [SITUATION], I want to [MOTIVATION], so I can [EXPECTED OUTCOME].
```

**Example (STEAM context):**
> "When *I have to assess 30 students in one week*, I want to *generate a rubric automatically*, so I can *spend that time giving individual feedback instead*."

### The 4 Forces of Progress

| Force | Type | Definition |
|-------|------|------------|
| **Push (+)** | Trigger | Current pains driving them away from the old solution. |
| **Pull (+)** | Attraction | Benefits/promises of the new solution. |
| **Anxiety (-)** | Resistance | Fear/doubt that the new solution won't work. |
| **Habit (-)** | Inertia | Attachment to the old workflow; reluctance to change. |

### 3 Job Dimensions

- **Functional:** The practical task that needs to get done (e.g., "Finish a lesson plan in 15 min").
- **Social:** How they want to be seen by others (e.g., "Be recognized as an AI-forward educator").
- **Emotional:** How they want to feel (e.g., "Feel confident standing in front of a STEAM class").

### Opportunity Scoring

```
Opportunity Score = Importance (1-10) + max(Importance − Satisfaction, 0)
```

| Score | Interpretation | Priority |
|-------|---------------|----------|
| ≥ 15 | Market is underserved. | Highest — prioritize immediately. |
| 10-14 | Moderate opportunity. | Medium — monitor and plan. |
| < 10 | Market is saturated or over-served. | Low — deprioritize or differentiate. |

## Quality Gate (Red Flags)

- ❌ Using product features as the Job (e.g., "I want to use the app" instead of "I want to manage time").
- ❌ Missing any of the 3 dimensions (Social/Emotional) — leads to shallow analysis.
- ❌ Not calculating opportunity scores before committing to a new feature.
- ❌ Forgetting to save results to `docs/jtbd/` for Marketing reference.

## Example Triggers

- "Run a JTBD analysis for pre-school teachers as the target audience."
- "Why are customers leaving our old solution to choose us?"
- "Write a Job Statement for the Grade 5 Robotics course."
- "Identify the underserved opportunities in this teacher training program."
