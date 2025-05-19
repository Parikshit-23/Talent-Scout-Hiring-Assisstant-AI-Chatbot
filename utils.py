
import sys
import openai


client = openai.OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

def generate_questions_from_openai(tech_stack):
    prompt = f"""
    Generate 10 technical interview questions for each of the following technologies: {tech_stack}.
    The questions should assess intermediate-level proficiency and be concise.
    Return the result as a numbered list.
    """

    response = client.chat.completions.create(
        model="anthropic/claude-3-haiku",
        messages=[
            {"role": "system", "content": "You are a helpful technical interviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    result = response.choices[0].message.content
    return [line[3:].strip() for line in result.splitlines() if line.strip().startswith(("1.", "2.", "3."))]
