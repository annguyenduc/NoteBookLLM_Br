# STRUCTURE: ARCH_TIS

Source file: `3-resources/raw_sources/ARCH_Thinking_in_Systems.pdf`
Source ID: `ARCH_TIS`
Canonical title: `Thinking in Systems: A Primer`
Canonical title slug: `Thinking_in_Systems`
Canonical source node: `SOURCE_ARCH_TIS_Thinking_in_Systems.md`
Status: `DRAFT`

## Scope

This artifact captures the whole-book structural view needed before chunk-level ingest.

It is the required structure-first control artifact for `ARCH_TIS`.

## Evidence Status

Current status:
- The source identity is confirmed.
- The source title is confirmed.
- Canonical term seeds are grounded by existing vault artifacts.
- Exact chapter/page boundaries are not yet extracted directly from the PDF in this artifact.

Rule:
- Do not treat inferred section groupings below as exact PDF chapter/page facts until a direct structural extraction pass confirms them.

## Canonical Identity

- Source ID: `ARCH_TIS`
- Display title: `Thinking in Systems: A Primer`
- Title slug: `Thinking_in_Systems`
- Raw filename stem: `ARCH_Thinking_in_Systems`
- Source node filename: `SOURCE_ARCH_TIS_Thinking_in_Systems.md`

## Structure-First Contract

Required hierarchy for this source:

`Part -> Chapter -> Section -> page_range`

Chunking priority:
1. chapter boundary first
2. section boundary second
3. page window only when a section remains too large

## Provisional Thematic Structure

The structure below is a working map inferred from existing concept coverage in the vault.

### Cluster A: Foundational Systems View

Canonical terms:
- `Systems_Lens`
- `System_Structure`
- `System_Boundaries`
- `Hierarchy`
- `Levels_of_Understanding`

Working interpretation:
- opening conceptual framing
- what a system is
- how structure drives behavior

### Cluster B: Stocks, Flows, and Dynamic Behavior

Canonical terms:
- `Stock_Foundation`
- `Flow_Foundation`
- `Nonlinear_Relationships`
- `Delays_in_Systems`
- `System_Dynamics`
- `Oscillation_Dynamics`
- `System_Equilibrium`

Working interpretation:
- dynamic mechanics of systems
- flow and accumulation logic
- delay-driven and oscillatory behavior

### Cluster C: Feedback Logic

Canonical terms:
- `Balancing_Feedback`
- `Reinforcing_Feedback`

Working interpretation:
- core feedback loop grammar
- balancing vs reinforcing behavior patterns

### Cluster D: System Qualities and Limits

Canonical terms:
- `Resilience`
- `Self_Organization`
- `System_Integrity`
- `Suboptimization`
- `Bounded_Rationality`
- `Limiting_Factors`
- `Mental_Model_Duality`

Working interpretation:
- limits of local optimization
- cognitive limits in system interaction
- robustness and adaptive capacity

## Initial Entity Set

Grounded by existing vault evidence:
- `Donella_Meadows`
- `Sustainability_Institute`
- `Jay_Forrester`
- `Ludwig_von_Bertalanffy`
- `Garrett_Hardin`
- `Justus_von_Liebig`

## Required Direct Extraction Pass

This structure file still needs a direct PDF structure pass to confirm:
- exact table of contents
- exact chapter list
- exact section list
- exact page ranges
- figure-bearing sections

When the direct structure pass runs, append:

### Confirmed Structure

For each confirmed chapter:
- `chapter_id`
- `chapter_title`
- `section_path`
- `page_range`
- `major_terms`

## Downstream Use

- `MAP_ARCH_TIS.md` should be updated from this file once direct structure extraction is complete.
- `NAMING_LOCK_ARCH_TIS.md` already locks canonical filenames and should remain stable.
- `Analysis_ARCH_TIS_CHUNK_XX.md` files must reference this structure artifact before any atom generation.

## References

- `1-projects/MAP_ARCH_TIS.md`
- `1-projects/NAMING_LOCK_ARCH_TIS.md`
- `.agent/workflows/ingest-lifecycle.md`
- `.agent/docs/INGEST_MAP_NAMING_LOCK_SPEC.md`
