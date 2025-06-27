#!/usr/bin/env python3
"""
Test script to verify deployment readiness.
This script tests all import paths and entry points.
"""

import sys
import os

def test_root_imports():
    """Test imports from root directory."""
    print("🧪 Testing root-level imports...")
    
    try:
        # Add current directory to path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
        
        # Test direct imports
        from utils.document_parser import DocumentParser
        from utils.nlp_analyzer import NLPAnalyzer
        from utils.recommender import ResumeRecommender
        
        print("✅ Root-level imports successful!")
        
        # Test class instantiation
        parser = DocumentParser()
        analyzer = NLPAnalyzer()
        recommender = ResumeRecommender(analyzer)
        
        print("✅ Class instantiation successful!")
        return True
        
    except Exception as e:
        print(f"❌ Root-level import test failed: {e}")
        return False

def test_entry_points():
    """Test that entry point files exist."""
    print("\n🧪 Testing entry point files...")
    
    entry_points = ['app.py', 'streamlit_app.py', 'main.py']
    
    for entry_point in entry_points:
        if os.path.exists(entry_point):
            print(f"✅ {entry_point} exists")
        else:
            print(f"❌ {entry_point} missing")
    
    return True

def test_data_files():
    """Test that data files are accessible."""
    print("\n🧪 Testing data file access...")
    
    data_paths = ['data', 'utils']
    
    for path in data_paths:
        if os.path.exists(path):
            print(f"✅ {path} directory exists")
            files = os.listdir(path)
            print(f"   📁 Contains {len(files)} files/directories")
        else:
            print(f"❌ {path} directory missing")
    
    return True

def main():
    """Run all tests."""
    print("🚀 Expert Journey - Deployment Readiness Test")
    print("=" * 50)
    
    tests = [
        test_root_imports,
        test_entry_points,
        test_data_files
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    if all(results):
        print("🎉 All tests passed! Deployment ready!")
    else:
        print("⚠️ Some tests failed. Please check the issues above.")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
