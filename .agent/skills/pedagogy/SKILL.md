---
name: pedagogy
description: "Use when designing lesson plans or learning sequences from Wiki Atoms, converting comparison content to PPTX slides, or packaging content for LMS/H5P export. Requires a Trainer Profile before starting. Do NOT use for raw data ingest or routine Wiki maintenance."
---

# Pedagogy

## Overview
Use this skill for instructional-design outputs, not for routine wiki maintenance. The folder contains export and conversion utilities for slides and LMS packaging, plus a process template for structured intermediate work.

## Guardrails
- Start only when the required `Trainer_Profile_[id].md` exists.
- Respect the pipeline: trainer profile first, learning design second, content production third.
- Use `.agent/skills/pedagogy/resources/PROCESS_TEMPLATE.md` for substantial intermediate files.
- Several scripts in this folder still assume legacy `d:/NoteBookLLM_Br/brain/...` paths. Inspect the target script before running it in the current vault layout.

## Workflow
1. Confirm the pedagogical prerequisites exist.
2. Create or update the working draft using the process template.
3. Choose the export path that matches the task:
   comparison to PPTX, HTML-to-slide generation, LMS conversion, or H5P relabeling.
4. Run the relevant script and verify the produced artifact before publishing it onward.

## Quick Reference
- Comparison to PPTX:
  `python .agent/skills/pedagogy/scripts/export_comparison_to_pptx.py --input <draft.md> --output <deck.pptx>`
- Standard slide generation:
  `python .agent/skills/pedagogy/scripts/generate_standard_slides_k10.py`
- H5P relabeling:
  `python .agent/skills/pedagogy/scripts/convert_h5p.py`
- LMS conversion utilities:
  `final_lms_conversion.py`, `convert_all_iot.py`, `convert_all_khmt.py`

## Common Mistakes
- Running a legacy script without checking its hard-coded paths.
- Starting design work before the trainer profile exists.
- Treating export scripts as if they also validate pedagogy quality.
