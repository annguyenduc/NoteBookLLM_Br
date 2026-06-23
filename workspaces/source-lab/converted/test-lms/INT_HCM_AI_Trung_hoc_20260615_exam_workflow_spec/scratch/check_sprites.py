import zipfile
import json
import os
import glob

def analyze_sb3(file_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            if 'project.json' in zip_ref.namelist():
                with zip_ref.open('project.json') as f:
                    project_data = json.load(f)
                    targets = project_data.get('targets', [])
                    # Stage has isStage: true, Sprites have isStage: false or absent
                    sprites = [t for t in targets if not t.get('isStage', False)]
                    
                    sprite_info = []
                    for s in sprites:
                        name = s.get('name')
                        blocks = s.get('blocks', {})
                        num_blocks = len(blocks)
                        sprite_info.append(f"{name} ({num_blocks} blocks)")
                    
                    return len(sprites), sprite_info
            else:
                return -1, ["Missing project.json"]
    except Exception as e:
        return -2, [str(e)]

def main():
    # Kiem tra ca hai thu muc media neu co
    media_dirs = [
        r"D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc\_GV-HO-AI-KT-Trí tuệ nhân tạo Trung học-Media",
        r"D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc\output_ban_giao_20260622_01\1_Media\GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media"
    ]
    
    # Su dung thu muc media dau tien ton tai
    media_dir = None
    for d in media_dirs:
        if os.path.exists(d):
            media_dir = d
            break
            
    if not media_dir:
        print("Error: No media directory found!")
        return
        
    sb3_files = sorted(glob.glob(os.path.join(media_dir, "*.sb3")))
    
    print(f"Analyzing {len(sb3_files)} .sb3 files in {media_dir}...\n")
    results = []
    for sb3 in sb3_files:
        basename = os.path.basename(sb3)
        num_sprites, sprite_info = analyze_sb3(sb3)
        results.append({
            "file": basename,
            "sprites": num_sprites,
            "info": sprite_info
        })
        print(f"File: {basename} | Sprites: {num_sprites} | Details: {sprite_info}")
        
    # Write output report
    report_path = os.path.join(os.path.dirname(media_dir) if "output_ban_giao" not in media_dir else os.path.dirname(os.path.dirname(media_dir)), "sb3_sprite_audit_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Báo cáo kiểm tra Sprite và Blocks tự động\n\n")
        f.write(f"Đã phân tích {len(sb3_files)} tệp `.sb3` trong thư mục `{media_dir}`.\n\n")
        f.write("| Tên tệp | Số lượng Sprite | Chi tiết Sprite & Số lượng Blocks |\n")
        f.write("| --- | --- | --- |\n")
        for r in results:
            f.write(f"| {r['file']} | {r['sprites']} | {', '.join(r['info'])} |\n")
            
    print(f"\nBáo cáo đã được lưu tại {report_path}")

if __name__ == "__main__":
    main()
