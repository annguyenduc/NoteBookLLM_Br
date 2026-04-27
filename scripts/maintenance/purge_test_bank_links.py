import os
import re

TEST_BANK_DIR = r"d:\NoteBookLLM_Br\brain\test-bank"
WIKI_PATTERN = re.compile(r'\[\[(.*?)\]\]')

def neutralize_links_in_test_bank():
    count = 0
    print(f"Scanning {TEST_BANK_DIR} for links to neutralize...")
    
    for root, dirs, files in os.walk(TEST_BANK_DIR):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = WIKI_PATTERN.sub(r'`\1`', content)
                    
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1
                        if count % 100 == 0:
                            print(f"  Neutralized links in {count} files...")
                except Exception as e:
                    print(f"Error processing {file}: {e}")
                    
    return count

if __name__ == "__main__":
    affected = neutralize_links_in_test_bank()
    print(f"\nSUCCESS: Neutralized all Wikilinks in {affected} files in test-bank.")
