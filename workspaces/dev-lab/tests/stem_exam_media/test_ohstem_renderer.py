from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = REPO_ROOT / "workspaces" / "dev-lab" / "tools" / "stem_exam_media" / "ohstem_renderer.py"


def load_renderer():
    spec = importlib.util.spec_from_file_location("ohstem_renderer", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def sample_spec(tmp_path: Path) -> Path:
    spec_path = tmp_path / "sample_ohstem.json"
    spec_path.write_text(
        json.dumps(
            {
                "asset_id": "MEDIA_OHSTEM_Q01_001",
                "title": "OhStem line follower checkpoint",
                "source_tool": "OhStem App",
                "source_url": "https://app.ohstem.vn/",
                "used_in": "Cau 01",
                "purpose": "Preview media for a STEM assessment question",
                "answer_leak_check": "NEEDS_REVIEW",
                "review_status": "PREVIEW_ONLY",
                "canvas": {"width": 960, "height": 540},
                "program": {
                    "device": "Yolo:Bit",
                    "blocks": [
                        {"kind": "robot", "label": "Khi nut A duoc nhan"},
                        {"kind": "line", "label": "Neu cam bien trai < 40"},
                        {"kind": "motor", "label": "Dieu chinh robot sang trai"},
                    ],
                },
                "question": {
                    "prompt": "Quan sat chuong trinh va du doan hanh vi robot.",
                    "alt_text": "So do khoi OhStem dieu khien robot bam vach.",
                },
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    return spec_path


class OhStemRendererTest(unittest.TestCase):
    def test_render_svg_escapes_content_and_marks_preview(self):
        renderer = load_renderer()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            media_spec = renderer.load_spec(sample_spec(tmp_path))

            svg = renderer.render_svg(media_spec)

        self.assertIn('<svg xmlns="http://www.w3.org/2000/svg"', svg)
        self.assertIn('width="960"', svg)
        self.assertIn("OhStem line follower checkpoint", svg)
        self.assertIn("Neu cam bien trai &lt; 40", svg)
        self.assertIn("PREVIEW_ONLY / NON_CANONICAL", svg)
        self.assertIn("Yolo:Bit", svg)
        self.assertIn('fill="#ff4ccd"', svg)
        self.assertIn('fill="#34ccf1"', svg)
        self.assertIn('fill="#0090f5"', svg)

    def test_palette_matches_aitt_robotics_extension_colors(self):
        renderer = load_renderer()

        self.assertEqual(("#717171", "#4f4f4f"), renderer.CATEGORY_COLORS["root"])
        self.assertEqual(("#ff4ccd", "#b83291"), renderer.CATEGORY_COLORS["robot"])
        self.assertEqual(("#0090f5", "#0067b3"), renderer.CATEGORY_COLORS["motor"])
        self.assertEqual(("#9b6af6", "#6d46ba"), renderer.CATEGORY_COLORS["sensor"])
        self.assertEqual(("#34ccf1", "#1f8faa"), renderer.CATEGORY_COLORS["line"])

    def test_write_package_creates_media_manifest_and_export_templates(self):
        renderer = load_renderer()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            output_dir = tmp_path / "package"

            result = renderer.write_package(sample_spec(tmp_path), output_dir)

            expected = {
                "media_ohstem_q01_001.svg",
                "media_ohstem_q01_001.html",
                "media_ohstem_q01_001_manifest.md",
                "exam_export.qmd",
                "exam_export.pandoc.md",
            }
            self.assertEqual(expected, {path.name for path in result.files})

            manifest = (output_dir / "media_ohstem_q01_001_manifest.md").read_text(encoding="utf-8")
            self.assertIn('asset_id: "MEDIA_OHSTEM_Q01_001"', manifest)
            self.assertIn('generation_method: "local_ohstem_style_renderer_preview"', manifest)
            self.assertIn('review_status: "PREVIEW_ONLY"', manifest)
            self.assertIn('canonical_status: "NON_CANONICAL"', manifest)
            self.assertNotIn("3-resources", manifest)

            qmd = (output_dir / "exam_export.qmd").read_text(encoding="utf-8")
            self.assertIn("format:", qmd)
            self.assertIn("html:", qmd)
            self.assertIn("docx:", qmd)
            self.assertIn("media_ohstem_q01_001.svg", qmd)
            self.assertIn("PREVIEW_ASSESSMENT", qmd)

            pandoc_md = (output_dir / "exam_export.pandoc.md").read_text(encoding="utf-8")
            self.assertIn("--resource-path=.", pandoc_md)
            self.assertIn("pandoc exam_export.pandoc.md", pandoc_md)
            self.assertIn("media_ohstem_q01_001.svg", pandoc_md)

    def test_render_svg_supports_inline_fields_and_reporter_blocks(self):
        renderer = load_renderer()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            spec_path = tmp_path / "sample_fields.json"
            spec_path.write_text(
                json.dumps(
                    {
                        "asset_id": "MEDIA_XBOT_FIELDS_Q01_001",
                        "title": "xBot field preview",
                        "source_tool": "OhStem App",
                        "source_url": "https://app.ohstem.vn/",
                        "used_in": "Cau 02",
                        "purpose": "Preview field-rich xBot block media",
                        "answer_leak_check": "NEEDS_REVIEW",
                        "review_status": "PREVIEW_ONLY",
                        "canvas": {"width": 980, "height": 420},
                        "program": {
                            "device": "xBot",
                            "blocks": [
                                {
                                    "kind": "basic",
                                    "shape": "statement",
                                    "fill": "#45c73b",
                                    "shadow": "#32962b",
                                    "segments": [
                                        {"type": "icon", "name": "pause"},
                                        {"type": "label", "text": "cho den khi"},
                                        {
                                            "type": "reporter",
                                            "fill": "#62a3f3",
                                            "shadow": "#4d7fc0",
                                            "text": "nut tren board duoc nhan",
                                        },
                                    ],
                                },
                                {
                                    "kind": "xbot_move",
                                    "shape": "statement",
                                    "fill": "#19c9c0",
                                    "shadow": "#11978f",
                                    "segments": [
                                        {"type": "icon", "name": "wheel"},
                                        {"type": "label", "text": "di chuyen"},
                                        {"type": "dropdown", "text": "up"},
                                        {"type": "label", "text": "voi toc do"},
                                        {"type": "number", "text": "50"},
                                        {"type": "label", "text": "trong"},
                                        {"type": "number", "text": "1"},
                                        {"type": "label", "text": "giay"},
                                    ],
                                },
                            ],
                        },
                        "question": {
                            "prompt": "Kiem tra block field-rich.",
                            "alt_text": "Preview with inline dropdown, number field, and reporter block.",
                        },
                    },
                    indent=2,
                ),
                encoding="utf-8",
            )

            media_spec = renderer.load_spec(spec_path)
            svg = renderer.render_svg(media_spec)

        self.assertIn('fill="#45c73b"', svg)
        self.assertIn('fill="#19c9c0"', svg)
        self.assertIn('fill="#62a3f3"', svg)
        self.assertIn(">50</text>", svg)
        self.assertIn(">1</text>", svg)
        self.assertIn("nut tren board duoc nhan", svg)


if __name__ == "__main__":
    unittest.main()
