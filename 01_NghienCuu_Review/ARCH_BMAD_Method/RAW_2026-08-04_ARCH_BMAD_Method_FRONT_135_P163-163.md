# HD SOURCE: ARCH_BMAD_Method_FRONT_135_P163-163
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_135
Part Title: NONE
Chapter Title: NONE
Section Title: Murat - master test architect
Chunk Range: Pages 163 to 163
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
u có)
```

```
- Branching narrative decisions (nế ## 5. art direction - Visual style reference - Color palette vàmood - Audio direction ## 6. technical requirements - Target platforms và performance - Engine constraints - Online features (nếu có)
```

## Narrative design support

GDS bao gồm hỗ trợ đặc biệt cho narrative design mà các module khác không có:

Nhân vật:

Personality profiles, arcs phát triển nhân vật, dialogue voice

Dialogue:

Branching dialogue trees và conversation flows

World-building:

Lore documents, faction design, world history timeline

Quest design:

Quest structures, objectives, reward systems

## Rapid prototyping với quick dev

```
bmad-quick-dev "Prototype core combat loop: -Người chơi tấn công bằng cách click vào enemy - Mỗiôattack giảm HP của enemy theo formula: [damage - defense] (min 1) - Enemy chết khi HP về 0, drop coin với rarity based on enemy type -Người chơi pick up coin bằng cách đi qua - Implement trong Godot 4 với GDScript"
```

Prototype cơchếtrước khi đầu tưvào full production implementation.

## 14.5 test architect (tea)  -  kiểm thử cấp doanh nghiệp

Mã code cài đặt: tea

## Môtả chính thức

"Chiến lược kiểm thử cấp doanh nghiệp, hướng dẫn automation, và quyết định release gate thông qua một expert agent và chín workflows cócấu trúc. TEA đi xa hơn QA agent được tích hợp sẵn với risk-based prioritization và requirements traceability."

TEA không phải là "QA agent tốt hơn" -đây làmột hệthống kiểm thử hoàn chỉnh với chiến lược, frameworks, và cổng release được document.

## Murat  -  master test architect