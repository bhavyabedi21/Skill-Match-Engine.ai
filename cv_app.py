from dotenv import load_dotenv
load_dotenv()  # Load environment variables
import streamlit as st
from pdf import process_pdf
from analysis import analyse_profile

# App Header
st.header("📄 Scan My :blue[CV.ai]", divider="green")
st.subheader("💡 Tips for Using the Application")

notes = '''
📥 **Upload the Resume (PDF only):** Please upload your resume in **PDF format** only.

✅ **Paste the Job Description:** Copy and paste the job description below for better context.

🧠 **Unleash the Power of LLMs:** Leverage the power of **Large Language Models (LLMs)** to derive smart, AI-driven insights about your resume.
'''

st.write(notes)

# Sidebar
st.sidebar.subheader("📥 Upload Your Resume")
pdf_doc = st.sidebar.file_uploader("Choose a resume (PDF format)", type=["pdf"])
st.sidebar.markdown("👨‍💻 Created by: :blue[Bhavya Bedi]")

# Job Description Input
st.subheader("📝 Enter the Job Description", divider=True)
job_desc = st.text_area(
    label="Paste the job description from job boards (e.g., LinkedIn, Indeed)",
    max_chars=10000,
    placeholder="e.g., We're looking for a Data Analyst with experience in Python, SQL, and Tableau..."
)

submit = st.button("🚀 Get AI-Powered Insights")

if submit:
    st.markdown(analyse_profile(pdf_doc=pdf_doc, job_desc=job_desc))