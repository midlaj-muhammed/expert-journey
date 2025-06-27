# 🚀 Expert Journey

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.15%2B-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![spaCy](https://img.shields.io/badge/spaCy-3.4%2B-orange.svg)](https://spacy.io/)

An intelligent AI-powered tool that helps job seekers optimize their resumes for specific job descriptions using advanced Natural Language Processing (NLP) and machine learning techniques.

## 🎯 Project Overview

Expert Journey analyzes your resume against job descriptions to provide:
- **Match Score**: Percentage compatibility between your resume and job requirements
- **Missing Keywords**: Important terms from job descriptions that are absent in your resume
- **Personalized Recommendations**: AI-generated suggestions to improve your resume
- **Instant Analysis**: Real-time feedback to optimize your job application success

Perfect for job seekers, career coaches, and HR professionals looking to streamline the resume optimization process.

## ✨ Key Features

### 📄 **Document Processing**
- **Multi-format Support**: Upload resumes in PDF or DOCX format
- **Intelligent Text Extraction**: Advanced parsing for clean text extraction
- **Error Handling**: Robust processing for various document formats

### 🤖 **AI-Powered Analysis**
- **Match Scoring**: Sophisticated algorithm calculating resume-job compatibility (0-100%)
- **Keyword Analysis**: Identifies missing critical keywords from job descriptions
- **Semantic Understanding**: Uses spaCy's advanced NLP for context-aware analysis
- **Skills Gap Detection**: Highlights areas for improvement

### 🎨 **User Experience**
- **Interactive Web Interface**: Clean, intuitive Streamlit-based UI
- **Real-time Results**: Instant analysis and feedback
- **Visual Score Display**: Color-coded match scores with progress bars
- **Mobile Responsive**: Works seamlessly across devices

### 📋 **Sample Job Library**
- **20+ Professional Job Descriptions** across 4 major categories:
  - 💻 **Technology** (10 roles): Software Engineer, Data Scientist, DevOps Engineer, etc.
  - 🎨 **Design & Creative** (4 roles): UX/UI Designer, Graphic Designer, etc.
  - 📈 **Business & Management** (6 roles): Product Manager, Business Analyst, etc.
  - 📢 **Marketing & Sales** (4 roles): Digital Marketing Manager, Sales Rep, etc.
- **Random Job Generator**: Quick testing with random sample descriptions
- **Editable Samples**: Customize sample jobs to match specific requirements

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/midlaj-muhammed/expert-journey.git
   cd expert-journey
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r resume_ranker_ai/requirements.txt
   ```

4. **Download spaCy Language Model**
   ```bash
   python -m spacy download en_core_web_md
   ```

## 📖 Usage Guide

### Running the Application

1. **Start the Streamlit Server**
   ```bash
   streamlit run resume_ranker_ai/app.py
   ```

2. **Access the Application**
   - Open your web browser
   - Navigate to `http://localhost:8501`

### Using the Features

1. **Upload Your Resume**
   - Click "Browse files" in the left column
   - Select your PDF or DOCX resume file
   - Wait for successful upload confirmation

2. **Choose Job Description**
   - **Option A**: Select from 20+ sample jobs using the dropdown
   - **Option B**: Click "🎲 Random Job" for quick testing
   - **Option C**: Choose "Custom" and paste your own job description

3. **Analyze & Optimize**
   - Click "Analyze Resume Match"
   - Review your match score and recommendations
   - Identify missing keywords highlighted in red
   - Implement suggested improvements

## 🛠️ Technology Stack

### Core Technologies
- **[Streamlit](https://streamlit.io/)**: Web application framework
- **[spaCy](https://spacy.io/)**: Advanced NLP and text processing
- **[scikit-learn](https://scikit-learn.org/)**: Machine learning algorithms
- **[Python](https://python.org/)**: Primary programming language

### Document Processing
- **[PyPDF2](https://pypdf2.readthedocs.io/)**: PDF text extraction
- **[pdfplumber](https://github.com/jsvine/pdfplumber)**: Enhanced PDF parsing
- **[python-docx](https://python-docx.readthedocs.io/)**: Microsoft Word document processing

### Analysis & Algorithms
- **TF-IDF Vectorization**: Text feature extraction
- **Cosine Similarity**: Document similarity calculation
- **Named Entity Recognition**: Skill and keyword identification
- **Semantic Analysis**: Context-aware text understanding

## 📁 Project Structure

```
expert-journey/
├── resume_ranker_ai/
│   ├── app.py                 # Main Streamlit application
│   ├── requirements.txt       # Python dependencies
│   ├── utils/                 # Core utility modules
│   │   ├── __init__.py
│   │   ├── document_parser.py # PDF/DOCX parsing logic
│   │   ├── nlp_analyzer.py    # NLP analysis and matching
│   │   └── recommender.py     # Recommendation generation
│   ├── data/                  # Sample data and test files
│   └── tests/                 # Unit tests and test cases
├── venv/                      # Virtual environment (created after setup)
├── README.md                  # Project documentation
└── LICENSE                    # MIT License file
```

## 🔧 How It Works

### 1. **Document Processing Pipeline**
- Extracts clean text from uploaded PDF/DOCX files
- Handles various document formats and encoding issues
- Preprocesses text for optimal NLP analysis

### 2. **NLP Analysis Engine**
- Tokenizes and processes both resume and job description text
- Applies advanced spaCy language models for semantic understanding
- Identifies key skills, technologies, and requirements

### 3. **Matching Algorithm**
- Converts text to TF-IDF vectors for numerical representation
- Calculates cosine similarity between resume and job description
- Generates percentage match score (0-100%)

### 4. **Recommendation System**
- Analyzes gaps between resume content and job requirements
- Identifies missing keywords and skills
- Provides actionable suggestions for resume improvement

## 📸 Screenshots

*Coming Soon: Application interface screenshots will be added to showcase the user experience.*

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute
- 🐛 **Bug Reports**: Found an issue? Please report it!
- 💡 **Feature Requests**: Have ideas for new features?
- 📝 **Documentation**: Help improve our docs
- 🧪 **Testing**: Add test cases and improve coverage
- 🎨 **UI/UX**: Enhance the user interface and experience

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Ensure all tests pass
5. Submit a pull request with a clear description

### Code Style
- Follow PEP 8 Python style guidelines
- Add docstrings to functions and classes
- Include type hints where appropriate
- Write meaningful commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **spaCy Team**: For the excellent NLP library
- **Streamlit Team**: For the amazing web app framework
- **Open Source Community**: For the various libraries that make this project possible

## 📞 Support

- 📧 **Email**: [midlajvalappil@gmail.com]
- 🐛 **Issues**: [GitHub Issues](https://github.com/midlaj-muhammed/expert-journey/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/midlaj-muhammed/expert-journey/discussions)

---

**Made with ❤️ for job seekers worldwide**

*Star ⭐ this repository if you find it helpful!*

