# NAMING LOCK: ARCH_TIS

Source file: `3-resources/raw_sources/ARCH_Thinking_in_Systems.pdf`
Source ID: `ARCH_TIS`
Status: `DRAFT`

## Naming Rule

Use `ARCH_TIS` as the only identity anchor for all future ingest artifacts from *Thinking in Systems*.

Do not create new files for this source using:

- `SYS_ARCH_TIS`
- `SYS_Thinking_in_Systems`
- `ARCH_Thinking_in_Systems` as a source identity prefix

## Canonical Filenames

- Source map: `MAP_ARCH_TIS.md`
- Naming lock: `NAMING_LOCK_ARCH_TIS.md`
- Master strategy: `Analysis_ARCH_TIS_MASTER_STRATEGY.md`
- Chunk analysis pattern: `Analysis_ARCH_TIS_CHUNK_XX.md`
- Source node: `SOURCE_ARCH_TIS_Thinking_in_Systems.md`

## Concept Filename Pattern

Use:

`CONCEPT_ARCH_TIS_[TERM_SLUG].md`

Approved seed mappings:

- `Systems Lens` -> `CONCEPT_ARCH_TIS_Systems_Lens.md`
- `System Structure` -> `CONCEPT_ARCH_TIS_System_Structure.md`
- `System Boundaries` -> `CONCEPT_ARCH_TIS_System_Boundaries.md`
- `Stock Foundation` -> `CONCEPT_ARCH_TIS_Stock_Foundation.md`
- `Flow Foundation` -> `CONCEPT_ARCH_TIS_Flow_Foundation.md`
- `Nonlinear Relationships` -> `CONCEPT_ARCH_TIS_Nonlinear_Relationships.md`
- `Delays in Systems` -> `CONCEPT_ARCH_TIS_Delays_in_Systems.md`
- `Balancing Feedback` -> `CONCEPT_ARCH_TIS_Balancing_Feedback.md`
- `Reinforcing Feedback` -> `CONCEPT_ARCH_TIS_Reinforcing_Feedback.md`
- `System Dynamics` -> `CONCEPT_ARCH_TIS_System_Dynamics.md`
- `Oscillation Dynamics` -> `CONCEPT_ARCH_TIS_Oscillation_Dynamics.md`
- `Resilience` -> `CONCEPT_ARCH_TIS_Resilience.md`
- `Self-Organization` -> `CONCEPT_ARCH_TIS_Self_Organization.md`
- `System Integrity` -> `CONCEPT_ARCH_TIS_System_Integrity.md`
- `Suboptimization` -> `CONCEPT_ARCH_TIS_Suboptimization.md`
- `Bounded Rationality` -> `CONCEPT_ARCH_TIS_Bounded_Rationality.md`
- `Hierarchy` -> `CONCEPT_ARCH_TIS_Hierarchy.md`
- `Levels of Understanding` -> `CONCEPT_ARCH_TIS_Levels_of_Understanding.md`
- `Limiting Factors` -> `CONCEPT_ARCH_TIS_Limiting_Factors.md`
- `Mental Model Duality` -> `CONCEPT_ARCH_TIS_Mental_Model_Duality.md`
- `System Equilibrium` -> `CONCEPT_ARCH_TIS_System_Equilibrium.md`

## Entity Filename Pattern

Use:

`ENTITY_ARCH_TIS_[NAME_SLUG].md`

Approved seed mappings:

- `Donella Meadows` -> `ENTITY_ARCH_TIS_Donella_Meadows.md`
- `Sustainability Institute` -> `ENTITY_ARCH_TIS_Sustainability_Institute.md`
- `Jay Forrester` -> `ENTITY_ARCH_TIS_Jay_Forrester.md`
- `Ludwig von Bertalanffy` -> `ENTITY_ARCH_TIS_Ludwig_von_Bertalanffy.md`
- `Garrett Hardin` -> `ENTITY_ARCH_TIS_Garrett_Hardin.md`
- `Justus von Liebig` -> `ENTITY_ARCH_TIS_Justus_von_Liebig.md`

## Enforcement

- If a term/entity is not listed here, do not invent a new filename pattern.
- Update this naming lock first, then generate the new atom.
- Canonical filename is stable identity.
- Human-readable title may change without renaming the file.

## Drift Resolution Intent

Existing legacy aliases in the vault should eventually be reconciled toward this naming lock, not treated as equal canonical variants.

## References

- Map: `1-projects/MAP_ARCH_TIS.md`
- Workflow: `.agent/workflows/ingest-lifecycle.md`
- Spec: `.agent/docs/INGEST_MAP_NAMING_LOCK_SPEC.md`
