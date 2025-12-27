from app.rag.vector_store import retrieve_context

query = "How to apply for Aadhaar?"
context = retrieve_context(query)

print(context)
