import json

def parse_skills(skill_json):
    return set(json.loads(skill_json))

def compute_skill_scores(resume_skills, required_skills, preferred_skills):
    matched_required = resume_skills.intersection(required_skills)
    matched_preferred = resume_skills.intersection(preferred_skills)

    if required_skills and len(matched_required) == 0:
        return None

    required_score = (
        len(matched_required) / len(required_skills)
        if required_skills else 0
    )

    preferred_score = (
        len(matched_preferred) / len(preferred_skills)
        if preferred_skills else 0
    )

    return matched_required, matched_preferred, required_score, preferred_score