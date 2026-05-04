import os
import re

TARGET_DIRS = [
    r"d:\NoteBookLLM_Br\brain\wiki",
    r"d:\NoteBookLLM_Br\brain\distilled"
]

# Pattern to find [[ ]] links that point to atoms or test-bank
# Matches:
# [[test-bank/...]]
# [[MCQ_...]]
# [[IOT_MCQ_...]]
# [[NON_MCQ_...]]
# [[NEEDS_REVIEW_MCQ_...]]
ATOM_PATTERN = re.compile(r'\[\[((?:test-bank/|MCQ_|IOT_MCQ_|NON_MCQ_|NEEDS_REVIEW_MCQ_).*?)\]\]')

def neutralize_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = ATOM_PATTERN.sub(r'`\1`', content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
    return False

def main():
    total_affected = 0
    for target_dir in TARGET_DIRS:
        print(f"Processing directory: {target_dir}")
        for root, dirs, files in os.walk(target_dir):
            for file in files:
                if file.endswith('.md'):
                    if neutralize_file(os.path.join(root, file)):
                        total_affected += 1
                        print(f"  Neutralized links in: {file}")
    
    print(f"\nDone! Neutralized atom links in {total_affected} files.")

if __name__ == "__main__":
    main()
