# FIGURES: ARCH_TIS

Source file: `00_Inbox/ARCH_Thinking_in_Systems.pdf`
Source ID: `ARCH_TIS`
Canonical source node: `SOURCE_ARCH_TIS_Thinking_in_Systems.md`
Status: `DRAFT`

## Purpose

This artifact tracks visual evidence for `ARCH_TIS`.

It exists because systems-thinking knowledge is often carried by diagrams, not just prose.

## Evidence Status

Current status:
- No direct figure extraction has been recorded into this file yet.
- Visual importance is already known from the domain and the existing concept set.

Rule:
- Do not assume text-only extraction is sufficient for this source.

## Visual Priority Areas

The following concept families are likely to require figure evidence:

### Priority A: Feedback Loop Diagrams

Related concepts:
- `Balancing_Feedback`
- `Reinforcing_Feedback`
- `Oscillation_Dynamics`

Why it matters:
- loop polarity and causal structure are usually clearer in diagrams than prose alone

### Priority B: Stock and Flow Diagrams

Related concepts:
- `Stock_Foundation`
- `Flow_Foundation`
- `System_Dynamics`

Why it matters:
- the relationship between accumulation, inflow, and outflow is often diagram-native

### Priority C: Boundary and Structure Diagrams

Related concepts:
- `System_Structure`
- `System_Boundaries`
- `Hierarchy`

Why it matters:
- system framing and boundary logic can be visually encoded

### Priority D: Delay and Stability Diagrams

Related concepts:
- `Delays_in_Systems`
- `System_Equilibrium`
- `Resilience`

Why it matters:
- delay behavior and equilibrium shifts are often represented through visual models

## Figure Mapping Template

Each confirmed visual item should be logged in this format:

- `figure_id`:
- `chapter_id`:
- `section_path`:
- `page`:
- `caption_or_label`:
- `asset_path`:
- `related_concepts`:
- `why_it_matters`:

## Extraction Rule

When figure extraction runs:
1. identify pages containing diagrams, tables, or charts
2. map each visual to `chapter -> section -> page`
3. save extracted assets with canonical `[ID]`-based naming
4. update this file before atom generation for concepts that depend on the figures

## Atom Rule

If a concept depends strongly on a diagram:
- the atom must reference the relevant figure entry from this file
- the atom should not be considered complete with text evidence alone

## Initial Action Queue

When the visual extraction pass is available, prioritize:
1. feedback loop visuals
2. stock/flow visuals
3. delay/equilibrium visuals
4. system boundary/structure visuals

## References

- `1-projects/STRUCTURE_ARCH_TIS.md`
- `1-projects/MAP_ARCH_TIS.md`
- `.agent/workflows/ingest.md`
- `.agent/docs/INGEST_MAP_NAMING_LOCK_SPEC.md`
