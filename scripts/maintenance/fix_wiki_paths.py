import os
import re

def fix_paths(root_dir):
    # Các pattern cần thay thế
    replacements = {
        r'brain/atoms/': '3-resources/wiki/',
        r'atoms/': 'wiki/',
        r'Total atoms:': 'Total wiki pages:',
        r'Tổng atoms:': 'Tổng wiki pages:',
    }

    for root, dirs, files in os.walk(root_dir):
        # Bỏ qua các thư mục không cần thiết
        if '.git' in root or 'node_modules' in root:
            continue
            
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = content
                    for pattern, replacement in replacements.items():
                        new_content = re.sub(pattern, replacement, new_content)
                    
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Fixed: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    target_dir = r"d:\NoteBookLLM_Br"
    print(f"Starting path synchronization in {target_dir}...")
    fix_paths(target_dir)
    print("Done.")
