---
name: wiki-breakdown
description: "Use when knowledge gaps need to be identified in the Wiki — specifically when terms are referenced in Atoms but have no corresponding page in concepts/ or entities/. Triggers on /breakdown command."
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
