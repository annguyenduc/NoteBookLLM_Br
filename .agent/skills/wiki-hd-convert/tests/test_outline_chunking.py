import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "scripts"))
import hd_converter


class TestOutlineChunking(unittest.TestCase):
    def test_assign_end_pages_tracks_sibling_boundaries(self):
        nodes = [
            {
                "title": "Chapter One",
                "page": 10,
                "children": [
                    {"title": "Section A", "page": 10, "children": []},
                    {"title": "Section B", "page": 20, "children": []},
                ],
            },
            {"title": "Chapter Two", "page": 30, "children": []},
        ]

        hd_converter.assign_end_pages(nodes, 40)

        self.assertEqual(nodes[0]["end_page"], 30)
        self.assertEqual(nodes[0]["children"][0]["end_page"], 20)
        self.assertEqual(nodes[0]["children"][1]["end_page"], 30)
        self.assertEqual(nodes[1]["end_page"], 40)

    def test_build_chunk_plan_prefers_section_before_page_split(self):
        nodes = [
            {
                "title": "PART ONE",
                "page": 0,
                "children": [
                    {
                        "title": "Chapter One The Basics",
                        "page": 5,
                        "children": [
                            {"title": "Section A", "page": 5, "children": []},
                            {"title": "Section B", "page": 25, "children": []},
                        ],
                    }
                ],
            }
        ]

        plan = hd_converter.build_chunk_plan(nodes, total_pages=40, max_pages=10)

        self.assertEqual(len(plan), 5)
        self.assertEqual(plan[0]["section_title"], "PART ONE - Intro")
        self.assertEqual(plan[0]["start_page"], 0)
        self.assertEqual(plan[0]["end_page"], 5)
        self.assertEqual(plan[1]["chapter_title"], "Chapter One The Basics")
        self.assertEqual(plan[1]["section_title"], "Section A")
        self.assertEqual(plan[1]["start_page"], 5)
        self.assertEqual(plan[1]["end_page"], 15)
        self.assertEqual(plan[1]["unit_id"], "CH01_SEC01_P01")
        self.assertEqual(plan[2]["unit_id"], "CH01_SEC01_P02")
        self.assertEqual(plan[3]["section_title"], "Section B")
        self.assertEqual(plan[3]["unit_id"], "CH01_SEC02_P01")
        self.assertEqual(plan[4]["unit_id"], "CH01_SEC02_P02")

    def test_build_chunk_plan_handles_frontmatter_without_chapter(self):
        nodes = [{"title": "Introduction", "page": 0, "children": []}]

        plan = hd_converter.build_chunk_plan(nodes, total_pages=5, max_pages=10)

        self.assertEqual(len(plan), 1)
        self.assertEqual(plan[0]["unit_id"], "FRONT_01")
        self.assertEqual(plan[0]["section_title"], "Introduction")

    def test_build_chunk_plan_adds_global_front_prelude(self):
        nodes = [{"title": "Contents", "page": 7, "children": []}]

        plan = hd_converter.build_chunk_plan(nodes, total_pages=10, max_pages=10)

        self.assertEqual(len(plan), 2)
        self.assertEqual(plan[0]["section_title"], "Front Matter Prelude")
        self.assertEqual(plan[0]["start_page"], 0)
        self.assertEqual(plan[0]["end_page"], 7)
        self.assertEqual(plan[1]["section_title"], "Contents")


if __name__ == "__main__":
    unittest.main()
