import os
from PIL import Image, ImageDraw

media_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'GV-HO-AI-KT- Trí tuệ nhân tạo Trung học - Media'))

def test_final_22():
    raw_22 = os.path.join(media_dir, "cau_22.raw.png")
    img22 = Image.open(raw_22).convert("RGB")
    draw22 = ImageDraw.Draw(img22)
    # Box này chừa ra 1 pixel ở rìa để không bị đè lên avatar phía trên (kết thúc ở y=120, avatar đi xuống y=116)
    # và không bị đè lên block bên dưới (bắt đầu ở y=170)
    box22 = (8, 121, 171, 169)
    for offset in range(3):
        draw22.rectangle([box22[0]-offset, box22[1]-offset, box22[2]+offset, box22[3]+offset], outline="red")
    img22.save(os.path.join(media_dir, "cau_22_final_test.png"))

if __name__ == "__main__":
    test_final_22()
