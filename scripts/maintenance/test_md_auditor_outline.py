import pathlib
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from md_auditor import MarkdownAuditor


def _write(path: pathlib.Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


class TestMdAuditorOutline(unittest.TestCase):
    def setUp(self):
        self.temp_dir = pathlib.Path(tempfile.mkdtemp(prefix="md_auditor_outline_", dir="scratch"))
        self.pdf = self.temp_dir / "source.pdf"
        self.pdf.write_bytes(b"%PDF-1.4\n%test\n")
        self.package = self.temp_dir / "package"
        self.chunks = self.package / "chunks"
        self.chunks.mkdir(parents=True)

        self.chunk_names = ["RAW_TEST_P001-001.md", "RAW_TEST_P002-002.md"]
        for name in self.chunk_names:
            _write(
                self.chunks / name,
                "\n".join(
                    [
                        "---",
                        "audit_stamp: true",
                        "audit:",
                        '  status: "PASSED"',
                        '  verify_scope: "chunk"',
                        "---",
                        f"# {name}",
                    ]
                )
                + "\n",
            )

        inventory = "\n".join(
            [
                "| Chunk | Pages | File | Status |",
                "|---|---:|---|---|",
                f"| 001 | 1-1 | `{self.chunk_names[0]}` | READY |",
                f"| 002 | 2-2 | `{self.chunk_names[1]}` | READY |",
            ]
        )
        _write(
            self.package / "manifest.md",
            f'---\nsource_file: "{self.pdf}"\n---\n# Manifest\n\n{inventory}\n',
        )

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_outline_package_scope_passes_against_manifest_and_audited_chunks(self):
        outline = self.package / "outline.md"
        _write(
            outline,
            "\n".join(
                [
                    "---",
                    'primary_ingest_contract: "outline"',
                    'source_id: "test"',
                    "---",
                    "# Outline",
                    "Chunks:",
                    f"- `{self.chunk_names[0]}` - One (1-1)",
                    f"- `{self.chunk_names[1]}` - Two (2-2)",
                ]
            )
            + "\n",
        )

        result = MarkdownAuditor().verify_package_scope(outline, outline.read_text(encoding="utf-8"))

        self.assertEqual(result["result"], "PASS")
        self.assertEqual(result["verify_scope"], "package")
        self.assertEqual(result["package_chunk_count"], 2)
        self.assertEqual(result["package_inventory_count"], 2)

    def test_outline_package_scope_fails_when_outline_omits_manifest_chunk(self):
        outline = self.package / "outline.md"
        _write(
            outline,
            "\n".join(
                [
                    "---",
                    'primary_ingest_contract: "outline"',
                    'source_id: "test"',
                    "---",
                    "# Outline",
                    "Chunks:",
                    f"- `{self.chunk_names[0]}` - One (1-1)",
                ]
            )
            + "\n",
        )

        result = MarkdownAuditor().verify_package_scope(outline, outline.read_text(encoding="utf-8"))

        self.assertEqual(result["result"], "FAIL")
        self.assertIn("outline_missing_chunks_1", result["gaps"])


if __name__ == "__main__":
    unittest.main()
