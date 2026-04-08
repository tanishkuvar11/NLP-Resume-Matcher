import pandas as pd
from utils.embedding_utils import load_model
from utils.scoring_utils import compute_final_score
from utils.skill_utils import compute_skill_scores, parse_skills
from utils.degree_utils import passes_degree_filter
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing.prepare_resume_corpus import preprocess_resume_dataframe


model = load_model()


def process_uploaded_resumes(
    df,
    job_title,
    required_skills,
    preferred_skills=None,
    required_degree_level=None,
    top_k=5
):
    df = preprocess_resume_dataframe(df)

    if preferred_skills is None:
        preferred_skills = set()

    # build query
    query_text = (
        job_title.lower() + " " +
        " ".join(required_skills) + " " +
        " ".join(preferred_skills)
    )

    query_embedding = model.encode([query_text])

    # embed resumes
    resume_texts = df["full_resume_text"].tolist()
    resume_embeddings = model.encode(resume_texts)

    semantic_scores = cosine_similarity(
        query_embedding,
        resume_embeddings
    )[0]

    results = []

    for idx, row in df.iterrows():

        if "degree_names_clean" in row:
            if not passes_degree_filter(
                row,
                required_degree_level
            ):
                continue

        # handle skills
        if "skills_clean" in row:
            resume_skills = parse_skills(
                row["skills_clean"]
            )
        else:
            resume_skills = set()

        skill_result = compute_skill_scores(
            resume_skills,
            required_skills,
            preferred_skills
        )

        if skill_result is None:
            continue

        (
            matched_required,
            matched_preferred,
            required_score,
            preferred_score
        ) = skill_result

        semantic_score = semantic_scores[idx]

        final_score = compute_final_score(
            semantic_score,
            required_score,
            preferred_score
        )

        results.append({
            "resume_index": idx,
            "final_score": round(final_score * 100, 2),
            "semantic_score": round(semantic_score * 100, 2),
            "required_score": round(required_score * 100, 2),
            "preferred_score": round(preferred_score * 100, 2),
            "matched_required": list(matched_required),
            "matched_preferred": list(matched_preferred)
        })

    results = sorted(
        results,
        key=lambda x: x["final_score"],
        reverse=True
    )

    return pd.DataFrame(results[:top_k])

if __name__ == "__main__":
    import pandas as pd

    df = pd.read_csv("datasets/resume_data.csv")

    result = process_uploaded_resumes(
        df=df,
        job_title="NLP Engineer",
        required_skills={
            "python",
            "machine learning",
            "nlp"
        },
        preferred_skills={
            "sql",
            "pytorch",
            "transformers"
        },
        top_k=5
    )

    print("\nTop Candidates:\n")
    print(result.to_string(index=False))