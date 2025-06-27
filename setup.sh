#!/bin/bash

# Download spaCy language model
python -m spacy download en_core_web_sm

# Alternative: try to download the medium model if available
python -m spacy download en_core_web_md || echo "Medium model not available, using small model"
