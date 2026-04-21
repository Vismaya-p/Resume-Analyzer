import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""

    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, job_desc):
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([resume_text, job_desc])

    similarity = cosine_similarity(vectors[0], vectors[1])

    return similarity[0][0]