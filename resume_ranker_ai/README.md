# Expert Journey

A tool that helps job seekers optimize their resumes for specific job descriptions using Natural Language Processing (NLP).

## Features

- Upload resume in PDF or DOCX format
- Input job descriptions
- Analyze resume-job match with NLP
- Generate match percentage score
- Provide specific recommendations to improve resume
- Highlight missing keywords and skills

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/resume-ranker-ai.git
   cd resume-ranker-ai
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Download the spaCy model:
   ```
   python -m spacy download en_core_web_md
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`

3. Upload your resume (PDF or DOCX format)

4. Paste the job description

5. Click "Analyze Resume Match" to get your results

## Project Structure

- `app.py`: Main Streamlit application
- `utils/`: Utility modules
  - `document_parser.py`: PDF/DOCX parsing functionality
  - `nlp_analyzer.py`: NLP analysis and matching
  - `recommender.py`: Recommendation generation
- `data/`: Sample data for testing
- `tests/`: Basic test files

## How It Works

1. **Document Parsing**: Extracts text from PDF and DOCX files
2. **NLP Analysis**: Uses spaCy to analyze the resume and job description
3. **Matching Algorithm**: Calculates similarity score using TF-IDF and cosine similarity
4. **Recommendation Engine**: Generates tailored recommendations based on analysis

## Dependencies

- Python 3.8+
- Streamlit
- spaCy
- PyPDF2
- pdfplumber
- python-docx
- scikit-learn

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.