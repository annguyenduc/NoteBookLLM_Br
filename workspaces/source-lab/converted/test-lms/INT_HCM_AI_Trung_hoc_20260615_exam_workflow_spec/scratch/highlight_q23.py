from pathlib import Path
from PIL import Image, ImageDraw

media_dir = Path(r"D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc\GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media")

for name in ["cau_23_a", "cau_23_b"]:
    png = media_dir / f"{name}.png"
    img = Image.open(png).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    if name.endswith('_a'):
        box = (int(w * 0.14), int(h * 0.77), int(w * 0.88), int(h * 0.94))
    else:
        box = (int(w * 0.10), int(h * 0.72), int(w * 0.92), int(h * 0.95))
    for offset in range(4):
        draw.rectangle((box[0]-offset, box[1]-offset, box[2]+offset, box[3]+offset), outline=(255, 0, 0, 255))
    img.save(png)
    print(f"highlighted {name}")