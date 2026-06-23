import os
from PIL import Image, ImageDraw

media_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'GV-HO-AI-KT- Trí tuệ nhân tạo Trung học - Media'))

def test_boxes(image_name, raw_name, boxes):
    raw_path = os.path.join(media_dir, raw_name)
    if not os.path.exists(raw_path):
        print(f"File {raw_path} not found")
        return
        
    for i, box in enumerate(boxes):
        img = Image.open(raw_path).convert("RGB")
        draw = ImageDraw.Draw(img)
        # Draw red box
        for offset in range(3):
            x1 = box[0] - offset
            y1 = box[1] - offset
            x2 = box[2] + offset
            y2 = box[3] + offset
            draw.rectangle([x1, y1, x2, y2], outline="red")
        
        out_name = image_name.replace(".png", f"_test_{i}.png")
        out_path = os.path.join(media_dir, out_name)
        img.save(out_path)
        print(f"Saved test image to {out_path} with box {box}")

if __name__ == "__main__":
    # Test boxes for cau_22
    # Option 0: current (7, 112, 172, 178) -> includes notch, might overlap block above/below
    # Option 1: exclude notch upper/lower (7, 120, 172, 170)
    # Option 2: safe bounds (5, 118, 175, 172)
    # Option 3: snug fit (7, 120, 172, 172)
    test_boxes("cau_22.png", "cau_22.raw.png", [
        (7, 112, 172, 178),
        (7, 120, 172, 170),
        (7, 119, 172, 172),
        (7, 118, 172, 171)
    ])
    
    # Test boxes for cau_23
    # Option 0: current (39, 280, 290, 330)
    # Option 1: exclude notch/safe (39, 286, 290, 324)
    # Option 2: snug fit (39, 282, 290, 326)
    test_boxes("cau_23.png", "cau_23.raw.png", [
        (39, 280, 290, 330),
        (39, 286, 290, 324),
        (39, 282, 290, 326),
        (39, 284, 290, 325)
    ])
