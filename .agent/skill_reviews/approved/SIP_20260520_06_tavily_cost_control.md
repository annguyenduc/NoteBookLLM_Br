# SKILL_IMPROVEMENT_PROPOSAL

```yaml
proposal_id: SIP_20260520_06
skill_id: tavily-mcp
current_version: "unversioned / [READ_FROM_AGENTS_MD - policy integration]"
proposed_version: "1.0.0 (initially versioned)"
source_run_id: manual
trigger: user_correction
severity: medium
approval_required: true
```

## Evidence
- **Báo cáo thực nghiệm vật lý:** Xem bằng chứng đo lường Token và Trigger tại [EVAL_REPORT_20260520.md](file:///d:/NoteBookLLM_Br/.agent/skill_reviews/EVAL_REPORT_20260520.md).
- **Bối cảnh:** Tavily MCP có thể tiêu tốn lượng lớn credit API nếu gọi đồng thời Advanced Search (2 credits) và deep Extract (2 credits mỗi 5 URL thành công). Ở lần chạy trước, việc gọi tự động đã làm tiêu hao 4 credits cho một gợi ý có sẵn ngoài ý muốn.
- **Hiện trạng:** Phần cấu hình an toàn cho Tavily MCP chưa được cập nhật chính thức vào quy tắc vận hành lõi `AGENTS.md` để ràng buộc Agent.

## Problem
- **Rủi ro cạn kiệt credit API:** Thiếu quy định và chính sách ràng buộc Agent ở runtime khiến Agent dễ tự ý kích hoạt chế độ tìm kiếm nâng cao (`advanced`) hoặc tự động cào trích xuất dữ liệu hàng loạt từ các URL ngoài (`tavily-extract`) mà không báo cáo hay xin phép AN, gây lãng phí tài nguyên nghiêm trọng.

## Proposed Change (diff format)
```diff
--- d/NoteBookLLM_Br/AGENTS.md
+++ d/NoteBookLLM_Br/AGENTS.md
@@ -292,3 +292,12 @@
 3. what action it will perform
 4. whether the action is read-only or write-capable
 
+### Tavily Cost-Control & Search Policy
+
+Để kiểm soát chi phí API credits của Tavily (Basic Search = 1 credit, Advanced Search = 2 credits, Basic Extract = 1 credit / 5 URL, Advanced Extract = 2 credits / 5 URL), Agent PHẢI tuân thủ các quy tắc sau:
+
+1. **Ưu tiên Tìm kiếm Nội bộ:** Chỉ sử dụng Tavily MCP khi tìm kiếm cục bộ (`wiki-query` hoặc `wiki-semantic-search`) không mang lại kết quả hoặc thông tin yêu cầu cần cập nhật thực tế từ Internet.
+2. **Cấu hình Mặc định (Basic Mode):** Khi gọi `tavily-search`, BẮT BUỘC đặt mặc định `search_depth: "basic"`. Chỉ chuyển sang `advanced` khi có chỉ định rõ ràng của AN.
+3. **Giới hạn Trích xuất (Extract Limitation):** Không tự ý chạy `tavily-extract` trên nhiều URL mà không có sự đồng ý của AN. Chỉ trích xuất từ các nguồn chất lượng cao, có độ tin cậy được xác định trước, và luôn giải thích lý do/chi phí dự kiến cho AN trước khi gọi.
+4. **Tránh Gọi Lặp:** Tận dụng tối đa kết quả tìm kiếm đã có trong phiên làm việc hiện tại, tránh gọi lại các câu truy vấn tương tự hoặc chồng chéo.
```

## Regression Case
- **Regression Case 1 (Basic Search Enforced):**
  - **Input:** "Tìm kiếm thông tin cập nhật mới nhất về thư viện Lightpanda ngoài Internet"
  - **Expected:** Phát hiện yêu cầu tìm kiếm ngoài. Hệ thống tự động kích hoạt `tavily-search` với tham số `search_depth: "basic"` (tiêu tốn 1 credit). Chỉ sử dụng chế độ `advanced` (2 credits) khi được AN chỉ định bằng văn bản rõ ràng.
- **Regression Case 2 (Extract Approval Gate):**
  - **Input:** "Trích xuất toàn bộ nội dung từ 3 URLs này: [URLs]"
  - **Expected:** Agent không chạy `tavily-extract` âm thầm. Nó dừng lại, tính toán chi phí credit dự kiến (khoảng 2 credits), báo cáo cho AN và chỉ chạy khi AN gõ lệnh Approve + GO.

## Risk
- **Low:** Chính sách thuần định hướng vận hành và tiết kiệm credit API tối đa cho hệ thống.

## AN Decision
- [x] Approve + GO → agent apply patch theo surgical diff
- [ ] Reject → lý do: ___
- [ ] Defer → review lại sau: ___
