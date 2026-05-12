# SCRIPTS_INDEX.md — NoteBookLLM_Br Script Directory
**Source of Truth for Automation & Maintenance**

## 1. CORE PIPELINE (Wiki 2.0)
| Script | Description | Status |
|---|---|---|
| `scripts/maintenance/audit_storage.py` | **SECURITY GATE**: Scans `raw_*` for unauthorized files and moves to Rejected. | ACTIVE |
| `scripts/maintenance/md_auditor.py` | **QUALITY GATE**: Audits and standardizes MD files in `00_Inbox` before promotion. | ACTIVE |
| `scripts/maintenance/promote.py` | **PROMOTION GATE**: Moves verified content from `00_Inbox` to `3-resources`. | ACTIVE |
| `.kiro/circuit_breaker.py` | **WRAPPER**: Protects promotion with retry limits and session locking. | ACTIVE |
| `scripts/maintenance/session_seal.py` | **INTEGRITY**: Seals the session and ensures all logs match filesystem changes. | ACTIVE |

## 2. MAINTENANCE & HEALING
| Script | Description | Status |
|---|---|---|
| `scripts/maintenance/heal_think_links.py` | Fixes internal thinking links and broken wikilinks. | ACTIVE |
| `scripts/maintenance/heal_encoding.py` | Standardizes UTF-8 encoding across the vault. | ACTIVE |
| `scripts/maintenance/normalize_atoms.py` | Standardizes metadata and frontmatter for Wiki Atoms. | ACTIVE |
| `scripts/maintenance/maint_cleanup_empty_folders.py` | Removes empty subdirectories from the workspace. | ACTIVE |

## 3. INFRASTRUCTURE & MCP
| Script | Description | Status |
|---|---|---|
| `scripts/mcp/run_mcp.py` | Orchestrator for running MCP servers (NotebookLM, etc). | ACTIVE |
| `scripts/setup/migrate_to_d.ps1` | Environment setup for migrating workspace to D: drive. | SETUP |

## 4. LEGACY / SPECIALIZED (Audit Pending)
- **Arduino Swarm**: `scripts/pipelines/arduino_swarm_*` (Specialized IoT pipeline).
- **LMS Ingest**: `scripts/maintenance/maint_lms_*` (Legacy LMS content tools).
- **SmartProxy Tests**: `scripts/tests/test_9router_*` (Legacy gateway connectivity tests).

## 5. SCRATCH & SANDBOX
*Mọi file trong `scratch/` là tệp tạm thời và có thể bị xóa định kỳ.*

---
> [!NOTE]
> Mọi script mới phải được đăng ký vào mục lục này. Cấm tạo script rác trực tiếp tại thư mục `scripts/`.
