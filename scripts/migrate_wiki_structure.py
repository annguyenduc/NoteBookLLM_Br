#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Migration: Restructure wiki/ into subdirectories. Remove WIKI_ prefix."""

import os, re, shutil
from pathlib import Path

WIKI_DIR = Path(r"d:\NoteBookLLM_Br\3-resources\wiki")
ROOT_DIR = Path(r"d:\NoteBookLLM_Br")

FILE_MAPPINGS = {
    # Entities
    "WIKI_ENTITY_Data_Science.md": ("entities", "ENTITY_Data_Science.md"),
    # Sources
    "WIKI_SOURCE_THINK_Data_Science_for_Business.md": ("sources", "SOURCE_THINK_Data_Science_for_Business.md"),
    "WIKI_SOURCE_THINK_Problem_Solving_101.md": ("sources", "SOURCE_THINK_Problem_Solving_101.md"),
    "WIKI_SOURCE_THINK_Thinking_with_Data.md": ("sources", "SOURCE_THINK_Thinking_with_Data.md"),
    # Concepts - THINK
    "WIKI_THINK_5_Whys.md": ("concepts", "THINK_5_Whys.md"),
    "WIKI_THINK_Action_Plan_Execution.md": ("concepts", "THINK_Action_Plan_Execution.md"),
    "WIKI_THINK_Clustering_KMeans.md": ("concepts", "THINK_Clustering_KMeans.md"),
    "WIKI_THINK_CoNVO_Framework.md": ("concepts", "THINK_CoNVO_Framework.md"),
    "WIKI_THINK_Data_Argumentation.md": ("concepts", "THINK_Data_Argumentation.md"),
    "WIKI_THINK_Data_Ethics_Scoping.md": ("concepts", "THINK_Data_Ethics_Scoping.md"),
    "WIKI_THINK_Data_Evidence_Types.md": ("concepts", "THINK_Data_Evidence_Types.md"),
    "WIKI_THINK_Data_Mining_Process_CRISP.md": ("concepts", "THINK_Data_Mining_Process_CRISP.md"),
    "WIKI_THINK_Data_Mining_Tasks.md": ("concepts", "THINK_Data_Mining_Tasks.md"),
    "WIKI_THINK_Decision_Trees_Induction.md": ("concepts", "THINK_Decision_Trees_Induction.md"),
    "WIKI_THINK_Ensemble_Methods.md": ("concepts", "THINK_Ensemble_Methods.md"),
    "WIKI_THINK_Entropy_Information_Gain.md": ("concepts", "THINK_Entropy_Information_Gain.md"),
    "WIKI_THINK_Expected_Value_Framework.md": ("concepts", "THINK_Expected_Value_Framework.md"),
    "WIKI_THINK_Hypothesis_Pyramid.md": ("concepts", "THINK_Hypothesis_Pyramid.md"),
    "WIKI_THINK_Hypothesis_Testing.md": ("concepts", "THINK_Hypothesis_Testing.md"),
    "WIKI_THINK_Logic_Tree.md": ("concepts", "THINK_Logic_Tree.md"),
    "WIKI_THINK_Logistic_Regression_Classifier.md": ("concepts", "THINK_Logistic_Regression_Classifier.md"),
    "WIKI_THINK_Naive_Bayes_Logic.md": ("concepts", "THINK_Naive_Bayes_Logic.md"),
    "WIKI_THINK_Overfitting_Avoidance.md": ("concepts", "THINK_Overfitting_Avoidance.md"),
    "WIKI_THINK_Prioritization_Matrix.md": ("concepts", "THINK_Prioritization_Matrix.md"),
    "WIKI_THINK_Problem_Solving_Process.md": ("concepts", "THINK_Problem_Solving_Process.md"),
    "WIKI_THINK_Pros_Cons_List.md": ("concepts", "THINK_Pros_Cons_List.md"),
    "WIKI_THINK_ROC_AUC_Evaluation.md": ("concepts", "THINK_ROC_AUC_Evaluation.md"),
    "WIKI_THINK_Root_Cause_Analysis.md": ("concepts", "THINK_Root_Cause_Analysis.md"),
    "WIKI_THINK_Similarity_Distance_Metrics.md": ("concepts", "THINK_Similarity_Distance_Metrics.md"),
    "WIKI_THINK_SVM_Linear_Separation.md": ("concepts", "THINK_SVM_Linear_Separation.md"),
    "WIKI_THINK_TF_IDF_Text_Mining.md": ("concepts", "THINK_TF_IDF_Text_Mining.md"),
    "WIKI_THINK_Vision_Mockups.md": ("concepts", "THINK_Vision_Mockups.md"),
    "WIKI_THINK_Yes_No_Tree.md": ("concepts", "THINK_Yes_No_Tree.md"),
    # Concepts - ACAD (no rename)
    "ACAD_AI_Cutoff_vs_Drift.md": ("concepts", "ACAD_AI_Cutoff_vs_Drift.md"),
    "ACAD_AI_Data_Bias.md": ("concepts", "ACAD_AI_Data_Bias.md"),
    "ACAD_AI_Human_In_The_Loop.md": ("concepts", "ACAD_AI_Human_In_The_Loop.md"),
    "ACAD_AI_Information_Toolkit.md": ("concepts", "ACAD_AI_Information_Toolkit.md"),
    "ACAD_AI_Knowledge_Cutoff.md": ("concepts", "ACAD_AI_Knowledge_Cutoff.md"),
    "ACAD_AI_Learning_Habits.md": ("concepts", "ACAD_AI_Learning_Habits.md"),
    "ACAD_AI_Model_Drift.md": ("concepts", "ACAD_AI_Model_Drift.md"),
    # Images -> assets (keep filenames)
    "WIKI_IMG_THINK_5_Whys.png": ("assets", "WIKI_IMG_THINK_5_Whys.png"),
    "WIKI_IMG_THINK_Action_Roadmap.png": ("assets", "WIKI_IMG_THINK_Action_Roadmap.png"),
    "WIKI_IMG_THINK_CoNVO_Framework.png": ("assets", "WIKI_IMG_THINK_CoNVO_Framework.png"),
    "WIKI_IMG_THINK_CRISP_DM_Process.png": ("assets", "WIKI_IMG_THINK_CRISP_DM_Process.png"),
    "WIKI_IMG_THINK_Data_Argumentation.png": ("assets", "WIKI_IMG_THINK_Data_Argumentation.png"),
    "WIKI_IMG_THINK_Data_Ethics.png": ("assets", "WIKI_IMG_THINK_Data_Ethics.png"),
    "WIKI_IMG_THINK_Data_Mining_Tasks.png": ("assets", "WIKI_IMG_THINK_Data_Mining_Tasks.png"),
    "WIKI_IMG_THINK_Evidence_Blocks.png": ("assets", "WIKI_IMG_THINK_Evidence_Blocks.png"),
    "WIKI_IMG_THINK_Hypothesis_Pyramid.png": ("assets", "WIKI_IMG_THINK_Hypothesis_Pyramid.png"),
    "WIKI_IMG_THINK_Hypothesis_Test.png": ("assets", "WIKI_IMG_THINK_Hypothesis_Test.png"),
    "WIKI_IMG_THINK_Logic_Tree.png": ("assets", "WIKI_IMG_THINK_Logic_Tree.png"),
    "WIKI_IMG_THINK_Prioritization_Matrix.png": ("assets", "WIKI_IMG_THINK_Prioritization_Matrix.png"),
    "WIKI_IMG_THINK_Problem_Solving_Process.png": ("assets", "WIKI_IMG_THINK_Problem_Solving_Process.png"),
    "WIKI_IMG_THINK_Pros_Cons_Scale.png": ("assets", "WIKI_IMG_THINK_Pros_Cons_Scale.png"),
    "WIKI_IMG_THINK_Root_Cause_Analysis.png": ("assets", "WIKI_IMG_THINK_Root_Cause_Analysis.png"),
    "WIKI_IMG_THINK_Vision_Mockup.png": ("assets", "WIKI_IMG_THINK_Vision_Mockup.png"),
    "WIKI_IMG_THINK_Yes_No_Tree.png": ("assets", "WIKI_IMG_THINK_Yes_No_Tree.png"),
}

