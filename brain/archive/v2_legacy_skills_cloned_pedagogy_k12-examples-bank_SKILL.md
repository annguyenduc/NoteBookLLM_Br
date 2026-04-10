---

name: k12-examples-bank
description: "K-12 — Thư viện examples chuẩn cho STEAM ID (Layer 4 - Blueprints)."
version: 2.0.0
---

# k12-examples-bank — STEAM Examples & Blueprints Bank (PRO)

> **Goal:** Provide high-quality few-shot samples and blueprints for AI. Examples are extracted from "Gold Standard" outputs to ensure the agent replicates deep pedagogical structures correctly.

## When to Activate

- The agent needs a concrete reference before generating a STEAM lesson
- Looking for a physical blueprint to model a ToT module structure
- Needing an analogy to explain a technical concept for K-12 audiences
- Running the Error Analysis Loop for a technical/AI module design

## Instructions

### Core Blueprints (Layer 4 Standards) — [ACTIVE]

These blueprints have been deployed and are ready for reference:

| Blueprint | File | Purpose |
|-----------|------|---------|
| **ToT Module Blueprint** | `examples/pattern-tot-module.md` | Lesson plan structure for teacher training (Bloom, Knowledge Map, Schedule). |
| **Assessment Blueprint** | `examples/pattern-assessment.md` | Assessment package structure (MCQ, Practice, Scenario). |
| **Analogy Logic** | `examples/pattern-analogy-logic.md` | How to explain technical terms in accessible K-12 language. |

### Invisible Standards in Action (Example)

| Old State | New State (PRO) |
|-----------|----------------|
| Label slide: "SAMR: Redefinition" | Design an activity that requires students to use computers to do something **previously impossible** (e.g., interviewing a remote expert via Zoom). The SAMR spirit lives in the **nature of the activity** — not the label. |

### Error Analysis Loop (For Technical/AI Modules)

When designing a technical or AI module, always apply this improvement loop:
1. **Test:** Run the code/model.
2. **Discover Error:** "Why isn't the result what we expected?"
3. **Improve:** Modify parameters/data.
4. **Compare:** Re-check accuracy against baseline.

## Quality Gate (Red Flags)

- ❌ Examples without annotation explaining "Why is this good?"
- ❌ Loose structure not following Bloom's Taxonomy progression.
- ❌ Missing pedagogical constraints (constraints that stimulate thinking).
- ⚠️ Always cross-reference with `k12-shared-references` for correct standard terminology.

## Example Triggers

- "Give me a 5E lesson plan example for physics."
- "Sample rubric for a race car design project."
- "Apply the ToT module structure to a Thunkable lesson."
- "Explain the concept of API using an analogy for Grade 8 students."
