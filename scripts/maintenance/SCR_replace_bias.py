import os
import re

directories_to_scan = ['brain/process', 'brain/distilled', 'brain/wiki']

replacements = {
    r'\bThầy giáo\b': 'Giáo viên',
    r'\bthầy giáo\b': 'giáo viên',
    r'\bCô giáo\b': 'Giáo viên',
    r'\bcô giáo\b': 'giáo viên',
    r'\bThầy/Cô\b': 'Giáo viên',
    r'\bThầy/cô\b': 'Giáo viên',
    r'\bthầy/cô\b': 'giáo viên',
    r'\bThầy thầy cô\b': 'Giáo viên',
    r'\bthầy cô\b': 'giáo viên',
    r'\bcủa thầy\b': 'của giáo viên',
    r'\bcủa cô\b': 'của giáo viên',
    r'\bThầy gợi ý\b': 'Tôi gợi ý',
    r'\bthầy gợi ý\b': 'tôi gợi ý',
    r'\bthầy rất vui\b': 'tôi rất vui',
    r'\bThầy rất vui\b': 'Tôi rất vui',
    r'\bthầy dẫn dắt\b': 'tôi dẫn dắt',
    r'\bthầy đặt ra\b': 'tôi đặt ra',
    r'\bThầy đặt ra\b': 'Tôi đặt ra',
    r'\bthầy sẽ\b': 'tôi sẽ',
    r'\bThầy sẽ\b': 'Tôi sẽ',
    r'\bthầy thấy\b': 'tôi thấy',
    r'\bThầy thấy\b': 'Tôi thấy',
    r'\bThầy có\b': 'Tôi có',
    r'\bthầy có\b': 'tôi có',
    r'\bhỏi thầy\b': 'hỏi tôi',
    r'\bhỏi cô\b': 'hỏi tôi'
}

count = 0
for d in directories_to_scan:
    if not os.path.exists(d): continue
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith(('.md', '.json', '.html')):
                filepath = os.path.join(root, f)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                original_content = content
                for pattern, replacement in replacements.items():
                    content = re.sub(pattern, replacement, content)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(content)
                    print(f"Updated: {filepath}")
                    count += 1

print(f"Total files updated: {count}")
