# SKILL: wiki-council

Giải quyết mâu thuẫn tri thức phức tạp thông qua cơ chế Hội đồng (Council) và biểu quyết (Poll).

## Context (Bối cảnh)
Khi hệ thống phát hiện các Atoms mâu thuẫn trực tiếp về mặt nội dung (CONTRADICTS) mà các logic tự động không thể xử lý, `wiki-council` sẽ được kích hoạt để đưa ra quyết định dựa trên bằng chứng và sự đồng thuận. Đây là một **shared utility** quan trọng cho mọi Agent.

## Workflow (Quy trình)

### Bước 1: Summon Council (Triệu tập hội đồng)
Mọi Agent phát hiện mâu thuẫn cấp cao đều có quyền triệu tập Council. Quy trình bao gồm việc liệt kê các Atoms mâu thuẫn và các `learning_source` tương ứng.

### Bước 2: Peer Review (Kiểm định chéo)
Các Agent tham gia sẽ thực hiện **peer review**:
- Đối chiếu độ tin cậy của nguồn (Confidence Score).
- Kiểm tra tính thời điểm (Recency).
- Phân tích logic của Claim.

### Bước 3: Poll & Decision (Biểu quyết)
Thực hiện một **poll** (biểu quyết) ảo để lấy ý kiến của các Agent chuyên trách.
- Nếu đạt > 70% đồng thuận: Cập nhật Atom mới và tạo cạnh `SUPERSEDES`.
- Nếu không đạt đồng thuận: Đẩy lên **Chairman** (Con người) để đưa ra quyết định cuối cùng.

## Keywords
- **council**: Hội đồng đưa ra quyết định tri thức.
- **conflict**: Mâu thuẫn tri thức cần giải quyết.
- **shared utility**: Công cụ dùng chung cho toàn hệ thống.
- **poll**: Cơ chế biểu quyết giữa các Agent.
- **peer review**: Quy trình kiểm định chéo giữa các bên.
- **chairman**: Người có quyền quyết định cuối cùng (User).

## Constraints
- Không được đưa ra quyết định nếu bằng chứng (Source Tracing) không rõ ràng.
- Mọi biên bản họp Council phải được lưu vào `3-resources/wiki/decisions/`.
