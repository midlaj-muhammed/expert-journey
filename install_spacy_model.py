#!/usr/bin/env python3
"""
Script to ensure spaCy models are installed before running the app.
This script will be called automatically when the app starts.
"""

import subprocess
import sys
import spacy
from spacy.cli import download
import os

def install_spacy_model():
    """Install spaCy model with multiple fallback methods."""
    
    models_to_try = ["en_core_web_sm", "en_core_web_md"]
    
    # First check if any model is already available
    for model_name in ["en_core_web_md", "en_core_web_sm", "en_core_web_lg"]:
        try:
            spacy.load(model_name)
            print(f"✅ spaCy model {model_name} is already available")
            return True
        except OSError:
            continue
    
    print("📥 No spaCy models found. Installing...")
    
    # Try to install models
    for model_name in models_to_try:
        print(f"🔄 Attempting to install {model_name}...")
        
        # Method 1: Using spacy.cli.download
        try:
            download(model_name)
            # Test if it loads
            spacy.load(model_name)
            print(f"✅ Successfully installed {model_name} using spacy.cli.download")
            return True
        except Exception as e:
            print(f"❌ Method 1 failed for {model_name}: {e}")
        
        # Method 2: Using subprocess with spacy download
        try:
            subprocess.check_call([
                sys.executable, "-m", "spacy", "download", model_name
            ])
            # Test if it loads
            spacy.load(model_name)
            print(f"✅ Successfully installed {model_name} using subprocess")
            return True
        except Exception as e:
            print(f"❌ Method 2 failed for {model_name}: {e}")
        
        # Method 3: Using pip install with direct URL
        try:
            # Get the latest version URL (this is a common pattern)
            model_url = f"https://github.com/explosion/spacy-models/releases/download/{model_name}-3.7.1/{model_name}-3.7.1-py3-none-any.whl"
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", model_url
            ])
            # Test if it loads
            spacy.load(model_name)
            print(f"✅ Successfully installed {model_name} using pip with URL")
            return True
        except Exception as e:
            print(f"❌ Method 3 failed for {model_name}: {e}")
        
        # Method 4: Using pip install directly
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", model_name
            ])
            # Test if it loads
            spacy.load(model_name)
            print(f"✅ Successfully installed {model_name} using direct pip install")
            return True
        except Exception as e:
            print(f"❌ Method 4 failed for {model_name}: {e}")
    
    print("⚠️ All installation methods failed. App will run in basic mode.")
    return False

if __name__ == "__main__":
    install_spacy_model()
