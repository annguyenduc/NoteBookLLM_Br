import os
from PIL import Image, ImageDraw

media_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'GV-HO-AI-KT- Trí tuệ nhân tạo Trung học - Media'))

def test_final_options():
    raw_22 = os.path.join(media_dir, "cau_22.raw.png")
    raw_23 = os.path.join(media_dir, "cau_23.raw.png")
    
    # Câu 22:
    # Option A: Bao trọn chữ và thân phẳng (snug fit) -> (10, 122, 169, 168)
    # Option B: Bao trọn tối đa bao gồm cả notch nhưng né tránh avatar ở trên -> (6, 118, 174, 179)
    # Option C: Hơi rộng ra một chút ở trên/dưới -> (6, 119, 174, 172)
    img22_B = Image.open(raw_22).convert("RGB")
    draw22_B = ImageDraw.Draw(img22_B)
    box22_B = (6, 118, 174, 179)
    for offset in range(3):
        draw22_B.rectangle([box22_B[0]-offset, box22_B[1]-offset, box22_B[2]+offset, box22_B[3]+offset], outline="red")
    img22_B.save(os.path.join(media_dir, "cau_22_opt_B.png"))

    img22_C = Image.open(raw_22).convert("RGB")
    draw22_C = ImageDraw.Draw(img22_C)
    box22_C = (6, 119, 174, 172)
    for offset in range(3):
        draw22_C.rectangle([box22_C[0]-offset, box22_C[1]-offset, box22_C[2]+offset, box22_C[3]+offset], outline="red")
    img22_C.save(os.path.join(media_dir, "cau_22_opt_C.png"))

    # Câu 23:
    # Option A: Bao trọn đuôi block change -> (41, 281, 313, 329)
    # Option B: Rộng hơn một chút ở rìa -> (40, 280, 314, 331)
    img23_A = Image.open(raw_23).convert("RGB")
    draw23_A = ImageDraw.Draw(img23_A)
    box23_A = (41, 281, 313, 329)
    for offset in range(3):
        draw23_A.rectangle([box23_A[0]-offset, box23_A[1]-offset, box23_A[2]+offset, box23_A[3]+offset], outline="red")
    img23_A.save(os.path.join(media_dir, "cau_23_opt_A.png"))

    img23_B = Image.open(raw_23).convert("RGB")
    draw23_B = ImageDraw.Draw(img23_B)
    box23_B = (40, 280, 314, 331)
    for offset in range(3):
        draw23_B.rectangle([box23_B[0]-offset, box23_B[1]-offset, box23_B[2]+offset, box23_B[3]+offset], outline="red")
    img23_B.save(os.path.join(media_dir, "cau_23_opt_B.png"))

if __name__ == "__main__":
    test_final_options()
