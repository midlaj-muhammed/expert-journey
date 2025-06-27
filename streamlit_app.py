#!/usr/bin/env python3
"""
Alternative entry point for Streamlit Cloud.
Some platforms look for streamlit_app.py as the default entry point.
"""

import sys
import os

# Setup paths for proper imports
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(current_dir, 'resume_ranker_ai')
utils_dir = os.path.join(app_dir, 'utils')

# Add all necessary paths
for path in [current_dir, app_dir, utils_dir]:
    if os.path.exists(path) and path not in sys.path:
        sys.path.insert(0, path)

# Change working directory to the app directory
if os.path.exists(app_dir):
    os.chdir(app_dir)

# Now import and run the main app
try:
    # Import the main app module
    import importlib.util
    
    app_file = os.path.join(app_dir, 'app.py')
    if os.path.exists(app_file):
        spec = importlib.util.spec_from_file_location("main_app", app_file)
        main_app = importlib.util.module_from_spec(spec)
        
        # Execute the main app
        spec.loader.exec_module(main_app)
    else:
        import streamlit as st
        st.error("❌ Main application file not found!")
        st.info("Please ensure the resume_ranker_ai/app.py file exists.")
        
except Exception as e:
    import streamlit as st
    st.error(f"❌ Error loading application: {e}")
    st.info("Please check the application structure and try again.")
