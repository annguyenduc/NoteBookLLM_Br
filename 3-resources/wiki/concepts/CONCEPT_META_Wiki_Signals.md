---
file_id: CONCEPT_META_WIKI_SIGNALS
title: "Wiki Signals (Mô hình Tín hiệu Wiki)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_NASHUS_LLMWIKI]]"
---

## ## For future Claude
Trang này định nghĩa Mô hình Tín hiệu Wiki (Wiki Signals) - hệ thống định vị bối cảnh cho Agent AI. Trong một biển tri thức khổng lồ, các "tín hiệu" (như liên kết, độ tươi của thông tin, hay vị trí trong đồ thị) giúp AI biết được đâu là thông tin quan trọng nhất, đáng tin cậy nhất để phục vụ cho việc suy luận và trả lời câu hỏi.

## ## Key Claims / Summary
1.  **Context Ranking**: Sử dụng các chỉ số để giúp LLM xác định độ ưu tiên của các đơn vị tri thức.
2.  **Hybrid Signals**: Kết hợp giữa liên kết thủ công (Direct) và độ tương đồng ý nghĩa (Semantic).
3.  **Graph Topology**: Tầm quan trọng của một Node tỷ lệ thuận với số lượng liên kết inbound/outbound.

## 1. Các loại tín hiệu chính
- **Direct Signals**: Các liên kết `[[target]]` do con người tạo ra.
- **Semantic Signals**: Độ tương đồng Vector giữa các bài viết.
- **Temporal Signals**: Thời gian cập nhật cuối (Độ tươi).
- **Topology Signals**: Chỉ số về vị trí và kết nối trong đồ thị tri thức.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Khi nạp trang "Transformer", hệ thống sử dụng Semantic Signals để tự động gợi ý liên kết đến "Attention Mechanism" ngay cả khi tài liệu thô không nhắc tới nhau trực tiếp. (Nguồn: [[SOURCE_META_NASHUS_LLMWIKI]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như các biển báo trên đường cao tốc. "Direct Signals" là các biển chỉ dẫn địa danh. "Semantic Signals" là các cửa hàng cùng loại nằm cạnh nhau. Tài xế (AI) dựa vào các tín hiệu này để đi đúng hướng mà không cần phải thuộc lòng toàn bộ bản đồ.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_NASHUS_LLMWIKI]] — Section: Signal Processing.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
