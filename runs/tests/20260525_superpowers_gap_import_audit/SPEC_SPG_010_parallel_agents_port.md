# SPEC-SPG-010: Port & Adapt `dispatching-parallel-agents` With Token Budget Guard

Bản Spec này chi tiết hóa cách thức nhập khẩu (port) kỹ năng điều phối tác nhân song song `dispatching-parallel-agents` từ Superpowers làm Core Standard, đồng thời tích hợp (merge) logic kiểm soát ngân sách token (Token Budget Guard) từ `cm-context-budget` cũ của vault `NoteBookLLM_Br`.

---

## 1. MỤC TIÊU & BỐI CẢNH

### 1.1. Bối cảnh
Khi đối mặt với nhiều lỗi kiểm thử hoặc nhiệm vụ phát triển độc lập trong cùng một phiên, việc chạy tuần tự (Sequential) gây lãng phí thời gian. Kỹ năng `dispatching-parallel-agents` của Superpowers giải quyết vấn đề này bằng cách chạy song song các tác nhân chuyên biệt (subagents) có ngữ cảnh cô lập.

### 1.2. Vấn đề của Vault
Chạy song song nhiều subagents trong một session của Antigravity sẽ nhân bản ngữ cảnh rất nhanh, dễ dẫn đến **Context Bloat** (phình token ngữ cảnh), gây chậm phản hồi hoặc vượt quá giới hạn cứng của mô hình LLM.

### 1.3. Giải pháp
Chuẩn hóa kỹ năng điều phối tác nhân song song theo Superpowers, đồng thời bổ sung một **Adaptation Section** chứa bộ quy tắc kiểm soát token nghiêm ngặt (Token Budget Guard & Context Circuit Breaker) kế thừa từ `cm-context-budget` của vault.

---

## 2. CHI TIẾT THÍCH NGHI (VAULT ADAPTATIONS)

Kỹ năng port mới sẽ bắt buộc Agent tuân thủ các chốt chặn an toàn sau trước khi dispatch subagents:

### 2.1. Quy tắc Tính toán & Kiểm soát Ngân sách Token (Token Budget Guard)
Trước khi quyết định dispatch bất kỳ subagent nào, Agent bắt buộc phải tính toán:
1. **Dung lượng token hiện tại của phiên chính:** Sử dụng công thức ước lượng `words * 1.3` (cho văn bản) hoặc `chars / 4` (cho code).
2. **Dung lượng token dự kiến của mỗi subagent:** Bao gồm system prompt, file context được truyền và nhiệm vụ cụ thể.
3. **Tổng dung lượng dự kiến sau khi nhân bản:** `Main Session Tokens + (Subagent count * Subagent estimated tokens)`.

### 2.2. Bộ Ngắt Mạch Ngữ Cảnh (Context Circuit Breaker)
- **Cảnh báo (Warning threshold) - 70% Context Window:** Nếu tổng dung lượng token dự kiến vượt quá 70%, Agent phải cảnh báo rõ trong phiên chính về nguy cơ phình token.
- **Ngắt mạch / Fallback tuần tự - 80% Context Window:** Nếu tổng dung lượng dự kiến vượt quá 80%, Agent **tuyệt đối cấm** chạy song song. Bắt buộc phải chuyển sang chế độ **Sequential Fallback** (chạy tuần tự từng tác nhân hoặc giải quyết trực tiếp trong phiên chính) để bảo vệ token budget.

### 2.3. Quy tắc Cô lập Ngữ cảnh (Isolated Context Rule)
- Subagent được dispatch tuyệt đối không được kế thừa toàn bộ lịch sử chat chính của phiên nếu không cần thiết.
- Phải xây dựng prompt cho subagent cực kỳ tập trung, self-contained và chỉ truyền các file thực sự liên quan trực tiếp đến nhiệm vụ của subagent đó.

---

## 3. CẤU TRÚC LẬP TRÌNH MỤC TIÊU (`dispatching-parallel-agents/SKILL.md`)

Tệp tin mới tại `.agent/skills/dispatching-parallel-agents/SKILL.md` sẽ có cấu trúc như sau:

```markdown
---
name: dispatching-parallel-agents
description: "Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies, with Token Budget Guard."
---

# Dispatching Parallel Agents (Vault Standard)

## Overview
[Nội dung gốc của Superpowers...]

## When to Use
[Nội dung gốc của Superpowers...]

## The Pattern
1. Identify Independent Domains
2. Create Focused Agent Tasks
3. Run Token Budget & Circuit Breaker Check [VAULT INTEGRATION]
4. Dispatch in Parallel / Sequential Fallback
5. Review and Integrate

## [NEW] Vault Adaptation: Token Budget & Circuit Breaker Guard

Trước khi gọi `invoke_subagent` song song, bạn BẮT BUỘC phải thực hiện các bước sau:

### Bước 1: Khảo sát ngân sách Token (Token Budget Audit)
- Ước lượng dung lượng token của phiên chính và các subagent định khởi chạy.
- Ngưỡng giới hạn Context Window của model hiện tại: [Khai báo model, ví dụ: Gemini 2.0 Flash = 1,000,000 tokens].

### Bước 2: Kích hoạt Ngắt mạch (Circuit Breaker)
- **Nếu Tổng dự toán < 70% Context Window:** Thực hiện dispatch song song.
- **Nếu Tổng dự toán từ 70% - 80% Context Window:** Phát cảnh báo và tối giản dung lượng file truyền vào subagent trước khi chạy.
- **Nếu Tổng dự toán > 80% Context Window:** **DỪNG LẠI**. Không chạy song song. Phải chạy tuần tự (Sequential) hoặc giải quyết đơn lẻ.

### Bước 3: Rà soát & Hợp nhất (Review & Integration)
- Khi các subagents trả về kết quả, tiến hành so sánh diff kỹ lưỡng, đảm bảo không có file nào bị chỉnh sửa trùng lặp chéo gây conflict.
- Chạy toàn bộ test suite để xác thực tích hợp an toàn.
```

---

## 4. KẾ HOẠCH XÁC THỰC (VERIFICATION PLAN)

### 4.1. Xác thực cấu trúc (Structural Verification)
Sau khi tạo file vật lý, chạy lệnh xác thực sự tồn tại và cú pháp của tệp tin:
```powershell
Test-Path .agent\skills\dispatching-parallel-agents\SKILL.md
```

### 4.2. Khớp Test Case (Test Matching)
- Việc chạy thử nghiệm của skill này sẽ được liên kết trực tiếp với kịch bản test case `T005_context_budget_trigger.md` trong `.agent/tests/skill-triggering/` để bảo đảm Agent tự động thực hiện tính toán token budget khi chạy tác vụ phức tạp.
