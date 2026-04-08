import pandas as pd
import re
import json


def clean_list_to_list(text):
    if pd.isna(text):
        return []

    text = str(text)

    text = re.sub(r"[\[\]']", "", text)

    items = [
        item.strip().lower()
        for item in text.split(",")
        if item.strip()
    ]

    return items


def preprocess_uploaded_resume_df(df):
    df = df.copy()

    # normalize important columns if present
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].fillna("").astype(str)

    if "skills" in df.columns:
        df["skills_clean"] = df["skills"].apply(
            clean_list_to_list
        )

    text_columns = [
        col for col in df.columns
        if df[col].dtype == object
    ]

    df["full_resume_text"] = (
        df[text_columns]
        .fillna("")
        .agg(" ".join, axis=1)
        .str.lower()
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    if "skills_clean" in df.columns:
        df["skills_clean"] = df["skills_clean"].apply(
            json.dumps
        )

    return df