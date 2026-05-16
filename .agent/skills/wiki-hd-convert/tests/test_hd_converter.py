import os
import shutil
import unittest

from scripts.hd_converter import convert_pdf_to_hd_markdown


class TestHDConverter(unittest.TestCase):
    def setUp(self):
        self.test_pdf = "00_Inbox/VIZ_10_Visualization_Tips.pdf"
        self.output_root = "00_Inbox/Converted_Sources/TEST_HD"
        if os.path.exists(self.output_root):
            shutil.rmtree(self.output_root)

    def test_conversion_success(self):
        """Test if conversion creates the expected files and image links."""
        output_path = convert_pdf_to_hd_markdown(self.test_pdf, self.output_root)

        self.assertTrue(os.path.exists(output_path), "Markdown file was not created.")

        base_name = os.path.splitext(os.path.basename(self.test_pdf))[0]
        image_dir = os.path.join(self.output_root, base_name, "images")
        self.assertTrue(os.path.exists(image_dir), "Image directory was not created.")

        images = os.listdir(image_dir)
        self.assertGreater(len(images), 0, "No images were extracted.")

        with open(output_path, "r", encoding="utf-8") as handle:
            content = handle.read()
            self.assertIn("![[", content, "Markdown missing image wikilinks.")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
