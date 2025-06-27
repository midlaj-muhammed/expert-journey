"""
Utils package for Expert Journey application.
Contains document parsing, NLP analysis, and recommendation modules.
"""

# Import all main classes for easier access
try:
    from .document_parser import DocumentParser
    from .nlp_analyzer import NLPAnalyzer
    from .recommender import ResumeRecommender

    __all__ = ['DocumentParser', 'NLPAnalyzer', 'ResumeRecommender']
except ImportError as e:
    # Fallback for environments where relative imports don't work
    import sys
    import os

    # Add current directory to path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)

    try:
        import document_parser
        import nlp_analyzer
        import recommender

        DocumentParser = document_parser.DocumentParser
        NLPAnalyzer = nlp_analyzer.NLPAnalyzer
        ResumeRecommender = recommender.ResumeRecommender

        __all__ = ['DocumentParser', 'NLPAnalyzer', 'ResumeRecommender']
    except ImportError:
        # If all imports fail, at least make the package importable
        __all__ = []