import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def generate_llm_advice(
    audit,
    missing_skills,
    job_title,
    resume_text,
    job_description
):
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = f"""
You are a senior ATS reviewer, giving resume reviews to candidates for required job descriptions.

Your task is to evaluate THIS SPECIFIC RESUME against THIS SPECIFIC JOB DESCRIPTION.

Be highly specific.
Do NOT give generic resume advice.
Every suggestion must reference something actually present or missing in the candidate's resume.

Target Role:
{job_title}

Resume Text:
{resume_text}

Job Description:
{job_description}

Fit Score:
{audit.get("overall_fit_score", "N/A")}

Instructions:
1. Briefly assess how well the candidate matches the role.
2. Mention 3 strengths from the actual resume that align with the JD.
3. Mention 3 specific gaps based on the JD.
4. Suggest exact projects, technologies, or bullet points the candidate should add.
5. Suggest concrete wording improvements for existing resume points.
6. Keep it personalized to THIS resume only.
7. Avoid generic phrases like "improve skills" or "add projects" unless you mention exactly what.

Output format:
- Overall assessment
- Strengths
- Gaps
- Exact resume improvements
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content