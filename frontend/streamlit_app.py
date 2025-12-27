import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

# ---------------- SESSION STATE ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "is_loading" not in st.session_state:
    st.session_state.is_loading = False

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Legal & Govt Assistant",
    page_icon="⚖️",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Settings")

theme_mode = st.sidebar.toggle("🌗 Dark Mode", value=True)

topic_hint = st.sidebar.selectbox(
    "🎯 Topic (optional)",
    [
        "Auto Detect",
        "Aadhaar",
        "PAN Card",
        "Voter ID",
        "FIR / Police",
        "Consumer Rights",
        "Tenant Rights"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "ℹ️ **Public awareness only**\n\n"
    "- ❌ No legal advice\n"
    "- ❌ No predictions\n"
    "- ✅ Official information"
)

# ---------------- THEME + ANIMATIONS ----------------
if theme_mode:
    # DARK MODE
    st.markdown("""
    <style>
    .stApp {
        background-color: #020617;
        color: #e5e7eb;
    }
    .block-container {
        background-color: #020617;
    }
    </style>
    """, unsafe_allow_html=True)

else:
    # LIGHT MODE
    st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc;
        color: #020617;
    }
    .block-container {
        background-color: #f8fafc;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<style>
@keyframes glowMove {
  0% { box-shadow: 0 0 15px #22d3ee; }
  50% { box-shadow: 0 0 35px #6366f1; }
  100% { box-shadow: 0 0 15px #ec4899; }
}

.title-card {
  background: linear-gradient(270deg, #22d3ee, #6366f1, #ec4899);
  background-size: 400% 400%;
  animation: gradientMove 8s ease infinite, glowMove 4s ease-in-out infinite;
  padding: 2rem;
  border-radius: 22px;
  color: white;
  font-size: 2rem;
  font-weight: 800;
  text-align: center;
  margin-bottom: 1.5rem;
  letter-spacing: 0.5px;
}
.subtitle {
  font-size: 0.9rem;
  opacity: 0.9;
  margin-top: 0.4rem;
}
</style>

<div class="title-card">
  ⚖️ AI Legal & Government Awareness Assistant
  <div class="subtitle">
    RAG-powered • Local LLM • Safe & Accurate
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------- CHAT HISTORY ----------------
for chat in st.session_state.chat_history:
    st.markdown(f"""
    <div class="chat-box user">
        <b>You:</b> {chat["question"]}
    </div>
    <div class="chat-box ai">
        <span class="badge {chat["badge"]}">{chat["topic"]}</span><br>
        {chat["answer"]}
        <div class="disclaimer">{chat["disclaimer"]}</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- INPUT ----------------
question = st.text_input(
    "",
    placeholder="Ask about Aadhaar, PAN, FIR, Tenant rights..."
)

ask_btn = st.button("🚀 Ask", disabled=st.session_state.is_loading)

# ---------------- API CALL ----------------
if ask_btn and question.strip() and not st.session_state.is_loading:
    st.session_state.is_loading = True

    with st.spinner("Thinking..."):
        try:
            res = requests.post(
                API_URL,
                json={"question": question},
                timeout=120
            )

            if res.status_code == 200:
                data = res.json()
                topic = data.get("topic", "General")

                badge_map = {
                    "aadhaar": "aadhaar",
                    "pancard": "pan",
                    "voterid": "voter",
                    "firprocedure": "fir",
                    "consumerrights": "consumer",
                    "tenantrights": "tenant"
                }

                st.session_state.chat_history.append({
                    "question": question,
                    "answer": data.get("answer", ""),
                    "topic": topic.upper(),
                    "badge": badge_map.get(topic, "aadhaar"),
                    "disclaimer": data.get("disclaimer", "")
                })
            else:
                st.error("Backend error. Please try again.")

        except Exception:
            st.error("Backend is starting. Please wait a moment.")

        finally:
            st.session_state.is_loading = False
            st.rerun()

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<center>⚠️ Public awareness only. Verify with official authorities.</center>",
    unsafe_allow_html=True
)
