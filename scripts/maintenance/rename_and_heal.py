import os
import re

# Configuration
WORKSPACE_ROOT = r"d:\NoteBookLLM_Br"

RENAMES = {
    r"3-resources\wiki\synthesis\ACAD_AI_Responsible_AI.md": r"3-resources\wiki\synthesis\SYNTHESIS_ACAD_AI_Responsible_AI.md",
    r"3-resources\wiki\synthesis\THINK_Analytical_Thinking.md": r"3-resources\wiki\synthesis\SYNTHESIS_THINK_Analytical_Thinking.md"
}

LINK_MAP = {
    "ACAD_AI_Responsible_AI": "SYNTHESIS_ACAD_AI_Responsible_AI",
    "THINK_Analytical_Thinking": "SYNTHESIS_THINK_Analytical_Thinking"
}

def rename_files():
    print("--- Phase 1: Renaming Files ---")
    for old_rel, new_rel in RENAMES.items():
        old_path = os.path.join(WORKSPACE_ROOT, old_rel)
        new_path = os.path.join(WORKSPACE_ROOT, new_rel)
        if os.path.exists(old_path):
            print(f"Renaming {old_rel} -> {os.path.basename(new_rel)}")
            try:
                os.rename(old_path, new_path)
            except Exception as e:
                print(f"Error renaming {old_path}: {e}")
        else:
            print(f"File not found: {old_path}")

def update_links():
    print("\n--- Phase 2: Healing Wikilinks ---")
    for root, dirs, files in os.walk(WORKSPACE_ROOT):
        # Skip internal directories
        if any(d in root for d in [".git", "node_modules", ".gemini", ".antigravity"]):
            continue
            
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = content
                    for old_link, new_link in LINK_MAP.items():
                        # Pattern for [[Link]]
                        pattern = r'\[\[' + re.escape(old_link) + r'\]\]'
                        new_content = re.sub(pattern, f'[[{new_link}]]', new_content)
                    
                    if new_content != content:
                        print(f"Updating links in {os.path.relpath(file_path, WORKSPACE_ROOT)}")
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    rename_files()
    update_links()
    print("\n--- DONE ---")
