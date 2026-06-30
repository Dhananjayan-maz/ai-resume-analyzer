import google.generativeai as genai
import os

def analyze_resume(resume_text, predicted_role):
    
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are an experienced ATS Resume Reviewer.

The predicted job role is:
{predicted_role}

Resume:
{resume_text}

Analyze the resume and return the result in plain text only.

Rules:
- Do NOT use Markdown.
- Do NOT use **, *, #, ---, or tables.
- Use simple headings.
- Use the bullet symbol (•) for lists.
- Keep each point short and easy to understand.
- Write in simple English suitable for students.
- Keep the response under 500 words.
- Give practical suggestions instead of lengthy explanations.

Use exactly this format:

Resume Review

Overall Score:
<Score>/100

Predicted Role:
{predicted_role}

Strengths:
• ...
• ...
• ...

Areas to Improve:
• ...
• ...
• ...

Missing Skills:
• ...
• ...
• ...

Resume Suggestions:
• ...
• ...
• ...

Interview Tips:
• ...
• ...
• ...

Finish with one motivational sentence.
"""

    response = model.generate_content(prompt)

    return response.text