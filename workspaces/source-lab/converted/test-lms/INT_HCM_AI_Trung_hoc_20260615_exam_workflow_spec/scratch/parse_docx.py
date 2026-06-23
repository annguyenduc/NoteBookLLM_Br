import zipfile
import re
import xml.etree.ElementTree as ET
import os

def extract_text_from_docx(docx_path):
    # Namespace to parse docx XML
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    texts = []
    try:
        with zipfile.ZipFile(docx_path, 'r') as docx:
            xml_content = docx.read('word/document.xml')
            root = ET.fromstring(xml_content)
            
            # Find all paragraph elements
            for paragraph in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                # Extract text from runs
                p_text = ""
                for run in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r'):
                    for text_node in run.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                        if text_node.text:
                            p_text += text_node.text
                if p_text.strip():
                    texts.append(p_text.strip())
    except Exception as e:
        print(f"Error: {e}")
    return texts

def main():
    docx_path = r"D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc\_GV-HO-AI-KT-Trí tuệ nhân tạo Trung học.docx"
    
    if not os.path.exists(docx_path):
        print(f"File not found: {docx_path}")
        return
        
    texts = extract_text_from_docx(docx_path)
    
    # Filter lines related to questions
    print("Finding questions in DOCX...")
    q_pattern = re.compile(r'^(Câu\s*\d+|Bài\s*tập\s*\d+|Phần\s*I|Phần\s*II|PHẦN\s*I|PHẦN\s*II)', re.IGNORECASE)
    
    question_lines = []
    for i, line in enumerate(texts):
        if q_pattern.match(line):
            question_lines.append((i, line))
            print(f"Index {i}: {line}")
            
    # Write to a report file
    report_path = r"D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc\docx_question_structure.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("DOCX Question Structure Analysis\n")
        f.write("=================================\n\n")
        for idx, q in question_lines:
            f.write(f"Line {idx}: {q}\n")
            # Write a few surrounding lines to understand context
            start = max(0, idx - 1)
            end = min(len(texts), idx + 5)
            for j in range(start, end):
                if j != idx:
                    f.write(f"  [{j}] {texts[j]}\n")
            f.write("\n")
            
    print(f"\nSaved structure report to {report_path}")

if __name__ == "__main__":
    main()
