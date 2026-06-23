import os
import re

src_path = r"D:\NoteBookLLM_Br\workspaces\source-lab\converted\GV-HO-AI-KT-Tri tue nhan tao Trung hoc co so.md"
dest_path = r"D:\_agent_worktrees\20260619_exam_ai_thcs_media\workspaces\source-lab\converted\Bai_kiem_tra_thuc_hanh_AI_THCS.md"

with open(src_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replacements mapping
replacements = {
    r"> \[MEDIA_TODO: Ảnh PNG chụp toàn bộ khối lệnh nhân vật chính trên Dancing with AI — thể hiện rõ Translate, TTS Speak, Ask, If…else, Repeat, biến số Điểm và Vòng\]": 
        r"![Đáp án gợi ý BT1](file:///D:/NoteBookLLM_Br/.agent/runs/exam_ai_thcs_media/bt1_code.raw.png)",
        
    r"> \[MEDIA_TODO: Ảnh PNG toàn bộ khối lệnh — thể hiện rõ cấu trúc 4 cảnh, If chọn ngôn ngữ, TTS Speak, Translate, Broadcast chuyển cảnh\]":
        r"![Đáp án gợi ý BT2](file:///D:/NoteBookLLM_Br/.agent/runs/exam_ai_thcs_media/bt2_code.raw.png)",
        
    r"> \[MEDIA_TODO: Ảnh PNG toàn bộ khối lệnh — thể hiện rõ If…else 4 nhánh, TTS Speak, List Lịch sử và logic xử lý chia 0\]":
        r"![Đáp án gợi ý BT3](file:///D:/NoteBookLLM_Br/.agent/runs/exam_ai_thcs_media/bt3_code.raw.png)",
        
    r"> \[MEDIA_TODO: Ảnh PNG 2 phần: \(1\) khối lệnh nhân vật Quiz Master — loop hỏi đáp với List; \(2\) nhân vật tổng kết — Broadcast receiver, Translate, TTS 2 ngôn ngữ\]":
        r"![Đáp án gợi ý BT4](file:///D:/NoteBookLLM_Br/.agent/runs/exam_ai_thcs_media/bt4_code.raw.png)",
        
    r"> \[MEDIA_TODO: Ảnh PNG toàn bộ khối lệnh — thể hiện rõ 3 Face Sensing Event blocks, Switch Costume/Backdrop, Say \+ Translate cho từng biểu cảm, và trạng thái chờ\]":
        r"![Đáp án gợi ý BT5](file:///D:/NoteBookLLM_Br/.agent/runs/exam_ai_thcs_media/bt5_code.raw.png)",
        
    r"> \[MEDIA_TODO: Ảnh PNG toàn bộ khối lệnh — thể hiện rõ Forever \+ Body Sensing Go to, If điều kiện ngưỡng Y \+ biến Đã đếm, TTS Speak và Space reset\]":
        r"![Đáp án gợi ý BT6](file:///D:/NoteBookLLM_Br/.agent/runs/exam_ai_thcs_media/bt6_code.raw.png)",
        
    r"> \[MEDIA_TODO: Ảnh PNG 3 phần: \(1\) khối Ask \+ Broadcast điều hướng; \(2\) một cảnh học mẫu — TTS vi \+ Say \+ Translate \+ Say en \+ Face Sensing chuyển bài; \(3\) khối tóm tắt kết thúc song ngữ\]":
        r"![Đáp án gợi ý BT7](file:///D:/NoteBookLLM_Br/.agent/runs/exam_ai_thcs_media/bt7_code.raw.png)",
        
    r"> \[MEDIA_TODO: Ảnh PNG 3 phần: \(1\) khối lệnh Rổ — Face Sensing Forever; \(2\) khối lệnh Bóng — rơi \+ If chạm \+ Điểm \+ Broadcast \+ đồng hồ; \(3\) khối lệnh Tổng kết \+ Space reset\]":
        r"![Đáp án gợi ý BT8](file:///D:/NoteBookLLM_Br/.agent/runs/exam_ai_thcs_media/bt8_code.raw.png)",
        
    r"> \[MEDIA_TODO: Ảnh PNG 3 phần: \(1\) khối lệnh Mũ — Forever Body Sensing \+ Broadcast receiver; \(2\) khối lệnh 2 bông tai dùng chung ChỉSốCostume; \(3\) Người dẫn — Space trigger, ChỉSốCostume, Translate, TTS\]":
        r"![Đáp án gợi ý BT9](file:///D:/NoteBookLLM_Br/.agent/runs/exam_ai_thcs_media/bt9_code.raw.png)",
        
    r"> \[MEDIA_TODO: Ảnh PNG 2 phần: \(1\) khối lệnh nhân vật chính — Teachable Machine, 3 If kiểm tra \+ Add to List \+ TTS đọc tên, đồng hồ đếm ngược, Broadcast; \(2\) Nhân vật Tổng kết — tính SốCó, TTS vi, Translate, TTS en\]":
        r"![Đáp án gợi ý BT10](file:///D:/NoteBookLLM_Br/.agent/runs/exam_ai_thcs_media/bt10_code.raw.png)"
}

for pattern, replacement in replacements.items():
    content, count = re.subn(pattern, replacement, content)
    print(f"Replaced {pattern[:40]}... -> {count} times")

# Double check if any MEDIA_TODO remains
leftover = re.findall(r"MEDIA_TODO", content)
if leftover:
    print(f"[WARN] There are {len(leftover)} unresolved MEDIA_TODO items left!")
else:
    print("[OK] All MEDIA_TODO items successfully resolved!")

# Save to destination
os.makedirs(os.path.dirname(dest_path), exist_ok=True)
with open(dest_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"[OK] Exam file compiled successfully and written to {dest_path}")
