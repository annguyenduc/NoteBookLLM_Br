import zipfile
import json
import os

def inspect_json(sb3_path):
    with zipfile.ZipFile(sb3_path, 'r') as z:
        if 'project.json' in z.namelist():
            project_json = json.loads(z.read('project.json').decode('utf-8'))
            print("Targets in project:")
            for target in project_json.get('targets', []):
                print(f"Name: {target.get('name')}, isStage: {target.get('isStage')}")
                print(f"  Costumes: {json.dumps(target.get('costumes', []), indent=2)}")
                print(f"  Blocks: {len(target.get('blocks', {}))}")
        else:
            print("No project.json found!")

def main():
    sb3_path = r"D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc\_GV-HO-AI-KT-Trí tuệ nhân tạo Trung học-Media\cau_24_a.sb3"
    inspect_json(sb3_path)

if __name__ == "__main__":
    main()
