import os

USE_LOCAL_LLM = os.getenv("USE_LOCAL_LLM", "true").lower() == "true"


def summarize_with_llm(question: str, context: str) -> str:
    """
    Uses FREE local LLM via Ollama in local mode.
    Cloud mode returns a safe placeholder response.
    """

    if not context.strip():
        return "No relevant official information was found for this query."

    # ---------------- CLOUD MODE ----------------
    if not USE_LOCAL_LLM:
        return (
            "This backend is deployed in cloud-safe mode. "
            "Full AI responses are available when running locally."
        )

    # ---------------- LOCAL MODE ----------------
    # Import ollama ONLY here (never at top-level)
    import ollama

    prompt = f"""
You are a Government & Legal Information Assistant.

RULES (MANDATORY):
- Answer ONLY using the provided context.
- Do NOT mix topics.
- Do NOT provide legal advice.
- If the answer is not found, say:
  "No relevant official information was found."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"].strip()
