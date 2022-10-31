from unittest.mock import MagicMock, patch
import os
from ..ocr_files import ocr_prototype as ocr
import unittest

import os.path
from os import path

absolute_path = os.path.dirname(__file__)
relative_path1 = "../ocr_files"
full_path = os.path.join(absolute_path, relative_path1)


class TestOcrMethods(unittest.TestCase):

    # Test to verify that the ending type function works for short and long strings
    def test_ending_type(self):
        result1 = ocr.ending_type('meme.png')
        result2 = ocr.ending_type('s.pdf')
        result3 = ocr.ending_type('verylongstringtotest.tiff')
        self.assertEqual(result1, 'png')
        self.assertEqual(result2, 'pdf')
        self.assertEqual(result3, 'tiff')

    # Tests the result for trying to convert a non pdf should be none
    def test_png_conversion_with_png(self):
        result1 = ocr.png_conversion('test.png')
        result2 = ocr.png_conversion('test.tiff')
        result3 = ocr.png_conversion('test.jiff')
        result4 = ocr.png_conversion('test.xml')
        self.assertIsNone(result1)
        self.assertIsNone(result2)
        self.assertIsNone(result3)
        self.assertIsNone(result4)

    # This test is to check what happens when you run the conversion with a real pdf value
    # The return should be a list of names of the files created. The issue is that we need to possible patch
    # os so we can simulate the files being opened so it can run the script. I am not very sure how to do this
    # but i'll try.
    # @patch.object(os.system, None)
    # def test_png_conversion_with_pdf(self):
    #   self.assertIsNotNone(ocr.png_conversion('test.pdf'))

    # Tests the ocr run function and makes sure the output matches expected
    def test_run_ocr(self):
        calulated_result = ocr.run_ocr(['web/ocr_files/test_image.png'])
        expected_result = ['This is a lot of 12 point text to test the\nocr code and see if it works on all types\nof file format.\n\nThe quick brown dog jumped over the\nlazy fox. The quick brown dog jumped\nover the lazy fox. The quick brown dog\njumped over the lazy fox. The quick\nbrown dog jumped over the lazy fox.\n']
        self.assertEqual(calulated_result,expected_result)

if __name__ == '__main__':
    unittest.main()
