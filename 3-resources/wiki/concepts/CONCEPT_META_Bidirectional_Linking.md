---
file_id: CONCEPT_META_BIDIRECTIONAL_LINKING
title: "Bidirectional Linking (Liên kết hai chiều)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_NASHUS_LLMWIKI]]"
  - "[[SOURCE_META_LLM_WIKI]]"
---

## ## For future Claude
Trang này định nghĩa sức mạnh của Liên kết hai chiều (Bidirectional Linking) trong việc biến Wiki từ một tập hợp các tệp văn bản rời rạc thành một Đồ thị tri thức (Knowledge Graph) sống động. Liên kết hai chiều cho phép Agent và người dùng khám phá các mối liên hệ ẩn và bối cảnh liên quan một cách tự động và toàn diện.

## ## Key Claims / Summary
1.  **Context Discovery**: Giúp Agent tìm thấy các khái niệm liên quan thông qua Backlinks.
2.  **Graph Construction**: Tự động xây dựng đồ thị tri thức từ các tham chiếu thủ công.
3.  **Backlink Analysis**: Đánh giá tầm quan trọng của một node dựa trên số lượng liên kết trỏ đến nó.

## 1. Định nghĩa
Liên kết hai chiều là cơ chế trong đó nếu Trang A link đến Trang B, thì Trang B cũng tự động nhận biết và hiển thị liên kết ngược lại từ Trang A.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Khi viết về "Neural Networks", bạn liên kết đến [[CONCEPT_DSML_Master_ML_Algorithms]]. Ở trang thuật toán, Agent sẽ tự động thấy "Neural Networks" trong phần Backlinks, giúp kết nối khái niệm cụ thể vào bức tranh tổng quát. (Nguồn: [[SOURCE_META_LLM_WIKI]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc bạn kết bạn trên mạng xã hội. Khi bạn kết bạn với ai đó (Link), người đó cũng tự động trở thành bạn của bạn (Backlink). Cả hai bên đều biết về mối quan hệ này mà không cần phải thực hiện thao tác lần hai.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_LLM_WIKI]] — Section 2.4: The Power of Backlinks.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
