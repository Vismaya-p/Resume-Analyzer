import streamlit as st
from utils import extract_text_from_pdf, calculate_similarity

st.title("Smart Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)")

job_desc = st.text_area("Paste Job Description")

if uploaded_file and job_desc:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_text_from_pdf("temp.pdf")
    score = calculate_similarity(resume_text, job_desc)

    st.write(f"Match Score: {round(score * 100, 2)}%")