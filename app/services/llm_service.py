import ollama


def summarize_with_llm(question: str, context: str) -> str:
    """
    Uses FREE local LLM via Ollama to summarize RAG output.
    No API key, no cost, fully offline.
    """

    if not context.strip():
        return "No relevant official information was found for this query."

    prompt = f"""
You are a Government & Legal Information Assistant.

RULES (MANDATORY):
- Answer ONLY about the topic mentioned below.
- Do NOT mention any other IDs or documents.
- If the answer is not found, say: "No relevant official information was found."

{context}

User Question:
{question}

Provide a clear, simple answer.
"""



    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()
