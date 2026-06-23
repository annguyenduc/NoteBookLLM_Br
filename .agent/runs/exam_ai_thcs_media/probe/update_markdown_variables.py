import re
import os

markdown_path = r"D:\_agent_worktrees\20260619_exam_ai_thcs_media\workspaces\source-lab\converted\Bai_kiem_tra_thuc_hanh_AI_THCS.md"

if not os.path.exists(markdown_path):
    print(f"Error: {markdown_path} does not exist.")
    exit(1)

with open(markdown_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Định nghĩa các phép thay thế chính xác
replacements = [
    # BT1
    (r"biến số `Điểm`", "biến số `score`"),
    (r"biến số `Vòng`", "biến số `round`"),
    (r"\bĐiểm\b", "score"),
    (r"\bVòng\b", "round"),
    (r"\bTừViệt\b", "vietWord"),
    (r"biến số `Điểm` và `Vòng`", "biến số `score` và `round`"),
    (r"biến Điểm và Vòng", "biến score và round"),
    (r"`Điểm` và `Vòng`", "`score` và `round`"),
    (r"`Điểm`", "`score`"),
    (r"`Vòng`", "`round`"),

    # BT2
    (r"biến số `Ngôn ngữ`", "biến số `language`"),
    (r"biến `Ngôn ngữ`", "biến `language`"),
    (r"`Ngôn ngữ`", "`language`"),
    (r"\bNgôn ngữ\b", "language"),
    (r"\"Cảnh 2\"", "\"scene2\""),
    (r"\"Cảnh 3\"", "\"scene3\""),
    (r"\"Cảnh 4\"", "\"scene4\""),
    (r"\"Cảnh 1\"", "\"scene1\""),
    (r"Cảnh 2", "scene2"),
    (r"Cảnh 3", "scene3"),
    (r"Cảnh 4", "scene4"),

    # BT3
    (r"biến số `Kết quả`", "biến số `calcResult`"),
    (r"biến `Kết quả`", "biến `calcResult`"),
    (r"`Kết quả`", "`calcResult`"),
    (r"List `Lịch sử`", "List `history`"),
    (r"`Lịch sử`", "`history`"),
    (r"Biến số `Số1`, `Số2`, `Phép chọn`", "Biến số `num1`, `num2`, `operation`"),
    (r"\bSố1\b", "num1"),
    (r"\bSố2\b", "num2"),
    (r"\bPhép chọn\b", "operation"),
    (r"\bKết quả\b", "calcResult"),
    (r"\bLịch sử\b", "history"),
    (r"`Số1`, `Số2`, `Phép chọn`", "`num1`, `num2`, `operation`"),
    (r"Biến `Kết quả`, `Số1`, `Số2`, `Phép chọn`", "Biến `calcResult`, `num1`, `num2`, `operation`"),

    # BT4
    (r"2 List: `Câu hỏi` \(5 câu\) và `Đáp án đúng`", "2 List: `questions` (5 câu) và `answers`"),
    (r"List `Câu hỏi`", "List `questions`"),
    (r"List `Đáp án đúng`", "List `answers`"),
    (r"`Câu hỏi`", "`questions`"),
    (r"`Đáp án đúng`", "`answers`"),
    (r"\bCâu hỏi\b", "questions"),
    (r"\bĐáp án đúng\b", "answers"),
    (r"\"Kết quả\"", "\"showResult\""),
    (r"Broadcast \"Kết quả\"", "Broadcast \"showResult\""),
    (r"Khi nhận \"Kết quả\"", "Khi nhận \"showResult\""),

    # BT5
    (r"trang phục \"chờ\"", "trang phục \"waiting\""),
    (r"trang phục \"vui\"", "trang phục \"smile\""),
    (r"trang phục \"buồn\"", "trang phục \"sad\""),
    (r"trang phục \"ngạc nhiên\"", "trang phục \"surprise\""),
    (r"trang phục \"cho\"", "trang phục \"waiting\""),
    (r"Switch costume → \"chờ\"", "Switch costume → \"waiting\""),
    (r"Switch costume → \"vui\"", "Switch costume → \"smile\""),
    (r"Switch costume → \"buồn\"", "Switch costume → \"sad\""),
    (r"Switch costume → \"ngạc nhiên\"", "Switch costume → \"surprise\""),
    (r"Switch backdrop → \"vui\"", "Switch backdrop → \"smile\""),
    (r"Switch backdrop → \"buồn\"", "Switch backdrop → \"sad\""),
    (r"Switch backdrop → \"ngạc nhiên\"", "Switch backdrop → \"surprise\""),

    # BT6
    (r"biến số `Số lần`", "biến số `count`"),
    (r"biến số `Đã đếm`", "biến số `isCounted`"),
    (r"`Số lần`", "`count`"),
    (r"`Đã đếm`", "`isCounted`"),
    (r"trang phục: \"đang tập\" và \"hoàn thành\"", "trang phục: \"exercise\" và \"completed\""),
    (r"cổ tay phải", "cổ tay trái"),
    (r"right wrist", "left wrist"),
    (r"\bSố lần\b", "count"),
    (r"\bĐã đếm\b", "isCounted"),
    (r"\"đang tập\"", "\"exercise\""),
    (r"\"hoàn thành\"", "\"completed\""),

    # BT7
    (r"biến số `Bài hiện tại`", "biến số `currentLesson`"),
    (r"biến `Bài hiện tại`", "biến `currentLesson`"),
    (r"`Bài hiện tại`", "`currentLesson`"),
    (r"\bBài hiện tại\b", "currentLesson"),
    (r"\"Bài 1\"", "\"Bai 1\""),
    (r"\"Bài 2\"", "\"Bai 2\""),
    (r"\"Bài 3\"", "\"Bai 3\""),
    (r"\"Bài 4\"", "\"Bai 4\""),
    (r"Broadcast \"Reset\"", "Broadcast \"Reset\""), # keep reset

    # BT8
    (r"Biến số `Điểm` và `Thời gian`", "Biến số `score` và `time`"),
    (r"biến số `Điểm`", "biến số `score`"),
    (r"biến số `Thời gian`", "biến số `time`"),
    (r"Broadcast \"Kết thúc\"", "Broadcast \"gameOver\""),
    (r"Khi nhận \"Kết thúc\"", "Khi nhận \"gameOver\""),
    (r"\"Kết thúc\"", "\"gameOver\""),
    (r"`Điểm` và `Thời gian`", "`score` và `time`"),
    (r"`Thời gian`", "`time`"),
    (r"\bThời gian\b", "time"),
    (r"\"Bắt được!\"", "\"Bat duoc!\""),
    (r"Biến `Thời gian`", "Biến `time`"),

    # BT9
    (r"biến số `ChỉSốCostume`", "biến số `costumeIndex`"),
    (r"biến `ChỉSốCostume`", "biến `costumeIndex`"),
    (r"`ChỉSốCostume`", "`costumeIndex`"),
    (r"\bChỉSốCostume\b", "costumeIndex"),
    (r"thông báo `ĐổiTrangSức`", "thông báo `changeJewelry`"),
    (r"\"ĐổiTrangSức\"", "\"changeJewelry\""),
    (r"`ĐổiTrangSức`", "`changeJewelry`"),

    # BT10
    (r"List `Đã điểm danh`", "List `presentList`"),
    (r"List `presentList` lưu tên", "List `presentList` lưu tên"),
    (r"`Đã điểm danh`", "`presentList`"),
    (r"Đã điểm danh", "presentList"),
    (r"tin nhắn `Hết giờ`", "tin nhắn `timeUp`"),
    (r"\"Hết giờ\"", "\"timeUp\""),
    (r"`Hết giờ`", "`timeUp`"),
    (r"\bSốCó\b", "presentCount"),
    (r"`SốCó`", "`presentCount`"),
]

new_content = content
for pattern, replacement in replacements:
    # Sử dụng Regex thay thế có phân biệt từ hoặc thay thế chuỗi trực tiếp
    new_content = re.sub(pattern, replacement, new_content)

# Lưu lại file
with open(markdown_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully updated markdown variables.")
