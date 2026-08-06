---
name: spec-writer
description: Sử dụng khi tác vụ trong learning-vault cần một thư mục tác vụ mới theo chuẩn spec-first, một file SPEC.md mới, hoặc viết lại các tài liệu đặc tả (spec artifacts) cho các thay đổi gồm nhiều bước. Cũng được sử dụng khi không có kỹ năng (skill) nào khớp hiện có trong agent/skills/. KHÔNG sử dụng cho các câu hỏi đọc-ghi đơn giản, triển khai trực tiếp sau khi được duyệt, hoặc tác vụ đã được hỗ trợ bởi một kỹ năng chuẩn hóa hiện có.
---

# Spec Writer (Trình Viết Đặc Tả)

## Tổng Quan (Overview)

Kỹ năng này giúp tạo và duy trì các tài liệu tác vụ theo quy trình spec-first cho `learning-vault`.

Quy tắc cốt lõi rất đơn giản: Đánh giá quản trị nội bộ trước (local governance), sau đó đến tài liệu đặc tả (spec artifacts), tiếp theo là phê duyệt (approval), và cuối cùng là thực hiện các bước tiếp theo (downstream work).

## Khi Nào Cần Sử Dụng (When to Use)

Sử dụng kỹ năng này khi:

- Một tác vụ sẽ làm thay đổi các file, quy trình (workflows), kỹ năng (skills), quy tắc (rules), cấu trúc (structure), hoặc tri thức chuẩn hóa (canonical knowledge).
- Một tác vụ yêu cầu tạo mới `agent/specs/YYYY-MM-DD_task-name/SPEC.md`.
- Một tác vụ yêu cầu dọn dẹp hoặc viết lại các tài liệu đặc tả trước khi triển khai.
- Không có kỹ năng chuẩn hóa nào khớp hiện có trong thư mục `agent/skills/`.

Không sử dụng kỹ năng này khi:

- Tác vụ chỉ là câu hỏi đọc đơn giản hoặc tóm tắt ngắn gọn.
- Người dùng muốn triển khai trực tiếp một tác vụ đã được phê duyệt và kỹ năng/quy trình hiện tại đã hỗ trợ đầy đủ.
- Một kỹ năng chuẩn hóa hiện có tại `agent/skills/<skill-name>/SKILL.md` là công cụ phù hợp nhất cho tác vụ.

## Các Trường Hợp Không Kích Hoạt (Anti-Triggers)

- KHÔNG sử dụng cho câu trả lời một dòng, dịch thuật, hoặc định dạng đơn giản.
- KHÔNG sử dụng để bỏ qua các kỹ năng chuẩn hóa hiện có.
- KHÔNG sử dụng để tạo các file `SKILL.md` ngoài đường dẫn được phê duyệt.
- KHÔNG sử dụng để triển khai mã nguồn trước khi tài liệu đặc tả được phê duyệt.

## Thứ Tự Ưu Tiên Nguồn (Source Priority)

Áp dụng chính xác thứ tự ưu tiên sau:

1. `AGENTS.md`
2. `VAULT_CONSTITUTION.md`
3. `agent/constitution/`
4. `agent/rules/`
5. `agent/templates/`
6. Các tài liệu tác vụ hiện tại trong thư mục `agent/specs/<spec-id>/`
7. Các tài liệu tham khảo cấp trên như Superpowers, Spec Kit, Kiro Specs, BMAD, và các quy ước chung về `SKILL.md`.

Nếu có bất kỳ khung tham chiếu bên ngoài nào xung đột với quy định quản trị nội bộ, hãy từ chối quy tắc bên ngoài và tuân thủ tuyệt đối quy định quản trị nội bộ.

## Quy Trình Thực Hiện (Workflow)

### 1. Kiểm tra quản trị nội bộ trước (Check local governance first)

Trước khi viết bất kỳ nội dung nào, chỉ đọc những file nội bộ cần thiết cho tác vụ, bắt đầu từ:

- `AGENTS.md`
- `VAULT_CONSTITUTION.md`
- `agent/constitution/README.md` và các file liên quan trong thư mục `agent/constitution/`
- Các file liên quan trong thư mục `agent/rules/`

### 2. Kiểm tra các kỹ năng chuẩn hóa hiện có (Check existing canonical skills)

Kiểm tra thư mục `agent/skills/` xem có kỹ năng nào khớp trước khi mở một spec track mới.

Nếu tồn tại một kỹ năng chuẩn hóa khớp:

- Dừng luồng tạo kỹ năng này.
- Sử dụng kỹ năng hiện có đó thay thế.
- Chỉ tiếp tục với spec-writer nếu người dùng yêu cầu rõ ràng việc làm việc với tài liệu đặc tả.

Nếu không có kỹ năng nào khớp:

