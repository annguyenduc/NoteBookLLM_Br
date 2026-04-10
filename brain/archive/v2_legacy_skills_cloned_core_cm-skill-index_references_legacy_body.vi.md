# 🗂️ Skill Index (LITE)

> **Goal:** Tiết kiệm 90%+ token thông qua cơ chế nạp lũy tiến (Progressive Disclosure). AI chỉ nạp danh mục sơ lược để chọn đúng skill, sau đó mới nạp chi tiết khi thực thi.

## 🏗️ 3-Layer Loading Model
| Layer | Name | Content | Token Cost |
|---|---|---|---|
| **L1** | **Index** | Name + Domain + Triggers. | ~100t / skill |
| **L2** | **Summary** | Description + Integration table. | ~300t / skill |
| **L3** | **Full** | Complete instructions + Red Flags. | 1500t+ / skill |

## 🚀 Core Skills Swarm (L1 Index)
Hệ thống được tối ưu hóa theo 3 luồng công việc chính (Gõ prefix để gọi nhanh):

| Domain | Skills | Key Triggers |
|---|---|---|
| **`ToT —`** (Trainer) | `module-architect`, `teacher-needs`, `steam-content-factory`, `assessment-forge`, `unit-planner` | dạy GV, đào tạo, lesson plan, slide training, audit ToT. |
| **`K-12 —`** (Student)| `k12-pbl-designer`, `k12-id-expert`, `k12-iot-scaffold`, `k12-math-expert`, `k12-science-inquiry` | dạy HS, dự án PBL, thí nghiệm, giải toán, robot lớp 5. |
| **`CORE —`** (System) | `cm-planning`, `cm-terminal`, `cm-git-flow`, `cm-code-review`, `cm-codeintell`, `cm-start` | lập plan, terminal, git, review, khởi động hệ thống. |
| **Orchestration** | `cm-execution`, `cm-continuity`, `cm-skill-mastery`, `cm-skill-chain` | thực thi, bộ nhớ, chọn kĩ năng, chuỗi tự động. |
| **Growth/Docs** | `cm-dockit`, `cm-document-publishing`, `cm-auto-publisher` | tạo tài liệu, xuất bản B2B, đẩy web Astro. |

## 🌍 Community Registry (npx)
- **Frontend:** `react-best-practices`, `astro-best-practices`, `nextjs-patterns`.
- **Backend/DB:** `supabase-postgres`, `prisma-client`, `drizzle-orm`.
- **AI/ML:** `vercel-ai-sdk`, `langchain-skills`, `openai-skills`.
- **Command:** `npx skills add {source} --skill {name}`.

## 📐 Usage Protocol
1. **At Session Start:** Nạp Layer 1 Index (~2500 tokens) để nắm bắt toàn bộ Kit.
2. **Task Matching:** Dựa vào Triggers để chọn skill phù hợp.
3. **Deep Dive:** Đọc Layer 2 (Common/First 20 lines) nếu cần xác nhận lại.
4. **Execution:** Nạp Layer 3 (Full `SKILL.md`) để bắt đầu thực hiện.

## 🚨 Quality Gate (Red Flags)
- ❌ Nạp toàn bộ 51 file `SKILL.md` ngay từ đầu (Lãng phí cực lớn token).
- ❌ Dùng sai skill do không check kỹ Triggers ở Layer 1.
- ❌ Quên cập nhật Index sau khi cài đặt Skill mới từ Community.
- ❌ Không phân loại Skill vào đúng Domain (Swarm) gây khó khăn khi tìm kiếm.

## 💡 Example Triggers
- "Liệt kê các skill hiện có trong bộ Kit."
- "Tìm skill nào hỗ trợ thiết kế database Prisma."
- "Tôi nên dùng skill nào cho task viết blog marketing?"

## Migration Compatibility (v5)
- Legacy `tot-*` IDs are mapped through `skill-alias-map.v5.json`.
- Router/index must resolve both legacy and canonical IDs during transition.

