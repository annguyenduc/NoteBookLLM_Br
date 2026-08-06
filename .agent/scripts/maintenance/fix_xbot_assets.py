import os
import re

asset_dir = r'd:/NoteBookLLM_Br/3-resources/assets'
mcq_dir = r'd:/NoteBookLLM_Br/3-resources/test-bank'

# 1. Rename assets
asset_files = os.listdir(asset_dir)
xbot_assets = [f for f in asset_files if 'xBot' in f and 'rId' in f]

mapping = {}

for f in xbot_assets:
    match = re.search(r'rId(\d+)', f)
    if match:
        rid = match.group(1)
        ext = os.path.splitext(f)[1]
        new_name = f'ASSET_ROBOT_xBot_De1_rId{rid}{ext}'
        
        old_path = os.path.join(asset_dir, f)
        new_path = os.path.join(asset_dir, new_name)
        
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"Renamed RID {rid} to {new_name}")
        mapping[rid] = new_name

# 2. Update MCQs
mcq_files = [f for f in os.listdir(mcq_dir) if f.startswith('ROBOT_xBot_MCQ')]

for f in mcq_files:
    path = os.path.join(mcq_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find all image links: ![Image](../assets/...)
    # The current links look like: ![Image](../assets/DESIGN_RAW_Robotics_xBot_Đề_trắc_nghiệm_1_-_xBot_rId7.png)
    
    new_content = content
    # Use regex to find any link containing 'xBot' and 'rId'
    links = re.findall(r'!\[Image\]\(\.\./assets/([^)]+xBot[^)]+rId(\d+)[^)]+)\)', content)
    
    for full_old_name, rid in links:
        if rid in mapping:
            new_name = mapping[rid]
            new_content = new_content.replace(full_old_name, new_name)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated: {f}")
