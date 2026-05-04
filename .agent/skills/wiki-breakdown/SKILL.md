---
name: wiki-breakdown
description: "Phát hiện lỗ hổng tri thức (Knowledge Gaps) bằng cách trích xuất danh từ chưa được định nghĩa và tạo các Stubs."
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
