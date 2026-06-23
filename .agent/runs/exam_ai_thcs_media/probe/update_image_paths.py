import re
import os

markdown_path = r"D:\_agent_worktrees\20260619_exam_ai_thcs_media\workspaces\source-lab\converted\Bai_kiem_tra_thuc_hanh_AI_THCS.md"

if not os.path.exists(markdown_path):
    print(f"Error: {markdown_path} does not exist.")
    exit(1)

with open(markdown_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Thay thế các link tuyệt đối của ảnh thành relative path
# Ví dụ: file:///D:/NoteBookLLM_Br/.agent/runs/exam_ai_thcs_media/bt1_code.raw.png -> bt1_code.raw.png
# Hỗ trợ cả path NoteBookLLM_Br và _agent_worktrees
pattern = r"file:///D:/(?:NoteBookLLM_Br|_agent_worktrees/[^/]+)/\.agent/runs/exam_ai_thcs_media/(bt\d+_code\.raw\.png)"
new_content = re.sub(pattern, r"\1", content)

# Đảm bảo các biến thể link khác cũng được làm sạch
new_content = re.sub(r"file:///D:/NoteBookLLM_Br/\.agent/runs/exam_ai_thcs_media/", "", new_content)
new_content = re.sub(r"file:///D:/_agent_worktrees/[^/]+/\.agent/runs/exam_ai_thcs_media/", "", new_content)

with open(markdown_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully updated image paths in markdown to relative paths.")
