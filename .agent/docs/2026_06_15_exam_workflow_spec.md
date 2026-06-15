# SPEC: Internal Exam Draft Workflow For STEM / AI / IoT Courses

## 1. Objective

Define a lightweight, reusable workflow for drafting end-of-course exams for STEM / AI / IoT courses before human publishing to Google Docs or LMS.

This workflow optimizes for:
- one internal draft source of truth
- clear media handling
- traceable code and demo assets
- low-friction handoff to human publishing

This workflow does **not** publish directly to LMS and does **not** create canonical vault artifacts.

## 2. Scope

This spec applies to exam drafting work based on course materials stored under:

```text
workspaces/learning/courses/
```

Primary drafting and preview artifacts live under:

```text
workspaces/source-lab/
```

Out of scope:
- direct writes to `3-resources/`
- canonical ingest
- automatic Google Docs generation
- automatic LMS publishing

## 3. Output Model

Each exam draft package uses exactly these primary artifacts:

### 3.1 Required

1. One internal exam draft markdown file.
2. One sibling media folder when the exam uses images, videos, gifs, code samples, or linked sample artifacts.

### 3.2 Optional

- Link references to external sample projects or design files.
- A final manifest section inside the markdown file when the exam contains many generated or traceable media assets.

## 4. Source Of Truth

The internal draft markdown file is the editing source of truth before human publishing.

Human operators may later:
- copy content into Google Docs
- remove internal-only fields such as answer keys
- publish the student-facing version to LMS

Agent output only needs to provide the structured exam content and asset references.

## 5. Draft File Contract

The draft exam markdown file must contain:

1. Exam title and course identity.
2. General exam information.
3. Materials / equipment table.
4. Exam blueprint / matrix.
5. Part I: 30 multiple-choice questions.
6. Part II: 3 practical exercises.
7. Delivery requirements.
8. Draft metadata / author-review history.

### 5.1 Multiple-Choice Question Contract

Every multiple-choice question must include:
- question number
- cognitive level
- question type
- question content
- options
- `Đáp án đúng`
- `Giải thích`
- `Trích dẫn`

If a question uses media, the question must also make it clear what the learner must observe.

### 5.2 Practical Exercise Contract

Each practical exercise keeps the current template structure:

1. `Nội dung đề bài`
2. `Yêu cầu kỹ thuật chi tiết`
3. `Sản phẩm yêu cầu bàn giao`
4. `Đáp án gợi ý (Kịch bản khối lệnh logic)`
5. `Tiêu chí chấm điểm (Rubric định lượng)`

## 6. Media Contract

If the exam uses media, the sibling media folder must contain all referenced assets used by the draft.

Accepted asset categories:
- image
- video
- gif
- physical code sample
- physical project file
- physical source export

The draft may reference media inline using existing file naming patterns already in use by the workspace.

## 7. Naming Reference Rules

The workflow does **not** force a new on-disk naming scheme.

Instead, the spec records these reference rules:
- media may be labeled in the exam body by question-local numbering such as `1.1`, `1.2`, `1.3`
- labels are for human reading and review
- physical filenames on disk may remain in the current workspace convention
- the draft must reference assets consistently enough for a human reviewer to locate them

## 8. Hard Rules For Code Samples And Demo Videos

### 8.1 Code Sample Rule

Code samples must never exist only as screenshots.

If a code sample appears in the exam as:
- block-code image
- code screenshot
- project sample
- generated tool screenshot

then there must be a corresponding physical source artifact in the media folder or an explicitly referenced physical source file.

Accepted physical source examples:
- `.sb3`
- `.xml`
- `.ino`
- `.py`
- `.js`
- equivalent tool-native project/source files

### 8.2 Demo Video Rule

If a demo video is included as sample media or evidence for a code-based scenario, there must also be a physical code or project file behind that demo.

Hard rule:

```text
No demo video without a physical source file.
```

### 8.3 Image Exception

Purely illustrative images may exist without a physical executable source file.

This exception applies to:
- interface screenshots
- equipment photos
- neutral illustrations

This exception does **not** apply when the image is representing executable or reproducible code logic that should be reviewable as a real artifact.

## 9. Practical Exercise Delivery Rule

For practical exercises, `Sản phẩm yêu cầu bàn giao` must explicitly state what learners submit.

Typical examples:
- one `.sb3` file
- one project file
- one video demo under 2 minutes
- one image set
- one public link

The requirement must be concrete enough that a human reviewer can determine whether the submission is complete without interpretation.

## 10. Link Rule

If the exam references sample project links, those links must:
- be clearly identified in the draft
- point to the intended artifact
- be reviewable by the human publishing step before LMS release

The agent may include the links in draft content, but the human publishing step owns final activation and placement in Google Docs / LMS.

## 11. Workflow

1. Select course materials from `workspaces/learning/courses/`.
2. Draft the internal exam markdown source.
3. Attach or reference media assets in the sibling media folder when needed.
4. Ensure every MCQ has `Đáp án đúng`, `Giải thích`, `Trích dẫn`.
5. Keep practical exercises in the agreed template structure.
6. If any code sample or demo video exists, confirm the physical source file exists.
7. Hand off the internal draft to human review.
8. Human copies approved content into Google Docs and later LMS.

## 12. Validation Checklist

Before handoff, verify:
- the draft contains exam information, matrix, MCQ, and practical sections
- each MCQ contains `Đáp án đúng`, `Giải thích`, `Trích dẫn`
- each practical exercise contains deliverables and rubric
- media references resolve to real files when required
- code sample screenshots are backed by physical source files
- demo videos are backed by physical source files

## 13. AI THCS Test Requirement

A concrete validation run for the AI THCS draft should prove at least:
- the practical section contains 3 exercises
- each practical exercise requests both a project/code deliverable and a demo video
- the exam package has physical code sample artifacts available for review

## 14. Non-Goals

This workflow intentionally does **not** require:
- a separate internal grading file by default
- automatic Google Docs rendering
- forced manifest files for every exam
- a new file naming migration for existing media assets

The workflow stays lightweight on purpose.