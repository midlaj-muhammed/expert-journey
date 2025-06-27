#!/bin/bash

echo "🚀 Setting up Expert Journey..."

# Update pip to latest version
python -m pip install --upgrade pip

# Install spaCy models with multiple fallback methods
echo "📥 Installing spaCy language models..."

# Method 1: Direct spaCy download
python -m spacy download en_core_web_sm || echo "Method 1 failed"

# Method 2: Try medium model
python -m spacy download en_core_web_md || echo "Medium model not available"

# Method 3: Direct pip install with URL
python -m pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl || echo "Method 3 failed"

# Method 4: Alternative URL
python -m pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.6.0/en_core_web_sm-3.6.0-py3-none-any.whl || echo "Method 4 failed"

# Verify installation
echo "🔍 Verifying spaCy model installation..."
python -c "import spacy; nlp = spacy.load('en_core_web_sm'); print('✅ en_core_web_sm loaded successfully')" || \
python -c "import spacy; nlp = spacy.load('en_core_web_md'); print('✅ en_core_web_md loaded successfully')" || \
echo "⚠️ No spaCy models available - app will run in basic mode"

echo "✅ Setup complete!"