# Wikilink renames: old stem -> new stem
WIKILINK_RENAMES = {}
for old_name, (subdir, new_name) in FILE_MAPPINGS.items():
    if old_name.endswith('.md'):
        old_stem = Path(old_name).stem
        new_stem = Path(new_name).stem
        if old_stem != new_stem:
            WIKILINK_RENAMES[old_stem] = new_stem

# Image path renames
IMAGE_RENAMES = {}
for old_name, (subdir, new_name) in FILE_MAPPINGS.items():
    if not old_name.endswith('.md'):
        IMAGE_RENAMES[f"3-resources/wiki/{old_name}"] = f"3-resources/wiki/{subdir}/{new_name}"
        IMAGE_RENAMES[old_name] = f"assets/{new_name}"  # relative refs

def create_directories():
    for d in ["entities", "concepts", "sources", "queries", "comparisons", "assets"]:
        p = WIKI_DIR / d
        p.mkdir(exist_ok=True)
        # Create .gitkeep for empty dirs
        gitkeep = p / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.touch()
    print("[1] Directories created.")

def move_files():
    moved, skipped = 0, 0
    for old_name, (subdir, new_name) in FILE_MAPPINGS.items():
        src = WIKI_DIR / old_name
        dst = WIKI_DIR / subdir / new_name
        if src.exists():
            shutil.move(str(src), str(dst))
            moved += 1
        else:
            skipped += 1
    print(f"[2] Moved: {moved} | Skipped (not found): {skipped}")

def update_file(filepath):
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception:
        return False
    original = content
    # Update wikilinks [[OLD]] -> [[NEW]]
    for old_stem, new_stem in WIKILINK_RENAMES.items():
        content = re.sub(
            r'\[\[' + re.escape(old_stem) + r'(\|[^\]]*)?]]',
            lambda m, ns=new_stem: f'[[{ns}{m.group(1) or ""}]]',
            content
        )
    # Update image paths
    for old_path, new_path in IMAGE_RENAMES.items():
        content = content.replace(old_path, new_path)
    if content != original:
        filepath.write_text(content, encoding='utf-8')
        return True
    return False

def update_all_files():
    updated = 0
    search_paths = [
        ROOT_DIR / "3-resources",
        ROOT_DIR / "1-projects",
        ROOT_DIR / "2-areas",
    ]
    for sp in search_paths:
        if sp.exists():
            for fp in sp.rglob("*.md"):
                if update_file(fp):
                    updated += 1
    for fp in ROOT_DIR.glob("*.md"):
        if update_file(fp):
            updated += 1
    print(f"[3] Wikilinks updated in {updated} files.")

if __name__ == "__main__":
    print("=== Wiki Structure Migration ===")
    create_directories()
    move_files()
    update_all_files()
    print("=== Done ===")
