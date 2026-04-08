import streamlit as st
import pandas as pd

from engines.recruiter_engine import process_uploaded_resumes
from engines.applicant_engine import analyze_resume_against_jd

st.set_page_config(
    page_title="NLP Resume Matcher",
    layout="wide"
)

st.title("NLP Resume Matcher")
st.write("Recruiter + Applicant Matching System")

mode = st.sidebar.selectbox(
    "Choose Module",
    ["Recruiter", "Applicant"]
)

if mode == "Recruiter":
    st.header("Recruiter Candidate Ranking")

    uploaded_file = st.file_uploader(
        "Upload Resume CSV",
        type=["csv"]
    )

    job_title = st.text_input("Job Role")

    required_skills = st.text_input(
        "Required Skills (comma separated)"
    )

    preferred_skills = st.text_input(
        "Preferred Skills (comma separated)"
    )

    top_k = st.slider(
        "Top Candidates",
        1,
        20,
        5
    )

    if uploaded_file and st.button("Find Candidates"):

        df = pd.read_csv(uploaded_file)

        req_skills = {
            s.strip().lower()
            for s in required_skills.split(",")
            if s.strip()
        }

        pref_skills = {
            s.strip().lower()
            for s in preferred_skills.split(",")
            if s.strip()
        }

        result_df = process_uploaded_resumes(
            df=df,
            job_title=job_title,
            required_skills=req_skills,
            preferred_skills=pref_skills,
            top_k=top_k
        )

        st.subheader("Top Matching Candidates")
        st.dataframe(result_df)

elif mode == "Applicant":
    st.header("Applicant Resume Analyzer")

    uploaded_resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    job_title = st.text_input("Target Role")

    job_description = st.text_area(
        "Paste Job Description",
        height=250
    )

    if uploaded_resume and st.button("Analyze Resume"):

        from engines.applicant_engine import (
            analyze_resume_against_jd
        )

        from utils.pdf_parser import (
            extract_text_from_pdf
        )

        with st.spinner("Analyzing resume..."):

            resume_text = extract_text_from_pdf(
                uploaded_resume
            )

            result = analyze_resume_against_jd(
                resume_text=resume_text,
                resume_skills=set(
                    resume_text.lower().split()
                ),
                job_title=job_title,
                job_description=job_description
            )

        audit = result["audit"]

        st.metric(
            "Overall Fit Score",
            f'{audit["overall_fit_score"]}%'
        )

        st.write("### LLM Resume Advice")
        st.write(result["advisor_output"])