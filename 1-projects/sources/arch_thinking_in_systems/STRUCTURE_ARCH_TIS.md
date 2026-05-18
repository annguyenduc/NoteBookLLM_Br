---
artifact_type: "ingest_structure"
source_id: "arch_thinking_in_systems"
source_evidence_file: "3-resources/raw_sources/ARCH_Thinking_in_Systems.pdf"
primary_ingest_file: "3-resources/raw_ingest/arch_thinking_in_systems/manifest.md"
status: "READY_FOR_REVIEW"
created_at: "2026-05-18"
---
# STRUCTURE_ARCH_TIS

## Tóm tắt trạng thái

Artifact này tái tạo lại structure map cho `ARCH_TIS` sau reset/cleanup. Nguồn canonical hiện tại là package raw ingest:

- `3-resources/raw_ingest/arch_thinking_in_systems/manifest.md`
- `3-resources/raw_ingest/arch_thinking_in_systems/outline.md`
- `3-resources/raw_ingest/arch_thinking_in_systems/chunks/`

## Cấu trúc nguồn đã khóa

| Vùng | Trang | Trạng thái | Ghi chú |
|---|---:|---|---|
| Chapter One - The Basics | 28-51 | READY | Batch analysis đầu tiên dùng chương này làm foundation batch. |
| Chapter Two - A Brief Visit to the Systems Zoo | 52-89 | READY | Dùng cho model examples sau khi foundation batch được duyệt. |
| Chapter Three - Why Systems Work So Well | 92-102 | READY | Resilience, self-organization, hierarchy. |
| Chapter Four - Why Systems Surprise Us | 103-127 | READY | Dùng cho traps/tensions sau. |
| Chapter Five - System Traps and Opportunities | 128-159 | READY | Dùng cho archetypes/traps. |
| Chapter Six - Leverage Points | 162-182 | READY | Dùng cho leverage points. |
| Chapter Seven - Living in a World of Systems | 187-211 | READY | Dùng cho thinking practice và worldview. |
| Front/back matter | 1-27, 90-91, 160-161, 183-186, 212-235 | READY | Chỉ dùng khi cần provenance, glossary, appendix, notes. |

## Batch materialize hiện tại

Batch đầu tiên chỉ bao phủ Chapter One:

- `RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC01_P028-028.md`
- `RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC02_P029-033.md`
- `RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC03_P034-041.md`
- `RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC04_P042-043.md`
- `RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC05_P044-046.md`
- `RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC06_P047-051.md`

## Dấu vết kiểm toán

Structure này không phải source evidence. Nó là control artifact để điều phối `ingest` trước khi chuyển sang `.agent/workflows/ingest-generate.md`.
