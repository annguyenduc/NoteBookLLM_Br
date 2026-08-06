import pathlib
import sys
import tempfile
import unittest

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.maintenance.exam_workflow_validator import validate_exam_package

SAMPLE_EXAM = """# Draft

## **PHẦN II: ĐỀ THI THỰC HÀNH**

## **Bài tập 1: Demo 1**
### 3. Sản phẩm yêu cầu bàn giao
- 1 file dự án `.sb3`.
- 1 video demo dưới 2 phút.

## **Bài tập 2: Demo 2**
### 3. Sản phẩm yêu cầu bàn giao
- 1 file dự án `.sb3`.
- 1 video demo dưới 2 phút.

## **Bài tập 3: Demo 3**
### 3. Sản phẩm yêu cầu bàn giao
- 1 file dự án `.sb3`.
- 1 video demo dưới 2 phút.
"""


class ExamWorkflowValidatorTests(unittest.TestCase):
    def test_validate_exam_package_detects_video_and_code_requirements(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            exam_path = root / "exam.md"
            media_dir = root / "exam-Media"
            media_dir.mkdir()
            exam_path.write_text(SAMPLE_EXAM, encoding="utf-8")
            (media_dir / "sample_logic.png").write_text("stub", encoding="utf-8")
            (media_dir / "sample_logic.xml").write_text("<xml />", encoding="utf-8")
            (media_dir / "sample_logic.sb3").write_text("stub", encoding="utf-8")

            report = validate_exam_package(exam_path, media_dir)

            self.assertEqual(report["practical_count"], 3)
            self.assertTrue(report["all_practicals_require_video_demo"])
            self.assertTrue(report["all_practicals_require_code_deliverable"])
            self.assertTrue(report["media_has_physical_code_sample"])
            self.assertTrue(report["all_code_images_have_loadable_program"])
            self.assertEqual(report["missing_loadable_programs"], [])

    def test_validate_exam_package_flags_code_image_without_loadable_project(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            exam_path = root / "exam.md"
            media_dir = root / "exam-Media"
            media_dir.mkdir()
            exam_path.write_text(SAMPLE_EXAM, encoding="utf-8")
            (media_dir / "sample_logic.png").write_text("stub", encoding="utf-8")
            (media_dir / "sample_logic.xml").write_text("<xml />", encoding="utf-8")

            report = validate_exam_package(exam_path, media_dir)

            self.assertFalse(report["all_code_images_have_loadable_program"])
            self.assertEqual(report["missing_loadable_programs"], ["sample_logic"])


if __name__ == "__main__":
    unittest.main()
