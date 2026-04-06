import ollama

def generate_llm_advice(
    audit,
    missing_skills,
    job_title,
    resume_text,
    job_description
):
    prompt = f"""
You are an expert ATS resume advisor.

Target Role:
{job_title}

Audit Scores:
{audit}

Missing Skills:
{missing_skills}

Resume:
{resume_text}

Job Description:
{job_description}

Provide:
1. top 3 specific resume improvements
2. project / internship suggestions
3. ATS keyword optimization advice
4. better bullet-point wording suggestions

Keep it actionable and concise.
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]