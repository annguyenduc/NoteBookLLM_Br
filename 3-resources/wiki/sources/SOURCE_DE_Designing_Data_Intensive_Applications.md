---
source_id: SOURCE_DE_Designing_Data_Intensive_Applications
title: "ACAD Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems"
author: "Martin Kleppmann"
category: ACAD
domain: "Data Engineering / Distributed Systems"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

relationships:
  - type: "relates_to"
    target: "[[ENTITY_SQL]]"
# ACAD Designing Data-Intensive Applications

## 📝 1. Phân tích Ingest (Analysis - Step 1)
- **Thực thể & Khái niệm then chốt:** Data Models, Storage & Retrieval, Encoding, Replication, Partitioning, Transactions, Distributed Systems, Batch/Stream Processing.
- **Kết nối Wiki:** Cung cấp tư duy hệ thống nâng cao cho nhóm [[index]]. Là nền tảng cho [[CONCEPT_DE_Data_Architecture_Basics]] và [[CONCEPT_DE_Indexing_Optimization]].
- **Điểm khác biệt/Mâu thuẫn:** Phá vỡ định kiến "Database là một hộp đen". Phân tích sâu về định lý CAP và các sự đánh đổi giữa tính nhất quán (Consistency) và tính sẵn sàng (Availability).
- **Đề xuất cấu trúc:** Tạo trang [[CONCEPT_DE_Batch_vs_Stream_Processing]] để DA biết khi nào nên phân tích dữ liệu theo mẻ (Batch) và khi nào cần xử lý thời gian thực (Stream).

## 📖 2. Tổng quan nguồn (Overview - Step 2)
Được coi là cuốn sách quan trọng nhất trong thập kỷ qua về kỹ thuật dữ liệu. DDIA giúp các kỹ sư và nhà phân tích hiểu rõ các nguyên lý cốt lõi đằng sau các công nghệ dữ liệu hiện đại, từ [[ENTITY_SQL|SQL]]/NoSQL đến các hệ thống xử lý phân tán, giúp họ xây dựng được những ứng dụng bền vững và có khả năng mở rộng cực cao.

## 🚀 3. Các Concept đã trích xuất (Rule 14 & 17)
- [[CONCEPT_DE_Data_Architecture_Basics]] | **Cơ sở kiến trúc dữ liệu** - Hiểu về cách các hệ thống kết nối với nhau.
- [[CONCEPT_DE_Indexing_Optimization]] | **Tối ưu hóa Index** - Bản chất của B-Trees và LSM-Trees.
- [[CONCEPT_DE_Data_Quality_Framework]] | **Khung chất lượng dữ liệu** - Đảm bảo tính tin cậy của hệ thống.

## 🔍 4. Review Items (Dành cho Human)
- [ ] Đánh giá xem kiến trúc dữ liệu hiện tại có đang gặp phải các vấn đề về Scalability khi số lượng học viên tăng đột biến không.
- [ ] Tìm hiểu về cơ chế "Replication" của database production để biết độ trễ của dữ liệu khi đổ về Warehouse.

--- 
**Nguồn thô:** `DE_Designing_Data_Intensive_Applications`
**Deep Research Query:** `Martin Kleppmann DDIA summary for data engineers and analysts`

## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
