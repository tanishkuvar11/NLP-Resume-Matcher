def generate_suggestions(missing_skills, job_title):
    suggestions = []

    if not missing_skills:
        return [
            f"Your resume aligns well with the {job_title} role."
        ]

    for skill in missing_skills:
        suggestions.append(
            f"Add a project, internship, coursework, or certification "
            f"that explicitly demonstrates '{skill}'."
        )

        suggestions.append(
            f"Ensure '{skill}' appears in the skills section and is "
            f"supported by work experience or project descriptions."
        )

    suggestions.append(
        "Use measurable impact points such as tools used, problem solved, "
        "and outcomes achieved."
    )

    return suggestions