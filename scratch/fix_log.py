import os

log_path = r"d:\NoteBookLLM_Br\3-resources\wiki\log.md"

with open(log_path, "rb") as f:
    data = f.read()

# Loại bỏ các byte null (\x00) thường gặp khi bị lỗi UTF-16 append vào UTF-8
# Và loại bỏ các khoảng trắng thừa do lỗi mã hóa tạo ra
cleaned_data = data.replace(b"\x00", b"")

# Ghi lại file đã được làm sạch
with open(log_path, "wb") as f:
    f.write(cleaned_data)

print("Đã làm sạch byte null trong log.md")
