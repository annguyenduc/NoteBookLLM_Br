---
file_id: CONCEPT_META_CONSOLIDATION_TIERS
title: "Consolidation Tiers (Các tầng hợp nhất tri thức)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_LLM_WIKI_V2]]"
---

## ## For future Claude
Trang này mô tả mô hình Các tầng hợp nhất tri thức (Consolidation Tiers) - "bộ lọc" để tinh luyện thông tin từ các quan sát thô thành các nguyên lý vận hành cốt lõi. Việc phân cấp tri thức giúp hệ thống quản lý bộ nhớ hiệu quả và đảm bảo rằng chỉ những kiến thức đã được xác minh mới được đưa vào các tầng lưu trữ vĩnh viễn.

## ## Key Claims / Summary
1.  **Knowledge Pipeline**: Tri thức di chuyển từ Working Memory lên Semantic Memory.
2.  **Tier Definition**: Phân chia rõ ràng giữa quan sát (Episodic) và nguyên lý (Semantic).
3.  **Promotional Logic**: Thông tin chỉ được nâng tầng khi có đủ bằng chứng (Evidence) tích lũy.

## 1. Các tầng tri thức (Tiers)
1. **Working Memory**: Các quan sát gần đây (vừa nạp vào `00_Inbox`).
2. **Episodic Memory**: Tóm tắt các phiên làm việc (Queries/Logs).
3. **Semantic Memory**: Các sự thực được củng cố (Concepts/Entities).
4. **Procedural Memory**: Các quy trình thực thi (Workflows/Workrules).

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Một ghi chú thô về cách dùng hàm `map()` trong Python sẽ bắt đầu ở tầng Working, sau đó được củng cố thành một Concept về Python (Semantic), và cuối cùng trở thành một Skill thực thi tự động (Procedural). (Nguồn: [[SOURCE_META_LLM_WIKI_V2]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như quá trình học tập của một học sinh. Ban đầu chỉ là những ghi chép vụn vặt khi làm bài tập (Working), sau đó trở thành hiểu biết về bài học (Semantic), và cuối cùng trở thành kỹ năng giải toán thành thạo mà không cần suy nghĩ (Procedural).

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_LLM_WIKI_V2]] — Section: Consolidation Tiers and Memory Architecture.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
