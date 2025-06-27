#!/usr/bin/env python3
"""
Main entry point for Expert Journey application.
This file handles import issues and ensures the app runs correctly in all environments.
"""

import sys
import os

# Ensure the correct paths are in sys.path
def setup_paths():
    """Setup Python paths for proper module imports."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Add current directory
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    
    # Add resume_ranker_ai directory
    app_dir = os.path.join(current_dir, 'resume_ranker_ai')
    if os.path.exists(app_dir) and app_dir not in sys.path:
        sys.path.insert(0, app_dir)
    
    # Add utils directory
    utils_dir = os.path.join(app_dir, 'utils')
    if os.path.exists(utils_dir) and utils_dir not in sys.path:
        sys.path.insert(0, utils_dir)

# Setup paths before any imports
setup_paths()

# Now run the main app
if __name__ == "__main__":
    # Change to the resume_ranker_ai directory
    app_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resume_ranker_ai')
    if os.path.exists(app_dir):
        os.chdir(app_dir)
    
    # Import and run the app
    import subprocess
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"] + sys.argv[1:])
