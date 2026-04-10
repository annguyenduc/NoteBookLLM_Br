---


name: cm-test-gate
description: "CORE — Thiết lập hệ thống kiểm tra tự động đảm bảo chất lượng nhất quán."
version: 2.0.0
---

# cm-test-gate — Multi-Layer Test Gate (LITE)

> **Goal:** Establish an automated quality control gate. The `test:gate` command is the first line of defense, verifying UI safety, API behavior, business logic, i18n consistency, and security in one run.

## When to Activate

- Setting up a test infrastructure for a new project
- Adding automated quality checks before any deployment pipeline
- Ensuring i18n key parity across language files
- Scanning for secrets accidentally left in the codebase

## Instructions

### The 5-Layer Defense System

| Layer | Name | Focus |
|-------|------|-------|
| **L1** | **Frontend Safety** | Prevent white screens — catch JS syntax errors, broken HTML tags. |
| **L2** | **API Routes** | Ensure endpoints respond correctly (200 OK), clean JSON handling. |
| **L3** | **Business Logic** | Test pure calculation and data transformation functions. |
| **L4** | **i18n Sync** | Ensure language files have equal structure and key counts. |
| **L5** | **Security Scan** | Scan for secrets or sensitive data accidentally committed to git. |

### Implementation Protocol

1. **Stack Detection:** Identify the framework (React, Vue, Workers) to configure Vitest/Jest appropriately.
2. **Environment Setup:** Configure `vitest.config.ts`, `jsdom`, and test setup files.
3. **Core Test Files:** Create 5 separate test files corresponding to each of the 5 Layers (do not merge them).
4. **Script Wiring:** Add `"test:gate": "vitest run --reporter=verbose"` to `package.json`.
5. **Verification:** Run `npm run test:gate` to prove the system works end-to-end.

## Quality Gate (Red Flags)

- ❌ Merging all test layers into a single file (makes maintenance very difficult).
- ❌ Using real production credentials in the test environment.
- ❌ Skipping Layer L1 (Frontend Safety) for SPA/complex UI projects.
- ❌ Intentionally skipping failing test cases to proceed with deployment.

## Example Triggers

- "Set up a test gate system for this project."
- "Install automated i18n consistency checking."
- "Create a quality gate that runs before every deploy."
- "Configure Vitest with all 5 layers: frontend, API, logic, i18n, security."
