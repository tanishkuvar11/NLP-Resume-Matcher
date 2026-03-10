import re
import json

degree_rank = {
    None: 0,
    "bachelors": 1,
    "masters": 2,
    "phd": 3
}

def normalize_degree(degree_list):
    text = " ".join(degree_list).lower()

    if "phd" in text or "doctor" in text:
        return "phd"
    if re.search(r"\b(m\.?|master)", text):
        return "masters"
    if re.search(r"\b(b\.?|bachelor)", text):
        return "bachelors"

    return None

def passes_degree_filter(row, required_level):
    if not required_level:
        return True

    if "degree_names_clean" not in row:
        return False

    try:
        degree_list = json.loads(row["degree_names_clean"])
    except:
        degree_list = eval(row["degree_names_clean"])

    resume_level = normalize_degree(degree_list)

    return degree_rank[resume_level] >= degree_rank[required_level]