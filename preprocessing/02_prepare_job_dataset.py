import pandas as pd

# Load dataset
df = pd.read_csv("datasets/training_data.csv")

print("Original rows:", len(df))

# Clean column names
df.columns = df.columns.str.strip()

# Keep only needed columns
df = df[["position_title", "job_description"]]

# Remove nulls
df["position_title"] = df["position_title"].fillna("")
df["job_description"] = df["job_description"].fillna("")

# Combine title + description
df["full_job_text"] = df["position_title"] + " " + df["job_description"]

# Basic cleaning
df["full_job_text"] = df["full_job_text"].str.lower()
df["full_job_text"] = df["full_job_text"].str.replace(r"\s+", " ", regex=True)
df["full_job_text"] = df["full_job_text"].str.strip()

# Remove empty rows
df = df[df["full_job_text"] != ""]

# Save cleaned dataset
df_final = df[["position_title", "full_job_text"]]

df_final.to_csv("cleaned_jobs.csv", index=False)

print("Cleaned rows:", len(df_final))
print("Done.")