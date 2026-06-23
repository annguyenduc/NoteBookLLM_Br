import os
from PIL import Image, ImageDraw

media_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'GV-HO-AI-KT- Trí tuệ nhân tạo Trung học - Media'))

def test_boxes(image_name, raw_name, boxes):
    raw_path = os.path.join(media_dir, raw_name)
    try:
        with Image.open(raw_path) as img:
            for idx, box in enumerate(boxes):
                test_img = img.copy()
                draw = ImageDraw.Draw(test_img)
                draw.rectangle(box, outline="red", width=3)
                out_name = f"{image_name.split('.')[0]}_perfect_{idx}.png"
                test_img.save(os.path.join(media_dir, out_name))
                print(f"Saved {out_name} with box {box}")
    except Exception as e:
        print(f"Error processing {raw_name}: {e}")

if __name__ == '__main__':
    # Cau 22: block wait 2 seconds. Need to encase without hitting top/bottom blocks
    # let's try x=8, y=121 to x=170, y=170 (tight body)
    # vs x=5, y=116 to x=215, y=176
    boxes_22 = [
        (6, 120, 172, 172),
        (5, 118, 174, 174),
        (4, 118, 215, 178),
        (8, 120, 168, 170)
    ]
    test_boxes('cau_22.png', 'cau_22.raw.png', boxes_22)

    # Cau 23: block change so lan cuoi by 1. Need to encompass right circle without hitting bottom/top
    # The right circle extends to x=290 or so
    boxes_23 = [
        (40, 281, 292, 328),
        (38, 280, 294, 329),
        (37, 278, 296, 331),
        (39, 281, 291, 329)
    ]
    test_boxes('cau_23.png', 'cau_23.raw.png', boxes_23)
