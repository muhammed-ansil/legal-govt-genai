# ⚖️ AI Legal & Government Awareness Assistant (GenAI + RAG)

A **topic-aware GenAI system** that provides **accurate, hallucination-free legal and government information** using **Retrieval-Augmented Generation (RAG)** and a **local Large Language Model (LLM)**.

The system is designed with **strict topic isolation**, **safety constraints**, and **production-style architecture** to ensure reliable public awareness responses.

> ⚠️ This project is for **public information only**. It does **not provide legal advice**.

---

## 🎯 Key Capabilities

- Topic-aware **RAG pipeline** (prevents cross-topic hallucination)
- Metadata-filtered **FAISS vector search**
- **Local LLM (Ollama – Llama3)** → no paid APIs
- Strict **safety & disclaimer enforcement**
- Modern, animated **Streamlit UI**
- Dark / Light mode with chat history
- Clean separation of **UI and AI logic**

---

## 🏛 Supported Domains

### Government
- Aadhaar
- PAN Card
- Voter ID

### Legal
- FIR / Police Procedure
- Consumer Rights
- Tenant Rights

Out-of-scope queries are **safely declined**.

---

## 🏗 System Architecture

Streamlit UI
│
▼
FastAPI Backend (/ask)
│
▼
Topic Detection
│
▼
FAISS Vector Search (metadata-filtered, k=1)
│
▼
Context Injection
│
▼
Local LLM (Ollama – Llama3)


---

## 🛠 Technology Stack

| Layer | Tools |
|-----|------|
| Frontend | Streamlit |
| Backend | FastAPI |
| LLM | Ollama (Llama3) |
| RAG | LangChain |
| Vector Store | FAISS |
| Embeddings | Sentence Transformers |
| Language | Python |

---

## 🧠 Engineering Highlights

- Enforced **single-topic retrieval (k=1)** to eliminate answer mixing
- Applied **metadata-based filtering** for document isolation
- Added **prompt-level constraints** to prevent unsafe responses
- Fully decoupled UI from backend to avoid regression during UI changes
- Designed for **local execution** without dependency on paid APIs

---

## ▶️ Local Setup

### Install Dependencies
```bash
pip install -r requirements.txt

Start LLM
ollama pull llama3

Run Backend
uvicorn app.main:app --reload

Run Frontend
streamlit run frontend/streamlit_app.py

🧪 Example Queries

How to apply for Aadhaar?

What is the FIR filing procedure?

What are tenant rights?

What are consumer rights?

🔐 Safety Considerations

No legal advice or case predictions

No personal data handling

Explicit disclaimers on every response

Designed strictly for public awareness

🚀 Deployment Notes

Optimized for local deployment (interviews, demos)

Backend: FastAPI + Uvicorn

Frontend: Streamlit

Ollama is intended for local execution.
Cloud deployment requires a hosted LLM replacement.

👤 Author

Muhammed Ansil
B.Tech – Artificial Intelligence & Data Science
Interests: GenAI, RAG Systems, AI Engineering

⭐ Acknowledgement

If this project is useful, feel free to ⭐ the repository.

**STOP COPYING HERE ⬆️**

---

## 🧠 SIMPLE RULE (REMEMBER THIS)

> **README = final product description**  
> **Chat = learning & guidance**

Only the **clean markdown content** belongs in the repo.

---

## ✅ WHAT TO DO NOW (SAFE STEPS)

1️⃣ Open `README.md`  
2️⃣ **Delete everything inside**  
3️⃣ Paste **only the markdown section above**  
4️⃣ Save  
5️⃣ `git add README.md`  
6️⃣ `git commit -m "Add concise senior-level README"`  
7️⃣ `git push`

---

## 🚀 NEXT (YOUR CHOICE)

Reply with one:

- **`RESUME POINTS`** → Convert this project into strong CV bullets  
- **`LINKEDIN POST`** → Professional post for recruiters  
- **`INTERVIEW EXPLANATION`** → How to explain this project clearly  

You’re doing this **the right way** — this level of care is exactly what stands out 👌