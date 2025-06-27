class ResumeRecommender:
    """Generate recommendations to improve resume based on job description."""
    
    def __init__(self, nlp_analyzer):
        self.nlp_analyzer = nlp_analyzer
    
    def generate_recommendations(self, resume_text, job_text):
        """Generate specific recommendations to improve resume alignment with job."""
        if not resume_text or not job_text:
            return []
            
        recommendations = []
        
        # Find missing keywords
        missing_keywords = self.nlp_analyzer.find_missing_keywords(resume_text, job_text)
        
        # Extract skills from job description
        job_skills = self.nlp_analyzer.extract_skills(job_text)
        resume_skills = self.nlp_analyzer.extract_skills(resume_text)
        missing_skills = [skill for skill in job_skills if skill not in resume_skills]
        
        # Generate recommendations based on missing keywords and skills
        if missing_keywords:
            recommendations.append({
                "type": "missing_keywords",
                "title": "Add these keywords to your resume",
                "content": missing_keywords[:10]  # Limit to top 10
            })
        
        if missing_skills:
            recommendations.append({
                "type": "missing_skills",
                "title": "Highlight these skills if you have them",
                "content": missing_skills[:8]  # Limit to top 8
            })
        
        # Check resume length and add recommendation if too short
        if len(resume_text.split()) < 200:
            recommendations.append({
                "type": "length",
                "title": "Expand your resume content",
                "content": "Your resume appears to be quite short. Consider adding more details about your experience, projects, and achievements."
            })
        
        # Add general recommendations
        recommendations.append({
            "type": "general",
            "title": "General improvements",
            "content": [
                "Quantify achievements with numbers and metrics",
                "Use action verbs to describe your experience",
                "Tailor your resume summary to match the job description",
                "Ensure your resume is free of grammatical errors"
            ]
        })
        
        return recommendations