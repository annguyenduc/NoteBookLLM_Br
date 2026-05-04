---
source_id: SOURCE_META_NASHUS_LLMWIKI
title: "WEB: Nashus [[CONCEPT_META_SB3_Graph_Analysis|LLM Wiki Methodology]] (System Guide)"
author: "Nashsu"
category: "WEB"
domain: "Knowledge Engineering"
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-03"
---

relationships:
  - type: "relates_to"
    target: "[[CONCEPT_META_SB3_Graph_Traversal]]"
  - type: "relates_to"
    target: "[[CONCEPT_META_SB3_Louvain_Clustering]]"

# WEB Nashus [[CONCEPT_META_SB3_Graph_Analysis|LLM Wiki Methodology]]

## 📝 1. Phân tích Ingest (Analysis - Step 1)
- **Thực thể & Khái niệm then chốt:** [[CONCEPT_META_SB3_Graph_Traversal|4-Signal Relevance Model]], [[CONCEPT_META_SB3_Louvain_Clustering|Louvain Community Detection]], Graph Insights (Knowledge Gaps), Async Review, Multi-format Document Support.
- **Kết nối Wiki:** Mở rộng mô hình Karpathy bằng các thuật toán đồ thị thực tế để tăng cường khả năng tự chữa lành (Self-healing).
- **Điểm khác biệt/Mâu thuẫn:** Nhấn mạnh vào việc sử dụng Graph Topology để phát hiện lỗ hổng tri thức (Gaps) và các kết nối bất ngờ (Surprising Connections).
- **Đề xuất cấu trúc:** Triển khai các concept về Graph Analysis cấp độ chuyên sâu (SB3).

## 📖 2. Tổng quan nguồn (Overview - Step 2)
Tài liệu trình bày các phương pháp hiện thực hóa mô hình Karpathy trên nền tảng Desktop. Trọng tâm là mô hình **Đồ thị tri thức 4 tín hiệu** và thuật toán **Louvain** để tự động phân cụm tri thức, giúp vượt qua giới hạn của phân cấp thư mục truyền thống.

### Mô hình Đồ thị 4 Tín hiệu (Nashus Model)
| Tín hiệu | Trọng số | Mô tả |
| :--- | :--- | :--- |
| **Direct link** | ×3.0 | Liên kết trực tiếp qua `[[wikilinks]]` |
| **Source overlap** | ×4.0 | Cùng chia sẻ nguồn raw thô |
| **Adamic-Adar** | ×1.5 | Chia sẻ các node lân cận chung |
| **Type affinity** | ×1.0 | Cùng loại (entity-entity, concept-concept) |

## 🚀 3. Các Concept đã trích xuất (Rule 14 & 17)
- [[CONCEPT_META_SB3_Graph_Traversal]] | **Graph Relevance** - Mô hình 4 tín hiệu đánh giá độ liên quan tri thức.
- [[CONCEPT_META_SB3_Louvain_Clustering]] | **Louvain Clustering** - Phân tích Topology để phát hiện Communities và Gaps.
- [[CONCEPT_META_Async_Review_System]] | **Async Review** - Hệ thống gắn cờ mâu thuẫn tri thức chờ người duyệt.

## 🔍 4. Review Items (Dành cho Human)
- [ ] Tích hợp Louvain Cohesion Score (< 0.15) vào dashboard báo cáo sức khỏe Wiki.
- [ ] Thử nghiệm mô hình Deep Research tự động dựa trên Graph Insights.

--- 
**Nguồn thô:** `AIMET_nashus_llmwiki.md`
**Deep Research Query:** `Nashsu LLM Wiki graph topology community detection Louvain weights`



## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
