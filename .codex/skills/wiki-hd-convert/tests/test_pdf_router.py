import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add scripts to path
sys.path.append(str(Path(__file__).parent.parent / "scripts"))
import pdf_router

class TestPdfRouter(unittest.TestCase):
    def setUp(self):
        self.test_pdf = "router_test.pdf"
        self.test_output = "router_output"
        if not os.path.exists(self.test_output):
            os.makedirs(self.test_output)

    def tearDown(self):
        import shutil
        if os.path.exists(self.test_pdf): os.remove(self.test_pdf)
        if os.path.exists(self.test_output): shutil.rmtree(self.test_output)

    @patch("pdf_router.get_pdf_signals")
    @patch("pdf_router.pymupdf_convert")
    def test_text_pdf_routing(self, mock_pymupdf, mock_signals):
        # sparse_ratio=0.1, avg_images=0.5 -> TEXT
        mock_signals.return_value = (0.1, 0.5, 100)
        mock_pymupdf.return_value = "fake_output.md"
        
        pdf_router.route_and_convert("dummy.pdf", self.test_output)
        
        mock_pymupdf.assert_called_once()

    @patch("pdf_router.get_pdf_signals")
    @patch("pdf_router.docling_convert")
    def test_scanned_pdf_routing(self, mock_docling, mock_signals):
        # sparse_ratio=0.8 -> SCANNED
        mock_signals.return_value = (0.8, 0, 100)
        mock_docling.return_value = "fake_output.md"
        
        pdf_router.route_and_convert("dummy.pdf", self.test_output)
        
        mock_docling.assert_called_once()

    @patch("pdf_router.get_pdf_signals")
    @patch("pdf_router.docling_convert")
    def test_chart_heavy_routing(self, mock_docling, mock_signals):
        # sparse_ratio=0.1, avg_images=5 -> CHART-HEAVY
        mock_signals.return_value = (0.1, 5.0, 100)
        mock_docling.return_value = "fake_output.md"
        
        pdf_router.route_and_convert("dummy.pdf", self.test_output)
        
        mock_docling.assert_called_once()

    @patch("pdf_router.get_pdf_signals")
    @patch("pdf_router.pymupdf_convert")
    def test_docling_unavailable_fallback(self, mock_pymupdf, mock_signals):
        # sparse_ratio=0.8 (SCANNED) but docling missing
        mock_signals.return_value = (0.8, 0, 100)
        mock_pymupdf.return_value = "fake_output.md"
        
        with patch("builtins.__import__", side_effect=lambda name, *args, **kwargs: 
                   (MagicMock() if name != "docling" else exec("raise ImportError"))):
            pdf_router.route_and_convert("dummy.pdf", self.test_output)
        
        # Should fall back to pymupdf
        mock_pymupdf.assert_called()

if __name__ == "__main__":
    unittest.main()
