\# NLP + LLM Resume Matcher



An end-to-end NLP + LLM based web application designed for both \*\*recruiters\*\* and \*\*job applicants\*\*.



The system performs \*\*semantic resume–job matching\*\* using transformer-based embeddings and provides \*\*personalized resume feedback\*\* using an LLM.



Deployed as an interactive \*\*Streamlit web application\*\*.



\---



\## Features



\### Recruiter Module



\* Upload candidate resumes as a CSV file

\* Enter target role and required skills

\* Rank candidates using semantic similarity and hybrid relevance scoring

\* View top matching resumes in real time



\### Applicant Module



\* Upload resume as PDF

\* Paste target job description

\* Get fit analysis against the role

\* Receive personalized, resume-specific improvement feedback powered by LLMs



\---



\## Tech Stack



\* Python

\* NLP

\* Sentence-Transformers (`all-MiniLM-L6-v2`)

\* PyTorch

\* Scikit-learn

\* Streamlit

\* Groq API (Llama 3)

\* Pandas / NumPy



\---



\## System Architecture



```text

Resume PDF / CSV

&#x20;       ↓

Text Extraction + Preprocessing

&#x20;       ↓

Semantic Embedding Generation

&#x20;       ↓

Cosine Similarity + Hybrid Scoring

&#x20;       ↓

Ranking / Resume Audit

&#x20;       ↓

LLM-based Personalized Feedback

```



\---



\## Core Components



\### Semantic Matching Engine



Uses Sentence-Transformers to generate dense vector embeddings for resumes and job descriptions.



Candidate relevance is computed using:



\* semantic similarity

\* cosine distance

\* scoring heuristics



\---



\### Recruiter Inference Pipeline



Processes uploaded resume datasets dynamically and ranks candidates for a given job role.



Supports:



\* CSV ingestion

\* resume preprocessing

\* candidate ranking

\* top-k retrieval



\---



\### Applicant Resume Analyzer



Analyzes uploaded PDF resumes against job descriptions.



Provides:



\* fit score

\* role alignment

\* personalized resume improvement suggestions



\---



\### LLM Feedback Layer



Integrated with Groq (Llama 3) for context-aware, resume-specific feedback generation.



Prompts are conditioned on:



\* resume content

\* job description

\* fit metrics



\---



\## Installation



```bash

git clone <your-repo-link>

cd nlp\_resume\_matcher

pip install -r requirements.txt

```



\---



\## Run Locally



```bash

python -m streamlit run app.py

```



\---



\## Environment Variables



Create a `.env` file:



```text

GROQ\_API\_KEY=your\_api\_key\_here

```



\---



\## Project Structure



```text

nlp\_resume\_matcher/

│

├── app.py

├── engines/

├── utils/

├── preprocessing/

├── requirements.txt

└── README.md

```

