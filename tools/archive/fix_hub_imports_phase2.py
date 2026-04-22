import os
import re

def fix_imports():
    root = "d:/Burn_Token"
    for dirpath, dirnames, filenames in os.walk(root):
        if ".venv" in dirpath or ".git" in dirpath or "__pycache__" in dirpath:
            continue
            
        for filename in filenames:
            if filename.endswith(".py") or filename.endswith(".md"):
                path = os.path.join(dirpath, filename)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                new_content = content
                
                # Replace 'libs.core' with 'libs.core'
                new_content = re.sub(r'\binfra\.core\b', 'libs.core', new_content)
                new_content = re.sub(r'\binfra/core\b', 'libs/core', new_content)
                
                # Replace 'apps/smart_proxy' with 'apps/smart_proxy'
                new_content = re.sub(r'\binfra/proxy\b', 'apps/smart_proxy', new_content)
                new_content = re.sub(r'\binfra\.proxy\b', 'apps.smart_proxy', new_content)
                
                if content != new_content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✅ Fixed: {path}")

if __name__ == "__main__":
    fix_imports()
