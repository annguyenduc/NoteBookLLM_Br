import os
from PIL import Image, ImageDraw

media_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'GV-HO-AI-KT- Trí tuệ nhân tạo Trung học - Media'))

def test_snug_boxes():
    # Câu 22: Thử nghiệm tọa độ co vào trong block wait (snug fit)
    # y1 từ 122 đến 124, y2 từ 166 đến 168, x1 từ 9 đến 11, x2 từ 168 đến 170
    raw_22 = os.path.join(media_dir, "cau_22.raw.png")
    img22 = Image.open(raw_22).convert("RGB")
    draw22 = ImageDraw.Draw(img22)
    box22 = (10, 122, 169, 168)
    for offset in range(3):
        draw22.rectangle([box22[0]-offset, box22[1]-offset, box22[2]+offset, box22[3]+offset], outline="red")
    img22.save(os.path.join(media_dir, "cau_22_snug_test.png"))

    # Câu 23: Thử nghiệm tọa độ co vào trong block change (snug fit)
    # y1 từ 282 đến 284, y2 từ 326 đến 328, x1 từ 42 đến 44, x2 từ 286 đến 288
    raw_23 = os.path.join(media_dir, "cau_23.raw.png")
    img23 = Image.open(raw_23).convert("RGB")
    draw23 = ImageDraw.Draw(img23)
    box23 = (42, 283, 287, 327)
    for offset in range(3):
        draw23.rectangle([box23[0]-offset, box23[1]-offset, box23[2]+offset, box23[3]+offset], outline="red")
    img23.save(os.path.join(media_dir, "cau_23_snug_test.png"))

if __name__ == "__main__":
    test_snug_boxes()
