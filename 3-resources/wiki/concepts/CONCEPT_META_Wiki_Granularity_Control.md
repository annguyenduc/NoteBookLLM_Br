---
file_id: CONCEPT_META_WIKI_GRANULARITY_CONTROL
title: "Wiki Granularity Control (Kiểm soát độ hạt tri thức)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_WIKI_GEN_CLONE]]"
---

## ## For future Claude
Trang này định nghĩa cơ chế Kiểm soát độ hạt (Granularity Control) - nghệ thuật chia nhỏ tri thức. Trong một hệ thống Wiki nguyên tử, việc giữ cho các bài viết không quá đồ sộ (Anti-Cramming) nhưng cũng không quá sơ sài (Anti-Thinning) là yếu tố sống còn để Agent AI có thể truy xuất và suy luận chính xác trên từng đơn vị tri thức hạt nhân.

## ## Key Claims / Summary
1.  **Anti-Cramming**: Ngăn chặn việc nhồi nhét quá nhiều chủ đề vào một trang; nếu một chủ đề phụ đủ lớn, nó phải có trang riêng.
2.  **Anti-Thinning**: Tránh tạo các trang "Stub" vô nghĩa; một Atom phải mang đủ bối cảnh tối thiểu để có giá trị.
3.  **The Concrete Noun Test**: Sử dụng danh từ cụ thể để xác định ranh giới của một đơn vị tri thức mới.

## 1. Các quy tắc "Vàng"
- **Ngưỡng chia tách**: Một bài viết vượt quá 120-150 dòng cần được xem xét chia nhỏ.
- **Quy tắc đoạn văn thứ 3**: Nếu bạn viết đến đoạn thứ 3 về một chủ đề phụ, hãy tách nó ra.
- **Tối thiểu bối cảnh**: Một trang mới phải có ít nhất 3 câu có ý nghĩa thay vì chỉ là một mẩu tin rời rạc.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Việc nhồi nhét mọi thứ về "Claude Code" vào một trang duy nhất sẽ làm mất đi bối cảnh chuyên sâu của "CLAUDE.md" hay "MCP Servers". Theo quy tắc độ hạt, mỗi thành phần này cần một trang riêng để tối ưu hóa việc truy vấn. (Nguồn: [[SOURCE_META_WIKI_GEN_CLONE]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc đóng gói thực phẩm. Nếu gói quá to (Cramming), bạn khó có thể lấy đúng thứ mình cần. Nếu gói quá nhỏ (Thinning) như chỉ chứa một hạt muối, việc đóng gói trở nên lãng phí và gây nhiễu cho kho chứa.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_WIKI_GEN_CLONE]] — Section: Anti-Cramming & Anti-Thinning / Granularity.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
