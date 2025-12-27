import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader

FILE_TOPIC_MAP = {
    "aadhaar": "aadhaar",
    "aadhar": "aadhaar",

    "pancard": "pancard",
    "pan": "pancard",

    "voterid": "voterid",

    "firprocedure": "firprocedure",

    "consumerrights": "consumerrights",

    "tenantrights": "tenantrights"
}

VALID_TOPICS = {
    "aadhaar": "aadhaar",
    "aadhar": "aadhaar",
    "uidai": "aadhaar",

    "pan": "pancard",
    "pancard": "pancard",
    "permanent account": "pancard",

    "voter": "voterid",
    "election": "voterid",

    "fir": "firprocedure",
    "police": "firprocedure",

    "consumer": "consumerrights",
    "tenant": "tenantrights",
    "rent": "tenantrights"
}

def normalize_filename(name: str) -> str:
    return (
        name.lower()
        .replace(".txt", "")
        .replace("_", "")
        .replace(" ", "")
    )

# 1️ Load all .txt files from data folder
def load_documents():
    documents = []

    base_path = "data"
    for folder in ["govt_docs", "legal_docs"]:
        folder_path = os.path.join(base_path, folder)

        for file in os.listdir(folder_path):
            if not file.endswith(".txt"):
                continue

            filename = normalize_filename(file)
            topic = FILE_TOPIC_MAP.get(filename)
            
            if not topic:
                continue  

            file_path = os.path.join(folder_path, file)
            loader = TextLoader(file_path, encoding="utf-8")
            loaded_docs = loader.load()

            for doc in loaded_docs:
                doc.metadata = {
                    "topic": topic,
                    "source": folder
                }

            documents.extend(loaded_docs)
            
    
    for d in documents:
     print(d.metadata)

    return documents



# 2️ Split text into smaller chunks
def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)


# 3️ Create vector store (FAISS)
def create_vector_store():
    documents = load_documents()
    split_docs = split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(split_docs, embeddings)
    return vector_store


# 4️ Retrieve relevant content for a query
def retrieve_context(query: str):
    vector_store = create_vector_store()
    topic = detect_topic(query)
    
    
    
    if not topic:
        return ""

    results = vector_store.similarity_search(query, k=1, filter={"topic": topic})

    
    if not results:
        return ""
    
    doc = results[0]
    
    context = f"""
TOPIC: {topic.upper()}

CONTENT:
{doc.page_content}
"""
    return context


# 5  Detect topic
def detect_topic(query: str):
    query = query.lower()
    for keyword, topic in VALID_TOPICS.items():
        if keyword in query:
            return topic
    return None
