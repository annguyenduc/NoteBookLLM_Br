import os
import re

test_bank_path = r"d:\NoteBookLLM_Br\3-resources\test-bank"

# Group by Prefix + De
# Example: Robot_Rover_MCQ_De1
stats = {}

for file in os.listdir(test_bank_path):
    if file.endswith(".md"):
        # Match [LEVEL1]_[LEVEL2]_MCQ_De[X]
        match = re.match(r'^([A-Za-z]+_[A-Za-z0-9_]+_MCQ_De\d+)', file)
        if match:
            key = match.group(1)
            stats[key] = stats.get(key, 0) + 1

print(f"{'Module & Exam':<40} | {'Count':<5}")
print("-" * 50)
for key in sorted(stats.keys()):
    print(f"{key:<40} | {stats[key]:<5}")
