# resume-analysis.ai

Resume Analysis...

### Steps for creating the project

- Create the Virtual Environment using `python -m venv .venv`
- Activate the Virtual Environment using `source .venv/Scripts/activate`
- Create the .env file to store the API key
- Create the requirements.txt file and add the libraries for installation using `pip install -r requirements.txt`

### Project Synopsis

- We want to create an application that will analyse the resume of the candidate using Gen AI model with the Job Description and provide insights sucg as:-
- ATS Score
- Probability of getting hired
- Am I good fit?
- Keyword analysis
- Swot analysis
- Suggestions for overall improvements

### Architecture

- app.py : Front-End creation and output of Gen AI model.
  --> It will have the feature of capturing information such as Resume and Job Description
- Information that we are capturing is `Resume.pdf` and `job_desc`.
- `pdf.py` that will process the information in pdf and thats why we have installed `pypdf`.
- `analysis.py` that will triangulate the pdf information and the JD and will provide insights and next step.