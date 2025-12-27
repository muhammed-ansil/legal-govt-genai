from fastapi import FastAPI
from app.api.ask import router as ask_router

app = FastAPI(
    title="AI Legal & Government Awareness Assistant",
    description="Law-safe GenAI system for public awareness",
    version="1.0"
)

app.include_router(ask_router)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Service is running"
    }
