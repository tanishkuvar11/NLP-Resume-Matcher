import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer

# Load cleaned resumes
resumes = pd.read_csv("cleaned_resumes.csv")

print("Total resumes:", len(resumes))

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Encoding resumes...")

resume_embeddings = model.encode(
    resumes["full_resume_text"].tolist(),
    show_progress_bar=True
)

# Save embeddings
with open("resume_embeddings.pkl", "wb") as f:
    pickle.dump(resume_embeddings, f)

# Save metadata (keep structured columns)
resumes.to_csv("resume_metadata.csv", index=False)

print("Embeddings saved.")
print("Metadata saved.")