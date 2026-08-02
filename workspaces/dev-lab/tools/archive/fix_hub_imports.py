import os
import re

def fix_imports():
    root = "d:/Burn_Token"
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".py"):
                path = os.path.join(dirpath, filename)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Replace 'from libs.core' with 'from libs.core'
                # Use regex to match boundaries
                new_content = re.sub(r'\bfrom libs.core\b', 'from libs.core', content)
                new_content = re.sub(r'\bimport core\b', 'import libs.core', new_content)
                
                # Replace 'from apps.pdf_translator.pipeline' with 'from apps.pdf_translator.pipeline'
                new_content = re.sub(r'\bfrom apps.pdf_translator.pipeline\b', 'from apps.pdf_translator.pipeline', new_content)
                
                if content != new_content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✅ Fixed: {path}")

if __name__ == "__main__":
    fix_imports()
