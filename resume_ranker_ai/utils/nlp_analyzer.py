import spacy
import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class NLPAnalyzer:
    """Analyze resume and job description using NLP techniques."""
    
    def __init__(self):
        # Load spaCy model
        self.nlp = spacy.load("en_core_web_md")
        
        # Common words to exclude from keyword analysis
        self.stop_words = self.nlp.Defaults.stop_words.union({
            "experience", "year", "years", "skill", "skills", "job", 
            "work", "working", "candidate", "ability", "position"
        })
    
    def preprocess_text(self, text):
        """Clean and preprocess text."""
        if not text:
            return ""
            
        # Convert to lowercase and remove special characters
        text = re.sub(r'[^\w\s]', ' ', text.lower())
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def extract_keywords(self, text, max_keywords=30):
        """Extract important keywords from text using spaCy."""
        doc = self.nlp(self.preprocess_text(text))
        
        # Extract nouns, proper nouns, and adjectives that aren't stop words
        keywords = []
        for token in doc:
            if (token.pos_ in ["NOUN", "PROPN"] or 
                (token.pos_ == "ADJ" and len(token.text) > 2)) and \
                not token.is_stop and token.text.lower() not in self.stop_words:
                keywords.append(token.text.lower())
        
        # Count frequencies and return top keywords
        keyword_freq = Counter(keywords)
        return [word for word, freq in keyword_freq.most_common(max_keywords)]
    
    def extract_skills(self, text):
        """Extract skills from text using a combination of NER and keyword extraction."""
        doc = self.nlp(self.preprocess_text(text))
        
        # Extract entities that might be skills
        skills = []
        for ent in doc.ents:
            if ent.label_ in ["ORG", "PRODUCT", "GPE"]:
                skills.append(ent.text.lower())
        
        # Add noun chunks that might represent skills
        for chunk in doc.noun_chunks:
            if not any(token.is_stop for token in chunk) and len(chunk.text) > 3:
                skills.append(chunk.text.lower())
        
        # Add technical terms and programming languages
        tech_pattern = r'\b(?:python|java|javascript|html|css|sql|react|node\.js|aws|docker|kubernetes|machine learning|ai|data science|nlp|c\+\+|ruby|php|swift|golang|scala|r|tableau|power bi|excel|word|powerpoint|photoshop|illustrator)\b'
        tech_skills = re.findall(tech_pattern, text.lower())
        skills.extend(tech_skills)
        
        # Remove duplicates and return
        return list(set(skills))
    
    def calculate_match_score(self, resume_text, job_text):
        """Calculate match percentage between resume and job description."""
        if not resume_text or not job_text:
            return 0
            
        # Preprocess texts
        resume_processed = self.preprocess_text(resume_text)
        job_processed = self.preprocess_text(job_text)
        
        # Use TF-IDF vectorization for better semantic matching
        vectorizer = TfidfVectorizer(stop_words='english')
        try:
            tfidf_matrix = vectorizer.fit_transform([resume_processed, job_processed])
            # Calculate cosine similarity
            similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
            
            # Convert to percentage
            match_percentage = round(similarity * 100)
            
            # Ensure the score is between 0 and 100
            return max(0, min(match_percentage, 100))
        except:
            # Fallback if vectorization fails
            return self._calculate_keyword_match(resume_text, job_text)
    
    def _calculate_keyword_match(self, resume_text, job_text):
        """Fallback method to calculate match based on keyword overlap."""
        job_keywords = set(self.extract_keywords(job_text, max_keywords=50))
        resume_keywords = set(self.extract_keywords(resume_text, max_keywords=100))
        
        if not job_keywords:
            return 0
            
        # Calculate overlap
        matching_keywords = resume_keywords.intersection(job_keywords)
        match_percentage = round((len(matching_keywords) / len(job_keywords)) * 100)
        
        return max(0, min(match_percentage, 100))
    
    def find_missing_keywords(self, resume_text, job_text):
        """Identify keywords from job description missing in resume."""
        job_keywords = set(self.extract_keywords(job_text, max_keywords=50))
        resume_keywords = set(self.extract_keywords(resume_text, max_keywords=100))
        
        missing_keywords = job_keywords - resume_keywords
        return list(missing_keywords)