---
file_id: "WIKI_CONCEPT_AI_MEMORY_MANAGEMENT_STRATEGIES"
title: "Chiến lược quản lý bộ nhớ Agent (Agent Memory Management Strategies)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["AI", "Memory", "Context Window", "Checkpointing"]
source: "RAW_PDF_Agentic_AI_Roadmap"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
agent_id: "@engineer"
---

# Chiến lược quản lý bộ nhớ Agent (Agent Memory Management Strategies)

Quản lý bộ nhớ là khả năng lưu trữ, truy xuất và nén thông tin để Agent duy trì ngữ cảnh trong thời gian dài.

## Core Principle
Hệ thống bộ nhớ Agent được chia làm hai loại chính dựa trên thời gian tồn tại và khả năng truy cập:
1. **Short-term Memory (Bộ nhớ ngắn hạn):** Nằm trực tiếp trong Context Window. Bao gồm lịch sử hội thoại gần nhất và trạng thái tác vụ hiện tại. Rất nhanh nhưng bị giới hạn dung lượng.
2. **Long-term Memory (Bộ nhớ dài hạn):** Lưu trữ bên ngoài (Vector DB, SQL, Files). Dùng cho tri thức lớn hoặc hồ sơ người dùng. Cần cơ chế **Retrieval (Truy xuất)** hiệu quả.

**Cơ chế Checkpointing:** Lưu lại trạng thái của luồng công việc tại các điểm quan trọng để có thể phục hồi (resume) sau khi gặp lỗi hoặc chờ con người phê duyệt.

## Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ tài liệu (Original)
Khi Context Window bị đầy, chúng ta áp dụng **Context Budgeting**: Ví dụ, giới hạn 30% cho tài liệu truy xuất, 20% cho tóm tắt bộ nhớ. Khi vượt quá, hệ thống sẽ tự động tóm tắt (summarize) hoặc loại bỏ các nội dung ít giá trị để nhường chỗ cho các chỉ dẫn cốt lõi.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Hãy tưởng tượng một học sinh đang ôn thi:
- **Bộ nhớ ngắn hạn:** Là những gì học sinh đang nhẩm trong đầu khi làm bài thi.
- **Bộ nhớ dài hạn:** Là các cuốn sách giáo khoa và vở ghi chép trên giá sách.
- **Context Budgeting:** Học sinh chỉ có một tờ giấy nháp nhỏ. Thay vì chép toàn bộ đề bài vào nháp, học sinh chỉ ghi lại các công thức quan trọng nhất và các kết quả trung gian để tiết kiệm không gian nháp.

## Liên kết tư duy
- [[CONCEPT_AI_Agentic_Workflow_Patterns]]
- [[CONCEPT_AI_Context_Window_Management]]

## 4F Reflection
- **Facts:** Tóm tắt (Summaries) tốt cho việc nhớ "chuyện gì đã xảy ra", còn Embeddings tốt cho việc "tìm kiếm tri thức chi tiết".
- **Feelings:** Việc Agent có thể nhớ được sở thích của người dùng từ các phiên làm việc trước tạo ra trải nghiệm cá nhân hóa sâu sắc.
- **Findings:** Checkpointing không chỉ để sửa lỗi mà còn là một công cụ audit quan trọng để hiểu tại sao Agent đưa ra quyết định đó.
- **Futures:** Quản lý bộ nhớ sẽ chuyển dịch sang mô hình "Lên kế hoạch bộ nhớ" (Memory Planning), nơi Agent tự quyết định thông tin nào đáng để ghi nhớ vĩnh viễn.

---
Nguồn: [[RAW_PDF_Agentic_AI_Roadmap]] (Section 6: Memory Management)
Xác nhận Rule 14 từ MarkItDown Conversion (2026-05-03).
