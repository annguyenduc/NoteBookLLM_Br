import os
import re

target_dir = r"d:\NoteBookLLM_Br\3-resources\wiki\concepts"

missing_examples = []
total_files = 0

# Tìm kiếm chuẩn xác Header chứa "Ví dụ minh họa", "Rule 17" hoặc "Double Examples"
pattern = re.compile(r'#+\s*.*(ví dụ minh họa|rule 17|double examples).*', re.IGNORECASE)

for filename in os.listdir(target_dir):
    if filename.endswith(".md"):
        total_files += 1
        filepath = os.path.join(target_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if not pattern.search(content):
                missing_examples.append(filename)
        except Exception as e:
            print(f"Error reading {filename}: {e}")

print(f"Total files scanned: {total_files}")
print(f"Files missing EXACT Double Examples header: {len(missing_examples)}")
for f in missing_examples:
    print(f" - {f}")
