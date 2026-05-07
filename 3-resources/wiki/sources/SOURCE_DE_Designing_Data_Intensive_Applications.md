---
file_id: "SOURCE_DE_DESIGNING_DATA_INTENSIVE_APPLICATIONS"
SOURCE_ID: SOURCE_DE_DESIGNING_DATA_INTENSIVE_APPLICATIONS
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

## ðŸ“ 1. PhÃ¢n tÃ­ch Ingest (Analysis - Step 1)
- **Thá»±c thá»ƒ & KhÃ¡i niá»‡m then chá»‘t:** Data Models, Storage & Retrieval, Encoding, Replication, Partitioning, Transactions, Distributed Systems, Batch/Stream Processing.
- **Káº¿t ná»‘i Wiki:** Cung cáº¥p tÆ° duy há»‡ thá»‘ng nÃ¢ng cao cho nhÃ³m [[CONCEPT_index]]. LÃ  ná»n táº£ng cho [[CONCEPT_DE_Data_Architecture_Basics]] vÃ  [[CONCEPT_DE_Indexing_Optimization]].
- **Äiá»ƒm khÃ¡c biá»‡t/MÃ¢u thuáº«n:** PhÃ¡ vá»¡ Ä‘á»‹nh kiáº¿n "Database lÃ  má»™t há»™p Ä‘en". PhÃ¢n tÃ­ch sÃ¢u vá» Ä‘á»‹nh lÃ½ CAP vÃ  cÃ¡c sá»± Ä‘Ã¡nh Ä‘á»•i giá»¯a tÃ­nh nháº¥t quÃ¡n (Consistency) vÃ  tÃ­nh sáºµn sÃ ng (Availability).
- **Äá» xuáº¥t cáº¥u trÃºc:** Táº¡o trang [[CONCEPT_DE_Batch_vs_Stream_Processing]] Ä‘á»ƒ DA biáº¿t khi nÃ o nÃªn phÃ¢n tÃ­ch dá»¯ liá»‡u theo máº» (Batch) vÃ  khi nÃ o cáº§n xá»­ lÃ½ thá»i gian thá»±c (Stream).

## ðŸ“– 2. Tá»•ng quan nguá»“n (Overview - Step 2)
ÄÆ°á»£c coi lÃ  cuá»‘n sÃ¡ch quan trá»ng nháº¥t trong tháº­p ká»· qua vá» ká»¹ thuáº­t dá»¯ liá»‡u. DDIA giÃºp cÃ¡c ká»¹ sÆ° vÃ  nhÃ  phÃ¢n tÃ­ch hiá»ƒu rÃµ cÃ¡c nguyÃªn lÃ½ cá»‘t lÃµi Ä‘áº±ng sau cÃ¡c cÃ´ng nghá»‡ dá»¯ liá»‡u hiá»‡n Ä‘áº¡i, tá»« [[ENTITY_SQL|SQL]]/NoSQL Ä‘áº¿n cÃ¡c há»‡ thá»‘ng xá»­ lÃ½ phÃ¢n tÃ¡n, giÃºp há» xÃ¢y dá»±ng Ä‘Æ°á»£c nhá»¯ng á»©ng dá»¥ng bá»n vá»¯ng vÃ  cÃ³ kháº£ nÄƒng má»Ÿ rá»™ng cá»±c cao.

## ðŸš€ 3. CÃ¡c Concept Ä‘Ã£ trÃ­ch xuáº¥t (Rule 14 & 17)
- [[CONCEPT_DE_Data_Architecture_Basics]] | **CÆ¡ sá»Ÿ kiáº¿n trÃºc dá»¯ liá»‡u** - Hiá»ƒu vá» cÃ¡ch cÃ¡c há»‡ thá»‘ng káº¿t ná»‘i vá»›i nhau.
- [[CONCEPT_DE_Indexing_Optimization]] | **Tá»‘i Æ°u hÃ³a Index** - Báº£n cháº¥t cá»§a B-Trees vÃ  LSM-Trees.
- [[CONCEPT_DE_Data_Quality_Framework]] | **Khung cháº¥t lÆ°á»£ng dá»¯ liá»‡u** - Äáº£m báº£o tÃ­nh tin cáº­y cá»§a há»‡ thá»‘ng.

## ðŸ” 4. Review Items (DÃ nh cho Human)
- [ ] ÄÃ¡nh giÃ¡ xem kiáº¿n trÃºc dá»¯ liá»‡u hiá»‡n táº¡i cÃ³ Ä‘ang gáº·p pháº£i cÃ¡c váº¥n Ä‘á» vá» Scalability khi sá»‘ lÆ°á»£ng há»c viÃªn tÄƒng Ä‘á»™t biáº¿n khÃ´ng.
- [ ] TÃ¬m hiá»ƒu vá» cÆ¡ cháº¿ "Replication" cá»§a database production Ä‘á»ƒ biáº¿t Ä‘á»™ trá»… cá»§a dá»¯ liá»‡u khi Ä‘á»• vá» Warehouse.

--- 
**Nguá»“n thÃ´:** `DE_Designing_Data_Intensive_Applications`
**Deep Research Query:** `Martin Kleppmann DDIA summary for data engineers and analysts`

## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
