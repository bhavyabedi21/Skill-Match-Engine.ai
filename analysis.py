import google.generativeai as genai
from pdf import process_pdf
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# Configure Gen AI & Model
genai.configure(api_key = os.getenv("GOOGLE_GEMINI_API"))
model = genai.GenerativeModel("gemini-1.5-flash") # flash is good for pdf


def analyse_profile(pdf_doc, job_desc):
    if pdf_doc is not None:
        pdf = process_pdf(pdf_doc)
        st.sidebar.markdown("✅ Uploaded Successfully")
    else:
        st.warning("📝 Upload the Resume")

    good_fit = model.generate_content(f'''Compare the {job_desc} with the 
                                      resume{pdf} and suggest Am I good fit for the role''').text

    ats_score = model.generate_content(f'''Compare the {job_desc} with the resume{pdf} 
                                       and suggest the ATS Score of the resume''').text

    probability = model.generate_content(f'''Compare the {job_desc} with the resume{pdf} and 
                                         suggest the Probability of getting selected in Percentage''').text

    keywords = model.generate_content(f''' Comapare the {job_desc} with
                                      resume{pdf} and give me a list of keywords
                                      shown in the job description but missing in the resume''').text
    
    swot = model.generate_content(f''' Comapare the {job_desc} with
                                      resume{pdf} and give me SWOT analysis
                                      followed by actionable insights in bulletin points''').text
    
    projects = model.generate_content(f''' Comapare the {job_desc} with resume{pdf} 
                                      and give me a list of ML competitions and projects that 
                                      are aligned with the Job Description and role''').text
    
    return (
            st.write(good_fit), 
            st.write(ats_score),
            st.write(probability), 
            st.write(keywords), 
            st.write(swot), 
            st.write(projects)
            )