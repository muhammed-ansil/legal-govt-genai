def classify_intent(query: str):
    blocked_keywords = [
        "sue", "court", "lawyer", "judge",
        "bribe", "escape", "case strategy"
    ]

    query_lower = query.lower()

    for word in blocked_keywords:
        if word in query_lower:
            return {
                "allowed": False,
                "message": "This assistant provides awareness only, not legal advice."
            }

    return {
        "allowed": True,
        "intent": "legal_or_govt_awareness"
    }
