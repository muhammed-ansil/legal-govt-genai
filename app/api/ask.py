from fastapi import APIRouter
from pydantic import BaseModel
import os

from app.services.llm_service import summarize_with_llm

router = APIRouter()

# Detect environment
USE_LOCAL_LLM = os.getenv("USE_LOCAL_LLM", "true").lower() == "true"


class QuestionRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_question(request: QuestionRequest):
    user_question = request.question

    # ---------------- CLOUD MODE ----------------
    # No RAG, no LangChain, no Ollama
    if not USE_LOCAL_LLM:
        return {
            "question": user_question,
            "answer": summarize_with_llm(user_question, ""),
            "disclaimer": "This information is for public awareness only."
        }

    # ---------------- LOCAL MODE ----------------
    # Import heavy modules ONLY when needed
    from app.safety.intent_classifier import classify_intent
    from app.rag.vector_store import retrieve_context

    # 1️⃣ Intent & safety check
    intent_result = classify_intent(user_question)
    if not intent_result.get("allowed"):
        return {
            "question": user_question,
            "answer": intent_result.get("message"),
            "disclaimer": "This assistant provides awareness only."
        }

    # 2️⃣ Retrieve context using RAG
    context = retrieve_context(user_question)

    # 3️⃣ Generate answer
    final_answer = summarize_with_llm(user_question, context)

    return {
        "question": user_question,
        "answer": final_answer,
        "disclaimer": "This information is for public awareness only and not legal advice."
    }
