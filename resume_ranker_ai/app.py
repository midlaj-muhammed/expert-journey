import streamlit as st
import os
import tempfile
import sys
import subprocess

# Check if we should redirect to root-level app
def check_redirect():
    """Check if we should redirect to the root-level app."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    root_app = os.path.join(parent_dir, 'app.py')

    # If we're in a subdirectory and root app exists, show redirect message
    if os.path.exists(root_app) and os.path.basename(current_dir) == 'resume_ranker_ai':
        st.info("🔄 **Note**: This app should be run from the root directory for optimal compatibility.")
        st.info("If you're experiencing issues, please use the root-level app.py file.")

# Setup Python path for imports
def setup_imports():
    """Setup imports with multiple fallback methods."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    utils_dir = os.path.join(current_dir, 'utils')

    # Add directories to Python path
    for path in [current_dir, parent_dir, utils_dir]:
        if path not in sys.path:
            sys.path.insert(0, path)

    # Try multiple import strategies
    try:
        # Strategy 1: Relative imports
        from utils.document_parser import DocumentParser
        from utils.nlp_analyzer import NLPAnalyzer
        from utils.recommender import ResumeRecommender
        return DocumentParser, NLPAnalyzer, ResumeRecommender
    except ImportError:
        try:
            # Strategy 2: Direct imports
            import document_parser
            import nlp_analyzer
            import recommender
            return document_parser.DocumentParser, nlp_analyzer.NLPAnalyzer, recommender.ResumeRecommender
        except ImportError:
            try:
                # Strategy 3: Absolute imports from utils
                sys.path.insert(0, os.path.join(current_dir, 'utils'))
                from document_parser import DocumentParser
                from nlp_analyzer import NLPAnalyzer
                from recommender import ResumeRecommender
                return DocumentParser, NLPAnalyzer, ResumeRecommender
            except ImportError as e:
                st.error(f"❌ Failed to import required modules: {e}")
                st.error(f"Current directory: {current_dir}")
                st.error(f"Python path: {sys.path[:3]}...")
                st.info("Please check that all utility modules are in the correct location.")
                st.stop()

# Import the classes
DocumentParser, NLPAnalyzer, ResumeRecommender = setup_imports()

# Check for redirect (show info but continue)
check_redirect()

# Ensure spaCy model is installed before proceeding
def ensure_spacy_model():
    """Ensure spaCy model is available before starting the app."""
    try:
        # Try to run the installation script
        script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "install_spacy_model.py")
        if os.path.exists(script_path):
            subprocess.run([sys.executable, script_path], check=False, capture_output=True)
    except Exception as e:
        print(f"Warning: Could not run spaCy installation script: {e}")

# Run spaCy model check
ensure_spacy_model()

# Set page configuration
st.set_page_config(
    page_title="Expert Journey - AI Resume Optimizer",
    page_icon="🚀",
    layout="wide"
)

# Initialize NLP components
@st.cache_resource
def load_nlp_components():
    progress_bar = st.progress(0)
    status_text = st.empty()

    try:
        status_text.text("🔄 Initializing AI components...")
        progress_bar.progress(25)

        status_text.text("📥 Loading NLP models (this may take a moment on first run)...")
        progress_bar.progress(50)

        nlp_analyzer = NLPAnalyzer()
        progress_bar.progress(75)

        status_text.text("🤖 Setting up recommendation engine...")
        recommender = ResumeRecommender(nlp_analyzer)
        progress_bar.progress(100)

        if nlp_analyzer.nlp:
            status_text.text("✅ All AI components loaded successfully!")
        else:
            status_text.text("⚠️ Running in basic mode - some features may be limited")

        # Clear progress indicators after a short delay
        import time
        time.sleep(1)
        progress_bar.empty()
        status_text.empty()

        return nlp_analyzer, recommender

    except Exception as e:
        progress_bar.empty()
        status_text.empty()
        raise e

# Load components with error handling
try:
    nlp_analyzer, recommender = load_nlp_components()

    # Only show warning if spaCy model is not available
    if not nlp_analyzer.nlp:
        st.info("ℹ️ **Note**: Running in basic mode. The app is fully functional, but some advanced NLP features are simplified. To enable full functionality, spaCy models need to be installed.")

except Exception as e:
    st.error(f"❌ Error loading AI components: {str(e)}")
    st.info("Please refresh the page or contact support if the issue persists.")
    st.stop()

