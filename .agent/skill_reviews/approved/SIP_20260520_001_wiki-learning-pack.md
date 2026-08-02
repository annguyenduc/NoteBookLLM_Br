# SIP_20260520_001_wiki-learning-pack.md

## Metadata
```yaml
sip_id: SIP_20260520_001
skill_id: wiki-learning-pack
proposed_skill_path: .agent/skills/wiki-learning-pack/SKILL.md
trigger: missing_step
created: 2026-05-20
status: APPROVED_IMPLEMENTED
author: "@librarian"
phase: IMPLEMENTED
approval_required: true
production_edit_performed: true
```

## Implementation Result

- AN approved with `go` after production state inspection.
- Production skill exists at `.agent/skills/wiki-learning-pack/SKILL.md`.
- `quick_validate.py` passed with `PYTHONUTF8=1`.
- No Learning Pack artifact was created in this closeout.
- No atom, ingest, rebuild, promote, or synthesis action was performed.

## Evidence

AN đã chốt rằng sau khi atom của `Thinking in Systems` đã xong thì không nên quay lại nhóm ingest. Lớp cần thêm là **Learning UX layer** đặt trên các atom đã có để học, luyện nhớ, ứng dụng và truy vấn nhanh.

AN đề xuất `wiki-learning-pack` là skill mới còn thiếu lớn nhất:

- Atom là "viên gạch"; Learning Pack là "buổi học".
- Output mong muốn là một learning artifact duy nhất, ví dụ `LEARNING_PACK_ARCH_TIS_Fast_Start.md`.
- Skill phải read-heavy, write-light: đọc nhiều atom nhưng chỉ sinh một file học tập.
- Không được làm loãng vault, không quay lại ingest, không đụng concepts/entities/sources.

Thông tin mục tiêu do AN cung cấp:

- `Thinking in Systems` hiện đã có 33 atom.
- Thành phần gồm 1 source atom, 3 entity atom, 29 concept atom.
- Index/database đã rebuild xong.

Unknowns:

- Trạng thái atom/count hiện tại chưa được verify lại bằng DB trong lượt này.
- Chưa kiểm tra folder `3-resources/wiki/learning_packs/` đã tồn tại chưa.
- Lúc tạo SIP ban đầu chưa có production skill; closeout hiện tại đã tạo `.agent/skills/wiki-learning-pack/SKILL.md` và `quick_validate.py` đã PASS với `PYTHONUTF8=1`.

## Problem

Vault hiện đã có các skill truy vấn và audit như `wiki-query`, `wiki-semantic-search`, `wiki-breakdown`, `wiki-learning-audit`, nhưng chưa có skill biến một cụm atom đã indexed thành một trải nghiệm học nhanh có cấu trúc.

Nếu chỉ dùng `/query`, output dễ biến thành summary dài hoặc trả lời cục bộ theo keyword. Nếu dùng `pedagogy` quá sớm, workflow nhảy thẳng sang giáo án/slide khi người học còn cần một gói tự học nhanh trước.

Khoảng trống cần lấp:

- Tổ chức atom thành learning path 60-90 phút.
- Tạo concept map, must-know atoms, failure modes, practice task và review questions.
- Giữ source trace rõ ràng.
- Không tạo atom mới, không chạy ingest, không tạo synthesis final.

## Proposed Change

Tạo skill mới `wiki-learning-pack` theo SPEC dưới đây.

# SPEC: wiki-learning-pack

## Objective

Tạo một Learning Pack từ các atom đã có để học nhanh một topic trong 60-90 phút mà không phải đọc lại toàn bộ source.

## Owner

Primary: `@librarian`  
Handoff: `@designer` nếu cần chuyển Learning Pack thành giáo án, slide, activity sheet, rubric.

## Scope

- Input: `source_id` hoặc topic, ví dụ `ARCH_TIS`.
- Consume: wiki atoms đã indexed.
- Ưu tiên atom `VERIFIED` / `SYNTHESIZED`.
- Cho phép dùng `DRAFT` atom chỉ khi output gắn nhãn `EXPLORATORY`.
- Output proposal:
  `3-resources/wiki/learning_packs/LEARNING_PACK_[TOPIC].md`

## Non-goals

- Không chạy ingest lại.
- Không tạo atom mới.
- Không set `SYNTHESIZED`.
- Không thay thế `wiki-query`, `wiki-semantic-search`, `wiki-breakdown`.
- Không biến thành giáo án hoặc slide; phần đó thuộc `pedagogy`.

## Status Policy

- Prefer `VERIFIED` / `SYNTHESIZED` atoms.
- `DRAFT` atoms chỉ được dùng nếu output gắn nhãn `EXPLORATORY`.
- Không được dùng atom thiếu source trace.
- Nếu status mixed hoặc thiếu trace, báo rõ trong `Missing Context` và không trình bày như kiến thức đã chốt.

## Output Contract

```md
# Big Picture
# Key Concepts
# Concept Map
# Must-Know Atoms
# Comparison Table
# Failure Modes
# Practice Task
# Review Questions
# Related Projects
# Source Trace
# Missing Context
# Next Action
```

## Workflow

