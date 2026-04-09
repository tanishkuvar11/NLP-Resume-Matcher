# NLP + LLM Resume Matcher

An end-to-end NLP + LLM powered web application for intelligent resume screening, candidate ranking, and personalized resume feedback.

The system is designed for both recruiters and applicants:

- **Recruiter Module** → ranks uploaded candidate resumes against a target role
- **Applicant Module** → analyzes resume PDFs against job descriptions and generates personalized feedback

Deployed as an interactive **Streamlit web application**.

---

## Features

### Recruiter Module
- Upload resume datasets as CSV files
- Enter target role and required skills
- Semantic candidate ranking using transformer embeddings
- Real-time top candidate retrieval

### Applicant Module
- Upload resume PDF
- Paste job description
- Resume–JD fit analysis
- Personalized LLM-based feedback

---

## Tech Stack

- Python
- NLP
- Sentence-Transformers (`all-MiniLM-L6-v2`)
- PyTorch
- Scikit-learn
- Streamlit
- Groq API (Llama 3)
- Pandas / NumPy

---

## System Workflow

```text
Resume PDF / CSV
        ↓
Text Extraction + Preprocessing
        ↓
Semantic Embedding Generation
        ↓
Cosine Similarity + Hybrid Scoring
        ↓
Ranking / Resume Audit
        ↓
LLM-based Personalized Feedback
````

---

## Core Components

### Semantic Matching Engine

Uses Sentence-Transformers to generate dense embeddings for resumes and job descriptions and computes semantic similarity using cosine similarity.

### Recruiter Inference Pipeline

Processes uploaded resume datasets dynamically and ranks candidates based on job role relevance.

### Applicant Resume Analyzer

Extracts text from uploaded PDF resumes and compares it against the target JD.

### LLM Feedback Layer

Uses Groq (Llama 3) to generate context-aware, resume-specific suggestions.

---

## Installation

```bash
git clone <your-repo-link>
cd nlp_resume_matcher
pip install -r requirements.txt
```

---

## Run Locally

```bash
python -m streamlit run app.py
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Project Structure

```text
nlp_resume_matcher/
│
├── app.py
├── engines/
├── utils/
├── preprocessing/
├── requirements.txt
└── README.md
```
```
```
