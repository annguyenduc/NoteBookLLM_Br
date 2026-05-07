---
file_id: "SOURCE_META_WIKI_GEN_CLONE"
SOURCE_ID: SOURCE_META_WIKI_GEN_CLONE
title: "WEB: Wiki Generation & Personal Knowledge Master Protocol"
author: "Community / Claude Code Users"
category: "WEB"
domain: "Knowledge Management / AI Engineering"
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-02"
last_accessed: "2026-05-02"
relationships:
  - type: "supports"
    target: "[[CONCEPT_META_Wiki_Absorption_Loop]]"
  - type: "supports"
    target: "[[CONCEPT_META_Wiki_Granularity_Control]]"
  - type: "supports"
    target: "[[CONCEPT_META_Wiki_Writing_Tone]]"
---

# WEB Wiki Generation & Personal Knowledge Master Protocol

## ðŸ“ 1. PhÃ¢n tÃ­ch Ingest (Analysis - Step 1)
*Pháº§n nÃ y ghi láº¡i káº¿t quáº£ phÃ¢n tÃ­ch cáº¥u trÃºc trÆ°á»›c khi táº¡o cÃ¡c trang Concept.*

- **Thá»±c thá»ƒ & KhÃ¡i niá»‡m then chá»‘t:** Writer vs Filing Clerk, Absorption Loop, Anti-Cramming, Concrete Noun Test, Wikipedia Tone.
- **Káº¿t ná»‘i Wiki:** ÄÃ¢y lÃ  ná»n táº£ng ká»¹ thuáº­t cho toÃ n bá»™ há»‡ thá»‘ng NoteBookLLM_Br, cung cáº¥p cÃ¡c lá»‡nh `absorb`, `cleanup`, `query`, `breakdown`, `rebuild-index`, vÃ  `status`.
- **Äiá»ƒm khÃ¡c biá»‡t/MÃ¢u thuáº«n:** Nháº¥n máº¡nh viá»‡c AI pháº£i Ä‘Ã³ng vai trÃ² "NgÆ°á»i viáº¿t lÃ¡ch" (Writer) Ä‘á»ƒ tá»•ng há»£p Ã½ nghÄ©a, thay vÃ¬ chá»‰ "ThÆ° kÃ½" (Filing Clerk) Ä‘á»ƒ lÆ°u trá»¯ sá»± tháº­t.
- **Äá» xuáº¥t cáº¥u trÃºc:** Chia nhá» thÃ nh cÃ¡c Concept vá»: Giao thá»©c háº¥p thá»¥, Kiá»ƒm soÃ¡t Ä‘á»™ háº¡t, Há»‡ thá»‘ng phÃ¢n loáº¡i (Taxonomy) vÃ  TiÃªu chuáº©n viáº¿t lÃ¡ch.

## ðŸ“– 2. Tá»•ng quan nguá»“n (Overview - Step 2)
TÃ i liá»‡u Ä‘á»‹nh nghÄ©a má»™t bá»™ Skill hoÃ n chá»‰nh cho Claude Code Ä‘á»ƒ xÃ¢y dá»±ng "Báº£n Ä‘á»“ tÃ¢m trÃ­" (Map of a mind). Trá»ng tÃ¢m khÃ´ng náº±m á»Ÿ viá»‡c lÆ°u trá»¯ mÃ  á»Ÿ viá»‡c **háº¥p thá»¥ tri thá»©c** â€” hiá»ƒu rÃµ Ã½ nghÄ©a vÃ  sá»± káº¿t ná»‘i cá»§a tá»«ng máº©u thÃ´ng tin Ä‘á»‘i vá»›i cuá»™c Ä‘á»i cá»§a chá»§ thá»ƒ.

