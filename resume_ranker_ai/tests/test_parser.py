import unittest
import os
from utils.document_parser import DocumentParser

class TestDocumentParser(unittest.TestCase):
    
    def test_parse_pdf(self):
        # This test assumes you have a sample PDF in the data directory
        sample_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                  'data', 'sample_resumes', 'sample_resume.pdf')
        
        # Skip test if sample file doesn't exist
        if not os.path.exists(sample_path):
            self.skipTest("Sample PDF file not found")
        
        text = DocumentParser.parse_pdf(sample_path)
        self.assertIsNotNone(text)
        self.assertTrue(len(text) > 0)
    
    def test_parse_docx(self):
        # This test assumes you have a sample DOCX in the data directory
        sample_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                  'data', 'sample_resumes', 'sample_resume.docx')
        
        # Skip test if sample file doesn't exist
        if not os.path.exists(sample_path):
            self.skipTest("Sample DOCX file not found")
        
        text = DocumentParser.parse_docx(sample_path)
        self.assertIsNotNone(text)
        self.assertTrue(len(text) > 0)

if __name__ == '__main__':
    unittest.main()