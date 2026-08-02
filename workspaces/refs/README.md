# External Reference Workspaces

Thư mục này chứa các repo bên ngoài dùng để tham chiếu, audit, hoặc chấm bộ skill/workflow của vault.

## Quy tắc

- Repo trong thư mục này không phải source of truth của vault.
- Không load skill từ đây như global runtime skill.
- Không copy nguyên xi skill vào `.agent/skills`.
- Không ghi nội dung từ đây vào `3-resources/`.
- Chỉ dùng theo yêu cầu rõ ràng: audit, chấm, so sánh, thiết kế test, hoặc port ý tưởng có SPEC/SIP riêng.

## Repo hiện có

### `superpowers/`

Nguồn: `https://github.com/obra/superpowers`

Vai trò:

- direct grader trong audit session;
- dùng để chấm skill discipline, planning discipline, verification discipline, skill governance, workspace isolation;
- không phải runtime skill source của `NoteBookLLM_Br`;
- không được import vào global skill path.
