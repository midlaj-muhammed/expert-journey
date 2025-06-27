#!/usr/bin/env python3
"""
Test script to verify all imports work correctly.
"""

import sys
import os

# Add the resume_ranker_ai directory to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(current_dir, 'resume_ranker_ai')
utils_dir = os.path.join(app_dir, 'utils')

print(f"Current directory: {current_dir}")
print(f"App directory: {app_dir}")
print(f"Utils directory: {utils_dir}")

# Add directories to Python path
sys.path.insert(0, app_dir)
sys.path.insert(0, utils_dir)

print("\nTesting imports...")

try:
    print("1. Testing direct imports...")
    from utils.document_parser import DocumentParser
    from utils.nlp_analyzer import NLPAnalyzer
    from utils.recommender import ResumeRecommender
    print("✅ Direct imports successful")
except ImportError as e:
    print(f"❌ Direct imports failed: {e}")
    
    try:
        print("2. Testing fallback imports...")
        import document_parser
        import nlp_analyzer
        import recommender
        DocumentParser = document_parser.DocumentParser
        NLPAnalyzer = nlp_analyzer.NLPAnalyzer
        ResumeRecommender = recommender.ResumeRecommender
        print("✅ Fallback imports successful")
    except ImportError as e:
        print(f"❌ Fallback imports failed: {e}")
        sys.exit(1)

print("\nTesting class instantiation...")

try:
    # Test NLPAnalyzer
    nlp_analyzer = NLPAnalyzer()
    print("✅ NLPAnalyzer instantiated successfully")
    
    # Test DocumentParser
    doc_parser = DocumentParser()
    print("✅ DocumentParser instantiated successfully")
    
    # Test ResumeRecommender
    recommender = ResumeRecommender(nlp_analyzer)
    print("✅ ResumeRecommender instantiated successfully")
    
    print("\n🎉 All tests passed! The app should work correctly.")
    
except Exception as e:
    print(f"❌ Error during instantiation: {e}")
    sys.exit(1)
