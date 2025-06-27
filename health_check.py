#!/usr/bin/env python3
"""
Health check script for Streamlit Cloud deployment.
This script verifies that all components are working correctly.
"""

import sys
import os

def health_check():
    """Perform comprehensive health check."""
    print("🏥 Expert Journey - Health Check")
    print("=" * 40)
    
    checks_passed = 0
    total_checks = 0
    
    # Check 1: Python version
    total_checks += 1
    print(f"🐍 Python version: {sys.version}")
    if sys.version_info >= (3, 8):
        print("✅ Python version OK")
        checks_passed += 1
    else:
        print("❌ Python version too old")
    
    # Check 2: Required packages
    total_checks += 1
    try:
        import streamlit
        import spacy
        import sklearn
        import PyPDF2
        import docx
        import pdfplumber
        print("✅ All required packages available")
        checks_passed += 1
    except ImportError as e:
        print(f"❌ Missing package: {e}")
    
    # Check 3: Utility modules
    total_checks += 1
    try:
        from utils.document_parser import DocumentParser
        from utils.nlp_analyzer import NLPAnalyzer
        from utils.recommender import ResumeRecommender
        print("✅ Utility modules importable")
        checks_passed += 1
    except ImportError as e:
        print(f"❌ Utility import error: {e}")
    
    # Check 4: spaCy model
    total_checks += 1
    try:
        import spacy
        models_available = []
        for model_name in ['en_core_web_sm', 'en_core_web_md']:
            try:
                nlp = spacy.load(model_name)
                models_available.append(model_name)
            except OSError:
                continue
        
        if models_available:
            print(f"✅ spaCy models available: {', '.join(models_available)}")
            checks_passed += 1
        else:
            print("⚠️ No spaCy models available (will run in basic mode)")
            checks_passed += 0.5  # Partial credit
    except Exception as e:
        print(f"❌ spaCy check failed: {e}")
    
    # Check 5: File structure
    total_checks += 1
    required_files = ['app.py', 'utils/', 'data/']
    missing_files = []
    
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if not missing_files:
        print("✅ File structure complete")
        checks_passed += 1
    else:
        print(f"❌ Missing files: {', '.join(missing_files)}")
    
    # Summary
    print("\n" + "=" * 40)
    success_rate = (checks_passed / total_checks) * 100
    print(f"📊 Health Check Results: {checks_passed}/{total_checks} ({success_rate:.1f}%)")
    
    if success_rate >= 80:
        print("🎉 System healthy - ready for deployment!")
        return True
    elif success_rate >= 60:
        print("⚠️ System partially healthy - may have limited functionality")
        return True
    else:
        print("❌ System unhealthy - deployment may fail")
        return False

if __name__ == "__main__":
    success = health_check()
    sys.exit(0 if success else 1)
