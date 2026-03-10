from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

def compute_semantic_scores(model, query_text, resume_embeddings):
    query_embedding = model.encode([query_text])
    return cosine_similarity(query_embedding, resume_embeddings)[0]