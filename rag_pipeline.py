# rag_pipeline.py

from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings
from typing import List

VECTOR_PATH = "vectorstore"

# Simple embedding class to avoid heavy dependencies
class SimpleEmbeddings(Embeddings):
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        import hashlib
        embeddings = []
        for text in texts:
            # Create a simple deterministic embedding from text hash
            hash_obj = hashlib.md5(text.encode())
            hash_val = int(hash_obj.hexdigest(), 16)
            # Generate a fixed-size embedding
            embedding = []
            for i in range(384):
                embedding.append(float((hash_val >> i) & 1) * 2 - 1)
            embeddings.append(embedding)
        return embeddings
    
    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]

embeddings = SimpleEmbeddings()

# Load vectorstore
vectorstore = FAISS.load_local(VECTOR_PATH, embeddings, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

def medical_guardrails(query):
    restricted_keywords = ["suicide", "self harm", "overdose"]
    for word in restricted_keywords:
        if word in query.lower():
            return "⚠️ If you are experiencing a medical emergency, please contact local emergency services immediately."
    return None

def generate_answer(query):
    # Guardrail check
    safety = medical_guardrails(query)
    if safety:
        return safety

    docs = retriever.invoke(query)
    
    if not docs:
        return "I couldn't find relevant information about your query. Please ask about common health conditions like cold, diabetes, asthma, heart disease, etc."

    context = "\n\n".join([doc.page_content for doc in docs])

    answer = f"""Based on the medical information database:

{context}"""

    disclaimer = "\n\n⚠️ This information is for educational purposes only and does not replace professional medical advice. Always consult with a healthcare provider for proper diagnosis and treatment."

    return answer + disclaimer