## ðŸš€ 3. CÃ¡c Concept Ä‘Ã£ trÃ­ch xuáº¥t (Rule 14 & 17)
- [[CONCEPT_META_Wiki_Absorption_Loop]] | **[[CONCEPT_META_Wiki_Absorption_Loop|Wiki Absorption Loop]]** - Giao thá»©c 5 bÆ°á»›c Ä‘á»ƒ biáº¿n entry thÃ´ thÃ nh bÃ i viáº¿t tá»•ng há»£p.
- [[CONCEPT_META_Wiki_Granularity_Control]] | **[[CONCEPT_META_Wiki_Granularity_Control|Granularity Control]]** - Quy táº¯c Anti-Cramming (chá»‘ng nhá»“i nhÃ©t) vÃ  Anti-Thinning (chá»‘ng há»i há»£t).
- [[CONCEPT_META_Wiki_Writing_Tone]] | **[[CONCEPT_META_Wiki_Writing_Tone|Wiki Writing Tone]]** - TiÃªu chuáº©n viáº¿t kiá»ƒu Wikipedia: khÃ¡ch quan, sÃºc tÃ­ch, khÃ´ng dÃ¹ng má»¹ tá»«.
- [[CONCEPT_META_Wiki_Directory_Taxonomy]] | **[[CONCEPT_META_Wiki_Directory_Taxonomy|Wiki Directory Taxonomy]]** - Há»‡ thá»‘ng 30+ thÆ° má»¥c phÃ¢n loáº¡i tri thá»©c tá»« Ä‘á»i sá»‘ng Ä‘áº¿n tÆ° duy.
- [[CONCEPT_META_Wiki_Breakdown_Mining]] | **[[CONCEPT_META_Wiki_Breakdown_Mining|Wiki Breakdown & Mining]]** - Ká»¹ thuáº­t dÃ¹ng "Concrete Noun Test" Ä‘á»ƒ phÃ¡t hiá»‡n lá»— há»•ng tri thá»©c.
- [[CONCEPT_META_Wiki_Cleanup_Audit]] | **[[CONCEPT_META_Wiki_Cleanup_Audit|Wiki Cleanup Audit]]** - Chu trÃ¬nh audit vÃ  enrich toÃ n wiki sau ingest Ä‘á»ƒ sá»­a cáº¥u trÃºc, tone vÃ  liÃªn káº¿t.
- [[CONCEPT_META_Wiki_Index_Synchronization]] | **[[CONCEPT_META_Wiki_Index_Synchronization|Wiki Index Synchronization]]** - CÆ¡ cháº¿ Ä‘á»“ng bá»™ index vÃ  backlinks Ä‘á»ƒ query, cleanup vÃ  reorganize hoáº¡t Ä‘á»™ng trÃªn cÃ¹ng má»™t graph.
- [[CONCEPT_META_Wiki_Status_Metrics]] | **[[CONCEPT_META_Wiki_Status_Metrics|Wiki Status Metrics]]** - Bá»™ chá»‰ sá»‘ Ä‘á»c sá»©c khá»e váº­n hÃ nh cá»§a wiki sá»‘ng.
- [[CONCEPT_META_Wiki_Reorganization]] | **[[CONCEPT_META_Wiki_Reorganization|Wiki Reorganization]]** - TÆ° duy tÃ¡i cáº¥u trÃºc wiki á»Ÿ cáº¥p kiáº¿n trÃºc: merge, split, reclassify vÃ  rebuild.
- [[CONCEPT_META_Wiki_Quote_Discipline]] | **[[CONCEPT_META_Wiki_Quote_Discipline|Wiki Quote Discipline]]** - Quy táº¯c giá»¯ article voice trung tÃ­nh báº±ng cÃ¡ch kiá»ƒm soÃ¡t sá»‘ lÆ°á»£ng quote trá»±c tiáº¿p.
- [[CONCEPT_META_Wiki_Article_Length_Targets]] | **[[CONCEPT_META_Wiki_Article_Length_Targets|Wiki Article Length Targets]]** - Bá»™ ngÆ°á»¡ng Ä‘á»™ dÃ i theo type Ä‘á»ƒ cÃ¢n báº±ng chiá»u sÃ¢u vÃ  kháº£ nÄƒng Ä‘á»c.
- [[ENTITY_TOOL_Claude_Code_Wiki_Gen]] | **[[ENTITY_TOOL_Claude_Code_Wiki_Gen|Claude Code Wiki Gen]]** - Thá»±c thá»ƒ cÃ´ng cá»¥ há»— trá»£ thá»±c thi toÃ n bá»™ giao thá»©c nÃ y.

## ðŸ” 4. Review Items (DÃ nh cho Human)
- [ ] XÃ¡c nháº­n xem cáº¥u trÃºc `3-resources/wiki/` hiá»‡n táº¡i cÃ³ nÃªn Ã¡p dá»¥ng bá»™ Taxonomy 30 thÆ° má»¥c nÃ y khÃ´ng.
- [ ] Kiá»ƒm tra kháº£ nÄƒng triá»ƒn khai `_backlinks.json` tá»± Ä‘á»™ng báº±ng Python script.
- [ ] ÄÃ¡nh giÃ¡ xem `The Golden Rule` cÃ³ nÃªn Ä‘Æ°á»£c tÃ¡ch thÃ nh má»™t concept atom Ä‘á»™c láº­p á»Ÿ vÃ²ng ingest sau hay khÃ´ng.

--- 
**Nguá»“n thÃ´:** `MISC_wikiepdia_generate.md, AIMET_wiki-gen-skill.md`
**Deep Research Query:** `Claude Code personal knowledge wiki writer vs filing clerk`


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
