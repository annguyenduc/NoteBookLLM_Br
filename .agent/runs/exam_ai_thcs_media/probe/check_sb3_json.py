import zipfile
import json
import os

sb3_path = r"D:\_agent_worktrees\20260619_exam_ai_thcs_media\workspaces\source-lab\converted\bt2_code.sb3"

print("Checking SB3 file:", sb3_path)
if not os.path.exists(sb3_path):
    print("File does not exist!")
    exit(1)

try:
    with zipfile.ZipFile(sb3_path, 'r') as zip_ref:
        print("Zip contents:")
        for name in zip_ref.namelist():
            print("-", name)
        
        if 'project.json' in zip_ref.namelist():
            project_data = json.loads(zip_ref.read('project.json').decode('utf-8'))
            print("\nProject Targets:")
            for target in project_data.get('targets', []):
                print(f"Target: {target.get('name')} (isStage: {target.get('isStage')})")
                print(f"  Costumes: {[c.get('name') for c in target.get('costumes', [])]}")
                blocks = target.get('blocks', {})
                print(f"  Blocks count: {len(blocks)}")
                # Print some blocks
                for block_id, block in list(blocks.items())[:5]:
                    print(f"    Block: {block.get('opcode')}")
except Exception as e:
    print("Error:", str(e))
