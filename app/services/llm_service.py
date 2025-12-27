import os
import ollama

# --------------------------------------------------
# Cloud / Local LLM Toggle
# --------------------------------------------------
# USE_LOCAL_LLM=true  -> Local Ollama (default)
# USE_LOCAL_LLM=false -> Cloud-safe mode (no Ollama)
# --------------------------------------------------

USE_LOCAL_LLM = os.getenv("USE_LOCAL_LLM", "true").lower() == "true"


def summarize_with_llm(question: str, context: str) -> str:
    """
    Uses FREE local LLM via Ollama in local mode.
    In cloud mode, safely disables LLM to avoid runtime failure.
    """

    # ---------------- NO CONTEXT ----------------
    if not context.strip():
        return "No relevant official information was found for this query."

    # ---------------- CLOUD MODE ----------------
    if not USE_LOCAL_LLM:
        return (
            "Backend deployed successfully.\n\n"
            "LLM responses are available only in local mode "
            "because this system uses a local LLM (Ollama).\n\n"
            "Please run the backend locally to enable full AI responses."
        )

    # ---------------- LOCAL MODE (OLLAMA) ----------------
    prompt = f"""
You are a Government & Legal Information Assistant.

RULES (MANDATORY):
- Answer ONLY about the topic mentioned below.
- Do NOT mention any other IDs or documents.
- Do NOT provide legal advice.
- If the answer is not found, say:
  "No relevant official information was found."

{context}

User Question:
{question}

Provide a clear, simple answer.
"""

    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response["message"]["content"].strip()

    except Exception:
        return (
            "The local LLM is not reachable.\n\n"
            "Please ensure Ollama is running and the model is available."
        )
