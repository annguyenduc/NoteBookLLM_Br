import zipfile
import json
import pathlib
import tempfile
import shutil

sb3_path = pathlib.Path(r'D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc\GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media\cau_26.sb3')

new_blocks_26 = {
  "q26_start": {
    "opcode": "event_whenflagclicked",
    "next": "q26_video",
    "parent": None,
    "inputs": {},
    "fields": {},
    "shadow": False,
    "topLevel": True,
    "x": 40,
    "y": 40
  },
  "q26_video": {
    "opcode": "poseFace_videoToggle",
    "next": "q26_forever",
    "parent": "q26_start",
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
    "parent": "q26_video",
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
  "q26_forever": {
    "opcode": "control_forever",
    "next": None,
    "parent": "q26_video",
    "inputs": {
      "SUBSTACK": [
        2,
        "q26_goto"
      ]
    },
    "fields": {},
    "shadow": False,
    "topLevel": False
  },
  "q26_goto": {
    "opcode": "poseFace_affdexGoToPart",
    "next": "q26_if",
    "parent": "q26_forever",
    "inputs": {},
    "fields": {
      "AFFDEX_POINT": [
        "11",
        None
      ]
    },
    "shadow": False,
    "topLevel": False
  },
  "q26_if": {
    "opcode": "control_if",
    "next": None,
    "parent": "q26_goto",
    "inputs": {
      "CONDITION": [
        2,
        "q26_wink"
      ],
      "SUBSTACK": [
        2,
        "q26_change"
      ]
    },
    "fields": {},
    "shadow": False,
    "topLevel": False
  },
  "q26_wink": {
    "opcode": "poseFace_affdexIsExpression",
    "next": None,
    "parent": "q26_if",
    "inputs": {
      "EXPRESSION": [
        1,
        "expr_val"
      ]
    },
    "fields": {},
    "shadow": False,
    "topLevel": False
  },
  "expr_val": {
    "opcode": "poseFace_menu_EXPRESSION",
    "next": None,
    "parent": "q26_wink",
    "inputs": {},
    "fields": {
      "EXPRESSION": [
        "eyeClosure",
        None
      ]
    },
    "shadow": True,
    "topLevel": False
  },
  "q26_change": {
    "opcode": "data_changevariableby",
    "next": "q26_sound",
    "parent": "q26_if",
    "inputs": {
      "VALUE": [
        1,
        [
          4,
          "1"
        ]
      ]
    },
    "fields": {
      "VARIABLE": [
        "Điểm",
        "q26_var_score"
      ]
    },
    "shadow": False,
    "topLevel": False
  },
  "q26_sound": {
    "opcode": "sound_playsounduntildone",
    "next": None,
    "parent": "q26_change",
    "inputs": {
      "SOUND_MENU": [
        1,
        "sound_val"
      ]
    },
    "fields": {},
    "shadow": False,
    "topLevel": False
  },
  "sound_val": {
    "opcode": "sound_sounds_menu",
    "next": None,
    "parent": "q26_sound",
    "inputs": {},
    "fields": {
      "SOUND_MENU": [
        "pop",
        None
      ]
    },
    "shadow": True,
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
    
    # Check variables in Stage (index 0)
    stage = project_data['targets'][0]
    if 'variables' not in stage:
        stage['variables'] = {}
    
    # Ensure "Điểm" variable with ID "q26_var_score" exists
    stage['variables']["q26_var_score"] = ["Điểm", 0]
    
    # Update blocks for Sprite1 (index 1)
    sprite = project_data['targets'][1]
    sprite['blocks'] = new_blocks_26
    
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
        print("Successfully updated SB3 file for Q26.")
        if backup_path.exists():
            backup_path.unlink()
    except Exception as e:
        print(f"Error packing zip: {e}")
        shutil.copy2(backup_path, sb3_path)
        if backup_path.exists():
            backup_path.unlink()
        raise e
