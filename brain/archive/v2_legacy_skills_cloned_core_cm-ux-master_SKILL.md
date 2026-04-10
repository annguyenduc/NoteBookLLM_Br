---


name: cm-ux-master
description: "CORE — Áp dụng 48 luật UX, heuristics Nielsen, phân tích trải nghiệm người dùng."
version: 2.0.0
---

# cm-ux-master — UX Master Platform (LITE)

> **Goal:** Design interfaces based on behavioral psychology and HCI ergonomics. Ensure the product is not only beautiful but also highly usable, high-performance, and accessible.

## When to Activate

- Reviewing a UI/UX design before implementation
- Evaluating an existing interface against UX principles
- Designing a new interface with mobile-first constraints
- Accessibility audit or conversion rate optimization

## Instructions

### The 7 Core UX Directives

| Directive | Rule | Action |
|-----------|------|--------|
| **1. Fitts's Law** | Touch ergonomics. | Interactive targets min 44×44px. Place primary action in Thumb Zone. |
| **2. Hick's Law** | Reduce cognitive load. | Use Progressive Disclosure (hide advanced). Max 1-2 Primary CTAs. |
| **3. Miller's Law** | Chunk information. | Group content into 5-9 items. Use whitespace to separate. |
| **4. Doherty** | Response speed. | Response < 400ms. Use Skeleton Loaders & Interactive States. |
| **5. A11y** | Accessibility. | WCAG 2.1 AA. Semantic HTML (`<nav>`, `<main>`, `<dialog>`). |
| **6. i18n Design** | Multi-language. | Design for the longest string (Vietnamese +20%, Thai +40%). Format date/number per locale. |
| **7. Mobile-First** | Mobile priority. | Especially for K-12 education. Min font 16px. No hover-only menus. |

### 48 UX Laws — Category Overview

- **Heuristic:** Aesthetic-Usability, Fitts's Law, Goal-Gradient, Hick's Law, Peak-End Rule.
- **Cognitive:** Anchoring, Confirmation Bias, Framing, Loss Aversion, Social Proof.
- **Visual:** Common Region, Proximity, Similarity, Enclosure, Continuity.

### 37 Design Tests (Before Publishing)

- **Contrast Test:** Ensure text/background contrast meets AA standard.
- **Squint Test:** Check visual hierarchy is clear even when squinting.
- **Thumb Zone Test:** Verify all key actions are reachable by thumb on mobile.
- **5-Second Test:** User can understand the page's purpose within 5 seconds.

## Quality Gate (Red Flags)

- ❌ Designing desktop-first then "squishing" it for mobile.
- ❌ Using hard-coded Hex colors instead of design tokens (Primary, Secondary).
- ❌ Missing critical UI states (Loading, Error, Empty State).
- ❌ Forgetting to account for Vietnamese (+20%) or Thai (+40%) string length expansion.

## Example Triggers

- "Review the UX of this Dashboard page."
- "Apply UX laws to improve the conversion rate of this form."
- "Design a mobile-first interface for primary school students."
- "Accessibility audit: does this UI meet WCAG 2.1 AA?"
