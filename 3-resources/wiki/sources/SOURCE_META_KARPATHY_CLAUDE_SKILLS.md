---
source_id: SOURCE_META_KARPATHY_CLAUDE_SKILLS
title: "WEB: Karpathy's Claude Skills Guide"
author: "Andrej Karpathy"
category: "WEB"
domain: "AI Engineering / Skills Architecture"
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-01"
---

relationships:
  - type: "relates_to"
    target: "[[CONCEPT_META_Skill_Modularity]]"
# WEB Karpathy's Claude Skills Guide

## 📝 1. Phân tích Ingest (Analysis - Step 1)
- **Thực thể & Khái niệm then chốt:** Skill Folders, CLAUDE.md, scripts/resources separation, Standardized Interface.
- **Kết nối Wiki:** Định hình cấu trúc cho thư mục `.agent/skills/` hiện tại của NoteBookLLM_Br.
- **Điểm khác biệt/Mâu thuẫn:** Ưu tiên tính module hóa tuyệt đối của công cụ thay vì nhồi nhét logic vào system prompt.
- **Đề xuất cấu trúc:** Tạo trang Concept về [[CONCEPT_META_Skill_Modularity|Skill Modularity]].

## 📖 2. Tổng quan nguồn (Overview - Step 2)
Hướng dẫn của Karpathy về việc đóng gói các khả năng của Agent thành các Skill độc lập, giúp hệ thống dễ bảo trì, mở rộng và giảm tải cửa sổ ngữ cảnh.

## 🚀 3. Các Concept đã trích xuất (Rule 14 & 17)
- [[CONCEPT_META_Skill_Modularity]] | **[[CONCEPT_META_Skill_Modularity|Skill Modularity]]** - Nguyên tắc đóng gói khả năng Agent thành module.

## 🔍 4. Review Items (Dành cho Human)
- [ ] User rà soát xem các Skill folder hiện tại (.agent/skills/) đã có đủ 3 thành phần (scripts, resources, SKILL.md) chưa.

--- 
**Nguồn thô:** `AIMET_Karpathys_CLAUDE_Skills_Guide.md`
**Deep Research Query:** `Andrej Karpathy Claude Skills architecture pattern`


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
