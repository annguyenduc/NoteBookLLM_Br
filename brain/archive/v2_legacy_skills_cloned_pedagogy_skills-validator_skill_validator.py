import os
import re
import yaml
from pathlib import Path

class SkillValidator:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.results = []

    def validate_file(self, file_path):
        """Kiểm tra một tệp SKILL.md theo các tiêu chí chuẩn."""
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # 1. Kiểm tra YAML Frontmatter
            frontmatter_match = re.search(r'^\ufeff?---\s*(.*?)\s*---', content, re.DOTALL)
            if not frontmatter_match:
                return {"file": str(file_path), "name": "N/A", "status": "FAIL", "errors": ["Thiếu YAML frontmatter"]}
            
            data = yaml.safe_load(frontmatter_match.group(1))
            errors = []
            
            # 2. Kiểm tra các trường bắt buộc
            for field in ['name', 'description', 'version']:
                if field not in data:
                    errors.append(f"Thiếu trường '{field}' trong YAML")

            # 3. Kiểm tra tiền tố mô tả (Standardization)
            valid_prefixes = ['ToT', 'K-12', 'CORE', 'STEAM', 'PRO', 'LITE']
            if 'description' in data and not any(prefix in data['description'] for prefix in valid_prefixes):
                errors.append(f"Description thiếu tiền tố chuẩn (Vd: {valid_prefixes[0]})")

            # 4. Kiểm tra Quality Gate
            if "Quality Gate" not in content and "Gate" not in content:
                errors.append("Thiếu phần 'Quality Gate' để kiểm soát output")

            # 5. Kiểm tra Triggers
            if "Trigger" not in content and "Example Triggers" not in content:
                errors.append("Thiếu phần 'Example Triggers' để AI nhận diện")

            # 6. Kiểm tra độ dài (Token Optimization)
            word_count = len(content.split())
            if word_count > 3000:
                errors.append(f"File quá dài ({word_count} từ), cần tối ưu Progressive Disclosure (Layer 1-2)")

            return {
                "file": str(file_path.relative_to(self.root_dir)),
                "name": data.get('name', 'Unknown'),
                "status": "PASS" if not errors else "FAIL",
                "errors": errors
            }
        except Exception as e:
            return {"file": str(file_path), "name": "N/A", "status": "ERROR", "errors": [str(e)]}

    def run_audit(self, target_path=None):
        """Chạy audit trên toàn bộ thư mục skills."""
        search_path = Path(target_path) if target_path else self.root_dir
        skill_files = list(search_path.rglob("SKILL.md"))
        
        print(f"🔬 Đang bắt đầu Audit {len(skill_files)} kỹ năng...")
        print("-" * 50)
        
        for skill_file in skill_files:
            res = self.validate_file(skill_file)
            self.results.append(res)
            
            status_icon = "✅" if res['status'] == "PASS" else "❌"
            print(f"{status_icon} [{res['name']}] - {res['file']}")
            if res['errors']:
                for err in res['errors']:
                    print(f"   ⚠️  {err}")

        # Summary
        passed = len([r for r in self.results if r['status'] == "PASS"])
        print("-" * 50)
        print(f"📊 TỔNG KẾT: {passed}/{len(skill_files)} đạt chuẩn.")

if __name__ == "__main__":
    # Đường dẫn mặc định đến thư mục .agent/skills
    skills_dir = os.path.join(os.getcwd(), ".agent", "skills")
    validator = SkillValidator(skills_dir)
    validator.run_audit()


