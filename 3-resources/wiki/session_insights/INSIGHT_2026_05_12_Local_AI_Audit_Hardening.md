---
id: INSIGHT_2026_05_12_Local_AI_Audit_Hardening
title: "Hardening Local AI Audit & gemma3:4b Integration"
date: 2026-05-12
agent: "@scout"
category: Infrastructure
status: COMPLETED
---

# Insight: Hardening Local AI Audit (Gap-Check)

## 1. Bối cảnh & Vấn đề
Trong quá trình nạp tài liệu *Thinking in Systems*, hệ thống Gap-Check (Local AI Audit) gặp một số lỗi vận hành:
- **Lỗi ghi đè:** Quên truyền `--chunk-num` khiến toàn bộ 16 chunks ghi đè vào `gap_001.md`.
- **Tràn ngữ cảnh:** Mặc định `num_ctx=2048` của Ollama không đủ chứa Prompt 6000 chars + Output 1024 tokens.
- **Định dạng không nhất quán:** Model tự ý thêm dấu `< >` hoặc giải thích thừa.

## 2. Giải pháp Kỹ thuật (Hardening)

### A. Scripting & Logic
- **Fix Surgical:** Cập nhật `gap_check.py` để xử lý chuỗi logic khắt khe hơn.
- **Batching:** Sử dụng vòng lặp PowerShell chuẩn hóa để trích xuất số thứ tự chunk từ tên file:
  `$num = [int]$matches[1]`
- **Context Expansion:** Nâng `num_ctx` lên **4096** trong Ollama API call để đảm bảo an toàn cho bộ nhớ đệm.

### B. Model Stack
- **Standardization:** Chốt dùng **`gemma3:4b`** cho tầng Audit. 
- **Performance:** Đạt tốc độ ~40-60s/chunk với chất lượng trích xuất sâu (Priority types: Concept, Method, Principle).

## 3. Cập nhật Governance (Rules R23-R26)
- **R23 (Manual Trigger):** @scout phải gọi thủ công sau mỗi chunk.
- **R24 (Non-blocking):** Lỗi AI local không được block pipeline chính.
- **R25 (Human Gate):** Chỉ Human mới được thăng cấp `gap_candidates/`.
- **R26 (Scope Isolation):** Chỉ dùng cho `DRAFT` atoms.

## 4. Operational Toolbox (New Commands)
Đã tích hợp vào `AGENTS.md` và `WORKSPACE_OVERVIEW.md`:
- `/gap-summary`: @librarian tổng hợp danh sách.
- `/gap-promote`: @engineer thăng cấp lên Atom nháp.
- `/gap-cleanup`: @auditor dọn dẹp inbox.

## 5. Kết luận
Hệ thống hiện đã sở hữu tầng "Phản biện tri thức" (Second Opinion) ổn định, chạy được trên phần cứng dân dụng (4GB VRAM) mà vẫn đảm bảo độ phủ kiến thức đạt chuẩn Wiki 2.0.

---
*Lưu ý: Tiếp tục theo dõi độ ổn định của gemma3:4b khi xử lý các chunks > 8000 chars.*
