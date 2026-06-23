import zipfile
import json
import pathlib
import tempfile
import shutil

sb3_path = pathlib.Path(r'D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc\GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media\cau_25.sb3')

new_blocks_25 = {
  "q25_start": {
    "opcode": "event_whenflagclicked",
    "next": "q25_video",
    "parent": None,
    "inputs": {},
    "fields": {},
    "shadow": False,
    "topLevel": True,
    "x": 40,
    "y": 40
  },
  "q25_video": {
    "opcode": "poseFace_videoToggle",
    "next": "q25_forever",
    "parent": "q25_start",
    "inputs": {
      "VIDEO_STATE": [
        1,
        "video_val"
      ]
    },
    "fields": {},
    "shadow": False,
    "topLevel": False
  },
  "video_val": {
    "opcode": "poseFace_menu_VIDEO_STATE",
    "next": None,
    "parent": "q25_video",
    "inputs": {},
    "fields": {
      "VIDEO_STATE": [
        "on",
        None
      ]
    },
    "shadow": True,
    "topLevel": False
  },
  "q25_forever": {
    "opcode": "control_forever",
    "next": None,
    "parent": "q25_video",
    "inputs": {
      "SUBSTACK": [
        2,
        "q25_goto_left"
      ]
    },
    "fields": {},
    "shadow": False,
    "topLevel": False
  },
  "q25_goto_left": {
    "opcode": "poseFace_affdexGoToPart",
    "next": "q25_goto_right",
    "parent": "q25_forever",
    "inputs": {},
    "fields": {
      "AFFDEX_POINT": [
        "0",
        None
      ]
    },
    "shadow": False,
    "topLevel": False
  },
  "q25_goto_right": {
    "opcode": "poseFace_affdexGoToPart",
    "next": None,
    "parent": "q25_goto_left",
    "inputs": {},
    "fields": {
      "AFFDEX_POINT": [
        "4",
        None
      ]
    },
    "shadow": False,
    "topLevel": False
  }
}

print(f"Reading {sb3_path}...")
with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir_path = pathlib.Path(tmpdir)
    
    # Extract existing sb3
    with zipfile.ZipFile(sb3_path, 'r') as zip_ref:
        zip_ref.extractall(tmpdir_path)
    
    # Modify project.json
    project_json_path = tmpdir_path / 'project.json'
    with open(project_json_path, 'r', encoding='utf-8') as f:
        project_data = json.load(f)
    
    # Update blocks for Sprite1 (index 1)
    sprite = project_data['targets'][1]
    sprite['blocks'] = new_blocks_25
    
    # Save modified project.json
    with open(project_json_path, 'w', encoding='utf-8') as f:
        json.dump(project_data, f, ensure_ascii=False, indent=2)
    
    # Repack to new sb3
    print(f"Repacking to {sb3_path}...")
    backup_path = sb3_path.with_suffix('.sb3.bak')
    shutil.copy2(sb3_path, backup_path)
    
    try:
        with zipfile.ZipFile(sb3_path, 'w', zipfile.ZIP_DEFLATED) as zip_write:
            for file_path in tmpdir_path.rglob('*'):
                if file_path.is_file():
                    zip_write.write(file_path, file_path.relative_to(tmpdir_path))
        print("Successfully updated SB3 file for Q25.")
        if backup_path.exists():
            backup_path.unlink()
    except Exception as e:
        print(f"Error packing zip: {e}")
        shutil.copy2(backup_path, sb3_path)
        if backup_path.exists():
            backup_path.unlink()
        raise e
