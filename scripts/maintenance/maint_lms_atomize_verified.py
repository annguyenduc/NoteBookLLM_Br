import os
import re

RAW_DIR = r"d:\NoteBookLLM_Br\brain\raw"
ATOMS_DIR = r"d:\NoteBookLLM_Br\brain\atoms"

def slugify(text):
    text = text.lower()
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    text = re.sub(r'[đ]', 'd', text)
    text = re.sub(r'[^a-z0-9_\-\.]', '_', text)
    return re.sub(r'_+', '_', text).strip('_')

def parse_raw_md(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm_match: return []
    
    fm_text = fm_match.group(1)
    source_match = re.search(r'source: "(.*?)"', fm_text)
    source = source_match.group(1) if source_match else os.path.basename(filepath)
    cat1_match = re.search(r'category: "(.*?)"', fm_text)
    cat1 = cat1_match.group(1) if cat1_match else "SYS"
    cat2_match = re.search(r'sub_category: "(.*?)"', fm_text)
    cat2 = cat2_match.group(1) if cat2_match else "General"
    
    body = content[fm_match.end():]
    
    # Split by "Câu X"
    # Pattern: "Câu " at start of line
    q_blocks = re.split(r'\n(?=Câu \d+)', body)
    
    questions = []
    for block in q_blocks:
        block = block.strip()
        if not block.startswith("Câu "): continue
        
        lines = block.split('\n')
        header = lines[0]
        q_num_match = re.search(r'Câu (\d+)', header)
        if not q_num_match: continue
        q_num = q_num_match.group(1)
        
        # Determine level
        level = "Unknown"
        level_match = re.search(r'\((.*?)\)', header)
        if level_match:
            level = level_match.group(1)
            
        # Parse content and choices
        q_text = []
        choices = {"A/": [], "B/": [], "C/": [], "D/": [], "E/": [], "F/": []}
        current_target = q_text
        answer = ""
        
        for line in lines[1:]:
            line = line.strip()
            if not line: continue
            
            # Check for choice start
            choice_match = re.match(r'^([A-F]/)', line)
            if choice_match:
                prefix = choice_match.group(1)
                current_target = choices[prefix]
                if "(Đáp án)" in line:
                    answer = prefix
                # Strip prefix and "(Đáp án)" from text
                clean_line = re.sub(r'^[A-F]/', '', line).replace('(Đáp án)', '').strip()
                if clean_line:
                    current_target.append(clean_line)
            else:
                # Check for answer marker in general line if not already found
                if "(Đáp án)" in line and not answer:
                    # Try to infer which choice this line belongs to
                    # If we are already in a choice, keep it there
                    pass
                
                # Append to current target
                current_target.append(line)
                
                # Double check for answer marker again
                if "(Đáp án)" in line:
                    # If this line is an image link but contains (Đáp án)
                    # it means the previous run was red.
                    # Usually (Đáp án) is added to the text.
                    pass

        questions.append({
            "num": q_num,
            "header": header,
            "level": level,
            "q_text": q_text,
            "choices": choices,
            "answer": answer,
            "source": source,
            "cat1": cat1,
            "cat2": cat2
        })
        
    return questions

def create_atom(q, file_slug):
    atom_id = f"QUESTION_{q['cat1']}_{q['cat2']}_{file_slug}_{q['num']}"
    filepath = os.path.join(ATOMS_DIR, atom_id + ".md")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"file_id: \"{atom_id}\"\n")
        f.write(f"title: \"{q['header']}\"\n")
        f.write(f"category: \"Atomic Question\"\n")
        f.write(f"prefix: \"QUESTION\"\n")
        f.write(f"tags: ['{q['cat1']}', '{q['cat2']}', '{q['level']}']\n")
        f.write(f"source: \"{q['source']}\"\n")
        f.write(f"level: \"{q['level']}\"\n")
        f.write(f"answer: \"{q['answer']}\"\n")
        f.write(f"status: \"draft\"\n")
        f.write(f"created: \"2026-04-22\"\n")
        f.write("---\n\n")
        
        f.write(f"# [QUESTION] {q['header']}\n\n")
        f.write("## ❓ Câu hỏi\n")
        for line in q['q_text']:
            # Handle image links - ensure they are correct
            line = line.replace('(Đáp án)', '').strip()
            if line:
                f.write(line + "\n")
        f.write("\n")
        
        f.write("## 📝 Đáp án lựa chọn\n")
        for prefix, lines in q['choices'].items():
            if not lines and prefix not in ["A/", "B/", "C/", "D/"]: continue
            
            ans_marker = " (Đáp án)" if q['answer'] == prefix else ""
            f.write(f"- **{prefix}{ans_marker}**\n")
            for line in lines:
                line = line.replace('(Đáp án)', '').strip()
                if line:
                    if line.startswith("![Image]"):
                        f.write(f"  {line}\n")
                    else:
                        f.write(f"  {line}\n")
        f.write("\n")
        
        f.write("## 🔗 Liên kết tư duy\n")
        f.write(f"- Kiến thức liên quan: [[WIKI_{q['cat1']}]]\n")
        f.write(f"- Module: [[{q['cat1']}_{q['cat2']}]]\n\n")
        
        f.write("## 📖 Nguồn\n")
        f.write(f"`📖 Nguồn: [{q['source'].strip('[]')}] — {q['num']}`\n")

def main():
    for f in os.listdir(RAW_DIR):
        if f.startswith(("KHMT_", "Robot_", "IOT_", "DESIGN_")) and f.endswith(".md"):
            print(f"Atomizing: {f}")
            file_slug = slugify(os.path.splitext(f)[0])
            # Remove prefix from slug if needed, but here we want it unique
            questions = parse_raw_md(os.path.join(RAW_DIR, f))
            for q in questions:
                create_atom(q, file_slug)

if __name__ == "__main__":
    main()
