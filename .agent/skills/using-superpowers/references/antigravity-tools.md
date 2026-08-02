# Antigravity Tool Mapping

Skills use Claude Code tool names. When you encounter these in a skill, use your Antigravity equivalent:

| Skill references | Antigravity equivalent |
|-----------------|------------------------|
| `Read` (file reading) | `mcp_filesystem_read_text_file` hoặc `view_file` |
| `Write` (file creation, new file) | `write_to_file` |
| `Edit` (file editing, existing file) | `replace_file_content` (1 block) hoặc `multi_replace_file_content` (nhiều block) |
| `Bash` (run commands) | `run_command` (PowerShell — Windows) |
| `Grep` (search file content) | `grep_search` |
| `Glob` (search files by name) | `mcp_filesystem_search_files` |
| `LS` (list directory) | `mcp_filesystem_list_directory` |
| `TodoWrite` (task tracking) | Không có tool trực tiếp — dùng artifact markdown task list với format: `- [ ] task` trong file `.md` tại scratch/ hoặc 1-projects/ |
| `Skill` tool (invoke a skill) | `view_file` trên path của SKILL.md |
| `WebSearch` | `search_web` |
| `WebFetch` (static HTML/markdown) | `read_url_content` |
| `WebFetch` (JS/dynamic/login) | `browser_subagent` |
| `Task` tool (dispatch subagent) | `browser_subagent` (chỉ cho browser tasks) — xem [Subagent support](#subagent-support) |

## Skill Invocation trong Antigravity

Trong Antigravity, "invoke a skill" = đọc file SKILL.md bằng `view_file`:

```
view_file("d:\\NoteBookLLM_Br\\.agent\\skills\\[skill-name]\\SKILL.md")
```

Không có `activate_skill` tool. Đọc SKILL.md = kích hoạt skill.

## Subagent support

Antigravity **không có** general-purpose subagent dispatcher.

`browser_subagent` chỉ dành cho tasks cần tương tác với browser (web navigation, UI interaction, recording).

| Skill instruction | Antigravity equivalent |
|-------------------|------------------------|
| `Task tool (superpowers:implementer)` | Không có — thực thi trực tiếp trong session hiện tại |
| `Task tool (superpowers:spec-reviewer)` | Không có — review trực tiếp trong session hiện tại |
| `Task tool (superpowers:code-reviewer)` | Không có — dùng `cm-code-review` skill thay thế |
| `Task tool (general-purpose)` với browser task | `browser_subagent` với prompt đầy đủ |
| `Task tool (general-purpose)` với non-browser task | Thực thi trực tiếp trong session hiện tại |

## Memory & Persistence

| Gemini/Codex concept | Antigravity equivalent |
|----------------------|------------------------|
| `save_memory` → GEMINI.md | KI system (`C:\Users\anngu\.gemini\antigravity\knowledge\`) |
| Session continuity | `cm-continuity` skill → `CONTINUITY.md` |

## Additional Antigravity-specific tools

Các tool này có trong Antigravity nhưng không có trong Claude Code hay Gemini CLI:

| Tool | Purpose |
|------|---------|
| `generate_image` | Tạo hoặc chỉnh sửa ảnh từ text prompt |
| `mcp_notebooklm-mcp-server_*` | Tương tác với Google NotebookLM (ingest profile) |
| `mcp_sqlite_*` | Query/write SQLite database (`wiki_brain.db`) |
| `mcp_local-ai_ollama_chat` | Chat với local Ollama model. Model mặc định: `gemma3:4b`. Nếu offline → WARNING, không block pipeline (R25) |
| `mcp_local-ai_gap_check` | Trigger gap analysis qua local AI (`gemma3:4b`). Chỉ dùng cho DRAFT atoms (R27) |
| `mcp_filesystem_edit_file` | Edit file line-based (thay thế cho `Edit` khi cần precision). ⚠️ **NOT a governance bypass tool**: phải tuân thủ cùng write boundaries như `replace_file_content`. Nếu built-in edit tool bị denied, KHÔNG dùng tool này để bypass — STOP và báo AN. |
| `mcp_filesystem_read_multiple_files` | Đọc nhiều file song song |
| `mcp_filesystem_directory_tree` | Xem cấu trúc thư mục dạng JSON tree |

## Shell Notes

- Shell mặc định: **PowerShell** (Windows)
- Không dùng Linux commands (`rm`, `mv`, `cat`) — dùng PowerShell equivalents
- File có tiếng Việt: **BẮT BUỘC** ghi qua Python với `encoding="utf-8"` (R4, Terminal Protocol)
- Không dùng `Out-File`, `Set-Content`, hoặc `>` redirect để ghi tiếng Việt
