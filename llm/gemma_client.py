import ollama

def ask_gemma(question, context):
    prompt = f"""
You are a telecom expert.
Compare telecom plans clearly and accurately.

Plans:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model="gemma3:1b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]