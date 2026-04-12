Để giải quyết vấn đề màu chữ không nổi bật trên nền khối, giải pháp tối ưu nhất là sử dụng thuật toán **tính toán độ sáng (Luminance)**. Nếu nền sáng, chữ sẽ tự động chuyển sang màu đen; nếu nền tối, chữ sẽ chuyển sang màu trắng.

Dưới đây là các sự kiện kỹ thuật và mã nguồn đã được tối ưu hóa dựa trên quy trình modular (hàm riêng biệt):

### TRÍCH XUẤT THÔNG TIN (Facts) - Volume v14

- **Fact:** Sử dụng công thức tính độ sáng chuẩn: $Brightness = \frac{(R \times 299 + G \times 587 + B \times 114)}{1000}$ để xác định độ tương phản cho chữ.
- **Source:** Hàm `get_text_color` trong mã nguồn Python.
- **Tag:** [vv14]

- **Fact:** Kích thước font chữ 40-48 kết hợp với kích thước khối 120x120 là thông số tối ưu để đảm bảo chữ không bị tràn và dễ quan sát.
- **Source:** Phần cấu hình `FONT_SIZE` và `pygame.draw.rect`.
- **Tag:** [vv14]

- **Fact:** Việc căn giữa chữ trong khối được thực hiện chính xác nhất bằng cách lấy `rect` của bề mặt chữ và đặt `center` trùng với tâm của khối.
- **Source:** Hàm `display_blocks` sử dụng `get_rect(center=...)`.
- **Tag:** [vv14]

---

### MÃ NGUỒN TỐI ƯU (Modular + Dynamic Contrast)

```python
import pygame
import random
import time

# Khởi tạo Pygame
pygame.init()

# Cấu hình hệ thống
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chọn khối không trùng - Optimized")

# Màu sắc và Font
COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]
FONT_SIZE = 40
FONT = pygame.font.Font(None, FONT_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Thông số trò chơi
clock = pygame.time.Clock()
FPS = 30
game_time = 60
level = 1
max_level = 5
score = 0

# 1. Hàm xác định màu chữ dựa trên độ sáng của nền (TỐI ƯU MÀU CHỮ)
def get_contrast_color(bg_color_name):
    color = pygame.Color(bg_color_name)
    # Công thức tính độ sáng chuẩn YIQ
    brightness = (color.r * 299 + color.g * 587 + color.b * 114) / 1000
    return BLACK if brightness > 128 else WHITE

# 2. Tạo các khối
def create_blocks(level):
    num_blocks = min(level + 1, 6)
    blocks = []
    correct_block_index = random.randint(0, num_blocks - 1)
    for i in range(num_blocks):
        color = random.choice(COLORS)
        text = random.choice(COLORS)
        if i == correct_block_index:
            while color == text:
                text = random.choice(COLORS)
        else:
            color = text
        blocks.append({"color": color, "text": text})
    return blocks, correct_block_index

# 3. Hiển thị các khối (TỐI ƯU KÍCH THƯỚC & CĂN GIỮA)
def display_blocks(blocks):
    num_blocks = len(blocks)
    block_size = 120
    gap = WIDTH // (num_blocks + 1)
    
    for i, block in enumerate(blocks):
        x = gap * (i + 1) - (block_size // 2)
        y = HEIGHT // 2 - (block_size // 2)
        
        # Vẽ khối
        rect = pygame.Rect(x, y, block_size, block_size)
        pygame.draw.rect(screen, pygame.Color(block["color"]), rect, border_radius=10)
        
        # Xác định màu chữ tương phản
        text_color = get_contrast_color(block["color"])
        
        # Vẽ chữ và căn giữa tuyệt đối
        text_surface = FONT.render(block["text"].upper(), True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

# 4. Kiểm tra nhấp chuột
def check_player_click(pos, blocks):
    num_blocks = len(blocks)
    block_size = 120
    gap = WIDTH // (num_blocks + 1)
    for i in range(num_blocks):
        x = gap * (i + 1) - (block_size // 2)
        y = HEIGHT // 2 - (block_size // 2)
        rect = pygame.Rect(x, y, block_size, block_size)
        if rect.collidepoint(pos):
            return i
    return None

# 5. Vòng lặp chính
def game_loop():
    global score, level
    start_time = time.time()
    blocks, correct_index = create_blocks(level)
    running = True

    while running:
        screen.fill((30, 30, 30)) # Nền xám tối cho dịu mắt
        
        remaining_time = max(0, game_time - (time.time() - start_time))
        if remaining_time == 0: running = False

        # UI: Điểm và Thời gian
        time_txt = FONT.render(f"Time: {int(remaining_time)}s", True, WHITE)
        score_txt = FONT.render(f"Score: {score}", True, WHITE)
        screen.blit(time_txt, (20, 20))
        screen.blit(score_txt, (20, 70))

        display_blocks(blocks)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_index = check_player_click(event.pos, blocks)
                if clicked_index is not None:
                    if clicked_index == correct_index:
                        score += 10
                        level = min(level + 1, max_level)
                    else:
                        score -= 5
                    blocks, correct_index = create_blocks(level)

        pygame.display.flip()
        clock.tick(FPS)

    # Kết thúc
    screen.fill(BLACK)
    msg = FONT.render(f"GAME OVER! Score: {score}", True, WHITE)
    screen.blit(msg, (WIDTH//2 - 150, HEIGHT//2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()

if __name__ == "__main__":
    game_loop()
```

### Những điểm đã tối ưu:
1.  **Hàm `get_contrast_color`**: Đây là "linh hồn" của bản cập nhật này. Nó tự động tính toán: nếu bạn có khối màu vàng (`yellow`), chữ sẽ là màu đen. Nếu khối màu xanh dương đậm (`blue`), chữ sẽ tự chuyển sang trắng.
2.  **Căn giữa bằng `rect.center`**: Thay vì cộng trừ tọa độ thủ công (dễ sai lệch), mã sử dụng thuộc tính `center` của đối tượng Rect để chữ luôn nằm chính giữa khối dù kích thước font có thay đổi.
3.  **Bo góc khối (`border_radius`)**: Thêm một chút thẩm mỹ giúp các ô nhìn hiện đại hơn.
4.  **Sử dụng `collidepoint`**: Thay vì so sánh tọa độ `x, y` bằng các phép tính `if` dài dòng, hàm `rect.collidepoint(pos)` giúp kiểm tra va chạm chuột cực kỳ ngắn gọn và chính xác.