# Sample job descriptions
SAMPLE_JOBS = {
    "Software Engineer": """We are seeking a skilled Software Engineer to join our development team. The ideal candidate will have experience with Python, JavaScript, React, Node.js, and SQL databases. You should be familiar with agile development methodologies, version control systems like Git, and cloud platforms such as AWS or Azure. Experience with Docker, Kubernetes, and CI/CD pipelines is a plus. Strong problem-solving skills and ability to work in a collaborative environment are essential.""",

    "Data Scientist": """Looking for a Data Scientist with expertise in machine learning, statistical analysis, and data visualization. Required skills include Python, R, SQL, pandas, scikit-learn, TensorFlow, and Tableau. Experience with big data technologies like Spark, Hadoop, and cloud platforms (AWS, GCP, Azure) is preferred. Strong background in statistics, mathematics, and experience with A/B testing and predictive modeling.""",

    "Product Manager": """Seeking an experienced Product Manager to drive product strategy and roadmap. Ideal candidate has experience with product lifecycle management, user research, market analysis, and cross-functional team leadership. Familiarity with agile methodologies, JIRA, analytics tools, and customer feedback systems. Strong communication skills and ability to translate business requirements into technical specifications.""",

    "Digital Marketing Manager": """We need a Digital Marketing Manager with expertise in SEO, SEM, social media marketing, content marketing, and email campaigns. Experience with Google Analytics, Google Ads, Facebook Ads, HubSpot, and marketing automation tools. Strong analytical skills and experience with A/B testing, conversion optimization, and ROI analysis.""",

    "UX/UI Designer": """Looking for a creative UX/UI Designer with experience in user-centered design, wireframing, prototyping, and visual design. Proficiency in Figma, Sketch, Adobe Creative Suite, and design systems. Experience with user research, usability testing, and responsive design. Strong portfolio demonstrating mobile and web design projects.""",

    "DevOps Engineer": """Seeking a DevOps Engineer with experience in infrastructure automation, containerization, and cloud technologies. Required skills include Docker, Kubernetes, Jenkins, Terraform, AWS/Azure/GCP, Linux, and scripting languages (Python, Bash). Experience with monitoring tools, CI/CD pipelines, and infrastructure as code.""",

    "Business Analyst": """We are hiring a Business Analyst to bridge the gap between business needs and technical solutions. Experience with requirements gathering, process mapping, data analysis, and stakeholder management. Proficiency in SQL, Excel, Tableau, and project management tools. Strong analytical and communication skills required.""",

    "Cybersecurity Analyst": """Looking for a Cybersecurity Analyst to protect our organization's digital assets. Experience with security frameworks, threat analysis, incident response, and vulnerability assessment. Knowledge of firewalls, SIEM tools, penetration testing, and compliance standards (ISO 27001, NIST). Security certifications preferred.""",

    "Sales Representative": """Seeking a motivated Sales Representative to drive revenue growth. Experience with CRM systems, lead generation, cold calling, and relationship building. Strong negotiation skills and track record of meeting sales targets. Knowledge of sales methodologies and customer acquisition strategies.""",

    "Human Resources Manager": """We need an HR Manager to oversee recruitment, employee relations, and HR policies. Experience with HRIS systems, talent acquisition, performance management, and employment law. Strong interpersonal skills and experience with diversity and inclusion initiatives.""",

    "Financial Analyst": """Looking for a Financial Analyst with expertise in financial modeling, budgeting, and forecasting. Proficiency in Excel, SQL, and financial software. Experience with variance analysis, financial reporting, and investment analysis. CFA or similar certification preferred.""",

    "Project Manager": """Seeking an experienced Project Manager with PMP certification. Experience with project planning, resource management, risk assessment, and stakeholder communication. Proficiency in project management tools like Microsoft Project, JIRA, and Asana. Strong leadership and organizational skills.""",

    "Content Writer": """We are hiring a Content Writer to create engaging content across multiple channels. Experience with SEO writing, blog posts, social media content, and email marketing. Strong research skills and ability to adapt writing style for different audiences. Knowledge of content management systems and analytics tools.""",

    "Mobile App Developer": """Looking for a Mobile App Developer with experience in iOS and Android development. Proficiency in Swift, Kotlin, React Native, or Flutter. Experience with mobile UI/UX principles, API integration, and app store deployment. Knowledge of mobile testing frameworks and performance optimization.""",

    "Cloud Architect": """Seeking a Cloud Architect to design and implement cloud infrastructure solutions. Expertise in AWS, Azure, or GCP services. Experience with microservices architecture, serverless computing, and cloud security. Strong background in system design and scalability planning.""",

    "Quality Assurance Engineer": """We need a QA Engineer with experience in manual and automated testing. Proficiency in testing frameworks, bug tracking tools, and test case design. Experience with Selenium, API testing, and performance testing. Strong attention to detail and analytical skills.""",

    "Graphic Designer": """Looking for a creative Graphic Designer with expertise in brand design, print design, and digital graphics. Proficiency in Adobe Creative Suite, typography, and color theory. Strong portfolio showcasing diverse design projects and brand identity work.""",

    "Operations Manager": """Seeking an Operations Manager to optimize business processes and improve efficiency. Experience with process improvement, supply chain management, and team leadership. Strong analytical skills and experience with operational metrics and KPIs.""",

    "Customer Success Manager": """We are hiring a Customer Success Manager to ensure customer satisfaction and retention. Experience with customer onboarding, account management, and relationship building. Strong communication skills and experience with CRM systems and customer analytics.""",

    "Machine Learning Engineer": """Looking for an ML Engineer with experience in deploying machine learning models to production. Proficiency in Python, TensorFlow, PyTorch, and MLOps tools. Experience with model optimization, A/B testing, and cloud ML platforms. Strong software engineering background.""",

    "Network Administrator": """Seeking a Network Administrator to manage and maintain network infrastructure. Experience with routers, switches, firewalls, and network protocols. Knowledge of network security, troubleshooting, and performance monitoring. Relevant certifications preferred.""",

    "Social Media Manager": """We need a Social Media Manager to develop and execute social media strategies. Experience with content creation, community management, and social media analytics. Proficiency in social media platforms and scheduling tools. Strong creative and analytical skills.""",

    "Database Administrator": """Looking for a DBA with experience in database design, optimization, and maintenance. Proficiency in SQL, database management systems (MySQL, PostgreSQL, Oracle), and backup/recovery procedures. Experience with performance tuning and security management.""",

    "Technical Writer": """Seeking a Technical Writer to create clear and comprehensive documentation. Experience with API documentation, user manuals, and technical guides. Strong writing skills and ability to translate complex technical concepts into user-friendly content."""
}

