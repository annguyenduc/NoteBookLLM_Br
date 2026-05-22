---
decision_id: "ADR_20260522_001"
title: "Hợp nhất cm-instinct-learning vào 3 cơ chế hiện có"
status: "PROPOSED"
created: "2026-05-22"
author: "agent (gợi ý), AN (quyết định)"
tags: ["governance", "skill-management", "memory", "instinct"]
---

# ADR-001: Xử lý cm-instinct-learning — Giữ hay Merge?

## Bối cảnh (Context)

Vault hiện có **4 cơ chế** phục vụ mục tiêu "ghi nhớ / học từ session":

| Cơ chế | Storage | Format | Đang dùng? |
|---|---|---|---|
| `session_insights/` | `3-resources/wiki/session_insights/INSIGHT_*.md` | Narrative markdown, 1 file/session | ✅ 27 files, active |
| `cm-continuity` | `CONTINUITY.md` (root) | YAML state, ghi đè liên tục | ✅ Active, runtime |
| `skill_reviews/SIP` | `.agent/skill_reviews/pending/*.md` | Structured patch proposal | ✅ 6 SIPs từ 20/5 |
| `cm-instinct-learning` | `.agent/instincts/*.yaml` | Atomic YAML + confidence score | ⚠️ Mới tạo, chưa có loader |

**Vấn đề phát hiện hôm nay (2026-05-22):**
- `cm-instinct-learning` được cherry-pick từ repo ngoài (ECC — `affaan-m/everything-claude-code`).
- Không có cơ chế nào trong AGENTS.md hoặc startup rules load `.agent/instincts/` tự động.
- Nội dung nó capture (behavioral patterns + evidence) đã được 3 cơ chế kia cover:
  - **Narrative** → session_insights
  - **Runtime state / lỗi gặp** → cm-continuity
  - **Hành động cụ thể cần patch skill** → SIP

## Phân tích trùng lặp

```
session_insights    ≈  instinct.Evidence + instinct.Action (dạng narrative dài)
cm-continuity       ≈  instinct.Evidence (runtime, sẽ bị ghi đè sau session)
skill_reviews/SIP   ≈  instinct đã đủ confidence → formalize thành skill patch
cm-instinct-learning = wrapper thêm: confidence score + trigger condition + atomic format
```

**Giá trị riêng của cm-instinct-learning** (nếu có loader):
- Confidence score → có thể tự tăng/giảm theo thời gian
- Trigger condition → routing agent tự động không cần human instruction
- Atomic format → dễ cluster và evolve thành Rules/Skills

**Chi phí nếu giữ nguyên không integrate:**
- 1 layer thêm không có giá trị thực (không ai đọc, không auto-load)
- Agent có thể trigger nhầm (như đã xảy ra hôm nay: "session insight" → đọc cm-instinct-learning)
- Maintenance overhead: phải update 4 chỗ thay vì 3

---

## Các lựa chọn (Options)

### Option A — Deprecate cm-instinct-learning (Merge vào 3 cơ chế hiện có)

**Làm gì:**
- Xóa (hoặc archive) skill `cm-instinct-learning` khỏi `.agent/skills/` và global skills.
- Xóa `.agent/instincts/` vừa tạo hôm nay.
- Thêm section `## Instincts` chuẩn hóa vào cuối mỗi `INSIGHT_*.md` (đã có pattern `## 4. Bài học hệ thống`).
- Khi instinct đủ mạnh → mở SIP.

**Ưu điểm:**
- Giảm cognitive overhead: 3 thay vì 4 hệ thống.
- Không thêm token/routing confusion.
- session_insights đã có slot `## 4. Bài học hệ thống / Instincts` — chỉ cần giữ nhất quán.

**Nhược điểm:**
- Mất confidence score và lifecycle evolution (tentative → promote).
- Nếu sau này muốn auto-routing instincts phải build lại từ đầu.

---

### Option B — Giữ cm-instinct-learning, nhưng integrate đúng cách

**Làm gì:**
- Thêm loader trong AGENTS.md: "On startup, nếu task liên quan đến git/scripting/skill-management, đọc `.agent/instincts/global/*.yaml`."
- Thêm note trong `session_insights` template: "Khi viết bài học hệ thống, nếu pattern đủ atomic → tạo file instinct tương ứng."
- Viết rõ boundary: instinct = future-facing behavior rule; session insight = past-facing narrative log.

**Ưu điểm:**
- Giữ được confidence lifecycle và auto-routing tiềm năng.
- 4 hệ thống hoạt động bổ sung nhau thay vì trùng lặp.

**Nhược điểm:**
- Cần thêm AGENTS.md rule → token overhead startup tăng.
- Cần maintain consistency giữa instinct và session insight (2 lần viết cùng 1 insight).
- Chưa chắc anh dùng confidence score — nếu không có người review thì score vô nghĩa.

---

### Option C — Defer: Giữ instinct files hôm nay, chưa integrate, review sau 30 ngày

**Làm gì:**
- Để `.agent/instincts/` như đang có.
- Không thêm loader.
- Review lại sau 1 tháng xem có instinct nào thật sự hữu ích không.

**Ưu điểm:**
- Không phải quyết định ngay.
- Có thêm evidence trước khi chọn.

**Nhược điểm:**
- Vẫn có routing confusion (agent có thể trigger nhầm).
- Files tồn tại nhưng không ai đọc — dead weight.

---

## Khuyến nghị của Agent

> **Option A** — Merge vào 3 cơ chế hiện có.

**Lý do:**

1. `session_insights` đã phục vụ tốt 27 sessions. Thêm `## Instincts` chuẩn hóa vào cuối là đủ.
2. `cm-instinct-learning` không có loader → confidence score hiện tại là metadata chết, không có giá trị thực thi.
3. Anh đã có `SIP` làm bước "promote instinct → skill patch" — đây chính là Phase 4 của cm-instinct-learning nhưng đã hoạt động tốt hơn.
4. Giảm từ 4 → 3 cơ chế = giảm cognitive load và routing confusion cho agent.

**Nếu sau này cần auto-routing instinct**, có thể revive Option B với đầy đủ loader mechanism — nhưng đó là feature riêng, không cần giữ skeleton chết hiện tại.

---

## AN Decision

- [ ] **Option A — Merge/Deprecate** `cm-instinct-learning`
  - [ ] Xóa skill khỏi `.agent/skills/` và global skills
  - [ ] Xóa `.agent/instincts/` vừa tạo hôm nay
  - [ ] Chuẩn hóa section `## Instincts` trong INSIGHT template
- [ ] **Option B — Integrate đúng cách** (thêm loader vào AGENTS.md)
- [ ] **Option C — Defer** 30 ngày
- [ ] Reject đề xuất — lý do: ___
