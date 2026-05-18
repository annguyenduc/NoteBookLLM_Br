---
artifact_type: "ingest_figures_map"
source_id: "arch_thinking_in_systems"
source_evidence_file: "3-resources/raw_sources/ARCH_Thinking_in_Systems.pdf"
primary_ingest_file: "3-resources/raw_ingest/arch_thinking_in_systems/manifest.md"
asset_root: "3-resources/raw_assets/"
status: "READY"
created_at: "2026-05-18"
---
# FIGURES_ARCH_TIS

## Tóm tắt trạng thái

Visual evidence đã có trong `3-resources/raw_assets/` cho các chunk Chapter One. Batch materialize hiện tại chỉ dùng các hình đã được chunk markdown nhúng bằng wikilink; không có `PENDING_EXTRACTION`.

## Hình cần chú ý trong batch đầu tiên

| Chunk | Trang | Asset status | Nội dung |
|---|---:|---|---|
| `RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC03_P034-041.md` | 34-41 | READY | Stock-and-flow diagrams, bathtub system, dynamic equilibrium. |
| `RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC04_P042-043.md` | 42-43 | READY | Feedback loop introduction. |
| `RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC05_P044-046.md` | 44-46 | READY | Balancing feedback loop, coffee/energy examples. |
| `RAW_2026-05-18_ARCH_Thinking_in_Systems_CH01_SEC06_P047-051.md` | 47-51 | READY | Reinforcing feedback loop, interest-bearing account, reinvestment loop. |

## Gate

- `PENDING_EXTRACTION`: NONE
- `ASSETS_PRESENT_BUT_UNREGISTERED`: NONE for current batch
- `READY`: YES

Nếu batch sau dùng chương khác, file này phải được mở rộng trước khi chuyển `READY_FOR_GENERATE`.
