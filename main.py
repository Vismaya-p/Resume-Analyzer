from utils import extract_text_from_pdf, calculate_similarity

print("Step 1: Program started")

# Load resume
resume_text = extract_text_from_pdf("sample_resume.pdf")
print("Step 2: Resume loaded")

# Ask input
job_description = input("Enter job description:\n")
print("Step 3: Input received")

# Calculate similarity
score = calculate_similarity(resume_text, job_description)

print(f"Match Score: {round(score * 100, 2)}%")
