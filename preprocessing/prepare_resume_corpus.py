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
        if item.strip() != ""
    ]

    return items


def preprocess_resume_dataframe(df):
    df = df.copy()

    df["skills_clean"] = df["skills"].apply(clean_list_to_list)
    df["positions_clean"] = df["positions"].apply(clean_list_to_list)

    df["career_objective"] = (
        df["career_objective"]
        .fillna("")
        .str.lower()
    )

    df["major_field_of_studies"] = (
        df["major_field_of_studies"]
        .fillna("")
        .str.lower()
    )

    df["responsibilities"] = (
        df["responsibilities"]
        .fillna("")
        .str.lower()
    )

    df["certification_skills"] = (
        df["certification_skills"]
        .fillna("")
        .str.lower()
    )

    df["degree_names_clean"] = df[
        "degree_names"
    ].apply(clean_list_to_list)

    df["full_resume_text"] = (
        "professional experience includes "
        + df["positions_clean"].apply(
            lambda x: " ".join(x)
        )
        + ". "
        + "skilled in "
        + df["skills_clean"].apply(
            lambda x: ", ".join(x)
        )
        + ". "
        + df["major_field_of_studies"]
        + " "
        + df["responsibilities"]
        + " "
        + df["career_objective"]
        + " "
        + df["certification_skills"]
    )

    df["full_resume_text"] = (
        df["full_resume_text"]
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    df = df[df["full_resume_text"] != ""]
    df = df.drop_duplicates(
        subset=["full_resume_text"]
    ).reset_index(drop=True)

    df["resume_id"] = df.index

    df["skills_clean"] = df["skills_clean"].apply(
        json.dumps
    )

    df["positions_clean"] = df[
        "positions_clean"
    ].apply(json.dumps)

    df["degree_names_clean"] = df[
        "degree_names_clean"
    ].apply(json.dumps)

    return df[[
        "resume_id",
        "full_resume_text",
        "skills_clean",
        "positions_clean",
        "degree_names_clean"
    ]]


if __name__ == "__main__":
    df = pd.read_csv("datasets/resume_data.csv")

    print("Original rows:", len(df))

    df_final = preprocess_resume_dataframe(df)

    df_final.to_csv(
        "cleaned_resumes.csv",
        index=False
    )

    print("Cleaned rows:", len(df_final))
    print("Done.")