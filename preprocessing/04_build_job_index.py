import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer

jobs = pd.read_csv("cleaned_jobs.csv")

print("Total jobs:", len(jobs))

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Encoding jobs...")

job_embeddings = model.encode(
    jobs["full_job_text"].tolist(),
    show_progress_bar=True
)

with open("data/job_embeddings.pkl", "wb") as f:
    pickle.dump(job_embeddings, f)

jobs.to_csv("data/job_metadata.csv", index=False)

print("Job embeddings saved.")
print("Metadata saved.")