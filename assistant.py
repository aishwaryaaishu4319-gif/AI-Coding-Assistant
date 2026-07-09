from openai import OpenAI
from config import GROQ_API_KEY

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """
You are an expert AI Coding Assistant.

You help users by:
- Writing clean code
- Explaining code line by line
- Finding bugs
- Fixing errors
- Converting code between programming languages
- Writing documentation
- Generating pytest unit tests

Always provide clear and beginner-friendly answers.
"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=2048
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error:\n{str(e)}"