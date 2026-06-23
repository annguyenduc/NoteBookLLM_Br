import os
from PIL import Image, ImageDraw, ImageFont

media_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'GV-HO-AI-KT- Trí tuệ nhân tạo Trung học - Media'))

def draw_grid(filename):
    path = os.path.join(media_dir, filename)
    if not os.path.exists(path):
        print(f"File {path} not found")
        return
    
    img = Image.open(path).convert("RGB")
    draw = ImageDraw.Draw(img)
    width, height = img.size
    
    # Draw vertical lines
    for x in range(0, width, 20):
        color = "blue" if x % 100 == 0 else "lightblue"
        draw.line([(x, 0), (x, height)], fill=color, width=1)
        if x % 40 == 0:
            draw.text((x + 2, 2), str(x), fill="black")
            
    # Draw horizontal lines
    for y in range(0, height, 20):
        color = "red" if y % 100 == 0 else "pink"
        draw.line([(0, y), (width, y)], fill=color, width=1)
        if y % 40 == 0:
            draw.text((2, y + 2), str(y), fill="black")
            
    out_path = os.path.join(media_dir, filename.replace(".raw.png", ".grid.png"))
    img.save(out_path)
    print(f"Saved grid image to {out_path}")

if __name__ == "__main__":
    draw_grid("cau_22.raw.png")
    draw_grid("cau_23.raw.png")
