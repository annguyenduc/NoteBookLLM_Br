---
artifact_type: "ingest_map"
source_id: "arch_thinking_in_systems"
source_evidence_file: "3-resources/raw_sources/ARCH_Thinking_in_Systems.pdf"
primary_ingest_file: "3-resources/raw_ingest/arch_thinking_in_systems/manifest.md"
status: "READY_FOR_REVIEW"
created_at: "2026-05-18"
---
# MAP_ARCH_TIS

## Vai trò

File này là extraction map cho `ARCH_TIS`, dùng để nối `STRUCTURE_ARCH_TIS.md`, `FIGURES_ARCH_TIS.md`, `NAMING_LOCK_ARCH_TIS.md`, và các `Analysis_ARCH_TIS_CHUNK_XX.md`.

## Knowledge pillars

| Pillar | Mô tả | Batch |
|---|---|---|
| System definition | Hệ thống gồm elements, interconnections, purpose/function. | 01 |
| Stock-flow dynamics | Stock là tích lũy/ký ức; flow thay đổi stock theo thời gian. | 01 |
| Feedback loops | Feedback loop nối stock, rules/actions, và flow quay lại thay đổi stock. | 01 |
| Stability vs amplification | Balancing loop ổn định; reinforcing loop khuếch đại. | 01 |
| System zoo | Các mô hình một stock/hai stock và ví dụ ứng dụng. | later |
| Resilience and self-organization | Vì sao hệ thống vận hành tốt. | later |
| Traps and leverage | Bẫy hệ thống và điểm đòn bẩy. | later |

## Batch 01 handoff

Batch 01 tạo analysis từ Chapter One, không tạo Atom trực tiếp. Atom candidates mạnh nhất:

- `CONCEPT_ARCH_TIS_System.md`
- `CONCEPT_ARCH_TIS_Stock.md`
- `CONCEPT_ARCH_TIS_Flow.md`
- `CONCEPT_ARCH_TIS_Dynamic_Equilibrium.md`
- `CONCEPT_ARCH_TIS_Feedback_Loop.md`
- `CONCEPT_ARCH_TIS_Balancing_Feedback.md`
- `CONCEPT_ARCH_TIS_Reinforcing_Feedback.md`
- `ENTITY_ARCH_TIS_Donella_Meadows.md`
- `SOURCE_ARCH_TIS_Thinking_in_Systems.md`

## Rủi ro

- NotebookLM recon chỉ là query notes; không dùng làm source evidence.
- Các Atom cũ trong DB có prefix `SYS_ARCH_TIS` đang `DEPRECATED`; không dùng làm canonical target.
- Batch 01 chỉ bao phủ nền tảng. Không được tạo Atom về system traps/leverage points cho đến khi đọc batch tương ứng.
