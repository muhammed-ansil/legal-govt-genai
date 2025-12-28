from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_question(request: QuestionRequest):
    return {
        "question": request.question,
        "answer": (
            "This backend is deployed in cloud-safe mode. "
            "Full AI responses are available when running locally."
        ),
        "disclaimer": "This information is for public awareness only."
    }
