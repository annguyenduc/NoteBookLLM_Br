import os
import re

test_bank_path = r"d:\NoteBookLLM_Br\3-resources\test-bank"
raw_path = r"d:\NoteBookLLM_Br\3-resources\raw\Tổng hợp đề kiểm tra LMS"

# 1. Get all raw docx files
raw_docs = []
for root, dirs, files in os.walk(raw_path):
    for file in files:
        if file.endswith(".docx"):
            raw_docs.append(file)

# 2. Count questions in test-bank per source
extracted_counts = {}
for file in os.listdir(test_bank_path):
    if file.endswith(".md"):
        path = os.path.join(test_bank_path, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Find source: "`filename.docx`"
            match = re.search(r'source: "`?([^`\n]+)`?"', content)
            if match:
                source = match.group(1).strip()
                extracted_counts[source] = extracted_counts.get(source, 0) + 1

# 3. Build report
print(f"{'Source Document':<60} | {'Count':<5} | {'Status'}")
print("-" * 80)
for doc in sorted(raw_docs):
    count = extracted_counts.get(doc, 0)
    status = "DONE" if count >= 20 else ("PARTIAL" if count > 0 else "MISSING")
    print(f"{doc[:60]:<60} | {count:<5} | {status}")
