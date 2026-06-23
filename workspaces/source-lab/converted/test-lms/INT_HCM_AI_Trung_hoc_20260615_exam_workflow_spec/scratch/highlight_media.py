import os
from PIL import Image, ImageDraw

# Thư mục chứa media
media_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'GV-HO-AI-KT- Trí tuệ nhân tạo Trung học - Media'))

def draw_red_box(image_name, box, raw_name=None):
    """
    Vẽ viền đỏ lên ảnh và lưu lại.
    image_name: Tên ảnh đích dùng trong đề thi (ví dụ: cau_22.png)
    box: Tọa độ viền đỏ dạng (x1, y1, x2, y2)
    raw_name: Tên ảnh raw gốc (ví dụ: cau_22.raw.png). Nếu không cung cấp, mặc định là image_name.raw.png
    """
    if not raw_name:
        raw_name = image_name.replace('.png', '.raw.png')
        
    raw_path = os.path.join(media_dir, raw_name)
    dest_path = os.path.join(media_dir, image_name)
    
    # Đảm bảo có ảnh raw
    if not os.path.exists(raw_path):
        if os.path.exists(dest_path):
            # Backup ảnh cũ làm raw
            os.rename(dest_path, raw_path)
            print(f"Backup {image_name} to {raw_name}")
        else:
            print(f"LỖI: Không tìm thấy ảnh nguồn {raw_path} hay {dest_path}")
            return
            
    # Mở ảnh raw và vẽ
    img = Image.open(raw_path)
    draw = ImageDraw.Draw(img)
    
    # Vẽ viền đỏ dày 3px bằng cách vẽ nhiều hình chữ nhật lồng nhau
    for offset in range(3):
        x1 = box[0] - offset
        y1 = box[1] - offset
        x2 = box[2] + offset
        y2 = box[3] + offset
        draw.rectangle([x1, y1, x2, y2], outline="red")
        
    img.save(dest_path)
    print(f"Đã vẽ viền đỏ và lưu: {image_name} (nguồn: {raw_name})")

# Danh sách các vùng cần vẽ viền đỏ
# Tọa độ căn chỉnh lại theo ảnh mới (chỉ phần block, không có flyout toolbox)
# Kích thước ảnh mới: cau_22=396x400, cau_23=396x400, cau_24=522x584,
#                     cau_26=303x272, cau_28=396x496, cau_29=501x416, cau_30=441x504
highlights = [
    {
        # Câu 3: Khoanh vùng thanh công cụ trên cùng (ảnh giao diện đầy đủ)
        'image': 'cau_3.png',
        'raw': 'cau_3.raw.png',
        'box': (5, 5, 800, 55)
    },
    {
        # Câu 22 (396x400): Khoanh vùng khối "wait 2 seconds"
        # Block wait: x=5~174, y=118~174 (perfect body fit)
        'image': 'cau_22.png',
        'raw': 'cau_22.raw.png',
        'box': (5, 118, 174, 174)
    },
    {
        # Câu 23 (396x400): Khoanh vùng khối "change Số lần cười by 1"
        # Block change: x=38~294, y=280~329 (perfect body fit)
        'image': 'cau_23.png',
        'raw': 'cau_23.raw.png',
        'box': (38, 280, 294, 329)
    },
    {
        # Câu 24 (522x584): Khoanh vùng nhánh if Lựa chọn = 2 (nhánh else thứ nhất)
        # Nánh if Lựa chọn=2 nằm khoảng y=370~460 (chỉ if+speak French)
        'image': 'cau_24.png',
        'raw': 'cau_24.raw.png',
        'box': (8, 370, 514, 460)
    },
    {
        # Câu 26 (303x272): Khoanh vùng khối "go to left upper eyelid"
        # Block go to nằm trong forever, khoảng y=170~230
        'image': 'cau_26.png',
        'raw': 'cau_26.raw.png',
        'box': (8, 170, 295, 232)
    },
    {
        # Câu 28 (396x496): Khoanh vùng 2 khối "add Vui vẻ to list" + "change Số lần cười"
        # add block: y=330~380, change block: y=380~430 (scan pixel thuc te)
        'image': 'cau_28.png',
        'raw': 'cau_28.raw.png',
        'box': (4, 327, 392, 433)
    },
    {
        # Câu 29 (501x416): Khoanh vùng 2 khối "ask ... and wait" liên tiếp
        # ask1: y=58~120, ask2: y=120~170 (scan pixel thuc te)
        'image': 'cau_29.png',
        'raw': 'cau_29.raw.png',
        'box': (4, 55, 380, 173)
    },
    {
        # Câu 30 (441x504): Khoanh vùng khối "turn video off" trong forever->if
        # turn video off: x=7~433, y=395~450 (scan pixel thuc te)
        'image': 'cau_30.png',
        'raw': 'cau_30.raw.png',
        'box': (4, 392, 436, 453)
    }
]

if __name__ == '__main__':
    print("Bắt đầu vẽ viền đỏ highlight cho các ảnh minh họa...")
    for hl in highlights:
        # Nếu là câu 3 và chưa có file backup, tự động tạo từ file cau_3.png hiện có
        draw_red_box(hl['image'], hl['box'], hl.get('raw'))
    print("Hoàn thành vẽ viền đỏ highlight!")
