from utils.embedding_utils import load_model
from utils.skill_utils import compute_skill_scores
from utils.scoring_utils import compute_final_score
from utils.pdf_parser import extract_text_from_pdf
from utils.jd_parser import extract_keywords_from_jd
from utils.llm_advisor import generate_llm_advice

from sklearn.metrics.pairwise import cosine_similarity


def analyze_resume(
    resume_text,
    resume_skills,
    job_title,
    required_skills,
    job_description="",
    preferred_skills=None
):
    if preferred_skills is None:
        preferred_skills = set()

    model = load_model()

    job_query = (
        job_title.lower() + " " +
        " ".join(required_skills) + " " +
        " ".join(preferred_skills)
    )

    resume_embedding = model.encode([resume_text])
    job_embedding = model.encode([job_query])

    semantic_score = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    skill_result = compute_skill_scores(
        set(resume_skills),
        set(required_skills),
        set(preferred_skills)
    )

    if skill_result is None:
        matched_required = set()
        matched_preferred = set()
        required_score = 0
        preferred_score = 0
    else:
        (
            matched_required,
            matched_preferred,
            required_score,
            preferred_score
        ) = skill_result

    final_score = compute_final_score(
        semantic_score,
        required_score,
        preferred_score
    )

    missing_skills = list(
        set(required_skills) - set(resume_skills)
    )

    skill_coverage = (
        len(matched_required) / len(required_skills)
        if required_skills else 0
    )

    gap_severity = (
        len(missing_skills) / len(required_skills)
        if required_skills else 0
    )

    audit = {
        "overall_fit_score": round(final_score * 100, 2),
        "semantic_alignment_score": round(semantic_score * 100, 2),
        "skill_coverage_score": round(skill_coverage * 100, 2),
        "gap_severity_score": round(gap_severity * 100, 2),
        "required_score": round(required_score * 100, 2),
        "preferred_score": round(preferred_score * 100, 2)
    }

    advisor_output = generate_llm_advice(
        audit=audit,
        missing_skills=missing_skills,
        job_title=job_title,
        resume_text=resume_text,
        job_description=job_description
    )

    return {
        "audit": audit,
        "matched_required": list(matched_required),
        "matched_preferred": list(matched_preferred),
        "missing_skills": missing_skills,
        "advisor_output": advisor_output
    }


def analyze_resume_against_jd(
    resume_text,
    resume_skills,
    job_title,
    job_description
):
    required_skills = extract_keywords_from_jd(
        job_description
    )

    return analyze_resume(
        resume_text=resume_text,
        resume_skills=resume_skills,
        job_title=job_title,
        required_skills=required_skills,
        job_description=job_description
    )


def analyze_resume_pdf_against_jd(
    pdf_path,
    job_title,
    job_description
):
    resume_text = extract_text_from_pdf(pdf_path)

    required_skills = extract_keywords_from_jd(
        job_description
    )

    text_lower = resume_text.lower()

    resume_skills = {
        skill.lower()
        for skill in required_skills
        if skill.lower() in text_lower
    }

    return analyze_resume(
        resume_text=resume_text,
        resume_skills=resume_skills,
        job_title=job_title,
        required_skills=required_skills,
        job_description=job_description
    )


if __name__ == "__main__":
    sample_resume_text = """
    Python developer with SQL,
    machine learning and NLP experience.
    Built REST APIs and model deployment systems.
    """

    sample_resume_skills = {
        "python",
        "sql",
        "machine",
        "learning",
        "nlp",
        "rest"
    }

    sample_jd = """
    We are looking for an NLP Engineer with strong
    Python, SQL, PyTorch, transformers and
    deployment experience.
    """

    result = analyze_resume_against_jd(
        resume_text=sample_resume_text,
        resume_skills=sample_resume_skills,
        job_title="NLP Engineer",
        job_description=sample_jd
    )

    print(result)