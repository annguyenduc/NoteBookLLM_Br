---
file_id: CONCEPT_META_WIKI_ARTICLE_LENGTH_TARGETS
title: "Wiki Article Length Targets (Mục tiêu độ dài bài viết Wiki)"
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
Trang này định nghĩa các ngưỡng độ dài khuyến nghị cho từng loại bài viết trong Wiki. Việc duy trì độ dài hợp lý (không quá mỏng gây thiếu bối cảnh, không quá dài gây nhiễu thông tin) là yếu tố kỹ thuật giúp tối ưu hóa hiệu quả đọc của cả con người và khả năng xử lý của LLM Context Window.

## ## Key Claims / Summary
1.  **Context Density**: Độ dài phải tương xứng với độ phức tạp của khái niệm.
2.  **Type-specific Targets**: Áp dụng các ngưỡng khác nhau cho Person, Era, Philosophy, và Experiment.
3.  **Anti-cramming**: Ngăn chặn việc dồn nén quá nhiều thông tin không liên quan vào một trang duy nhất.

## 1. Các ngưỡng cốt lõi
- **Person**: 20-80 dòng (tùy vào tầm ảnh hưởng).
- **Philosophy / Pattern**: 40-80 dòng (cần độ sâu lý luận).
- **Experiment / Idea**: 25-45 dòng (tập trung vào kết quả).
- **Minimum**: 15 dòng (đảm bảo đủ bối cảnh tối thiểu).

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Nếu một bài viết về "Philosophy" dài hơn 100 dòng, hệ thống Cleanup sẽ gợi ý "Breakdown" (chia nhỏ) nó thành các tiểu chủ đề để tránh sự quá tải thông tin. (Nguồn: [[SOURCE_META_WIKI_GEN_CLONE]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như thiết kế các túi quà tặng. Túi quà cho trẻ em (Idea thô) chỉ cần nhỏ và gọn, nhưng túi quà cho người lớn (Philosophy/Triết lý) cần phải to và chứa đựng nhiều ý nghĩa hơn. Nếu túi quá nhỏ sẽ không đựng hết quà, còn túi quá to sẽ làm món quà bên trong bị lọt thỏm.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_WIKI_GEN_CLONE]] — Section: Length Targets and Granularity.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
