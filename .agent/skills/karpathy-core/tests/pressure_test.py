import os

def test_karpathy_compliance():
    print("Running Pressure Test for Karpathy Core...")
    skill_path = r'd:\NoteBookLLM_Br\.agent\skills\karpathy-core\SKILL.md'
    
    if not os.path.exists(skill_path):
        print("[FAIL] SKILL.md does not exist.")
        return False

    with open(skill_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    if "Use when" not in content:
        errors.append("Description does not start with 'Use when'.")
    if "### Examples" not in content and "## Examples" not in content:
        errors.append("Missing Examples section.")
    if "## Common Mistakes" not in content:
        errors.append("Missing Common Mistakes section.")
    if "## Red Flags" not in content:
        errors.append("Missing Red Flags section.")

    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return False
    else:
        print("[SUCCESS] All Karpathy Hardening criteria met. GREEN phase reached.")
        return True

if __name__ == "__main__":
    test_karpathy_compliance()
