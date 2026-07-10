from openai import OpenAI
from config import GROQ_API_KEY
from prompts import FEATURE_PROMPTS

# ----------------------------------
# Create Groq Client
# ----------------------------------
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


# ----------------------------------
# AI Response Function
# ----------------------------------
def generate_response(prompt, feature, language):

    # Get prompt template
    feature_prompt = FEATURE_PROMPTS.get(
        feature,
        "Provide the best possible programming assistance."
    )

    # System Prompt
    system_prompt = f"""
You are AI Coding Assistant Pro.

Programming Language:
{language}

Selected Feature:
{feature}

Task:
{feature_prompt}

Instructions:

• Give beginner-friendly explanations.
• Write clean and optimized code.
• Follow best coding practices.
• Format the response professionally.
• If code is generated, wrap it inside Markdown code blocks.
• Explain important concepts whenever necessary.
"""

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
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