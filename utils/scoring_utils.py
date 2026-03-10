def compute_final_score(semantic_score, required_score, preferred_score):
    return (
        0.5 * semantic_score +
        0.4 * required_score +
        0.1 * preferred_score
    )