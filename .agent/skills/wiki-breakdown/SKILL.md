---
name: wiki-breakdown
description: "Use when knowledge gaps need to be identified in the Wiki — specifically when terms are referenced in Atoms but have no corresponding page in concepts/ or entities/. Triggers on /breakdown command."
---

Detect knowledge gaps in the Wiki by extracting undefined terms and creating initial stubs.

## Context
During ingestion, many concepts are mentioned but don't yet have dedicated Atom pages. `wiki-breakdown` automates the discovery of these gaps to prioritize future research.

## Workflow

### Step 1: Noun Mining
Scan the entire Wiki for capitalized keywords or terms wrapped in `[[ ]]` that lack a corresponding file in `concepts/` or `entities/`.
```bash
python .agent/skills/wiki-breakdown/scripts/noun_miner.py
```

### Step 2: Gap Analysis
Classify discovered gaps based on frequency:
- **Critical Gap**: Mentioned > 5 times.
- **Secondary Gap**: Mentioned 1-2 times.

### Step 3: Stub Creation
Generate temporary Atom files (Stubs) with basic metadata to mark the existence of the concept.

## Constraints
- Do not create atoms without a clear source reference.
- All discovered gaps must be saved to the `review_queue` for User approval.
description: Use when wiki pages contain repeated broken wikilinks or undefined concepts and you need a gap report, frequency signal, or optional placeholder stubs for follow-up work.
---

# Wiki Breakdown

## Overview
Mine the wiki for missing concepts by scanning broken wikilinks in current markdown files. Use this to decide what the vault should explain next.

## Guardrails
- Start in report mode.
- Only use stub creation when placeholder pages are explicitly wanted.
- The current script writes `STUB` pages and DB rows; treat that as temporary technical debt, not verified knowledge.
- Do not invent definitions or sources while creating placeholders.

## Workflow
1. Run a scan first:
   `python .agent/skills/wiki-breakdown/scripts/noun_miner.py --source broken-links`
2. Review the frequency-ranked gaps.
3. If placeholders are needed, run:
   `python .agent/skills/wiki-breakdown/scripts/noun_miner.py --create-stubs --min-occurrence 2`
4. After stub creation, review the generated files in `3-resources/wiki/concepts/` and decide what should become real sourced atoms.

## Quick Reference
- Report only:
  `python .agent/skills/wiki-breakdown/scripts/noun_miner.py`
- Raise the threshold:
  `python .agent/skills/wiki-breakdown/scripts/noun_miner.py --min-occurrence 5`
- Create placeholders:
  `python .agent/skills/wiki-breakdown/scripts/noun_miner.py --create-stubs`

## Common Mistakes
- Using stub creation as a substitute for real ingest and sourcing.
- Forgetting that the script writes files and DB entries.
- Treating every broken link as equally important instead of ranking by recurrence.
