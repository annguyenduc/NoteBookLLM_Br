import os
import re

dist_dir = r'd:\NoteBookLLM_Br\brain\distilled'
files = [f for f in os.listdir(dist_dir) if f.startswith('LMS_DIST_') and f.endswith('.md')]

# Regex: ![Image](../assets/FILENAME.png)
# Group 1: ../assets/FILENAME.png
# Group 2: FILENAME.png
pattern = r'!\[Image\]\((\.\./assets/([^)]+))\)'

for fname in files:
    path = os.path.join(dist_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replace_image(match):
        rel_path = match.group(1)
        filename = match.group(2)
        abs_uri = f'file:///d:/NoteBookLLM_Br/brain/assets/{filename}'
        return f'[![Image]({rel_path})]({abs_uri})'
    
    new_content = re.sub(pattern, replace_image, content)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        # print(f"Healed images in {fname}")