1. Chạy `wiki-status` hoặc đọc index để xác nhận topic đã có atom.
2. Dùng `wiki-query` lấy atom chính xác theo `source_id/topic`.
3. Dùng `wiki-semantic-search` bổ sung atom liên quan khi keyword thiếu.
4. Gom atom thành learning path 60-90 phút.
5. Tạo Learning Pack theo Output Contract.
6. Gắn `Source Trace` tới atom/source, không trích từ recon/NotebookLM.
7. Đưa `Missing Context` sang `wiki-breakdown` nếu thiếu khái niệm cản học.

## Write Boundary

- Chat-only proposal trước GO.
- Khi được GO, chỉ tạo file trong:
  `3-resources/wiki/learning_packs/`
- Không patch concepts/entities/sources.
- Không rebuild nếu chưa có yêu cầu riêng.
- Không promote, không move, không xoá artifact khác.

## Governance Note

Learning Pack là learning artifact, không phải final synthesis.
Không được set `SYNTHESIZED`.
Nếu có metadata, dùng `status: "DRAFT"` hoặc `status: "LEARNING_DRAFT"`.

## Acceptance Criteria

- Người học biết học gì trước, gì sau.
- Mỗi claim quan trọng trace được về atom/source.
- Có practice task để chuyển từ đọc sang dùng.
- Có failure modes để tránh hiểu sai.
- Có review questions để tự kiểm tra.
- Không sinh thêm atom hoặc ingest artifact.
- Không dùng NotebookLM recon làm source of truth.
- Không dùng atom thiếu source trace.

## First Use Case

`LEARNING_PACK_ARCH_TIS_Fast_Start.md`

Mục tiêu: học nhanh `Thinking in Systems` trong 60-90 phút từ 33 atom hiện có.

## Proposed Skill Behavior

Future `SKILL.md` nên ngắn, operational, và không chứa toàn bộ domain content. Body nên nói rõ:

- Khi nào dùng: user muốn học nhanh từ atom/wiki, tạo fast-start learning pack, tạo review path từ topic/source.
- Khi nào không dùng: ingest, atom creation, synthesis final, pedagogy output, slide/lesson plan.
- Primary owner là `@librarian`; handoff sang `@designer` khi user yêu cầu giáo án/slide/activity.
- Luôn kiểm status/source trace trước khi viết.
- Mặc định trả proposal trong chat; chỉ tạo file khi AN GO.

Không cần script trong Phase 1. Có thể bắt đầu bằng `SKILL.md` thuần hướng dẫn; nếu workflow lặp lại nhiều mới thêm script hỗ trợ query/gom atom.

## Regression Cases

### Case 1: ARCH_TIS Fast Start

Input:

```text
Tạo Learning Pack Fast Start cho ARCH_TIS
```

Expected:

- Skill dùng `wiki-query` / index để gom atom liên quan.
- Output theo đúng Output Contract.
- Nếu viết file, chỉ viết `3-resources/wiki/learning_packs/LEARNING_PACK_ARCH_TIS_Fast_Start.md`.
- Không tạo atom mới, không chạy ingest, không rebuild.

### Case 2: Mixed Status Atoms

Input:

```text
Tạo Learning Pack cho một topic có cả VERIFIED và DRAFT atoms
```

Expected:

- VERIFIED/SYNTHESIZED được ưu tiên.
- DRAFT chỉ được dùng trong phần gắn nhãn `EXPLORATORY`.
- Missing trace/status được đưa vào `Missing Context`.

### Case 3: User Asks For Slide

Input:

```text
Biến ARCH_TIS thành slide dạy học
```

Expected:

- `wiki-learning-pack` không tự làm slide.
- Handoff sang `@designer` / `pedagogy` sau khi Learning Pack hoặc learning outline rõ.

## Validation Plan For Implementation

Khi AN approve + GO tạo production skill:

1. Tạo `.agent/skills/wiki-learning-pack/SKILL.md`.
2. Không sửa skill khác nếu chưa có GO riêng.
3. Chạy structural validation bằng `quick_validate.py` nếu available; trên Windows dùng `PYTHONUTF8=1` nếu cần.
4. Kiểm tra không có duplicate frontmatter.
5. Kiểm tra `SKILL.md` không chứa absolute path ngoài các path policy cần thiết của vault.
6. Smoke test chat-only với input `ARCH_TIS Fast Start` trước khi cho phép write artifact thật.

## Risk

Risk: medium.

Lý do:

- Skill này đọc rộng qua wiki atoms, nên dễ kéo quá nhiều context nếu không có output contract.
- Nếu không có status/source trace policy, Learning Pack có thể biến DRAFT/untraced atoms thành tri thức có vẻ đã chốt.
- Nếu không có write boundary, workflow có thể vô tình quay lại ingest hoặc tạo thêm atom.

Mitigation:

- Giữ read-heavy, write-light.
- Enforce Output Contract.
- Enforce Status Policy và Write Boundary.
- Chỉ tạo một learning artifact duy nhất khi có GO.

## AN Decision

- [x] Approve + GO -> production skill exists at `.agent/skills/wiki-learning-pack/SKILL.md`; SIP lifecycle closed.
- [ ] Reject -> reason: ___
- [ ] Defer -> review again after: ___
