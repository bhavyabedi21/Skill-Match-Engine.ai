import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv
load_dotenv()  # activate the key key
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))


# Movie Recommmender System Front End

st.title("🍿🎥Movie Recommender System🎥🍿")
user_input = st.text_input('Enter the Movie Name')
submit = st.button('Cick Here')

model = genai.GenerativeModel('gemini-1.5-flash-002')

if submit and user_input:
    response = model.generate_content(f"Generate Mcovie Recommendations for {user_input}").text
    st.write(f'Recommendations:\n{response}')
else:
    st.warning('Enter the Movie Name')