# App title and description
st.title("🚀 Expert Journey")
st.markdown("""
<div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
    <h4 style="color: #1f4e79; margin-top: 0;">🎯 Navigate Your Career Path with AI</h4>
    <p style="color: #2c3e50; margin-bottom: 0;">
        Upload your resume, paste a job description, and get AI-powered insights to accelerate your expert journey!
    </p>
</div>
""", unsafe_allow_html=True)

# Create columns for input
col1, col2 = st.columns(2)

with col1:
    st.subheader("Upload Your Resume")
    uploaded_resume = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    
    if uploaded_resume:
        # Save uploaded file to temp location
        temp_dir = tempfile.TemporaryDirectory()
        file_path = os.path.join(temp_dir.name, uploaded_resume.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_resume.getbuffer())
        
        # Parse the document
        resume_text = DocumentParser.parse_document(file_path)
        
        if resume_text:
            st.success(f"Resume uploaded successfully: {uploaded_resume.name}")
            with st.expander("Preview Resume Text"):
                st.text_area("Extracted Text", resume_text, height=300)
        else:
            st.error("Failed to extract text from the resume. Please try another file.")

with col2:
    st.subheader("Enter Job Description")

    # Sample job selector
    st.markdown("**Quick Start:** Choose a sample job description or paste your own")

    col2a, col2b = st.columns([2, 1])

    with col2a:
        selected_job = st.selectbox(
            "Select a sample job description:",
            ["Custom (paste your own)"] + list(SAMPLE_JOBS.keys()),
            index=0
        )

    with col2b:
        if st.button("🎲 Random Job", help="Pick a random sample job"):
            import random
            random_job = random.choice(list(SAMPLE_JOBS.keys()))
            st.session_state.selected_job = random_job
            selected_job = random_job

    # Handle session state for random selection
    if 'selected_job' in st.session_state and st.session_state.selected_job != "Custom (paste your own)":
        selected_job = st.session_state.selected_job

    # Job description text area
    if selected_job == "Custom (paste your own)":
        job_description = st.text_area("Paste the job description here", height=300)
    else:
        job_description = st.text_area(
            f"Job description for {selected_job}:",
            value=SAMPLE_JOBS[selected_job],
            height=300
        )
        st.info(f"💡 You can edit this sample job description or select 'Custom' to paste your own.")

