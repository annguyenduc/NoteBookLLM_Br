# Session Insight: Wiki 2.0 Governance & System Thinking
**Ngày**: 2026-05-14 | **Agent**: @pm, @engineer, @scout
**Chủ đề**: Tổng kết hạ tầng kỹ thuật, Quản trị hệ thống bằng kiến trúc và Triết lý Ingest Karpathy-centric.

## 1. Những gì đã hoàn thành

### Hardware & Model Stack (GTX 1650 Optimized)
- **Gap-Check Engine**: Chuyển đổi sang `gemma3:4b` để giải quyết triệt để lỗi RAM leak.
- **Semantic Search**: Thay thế `nomic-embed-text` bằng giải pháp local tích hợp trong `qmd`, giảm tải VRAM.
- **Ollama Stable Stack**: `gemma3:4b` (Audit) | `phi3:mini` (Quick tasks) | `llama3.2:3b` (General) | `qwen3:4b` (Backup).

### Pipeline Hardening (Fail-Closed Architecture)
- **gap_check.py**: Cấu trúc lại với `audit_stamp`, tích hợp hàng đợi lỗi DLQ (`failed_queue`), mở rộng `num_ctx=4096`.
- **synthesis_guard.py**: Xóa bỏ cờ `--force`, thực thi quét toàn bộ Wiki, tự động phục hồi (auto-revert) các trạng thái `SYNTHESIZED` trái phép.
- **promote.py**: Gia cố Gate 3 với cơ chế xác thực HMAC Signature (Fail-Hard).

### Architecture v2.0 Sprint
- **Rule Optimization**: Cắt giảm 56% token trong `GEMINI.md` bằng cách phân tán luật vào các Agent-scoped files.
- **VRAM Guard**: Triển khai `vram_guard.py` với atomic lock (`.kiro/vram.lock`) để ngăn chặn race condition giữa các agent.
- **DLQ System**: Chuyển đổi lỗi âm thầm (Silent failures) thành các explicit tickets trong `failed_queue/` có thể truy vết và retry.

## 2. Insights quan trọng về tư duy hệ thống

1. **Naming là Governance**: Tên hàm và docstring không chỉ là code, chúng là Instructions. Agent suy luận quyền hạn dựa trên ngôn ngữ (ví dụ: `approve` implies human-level authority).
2. **Architectural Enforcement > Prompt Enforcement**: Code-based gate (TTY, HMAC, Auto-revert) là tuyệt đối và không thể bị bypass bằng reasoning như prompt-based rules.
3. **Silent Failure là kẻ thù**: Mọi lỗi (kể cả offline model) phải được vật lý hóa thành file trong DLQ để đảm bảo tính toàn vẹn của Knowledge Graph.
4. **Global Context trong Ingest**: Khắc phục tính cục bộ của Chunking bằng cơ chế Pass 1 (Global Scan) để inject cấu trúc tổng thể vào từng chunk xử lý sau đó.
5. **Retrieval Quality > Model Quality**: Wiki 2.0 là hệ thống lấy Retrieval làm trung tâm. Chất lượng Embedding và Semantic Search quan trọng hơn kích thước Chat Model.

## 3. Pending cho session tiếp theo

- [ ] **Update SPEC_NoteBookLLM_Br.md**: Phản ánh đầy đủ kiến trúc v2.0 và quy trình HMAC.
- [ ] **Setup GitHub & SQLite MCP**: Cấu hình `mcp_config.json` để mở rộng khả năng truy vấn.
- [ ] **Ingest Campaign**: Thực thi chiến dịch nạp tri thức *Thinking in Systems* và các nguồn ARCH tiếp theo.
- [ ] **Wiki Health Audit**: Sử dụng `wiki-status` để đánh giá mật độ liên kết (Link Density) hiện tại.
- [ ] **Output Layer Planning**: Thiết kế lớp xuất bản dữ liệu sau khi đạt đủ độ phủ (Coverage) của PKB.

---
*Verified by Antigravity Governance Engine.*
