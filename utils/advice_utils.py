def generate_smart_advice(
    missing_skills,
    semantic_score,
    job_title
):
    advice = []

    if semantic_score >= 0.25:
        advice.append(
            f"Your resume already shows strong alignment with the {job_title} role."
        )
    elif semantic_score >= 0.15:
        advice.append(
            f"Your resume shows partial alignment with the {job_title} role."
        )
    else:
        advice.append(
            f"Your resume currently has weak alignment with the {job_title} role."
        )

    if missing_skills:
        advice.append(
            "The main missing technical areas are: "
            + ", ".join(missing_skills)
            + "."
        )

        advice.append(
            "Add at least one project, internship, or coursework entry "
            "that demonstrates these skills."
        )

        advice.append(
            "Ensure these skills are explicitly mentioned in the skills "
            "section and supported by measurable outcomes."
        )
    else:
        advice.append(
            "No major technical skill gaps detected."
        )

    return advice