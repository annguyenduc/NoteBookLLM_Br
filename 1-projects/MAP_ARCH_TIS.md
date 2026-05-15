# MAP: ARCH_TIS

Source file: `00_Inbox/ARCH_Thinking_in_Systems.pdf`
Source ID: `ARCH_TIS`
Title slug: `Thinking_in_Systems`
Canonical source node: `SOURCE_ARCH_TIS_Thinking_in_Systems.md`
Status: `DRAFT`

## Purpose

Global map for the source *Thinking in Systems*.

This file exists to preserve whole-book context while chunking remains a technical extraction mechanism.

## Canonical Identity

- Source ID: `ARCH_TIS`
- Title display: `Thinking in Systems: A Primer`
- Title slug: `Thinking_in_Systems`
- Raw filename stem: `ARCH_Thinking_in_Systems`
- Canonical source node filename: `SOURCE_ARCH_TIS_Thinking_in_Systems.md`

## Known Drift Aliases To Eliminate

These names already appear in the vault and must not be reused as new canonical identities:

- `SOURCE_ARCH_Thinking_in_Systems`
- `SOURCE_SYS_ARCH_TIS`
- `SOURCE_SYS_Thinking_in_Systems`
- `CONCEPT_SYS_ARCH_TIS_*`
- `ENTITY_SYS_ARCH_TIS_*`

Rule:
- `ARCH_TIS` is the only valid source identity anchor for future ingest of this source.

## Structural Map

Current state:
- Full chapter/section structure has not yet been extracted into this file.
- Chunking should be driven by chapter and section boundaries once the first structural pass is completed.

Required additions in the next mapping pass:
- table of contents
- chapter boundaries
- section boundaries
- page ranges
- candidate canonical terms
- candidate canonical entities

## Initial Canonical Terms

Seed terms already evidenced by existing vault content:

- `Systems_Lens`
- `System_Structure`
- `System_Boundaries`
- `Stock_Foundation`
- `Flow_Foundation`
- `Nonlinear_Relationships`
- `Delays_in_Systems`
- `Balancing_Feedback`
- `Reinforcing_Feedback`
- `System_Dynamics`
- `Oscillation_Dynamics`
- `Resilience`
- `Self_Organization`
- `System_Integrity`
- `Suboptimization`
- `Bounded_Rationality`
- `Hierarchy`
- `Levels_of_Understanding`
- `Limiting_Factors`
- `Mental_Model_Duality`
- `System_Equilibrium`

## Initial Canonical Entities

Seed entities already evidenced by existing vault content:

- `Donella_Meadows`
- `Sustainability_Institute`
- `Jay_Forrester`
- `Ludwig_von_Bertalanffy`
- `Garrett_Hardin`
- `Justus_von_Liebig`

## Chunking Rule

For this source:

1. chunk by chapter boundary first
2. chunk by section boundary second
3. use page windows only when a section is still too large

Every chunk analysis file must declare:

- `source_id: ARCH_TIS`
- `chapter_id`
- `section_path`
- `page_range`
- `canonical_terms`

## References

- Workflow: `.agent/workflows/ingest.md`
- Spec: `.agent/docs/INGEST_MAP_NAMING_LOCK_SPEC.md`
