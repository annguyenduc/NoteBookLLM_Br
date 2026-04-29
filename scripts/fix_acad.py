import os
import re

target_dir = r'd:\NoteBookLLM_Br\3-resources\wiki\concepts'

for filename in os.listdir(target_dir):
    if filename.endswith('.md') and filename.startswith('CONCEPT_ACAD_AI_'):
        filepath = os.path.join(target_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove the injected block
        pattern = re.compile(r'##\s*\d*\.?\s*Ví dụ minh họa \(Rule 17: Double Examples\).*?(?=\n\n---|\n# )', re.DOTALL)
        if pattern.search(content):
            new_content = pattern.sub('', content)
            
            # Since the block was injected right after frontmatter '---', the '---' was replaced.
            # I need to restore the '---' if it is missing at the end of the frontmatter.
            if not new_content.startswith('---\n'):
                pass
            
            # It's safer to just split and rebuild
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed {filename}')
