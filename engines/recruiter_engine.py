import pandas as pd
import pickle

from utils.embedding_utils import load_model, compute_semantic_scores
from utils.skill_utils import parse_skills, compute_skill_scores
from utils.degree_utils import passes_degree_filter
from utils.scoring_utils import compute_final_score

resumes = pd.read_csv("data/resume_metadata.csv")

with open("data/resume_embeddings.pkl", "rb") as f:
    resume_embeddings = pickle.load(f)

model = load_model()

job_title = "Web Developer"
required_skills = {"php", "mysql", "html", "css"}
preferred_skills = {"laravel", "jquery", "rest"}
required_degree_level = None

query_text = (
    job_title.lower() + " " +
    " ".join(required_skills) + " " +
    " ".join(preferred_skills)
)

semantic_scores = compute_semantic_scores(
    model,
    query_text,
    resume_embeddings
)

results = []

for idx, row in resumes.iterrows():

    if not passes_degree_filter(row, required_degree_level):
        continue

    resume_skills = parse_skills(row["skills_clean"])

    skill_result = compute_skill_scores(
        resume_skills,
        required_skills,
        preferred_skills
    )

    if skill_result is None:
        continue

    matched_required, matched_preferred, required_score, preferred_score = skill_result

    semantic_score = semantic_scores[idx]

    final_score = compute_final_score(
        semantic_score,
        required_score,
        preferred_score
    )

    results.append({
        "resume_id": row["resume_id"],
        "final_score": final_score,
        "semantic_score": semantic_score,
        "required_score": required_score,
        "preferred_score": preferred_score,
        "matched_required": list(matched_required),
        "matched_preferred": list(matched_preferred)
    })

results = sorted(results, key=lambda x: x["final_score"], reverse=True)

for r in results[:5]:
    print(r)