- Tiếp tục với quy trình spec-first bên dưới.

### 3. Tạo tài liệu kiểm soát đầu tiên (Create the first controlled artifact)

Tài liệu kiểm soát đầu tiên luôn luôn là:

`agent/specs/YYYY-MM-DD_task-name/SPEC.md`

Hãy tạo mới hoặc chỉnh sửa file `SPEC.md` trước tiên.

Không tạo các file phụ trợ dạng nháp như `CHECKLIST.md`, `PLAN.md`, `TASKS.md`, hoặc `REPORT.md` trước khi `SPEC.md` được phê duyệt, trừ khi người dùng cho phép rõ ràng.

### 4. Xây dựng tài liệu đặc tả chính xác (Build the spec correctly)

Mỗi file `SPEC.md` cần xác định rõ:

- Mục tiêu (objective)
- Phạm vi (scope)
- Tài liệu tham chiếu (references)
- Thứ tự ưu tiên nguồn (source priority)
- Các cổng phê duyệt (approval gates)
- Các hành động bị cấm (forbidden actions)
- Các giai đoạn dự kiến trong tương lai (expected future phases)

Phần `References` (Tài liệu tham chiếu) cần phân tách rõ ràng:

- Các quy định nội bộ (internal local rules)
- Các khung tham chiếu bên ngoài (external frameworks)
- Tài liệu tham khảo cấp trên (upstream references)
- Các tài liệu tham khảo bị từ chối hoặc không áp dụng (rejected or non-applicable references)

### 5. Yêu cầu phê duyệt trước khi tạo tài liệu hạ nguồn (Require approval before downstream artifacts)

Không triển khai mã nguồn trước khi được phê duyệt.

Sau khi `SPEC.md` được duyệt, tạo các tài liệu hạ nguồn theo nhu cầu thực tế và theo đúng thứ tự sau:

1. `CHECKLIST.md`
2. `PLAN.md`
3. `TASKS.md`
4. `REPORT.md` (chỉ tạo trong các giai đoạn xác minh/báo cáo sau đó)

### 6. Bảo toàn ranh giới nội bộ (Preserve local boundaries)

Chỉ sử dụng Superpowers như tài liệu tham khảo cấp trên.

Tuyệt đối không sao chép trực tiếp Superpowers vào `agent/skills/`.

Mọi hành vi bắt nguồn từ Superpowers phải được viết lại để phù hợp với đường dẫn nội bộ, quyền nội bộ, và các cổng phê duyệt nội bộ.

## Rào Chắn Bảo Vệ (Guardrails)

- Giữ tất cả công việc liên quan đến gói kỹ năng này trong thư mục `agent/skills/spec-writer/SKILL.md`.
- Không sử dụng `agent/skills/skill_<name>/` cho spec track này.
- Không chỉnh sửa `AGENTS.md`.
- Không chỉnh sửa `VAULT_CONSTITUTION.md`.
- Không chỉnh sửa các file trong `agent/constitution/` hoặc `agent/rules/` nếu không được phê duyệt rõ ràng.
- Không đưa nội dung thử nghiệm (lab content) lên các phân vùng chính thức (canonical zones) khi chưa được phê duyệt rõ ràng.
- Không xóa hoặc di chuyển file khi chưa được phê duyệt rõ ràng.
- Không commit hoặc push khi chưa được phê duyệt rõ ràng.
- Không nhúng mã nguồn thực thi trực tiếp vào kỹ năng này.

## Tham Khảo Nhanh (Quick Reference)

- File đầu tiên: `agent/specs/YYYY-MM-DD_task-name/SPEC.md`
- Quyết định đầu tiên: Kiểm tra xem có kỹ năng chuẩn hóa hiện có nào phù hợp hay không.
- Cổng đầu tiên: Đánh giá quản trị nội bộ.
- Cổng thứ hai: Phê duyệt `SPEC.md`.
- Các tài liệu hạ nguồn sau phê duyệt: `CHECKLIST.md`, `PLAN.md`, `TASKS.md`.
- Phương pháp bên ngoài: Chỉ dùng làm tài liệu tham khảo, tuyệt đối không có quyền cao hơn quy định quản trị nội bộ.

## Lỗi Thường Gặp (Common Mistakes)

- Tạo `PLAN.md` hoặc `TASKS.md` trước khi `SPEC.md` được phê duyệt.
- Coi Superpowers là nội dung chuẩn hóa nội bộ.
- Sử dụng trường `description` để tóm tắt quy trình (workflow) thay vì mô tả các điều kiện kích hoạt (trigger conditions).
- Bỏ qua việc kiểm tra kỹ năng chuẩn hóa hiện có.
- Coi các mẫu bên ngoài là lý do để phớt lờ quy định quản trị nội bộ.
