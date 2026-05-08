---
name: wiki-council
description: "Use when knowledge contradictions (CONTRADICTS edges) cannot be resolved by automated logic and require multi-agent weighted consensus (The Iron Triangle). Triggers automatically from wiki-absorb or via /council command."
---

# Wiki Council (Iron Triangle v3.0)

## Overview
Hội đồng quản trị tri thức (Governance) sử dụng mô hình **Multi-Agent Epistemic Governance** để giải quyết các mâu thuẫn tri thức phức tạp. Hệ thống không chỉ đơn thuần là "bỏ phiếu đa số" mà áp dụng cơ chế **Trọng số theo vai diễn (Weighted Roles)** để đảm bảo tính phản biện và chính xác cao nhất.

## The Iron Triangle (Đội hình 3 Elder)
Hệ thống vận hành tối ưu trên 4GB VRAM với 3 thành viên chủ chốt:
1. **Logician (`qwen2.5:3b`) - Trọng số 1.0**: (R4) Soi xét tính nhất quán, logic và kỷ luật định dạng.
2. **Generalist (`phi3:mini`) - Trọng số 0.8**: Đánh giá giá trị nội dung và khả năng đọc hiểu.
3. **Dissenter (`qwen3:4b`) - Trọng số 1.2**: Vai trò quan trọng nhất — chuyên tìm kiếm lỗ hổng, nghi ngờ nguồn tin và đặt câu hỏi phản biện.

## Governance Protocol (3-Stage)
1. **Stage 1 (Local Deliberation):** 3 Elder độc lập đánh giá mâu thuẫn dựa trên Role-specific Prompts.
2. **Stage 2 (Weighted Consensus):** Tổng hợp phiếu bầu theo trọng số. 
   - Ngưỡng đồng thuận: **> 1.5**.
   - Nếu vượt ngưỡng, phán quyết được thi hành ngay.
3. **Stage 3 (Chairman Synthesis):** Nếu Local không đạt đồng thuận (hoặc có lỗi hệ thống), hồ sơ được chuyển lên **Chairman (Cloud Nemotron-120B)** để đưa ra phán quyết cuối cùng dựa trên toàn bộ chứng cứ.

## Guardrails
- **Surgical Change**: Hội đồng chỉ can thiệp khi có `CONTRADICTS`. Không dùng cho việc sửa lỗi chính tả hay đổi tên file.
- **Traceability (R3)**: Mọi phán quyết của Council phải được ghi log vào `3-resources/wiki/decisions/`.
- **Logging First (R21)**: Phải tạo entry nhật ký ngày trước khi thực thi phán quyết.
- **Latency**: Tổng thời gian xử lý mục tiêu cho 3 Elder là **< 120 giây**.

## Quick Reference
- **Engine**: `.agent/skills/wiki-council/scripts/council_engine.py`
- **Audit Log**: `3-resources/wiki/decisions/` (Dành cho các phán quyết phức tạp).
- **Template**: Sử dụng `.agent/skills/references/DECISION_TEMPLATE.md` để ghi nhận phán quyết.


## Technical Keywords (Audit)
- **conflict**: Knowledge contradiction requiring resolution.
- **shared utility**: Common goal of systemic integrity.
- **poll**: Mechanism for multi-agent weighted voting.
- **peer review**: Cross-validation of agent conclusions.

## Technical Reference
- council: shared utility, không trigger độc lập
- conflict: điều kiện kích hoạt council
- shared utility: gọi từ wiki-absorb hoặc wiki-query
- poll: Stage 1 — gửi query đến tất cả council members
- peer review: Stage 2 — các model đánh giá nhau
- chairman: Stage 3 — tổng hợp output cuối cùng