# Analysis button
if st.button("Analyze Resume Match"):
    if not uploaded_resume:
        st.warning("Please upload your resume first.")
    elif not job_description:
        st.warning("Please enter a job description.")
    else:
        with st.spinner("Analyzing your resume against the job description..."):
            # Calculate match score
            match_score = nlp_analyzer.calculate_match_score(resume_text, job_description)
            
            # Generate recommendations
            recommendations = recommender.generate_recommendations(resume_text, job_description)
            
            # Display results
            st.subheader("Analysis Results")
            
            # Create columns for results
            score_col, rec_col = st.columns([1, 2])
            
            with score_col:
                # Display match score with improved styling
                score_color = '#28a745' if match_score >= 70 else '#ffc107' if match_score >= 50 else '#dc3545'
                st.markdown(f"""
                <div style="text-align: center; background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    <h3 style="color: #2c3e50; margin-bottom: 10px;">🎯 Match Score</h3>
                    <div style="font-size: 4rem; font-weight: bold; color: {score_color}; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);">
                        {match_score}%
                    </div>
                    <div style="width: 100%; background-color: #e9ecef; border-radius: 10px; height: 10px; margin-top: 15px;">
                        <div style="width: {match_score}%; background-color: {score_color}; height: 100%; border-radius: 10px; transition: width 0.3s ease;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Score interpretation with emojis
                if match_score >= 70:
                    st.success("🎉 Excellent match! Your resume aligns well with this job.")
                elif match_score >= 50:
                    st.info("⚡ Good potential! With some improvements, your resume could be a better fit.")
                else:
                    st.warning("🔧 Room for improvement. Consider incorporating more relevant keywords and skills.")
            
            with rec_col:
                st.subheader("Recommendations")
                
                for rec in recommendations:
                    with st.expander(rec["title"]):
                        if isinstance(rec["content"], list):
                            for item in rec["content"]:
                                st.markdown(f"• {item}")
                        else:
                            st.write(rec["content"])
            
            # Display missing keywords
            missing_keywords = nlp_analyzer.find_missing_keywords(resume_text, job_description)
            if missing_keywords:
                st.subheader("Missing Keywords")
                st.markdown("These important keywords from the job description are missing in your resume:")

                # Display as pills/tags with better visibility
                keyword_html = ""
                for keyword in missing_keywords[:15]:  # Limit to 15 keywords
                    keyword_html += f'<span style="background-color: #ff6b6b; color: white; padding: 8px 12px; margin: 5px; border-radius: 20px; display: inline-block; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">{keyword}</span>'

                st.markdown(keyword_html, unsafe_allow_html=True)

                # Keyword usage suggestion
                st.info("💡 Try incorporating these keywords naturally into your resume where applicable.")

# Sample jobs showcase
st.markdown("---")
st.subheader("📋 Available Sample Jobs")
st.markdown("Choose from 20+ professionally crafted job descriptions across various industries:")

# Organize jobs by category
job_categories = {
    "💻 Technology": [
        "Software Engineer", "Data Scientist", "DevOps Engineer", "Cybersecurity Analyst",
        "Mobile App Developer", "Cloud Architect", "Quality Assurance Engineer",
        "Machine Learning Engineer", "Network Administrator", "Database Administrator"
    ],
    "🎨 Design & Creative": [
        "UX/UI Designer", "Graphic Designer", "Content Writer", "Technical Writer"
    ],
    "📈 Business & Management": [
        "Product Manager", "Business Analyst", "Project Manager", "Operations Manager",
        "Human Resources Manager", "Financial Analyst"
    ],
    "📢 Marketing & Sales": [
        "Digital Marketing Manager", "Sales Representative", "Social Media Manager",
        "Customer Success Manager"
    ]
}

# Display categories in columns
cols = st.columns(2)
for i, (category, jobs) in enumerate(job_categories.items()):
    with cols[i % 2]:
        st.markdown(f"**{category}**")
        for job in jobs:
            st.markdown(f"• {job}")

# Add footer
st.markdown("---")
st.markdown("**Expert Journey** - Navigate your career path with AI-powered insights and optimization")