import re
from collections import Counter


STOPWORDS = {
    "the", "and", "for", "with", "of", "to", "in",
    "a", "an", "is", "are", "we", "looking",
    "experience", "knowledge", "strong", "good",
    "ability", "role", "engineer", "developer",
    "analyst", "manager", "required"
}


def extract_keywords_from_jd(job_description, top_k=10):
    text = job_description.lower()

    words = re.findall(r"\b[a-zA-Z][a-zA-Z+\-#\.]*\b", text)

    filtered_words = [
        word for word in words
        if word not in STOPWORDS and len(word) > 2
    ]

    freq = Counter(filtered_words)

    return {
        word
        for word, _ in freq.most_common(top_k)
    }