---
title: "STEM Exam Media Export"
lang: vi
---

> Status: `PREVIEW_ASSESSMENT`, `PREVIEW_ONLY`, `NON_CANONICAL`.

## Media Prompt

Replace this prompt with the assessment question stem.

![Replace with concise alt text](media_ohstem_qxx_001.svg)

## Pandoc Export

```powershell
pandoc exam_export.pandoc.md --resource-path=. --standalone -o exam_export.html
pandoc exam_export.pandoc.md --resource-path=. --standalone -o exam_export.docx
```

