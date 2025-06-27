import PyPDF2
import pdfplumber
import docx
import os

class DocumentParser:
    """Parse PDF and DOCX documents to extract text content."""
    
    @staticmethod
    def parse_pdf(file_path):
        """Extract text from PDF files using pdfplumber for better text extraction."""
        text = ""
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
            
            # If pdfplumber fails to extract text, try PyPDF2 as fallback
            if not text.strip():
                with open(file_path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    for page_num in range(len(reader.pages)):
                        text += reader.pages[page_num].extract_text() or ""
        except Exception as e:
            print(f"Error parsing PDF: {e}")
            return None
        
        return text.strip()
    
    @staticmethod
    def parse_docx(file_path):
        """Extract text from DOCX files."""
        try:
            doc = docx.Document(file_path)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            return text.strip()
        except Exception as e:
            print(f"Error parsing DOCX: {e}")
            return None
    
    @staticmethod
    def parse_document(file_path):
        """Parse document based on file extension."""
        _, file_extension = os.path.splitext(file_path)
        
        if file_extension.lower() == '.pdf':
            return DocumentParser.parse_pdf(file_path)
        elif file_extension.lower() == '.docx':
            return DocumentParser.parse_docx(file_path)
        else:
            print(f"Unsupported file format: {file_extension}")
            return None