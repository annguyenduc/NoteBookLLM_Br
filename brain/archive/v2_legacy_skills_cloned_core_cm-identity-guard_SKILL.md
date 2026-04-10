---


name: cm-identity-guard
description: "CORE — Kỹ năng chuyên biệt đóng vai trò là 'Cổng an ninh'. Kiểm tra thẩm quyền (Identity & Permission) trước khi thực hiện các tác vụ rủi ro cao."
version: 2.0.0
---

# cm-identity-guard — Identity & Permission Guard (LITE)

> **Goal:** Ensure that every high-risk task (data destruction, system configuration changes) is authenticated and approved by a human administrator before execution.

## When to Activate

- Any command that deletes files or directories
- Any command that rewrites git history
- Any command that modifies global system state or environment
- When another skill explicitly calls the Permission Gate

## Instructions

### The Verification Protocol

1. **Detect High-Risk Mission:** When receiving a request involving:
   - File/folder deletion (`rm`, `del`, `rmdir`).
   - Rewriting source history (`git push --force`, `git reset --hard`).
   - Wiping a database (`DROP TABLE`, `DELETE FROM` without WHERE).
   - System-level installs or uninstalls (`npm uninstall -g`, `pip install --system`).

2. **Stop & Ask (Mandatory):** Halt and send an explicit confirmation message:
   > *"I detected the action [action description] as high-risk. Are you sure you want to continue?"*
   - Never execute if the user has not responded, or responds "No".

3. **Log the Consent:** After user approval, record the event in `CONTINUITY.md` or the system log with timestamp and action description.

### Dangerous Command List (Red List)

| Command | Risk Reason | Risk Level |
|---------|------------|------------|
| `rm -rf` | Unrecoverable deletion. | High |
| `git reset --hard` | Loses uncommitted data. | High |
| `npm uninstall -g` | Breaks global environment. | Medium |
| `DROP TABLE` | Permanent data loss. | Critical |
| `format` | Wipes entire partition. | Critical |

## Quality Gate (Red Flags)

- ❌ Running `rm` automatically because it "seems like part of the task."
- ❌ Describing the action vaguely to trick the user into accidentally approving.
- ❌ Not reviewing the list of affected files before requesting deletion approval.

## Example Triggers

- "Delete the entire build and node_modules directory."
- "Reset this repo back to the old commit."
- "Uninstall module X from the system."
- "Force push to main — are you sure?"
