from fastapi import APIRouter
from pydantic import BaseModel
from streamlit import context

from app.safety.intent_classifier import classify_intent
from app.rag.vector_store import retrieve_context
from app.services.llm_service import summarize_with_llm

router = APIRouter()

# Request body model
class QuestionRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_question(request: QuestionRequest):
    user_question = request.question

    # 1️ Intent & safety check
    intent_result = classify_intent(user_question)

    if not intent_result.get("allowed"):
        return {
            "answer": intent_result.get("message"),
            "disclaimer": "This assistant provides awareness only."
        }

    # 2️ Retrieve relevant context using RAG
    context = retrieve_context(user_question)

    # 3️ Return response (RAG-only for now)
   
    final_answer = summarize_with_llm(user_question, context)
   
    return {
    "question": user_question,
    "answer": final_answer,
    "disclaimer": "This information is for public awareness only and not legal advice."
}
